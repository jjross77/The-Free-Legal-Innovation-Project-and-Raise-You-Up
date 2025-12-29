# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:24:14 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import copy
import torch
from .bert import *
import copy
import torch
from torch import nn
from collections import Sequence
from packaging import version
import numpy as np
import math
import os
import pdb

from .cache_utils import load_model_state

class BertEmbeddings(nn.Module):
  """Construct the embeddings from word, position and token_type embeddings.
  """
  def __init__(self, config):
    super(BertEmbeddings, self).__init__()
    padding_idx = getattr(config, 'padding_idx', 0)
    self.embedding_size = getattr(config, 'embedding_size', config.hidden_size)
    self.word_embeddings = nn.Embedding(config.vocab_size, self.embedding_size, padding_idx = padding_idx)
    self.position_biased_input = getattr(config, 'position_biased_input', True)
    self.position_embeddings = nn.Embedding(config.max_position_embeddings, self.embedding_size)

    if config.type_vocab_size>0:
      self.token_type_embeddings = nn.Embedding(config.type_vocab_size, self.embedding_size)
    
    if self.embedding_size != config.hidden_size:
      self.embed_proj = nn.Linear(self.embedding_size, config.hidden_size, bias=False)
    self.LayerNorm = LayerNorm(config.hidden_size, config.layer_norm_eps)
    self.dropout = StableDropout(config.hidden_dropout_prob)
    self.output_to_half = False
    self.config = config

  def forward(self, input_ids, token_type_ids=None, position_ids=None, mask = None):
    seq_length = input_ids.size(1)
    if position_ids is None:
      position_ids = torch.arange(0, seq_length, dtype=torch.long, device=input_ids.device)
      position_ids = position_ids.unsqueeze(0).expand_as(input_ids)
    if token_type_ids is None:
      token_type_ids = torch.zeros_like(input_ids)

    words_embeddings = self.word_embeddings(input_ids)
    position_embeddings = self.position_embeddings(position_ids.long())

    embeddings = words_embeddings
    if self.config.type_vocab_size>0:
      token_type_embeddings = self.token_type_embeddings(token_type_ids)
      embeddings += token_type_embeddings

    if self.position_biased_input:
      embeddings += position_embeddings

    if self.embedding_size != self.config.hidden_size:
      embeddings = self.embed_proj(embeddings)
    embeddings = MaskedLayerNorm(self.LayerNorm, embeddings, mask)
    embeddings = self.dropout(embeddings)
    return {
        'embeddings': embeddings,
        'position_embeddings': position_embeddings}



class BertEncoder(nn.Module):
  """ Modified BertEncoder with relative position bias support
  """
  def __init__(self, config):
    super().__init__()
    #layer = BertLayer(config)
    self.layer = nn.ModuleList([BertLayer(config) for _ in range(config.num_hidden_layers)])
    self.relative_attention = getattr(config, 'relative_attention', False)
    if self.relative_attention:
      self.max_relative_positions = getattr(config, 'max_relative_positions', -1)
      if self.max_relative_positions <1:
        self.max_relative_positions = config.max_position_embeddings
      self.position_buckets = getattr(config, 'position_buckets', -1)
      pos_ebd_size = self.max_relative_positions*2
      if self.position_buckets>0:
        pos_ebd_size = self.position_buckets*2
      self.rel_embeddings = nn.Embedding(pos_ebd_size, config.hidden_size)

    self.norm_rel_ebd = [x.strip() for x in getattr(config, 'norm_rel_ebd', 'none').lower().split('|')]
    if 'layer_norm' in self.norm_rel_ebd:
      self.LayerNorm = LayerNorm(config.hidden_size, config.layer_norm_eps, elementwise_affine = True)
    kernel_size = getattr(config, 'conv_kernel_size', 0)
    self.with_conv = False
    if kernel_size > 0:
      self.with_conv = True
      self.conv = ConvLayer(config)

  def get_rel_embedding(self):
    rel_embeddings = self.rel_embeddings.weight if self.relative_attention else None
    if rel_embeddings is not None and ('layer_norm' in self.norm_rel_ebd):
      rel_embeddings = self.LayerNorm(rel_embeddings)
    return rel_embeddings

  def get_attention_mask(self, attention_mask):
    if attention_mask.dim()<=2:
      extended_attention_mask = attention_mask.unsqueeze(1).unsqueeze(2)
      attention_mask = extended_attention_mask*extended_attention_mask.squeeze(-2).unsqueeze(-1)
      attention_mask = attention_mask.byte()
    elif attention_mask.dim()==3:
      attention_mask = attention_mask.unsqueeze(1)

    return attention_mask

  def get_rel_pos(self, hidden_states, query_states=None, relative_pos=None):
    if self.relative_attention and relative_pos is None:
      q = query_states.size(-2) if query_states is not None else hidden_states.size(-2)
      relative_pos = build_relative_position(q, hidden_states.size(-2), bucket_size = self.position_buckets, max_position=self.max_relative_positions)
    return relative_pos

  def forward(self, hidden_states, attention_mask, output_all_encoded_layers=True, return_att=False, query_states = None, relative_pos=None):
    if attention_mask.dim()<=2:
      input_mask = attention_mask
    else:
      input_mask = (attention_mask.sum(-2)>0).byte()
    attention_mask = self.get_attention_mask(attention_mask)
    relative_pos = self.get_rel_pos(hidden_states, query_states, relative_pos)

    all_encoder_layers = []
    att_matrices = []
    if isinstance(hidden_states, Sequence):
      next_kv = hidden_states[0]
    else:
      next_kv = hidden_states
    rel_embeddings = self.get_rel_embedding()
    for i, layer_module in enumerate(self.layer):
      output_states = layer_module(next_kv, attention_mask, return_att, query_states = query_states, relative_pos=relative_pos, rel_embeddings=rel_embeddings)
      if return_att:
        output_states, att_m = output_states

      if i == 0 and self.with_conv:
        prenorm = output_states #output['prenorm_states']
        output_states = self.conv(hidden_states, prenorm, input_mask)

      if query_states is not None:
        query_states = output_states
        if isinstance(hidden_states, Sequence):
          next_kv = hidden_states[i+1] if i+1 < len(self.layer) else None
      else:
        next_kv = output_states

      if output_all_encoded_layers:
        all_encoder_layers.append(output_states)
        if return_att:
          att_matrices.append(att_m)
    if not output_all_encoded_layers:
      all_encoder_layers.append(output_states)
      if return_att:
        att_matrices.append(att_m)
    return {
        'hidden_states': all_encoder_layers,
        'attention_matrices': att_matrices
        }






