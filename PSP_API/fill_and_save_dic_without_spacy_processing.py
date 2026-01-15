# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 18:10:36 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
# transmit commands as a json maybe
class fill_single():
    
    
    def __init__(self):
        """ """
    def testing_pickle_function(self,filee,objectt,testing1=True,testing2=False):
        """ """
        if testing1==True:     
            with open(filee, 'wb') as file:
                pickle.dump(objectt, file)
                
        if testing2==True:
            with open(filee, 'rb') as file:
                person_comp_info_dic_with_action = pickle.load(file)
        return person_comp_info_dic_with_action
            
        
        
    def sub_proper_noun_from_pronoun(self,sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,pronoun_iter_in_sub_list):
        """ find the mention of org and sub it into sentence"""
        proper_noun_found=False
        proper_noun_phrase_list=["--REFFERENTIAL PHRASE--"]
        pos_phrase_list=["PROPN"]
        current_sentence_word_list=sentence_word_list[current_sent_iter]
        current_sentence_pos_list=token_pos_list[current_sent_iter]
        previous_sentence_word_sub_list=sentence_word_list[current_sent_iter-minus_current_sen_iter]
        previous_sentence_token_pos_list=token_pos_list[current_sent_iter-minus_current_sen_iter]
        for i13, possss in enumerate(previous_sentence_token_pos_list):   
            if possss=="PROPN":
                proper_noun_found=True              
                proper_noun_word=previous_sentence_word_sub_list[i13]
                proper_noun_phrase_list.append(proper_noun_word)
                pos_phrase_list.append(possss)
                continue
            if proper_noun_found==True:# rthis will prevent us getting proper nouns that are not related
                break
        if proper_noun_found==True:
            # adding 1 here ot remove the word being subbed over the pronoun word
            current_sentence_word_list=current_sentence_word_list[:pronoun_iter_in_sub_list]+proper_noun_phrase_list+current_sentence_word_list[pronoun_iter_in_sub_list+1:]
            current_sentence_pos_list=current_sentence_pos_list[:pronoun_iter_in_sub_list]+pos_phrase_list+current_sentence_pos_list[pronoun_iter_in_sub_list+1:]
            
            #current_sentence_word_list.insert(pronoun_iter_in_sub_list,proper_noun_phrase_list) 
        return  current_sentence_word_list,current_sentence_pos_list, proper_noun_found
    
    
    def get_intital_action_info_from_page(self,page_text,intital_link):
        """ # first divide up text into sentences
        # second run through each sentence find all instances of noun chunk verb object 
        # sub pronoun for proper nouns and make notes of this all referential phrases 2-3 sentences ahead
        # store these approrpiately in dicitonaries if they have this info

        # then store all of them in dic based on qualities to divide up all actions into next actions and sub actions
        # using order and sub action function"""
        import re
        import copy
        import spacy
        import time
        person_comp_info_dic_with_action_list=[]
        from nltk.corpus import stopwords     
        cleaned_noun_chunk_list=[]
        self.nlp = spacy.load("en_core_web_sm")# this is temporary
        #print(f" page_text {page_text}")
        #print(f" intital_link {intital_link}")
        #input('this is the function to islate and test')


        
        person_comp_info_dic_with_action={         
            "action":"",
            "action_temporal_placement_in_life_list":"#",  
            "full_action_sentence":[],
             
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            "intital_page_text":[],
            # run through all info in action dic to better choose actions
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],
            "object":[],

            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[], }
        
        
        sentence_list=[]
        sentence_word_list=[]
        iter_list=[]
        token_label_list=[]
        token_pos_list=[]
        iter_sub_list=[]
        token_sub_label_list=[]
        token_pos_sub_list=[]
        sentence_word_sub_list=[]
        entity_text_dic={}
        chunk_span_sub_list=[]       
        saved_noun_chunk_list=[]
        saved_noun_chunk_sub_list=[]       
        sentence=""
        # clean the text  
        #page_text=sel_soup.text
        page_text=re.sub("[\[\]{}\'\(\)]","",page_text) 
        page_text=re.sub("  ", " ", page_text)
        page_text=re.sub("-", " ", page_text)
        #spacy_dic=self.label_website_text_with_spacy(website_text)
        doc = self.nlp(page_text)
        for ent in doc.ents:
            #print(f"{ent.text},{ent.label_}")
            #print('hehe')
            textt=ent.text
            labell=ent.label_
            if " " in textt:
                textt_list=textt.split()
            else:
                textt_list=[textt]
            for textt in textt_list:
                if ent.label_ == "PERSON":
                    entity_text_dic[ent.text]="PERSON"
                if ent.label_ == "ORG":
                    entity_text_dic[ent.text] = "ORG"                
                if ent.label_ == "DATE":
                    entity_text_dic[ent.text] = "DATE"
                if ent.label_ == "MONEY":
                    entity_text_dic[ent.text] = "MONEY"         
                continue 
            
            
            
        #input("meow")
        # noun chunks must be in order 
        
        ### LOOP 1        
        used_noun_chunk_iter_list=[]
        used_noun_chunk_sub_iter_list=[]         
        used_word_sentence_iter_list=[]       
        used_word_sentence_sub_iter_list=[]  
        used_word_iter_list=[]
        #empty_noun_chunk_word_matching_list=[None for iterr in range(len(doc))]
        empty_noun_chunk_word_matching_list=[[str(token.text),None] for token in doc]

        
        noun_chunk_words_found=0
        used_noun_chunk_iter_dic={}
        noun_chunk_iter=0       
        all_noun_chunk_list=[]
        
        for noun_chunk in doc.noun_chunks:
            new_noun_chunkkk=""
            noun_chunkk=str(noun_chunk).split()
            for wordddd in noun_chunkk:
                #print(wordddd)            
                if wordddd!="":
                    if new_noun_chunkkk =="":
                        #print('hi')
                        new_noun_chunkkk=f"{wordddd}"
                    else:
                        new_noun_chunkkk+=f" {wordddd}"
            all_noun_chunk_list.append(str(new_noun_chunkkk)) 
            #nounn_chunk_list=str(noun_chunk).split(" ")  
        all_noun_chunk_list_len=len(all_noun_chunk_list)
   
        noun_chunkkk=all_noun_chunk_list[noun_chunk_iter]
        nounn_chunk_list=noun_chunkkk.split(" ")
        noun_chunk_list_len=len(nounn_chunk_list)  
        for word_iter, tokenn in enumerate(doc):
            if word_iter in used_word_iter_list:
                continue
            wordd=tokenn.text  
            #print(wordd)
            #print(noun_chunk_iter)
            #print(nounn_chunk_list)
            if wordd in nounn_chunk_list:
                #print("word in")               
                if noun_chunk_iter not in used_noun_chunk_iter_dic:
                    used_noun_chunk_iter_dic[noun_chunk_iter]=[]                   
                used_noun_chunk_iter_dic_len=len(used_noun_chunk_iter_dic[noun_chunk_iter])  
                # want to check if next word in noun chunk is the word and add it to the used word list
                # also want to see if noun chunk list is long enough to check this
                print(f"used_noun_chunk_iter_dic_len {used_noun_chunk_iter_dic_len}")
                if nounn_chunk_list[used_noun_chunk_iter_dic_len]==wordd:
                            used_noun_chunk_iter_dic[noun_chunk_iter].append(wordd)
                            empty_noun_chunk_word_matching_list[word_iter][1]=noun_chunk_iter
                else:
                    continue
                if used_noun_chunk_iter_dic[noun_chunk_iter]==nounn_chunk_list:
                    print('lists match')
                    noun_chunk_iter+=1
                    print(noun_chunk_iter)
                    if noun_chunk_iter==all_noun_chunk_list_len:# this avoids the error where last value tries to grab a value not in noun chunk list
                        break
                    else:
                        noun_chunkkk=all_noun_chunk_list[noun_chunk_iter]
                        nounn_chunk_list=noun_chunkkk.split(" ")
                        noun_chunk_list_len=len(nounn_chunk_list)  
                        continue                          
        #print(all_noun_chunk_list)
        #print(used_noun_chunk_iter_dic)
        #print(empty_noun_chunk_word_matching_list)                          
        #input() 
          
        ### LOOP 2
        # need to sub numbers and non word characters out of noun chunks
        # like periods brackets and [] and slashes
        # have sentence a key and pos values and text and noun chunk values all included
        # get noun chunk related to work
        # mark noun chunk components as used and words as used to avoid getting duplicates
        # once you find a matching word for a noun chunk consider the length of noun chunk and try to find the remainer in the sentence
        # that way
        ## aux could be verb as well or ahelping verb
        #sentence_assocaited_chunk_list=[] 
        #sentence_assocaited_sub_chunk_list=[]
        # going to move this before the other loop and make this loop one
        #noun_chunk_list=[]
        #noun_chunk_sub_list=[]
        for i8, token in enumerate(doc):
            noun_chunk_group=empty_noun_chunk_word_matching_list[i8]
            token_label=None
            if token.text in entity_text_dic:
                token_label=entity_text_dic[token.text]
                
            if sentence != "":
                text_len=len(token.text)
                sentence+=f" {token.text}"
                iter_sub_list.append(i8)
                token_sub_label_list.append([token.text,token_label])
                token_pos_sub_list.append(token.pos_)
                sentence_word_sub_list.append(token.text)
                saved_noun_chunk_sub_list.append(noun_chunk_group)
                
                    
            else:
                text_len=len(token.text)
                sentence=f"{token.text}" 
                iter_sub_list.append(i8)
                token_sub_label_list.append([token.text,token_label])
                token_pos_sub_list.append(token.pos_)
                sentence_word_sub_list.append(token.text)
                saved_noun_chunk_sub_list.append(noun_chunk_group)


                
            if "." in token.text :# will need to test htis one
              sentence=re.sub(r"[\n\r]"," ",sentence)
              sentence=re.sub(r"\s\s+","  ",sentence)
              sentence_list.append(sentence)
              iter_list.append(iter_sub_list)
              token_label_list.append(token_sub_label_list)
              token_pos_list.append(token_pos_sub_list)
              sentence_word_list.append(sentence_word_sub_list)
              saved_noun_chunk_list.append(saved_noun_chunk_sub_list)
              sentence="" 
              iter_sub_list=[]
              token_sub_label_list=[]
              token_pos_sub_list=[]
              sentence_word_sub_list=[]
              saved_noun_chunk_sub_list=[]
        #for i in range(len(sentence_list)):
            #print(i)
            #print(sentence_list[i])
            #print('------')
            #print(token_label_list[i])
            #print('------')

            ##print(token_pos_list[i]) 
            #print('------')

            #print(saved_noun_chunk_list[i])
            #print('------')
        #print('stop')
        #print(saved_noun_chunk_list)
        #input(used_noun_chunk_iter_dic)
        ### LOOP 3   
        # match the chunk words with the words in the sentnece
        # so you know each word that goes with each chunk so you can match verb against noun chunk
        # and fiue out the action part of the sentence
        # create the action sentences here
        # use this to fill in the action dicitionary
        
        # sub out pronouns now for referential phrases
        temporal_counter=0
        used_action_list=[]
        for current_sent_iter, sentenceee in enumerate(sentence_list):
            temp_chunk_str_dic={}
            noun_chunk2_number=None
            last_chunk=None
            add_next_noun_chunk=False
            token_sub_label_list=token_label_list[current_sent_iter]
            token_pos_sub_list=token_pos_list[current_sent_iter]
            sentence_word__sub_list=sentence_word_list[current_sent_iter]
            sentence_assocaited_sub_chunk_list=saved_noun_chunk_list[current_sent_iter]
            person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
            verb_counter=0
            #first_chunk_number=0# just by default set this mayneed to change later not usre the effect t wil have
            #first_chunk_end_iter=0
            #first_chunk_number=0# may need to change htis just addign it int o fix a error
            if "VERB" in token_pos_sub_list or "AUX" in token_pos_sub_list:
                for pos_iter, posss in enumerate(token_pos_sub_list):                   
                    verb_wordddd=sentence_word__sub_list[pos_iter]
                    posss=posss
                    
                    
                    current_chunk_number=None
                    chunk_str=""
                    if posss == "VERB" or posss == "AUX":
                         first_chunk_number=None
                         verb_counter+=1# this makes sure we only sub out PRON in intital noun chunk and no others in setnece
                         # find noun chunk before find noun chunk after
                         for chunkk_iter, chunk_word in enumerate(sentence_assocaited_sub_chunk_list):                             
                             wordd=chunk_word[0]
                             chunkk=chunk_word[1]
                             if chunkk!=None:
                                 current_chunk_number=chunkk
                                 chunk_iter=chunkk_iter
                                 
                             if chunkk_iter==pos_iter and current_chunk_number!=None :
                                 chunk_text1=" ".join(used_noun_chunk_iter_dic[current_chunk_number])
                                 #chunk_str=chunk_text1 + f" {verb_wordddd}  "
                                 #first_chunk_iter=chunkk_iter
                                 first_chunk_number=current_chunk_number
                                 first_chunk_end_iter=chunk_iter
                                 continue

                             if chunkk_iter>pos_iter and chunkk!=None:
                                 if first_chunk_number!=None:
                                     first_chunk_len_minus_1=len(used_noun_chunk_iter_dic[first_chunk_number])-1
                                     second_chunk_len_minus_1=len(used_noun_chunk_iter_dic[current_chunk_number])
                                     #print(f"second chunk {used_noun_chunk_iter_dic[current_chunk_number]}")

                                     # will hopedully get us to the end of the chunk
                                     #chunk_text2=" ".join(used_noun_chunk_iter_dic[current_chunk_number]) 
                                     #find the end of the second second chunk segement
                                     second_chunk_end_iter=chunkk_iter   
                                     #print(f"sentence_word__sub_list {sentence_word__sub_list}")
                                     #action_segment=" ".join(sentence_word__sub_list[first_chunk_end_iter-first_chunk_len_minus_1:second_chunk_end_iter+second_chunk_len_minus_1])# but by adding this value here hopefully will get us to the end of the chunk                                
                                     #sub out in first chunk using pos any pronouns for proper nouns
                                     #and other referential phrases for their given referenced nouns
                                     # or likely referecned nouns
                                     first_chunk_pos=token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1:first_chunk_end_iter+1]
                                     #print("first_chunk_pos")
                                     #print(first_chunk_pos)
                                     #input() 
                                     if verb_counter<=1:
                                         # do this only for the first chunk of a sentence and first verb of sentence
                                         # dont sub out pronouns in second half of sentence
                                         for iter_pos_noun_chunk_1, posssss in enumerate(first_chunk_pos):
                                             if posssss=="PRON":
                                                 # need to locate htis iter in the token_pos_list
                                                 token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1:first_chunk_end_iter+1]
                                                 current_poss_in_sub_list=token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1+iter_pos_noun_chunk_1]
                                                 current_poss_in_sub_list_iter=first_chunk_end_iter-first_chunk_len_minus_1+iter_pos_noun_chunk_1
                                                 #print(f"current_poss_in_sub_list {current_poss_in_sub_list}")
                                                 #print('FOUND PRON')
                                                 #print(posssss)
                                                 #print(f"current_sent_iter {current_sent_iter}")

                                                 if current_sent_iter>3:#  look back 3 at intitally 2 1 0
                                                     for minus_current_sen_iter in range(1,4):
                                                         sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)
                                                         #print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                         #print(f"proper_noun_found {proper_noun_found}")  
                                                         if proper_noun_found==True:
                                                             break                                                    
                                                     continue
                                                 if current_sent_iter==2:# only look back 2  
                                                     for minus_current_sen_iter in range(1,3):
                                                         sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)  
                                                         #print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                         #print(f"proper_noun_found {proper_noun_found}")
                                                         if proper_noun_found==True:
                                                             break      
                                                     continue                       
                                                 if current_sent_iter==1:# only look back 1
                                                     for minus_current_sen_iter in range(1,2):
                                                         sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)
                                                         #print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                         #print(f"proper_noun_found {proper_noun_found}")
                                                         if proper_noun_found==True:
                                                             break
                                                     continue                      
                                                 if current_sent_iter==0:# dont look back
                                                     continue                                    
        
                                     action_segment=" ".join(sentence_word__sub_list[first_chunk_end_iter-first_chunk_len_minus_1:])# but by adding this value here hopefully will get us to the end of the chunk
                                     #print(f"action_segment {action_segment}")                                
                                     #chunk_str=chunk_str+chunk_text                                                        
                                     #print('object')
                                     #print(chunk_text1)    
                                     #print(action_segment)
                                     #print(f" trans {sentence_word__sub_list[first_chunk_end_iter+1:chunkk_iter]}")
                                     #input()
                                     person_comp_info_dic_with_action_copy['action']= action_segment
                                     person_comp_info_dic_with_action_copy['object']= chunk_text1  
                                     person_comp_info_dic_with_action_copy['other_things_effected'].append(sentence_word__sub_list[chunkk_iter:])
                                     person_comp_info_dic_with_action_copy['transformations'].append(sentence_word__sub_list[first_chunk_end_iter+1:chunkk_iter])
                                     temporal_counter+=1
                                     person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
                                     person_comp_info_dic_with_action_copy["link"]=intital_link
                                     
                                     
                                     #print('effects')
                                     #print(sentence_word__sub_list[chunkk_iter:])
                                     #print('transs')
                                     #print(sentence_word__sub_list[first_chunk_end_iter+1:chunkk_iter])
                                     #input()
                                     chunk_str=""
                                     break
                                     
                                 
                                           
                         #print(person_comp_info_dic_with_action_copy['action'])
                         if person_comp_info_dic_with_action_copy["object"]!=[]:
                             if person_comp_info_dic_with_action_copy["action"] in used_action_list:
                                 continue
                             used_action_list.append(person_comp_info_dic_with_action_copy["action"])
                             person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
                             person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)   
                         # create action
                    else:
                         continue
        #print(person_comp_info_dic_with_action_list)
        #input()
        return person_comp_info_dic_with_action_list
    # if verb followed by other verb in between noun chunks
    # group these as a verb chunk
    # then done
    #who work  the rights
    #who protect  the rights
    #because getting this error now
    #should jusrt be work to protect the rights
    # sub out referentisal phrase
    # for referntial phrases add
    # if referential phrase sub in last referecned noun chunk
    #before the current noun chunk
    # if pronoun sub in proper noun
    # if followed by a aux 
                             # if first chunk is not before the verb
                             # then just grav the text before
                             # want the chunk iterr to line up 
                             # the word before is 1
                             # the could be siutation where they are equal
                             # but the current chunk number is None
                    
    def decide_whether_to_add_sub_task_to_sub_task_lists_or_not(self,person_comp_info_dic_with_action_list,sub_action_dic,previous_patterns_add_versus_not):
        """ """
        
    def add_sub_actions_to_list_sorted_by_objective_break_up_if_two_actions_conflict(self,sub_action_dic,objective_sub_task_list_list,prompt_objectives_to_score_list,person_comp_info_dic_with_action_list,patterns_for_placing_actions_via_objectives):
        """ """
             
        

    def use_previous_paragraph_structures_to_order_sub_task_in_strat(self,objective_sub_task_list_list, previous_paragraph_patterns):
        """ """
    def use_problem_envrionment_to_decide_whether_to_add_sub_task_or_not(self,sub_action_dic,action_problem_environemnt_context,stop_words):
        """ this is currently not retrieivng a output need to get it to"""
        non_stop_word_objects_list=[]
        action_object=sub_action_dic['object']
        print(f"action_object {action_object}")
        #input()
        action_object_list=str(action_object[1:-1]).split(" ")
        includee=False
        for objectt_word in action_object_list:
            if objectt_word.lower() not in stop_words:
                non_stop_word_objects_list.append(objectt_word)
            else:
                continue
        for non_stop_word_object in non_stop_word_objects_list:
            if non_stop_word_object in action_problem_environemnt_context:
                includee=True
                return includee
            if non_stop_word_object not in action_problem_environemnt_context:
                continue
        return includee
            
        
    def fill_and_save_sub_action_dic(self,sub_action_dic):
        """ """
        from multiprocessing import Process, Queue
        import sys
        import json
        import re
        import spacy
        import time
        import psycopg2
        import pickle
        import copy
        import pickle
        import subprocess
        person_comp_info_dic_with_action_template={         
            "action":"",
            "action_temporal_placement_in_life_list":"#",               
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":[],
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            "intital_page_text":[],
            # run through all info in action dic to better choose actions
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],
            "object":[],
            
            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[], }

        table_name="guide_person_positional_info_with_action_info"
        #person_comp_info_dic_with_action_list=sys.argv[1]
        #person_comp_info_dic_with_action_list=json.loads(person_comp_info_dic_with_action_list)
        #fill=fill_single()
        
        #fill.nlp = spacy.load("en_core_web_sm")
        print('heheh')
        #input('this is start of sub action fill')
        
        
        print('Fill and save sub dic websites')
        person_comp_info_dic_with_action_temp=sub_action_dic# use example
        wiki_thing_being_discussed=person_comp_info_dic_with_action_temp["link"]
        single_link_list=re.split(r"/",wiki_thing_being_discussed)
        link_item_title=single_link_list[-1]
        #all_link_item_titles_str=".  ".join(all_link_item_titles_list)
        link_item_title=re.sub("_"," ",link_item_title)   
        print(link_item_title)
        print('questio4n!')
        print(f'INTITAL sub_action_dic {sub_action_dic} ')
        orginal_action=sub_action_dic["action"]
        person_comp_info_dic_with_action=copy.deepcopy(person_comp_info_dic_with_action_template)
        person_comp_info_dic_with_action["action"]=orginal_action
        person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=sub_action_dic["action_temporal_placement_in_life_list"]
        person_comp_info_dic_with_action["link"]=sub_action_dic["link"]
        person_comp_info_dic_with_action['object']=sub_action_dic["object"]
        person_comp_info_dic_with_action['transformations']=sub_action_dic["transformations"]
 
        #duck duck
        problemm0=person_comp_info_dic_with_action["action"]
        duckduck = Queue()
        p = Process(target=retreive_problem_data_from_web, args=(duckduck,problemm0))
        p.start()
        
        
        #get_sub_action_list_data_use_patent_data_and_other
        problemm1="what are the steps i would take to " + person_comp_info_dic_with_action1["action"]
        sub_action = Queue()
        p1 = Process(target=retreive_problem_data_from_web, args=(sub_action,problemm1))
        p1.start()
             
        #get_placement_of_other_people_places_and_things_related_to_action
        problemm2="what are other things i should consider relating to " + person_comp_info_dic_with_action1["action"]
        placement = Queue()
        p2 = Process(target=retreive_problem_data_from_web, args=(placement,problemm2))
        p2.start()
        
        
        
        #figure out all things you can use
        problemm4="what is the location i would take to " + person_comp_info_dic_with_action1["action"]
        locate = Queue()
        p3 = Process(target=retreive_problem_data_from_web, args=(locate,problemm4))
        p3.start()
        
        problemm5="what are the resources i would take to " + person_comp_info_dic_with_action1["action"]
        resource = Queue()
        p4 = Process(target=retreive_problem_data_from_web, args=(resource,problemm5))
        p4.start()
        print('hi')

        # tools
        problemm3="what are the tools i would use to " + person_comp_info_dic_with_action1["action"]
        tools = Queue()
        p5 = Process(target=retreive_problem_data_from_web, args=(tools,problemm3))
        p5.start()
        
        problemm6="what are the skills that I would take to " + person_comp_info_dic_with_action1["action"]
        skil = Queue()
        p6 = Process(target=retreive_problem_data_from_web, args=(skil,problemm6))
        p6.start()
        
        
        duckduck=duckduck.get()
        sub_action=sub_action.get()  
        placement=placement.get()
        tools=tools.get() 
        locate=locate.get()
        resource=resource.get()
        skil=skil.get()          
        p.join()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        
        for website_text1 in duckduck:
            #print(website_text1)
            person_comp_info_dic_with_action["action_objects"].append(website_text1)
        #for website_text2 in sub_action:
        #    person_comp_info_dic_with_action["sub_steps_to_complete_actions"].append(sub_action_list_list)
        print('in the future need to get actions for these sub actions but for now just recurse on actions')
            
        for website_text3 in placement:
            person_comp_info_dic_with_action["position_of_other_people_places_and_things"].append(website_text3)
            
        for website_text4 in tools:
            person_comp_info_dic_with_action["tools_required_to_perform_action"].append(website_text4)
            
        for website_text5 in locate:
            person_comp_info_dic_with_action["location_needed_to_take_action"].append(website_text5)
        for website_text6 in resource:
            person_comp_info_dic_with_action["resources_required_to_perform_action"].append(website_text6)
            
        for website_text7 in skil:
            person_comp_info_dic_with_action["skills_required_to_perform_action"].append(website_text7)
  
        person_comp_info_dic_with_action["work_experience"].insert(0,bio)
        person_comp_info_dic_with_action["work_experience"].insert(0,hist)
        person_comp_info_dic_with_action["projects_interested_in"].insert(0,projects_int)
        
        print('done all one round')
        fill.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        fill.cur = fill.conn.cursor()      
        fill.store_value_in_sql_table(person_comp_info_dic_with_action,table_name)
        filled_sub_action_dic=person_comp_info_dic_with_action  
        #input('check storing of value')
        print(f" FILLED SUB DIC {filled_sub_action_dic['tools_required_to_perform_action']}")
        #input()
        return filled_sub_action_dic

    
    def fill_saved_sub_action_dic_and_order_and_divide_actions_into_action_lists(self,sub_action_person_comp_info_dic_with_action_list,person_comp_info_dic_with_action1):
        """refer to methods in problem solving tkinyter program for guaince on how to build this
        ?? how do i sort actions using various objectives like amount of people impacted most money most people help which look at the alternative actions effects and objects involved? ###fYoKuAhEsPaNrAtDoIfJ
        THIS IS HOW I WILL SORT ACTIONS SUPER IMPORTANT
        problem solving program
        need to also build a life action tree from this to take best actions
        THIS IS KEY
        self.action_space_with_effects_dic
        the action space
        is actions and there effects
        objects and effects
        so we will sort and search this space using the effects as context
        and the positonal info dic and objectives will be key in finding actions in this space using these effects
        so how do we do that
        Build FFNN?
        make sure that qualities of object are associated with specific transformations  
        
        strategy_methods_problem_tree_dic=
        self.sort_actions_into_strat_by_max_different_effect_score(self.strategy_methods_problem_tree_dic)
        
        how do you integrate the objective and  positional info into the search and choice of actions
        self.consider_past_problem_data() to search and sort actions
        
        # use nn maybe to rank actions amd 
        maybe make the search much faster with nn
        
        search will be two for loops
        each qualtity of personal information run against all actions to rank actions
        or to search for best action
        then return actions to take
        
        use peoples lives to collect data about possible actions 
        to train nn and so can better know effects
        
        convert objective into something useful
        compare each perosnal ifnormation qualtity against 
        for personal_qualtity in objective_personal_qualtity_dic:# and o
            for actionn in actionn_dic:
                #give action a ranking for this personal qualtiy some pattern or relationship between them
                # use data to determine this relationship
                #then use objective as a additianl critiera that is more heavily weighted
                 then add all the values up to a number to determine actions rank
                 then sort list
                 
        # issue is we dont have the labels of best action based on objective/position so maybe nn not best choice
        # OR USE NN
        input is all personal qualities and objective values
        out put is action chocie based on those values
        
        history repeats itself is the idea
        
        so the same or similar actions should have same or simlar effects 
        if another person takes it
        
        ###
        use exmaples of peoples lives because it will elminate all actions in action space that are not possible and those that never have been done before ( but assuming we make ones found generic enough this is ok)
        and then make the actions more generic to allow for creativty and more useful so can think around
        like for example invent something rather than invent car if that is what a person did
        more example the strategies or action_sets are peoples actual lives who were successful like mlk
        or greta thunberg or elon musk
        or dad or mom
        
        using people lives will get us actions worth doing and the effects of such action
        and we can cateogrize peoples lives related to an objective
        
        so for example greta thunberg life_action_set would be under helping most people and in that area
        
        


        the effects are what the person ended up with at the end of there life and got by completing a different action
        see if i can get effects for each aciton rahter than each whole life_action_list for a person
        
        so suggest these action sets based on peoples perosnal information put in to get different objectives like help most people or make the most money
        
        if complete action should get simialr effects and similar future possible actions
        
        
        look at the actions these people take will allow you to create action space
        
        ###
        so when i log on it will display trunciated life_action_list to use to maxmize different objectives
        and will rotate the ones shown so build this in too
        but will show specific life_action_list based on current position and perosnal info inputted
        
        ------------------------
        
        LEFT OFF HERE how to write this function to sort/search life_action_lists
        so how do i  divide life action on objective MAYBE use personal qualitites of persons life_action_list we are using , maybe use effects words of actions and there relationship to objective words   
        # then rank each actions and life_action_lists relationship to the objective and how well it achevies it
         
        #use personal characeristic of persons who I get the life_action_lists from to figure out how to rank/suggest life_action_lists to a  user  based on an users perosnal info dic
        so for example greta thunber is a women who is young sweidsh etc so would suggest for a user who is swedish and a young woman and at greta age a truncated life dag to the women current age
        under the objective category of making the world better
        
        so for
        maybe 3 deep neural network
        LEFT OFF HERE
        SO  for each life_action_list create scores for each category of objective which take the objective and perosnal characeritcs into account
        
        then display these strats
        takign perosnal characeritic into consideration
        
        
        
        #score based on objective and 
        
        
        # then would cateogrize greta life dag under helping most people giving it a high rank
        
        # note how the person is simialr to them on what dimensions 


        #
        so if greta thunberg then put in helping people

        and how do i divide on perosnal characeristics so i know how much of life_action_list to display 
        and which life_action_list to display
        ###
        what informaiton do i need to scrape to sort and or search the life_action_lists based on objective and perosnal information
        look at peoples lives
        look at people who helped the most people
        look at people who made the most moeny
        and the actions they took to get to where they are
        and then train model using these people actions or histories life_action_list
        inputting their personal characeritisc and then the action they took
        to recommend to someone in a simialr simualr the best action they could take to accomplish objective
        use biographies and books and linkeind etc
                    self.keep_updating_and_stealing_existing_business_methods_and_final_product_funnel_work_into_problem_environment_to_solve_problem()
        """
        #keys are obejhctives
        #values are lists lists
        import pickle
        prompt_objectives_to_score_list=["helping the most people Helping others is an important part of life, giving you a sense of purpose and boosting your happiness. In fact, acts of kindness can boost feelings of confidence, control, happiness, and optimism, says the Mental Health Foundation.Supporting others has a positive effect on the world around you. Kind acts may also encourage others to repeat the good deeds they’ve experienced themselves, contributing to a more positive community.If you want to help others more but aren’t sure where to start, look no further. Whether you’re looking for ways to help friends and family or give back to your community, keep reading for a list of ideas to get you started helping others.Where can I find ways to help others?First, focus on your passion when considering ways to help others. Your passion for helping others can be the foundation for your giving. Helping someone in need isn’t about how much you give but how much love you put into it.Inspiration for how to help others in need can happen anywhere. Small acts of kindness, like holding the door or offering a compliment, can have a significant impact. Helping people can include more substantial efforts, like making donations — whether of time or money — or giving items to help someone in need.Here are some ideas for finding ways to help others that will bring you joy and a sense of connection.Ask community leaders, friends, and family how you can help. Explain to them how you hope to help others and why you desire to help and see what they suggest. The opportunities for helping someone in need may surprise you!Look for opportunities to help and lend a hand without being asked to find out the best way to help. For example, hold the elevator door for a colleague or offer to take a photo for a group of tourists if they’re struggling with a selfie stick.1. Be proactive, not reactive.Many lives are lost to health emergencies that could have been managed through learning lifesaving skills Knowledge of cardiopulmonary resuscitation (CPR) and first aid help in emergencies at home, in public, or at work by providing immediate care, reducing injury severity, promoting safety, providing reassurance, and increasing workplace safety.Becoming trained in CPR and first aid is one of the best ways to support others and the community, helping others in need.American Red Cross Training Services offers a variety of CPR and first aid training programs, which you can take online, in person, or in combination to help everyone, whether your neighbors, colleagues, family, or friends. Find a CPR and first aid training program that fits your schedule.Find a ClassCPRFamily sharing a meal.Benefits of Taking a CPR, AED or First Aid CourseBe prepared: Protect your loved onesBe confident: Act with hands-on trainingPeace of mind: Know how to handle emergenciesHelp your community: Use lifesaving skills when neededTake a CPR Class2. Give your time.The gift of time is valuable and satisfying. It also makes giving accessible since we don’t all have the same amount of money, but we all have the same amount of time.Here are some ways to give your time and help people in need.Teach: Offer to teach friends and family members struggling with a skill you know well. Learn how to become a CPR Instructor! Teach people outside your social circle, too — try tutoring a student in math, for example, or showing your coworker how to use the office copier.Support: Be the first to offer condolences when someone you care about is suffering. Do what you can to comfort them, whether they need a hug, a shoulder to cry on, or a helping hand. Talk to them with empathy and compassion and ask if there is anything you can do to help.Listen: Not everybody seeks hands-on help or a solution to their problems; they might simply need to express their feelings while a supportive friend listens.Compliment: While giving compliments might not be what you traditionally picture when you think of helping people, it does help. Offer compliments to everyone around you, giving sincere praise while celebrating their successes and qualities you admire the most.Volunteer: Find a charity you’d like to support, like a shelter or soup kitchen, and spend time there doing whatever needs to be done. Not only will this help others, but it’ll also give you a newfound appreciation for all the good things in your life — and it’ll make you a more compassionate person.3. Donate to a worthy cause.Monetary donations are a great way to help others but aren’t the only way to donate to help those in need.Here are a few ideas for donating to worthy causes and supporting others.Donate furniture and clothing to a local shelter.Donate unopened spices, canned soups, or beans to a local food bank.Donate toys to local shelters and food banks.Donate blood if you can.Donate the opportunity for holiday and birthday gifts. Ask friends and family to make donations to charities instead of getting you gifts.Donate your car.4. Send a thoughtful note or care package.Sometimes, helping others is as simple as letting them know that you care. When people feel isolated or cut off from their friends or family, even a small gesture can help them feel more connected and brighten their day.Send handwritten cards and even care packages with special treats inside.Write a friendly email or letter and casually mention why you like the recipient.5. Express appreciation.Receiving thanks is another way to help each other and help our community. Plus, showing gratitude not only helps others feel appreciated but makes you happier too!Express appreciation when someone does something nice for you. Let your loved ones know how much you appreciate them, even when there’s nothing specific to thank them for.Practice gratitude by creating a list of things you’re grateful for and sharing it with others.Share a social media post about how much you appreciate someone’s support as you change careers or tell a friend how proud you are that they ran a whole marathon.Compliment underappreciated people, like the person bagging your groceries or bussing your table at a restaurant.Thank frontline health workers and first responders.Be neighborly. Check on neighbors, especially those who live alone, are elderly, have health or mobility issues, or care for children.Finally, helping other people should not equal a guilt trip. We have all felt the dread that comes from being coerced into helping others. When considering ways to help others, think about what you have excess — time, money, or unused items — and how that may help others in need.Now that you have the tools and inspiration to help others, it's time to put them into action. Together, we can make a positive impact on the world!",
                                         "making the most money The 6 figure income in your teens is the way outlier. The 9-5 is the path to comfort for the vast majority. The secret to fast easy money can be a couple things, incredible talent, large up front investment, a great idea, fraud, or dynamic charisma all coupled with the largest single factor, luck. You are comparing yourself to the top .001% or just liars. It's not worth it to hunt for a secret. It is worth it to better yourself, try and increase your worth and find someone willing to pay you what you're worth. It is worth it to be as happy and content as you can with what you have. It is certainly worth it to live on less than you make and sacrifice for the future. Side hustles are popular, and possible. What you need is a good idea and the motivation to make it happen.25 ways to make moneyWe turned 25 ways, complete with need-to-know details, to inspire you to earn. While most people want to make money fast, don’t discount the “slow” gigs, as they may pay more in the long run.How to make money onlineHow to make money from homeHow to make money offlineFor sections with input from Redditors: We sifted through Reddit forums to get a pulse check on how users feel about certain side hustles. We used an AI tool to help analyze the feedback and then summarized insight. People post anonymously, so we cannot confirm their individual experiences or circumstances.How to make money online1. Pick up freelance work onlineMake money online through websites such as Upwork, Fiverr and Freelancer.com. These sites offer opportunities to do a variety of freelance jobs, like writing, programming, design, marketing, data entry and being a virtual assistant.A report from Freelancer.com found that computer security jobs had the fastest growth in listings on its site in the second quarter of 2024, up 27.1%.Jobs involving writing skills are also in high demand. Although generative artificial intelligence (AI) is being used more for content creation, it can’t fully do the work of human writers.Companies are looking for writers who know how to edit AI content and who have at least a basic understanding of search engine optimization — learning or beefing up SEO skills could be a lucrative side hustle.No matter what freelancing you do, keep track of the going rate for the kind of work you provide so you know what to charge. Some freelancers are charging $100 an hour or more for their freelance writing services.Expert take: Soraya Ivette is a content marketing strategist who offers services on Fiverr. She started freelancing part time when she was home with her young children, and has done well.Once I set up my profile on Fiverr, I started getting job requests within a couple of weeks and I started taking on more jobs and making regular money consistently every month, she said in an email interview.Total time: It can take a while to get your first gig.Setup: 24-48 hours.How easy to start: Easy, if you have the expertise.Age threshold: Typically 16 to 18+.How fast you'll get paid: Varies by site.Need to knowIt takes Upwork up to 48 hours to approve your profile. Keep in mind it can also take time to land your first freelance gig.Payment varies by site. On Upwork the timeline for receiving earnings depends on the type of payment. Hourly contracts have a weekly billing cycle and you can withdraw funds 10 days later. Fixed-price contracts have a five-day waiting period after reaching a milestone. On Fiverr, you're paid when the work order is complete, but you can't withdraw funds for 14 days. (The waiting time is shorter for Top Rated Sellers.)RequirementsUpwork and Fiverr require users to be at least 18 to sell work. Fiverr allows users age 13 and older to use a parent or guardian’s account, with permission. And Freelancer.com requires users to be at least 16.2. Test websites and appsAnother way to make money from home is on sites like UserTesting.com. You get paid for your thoughts on how well — or not so well — certain websites and apps work. You’ll have to complete a short test to be accepted by UserTesting, then you’ll be paid depending on the test type.Total time: Approval can take a few days.Setup: Less than an hour.How easy to start: Easy, if you have the tech gear and complete a sample test.Age threshold: 18+.How fast you'll get paid: Usually after 14 days.Need to knowYou need to complete a sample test as part of the UserTesting application process.You will start receiving testing opportunities after your application is approved.The timeline for approval can vary.Payment amounts vary based on the length of the tests. You get paid 14 days after completing a website or app test via PayPal.RequirementsYou need to be at least 18.You need a device that meets UserTesting’s requirements, internet connection and microphone.The practice test and most user testing requires English, German or French; some test opportunities may be in additional languages.3. Learn to use AI toolsGenerative artificial intelligence is so hot right now. Research from PwC estimates that the North American economy will see a $3.7 trillion impact by 2030, thanks to the AI market.It's a good time to learn how to make money by using AI tools. Some AI-related side hustles include:Integrating AI tools as a freelancer, to help you create digital products or to edit AI content for a client.Improving your advertising, marketing efforts and management of your existing small business.Teaching others to use AI tools.Total time: Depends on demand.Setup: Around 24-48 hours if using a site like Upwork or Freelancer.com.How easy to start:  If you’re already familiar with AI tools, it will be easier to get started.Age threshold: 16+ for Freelancer.com and 18 for Upwork.How fast you'll get paid: Varies by client or the number of products you sell and your chosen platform.Need to knowGive yourself time to get familiar with using AI tools.You’ll need to meet the requirements of the freelance gig site you choose.Payment will depend on your client and the site’s terms and conditions.RequirementsYou’ll need a computer and an internet connection.4. Take surveys for moneyYou can make money from home by taking online surveys, but don’t expect to earn a lot. Survey sites don’t typically offer a big payoff, and many sites are more useful for earning gift cards than cash.Some of the more popular survey sites include Swagbucks and Survey Junkie. Read about how little we made with survey sites to find out which one might be best suited for you.Total time: It will take a while.Setup: Just minutes.How easy to start: Very. Just register and begin.Age threshold: 13 to 18+, depending on the site.How fast you'll get paid: Varies by site.Need to knowSurvey sites could be an option for how to make money online for beginners because you can register with a site and start taking surveys in a matter of minutes.The time it takes to get paid depends on the survey site and how much time you dedicate to taking surveys.Some sites let you cash out only after you hit a minimum earnings threshold.Other survey sites issue points, which can be redeemed for cash (via PayPal) or gift cards.RequirementsMost survey sites have a minimum age requirement, which ranges from 13 to 18 (depending on the site) making these sites one idea for teens to make money online.Individual surveys may have specific requirements. Don't be surprised if you are disqualified from a survey without much explanation.5. Make money from your blog with affiliate linksIf you’re a blogger who gets decent traffic, you could make money by joining an affiliate network. Affiliates get paid when someone clicks through from the website to the partner site and buys something there.Some bloggers make a lot of money this way, particularly those who do affiliate marketing full-time. You can use social media or a platform like Pinterest to drive traffic to your blog. Read more about affiliate marketing and other ways to make money blogging.Total time: It can take quite a while to build an audience.Setup: With blog templates, building a site is easy.How easy to start: While getting started can be easy, creating regular content may be another matter.Age threshold: Varies.How fast you'll get paid: A month or two, on average.Need to knowFirst, you need a blog, social media account or other online presence that draws a healthy number of visitors each month.Then, you need to apply for and be approved by an affiliate marketing network like CJ, ShareASale, FlexOffers, Rakuten Advertising or Amazon Associates.Payment schedules and thresholds vary by affiliate network, but expect to wait at least a month or two for your first paycheck.Amazon Associates pays out earnings 60 days after the end of the calendar month in which they were earned.ShareASale disburses earnings monthly.RequirementsA blog, social media account or other online presence that attracts a steady stream of visitors.6. Sell your wares on EtsyHave a penchant for woodworking, jewelry-making, embroidery or pottery? Sell your crafts on Etsy, the go-to site for artisans selling home goods, art and knickknacks. According to Etsy, the company has more than 95 million active buyers. Learn more about how to make money on Etsy.Total time: It might take quite a while for customers to find you.Setup: Can be quite involved.How easy to start: Leaning toward hard on the difficulty meter.Age threshold: 13+.How fast you'll get paid: Daily, weekly, biweekly or monthly, depending on your preference.Need to knowOpening an Etsy shop is the easy part. It can be done in a few hours.You need merchandise to sell, photos and descriptions to post, a name for your shop and a business plan to help you succeed. Once that’s done, you’ll still need to find customers.Once you sell an item, payment is deposited into your Etsy Payments account first, then to your bank account depending on your desired deposit schedule.RequirementsIf you’re over 13 years old but under 18, you can sell on Etsy but would be considered a minor and must follow extra policies.You need to have all necessary intellectual property rights to the merchandise sold in your shop.7. Self-publish an e-bookWriting a good book is tough, but the internet makes it easy to bring it to market. If you’re a writer who can churn out pages, you can use Amazon’s Kindle Direct Publishing to sell your books(s) on the Kindle store. It’s free to publish a book, and you can earn up to 70% of each sale in royalties. Write your book, enter a clear description and the details to be displayed and upload your manuscript. Set the price and see if it sells.Total time: How fast can you type? We don’t have to tell you writing a book can be a slog.Setup: Quick and easy on KDP once the book is ready.How easy to start: Just start writing.Age threshold: 18+, but parents and guardians can use their accounts to sell minors’ books.How fast you’ll get paid: Monthly. You'll need to meet a $100 threshold for wire or check payments.Need to knowJust because it’s simple to self-publish doesn’t mean your book will sell. Competition is high with millions of e-book titles on the Kindle Store.Choose one of two royalty options: 70% or 35%. You’ll have to price your book between $2.99 and $9.99 if you select the 70% option. You have more pricing flexibility when you pick 35%.RequirementsYou need to create a Kindle Direct Publishing account to get started.Proper formatting is important. Amazon says most Microsoft Word documents convert to e-books easily, but other formats are also supported.Take control of your finances with the NerdWallet appOur app tracks your spending, credit score, net worth and more — so you have a clear view of your day-to-day and long-term finances.8. Get advertising revenue from your blog or YouTube channelIf your YouTube videos or blog posts draw an audience, you may be able to make money from advertising. YouTube sets 1,000 subscribers as the benchmark for applying to the YouTube Partner Program if you want to place ads on your channel.You can apply with 500 subscribers for other monetizing features like channel memberships. You can also use Google’s AdSense, the same ad platform on YouTube, to put relevant ads on your blog or website for earning potential. Read more about how to make money on YouTube and Google AdSense.Total time: It can take several weeks to get up and running.Setup: Fairly easy.How easy to start: Depends on how good you are at producing interesting videos.Age threshold: 18+.How fast you'll get paid: Could take a long while to earn the first payout; then monthly.Need to knowSigning up for Google AdSense is pretty easy, but to use AdSense with YouTube, you’ll need to be part of the Partner Program.You can use AdSense on a website or blog with fewer eligibility requirements.Allow at least two months for ad revenue to start trickling in.You need to earn at least $100 before you're eligible for a payout.Once you hit the $100 threshold, earnings are issued between the 21st and 26th of the following month.RequirementsYour own website that has been active for at least six months.For YouTube, you need at least 1,000 subscribers and to meet requirements related to views or watch hours.You must be at least 18.9. Become an Instagram influencerCompanies are using Instagram influencers — people with large, dedicated followings on the platform — to rep their products. You can get in on the action by applying for opportunities via a marketing platform like Open Influence or Aspire, or by contacting the brands you want to work with. You can also make money on TikTok this way.Total time: You'll need to stick with it.Setup: Quick and easy.How easy to start: Not that easy. Read: Must build following to gain influence.Age threshold: 13+.How fast you'll get paid: Varies on partnerships.Need to knowCreating an Instagram account is quick, but building a following can take months or even years.Once you have the numbers, you'll need to find paid opportunities. You can do this via affiliate networks or by pitching brands you want to work with.The time to receive your payment will depend on the terms of your agreement, but affiliate networks typically pay out earnings the month after a campaign is completed.RequirementsAn Instagram account with a dedicated, engaged following.You'll also need to meet the requirements of any affiliate network.10. Monetize your Twitch channelGaming could be a way to make money from home if you have a steady following on Twitch, the go-to site for gamers. Streamers can receive money from viewers’ virtual cheers, or “Bits,” and even get a share of subscription and ad revenue if they reach Affiliate or Partner status. Learn more about how to make money on Twitch.Total time: This can be a long game.Setup: Quick and easy.How easy to start: Easy to start; takes a while to build a following.Age threshold: 13+.How fast you'll get paid: Monthly.Need to knowYou can launch a Twitch channel and start streaming in a day, but it will take weeks or even months to build a following.Subscription and ad revenue earned as a Twitch Partner or Affiliate is paid out around the 15th of every month, and you must have a balance of at least $50 for most payout methods (it's $100 for wire transfers).RequirementsYou need to hit certain viewership and broadcast milestones to become a Twitch Affiliate or Partner and qualify for a share of game sales, ads and subscription revenue.» MORE: How to make money as a kid11. Sell your photographyTurn your photographs into cash via sites like Fine Art America, which lets you upload your images to sell as prints, T-shirts, phone cases and more. Other marketplaces for photographers include SmugMug, 500px and PhotoShelter. Some sites require a subscription but may provide features ranging from cloud storage to password-protected galleries and a customized website.What the Redditors say: Success selling photos requires both high-quality content and a bit of business savvy around rights management and pricing. A general theme is that you may do better by forming direct relationships with buyers than purely relying on stock sites.Total time: Buyers need to find you — and like your work.Setup: Just a few hours.How easy to start: If you have a library of photos, you're on the way.Age threshold: Varies.How fast you'll get paid: Depends on your sales platform.Need to knowYou can set up a profile with sites like SmugMug, PhotoShelter or Fine Art America in a few hours, assuming you have a body of original work.Payment varies widely depending on the site.Fine Art America: Payment issued after 30-day return window expires. Sent on the 15th of each month.PhotoShelter: Payment issued at time of sale to your chosen payment method (PayPal, Stripe, etc.).SmugMug: You can request payment be issued the following month if you have a balance of at least $5.RequirementsRequirements vary by site, but you need to have all necessary rights to the images you sell.How to make money from homeSome side hustles don't even require you to leave the house. Or if they do, it might just be a short walk around the block with a furry friend. Working from home requires a little creativity and a stick-to-it spirit. Here are some excellent ideas for side gigs from home:12. Become a dog walker with Rover or WagLove dogs? Choose dog walking as a beginner's way to make money. Apps like Wag and Rover offer on-demand dog walking, so you can pick up walks when your schedule allows. If you have space (and your landlord’s permission, if you rent), you could offer overnight dog boarding. Read the fine print if you sign up for these services.What Redditors say: There's potential to earn an extra $300+ per month with a gig service like Rover when you have regular clientele, but success can depend heavily on location and market. Are dogs trending in your town?Total time: Building a client base may take some time.Setup: Can take a few weeks to be approved.How easy to start: Love pets? You're good to go.Age threshold: 18+.How fast you'll get paid: Two days to a week.Need to knowIt takes about 5 to 10 business days for your Rover profile to be reviewed and approved.The application process for Wag takes about two weeks and you must pass a background check and pet care quiz.RequirementsFor Rover or Wag, you’ll need to live in an area where the service operates.If you want to pet-sit in your own home, you’ll need an apartment or house that allows pets.You’ll have to pass a background check.13. Sell unused gift cardsMake extra money by selling unused or partially used gift cards on a site like CardCash or GiftCash. CardCash notes it will pay you up to 92% of the card’s value, or you can trade in your card for one you’ll use. Read more about what to do with unwanted gift cards.Total time: In minutes if your gift card is for a popular store.Setup: Easy.How easy to start: The more gift cards you have to sell, the better.Age threshold: 18+.How fast you'll get paid: A few days to about two weeks.Need to knowYou can get an instant offer or quote via sites like CardCash and GiftCash.You can sell gift cards at kiosks and participating retail locations to get cash the same day, or try to sell them online. The latter takes longer, but you may get a better offer for your gift card.RequirementsYour gift card may need to meet a minimum balance to be resold. Not all cards will generate offers.Gift cards with expiration dates may not be eligible.14. List your spare bedroom on AirbnbRenting out your home or spare bedroom on vacation rental sites is another way to make extra money. Be prepared to spend some money to clean and keep up the property, replace home goods and pay toward service fees. And scrutinize your rental agreement, HOA rules and zoning or other restrictions before you get started. Learn more about how to start an Airbnb business.Total time: Demand drives success, and that depends on your location.Setup: A listing can be created and live in hours.How easy to start: If you have a place to rent, it's a simple process.Age threshold: 18+.How fast you'll get paid: A day or more after check-in.Need to knowYou can create a listing and start accepting reservations on the same day.Payment is typically disbursed about 24 hours after your guest’s scheduled check-in time, but processing time for that payment depends on the payout method.RequirementsComply with any rules governing short-term or vacation rentals in your property, including city ordinances and rules issued by your landlord, condo board or homeowners association.How to make money offlineThere's online and at-home ways to make extra money — and then there's a third alternative: offline. This version of the gig economy may require more work, but the upside can be substantial. Since there’s no escaping the internet these days, some of these offline methods do have online components:15. Sell your gently used clothesA woman makes extra money by selling her clothes.Selling clothes you no longer wear is a quick way to make some money. Start with local consignment shops to make money quicker or use sites like ThredUp and Poshmark to find buyers. When listing items online, be sure to take clear, well-lit photos of your pieces and research similar items to set competitive prices. Get tips on how to sell your clothing.Total time: Varies by sales channel.Setup: Easy and fast. You can simply go to a consignment shop or fill a box with clothes and send it in.How easy to start: Easy. Cleaning out the closet may be the hardest part.Age threshold: 13+.How fast you'll get paid: Varies by sales channel.Need to knowYou can sell used clothing and accessories several ways, but they're all pretty quick to start.Fast: A brick-and-mortar consignment store like Plato's Closet will give you cash on the spot.Medium: Other in-person and online consignment shops pay you when your items sell, or when they receive and inspect your items. Either way, allow at least a month for your payout.RequirementsGently worn shoes, clothing and accessories.Items will go through various inspections before being accepted. For example, ThredUp checks items for pilling, fading, shrinkage, missing parts (like buttons) and stains.16. Trade in old phones, electronics for cashHave an old phone, iPad, laptop or gaming system lying around? Sell it on a site like Swappa, Gazelle or Facebook Marketplace. Check out Amazon’s trade-in program, which pays participants in Amazon gift cards — and eBay, too. If you’re in a rush, try an ecoATM kiosk, which offers cash on the spot for your device.Total time: Lots of options, so your time spent will vary.Setup: A breeze.How easy to start: Easy, especially if your device is in good shape.Age threshold: Typically 18; check terms of service.How fast you'll get paid: Varies by where you sell.Need to knowSelling directly (Swappa, OfferUp, Facebook Marketplace): In most cases, you take photos of the phone, verify the electronic serial number is clean and post your listing. Some sites review and approve postings, but the time is minimal. Fees vary. Swappa, for example, charges a 3% seller fee.Selling to reseller (Gazelle): Answer a few questions online for an instant quote. Then send in your device and get paid once the company confirms its condition is as described.Selling directly: When you get paid depends on how quickly your phone or device sells. Once the item sells, payment is fast.RequirementsA used phone, laptop, gaming system, etc.Cell phones: You need to verify the phone is not stolen or under a repayment plan. Check terms of service for additional requirements, such as no activation lock.17. Get a babysitting gigEveryone from college students to recent retirees can make money by watching other people’s children. Word-of-mouth referrals from friends and family are still a great way to get started, but you can also create a profile for free on Care.com or Sittercity to expand your reach. Note any specialized skills, such as CPR certifications, to make yourself more marketable.Total time: Online setup takes minutes; neighborhood referrals may take a while.Setup: Just minutes.How easy to start: Getting the word out is the main thing.Age threshold: Very young if you're using referrals. 18+ online.How fast you'll get paid: When the parents come home.Need to knowYou can create a profile on Care.com or Sittercity in a matter of minutes.You typically get paid when you complete your gig, whether by a service or direct from the customer.RequirementsYou need to be at least 18 to list as a caregiver on Care.com and Sittercity.Clients may request a background check.18. Rent out your carCity-dwellers often don’t use their cars for days or weeks at a time. That idle time can translate to extra money with services like Getaround and Turo, which let you rent out your car by the hour or day. You take home the majority of those earnings, while Getaround or Turo takes a cut for protecting your car while it’s being rented.Total time: Demand for your car will depend on the local market.Setup: It takes about a half hour to set up an account.How easy to start: With an appropriate vehicle, it's easy.Age threshold: 21+ with a valid driver's license for Turo; Getaround does not list an age requirement.How fast you'll get paid: Varies by site.Need to knowYou can create a listing on Turo or Getaround in under 30 minutes.Turo initiates payment within three hours of the end of the rental, but you can expect it to take a few days for your bank to process the deposit. (This is the case for all trips after the first one, which takes a few days for Turo to send.)Getaround rental earnings accrue daily or monthly. Payments are made via direct deposit.RequirementsIf you lease your car, check the terms of your agreement and financing documents to make sure you’re allowed to share it.Your car must meet certain requirements (make/model/year/mileage) and satisfy maintenance and safety standards. You may also be asked to agree not to list on other platforms.19. Sign up for TaskRabbitIf you actually enjoy putting together Ikea furniture or standing in long lines, you may be cut out for doing tasks for others. Websites like TaskRabbit can connect you with people who need help with a variety of things, such as moving, cleaning, delivery and handyman services. The site also offers several virtual and online tasks, such as helping with a research project or data entry. Read about how to make money with TaskRabbit.What Redditors say: This is a flexible side hustle that can be good for a couple hundred bucks of supplemental income per month. But, like with other gig service sites, your success is dependent on location and demand.Total time: Local demand for your skills will determine the time you spend.Setup: A couple of hours, then some time for approval.How easy to start: Easy, though you'll need to do some research.Age threshold: 18+.How fast you'll get paid: A few days after a job.Need to knowYou can set up your profile and register in a matter of hours, but can't start accepting tasks until your profile is approved by TaskRabbit. This may take a few days.Once approved, you need to pay a $25 fee, so you may first want to research your market and the value of your skills to determine if that fee is worth it to you.You're paid after the task is completed through direct deposit to a checking account. Payment typically takes a few days to appear in your account.RequirementsYou need to be at least 18 to start working with TaskRabbit.Prospective Taskers must also pass a background check.20. Become a private tutorParlay your math, science, foreign-language or test-prep expertise into a lucrative side gig by becoming a private tutor. You can tutor people online or in-person.What you charge can depend on your experience, expertise and what’s in demand. To get started, see what types of tutors are needed on Craigslist, or create a profile on sites like Tutor.com or Care.com. You can also advertise your services at local schools and community centers.Total time: Varies by subject matter. Some companies might require a minimum availability per week (e.g., Tutor.com requires 5 hours).Setup: Can be a bit involved.How easy to start: Students will have to find you, and that might take a while.Age threshold: Any.How fast you'll get paid: Depends on the platform; check the terms of service.Need to knowStartup time depends on demand in your area. It could take a while before you get your first student.If you haven't tutored before, you'll want to allow for time to prep so students feel like they're getting the most out of their time with you.How quickly you get paid depends on whether you tutor via a platform or in-person; either way, it likely won't take long.RequirementsYou'll need deep knowledge in an area that people need help understanding, like mathematics, a foreign language or test prep.Educational requirements might apply. Some tutors might be required to be currently enrolled in a four-year university or have at least a bachelor's degree from an accredited four-year university.21. Drive for Uber, LyftJoin Uber or Lyft (or both) and make money by driving passengers around. Just don’t forget to factor in gas and maintenance costs. You need an eligible car in good condition and must agree to a background check and a review of your driving history. Learn how to become an Uber driver or how to make money as a Lyft driver.Total time: Depends on your market demand.Setup: A few weeks.How easy to start: Not difficult, but you'll need the right type of vehicle.Age threshold: Varies by region from 21-25.How fast you'll get paid: Very fast. Either instantly or within days.Need to knowAllow some time for the application process, background check and car inspection.Lyft and Uber can pay you instantly through a debit card or transfer earnings to your bank account pretty quickly.RequirementsA car with four doors. It must also meet other requirements, such as year, physical condition, etc.Depending on your state, you may need to have at least one year of licensed driving experience to drive for Lyft. Uber requires at least one year of licensed driving experience in the U.S. (or three years if you’re under 25).Let your car insurance company know of your plans before you start driving.Nerdy PerspectiveDriving for Uber was not my favorite side hustle, but it was accessible and the little money I made over a week-long test came quickly. I'd be worried about gas costs, wear and tear on my car, and lots of awkward silence if I were to do it long term, though. I was happier when I delivered food and groceries. I delivered with DoorDash and became a full-service Instacart shopper for short stints in 2024, and found these driving gigs to be less stressful than doing rideshare. Trips were shorter, I spent less time in the car and it was easy to get started, even in my small town.Profile photo of Tommy TindallTommy TindallI've tried driving gigs22. Make deliveries for Amazon, Uber EatsTake advantage of the growing delivery trend and sign up for a service like Instacart, Uber Eats, Postmates, DoorDash or Amazon Flex. You get paid per delivery, in most cases, and can even earn tips. A car isn’t always required — Postmates and DoorDash let you use a bike or scooter to make deliveries in some cities. However, a background check is almost always part of the deal. Learn more about how to get started with Amazon Flex, Uber Eats and Instacart.Total time: Depends on your market demand.Setup: About a week.How easy to start: Easy, if you have dependable transportation.Age threshold: Varies by the service, but at least 18.How fast you'll get paid: Varies by vendor.Need to knowThe background check can take a few days, and timing can vary.Payments from these services also vary, but are generally issued weekly or quicker.RequirementsYou'll need a way to deliver items. It could be a car, scooter or bike, depending on the service.A smartphone is necessary to accept and process jobs.Each delivery service has a minimum age requirement, but it varies by service.23. Find work as a housesitterIf you’re willing to watch someone’s home — and maybe feed the pets, water the plants and take out the garbage — become a housesitter. Tap your personal network for referrals or try out HouseSitter.com, which connects homeowners with housesitters.Total time: Depends on your market demand.Setup: Minutes — or more if you try to drum up business by referrals.How easy to start: That can depend on the need in your area.Age threshold: Varies by site.How fast you'll get paid: Typically at the end of a gig; make arrangements with clients.Need to knowYou can create a profile on HouseSitter.com in a matter of minutes, though it may take time to secure your first housesitting gig.You typically get paid by the homeowner when you complete your gig.RequirementsMost sites have an age requirement.24. Sign up to be a mystery shopperBusinesses often want to know how they’re performing from a customer’s perspective. Sign up to be their eyes and ears. You can apply online via sites like IntelliShop, BestMark and Sinclair Customer Metrics. Just beware of scams and do thorough research before signing on.Total time: Varies by site.Setup: Applying takes little time, but approval can take a while.How easy to start: Relatively easy if you have required transportation and tech.Age threshold: May vary by site.How fast you'll get paid: Varies by company.Need to knowThe application process is typically quick, but then it's in the company's hands. It can take days, or more, to assess your application, depending on demand.Payout timing and method vary by company. BestMark, for example, issues payments monthly.RequirementsMost mystery shopping services have an age requirement. You have to be at least 18 to shop for BestMark.Depending on the service, you may need internet access.25. Put your drone to workSome of the best camera drones can cost less than $500 — and you can use that investment to make money. Real estate agents turn to drone pilots to generate aerial photos of a home's exterior, and even neat fly-through videos of interiors, which can translate to a relatively easy money-making venture.If you're willing to learn more advanced skills, like drone mapping, you can often charge more for clients seeking aerial inspections and land mapping.You need to pass a test to become a drone pilot and register your drone with the Federal Aviation Administration. Then, you can apply for flying gigs.Total time: Depends on demand.Setup: You'll need to make time to pass a test, and then find clients.How easy to start: If you already have a drone, you're likely qualified.Age threshold: 16+.How fast you'll get paid: Varies by company.",
                                  "producing activism Activism consists of efforts to promote, impede, direct or intervene in social, political, economic or environmental reform with the desire to make changes in society toward a perceived common good. Forms of activism range from mandate building in a community (including writing letters to newspapers), petitioning elected officials, running or contributing to a political campaign, preferential patronage (or boycott) of businesses, and demonstrative forms of activism like rallies, street marches, strikes, sit-ins, or hunger strikes.Activism may be performed on a day-to-day basis in a wide variety of ways, including through the creation of art (artivism), computer hacking (hacktivism), or simply in how one chooses to spend their money (economic activism). For example, the refusal to buy clothes or other merchandise from a company as a protest against the exploitation of workers by that company could be considered an expression of activism. However, the term commonly refers to a form of collective action, in which numerous individuals coordinate an act of protest together.[1] Collective action that is purposeful, organized, and sustained over a period of time becomes known as a social movement.[2]Historically, activists have used literature, including pamphlets, tracts, and books to disseminate or propagate their messages and attempt to persuade their readers of the justice of their cause. Research has now begun to explore how contemporary activist groups use social media to facilitate civic engagement and collective action combining politics with technology.[3][4] Left-wing and right-wing online activists often use different tactics. Hashtag activism and offline protest are more common on the left. Working strategically with partisan media, migrating to alternative platforms, and manipulation of mainstream media are more common on the right (in the United States).[5] In addition, the perception of increased left-wing activism in science and academia may decrease conservative trust in science and motivate some forms of conservative activism, including on college campuses.[6] Some scholars have also shown how the influence of very wealthy Americans is a form of activism.[7][8]Separating activism and terrorism can be difficult and has been described as a 'fine line",
                                  ]# treat this as a document
        print('3 possible strats which might be sub divided strata ')
        print('#0 is helping peoplp')
        print('#1 is making the most money')
        print('#2 is producting activism')
        sorted_life_action_dic_for_objective={}
        final_all_sorted_life_action_for_objective_dic_list=[]
        objective_sub_task_list_list=[[],
                                      [],
                                      []]                                                             
        sorted_life_sub_action_lists_for_objective_list=""
        import numpy as np
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
        previous_patterns_add_versus_not=[]
        patterns_for_placing_actions_via_objectives=[]
        previous_paragraph_patterns=[]
        sub_action_person_comp_info_dic_with_action_list_2=[]
        print('add_sub_actions_to_list_sorted_by_objective_break_up_if_two_actions_cant_be_completed')
        intital_page_text=person_comp_info_dic_with_action1["intital_page_text"]
        action_objects_list=person_comp_info_dic_with_action1["action_objects"]
        action_problem_environemnt_context=" ".join(action_objects_list)
        action_problem_environemnt_context=intital_page_text+action_problem_environemnt_context
        testing1=False
        testing2=True
        filee=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\strategies\test_pickle.pickle"
        if testing2!=True:
            for sub_action_dic in sub_action_person_comp_info_dic_with_action_list:# these are all the sub actions with other context info
                #input(f"sub_action_dic {sub_action_dic}")
                print('part 1 decide whether to include the sub task or not as a action in strat and fill and save the dictionary') 
                print(f"sub_action_person_comp_info_dic_with_action_list {sub_action_person_comp_info_dic_with_action_list}")
                #input()
                includee=self.use_problem_envrionment_to_decide_whether_to_add_sub_task_or_not(sub_action_dic,action_problem_environemnt_context,stop_words)# this has the problem galaxy to help us to decide to keep an action
                if includee==False:
                    continue
                filled_sub_action_dic=self.fill_and_save_sub_action_dic(sub_action_dic)
                sub_action_person_comp_info_dic_with_action_list_2.append(filled_sub_action_dic)
                if testing1==True:
                    print('TESTING IS TRUE RIGHT NO NEED TO TURN THIS OFF')
                    break 
                if testing1!=True:
                    print('testing is falsse we good')
                    continue
                
        if testing1==True:  
            print('TESTING IS TRUE TURN THIS OFF for production  ')
            with open(filee, 'wb') as file:
                pickle.dump(sub_action_person_comp_info_dic_with_action_list_2, file)
        
        if testing2==True:
            print('TESTING 2 IS TRUE TURN THIS OFF for production  ')
            with open(filee, 'rb') as file:
                sub_action_person_comp_info_dic_with_action_list_2 = pickle.load(file)
                   
        #working here now need to ge thtis to run through
        # and do the math adn rank the 
        # pickle this and load it for faster testing?
    
        print('part 2 get the score  of the action relative to each objective and store the score')
        for obejctive_doc in prompt_objectives_to_score_list:         
            for sub_action_dic in sub_action_person_comp_info_dic_with_action_list_2:                
                root_action=person_comp_info_dic_with_action_list['action']# this is the main action dic
                guide_person_life_action_list_score=self.create_document_similarity_score(sub_action_dic,obejctive_doc,typee="get_guides_life_action_list_score_for_objective")
                # compare sub action against action
                sub_action_compared_to_main_action=self.create_document_similarity_score(sub_action_dic,person_comp_info_dic_with_action,typee="get_user_perosnal_info_score_for_guide_personal_info")
                # compare other qualtites of sub action against objective
                action_with_respect_to_objective_score=self.create_document_similarity_score(sub_action_dic,obejctive_doc,typee="get_action_list_score_for_objective")             
                print('STILL NEED TO WRITE THIS ONE use random qualtities we have')
                other_qualities_score=self.create_document_similarity_score(sub_action_dic,obejctive_doc,typee="use_all_qualtities_of_input_data_strategies_and_personal_info_in_different_ways_to_help_rank_action")            
                time_to_complete_action=sub_action_dic["time_to_complete_action"][iterr]
                monetary_cost_of_action=sub_action_dic["monetary_cost_of_action"][iterr]      
                money_to_complete_action_score,time_to_cmplete_action_score=self.consider_factors_such_as_time_to_complete_action_monetary_roi_cost_of_action_and_action_effects(time_to_complete_action,monetary_cost_of_action)# like know enemy can do x actions so to avoid getting back stabbed do y
                # done is the one one above              
                action_location_data_dic_list=sub_action_dic["action_geo_locations"][iterr]
                action_location_data_dic_list=action_location_data_dic_list[1:-1].split(",")
                print('only consider the numeric distance of the action location here')
                place_of_people_and_things_score=self.consider_numeric_distances_and_placement_of_other_people_places_and_things_when_choosing_action_use_map(action_location_data_dic_list)
                # done the above
                print('use lemma and make it so good for exaxct word matches works need to write these algorhim and gahter the data ')               
                # look at all the actions past data stuff
                user_past_actions_list=sub_action_dic["user_past_actions_list"][iterr]
                user_past_actions_list=user_past_actions_list[1:-1].split(",")


                user_time_past_use_of_action_list=sub_action_dic["user_time_past_use_of_action_list"][iterr]
                user_time_past_use_of_action_list=user_time_past_use_of_action_list[1:-1].split(",")
                numer_of_last_use_of_action_score,time_from_last_use_of_action_score,proxmity_of_action_to_other_past_used_action_score=self.use_patterns_in_strategies_help_rank_action(user_past_actions_list,user_time_past_use_of_action_list,sub_action)# like previous strategies data used etc 
                #done still need to write it but idea is there
                resources_required_for_action_context=str(sub_action_dic["resources_required_to_perform_action"][iterr])
                personal_resources_context=str(sub_action_dic["assets"][iterr])
                resources_score=self.consider_distance_of_resources_you_have_avilable_to_you_vs_resources_required_to_take_action(resources_required_for_action_context,personal_resources_context)
                print(' the inputs are generaqted up top for this function consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action')
                #current_life_action_list=sub_action_dic[linkkkkk]
                other_people_postiion_score,other_people_available_action_score=self.consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action(str(current_life_action_list), sub_action_dic,person_organizaion_position_list_dic,person_organizaion_action_list_dic)                    
                weights = [14.424, 14.421, 14.417,11.324,11.324,11.324,11.324,-2.324,100.324,100.324,100.324,100.324,100.324]
                # make the distance of things score negative
                # money and time most valuable factors
                amount = [guide_person_life_action_list_score, 
                          action_with_respect_to_objective_score,
                          numer_of_last_use_of_action_score,
                          time_from_last_use_of_action_score,
                          proxmity_of_action_to_other_past_used_action_score,
                          other_people_postiion_score,
                          other_people_available_action_score,
                          resources_score,
                          place_of_people_and_things_score,
                          money_to_complete_action_score,
                          time_to_cmplete_action_score]
                weighted_avg_score = np.average(amount, weights=weights,axis=0)
                # save the weight values and the weight averages
                # need to create sub lists
                print('need to create proper life_sub_action_lists to get this to work')
                sorted_life_action_dic_for_objective[weighted_avg_score]=[life_action,life_sub_action_lists,effects,obejctive_doc]
                # save every 5 because wont probably get throguh all sub actions
                # save the dic with score for the objective
                
            print('each tuple output of sorted is the key as item zero and then values in values as subsequent items')
            sorted_life_action_tuple_for_objective=sorted(sorted_life_action_dic_for_objective.items(),reverse=True)
            sorted_life_action_tuple_for_objective=sorted_life_action_tuple_for_objective[:20]# show top 10 hits
            print(sorted_life_action_tuple_for_objective)
            print(' decide how to split and order actions in the objective sorted list so they seem better organized and understandable and usable')
            sorted_life_action_tuple_for_objective=self.use_previous_paragraph_structures_to_order_sub_task_in_strat(sorted_life_action_tuple_for_objective, previous_paragraph_patterns)# need a nn for this   
            #add each all sorted life action for object 
            objective_sub_task_list_list.append(sorted_life_action_tuple_for_objective)
        return objective_sub_task_list_list
        print('''super imporant to consider other plahyers moves! think sc2 and civ pro
                      by anticipating other peoples moves then limit their future moves with your moves you can better precift their future move
                      then can counter this move and beat them''')
                      
                      # other peoples available actions are all their life action lists
                      # create life action context for each indivudal person/org/link
                      # link is key   
    def create_sub_actions_for_action_2(self,page_text,person_comp_info_dic_with_action1):
        
        """ """
        import re
        substep_list=str(page_text).split(".")  
        return  substep_list
    
        
        
        
    def create_sub_actions_for_action(self,page_text,person_comp_info_dic_with_action1):
         linkk=page_text[1]
         print(linkk)
         sub_action_person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page(page_text[0],linkk)
         sub_action_list_list=self.fill_saved_sub_action_dic_and_order_and_divide_actions_into_action_lists(sub_action_person_comp_info_dic_with_action_list,person_comp_info_dic_with_action1)# it is filled in here so use all the qualtites to sort and divide up the adrtion
         return sub_action_list_list
        
    
    def pre_process_text(self, saved_text_from_website):
        """ what is needed to reduce the size and make the text consistent before it goes in the network"""
        import re
        import unicodedata
        """ remove extra spacing, names, tabs, and other unwanted values"""
        website_data= re.sub("\n"," ", saved_text_from_website)
        website_data= re.sub("\t"," ", website_data)
        website_data= re.sub("\r"," ", website_data)
        website_data=re.sub(r" \s+", r" ", website_data)
        website_data= re.sub(r"\\x\S+",r" ",website_data )
        website_data= re.sub(r"@", "",website_data)

        website_data= unicodedata.normalize("NFKD",website_data)
        return website_data
        # repeat for law_document
    def divide_text_into_sentences(self,website_data):
        """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
        from nltk.tokenize import sent_tokenize
        # can add neural network here when i feel more comfortable
        # divide into sentence non sentence here
        import re
        index_used_list=[]
        self.sentences=[]
        final_sentence_list=[]
        find_word_pattern = re.compile(r"\w+")
        #from nltk.tokenize import word_tokenize
        modifying_sentences = sent_tokenize(website_data)
        for i7, sentence_15 in enumerate(modifying_sentences):
            words_in_current_sentence=find_word_pattern.findall(sentence_15)
            if len(words_in_current_sentence)<4: 
                print(sentence_15)
                continue
            if len(words_in_current_sentence)>60: 
                print(sentence_15)
                continue
            if "https" in sentence_15:
                print(sentence_15)
                continue
            else:
                final_sentence_list.append(sentence_15)
        return final_sentence_list 
    def label_text_with_spacy(self,website_text): 
     """ generate spacy information for a sentnece"""
     import spacy
     sentence=website_text.replace("'","").replace(",","")
     if self.spacy_switch==0:
         self.nlp = spacy.load("en_core_web_sm")
         self.spacy_switch=1
         #https://github.com/explosion/spaCy/issues/12659
         #python -m pip install -U pydantic spacy
         #python -m spacy download en_core_web_sm

     doc = self.nlp(sentence)
     noun_chunks = [chunk.text for chunk in doc.noun_chunks]
     entities = [(ent.text, ent.label_) for ent in doc.ents]
     sentences = [sent.text for sent in doc.sents]
     lemmatized_tokens = [token.lemma_ for token in doc]
     pos_tags = [(token.text, token.pos_) for token in doc]
     return {
         "noun_chunks": noun_chunks,
         "entities": entities,
         "sentence": sentence,
         "lemmatized_tokens": lemmatized_tokens,
         "pos_tags": pos_tags}


    def get_objects_and_qualitites_of_objects_in_sentence(self,spacy_dic,person_comp_info_dic_with_action):
         """get the intital objects and qualtites in the sentnece """
         import re
         cleaned_noun_chunk_list=[]
         for noun_chunk_number, noun_chunk in enumerate(spacy_dic["noun_chunks"]):
             words_in_noun_chunk=re.split(r" ",noun_chunk)
             cleaned_noun_chunk=""
             for word_placement_value, worddd in enumerate(words_in_noun_chunk):
                 
                 try:
                     index_of_word=spacy_dic["text_only_tags"].index(worddd)
                 except:
                     print(f"{worddd} NOT FOUND")
                     continue    
                 poss=spacy_dic["pos_only_tags"][index_of_word]
                 if poss =="NOUN" or poss =="PROPN":
                     cleaned_noun_chunk+=f"{worddd} "       
             cleaned_noun_chunk=cleaned_noun_chunk.strip()            
             if cleaned_noun_chunk=="":
                 continue
             cleaned_noun_chunk_list.append(cleaned_noun_chunk)
             
             # create qualtities of object here
             # add subsequent noun chunk
             if cleaned_noun_chunk not in person_comp_info_dic_with_action["action_objects"]:
                 person_comp_info_dic_with_action["action_objects"][cleaned_noun_chunk]={"qualtity_list":[],"transformation_list":[]}
             if noun_chunk_number!=len(spacy_dic["noun_chunks"])-1:
                 # if last noun chunk then dont add qualtity
                 if spacy_dic["noun_chunks"][noun_chunk_number+1] in person_comp_info_dic_with_action["action_objects"][cleaned_noun_chunk]["qualtity_list"]:
                     continue
                 else:
                     person_comp_info_dic_with_action["action_objects"][cleaned_noun_chunk]["qualtity_list"].append(spacy_dic["noun_chunks"][noun_chunk_number+1])# noun chunk after this one
         return person_comp_info_dic_with_action,cleaned_noun_chunk_list
     
        
    def get_transformation_of_objects_in_sentence(self,spacy_dic,cleaned_noun_chunk_list,person_comp_info_dic_with_action):
         """using the dictionary we created to get qual and object now get verbs or transformations for each object """
         current_noun_chunk=""
         #print(spacy_dic)
         #print(cleaned_noun_chunk_list)
         if cleaned_noun_chunk_list:
             for i2, word_tag in enumerate(spacy_dic["pos_tags"]):# skip how do i is why we start at 3 
                 # find associated noun chunk
                 word=word_tag[0]
                 pos=word_tag[1]
                 # determine current noun chunk
                 if pos =="NOUN" or pos =="PROPN":
                     word_prior=None
                     word_after=None
                     current_word=None
                     noun_chunk_score_list=[]
                     current_word=spacy_dic["text_only_tags"][i2]
                     if i2!=len(spacy_dic["text_only_tags"])-1:
                         word_prior=spacy_dic["text_only_tags"][i2+1]
                     if i2!=0:
                         word_after=spacy_dic["text_only_tags"][i2-1] 
                     for noun_chunkk in cleaned_noun_chunk_list:
                         noun_chunk_score=0
                         if current_word in  noun_chunkk:
                              noun_chunk_score+=1
                         if word_prior !=None and word_prior in noun_chunkk:
         
                               noun_chunk_score+=1 
                         if word_after !=None and word_after in noun_chunkk:
                               noun_chunk_score+=1
                         noun_chunk_score_list.append(noun_chunk_score)
                     #print(noun_chunk_score_list)
                     max_noun_chunk_value=max(noun_chunk_score_list)
                     max_noun_chunk_index=noun_chunk_score_list.index(max_noun_chunk_value)
                     current_noun_chunk=cleaned_noun_chunk_list[max_noun_chunk_index] 
                     #current_noun_chunk=cleaned_noun_chunk_list[current_noun_chunk_index]
                     
                 if pos == "VERB" and current_noun_chunk!="":
                     person_comp_info_dic_with_action["action_objects"][current_noun_chunk]["transformation_list"].append(word)    
                     
         return person_comp_info_dic_with_action
     
    def create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(self,spacy_dic,person_comp_info_dic_with_action):
        """ """
        import re
        import copy
        #orignal sentence saved so if want to modify algorhim later i can
        saved_word_word_chunk_cross_reference_dic={}
        cleaned_noun_chunk_list=[] 
        person_comp_info_dic_with_action,cleaned_noun_chunk_list=self.get_objects_and_qualitites_of_objects_in_sentence(spacy_dic,person_comp_info_dic_with_action) 
        person_comp_info_dic_with_action=self.get_transformation_of_objects_in_sentence(spacy_dic,cleaned_noun_chunk_list,person_comp_info_dic_with_action) 
        return person_comp_info_dic_with_action  

    def search_through_patents_to_get_sub_actions(self):
        """ will need to write htis later """
    def create_sub_action_list(self,single_website_text):
        """need to parse website text to create the sub action list for an action """
        sub_action_list=[]
        doc = self.nlp(single_website_text)      
        action_sentence=False 
        sentence_action_type_dic={}
        sentence=""
        counterr=0
        action_sentence_value="not action sentence"
        entity_text_dic={}
        for ent in doc.ents:
            #print(f"{ent.text},{ent.label_}")
            #print('hehe')
            textt=ent.text
            labell=ent.label_
            if " " in textt:
                textt_list=textt.split()
            else:
                textt_list=[textt]
            for textt in textt_list:
                if ent.label_ == "PERSON":
                    entity_text_dic[ent.text]="PERSON"
                if ent.label_ == "ORG":
                    entity_text_dic[ent.text] = "ORG"                
                if ent.label_ == "DATE":
                    entity_text_dic[ent.text] = "DATE"
                if ent.label_ == "MONEY":
                    entity_text_dic[ent.text] = "MONEY"         
                continue 
            
        for token in doc:
            #print(token.text, token.pos_)
            if token.text in entity_text_dic:
                token_label=entity_text_dic[token.text]
                if token_label=="PERSON" or token_label=="ORG":
                    action_sentence_value=="action sentence"  
                    
            if sentence != "":
                sentence+=f" {token.text}"
            else:
                sentence=f"{token.text}"  
                
            if token.text==".":
                #print(token.text)
                #print(f"sentence: {sentence}")
                #print('meow')
                if action_sentence_value=="action sentence":
                    counterr+=1
                    sub_action_list.append(sentence)
                    #person_comp_info_dic_with_action["action"]=sentence
                    #person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=counterr
                    #person_comp_info_dic_with_action["link"]=intital_link
                    #person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                    # clear the dicitonary
                    #person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)
                sentence="" 
                action_sentence_value="not action sentence"                           
            if token.pos_== "PRON":
                action_sentence_value="action sentence"
                # action sentence
                action_sentence=True
                #print('hi')
                continue
        print(sub_action_list)
        #input("hi my name is jeff")
        return sub_action_list
        
    def label_sentence_with_spacy(self,sentence): 
         #a1_1_1.1.1.1_1
         """ generate spacy information for a sentnece"""
         sentence=sentence.replace("?","").replace(",","")
         doc = self.nlp(sentence)
         noun_chunks = [chunk.text.lower() for chunk in doc.noun_chunks]
         entities = [(ent.text, ent.label_) for ent in doc.ents]
         sentences = [sent.text for sent in doc.sents]
         lemmatized_tokens = [token.lemma_ for token in doc]
         pos_tags = [(token.text.lower(), token.pos_) for token in doc]
         pos_only_tags = [(token.pos_) for token in doc]
         text_only_tags = [(token.text.lower()) for token in doc]
         # lower everything
         return {
             "noun_chunks": noun_chunks,
             "entities": entities,
             "sentence": sentence,
             "lemmatized_tokens": lemmatized_tokens,
             "pos_tags": pos_tags,
             "pos_only_tags":pos_only_tags,
             "text_only_tags":text_only_tags
             }
      
    def fill_in_dic_with_duck_duck_go(self,person_comp_info_dic_with_action,saved_text_from_website_and_link_list):
       """ this function will get results from various search browsers and then upload them to """
       import spacy
       import time
       for text_link in saved_text_from_website_and_link_list:
           single_website_text=self.pre_process_text(text_link[0])
           final_sentence_list=self.divide_text_into_sentences(single_website_text)
           for sentence in final_sentence_list:
               spacy_dic=self.label_sentence_with_spacy(sentence)
               person_comp_info_dic_with_action=self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(spacy_dic,person_comp_info_dic_with_action)
       return person_comp_info_dic_with_action

    def generalize_action_words_to_make_it_more_applicable_to_people_and_useable(self,actionn):
        """ run spacy over the action and if any entites show up replace hte eneitty with the gneeric entity value
        like if a name is in the action replace the name with NAME etc"""
        import re
        import time
        import copy
        import spacy
        doc = self.nlp(actionn)
        generalized_action=copy.deepcopy(actionn)
        #actionn_word_list=actionn.split(" ")
        for ent in doc.ents:
            print(f"{ent.text},{ent.label_}")
            print('hehe')
            textt=ent.text
            labell=ent.label_
            if ent.label_ == "PERSON":
                generalized_action=re.sub(textt,"person",generalized_action)                     
            if ent.label_ == "ORG":
                generalized_action=re.sub(textt,"organizaion",generalized_action)  
            if ent.label_ == "DATE":
                generalized_action=re.sub(textt,"date",generalized_action)
            if ent.label_ == "MONEY":
                generalized_action=re.sub(textt,"money",generalized_action)        
            continue 
          
            continue     
        return generalized_action

    def get_sub_action_list_data_use_patent_data_and_other(self,person_comp_info_dic_with_action,saved_text_from_website_and_link_list):
        """#https://data.uspto.gov/bulkdata/datasets/ptgraps?fileDataFromDate=1976-01-06&fileDataToDate=2001-12-25
        use this script to get more patent data in busienss fucntons in getting_patent_data"""
        #just look through other actions and suggest action lists as sub actions
        # upload all possible action_lists
        #upload patent data as actions if possible
        #then figure top possible sub actions lists that could be used for this action
        #how to incorporate patent # patent will be not a sub task so skip this for now       
        #for action_list in all_possible_action_list_list:          
        # do a duckduckgo search to find  sub action data how do i
        import spacy
        # spacy should be loaded now
        #testing=True
        #if testing==True:
        #    self.nlp = spacy.load("en_core_web_sm")
        self.search_through_patents_to_get_sub_actions()
        print('still need to write this function')
        problemm="what are the steps i would take to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0])
            sub_action_list=self.create_sub_action_list(single_website_text)
            person_comp_info_dic_with_action["sub_steps_to_complete_actions"].append([sub_action_list,text_link[1]]) 
        return person_comp_info_dic_with_action

    def get_placement_of_other_people_places_and_things_related_to_action(self,person_comp_info_dic_with_action,saved_text_from_website_and_link_list):
        """sub actions to complete task are essentially 
        go to do a duckdcukgo search with a specific parameter
        then going to save the text as context 
        do i parse ?
        I think i only save snetneces maybe we will see"""
        import spacy
        problemm="what are other things i should consider relating to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)            
            person_comp_info_dic_with_action["position_of_other_people_places_and_things"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
        return person_comp_info_dic_with_action
    def get_intital_action_info_from_page_2(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """ get verbs in sentence and identify intital noun and cut from there for actions"""
        import re
        import copy
        import spacy
        import time
        from nltk.corpus import stopwords     
        cleaned_noun_chunk_list=[]
        person_comp_info_dic_with_action={         
            "action":"",
            "action_temporal_placement_in_life_list":"#",               
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],

            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[], }
        
        sentence_list=[]
        sentence_word_list=[]
        iter_list=[]
        token_label_list=[]
        token_pos_list=[]
        iter_sub_list=[]
        token_sub_label_list=[]
        token_pos_sub_list=[]
        sentence_word_sub_list=[]
        entity_text_dic={}
        chunk_span_sub_list=[]       
        saved_noun_chunk_list=[]
        saved_noun_chunk_sub_list=[] 
        
        
        person_comp_info_dic_with_action_list=[]
        # clean the text       
        website_text=sel_soup.text
 
        website_text=re.sub("[\[\]{}\'\(\)]","",website_text) 
        website_text=re.sub("  ", " ", website_text)
        website_text=re.sub("-", " ", website_text)
        #spacy_dic=self.label_website_text_with_spacy(website_text)
        # need to divid
        finished_noun_chunk=False
        noun_chunk_segment=False
        verb_found=False
        keep_sentence=False
        keep_sentence1=False
        keep_sentence2=False
        noun_chunk=""
        transformations=""
        action_sentence=""

        person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
        temporal_counter=1
        doc = self.nlp(website_text)      
        for token in doc:
            textt=token.text
            poss=token.pos_
            #print(f"poss {poss}")
            #print(f"textt {textt}")
            
                
            if poss=="PRON" or poss=="NOUN" or poss=="PROPN":
                print('found first noun chunk')
                keep_sentence1=True
                if finished_noun_chunk==True:
                    action_sentence+=f" {textt}"                   
                    continue
                else:
                    noun_chunk+=f" {textt}"
                    action_sentence+=f" {textt}"
                    continue
                
            
 
            if poss=="AUX" or poss=="VERB":
                print('end of first noun chunk')# append rest of sentence
                keep_sentence2=True
                #save the verb word
                if verb_found ==True:
                    print("verb found")
                    action_sentence+=f" {textt}"
                    continue
                else:
                    action_sentence+=f" {textt}"
                    print('finished noun chunkk!!!!')
                    
                    finished_noun_chunk=True
                    # merge the rest of the sentences
                    transformations+=f" {textt}"
                   # then add the remainder of the sentence
                    person_comp_info_dic_with_action_copy['object']= noun_chunk 
                    print(noun_chunk)
                    verb_found=True
                    continue
                
            if finished_noun_chunk ==False and keep_sentence2==False:
                if noun_chunk=="":
                    continue
                else:
                    noun_chunk+=f" {textt}"
                    #input(f"noun_chunk {noun_chunk} ")
                    
     
            if keep_sentence1==True or keep_sentence2 ==True:
                action_sentence+=f" {textt}"
                
            if keep_sentence2==True and keep_sentence1==True:
                if textt=="." :# need to test this 
                   print('sentence end')
                   print(action_sentence)
                   # save action keep the remainder of the sentence
                   person_comp_info_dic_with_action_copy['action']= action_sentence
                   person_comp_info_dic_with_action_copy['transformations'].append(transformations)
                   person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
               
                   person_comp_info_dic_with_action_copy['link']=intital_link 
                   person_comp_info_dic_with_action_copy['intital_page_text']=website_text 


                   
                   temporal_counter+=1                       
                   print('starting new sentence add all previous after noun chunk to dictionary')
                   person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
                   # clear the dictionary
                   person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                   print(f"action_sentence {action_sentence}")
                   print(f"transformations {transformations}")
                   print(f" noun_chunk {noun_chunk}")
                   finished_noun_chunk=False
                   noun_chunk_segment=False
                   verb_found=False
                   noun_chunk=""
                   transformations=""
                   action_sentence=""
                   keep_sentence1=False
                   keep_sentence2=False
                   #input(action_sentence)
                
        return person_comp_info_dic_with_action_list
    
    
    def process_crawl_data_2(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page_2(sel_soup,person_comp_info_dic_with_action_list,intital_link)
        #person_comp_info_dic_with_action_list=self.order_and_divide_actions_into_action_lists(person_comp_info_dic_with_action_list)# it is filled in here so use all the qualtites to sort and divide up the adrtion
        return person_comp_info_dic_with_action_list
    


    def identify_tools_to_solve_the_problem(self,person_comp_info_dic_with_action,saved_text_from_website_and_link_list):
        """ask many more questions to send to duckduckgo here 
        figure_out_all_things_you_can_use_ask_many_questions_on_objects_in_problem_words_in_problem_and_qualtites_to_generate_expert_problem_environment"""
        import spacy
        problemm="what are the tools i would use to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)            
            person_comp_info_dic_with_action["tools_required_to_perform_action"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
        return person_comp_info_dic_with_action
    def get_website_text_lemmas(self,single_website_text):
        """ """
        lemma_str=""
        single_website_text=single_website_text[:800000]
        doc = self.nlp(single_website_text)
        for token in doc:
            lemma_str+=" "+token.lemma_           
        #lemmatized_tokens = [token.lemma_ for token in doc]
        return lemma_str
    
    def process_website_text_and_lemmaize(self,saved_text_from_website_and_link_list):
        """ """
        lemmaized_text_str_list=[]
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)
            lemmaized_text_str_list.append([lemmaized_text_str,text_link[1]])         
            #person_comp_info_dic_with_action[key].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
        return lemmaized_text_str_list

    def figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(self,person_comp_info_dic_with_action,saved_text_from_website_and_link_list,key):
        """ask many more questions to send to duckduckgo here 
        figure_out_all_things_you_can_use_ask_many_questions_on_objects_in_problem_words_in_problem_and_qualtites_to_generate_expert_problem_environment"""
        print(' upload a ton of questions of a database and use these')
        print(' ask questions on all qualtiites of problem dic in relation to question')
        print(' ask questions about problem words, objects in the prboelm envrionment and their qualtiies about everytrhing and max out the context')
        import re
        import spacy
        ### question 1 to ask
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
            person_comp_info_dic_with_action[key].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
        return person_comp_info_dic_with_action
             
    def store_value_in_sql_table(self,dictionary_of_values,table_name):
        """key are row names, value is the values that go in the rows """
        testing=False
        if testing==True:
            import psycopg2
            self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
            self.cur = self.conn.cursor() 
        import re
        table_columns=""
        values_string=""
        #if self.sql_switch==0:
        #    self.sql_switch=self.init_sql()
        for i, (table_column, column_value) in enumerate(dictionary_of_values.items()):
            column_value=str(column_value)
            column_value=column_value.replace("\'","")
            column_value=column_value.replace("\"","")
            column_value=column_value.replace(","," ")
            column_value=column_value.replace("'","")
            column_value=re.sub("\"","",column_value)
            if i ==0:
                table_columns =  f"{table_column}"
                values_string = f"'{column_value}'"
                continue
            else:
                table_columns=  table_columns+f",{table_column}"
                values_string= values_string+f",'{column_value}'"
                continue
        sql_str=f"INSERT INTO {table_name} ({table_columns}) VALUES ({values_string});"
        try:
            self.cur.execute(sql_str)
        except Exception as E:
            print(E)
            
        self.conn.commit()     
    #def f(q):
    #    q.put([42, None, 'hello'])
    
# keep as seeprate function
def remove_stopwords(text):
    """
    
    Removes English stopwords from a given text.
    """
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    # 1. Get the set of English stopwords for faster lookups (O(1) average time complexity)
    stop_words = set(stopwords.words('english'))
    text=str(text)
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words and word.isalnum()]
    return " ".join(filtered_words)

def retreive_problem_data_from_web(q,problemmm):
     import re
     import requests
     import pickle
     from selenium import webdriver
     from bs4 import BeautifulSoup
     from selenium.webdriver.common.by import By
     from selenium.webdriver.common.keys import Keys
     import time
     from selenium.webdriver.firefox.options import Options as FirefoxOptions
     links_of_dif_docs=[]
     saved_link_list=[]
     saved_text_from_website_and_link_list=[]
     link = r"https://html.duckduckgo.com/html/"
     problemmm=str(problemmm)
     question_striped=problemmm.strip()
     question_to_search_for=re.sub(r"\?","",question_striped)
     question_to_search_for=re.sub(r"\n"," ",question_striped)
     question_to_search_for=re.sub(r"\s+"," ",question_striped)

     question_to_search_for=question_to_search_for[:200]
     # will have to figure out best number here
     # run it as a subprocess or multi process
     

     #print(question_to_search_for)
     #input('checking whether prompt is ok here')

     #striped_problem=problem_recorded.strip()
     #problem_to_search_for=re.sub(r"\?","",striped_problem)
     firefox_options = FirefoxOptions()
     firefox_options.headless = True
     try:
         driver= webdriver.Firefox(options=firefox_options)
     except Exception as E:
        print(E)
     # need to fix firefox
     #driver= webdriver.Firefox()
     # need to only include links which are names or orgnaizaitons
     # run link title through spacy
     #
     session = requests.Session()
     headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
     'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
     'Accept':'text/html,application/xhtml+xml,application/xml;'
     'q=0.9,image/webp,*/*;q=0.8'}
     print('this error here seems to be caused by global memroy or ram so give more memory to computer so this will work better and more ram')

     driver.get(link) #the pages link must be inserted here
     content = driver.find_element(By.CLASS_NAME, 'search__input')
     content.send_keys(f"{question_to_search_for}")
     content.send_keys(Keys.ENTER)
     time.sleep(2)
     #print(content)
     html= driver.execute_script("return document.documentElement.outerHTML")
     if html:
         sel_soup = BeautifulSoup(html) #'html.parser'
         links_of_dif_docs= sel_soup.findAll("a") 
         #print(links_of_dif_docs)
   
     if links_of_dif_docs:
         #print('hi')
         for link_found in links_of_dif_docs:
             try:
                 if link_found:
                     final_link=link_found.get('href')
                     if final_link not in saved_link_list:
                         #print(final_link)
                         if final_link:
                             if "https" in final_link:
                                 saved_link_list.append(final_link)
                             else:
                                 continue
             except:
                 continue
             
         for link_finals in saved_link_list:
             try:
                 req = session.get(link_finals, headers=headers,timeout=5)
                 req=req.text
                 if req:
                     soup = BeautifulSoup(req)
                     p_tag_text=soup.get_text()[:70000]
                     #print(p_tag_text)
                     saved_text_from_website_and_link_list.append([str(p_tag_text),link_finals])
                 
                     
                 
             except:
                 continue
     driver.quit()# check if this screen changes
     q.put(saved_text_from_website_and_link_list)
         #return saved_text_from_website_and_link_list
         
if __name__ == '__main__':
    person_comp_info_dic_with_action_template={ 
        "action_iterator":[],
        "action":"",
        "generalized_action":[],         
        "action_temporal_placement_in_life_list":"#",               
        ### action qualities
        "user_time_past_use_of_action_list":[],
        "user_past_actions_list":[],
        "action_geo_locations":[],
        "time_to_complete_action":0,
        "other_losses":[],
        "other_gains":[],
        "monetary_cost_of_action":0,
        "monetary_gain_of_action":0,
        "risk_of_failing":[],
        "expected_roi":[],
        "tools_needed":[],
        "legality":[],
        "action_objects":[],
        "number_of_people_impacted":[],
        "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
        # run through all info in action dic to better choose actions
        "intital_page_text":[],


        "tools_required_to_perform_action":[],
        "skills_required_to_perform_action":[],
        "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
        "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
        "other_things_effected":[],
        "transformations":[], # that can be applied to action besides current 1
        "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects

        "sub_steps_to_complete_actions":[] ,
        "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

        "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
        # use concepts from different fileds to rank action
       # like in _allnce or engineering or law
       # sequentally go through each action in your head, look at factors/qualtities of actions
       #then assign a score for that action
       #then based on scored actions choose an action to take
        ### guide perosnal info qualities during action 
        "organization_or_human":[],
        "age":[],
         "height":[],
         "date":[],
          "birth_date":[],
          "property":[],
          "personalty":[],
          "connections":[],
          "followers":[],
          "messages":[],
          "skills":[],           
          "work_experience":[],
          "degrees":[],
          "books_read":[],
          "marriage_status":[],
          "skills":[],
          "life_actions":[],
          "search_history":[],
          "assets":[],# like money etc
          "liaibities":[],
          "glasses":[],
          "race":[],
          "gender":[],
          "education":[],
          "friends_and_there_qualities":[],
          "employment_history":[],
          "photo":[],
          "pronouns":[],
          "email":[],
          "places_lived":0,
          "profile_photo":[],
          "photos":[],
          "licenses_certificates":[],
          "volunteering":[],
          "skills":[],
          "honours_and_awards":[],
          "interests":[],
          "groups":[],
          "newsletters":[],
          "about_paragraph":[],
          "projects_worked_on":[],
          "projects_interested_in":[],
          "personality_type":[],
          "family_members_and_family_members_qualities":[],
          "phone_info_phone_numbers_contacts":[],
          "other_social_media_info":[],
          "phone_info_phone_numbers_contacts":[],
          "pets":[],
          "animals":[],
          "money":[],
          "plants":[],
          "buying_history":[],
          "selling_history":[],
          "financial_history":[],
          "profile_views_info":[],
          "people_who_searched_info":[],
          "physical_disability":[],
          "mental_disability":[],
          "religion":[],
          "web_search_history":[],
          "age":[],
          "record_of_offenses":[],
          "nationality":[],
          "income":[],
          "link":[],}
    
    from multiprocessing import Process, Queue
    import sys
    import json
    import re
    import spacy
    import time
    import psycopg2
    import pickle
    import copy
    import random
    import string
    context_size_for_websites=1000

    
    table_name="guide_person_positional_info_with_action_info"
    #person_comp_info_dic_with_action_list=sys.argv[1]
    #person_comp_info_dic_with_action_list=json.loads(person_comp_info_dic_with_action_list)
    fill=fill_single()   
    #fill.nlp = spacy.load("en_core_web_sm")
    print('heheh')
    import pickle
    import subprocess
    picklee=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api\person_comp_info_dic_with_action_list.pickle"
    with open(picklee,"rb") as f10:
               person_comp_info_dic_with_action_list=pickle.load( f10)     
    
    
    print(' these are the website related searches we want to only do once rather than for every action')
    person_comp_info_dic_with_action_temp=person_comp_info_dic_with_action_list[0]# use example
    wiki_thing_being_discussed=person_comp_info_dic_with_action_temp["link"]
    single_link_list=re.split(r"/",wiki_thing_being_discussed)
    link_item_title=single_link_list[-1]
    #all_link_item_titles_str=".  ".join(all_link_item_titles_list)
    link_item_title=re.sub("_"," ",link_item_title)   
    print(link_item_title)
    print('questio4n!')
    import pickle
    testing1=False
    testing2=False
    filee=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\strategies\test_pickle2.pickle"
    
    if testing2!=True:
        print('TESTING2 IS TRUE RIGHT NO NEED TO TURN THIS OFF')
        problemm01=f"what is the history of {link_item_title}"
        hist = Queue()
        p0 = Process(target=retreive_problem_data_from_web, args=(hist,problemm01))
        p0.start()
        
        problemm02="what is the biography of " + link_item_title
        bio = Queue()
        p01 = Process(target=retreive_problem_data_from_web, args=(bio,problemm02))
        p01.start()
        
        problemm03="what are the interests of " + link_item_title
        projects_int = Queue()
        p02 = Process(target=retreive_problem_data_from_web, args=(projects_int,problemm03))
        p02.start()

        # now we will deal with questions relatingt o each idnivdual action
        for iterr, person_comp_info_dic_with_action1 in enumerate(person_comp_info_dic_with_action_list):
            
            #person_comp_info_dic_with_action["action_objects"]["1"]=[]
            #person_comp_info_dic_with_action2=copy.deepcopy(person_comp_info_dic_with_action)
            person_comp_info_dic_with_action=copy.deepcopy(person_comp_info_dic_with_action_template)
            letters = string.ascii_letters   
            result_list = random.choices(letters, k=10)
            result_string = "".join(result_list)
            person_comp_info_dic_with_action["action_iterator"]=result_string
            
            person_comp_info_dic_with_action["action"]=person_comp_info_dic_with_action1["action"]
            person_comp_info_dic_with_action["full_action_sentence"]=person_comp_info_dic_with_action1["full_action_sentence"]

            person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=person_comp_info_dic_with_action1["action_temporal_placement_in_life_list"]
            person_comp_info_dic_with_action["link"]=person_comp_info_dic_with_action1["link"]
            person_comp_info_dic_with_action["intital_page_text"]=person_comp_info_dic_with_action1["intital_page_text"]
            person_comp_info_dic_with_action["noun_and_verb_chunk_list"]=person_comp_info_dic_with_action1["noun_and_verb_chunk_list"]
            person_comp_info_dic_with_action["noun_and_verb_chunk_pos_list"]=person_comp_info_dic_with_action1["noun_and_verb_chunk_pos_list"]
            
            #duck duck
            problemm0=person_comp_info_dic_with_action["action"]
            duckduck = Queue()
            p = Process(target=retreive_problem_data_from_web, args=(duckduck,problemm0))
            p.start()
            
            
            #get_sub_action_list_data_use_patent_data_and_other
            problemm1="what are the steps i would take to " + person_comp_info_dic_with_action1["action"]
            sub_action = Queue()
            p1 = Process(target=retreive_problem_data_from_web, args=(sub_action,problemm1))
            p1.start()
                 
            #get_placement_of_other_people_places_and_things_related_to_action
            problemm2="what are other things i should consider relating to " + person_comp_info_dic_with_action1["action"]
            placement = Queue()
            p2 = Process(target=retreive_problem_data_from_web, args=(placement,problemm2))
            p2.start()
            
            
            
            #figure out all things you can use
            problemm4="what is the location i would take to " + person_comp_info_dic_with_action1["action"]
            locate = Queue()
            p3 = Process(target=retreive_problem_data_from_web, args=(locate,problemm4))
            p3.start()
            
            problemm5="what are the resources i would take to " + person_comp_info_dic_with_action1["action"]
            resource = Queue()
            p4 = Process(target=retreive_problem_data_from_web, args=(resource,problemm5))
            p4.start()
            print('hi')

            # tools
            problemm3="what are the tools i would use to " + person_comp_info_dic_with_action1["action"]
            tools = Queue()
            p5 = Process(target=retreive_problem_data_from_web, args=(tools,problemm3))
            p5.start()
            
            problemm6="what are the skills that I would take to " + person_comp_info_dic_with_action1["action"]
            skil = Queue()
            p6 = Process(target=retreive_problem_data_from_web, args=(skil,problemm6))
            p6.start()
            
            if iterr==0:
                bio=bio.get()
                hist=hist.get()
                projects_int=projects_int.get()
                p0.join()
                print('join1')
                p01.join()
                print('join2')
                p02.join()  
                print('join3')
                bio=remove_stopwords(bio)
                hist=remove_stopwords(hist)
                projects_int=remove_stopwords(projects_int)
                bio=str(bio)
                hist=str(hist)
                projects_int=str(projects_int)
                bio=bio[:context_size_for_websites]
                hist=hist[:context_size_for_websites]
                projects_int=projects_int[:context_size_for_websites]



                
                #for website_text0 in duckduck:
                #    person_comp_info_dic_with_action["action_objects"]["1"].append(website_text)
                #for website_text01 in duckduck:
                #    person_comp_info_dic_with_action["action_objects"]["1"].append(website_text)
                #for website_text02 in duckduck:
                #    person_comp_info_dic_with_action["action_objects"]["1"].append(website_text)
                
                   
                #bio=fill.process_website_text_and_lemmaize(bio)
                #print('bio')
                #hist=fill.process_website_text_and_lemmaize(hist)
                #print('hist')
                #projects_int=fill.process_website_text_and_lemmaize(projects_int)
                #print('projects_int')
                
                
            duckduck=duckduck.get()
            sub_action=sub_action.get()  
            placement=placement.get()
            tools=tools.get() 
            locate=locate.get()
            resource=resource.get()
            skil=skil.get()          
            p.join()
            p1.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            #for website_text1 in duckduck:
            #    print(website_text1[1])
            #input(f"duckduck")
            #for website_text1 in sub_action:
            #    print(website_text1[1])
            #input(f"sub_action")
            #for website_text1 in placement:
            #    print(website_text1[1])
            #input(f"placement")
            #for website_text1 in tools:
            #    print(website_text1[1])
            #input(f"tools")
            #for website_text1 in locate:
            #    print(website_text1[1])
            #input(f"locate")
            #for website_text1 in resource:
            #    print(website_text1[1])
            #input(f"resource")
            #for website_text1 in skil:
            #    print(website_text1[1])
            #input(f"skil")
            
            #print(f"duckduck")
            #input(sub_action)
            #print(f"sub_action")
            #input(placement)
            #print(f"placement")
            #input(locate)
            #print(f"locate")
            #input(resource)
            #print(f"resource")
            #input(skil)
            #print(f"skil")
            for website_text1 in duckduck:
                #print(f"website_text1  {website_text1}")
                website_text1=remove_stopwords(website_text1)
                #print(f"website_text1  2 {website_text1}")
                person_comp_info_dic_with_action["action_objects"].append(website_text1)
                
            person_comp_info_dic_with_action["action_objects"]=str(person_comp_info_dic_with_action["action_objects"])
            person_comp_info_dic_with_action["action_objects"]=person_comp_info_dic_with_action["action_objects"][:context_size_for_websites]

            #if testing1==True: 
            #    print('TESTING1 IS TRUE RIGHT NO NEED TO TURN THIS OFF')
            #    with open(filee, 'wb') as file:
            #        pickle.dump(person_comp_info_dic_with_action, file)
                    
            #if testing2==True:
            #    print('TESTING2 IS TRUE RIGHT NO NEED TO TURN THIS OFF')
             #   with open(filee, 'rb') as file:
             #       person_comp_info_dic_with_action = pickle.load(file) 
                    
                    
            for website_text2 in sub_action:
                website_text2=remove_stopwords(website_text2)
                substep_list=fill.create_sub_actions_for_action_2(website_text2,person_comp_info_dic_with_action1)
                person_comp_info_dic_with_action["sub_steps_to_complete_actions"].append(substep_list)
                
            person_comp_info_dic_with_action["sub_steps_to_complete_actions"]=str(person_comp_info_dic_with_action["sub_steps_to_complete_actions"])
            person_comp_info_dic_with_action["sub_steps_to_complete_actions"]=person_comp_info_dic_with_action["sub_steps_to_complete_actions"][:context_size_for_websites]

            
    
            for website_text3 in placement:
                website_text3=remove_stopwords(website_text3)
                person_comp_info_dic_with_action["position_of_other_people_places_and_things"].append(website_text3)
                
            person_comp_info_dic_with_action["position_of_other_people_places_and_things"]=str(person_comp_info_dic_with_action["position_of_other_people_places_and_things"])

            person_comp_info_dic_with_action["position_of_other_people_places_and_things"]=person_comp_info_dic_with_action["position_of_other_people_places_and_things"][:context_size_for_websites]

            for website_text4 in tools:
                website_text4=remove_stopwords(website_text4)
                person_comp_info_dic_with_action["tools_required_to_perform_action"].append(website_text4)
                
            person_comp_info_dic_with_action["tools_required_to_perform_action"]=str(person_comp_info_dic_with_action["tools_required_to_perform_action"])
            person_comp_info_dic_with_action["tools_required_to_perform_action"]=person_comp_info_dic_with_action["tools_required_to_perform_action"][:context_size_for_websites]
    
    
                
                
            for website_text5 in locate:
                website_text5=remove_stopwords(website_text5)
                person_comp_info_dic_with_action["location_needed_to_take_action"].append(website_text5)
                
            person_comp_info_dic_with_action["location_needed_to_take_action"]=str(person_comp_info_dic_with_action["location_needed_to_take_action"])
   
            person_comp_info_dic_with_action["location_needed_to_take_action"]=person_comp_info_dic_with_action["location_needed_to_take_action"][:context_size_for_websites]
   
                
            for website_text6 in resource:
                website_text6=remove_stopwords(website_text6)
                person_comp_info_dic_with_action["resources_required_to_perform_action"].append(website_text6)
                
            person_comp_info_dic_with_action["resources_required_to_perform_action"]=str(person_comp_info_dic_with_action["resources_required_to_perform_action"])

            person_comp_info_dic_with_action["resources_required_to_perform_action"]=person_comp_info_dic_with_action["resources_required_to_perform_action"][:context_size_for_websites]

                
            for website_text7 in skil:
                website_text7=remove_stopwords(website_text7)
                person_comp_info_dic_with_action["skills_required_to_perform_action"].append(website_text7)
            #print(type(person_comp_info_dic_with_action["skills_required_to_perform_action"]))  
            #print('MEOWW')
            person_comp_info_dic_with_action["skills_required_to_perform_action"]=str(person_comp_info_dic_with_action["skills_required_to_perform_action"])

            person_comp_info_dic_with_action["skills_required_to_perform_action"]=person_comp_info_dic_with_action["skills_required_to_perform_action"][:context_size_for_websites]

                
                
            

            person_comp_info_dic_with_action["work_experience"].insert(0,bio)
            person_comp_info_dic_with_action["work_experience"].insert(0,hist)
            person_comp_info_dic_with_action["work_experience"]=person_comp_info_dic_with_action["work_experience"][:context_size_for_websites]
            person_comp_info_dic_with_action["projects_interested_in"].insert(0,projects_int)
            person_comp_info_dic_with_action["projects_interested_in"]=person_comp_info_dic_with_action["projects_interested_in"][:context_size_for_websites]

            
            print('done all one round')
            fill.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
            fill.cur = fill.conn.cursor()
            
            fill.store_value_in_sql_table(person_comp_info_dic_with_action,table_name)

        

        

        #generalized_action=fill.generalize_action_words_to_make_it_more_applicable_to_people_and_useable(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
        #person_comp_info_dic_with_action["sub_steps_to_complete_actions"].append([sub_action_list,text_link[1]])
        #person_comp_info_dic_with_action["position_of_other_people_places_and_things"].append([lemmaized_text_str,text_link[1]]) 
        #person_comp_info_dic_with_action["tools_required_to_perform_action"].append([lemmaized_text_str,text_link[1]])
        #person_comp_info_dic_with_action["skills_required_to_perform_action"].append([skil])
        
            # need to process this so i actually get the sub takss to be correct
            # also need to change the search and make this right
            # may be a bit complicated but i can do it
            # maybe use problem galaxy
            # need to get all altwrnative sub task strats
            # because people will have to look at it
            # also need to fix refferal phrasing if possible
 
        
        
        
        
        ### duckduck
        
        #person_comp_info_dic_with_action=fill.fill_in_dic_with_duck_duck_go(person_comp_info_dic_with_action,duckduck) #get effects by doing this
        #print(person_comp_info_dic_with_action)    
        #print(generalized_action)
        
        ### sub action!                           
        #person_comp_info_dic_with_action=fill.get_sub_action_list_data_use_patent_data_and_other(person_comp_info_dic_with_action,sub_action)# THIS IS KEY
        #print(person_comp_info_dic_with_action)
        #print('sub action sub list')
        
        ### placement!                            
        #person_comp_info_dic_with_action=fill.get_placement_of_other_people_places_and_things_related_to_action(person_comp_info_dic_with_action,placement)
        #print('think mutliple moves ahead')
        #print(person_comp_info_dic_with_action)
        
        ### tools!
        #print('placement of other people')
                               
        #person_comp_info_dic_with_action=fill.identify_tools_to_solve_the_problem(person_comp_info_dic_with_action,tools)

        ### generic ask many question function
        
        #person_comp_info_dic_with_action=fill.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,locate,"location_needed_to_take_action")
        
        #person_comp_info_dic_with_action=fill.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,resource,"resources_required_to_perform_action")
        #person_comp_info_dic_with_action=fill.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,skil,"skills_required_to_perform_action")
        #person_comp_info_dic_with_action["work_experience"].insert(0,bio)
        #person_comp_info_dic_with_action["work_experience"].insert(0,hist)
        #person_comp_info_dic_with_action["projects_interested_in"].insert(0,projects_int)
        
        
        #del fill.conn
        #del fill.cur



