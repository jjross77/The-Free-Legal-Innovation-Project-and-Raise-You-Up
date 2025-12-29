# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 07:21:20 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

from transformers import DistilBertTokenizerFast
from transformers import DistilBertModel
#from transformers import Trainer, TrainingArguments
#dog=Trainer()
import re
import torch
import pickle
finding_start_of_second_sentence=re.compile(r"1")

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased", truncation_side="left")
model = DistilBertModel.from_pretrained("distilbert-base-uncased").to("cuda")
existing_sentences= ", c. 12, s. 186. In 2018, Parliament enacted the Greenhouse Gas Pollution Pricing Act (“GGPPA”). The GGPPA comprises four parts and four schedules. Part 1 establishes a fuel charge that applies to producers, distributors and importers of various types of carbon-based fuel. Part 2 sets out a pricing mechanism for industrial greenhouse gas (“GHG”) emissions by large emissions-intensive industrial facilities. Part 3 authorizes the Governor in Council to make regulations providing for the application of provincial law concerning GHG emissions to federal works and undertakings, federal land and Indigenous land located in that province, as well as to internal waters located in or contiguous with the province. Part 4 requires the Minister of the Environment to prepare an annual report on the administration of the GGPPA and have it tabled in Parliament. Saskatchewan, Ontario and Alberta challenged the constitutionality of the first two parts and the four schedules of the GGPPA by references to their respective courts of appeal, asking whether the GGPPA is unconstitutional in whole or in part. In split decisions, the courts of appeal for Saskatchewan and Ontario held that the GGPPA is constitutional, while the Court of Appeal of Alberta held that it is unconstitutional. The Attorney General of British Columbia, who had intervened in the Court of Appeal of Alberta, the Attorney General of Saskatchewan and the Attorney General of Ontario now appeal as of right to the Court. Held (Côté J. dissenting in part and Brown and Rowe JJ. dissenting): The appeals by the Attorney General of Saskatchewan and the Attorney General of Ontario should be dismissed, and the appeal by the Attorney General of British Columbia should be allowed. The reference questions are answered in the negative. Per Wagner C.J. and Abella, Moldaver, Karakatsanis, Martin and Kasirer JJ. : The GGPPA is constitutional. It sets minimum national standards of GHG price stringency to reduce GHG emissions. Parliament has jurisdiction to enact this law as a matter of national concern under the peace, order, and good government (“POGG”) clause of s. 91 of the Constitution Act, 1867. Federalism is a foundational principle of the Canadian Constitution. Its objectives are to reconcile diversity with unity, promote democratic participation by reserving meaningful powers to the local and regional level and foster cooperation between Parliament and the provincial legislatures for the common good. Sections 91 and 92 of the Constitution give expression to the principle of federalism and divide legislative powers between Parliament and the provincial legislatures. Under the division of powers, broad powers were conferred on the provinces to ensure diversity, while at the same time reserving to the federal government powers better exercised in relation to the country as a whole to provide for Canada’s unity. Federalism recognizes that within their spheres of jurisdiction, provinces have autonomy to develop their societies. Federal power cannot be used in a manner that effectively eviscerates provincial power. Courts, as impartial arbiters, are charged with resolving jurisdictional disputes over the boundaries of federal and provincial powers on the basis of the principle of federalism. Although early Canadian constitutional decisions by the Judicial Committee of the Privy Council applied a rigid division of federal-provincial powers as watertight compartments, the Court has favoured a flexible view of federalism, best described as a modern cooperative federalism, that accommodates and encourages intergovernmental cooperative efforts. However, the Court has also always maintained that flexibility and cooperation, while important, cannot override or modify federalism and the constitutional division of powers."
sentence_2= "The review of legislation on federalism grounds consists of the well-established two-stage analytical approach."
#inputs = tokenizer(existing_sentences,sentence_2, return_tensors="pt", truncation=True, return_token_type_ids=True)
inputs = tokenizer(existing_sentences,sentence_2, return_tensors="pt", truncation=True, return_token_type_ids=True)


strwoo=(str((inputs['token_type_ids'])))
tokens_in_current_sentence= re.findall(finding_start_of_second_sentence, string=strwoo)
amount_of_tokens=len(tokens_in_current_sentence)  # for final token that will be labeled as 
#a 1 still need to remove this or find a way to remove the final token
# I think I did manage to do this in the end
#inputs = tokenizer(sentence_2, return_tensors="pt", truncation=True).to("cuda")
print(inputs[1])
#print(inputs)

#output = model(**inputs)

#embedding_with_extra_end_token=output[0][0][-amount_of_tokens:]
#good_embeddings= embedding_with_extra_end_token[:-1]

#sentence_embedding= torch.mean(good_embeddings, dim=0)# need to test this seems fine
#dog2=sentence_embedding
#with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\embedding_list_distilbert.pickle","rb") as ff:
#    original_case_dict=pickle.load(ff)
#dude=original_case_dict['1: 4: The review of legislation on federalism grounds consists of the well-established two-stage analytical approach.']
#dog=dude
#print(dog)
#print(dog2)
#print(sentence_2.encode("utf-8"))

#tokenized_datasets = dataset.map(tokenize_function, batched=True)