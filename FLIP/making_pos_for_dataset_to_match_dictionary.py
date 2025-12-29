# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 01:17:34 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""


""" This Program parses Sentences using SPACY into Subject Object and Verb Parts"""

#import spacy
#nlp = spacy.load("en_core_web_sm")

import en_core_web_sm
import copy
import re
import pickle
from openpyxl import load_workbook


def Convert_To_Good_Lists(sentence_chunk_list, sentence_chunk_final2):
    """ remove repeats from each list"""
    previous_temp_list = []
    previous_value_temp_list = []
    
    for ii, obj1 in enumerate(sentence_chunk_list):
        temp_list = []
        for obj2 in obj1:
            obj3=obj2[2]
            temp_list.append(obj3)
        if ii > 0:
            print(previous_value_temp_list[0])
            checking_for_repeats = any(obj4 in temp_list for obj4 in previous_temp_list[0])
            if checking_for_repeats is True:
                sentence_chunk_final2.remove(previous_value_temp_list[0])
                
                
        previous_value_temp_list.clear()        
        previous_temp_list.clear()   
        previous_temp_list.append(temp_list)
        previous_value_temp_list.append(obj1)
    return sentence_chunk_final2

nlp = en_core_web_sm.load()
path = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\Sparrow_with_dic_for_showcase.xlsx"

wb = load_workbook(filename=path)
sheet = wb.active

sentence_list = []


with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\numpy_dict_of_embeddings.pickle","rb") as ff:
    original_case_dict=pickle.load(ff)
    
pattern_for_labels= re.compile(r'(\d+): (\d+): (\d+): (.*)') # group 2 is label 2 group 1 is label 1 group 4 is sentence


for key, value in original_case_dict.items():
    keyy=str(key)
    label_regex_obj=pattern_for_labels.search(keyy)
    sentence_group =label_regex_obj.group(4)
    sentence_group = re.sub(' +', ' ', sentence_group)

    sentence_list.append(sentence_group)
    