__all__ = ['DeBERTa']

class DeBERTa(torch.nn.Module):
  """ DeBERTa encoder
  This module is composed of the input embedding layer with stacked transformer layers with disentangled attention.
  Parameters:
    config:
      A model config class instance with the configuration to build a new model. The schema is similar to `BertConfig`, \
          for more details, please refer :class:`~DeBERTa.deberta.ModelConfig`
    pre_trained:
      The pre-trained DeBERTa model, it can be a physical path of a pre-trained DeBERTa model or a released configurations, \
          i.e. [**base, large, base_mnli, large_mnli**]
  """

  def __init__(self, config=None, pre_trained=None):
    super().__init__()
    state = None
    if pre_trained is not None:
      state, model_config = load_model_state(pre_trained)
      if config is not None and model_config is not None:
        for k in config.__dict__:
          if k not in ['hidden_size',
            'intermediate_size',
            'num_attention_heads',
            'num_hidden_layers',
            'vocab_size',
            'max_position_embeddings']:
            model_config.__dict__[k] = config.__dict__[k]
      config = copy.copy(model_config)
    self.embeddings = BertEmbeddings(config)
    self.encoder = BertEncoder(config)
    self.config = config
    self.pre_trained = pre_trained
    self.apply_state(state)

  def forward(self, input_ids, attention_mask=None, token_type_ids=None, output_all_encoded_layers=True, position_ids = None, return_att = False):
    """
    Args:
      input_ids:
        a torch.LongTensor of shape [batch_size, sequence_length] \
      with the word token indices in the vocabulary
      attention_mask:
        an optional parameter for input mask or attention mask.
        - If it's an input mask, then it will be torch.LongTensor of shape [batch_size, sequence_length] with indices \
      selected in [0, 1]. It's a mask to be used if the input sequence length is smaller than the max \
      input sequence length in the current batch. It's the mask that we typically use for attention when \
      a batch has varying length sentences.
        - If it's an attention mask then it will be torch.LongTensor of shape [batch_size, sequence_length, sequence_length]. \
      In this case, it's a mask indicate which tokens in the sequence should be attended by other tokens in the sequence.
      token_type_ids:
        an optional torch.LongTensor of shape [batch_size, sequence_length] with the token \
      types indices selected in [0, 1]. Type 0 corresponds to a `sentence A` and type 1 corresponds to \
      a `sentence B` token (see BERT paper for more details).
      output_all_encoded_layers:
        whether to output results of all encoder layers, default, True
    Returns:
      - The output of the stacked transformer layers if `output_all_encoded_layers=True`, else \
      the last layer of stacked transformer layers
      - Attention matrix of self-attention layers if `return_att=True`
    Example::
      # Batch of wordPiece token ids.
      # Each sample was padded with zero to the maxium length of the batch
      input_ids = torch.LongTensor([[31, 51, 99], [15, 5, 0]])
      # Mask of valid input ids
      attention_mask = torch.LongTensor([[1, 1, 1], [1, 1, 0]])
      # DeBERTa model initialized with pretrained base model
      bert = DeBERTa(pre_trained='base')
      encoder_layers = bert(input_ids, attention_mask=attention_mask)
    """

    if attention_mask is None:
      attention_mask = torch.ones_like(input_ids)
    if token_type_ids is None:
      token_type_ids = torch.zeros_like(input_ids)

    ebd_output = self.embeddings(input_ids.to(torch.long), token_type_ids.to(torch.long), position_ids, attention_mask)
    embedding_output = ebd_output['embeddings']
    encoder_output = self.encoder(embedding_output,
                   attention_mask,
                   output_all_encoded_layers=output_all_encoded_layers, return_att = return_att)
    encoder_output.update(ebd_output)
    return encoder_output

  def apply_state(self, state = None):
    """ Load state from previous loaded model state dictionary.
      Args:
        state (:obj:`dict`, optional): State dictionary as the state returned by torch.module.state_dict(), default: `None`. \
            If it's `None`, then will use the pre-trained state loaded via the constructor to re-initialize \
            the `DeBERTa` model
    """
    if self.pre_trained is None and state is None:
      return
    if state is None:
      state, config = load_model_state(self.pre_trained)
      self.config = config
    
    prefix = ''
    for k in state:
      if 'embeddings.' in k:
        if not k.startswith('embeddings.'):
          prefix = k[:k.index('embeddings.')]
        break

    missing_keys = []
    unexpected_keys = []
    error_msgs = []
    self._load_from_state_dict(state, prefix = prefix, local_metadata=None, strict=True, missing_keys=missing_keys, unexpected_keys=unexpected_keys, error_msgs=error_msgs)