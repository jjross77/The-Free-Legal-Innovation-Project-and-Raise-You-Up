# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:18:58 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from torch.nn import CosineSimilarity
from torch import mean
from pipe_line_to_process_documents3 import document_FIRAC_labeler
import json
import torch
#import torch
docf=document_FIRAC_labeler()
dog=docf.upload_embeddings_from_case_database("embedding_sentences", "%reichman%")
dog2 =docf.upload_embeddings_from_case_database("embedding_sentences", "%T.H. v T.A.%")


doc_1=docf.transform_to_pos_format(dog)
doc_2=docf.transform_to_pos_format(dog2)
#doc_4=[[1],[2]]
#doc_1[0]=doc_1[0][715:725]
#doc_1[1]=doc_1[1][715:725]
#woo=doc_1[0][0][2]
#woo2=doc_2[0][0][2]
#print(torch.matmul(woo,woo2.T))
print('meow')

verb_dog=docf.cosine_sim_matrix_dot(doc_1,doc_2,noun_or_verb=1)
noun_dog=docf.cosine_sim_matrix_dot(doc_1,doc_2,noun_or_verb=0)
print('woo')

ultimate_dog=docf.combine_verb_and_noun_cosines(noun_dog,verb_dog)

highest_matches=docf.find_best_matching_doc_sentences(ultimate_dog)

docf.save_cosine_simialrities_in_firac_labels(highest_matches)

#selects the dot products that coresspond to a1 or the first vector of the first matrix
#doc_5=[[1],[2]]
#doc_5[0]=doc_1[0][450:470]
#doc_5[1]=doc_1[1][450:470]

#doc_4[0]=doc_1[0][450:470]
#doc_4[1]=doc_1[1][450:470]


#save max of eahc sentence

#ultimate_dog=docf.cosine_simairlity_pos_embeddings(doc_1,doc_2)
#review1=docf.noun_dic_comparison_word
#review2=docf.verb_dic_comparison_word
#high correlation with a bunch of sentences may be an idea
#937:37
#519:463
#634:29
# can only use a word once when doing the comparisons max one
# so we will take the second best result or third best result of the matches so we don't reuse words
# choose which word to use based upon  highest correlation score with other word in the sentence 
#715:71