for iiii, sentence1 in enumerate(sentence_list):
    
    
    sentence = nlp(sentence1)
    sentence_len=len(sentence)
    final_value_index= sentence_len-1
    
    
    subject_dic = {}
    object_dic = {}
    verb_dic_total = {}
    subject_list_final = []
    object_list_final = []
    verb_list_final = []
    sentence_list2 = []


    counterr_subject = 0
    counterr_object = 0
    counterr_total = 0

    subject_dic.clear()
    object_dic.clear()
    verb_dic_total.clear()
    sentence_list2.clear()
    
    for i,  part_of_speech_parts in enumerate(sentence):
            
        value_to_slide_window_sub = 0
        value_to_slide_window_verb = 0
        value_to_slide_window_obj = 0
        value_to_slide_window_obj2 = 0
        return_value_sub = "found"
        return_value_verb = "found"
        return_value_obj = "found"
        
        
        
        
        if i == 0:
            subject_dic[counterr_subject] = []
            object_dic[counterr_object] = []
            verb_dic_total[counterr_total] = []

        if len(subject_dic) > counterr_subject:
            counterr_subject+= 1
            subject_dic[counterr_subject] = []
            
        if len(object_dic) > counterr_object:
            counterr_object+= 1
            object_dic[counterr_object] = []
            
        if len(verb_dic_total) > counterr_total:
            counterr_total+= 1
            verb_dic_total[counterr_total] = []
            
        #print(type(part_of_speech_parts.pos_))
        
        if part_of_speech_parts.pos_ == "AUX":
            verb_dic_total[counterr_total].append([part_of_speech_parts.text, part_of_speech_parts.pos_, i])
            print(final_value_index)
            print(i)
            if final_value_index > i : # need to figure this out
                if sentence[i+1].pos_ == "AUX" or sentence[i+1].pos_ == "ADV" :
                    verb_dic_total[counterr_total].append([sentence[i+1].text, sentence[i+1].pos_, i+1])
                    
         
        
        if part_of_speech_parts.pos_ == "VERB":
            verb_dic_total[counterr_total].append([part_of_speech_parts.text, part_of_speech_parts.pos_, i])
            if sentence[i-1].pos_ == "AUX":
                verb_dic_total[counterr_total].insert(0,[sentence[i-1].text, sentence[i-1].pos_, i-1])
                
            if final_value_index > i:
                if sentence[i+1].pos_ == "ADV":
                    verb_dic_total[counterr_total].append([sentence[i+1].text, sentence[i+1].pos_, i+1])
                
            
         

        if part_of_speech_parts.pos_ == "NOUN" or part_of_speech_parts.pos_ ==  "NUM" or part_of_speech_parts.pos_ == "PROPN" or part_of_speech_parts.pos_ == "PRON":
            
            
            if i == final_value_index:
                print("hi")
                object_dic[counterr_object].append([part_of_speech_parts.text, part_of_speech_parts.pos_ , i])

                while return_value_obj=="found": 
                    value_to_slide_window_obj2 -= 1
                    if i+value_to_slide_window_obj2 > -1:
                        if sentence[i+value_to_slide_window_obj2].pos_ == "DET" or sentence[i+value_to_slide_window_obj2].pos_ == "CCONJ" or sentence[i+value_to_slide_window_obj2].pos_ == "NOUN" or sentence[i+value_to_slide_window_obj2].pos_ == "ADJ" or sentence[i+value_to_slide_window_obj2].pos_ == "PROPN" or sentence[i+value_to_slide_window_obj2].pos_ == "PRON" or sentence[i+value_to_slide_window_obj2].pos_ == "NUM" or sentence[i+value_to_slide_window_obj2].pos_ == "PART" or sentence[i+value_to_slide_window_obj2].pos_ == "ADP":
                            object_dic[counterr_object].insert(0, [sentence[i+value_to_slide_window_obj2].text, sentence[i+value_to_slide_window_obj2].pos_ , i+value_to_slide_window_obj2])
                            continue                    
                    break
                    

               
                
            if i == final_value_index:
                break
            
            
            if sentence[i+1].pos_ == "AUX" or sentence[i+1].pos_ == "VERB":
                #print(sentence[i+1].pos_)
                
                subject_dic[counterr_subject].append([part_of_speech_parts.text, part_of_speech_parts.pos_, i])
                if i > 0:
                    while return_value_sub=="found":
                        value_to_slide_window_sub-= 1
                        #print(value_to_slide_window_sub)
                        #print(i+value_to_slide_window_sub)
                        if i+value_to_slide_window_sub > -1:
                            if sentence[i+value_to_slide_window_sub].pos_ == "DET" or  sentence[i+value_to_slide_window_sub].pos_ == "NOUN" or sentence[i+value_to_slide_window_sub].pos_ == "ADJ" or sentence[i+value_to_slide_window_sub].pos_ == "PROPN" or sentence[i+value_to_slide_window_sub].pos_ == "PRON" or sentence[i+value_to_slide_window_sub].pos_ == "NUM" or sentence[i+value_to_slide_window_sub].pos_ == "PART" or sentence[i+value_to_slide_window_sub].pos_ == "ADP" or sentence[i+value_to_slide_window_sub].pos_ == "CCONJ" :
                                subject_dic[counterr_subject].insert(0,[sentence[i+value_to_slide_window_sub].text, sentence[i+value_to_slide_window_sub].pos_, i + value_to_slide_window_sub])
                                continue
                        return_value_sub = "not"
     
            else: 
                object_dic[counterr_object].append([part_of_speech_parts.text, part_of_speech_parts.pos_ , i])

                while return_value_obj =="found": 
                    
                    value_to_slide_window_obj+= 1
                    if i+value_to_slide_window_obj > final_value_index:
                        break
                        
                    if sentence[i+value_to_slide_window_obj].pos_ == "DET" or  sentence[i+value_to_slide_window_obj].pos_ == "NOUN" or sentence[i+value_to_slide_window_obj].pos_ == "ADJ" or sentence[i+value_to_slide_window_obj].pos_ == "PROPN" or sentence[i+value_to_slide_window_obj].pos_ == "PRON" or sentence[i+value_to_slide_window_obj].pos_ == "NUM" or sentence[i+value_to_slide_window_obj].pos_ == "PART" : 
                        object_dic[counterr_object].append([sentence[i+value_to_slide_window_obj].text, sentence[i+value_to_slide_window_obj].pos_ , i+value_to_slide_window_obj])
                        continue
                    return_value_obj = "not found"
                    
                return_value_obj = "found"
                if i > 0:
                    while return_value_obj=="found": 
                        value_to_slide_window_obj2 -= 1
                        if i+value_to_slide_window_obj2 > -1:
                            if sentence[i+value_to_slide_window_obj2].pos_ == "DET" or  sentence[i+value_to_slide_window_obj2].pos_ == "NOUN" or sentence[i+value_to_slide_window_obj2].pos_ == "ADJ" or sentence[i+value_to_slide_window_obj2].pos_ == "PROPN" or sentence[i+value_to_slide_window_obj2].pos_ == "PRON" or sentence[i+value_to_slide_window_obj2].pos_ == "NUM" or sentence[i+value_to_slide_window_obj2].pos_ == "PART" or sentence[i+value_to_slide_window_obj2].pos_ == "ADP" or sentence[i+value_to_slide_window_sub].pos_ == "CCONJ":
                                object_dic[counterr_object].insert(0, [sentence[i+value_to_slide_window_obj2].text, sentence[i+value_to_slide_window_obj2].pos_ , i+value_to_slide_window_obj2])
                                continue                    
                        return_value_obj = "not found"
    #cleaning dicitonaries

    [sentence_list2.append([word.text, word.pos_ , i]) for i, word in enumerate(sentence)]


    for sub, obj, ver in zip(subject_dic.values(), object_dic.values(), verb_dic_total.values()):
        if sub:
            subject_list_final.append(sub)       
        if obj:
            object_list_final.append(obj)
        if ver:
            verb_list_final.append(ver)
            

    subject_list_final2=copy.deepcopy(subject_list_final)
    object_list_final2=copy.deepcopy(object_list_final)
    verb_list_final2=copy.deepcopy(verb_list_final)
    Convert_To_Good_Lists(object_list_final, object_list_final2)
    Convert_To_Good_Lists(subject_list_final, subject_list_final2)
    Convert_To_Good_Lists(verb_list_final, verb_list_final2)
    sheet[f'A{iiii+2}'] = str(sentence1)
    sheet[f'B{iiii+2}'] = str(sentence_list2)
    sheet[f'C{iiii+2}'] = str(subject_list_final2)
    sheet[f'D{iiii+2}'] = str(object_list_final2)
    sheet[f'E{iiii+2}'] = str(verb_list_final2)
    
      
wb.save(path)
       