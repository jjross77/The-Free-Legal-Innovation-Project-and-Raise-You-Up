# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:50:55 2023

@author: rossg
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained('cross-encoder/nli-deberta-v3-base')
tokenizer = AutoTokenizer.from_pretrained('cross-encoder/nli-deberta-v3-base')
sen1 ="In 2018, Parliament enacted the Greenhouse Gas Pollution Pricing Act (“GGPPA”)."
sen2 ="The GGPPA comprises four parts and four schedules."
sen3= "Part 1 establishes a fuel charge that applies to producers, distributors and importers of various types of carbon-based fuel."
sen4= "Part 2 sets out a pricing mechanism for industrial greenhouse gas (“GHG”) emissions by large emissions-intensive industrial facilities."
sen5= "Part 3 authorizes the Governor in Council to make regulations providing for the application of provincial law concerning GHG emissions to federal works and undertakings, federal land and Indigenous land located in that province, as well as to internal waters located in or contiguous with the province."
sen6= "Part 4 requires the Minister of the Environment to prepare an annual report on the administration of the GGPPA and have it tabled in Parliament."
features = tokenizer(['A man is eating pizza', 'A black race car starts up in front of a crowd of people.'], ['A man eats something', 'A man is driving down a lonely road.'],  padding=True, truncation=True, return_tensors="pt")

model.eval()
with torch.no_grad():
    scores = model(**features).logits
    label_mapping = ['contradiction', 'entailment', 'neutral']
    labels = [label_mapping[score_max] for score_max in scores.argmax(dim=1)]
    print(labels)