# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 16:40:44 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

class process_crawl_class():
    def __init__(self):
        """ """
        import pyperclip
        from ctypes import windll
        import pyautogui
    def order_and_divide_actions_into_action_lists(self,person_comp_info_dic_with_action_list):
        """ this we will use qualtiies of actions and dic to create action lists and order actions probably using some sort of context        
        the person_comp_info_dic_with_action_list is filled in here so use all the qualtites to sort and divide up the actions maybe build a NN to do it
        """
        for person_comp_info_dic_with_action in person_comp_info_dic_with_action_list.items():
            actionn=person_comp_info_dic_with_action['action']
            print(actionn)
            
            
            
        
        # if context seems the same group those actions maybe
        # if other text seems to make those text fit together do those actions
        
    def label_website_text_with_spacy(self,website_text): 
        #a1_1_1.1.1.1_1
        """ generate spacy information for a sentnece"""
        website_text=website_text.replace("?","").replace(",","")
        doc = self.nlp(website_text)
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
            "sentence": website_text,
            "lemmatized_tokens": lemmatized_tokens,
            "pos_tags": pos_tags,
            "pos_only_tags":pos_only_tags,
            "text_only_tags":text_only_tags
            }
    
    def get_transformation_of_objects_in_sentence(self,spacy_dic,cleaned_noun_chunk_list,person_comp_info_dic_with_action_list):
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
                    self.automated_problem_galaxy_dic[current_noun_chunk]["transformation_list"].append(word)    
                    
        return self.automated_problem_galaxy_dic
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
        #website_text=sel_soup.text
 
        website_text=re.sub("[\[\]{}\'\(\)]","",sel_soup) 
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
            
                
            if poss=="PRON"  or poss=="PROPN":
                #print('found first noun chunk')
                
                if finished_noun_chunk==True:
                    action_sentence+=f" {textt}"                   
                    continue
                else:
                    keep_sentence1=True
                    noun_chunk+=f" {textt}"
                    action_sentence+=f" {textt}"
                    continue
                
            
 
            if poss=="AUX" or poss=="VERB":
                #print('end of first noun chunk')# append rest of sentence
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
                
                
            if "." in textt:
                if keep_sentence2==False or keep_sentence1==False:
                    #print('starting new sentence add all previous after noun chunk to dictionary')
                    # clear the dictionary
                    person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                    print(f"action_sentence {action_sentence}")
                    print('fail')
                    #print(f"transformations {transformations}")
                    #print(f" noun_chunk {noun_chunk}")
                    finished_noun_chunk=False
                    noun_chunk_segment=False
                    verb_found=False
                    noun_chunk=""
                    transformations=""
                    action_sentence=""
                    keep_sentence1=False
                    keep_sentence2=False
                    continue
                    
                
            if keep_sentence2==True and keep_sentence1==True:
                if "." in textt: 
                   print('sentence end')
                   print('success')
                   print(action_sentence)
                   # save action keep the remainder of the sentence
                   person_comp_info_dic_with_action_copy['action']= action_sentence
                   person_comp_info_dic_with_action_copy['transformations'].append(transformations)
                   person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
               
                   person_comp_info_dic_with_action_copy['link']=intital_link 
                   person_comp_info_dic_with_action_copy['intital_page_text']=website_text 


                   
                   temporal_counter+=1                       
                   #print('starting new sentence add all previous after noun chunk to dictionary')
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
                   input('input')
                
        return person_comp_info_dic_with_action_list  
              
     
          
        
    
    def get_intital_action_info_from_page(self,website_text,person_comp_info_dic_with_action_list):
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
        sentence=""
        # clean the text       
        website_text=re.sub("[\[\]{}\'\(\)]","",website_text) 
        website_text=re.sub("  ", " ", website_text)
        website_text=re.sub("-", " ", website_text)
        #spacy_dic=self.label_website_text_with_spacy(website_text)
        doc = self.nlp(website_text)
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
                print(wordddd)            
                if wordddd!="":
                    if new_noun_chunkkk =="":
                        print('hi')
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
            print(wordd)
            print(noun_chunk_iter)
            print(nounn_chunk_list)
            if wordd in nounn_chunk_list:
                print("word in")               
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
        print(all_noun_chunk_list)
        print(used_noun_chunk_iter_dic)
        print(empty_noun_chunk_word_matching_list)                          
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
        for i in range(len(sentence_list)):
            print(i)
            print(sentence_list[i])
            print('------')
            print(token_label_list[i])
            print('------')

            print(token_pos_list[i]) 
            print('------')

            print(saved_noun_chunk_list[i])
            print('------')
        print('stop')
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
            if "VERB" in token_pos_sub_list or "AUX" in token_pos_sub_list:
                for pos_iter, posss in enumerate(token_pos_sub_list):                   
                    verb_wordddd=sentence_word__sub_list[pos_iter]
                    posss=posss
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
                    
                    current_chunk_number=None
                    chunk_str=""
                    if posss == "VERB" or posss == "AUX":
                         verb_counter+=1# this makes sure we only sub out PRON in intital noun chunk and no others in setnece
                         # find noun chunk before find noun chunk after
                         for chunkk_iter, chunk_word in enumerate(sentence_assocaited_sub_chunk_list):                             
                             wordd=chunk_word[0]
                             chunkk=chunk_word[1]
                             if chunkk!=None:
                                 current_chunk_number=chunkk
                                 chunk_iter=chunkk_iter
                             
                             # want the chunk iterr to line up                          
                             if chunkk_iter==pos_iter and current_chunk_number!=None :
                                 chunk_text1=" ".join(used_noun_chunk_iter_dic[current_chunk_number])
                                 #chunk_str=chunk_text1 + f" {verb_wordddd}  "
                                 #first_chunk_iter=chunkk_iter
                                 first_chunk_number=current_chunk_number
                                 first_chunk_end_iter=chunk_iter
                                 continue
                             if chunkk_iter>pos_iter and chunkk!=None:
                                 #this is the next chunk
                                 print(f"first chunk {used_noun_chunk_iter_dic[first_chunk_number]}")
                                 first_chunk_len_minus_1=len(used_noun_chunk_iter_dic[first_chunk_number])-1

                                 second_chunk_len_minus_1=len(used_noun_chunk_iter_dic[current_chunk_number])
                                 print(f"second chunk {used_noun_chunk_iter_dic[current_chunk_number]}")

                                 # will hopedully get us to the end of the chunk
                                 #chunk_text2=" ".join(used_noun_chunk_iter_dic[current_chunk_number]) 
                                 #find the end of the second second chunk segement
                                 second_chunk_end_iter=chunkk_iter   
                                 print(f"sentence_word__sub_list {sentence_word__sub_list}")
                                 #action_segment=" ".join(sentence_word__sub_list[first_chunk_end_iter-first_chunk_len_minus_1:second_chunk_end_iter+second_chunk_len_minus_1])# but by adding this value here hopefully will get us to the end of the chunk                                
                                 #sub out in first chunk using pos any pronouns for proper nouns
                                 #and other referential phrases for their given referenced nouns
                                 # or likely referecned nouns
                                 first_chunk_pos=token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1:first_chunk_end_iter+1]
                                 print("first_chunk_pos")
                                 print(first_chunk_pos)
                                 input() 
                                 if verb_counter<=1:
                                     # do this only for the first chunk of a sentence and first verb of sentence
                                     # dont sub out pronouns in second half of sentence
                                     for iter_pos_noun_chunk_1, posssss in enumerate(first_chunk_pos):
                                         if posssss=="PRON":
                                             # need to locate htis iter in the token_pos_list
                                             token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1:first_chunk_end_iter+1]
                                             current_poss_in_sub_list=token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1+iter_pos_noun_chunk_1]
                                             current_poss_in_sub_list_iter=first_chunk_end_iter-first_chunk_len_minus_1+iter_pos_noun_chunk_1
                                             print(f"current_poss_in_sub_list {current_poss_in_sub_list}")
                                             print('FOUND PRON')
                                             print(posssss)
                                             print(f"current_sent_iter {current_sent_iter}")

                                             if current_sent_iter>3:#  look back 3 at intitally 2 1 0
                                                 for minus_current_sen_iter in range(1,4):
                                                     sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)
                                                     print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                     print(f"proper_noun_found {proper_noun_found}")  
                                                     if proper_noun_found==True:
                                                         break                                                    
                                                 continue
                                             if current_sent_iter==2:# only look back 2  
                                                 for minus_current_sen_iter in range(1,3):
                                                     sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)  
                                                     print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                     print(f"proper_noun_found {proper_noun_found}")
                                                     if proper_noun_found==True:
                                                         break      
                                                 continue                       
                                             if current_sent_iter==1:# only look back 1
                                                 for minus_current_sen_iter in range(1,2):
                                                     sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)
                                                     print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                     print(f"proper_noun_found {proper_noun_found}")
                                                     if proper_noun_found==True:
                                                         break
                                                 continue                      
                                             if current_sent_iter==0:# dont look back
                                                 continue                                    
    
                                 action_segment=" ".join(sentence_word__sub_list[first_chunk_end_iter-first_chunk_len_minus_1:])# but by adding this value here hopefully will get us to the end of the chunk
                                 print(f"action_segment {action_segment}")                                
                                 #chunk_str=chunk_str+chunk_text                                                        
                                 #print('object')
                                 #print(chunk_text1)    
                                 person_comp_info_dic_with_action_copy['action']= action_segment
                                 person_comp_info_dic_with_action_copy['object']= chunk_text1  
                                 person_comp_info_dic_with_action_copy['other_things_effected'].append(sentence_word__sub_list[chunkk_iter:])
                                 person_comp_info_dic_with_action_copy['transformations'].append(sentence_word__sub_list[first_chunk_end_iter+2:chunkk_iter])
                                 temporal_counter+=1
                                 person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
                                 #print('effects')
                                 #print(sentence_word__sub_list[chunkk_iter:])
                                 #print('transs')
                                 #print(sentence_word__sub_list[first_chunk_end_iter+1:chunkk_iter])
                                 #input()
                                 chunk_str=""
                                 print(f"action {person_comp_info_dic_with_action_copy['action']}")
                                 print(f"object {person_comp_info_dic_with_action_copy['object']}")
                                 print(f"other_things_effected {person_comp_info_dic_with_action_copy['other_things_effected']}")
                                 print(f"transformations {person_comp_info_dic_with_action_copy['transformations']}")

                                 break          
                         #print(person_comp_info_dic_with_action_copy['action'])
                         person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
                         person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                         # create action
                    else:
                         continue
        return person_comp_info_dic_with_action_list
            
            
                
    
    def get_objects_and_qualitites_of_objects_in_sentence(self,spacy_dic,person_comp_info_dic_with_action_list):
        """get the intital objects and qualtites in the sentnece """
        import re
        import copy
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
        person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
        
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
                    
                if poss == "VERB" and noun_chunk!="":
                    person_comp_info_dic_with_action_copy["transformation_list"].append(worddd) 
            cleaned_noun_chunk=cleaned_noun_chunk.strip()            
            if cleaned_noun_chunk=="":
                continue            
            cleaned_noun_chunk_list.append(cleaned_noun_chunk)           
            # create qualtities of object here
            # add subsequent noun chunk
            if cleaned_noun_chunk not in self.automated_problem_galaxy_dic:
                person_comp_info_dic_with_action_copy['action']=cleaned_noun_chunk
                #self.automated_problem_galaxy_dic[cleaned_noun_chunk]={"qualtity_list":[],"transformation_list":[]}
            if noun_chunk_number!=len(spacy_dic["noun_chunks"])-1:
                # if last noun chunk then dont add qualtity
                if spacy_dic["noun_chunks"][noun_chunk_number+1] in self.automated_problem_galaxy_dic[cleaned_noun_chunk]["qualtity_list"]:
                    continue
                else:
                    person_comp_info_dic_with_action_copy["qualtity_list"].append(spacy_dic["noun_chunks"][noun_chunk_number+1])# noun chunk after this one
            person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
        
        return person_comp_info_dic_with_action_list,cleaned_noun_chunk_list
    ## only grab last word in noun chink here which is a noun
    # and use a lemma
    
    
    def create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(self,website_text,person_comp_info_dic_with_action_list):
        """ need to place automated problem galaxy in person comp info so i can retrieve it form sql later
        then need to modify automated problem galasy so it has the same sort of strcutre as the other function
        with the actions grouped by proper noun and actions found for proper noun used
        and pronouns subsistuted out for proper nouns and notes made about this
        want to add as action the object to the end of qual list
        and want to add every action and qual list"""
        import re
        import copy
        #orignal sentence saved so if want to modify algorhim later i can
        saved_word_word_chunk_cross_reference_dic={}
        cleaned_noun_chunk_list=[] 
        spacy_dic=self.label_website_text_with_spacy(website_text)
        person_comp_info_dic_with_action_list=self.get_i#ntital_action_info_from_page()       
        person_comp_info_dic_with_action_list,cleaned_noun_chunk_list=self.get_objects_and_qualitites_of_objects_in_sentence(spacy_dic,person_comp_info_dic_with_action_list) 
        person_comp_info_dic_with_action_list=self.get_transformation_of_objects_in_sentence(spacy_dic,cleaned_noun_chunk_list,person_comp_info_dic_with_action_list) 
        return person_comp_info_dic_with_action_list
    
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
    
    
    def sub_pos(self,token_sub_label_list1,sentence_word_list,token_pos_sub_list,i10,i11):
        """ find the mention of org and sub it into sentence"""
        found_org=False
        org_or_person_word="--REFFERENTIAL PHRASE--"
        for i13, entss in enumerate(token_sub_label_list1):    
            if entss=="ORG" or entss=="PERSON":
                found_org=True
                sentence_word_sub_list=sentence_word_list[i10-i11]
                single_org_or_person_word=sentence_word_sub_list[i13]
                org_or_person_word+=f" (({single_org_or_person_word}))" 
                #org_or_person_word+=f" (({entss}))"
                continue
            if found_org==True:
                break
        for i15, poss in enumerate(token_pos_sub_list):
            if poss=="PRON":
                current_setnece_word_list=sentence_word_list[i10]
                current_setnece_word_list[i15]=org_or_person_word
                sentencee=""
                for i20, wordd in enumerate(current_setnece_word_list):
                    if i20=="":
                        sentencee=wordd
                    else:
                        sentencee+=f" {wordd}"
                break 
        return  sentencee 
    def NOT_USABLE_use_othernew_action_algo_for_prop_nouns(self):
        """ """
        import spacy
        person_comp_info_dic_with_action_list=[]
        # start of actual function to be modified
        import re
        import time
        import copy
        from nltk.corpus import stopwords
        #import nltk
        #nltk.download("stopwords")
        #filtered_words = [word for word in word_list if word not in stopwords.words('english')]
        print(f"intital_link {intital_link}")
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
        #print(' make sure the first noun group/subject of sentence or pronoun is a person or organzaion if i do that im good or if atleast a proper noun is in the sentence ')
        #print('use qualtites from spacy in whatever way necessary to get best result so noun groups whatever works or using parsing trees')
        # edit the below at one point
        #print(' need to add in re patterns to search for if psosible for action sentneces to get better action sentences and if not do a neural net')
        #print('key is parsing action sentences let do it boys and do referential phrasing sentecnes and fix these')
        #
        re_action_sentence_patterns_list=[]
        person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
        #page_text=sel_soup.text
        page_text=final_example_str
        doc = self.nlp(page_text) 
        #for i6, chunk in enumerate(doc.noun_chunks):
        #    print(chunk)
        #input()

        action_sentence=False 
        sentence_action_type_dic={}
        sentence=""
        counterr=0
        action_sentence_value="not action sentence"
        pos_list=[]
        pos_dic={}
        entity_text_dic={}
        ### check for if there is any person org date or moeny in the document
        print('only do pronouns which are preceded by in 4 previous sentences back atleast a proper noun or org')
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
                    entity_text_list=ent.text.split(" ")
                    for textt in entity_text_list:
                        if textt =="-":                    
                            continue
                        if textt ==",":                    
                            continue
                        if textt not in stopwords.words('english'):
                            entity_text_dic[textt]="PERSON"
           
                if ent.label_ == "ORG":
                    entity_text_list=ent.text.split(" ")
                    for textt in entity_text_list:
                        if textt ==",":                   
                            continue
                        if textt =="-":                   
                            continue
                        if textt not in stopwords.words('english'):
                            entity_text_dic[textt]="ORG"   

                if ent.label_ == "DATE":
                    entity_text_list=ent.text.split(" ")
                    for textt in entity_text_list:
                        if textt ==",":                    
                            continue
                        if textt =="-":                    
                            continue
                        if textt not in stopwords.words('english'):
                            entity_text_dic[textt]="DATE"
                        
                        
                    #entity_text_dic[ent.text] = "DATE"
                if ent.label_ == "MONEY":
                    entity_text_list=ent.text.split(" ")
                    for textt in entity_text_list:
                        if textt not in stopwords.words('english'):
                            entity_text_dic[textt]="MONEY"

                            
                        
                    
                continue
        #print(entity_text_dic)
        #input('entity text dic')
        ### get sentences in the document
        sentence_list=[]
        sentence_word_list=[]
        iter_list=[]
        token_label_list=[]
        token_pos_list=[]
        iter_sub_list=[]
        token_sub_label_list=[]
        token_pos_sub_list=[]
        sentence_word_sub_list=[]
        sentence=""
        #entity_text_dic[ent.text] = "ORG"
          

        #print(page_text)
        #print(entity_text_dic)
        # need to remove stop words from t he lsit
        #input()
        for i8, token in enumerate(doc):
            token_label=None
            if token.text in entity_text_dic:
                token_label=entity_text_dic[token.text]
                
            if sentence != "":
                sentence+=f" {token.text}"
                iter_sub_list.append(i8)
                token_sub_label_list.append(token_label)
                token_pos_sub_list.append(token.pos_)
                sentence_word_sub_list.append(token.text)
                
                    
            else:
                sentence=f"{token.text}" 
                iter_sub_list.append(i8)
                token_sub_label_list.append(token_label)
                token_pos_sub_list.append(token.pos_)
                sentence_word_sub_list.append(token.text)

                
            if "." in token.text :# will need to test htis one
              sentence=re.sub(r"[\n\r]"," ",sentence)
              sentence=re.sub(r"\s\s+","  ",sentence)
              sentence_list.append(sentence)
              iter_list.append(iter_sub_list)
              token_label_list.append(token_sub_label_list)
              token_pos_list.append(token_pos_sub_list)
              sentence_word_list.append(sentence_word_sub_list)
              sentence="" 
              iter_sub_list=[]
              token_sub_label_list=[]
              token_pos_sub_list=[]
              sentence_word_sub_list=[]
        for i in range(len(sentence_list)):
            print(i)
            print(sentence_list[i])
            print(token_label_list[i])
            print(token_pos_list[i])
            
        #print(sentence_list)  
        #print(iter_list)
        #print(token_label_list)  
        #print(token_pos_list)                                   
        #input()   
        ### use informaiton to dignoise action vs non action sentences
        # so this intital part was to gather information
        # now just gotta write the proper pronoun rule so if last two sentneces had a org or person mentioned
        # and this has a pronoun this assume its an action setnence
        # if a sentnece has a org or person mentioned it is also an action sentence
        #  and if it has proper sentnece structure like other words it cant just be a mention of a person or orgs name
        # maybe use re patterns for this



        # need to look for the specific subject object verb pattern in sentnece to avoid
        # sentneces that are just added that are things but not actions sentecnes of thing
        # or need to find a way to 
        # so check if the sentnece for its pos has a noun verb ands noun strcutre
        # and if ti meet shtis strcutre then its action sentence in additon to other aqttributes
        # 
        # what else can i use to differnitate between action and non action sentneces
        print('try the below notes next to improve results')
        print('''
              # maybe try this approach with or without person org/pron approach
              # my inkly says use  ton of pos patterns to parse action vs non action sentences
              # and expand from there
              # and just add like 100 different pos strctures and slight variatins
              # and that should do''')



        # so the pos need to follow a specific pattern
        # use pos strcutre of wanted setneces to differnitate between wanted and un wanted
        # the short ugly citations versus action sentneces

        # butessentially sue qualtities of input data to parse these action sentences and find patterns
        # relating to action sentences that uses this data
        # these are two specific pattenrs need to generlaize them so they work better
        # either for unwanted or wanted

        # must be a noun/pron/propn  verb object
        # need a subject verb object if not sentence does not count
        #use token.dep_ and tree of sentence with subject verb object where possible
        # find the pos patterns i like within sentecnes that are attributed to actions
        # and use these to find action sentences
        # group into for sure action setnences and not sure action sentences for now
        # and then can slowly build up list of for sure action sentences pos patterns examples

        # break up sentences adn only include action part? like parts of speech attribtued to the action
        # or rather group action sentences by the subject of the sentence
        # so group all sentences with the conservatives and liberals as subject together to shwo their actions
        # for pronouns need to find the reference for the pronoun
        #and group these to the earlier sentences for referentrial phrasing
        # the earlier proper noun being the referential phrase
        wanted_pos_pattern_list=[['PRON', 'AUX', 'DET', 'NOUN', 'ADP', 'PROPN', 'PROPN', 'PROPN', 'ADP', 'PROPN'],
         ['PRON', 'AUX', 'VERB'],
         ['PRON', 'VERB', 'VERB', 'NOUN'],
         ['PROPN', 'PROPN', 'PROPN', 'PUNCT', 'PRON', 'VERB', 'PART', 'VERB', 'DET', 'NOUN', 'ADP', 'NOUN', 'ADP', 'NOUN', 'ADP', 'ADJ', 'NOUN'],
         ['PROPN', 'NOUN', 'PUNCT', 'AUX', 'DET', 'NOUN', 'ADP', 'NOUN', 'ADP', 'PRON', 'NOUN', 'VERB', 'DET', 'VERB', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'ADJ', 'NOUN',],
         ]


        # trying to find the pattern in example of wanted action sentences pos
        # most broad pattern is a pron/propn followed by verb or aux
        #pron propn or                    
        # sentence must have 
        #pron/propn followed by aux or verb 
        # find the pron or prop noun being referecned and saved based on referecned noun pro noun
        # of action
        # and incorproate the other function into this one     

                       
        unwanted_pos_pattern_list=[['PROPN', 'SPACE', 'NUM', 'SYM', 'NUM', 'PUNCT'],
                                   ['SPACE', 'PUNCT', 'DET', 'NOUN', 'PROPN', 'PUNCT', 'PROPN', 'PUNCT', 'PROPN', 'PUNCT', 'PROPN', 'PROPN'],
                                   ['ADP', 'SPACE', 'NOUN', 'NOUN', 'SPACE', 'PUNCT', 'VERB', 'PROPN', 'PUNCT', 'VERB', 'PUNCT', 'ADJ', 'NOUN', 'PUNCT'],
                                   ['PROPN', 'PROPN', 'PUNCT'],]

        action_sentence=False
        for i10, sentence in enumerate(sentence_list):
            token_sub_label_list=token_label_list[i10]
            token_pos_sub_list=token_pos_list[i10]
            if "ORG" in token_sub_label_list or "PERSON" in token_sub_label_list:
                if "PROPN" in token_pos_sub_list or "PRON" in token_pos_sub_list:
                    if "VERB" in token_pos_sub_list or "AUX" in token_pos_sub_list:
                        person_comp_info_dic_with_action["action"]=sentence
                        person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=i10
                        person_comp_info_dic_with_action["link"]=intital_link
                        person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                        # clear the dicitonary
                        person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)
                        continue  
            if "PRON" in token_pos_sub_list:
                if "VERB" in token_pos_sub_list or "AUX" in token_pos_sub_list:
                    if i10>3:#  look back 3 at intitally 2 1 0
                        for i11 in range(1,4):
                            token_sub_label_list1=token_label_list[i10-i11]
                            if "ORG" in token_sub_label_list1 or "PERSON" in token_sub_label_list1:
                                sentencee=self.sub_pos(token_sub_label_list1,sentence_word_list,token_pos_sub_list,i10,i11)
                                person_comp_info_dic_with_action["action"]=sentencee
                                person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=i10
                                person_comp_info_dic_with_action["link"]=intital_link
                                person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                                # clear the dicitonary
                                person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)                     
                                break
                        continue
                    if i10==2:# only look back 2  
                        for i11 in range(1,3):
                            token_sub_label_list1=token_label_list[i10-i11]
                            if "ORG" in token_sub_label_list1 or "PERSON" in token_sub_label_list1:
                                sentencee=self.sub_pos(token_sub_label_list1,sentence_word_list,token_pos_sub_list,i10,i11)                       
                                person_comp_info_dic_with_action["action"]=sentencee
                                person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=i10
                                person_comp_info_dic_with_action["link"]=intital_link
                                person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                                # clear the dicitonary
                                person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)                     
                                break
                        continue                       
                    if i10==1:# only look back 1
                    # need to sub the whole noun group not just the noun word
                        for i11 in range(1,2):
                            token_sub_label_list1=token_label_list[i10-i11]
                            if "ORG" in token_sub_label_list1 or "PERSON" in token_sub_label_list1:
                                sentencee=self.sub_pos(token_sub_label_list1,sentence_word_list,token_pos_sub_list,i10,i11)
                                person_comp_info_dic_with_action["action"]=sentencee
                                person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=i10
                                person_comp_info_dic_with_action["link"]=intital_link
                                person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                                # clear the dicitonary
                                person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)                     
                                break
                        continue                      
                    if i10==0:# dont look back
                        continue
            # going to leave pattern list empty for now but have idea for later
            for pattern in re_action_sentence_patterns_list:
                result=re.search(pattern,sentence)
                if result:
                    action_sentence=True
                    person_comp_info_dic_with_action["action"]=sentence
                    person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=i10
                    person_comp_info_dic_with_action["link"]=intital_link
                    person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                    # clear the dicitonary
                    person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)  
                print('hi')
                
        print('these are the action sentences')        
        for  i12, person_comp_info_dic_with_actionn in enumerate(person_comp_info_dic_with_action_list):
            print(i12)
            print(person_comp_info_dic_with_actionn["action"])
            
        ### notes for wiki actions of life dag    
        print('group by org or person being talked about in the sentence not the page')
        print('and order in a list by mention as the life dag and then use other info as necessary to place it correctly') 
        print('save by page as well so save by person/org mention in sentnece and save by page')
    def process_crawl_data_try_2(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """write this function tonight 
        just get first noun and if verb in sentence is action sentence, add first as transformation"""
        person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page_2(sel_soup,person_comp_info_dic_with_action_list,intital_link)
        #person_comp_info_dic_with_action_list=self.order_and_divide_actions_into_action_lists(person_comp_info_dic_with_action_list)# it is filled in here so use all the qualtites to sort and divide up the adrtion
        return person_comp_info_dic_with_action_list
        
    def process_crawl_data(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """ need to place automated problem galaxy in person comp info so i can retrieve it form sql later
        then need to modify automated problem galasy so it has the same sort of strcutre as the other function
        with the actions grouped by proper noun and actions found for proper noun used
        and pronouns subsistuted out for proper nouns and notes made about this
        [action] will be object to end of qual list
        alternative actions will be alternative quals with object(proper noun) and verb
        add in pronoun thing subbing in proper noun for it
        add in proper noun thing so they line up
        add effects and transformaton list in action's keys
        bascially add all info to the action dic
        sort out ordering and dividing into aciton list in second function                
        """
        person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page(sel_soup,person_comp_info_dic_with_action_list)
        #person_comp_info_dic_with_action_list=self.order_and_divide_actions_into_action_lists(person_comp_info_dic_with_action_list)# it is filled in here so use all the qualtites to sort and divide up the adrtion
        return person_comp_info_dic_with_action_list
        


import spacy
person_comp_info_dic_with_action_list=[]
og_linkk="meow"
example_list=["He was the founder of Harmony Baptist Church in Augusta , Georgia , in 1869 , and of other churches .",
              "On April 1 , 1866 , he was ordained , and he began holding meetings on June 16 , 1867 , in what was known as McKinley s grove on a farm owned by Mary Bouyer McKinley and presided by Rev. George Barnes .",
              "[7 ] This study also found , in general ,  old money is , if anything , more uniformly conservative than new money .",
              "The Digital Rights movement[47 ] consists of activists and organizations , such as the Electronic Frontier Foundation , who work to protect the rights of people in relation to new technologies , particularly concerning the Internet and other information and communications technologies .",
              "  Economic activism[edit ]  Further information : Economic activism  Economic activism involves using the economic power of government , consumers , and businesses for social and economic policy change.[56 ] Both conservative and liberal groups use economic activism as a form of pressure to influence companies and organizations to oppose or support particular political , religious , or social values and behaviors.[57 ] This may be done through ethical consumerism to reinforce  good  behavior and support companies one would like to succeed , or through boycott or divestment to penalize  bad  behavior and pressure companies to change or go out of business .",
              "  Brand activism[58 ] is the type of activism in which business plays a leading role in the processes of social change .",
              "ISSN  1751 - 9020 .",
              "  ^ a b Ince , Jelani ; Finlay , Brandon M. ; Rojas , Fabio ( 2018 ) .",
              "  See also[edit ]  Arab Spring  Advocacy evaluation  Advocacy group  Advocacy  Animal rights  Asian American activism  Civil disobedience  Community leader  Counterculture of the 1960s  Cultural activism  Demonstration ( protest )  Dissident  Human rights activists  List of activists  List of peace activists  Media manipulation  Restorationism  Slacktivism  Social engineering ( political science )  Spiritual activism  Student activism  Water protectors  Youth activism  References[edit ]  ^ Tarrow , Sidney ( 1998 ) .",
              "  Métis - Wikipedia  Jump to content  Main menu  Main menu  move to sidebar  hide  Navigation  Main pageContentsCurrent eventsRandom articleAbout WikipediaContact us  Contribute  HelpLearn to editCommunity portalRecent changesUpload fileSpecial pages  Search  Search  Appearance  Donate  Create account  Log in  Personal tools  Donate Create account Log in  Pages for logged out editors learn more  ContributionsTalk  Contents  move to sidebar  hide  ( Top )  1  Background  Toggle Background subsection  1.1  Etymology  1.2  Semantic definitions  1.2.1  Lowercase  m   1.2.2  Uppercase  M   1.3  Other groups and individuals  1.4  Riel s Métis  2  Métis people in Canada  Toggle Métis people in Canada subsection  2.1  Identity  2.1.1  Self - identity and legal status  2.1.2  View of identity  2.1.3  Lack of a legal definition  2.1.4  Definitions used by Métis representative organizations  2.1.5  Cultural definitions  2.2  Canadian history  2.3  Culture  2.3.1  Language  2.3.2  Flag  2.3.3  Cultural genocide  2.4  Land ownership  2.5  Distribution  2.6  Métis settlements of Alberta  3  Organizations in Canada  Toggle Organizations in Canada subsection  3.1  Pre - Batoche  3.2  Métis Nation of Alberta ( 1928 )  3.3  Manitoba Métis Federation ( 1967 )  3.4  Congress of Aboriginal Peoples ( 1971 )  3.5  Metis National Council ( 1983 )  3.6  Ontario Métis Aboriginal Association  4  Métis people in the United States  Toggle Métis people in the United States subsection  4.1  Geography  4.2  United States history  4.3  Current population  4.4  Louis Riel and the United States  5  Medicine Line ( Canada – U.S. border )  6  See also  7  Citations  8  Bibliography  9  External links  Toggle the table of contents  Métis  34 languages  العربيةBoarischCatalàČeštinaDeutschΕλληνικάEspañolEsperantoفارسیFrançaisGalego한국어हिन्दीBahasa IndonesiaItalianoBahasa MelayuNederlandsNēhiyawēwin / ᓀᐦᐃᔭᐍᐏᐣ日本語Norsk bokmålਪੰਜਾਬੀPortuguêsРусскийSimple EnglishСрпски / srpskiSrpskohrvatski / српскохрватскиSuomiSvenskaTürkçeУкраїнськаاردو吴语粵語中文  Edit links  ArticleTalk  English  ReadEditView history  Tools  Tools  move to sidebar  hide  Actions  ReadEditView history  General  What links hereRelated changesUpload filePermanent linkPage informationCite this pageGet shortened URLDownload QR code  Print / export  Download as PDFPrintable version  In other projects  Wikimedia CommonsWikidata item  Appearance  move to sidebar  hide  From Wikipedia , the free encyclopedia  Mixed Indigenous ethnic group of Canada and the US  For other uses , see Metis .",
              "  Not to be confused with Meitei people in Canada or Métis ( Belgian Congo ) .",
              "  Stand - alone list articles[edit ]  Main page : Wikipedia : Stand - alone lists  See also : Wikipedia : Manual of Style / Lists of works  List articles are encyclopedia pages consisting of introductory material in the lead section followed by a list , possibly arranged in sub - sections .",
              "Art activism can activate utopian thinking , which is imagining about an ideal society that is different from the current society , which is found to be effective for increasing collective action intentions .",
              " Advocacy 2.0 : An Analysis of How Advocacy Groups in the United States Perceive and Use Social Media as Tools for Facilitating Civic Engagement and Collective Action  .",
              "For  list articles  , see Wikipedia : Stand - alone lists .",
              
              
              
              
              
              ]
final_example_str=""
intital_link="meow"
for i, example in enumerate(example_list):
    final_example_str+=example + " "


crawl=process_crawl_class()  
crawl.nlp = spacy.load("en_core_web_sm")

person_comp_info_dic_with_action_list=crawl.process_crawl_data_try_2(final_example_str,person_comp_info_dic_with_action_list,og_linkk)   
input('hi')  

 #person_comp_info_dic_with_action_list=self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(sel_soup,person_comp_info_dic_with_action_list)
 #print(person_comp_info_dic_with_action_list)     
        
        # for referntial phrasing maybe sub in the name of the page

        ### sub_methods notes on consturcting aloghrim
        #print('so for sub methods need a differetn search probably based on the one we wrote for building problem galaxy')     
        #print('if the subject of the snetence seems to be related to the search then add it as a sub method step otherwise focused') 
        #print(' so first run throguh gets actions actual done by the guy looking on pron and prop nouns etc second run through gets all actions discussed in doc then get sprinkle in these extra action later')  
        #print('do a second run through which catches all actions on the web page  which we can add to strat later using some rules using the below function ')
        #print('the value of first one is it incorproates actual actions the person took other one gets all the actions but may not be persons so use in different ways')
        # need to do the create problems galxies function
        # from text for problem using pos in the sentence
        # need to modify the create galasxies transofrmation text and add the top stuff
        #essentially want to improve the noun chunks being grabbed so we grab proper nouns
        # and pronouns