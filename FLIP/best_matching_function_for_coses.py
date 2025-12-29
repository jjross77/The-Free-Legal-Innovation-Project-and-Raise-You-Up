# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:39:05 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
dog={"1:12":[[517.9185791015625, 629.2070922851562], ['STRUCT', 'ered', 'ARD'], ['ĠIss', 'ued'], 'Reichmann v. Vered, 2003 CanLII 49295 (ON SC)', 'T.H. v T.A., 2022 YTRTO 22 (CanLII)'], "1:13":[[300.6091003417969, 511.163330078125, 542.1610107421875, 488.1941833496094, 545.9029541015625, 492.4716491699219], ['STRUCT', 'ered', 'ARD'], ['Ġdated', 'Ġappeared', 'Ġsuggest', 'Ġreceive', 'Ġstated', 'Ġforwarded'], 'Reichmann v. Vered, 2003 CanLII 49295 (ON SC)', 'T.H. v T.A., 2022 YTRTO 22 (CanLII)']}
def find_best_matching_doc_sentences(noun_cosines):
     import re
     seen_num_dic={}
     
     for key, value in noun_cosines.items():
         key=str(key)
         first_sentence_num=re.search(r"(\d+):",key).group(1)
         print(first_sentence_num)
         if seen_num_dic.get(first_sentence_num):
             seen_num_dic[first_sentence_num].append(value[5])
             continue
         print(value[5])
         seen_num_dic[first_sentence_num]=[value[5]]
         
     #for keyy, valuee in seen_num_dic.items():
         #seen_num_dic[keyy]=valuee.sort()
     return seen_num_dic
 
find_best_matching_doc_sentences(dog)
         