#745.9832000732422
#[['He', 'I', 689.1912231445312], ['He', 'Ġhome', 514.3927001953125], ['He', 'lord', 456.2782287597656], ['He', 'Ļ', 410.4534912109375], ['He', 'Ġson', 579.78857421875], ['He', 'Ġname', 464.5901184082031], ['He', 'Ġhe', 742.1282958984375], ['He', 'Ġjob', 495.2228088378906], ['He', 'Ġemoji', 505.54425048828125], ['He', 'Ġtenant', 551.90771484375], ['He', 'Ġthey', 746.0551147460938], ['He', 'Ġreason', 562.4185180664062], ['He', 'Ġtenancy', 445.1850891113281], ['He', 'Ġexped', 375.1872863769531], ['He', 'Ġmanner', 529.6392822265625], ['He', 'cause', 599.302734375], ['Ġright', 'I', 426.135986328125], ['Ġright', 'Ġhome', 415.5062255859375], ['Ġright', 'lord', 350.71783447265625], ['Ġright', 'Ļ', 339.5648193359375], ['Ġright', 'Ġson', 419.85992431640625], ['Ġright', 'Ġname', 361.7732238769531], ['Ġright', 'Ġhe', 449.387939453125], ['Ġright', 'Ġjob', 395.9875793457031], ['Ġright', 'Ġemoji', 354.6074523925781], ['Ġright', 'Ġtenant', 408.74493408203125], ['Ġright', 'Ġthey', 487.87725830078125], ['Ġright', 'Ġreason', 581.4933471679688], ['Ġright', 'Ġtenancy', 383.6141357421875], ['Ġright', 'Ġexped', 338.1720275878906], ['Ġright', 'Ġmanner', 451.4642028808594], ['Ġright', 'cause', 405.0552062988281], ['Ġarbit', 'I', 244.0749969482422], ['Ġarbit', 'Ġhome', 267.51220703125], ['Ġarbit', 'lord', 277.3008117675781], ['Ġarbit', 'Ļ', 239.0989990234375], ['Ġarbit', 'Ġson', 306.667236328125], ['Ġarbit', 'Ġname', 239.35035705566406], ['Ġarbit', 'Ġhe', 266.3668212890625], ['Ġarbit', 'Ġjob', 245.9192657470703], ['Ġarbit', 'Ġemoji', 264.2555236816406], ['Ġarbit', 'Ġtenant', 310.17388916015625], ['Ġarbit', 'Ġthey', 308.73529052734375], ['Ġarbit', 'Ġreason', 282.57147216796875], ['Ġarbit', 'Ġtenancy', 314.5617980957031], ['Ġarbit', 'Ġexped', 336.61212158203125], ['Ġarbit', 'Ġmanner', 287.1024475097656], ['Ġarbit', 'cause', 272.9897766113281], ['Ġissue', 'I', 451.9914245605469], ['Ġissue', 'Ġhome', 438.2903747558594], ['Ġissue', 'lord', 397.6524658203125], ['Ġissue', 'Ļ', 337.8155517578125], ['Ġissue', 'Ġson', 456.8918762207031], ['Ġissue', 'Ġname', 401.8622131347656], ['Ġissue', 'Ġhe', 477.577880859375], ['Ġissue', 'Ġjob', 420.55682373046875], ['Ġissue', 'Ġemoji', 416.5854797363281], ['Ġissue', 'Ġtenant', 493.1911926269531], ['Ġissue', 'Ġthey', 510.59033203125], ['Ġissue', 'Ġreason', 487.650390625], ['Ġissue', 'Ġtenancy', 479.51617431640625], ['Ġissue', 'Ġexped', 341.5966491699219], ['Ġissue', 'Ġmanner', 485.2857666015625], ['Ġissue', 'cause', 479.9287414550781], ['ĠProject', 'I', 376.731201171875], ['ĠProject', 'Ġhome', 354.4668273925781], ['ĠProject', 'lord', 393.2095947265625], ['ĠProject', 'Ļ', 315.4139404296875], ['ĠProject', 'Ġson', 381.93780517578125], ['ĠProject', 'Ġname', 330.19873046875], ['ĠProject', 'Ġhe', 410.85980224609375], ['ĠProject', 'Ġjob', 349.9138488769531], ['ĠProject', 'Ġemoji', 353.7964172363281], ['ĠProject', 'Ġtenant', 404.281005859375], ['ĠProject', 'Ġthey', 446.12799072265625], ['ĠProject', 'Ġreason', 401.9864196777344], ['ĠProject', 'Ġtenancy', 394.35107421875], ['ĠProject', 'Ġexped', 299.96319580078125], ['ĠProject', 'Ġmanner', 377.9923400878906], ['ĠProject', 'cause', 430.4271545410156], ['ĠAgreement', 'I', 374.70751953125], ['ĠAgreement', 'Ġhome', 366.91461181640625], ['ĠAgreement', 'lord', 389.0615539550781], ['ĠAgreement', 'Ļ', 308.4270324707031], ['ĠAgreement', 'Ġson', 396.95916748046875], ['ĠAgreement', 'Ġname', 357.190185546875], ['ĠAgreement', 'Ġhe', 393.9308776855469], ['ĠAgreement', 'Ġjob', 363.6365966796875], ['ĠAgreement', 'Ġemoji', 386.95654296875], ['ĠAgreement', 'Ġtenant', 410.53814697265625], ['ĠAgreement', 'Ġthey', 432.9520263671875], ['ĠAgreement', 'Ġreason', 408.0133056640625], ['ĠAgreement', 'Ġtenancy', 435.7119140625], ['ĠAgreement', 'Ġexped', 304.1399230957031], ['ĠAgreement', 'Ġmanner', 433.0145263671875], ['ĠAgreement', 'cause', 418.41937255859375]]
#0.824278861284256


# 201:63
# only do sentences that have both a noun and a verb
#print(woo)
# short and uses pronouns
# if two things are short and use this is problem