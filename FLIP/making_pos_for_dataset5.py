# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 05:29:47 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

""" This Program parses Sentences using SPACY into Subject Object and Verb Parts"""

#import spacy
#nlp = spacy.load("en_core_web_sm")
import en_core_web_sm
import copy
nlp = en_core_web_sm.load()
# need to feed sentences from excel into this to get pos and chunk labels
str11 = "The transition to law school can be difficult."
str1 = "S and C entered into an agreement that required C to pay S a finder’s fee in relation to the acquisition of a molybdenum mining property by C."
str2= "The parties agreed that under this agreement, S was entitled to a finder’s fee of US$1.5 million and was entitled to be paid this fee in shares of C."
#with open(directory, "r",  encoding = "utf-8") as f:
#    document1=f.read()
    

subject_dic = {}
object_dic = {}
verb_dic_total = {}


subject_list_final = []
object_list_final = []
verb_list_final = []
sentence_list= []


counterr_subject = 0
counterr_object = 0
counterr_total = 0

sentence = nlp(str2)
subject_dic.clear()
object_dic.clear()
verb_dic_total.clear()
sentence_list.clear()

sentence_len=len(sentence)
final_value_index= sentence_len-1
[print(i.pos_) for i in sentence]
# clean 
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
                        if sentence[i+value_to_slide_window_sub].pos_ == "DET" or sentence[i+value_to_slide_window_sub].pos_ == "CCONJ" or sentence[i+value_to_slide_window_sub].pos_ == "NOUN" or sentence[i+value_to_slide_window_sub].pos_ == "ADJ" or sentence[i+value_to_slide_window_sub].pos_ == "PROPN" or sentence[i+value_to_slide_window_sub].pos_ == "PRON" or sentence[i+value_to_slide_window_sub].pos_ == "NUM" or sentence[i+value_to_slide_window_sub].pos_ == "PART" or sentence[i+value_to_slide_window_sub].pos_ == "ADP" :
                            subject_dic[counterr_subject].insert(0,[sentence[i+value_to_slide_window_sub].text, sentence[i+value_to_slide_window_sub].pos_, i + value_to_slide_window_sub])
                            continue
                    return_value_sub = "not"
 
        else: #sentence[i+1].pos_ != "AUX" or sentence[i+1].pos_ != "VERB":
            object_dic[counterr_object].append([part_of_speech_parts.text, part_of_speech_parts.pos_ , i])

            while return_value_obj =="found": 
                
                value_to_slide_window_obj+= 1
                if sentence[i+value_to_slide_window_obj].pos_ == "DET" or sentence[i+value_to_slide_window_obj].pos_ == "CCONJ" or sentence[i+value_to_slide_window_obj].pos_ == "NOUN" or sentence[i+value_to_slide_window_obj].pos_ == "ADJ" or sentence[i+value_to_slide_window_obj].pos_ == "PROPN" or sentence[i+value_to_slide_window_obj].pos_ == "PRON" or sentence[i+value_to_slide_window_obj].pos_ == "NUM" or sentence[i+value_to_slide_window_obj].pos_ == "PART" : 
                    object_dic[counterr_object].append([sentence[i+value_to_slide_window_obj].text, sentence[i+value_to_slide_window_obj].pos_ , i+value_to_slide_window_obj])
                    continue
                return_value_obj = "not found"
                
            return_value_obj = "found"
            if i > 0:
                while return_value_obj=="found": 
                    value_to_slide_window_obj2 -= 1
                    if i+value_to_slide_window_obj2 > -1:
                        if sentence[i+value_to_slide_window_obj2].pos_ == "DET" or sentence[i+value_to_slide_window_obj2].pos_ == "CCONJ" or sentence[i+value_to_slide_window_obj2].pos_ == "NOUN" or sentence[i+value_to_slide_window_obj2].pos_ == "ADJ" or sentence[i+value_to_slide_window_obj2].pos_ == "PROPN" or sentence[i+value_to_slide_window_obj2].pos_ == "PRON" or sentence[i+value_to_slide_window_obj2].pos_ == "NUM" or sentence[i+value_to_slide_window_obj2].pos_ == "PART" or sentence[i+value_to_slide_window_obj2].pos_ == "ADP":
                            object_dic[counterr_object].insert(0, [sentence[i+value_to_slide_window_obj2].text, sentence[i+value_to_slide_window_obj2].pos_ , i+value_to_slide_window_obj2])
                            continue                    
                    return_value_obj = "not found"
#cleaning dicitonaries

[sentence_list.append([word.text, word.pos_ , i]) for i, word in enumerate(sentence)]


for sub, obj, ver in zip(subject_dic.values(), object_dic.values(), verb_dic_total.values()):
    if sub:
        subject_list_final.append(sub)       
    if obj:
        object_list_final.append(obj)
    if ver:
        verb_list_final.append(ver)
        
previous_obj_temp_list = []   
previous_obj__value_temp_list = []  
object_list_final2=copy.deepcopy(object_list_final)

    
    

for ii, obj1 in enumerate(object_list_final):
    obj_temp_list = []
    for obj2 in obj1:
        obj3=obj2[2]
        obj_temp_list.append(obj3)
    if ii > 0:
        print(obj_temp_list)
        print(previous_obj_temp_list[0])
        checking_for_repeats = any(obj4 in obj_temp_list for obj4 in previous_obj_temp_list[0])
        print(checking_for_repeats)
        if checking_for_repeats is True:
            print(previous_obj__value_temp_list)
            object_list_final2.remove(previous_obj__value_temp_list[0])
            
            
    previous_obj__value_temp_list.clear()        
    previous_obj_temp_list.clear()   
    previous_obj_temp_list.append(obj_temp_list)
    previous_obj__value_temp_list.append(obj1)
    
#del object_list_final[i for i in object_items_to_remove]
print(object_list_final2)
print("hi")
object_list_final2 # THIS IS THE ONE WANT TO WORK WITH NOW
   

    
    
    


