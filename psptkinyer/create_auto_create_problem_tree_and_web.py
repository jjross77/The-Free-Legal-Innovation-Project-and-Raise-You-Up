    # -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:10:14 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

class create_auto_create_problem_tree_and_web():
    def __init__(self):
        """ """
    def retreive_problem_data_from_web(self,problemmm):
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
         saved_text_from_website_list=[]
         link = r"https://html.duckduckgo.com/html/"
         question_striped=problemmm.strip()
         question_to_search_for=re.sub(r"\?","",question_striped)
         print(question_to_search_for)

         #striped_problem=problem_recorded.strip()
         #problem_to_search_for=re.sub(r"\?","",striped_problem)
         firefox_options = FirefoxOptions()
         firefox_options.headless = True
         driver= webdriver.Firefox(options=firefox_options)
         #driver= webdriver.Firefox()
         session = requests.Session()
         headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
         'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
         'Accept':'text/html,application/xhtml+xml,application/xml;'
         'q=0.9,image/webp,*/*;q=0.8'}

         driver.get(link) #the pages link must be inserted here
         content = driver.find_element(By.CLASS_NAME, 'search__input')
         content.send_keys(f"{question_to_search_for}")
         content.send_keys(Keys.ENTER)
         time.sleep(2)
         #print(content)
         html= driver.execute_script("return document.documentElement.outerHTML")
         sel_soup = BeautifulSoup(html, 'html.parser')
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
                     req = session.get(link_finals, headers=headers)
                     soup = BeautifulSoup(req.text)
                     p_tag_text=soup.get_text()
                     #print(p_tag_text)
                     saved_text_from_website_list.append(str(p_tag_text))
                 
                 except:
                     continue
             driver.quit()
             return saved_text_from_website_list
     # process text throw out trash vs non trash
     # divide using sentnece non sentence
     # reuse processing text from project
     # reuse from business class
     
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
     
    def get_objects_and_qualitites_of_objects_in_sentence(self,spacy_dic):
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
             if cleaned_noun_chunk not in self.automated_problem_galaxy_dic:
                 self.automated_problem_galaxy_dic[cleaned_noun_chunk]={"qualtity_list":[],"transformation_list":[]}
             if noun_chunk_number!=len(spacy_dic["noun_chunks"])-1:
                 # if last noun chunk then dont add qualtity
                 if spacy_dic["noun_chunks"][noun_chunk_number+1] in self.automated_problem_galaxy_dic[cleaned_noun_chunk]["qualtity_list"]:
                     continue
                 else:
                     self.automated_problem_galaxy_dic[cleaned_noun_chunk]["qualtity_list"].append(spacy_dic["noun_chunks"][noun_chunk_number+1])# noun chunk after this one
         return self.automated_problem_galaxy_dic,cleaned_noun_chunk_list
               
    def get_transformation_of_objects_in_sentence(self,spacy_dic,cleaned_noun_chunk_list):
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
     
    def create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(self,spacy_dic):
        """ """
        import re
        import copy
        #orignal sentence saved so if want to modify algorhim later i can
        saved_word_word_chunk_cross_reference_dic={}
        cleaned_noun_chunk_list=[] 
        automated_problem_galaxy_dic,cleaned_noun_chunk_list=self.get_objects_and_qualitites_of_objects_in_sentence(spacy_dic) 
        automated_problem_galaxy_dic=self.get_transformation_of_objects_in_sentence(spacy_dic,cleaned_noun_chunk_list) 
        return automated_problem_galaxy_dic
    
    def clean_strs_before_input_into_sql(self,strrr):
        """ """
        import re
        strrr=re.sub('\'',"",str(strrr))
        strrr=re.sub('\"',"",strrr)
        strrr=re.sub('\n',"",strrr)
        return strrr
        
    def store_auto_created_galaxies_and_transformation_for_problem_web_in_sql(self):
        """ """
        #auto_problem_table columns
        import time
        current_time=time.time()
        for objectt, objectt_dic in self.automated_problem_galaxy_dic.items():
            qualtity_list=self.automated_problem_galaxy_dic[objectt]["qualtity_list"]
            transformation_list=self.automated_problem_galaxy_dic[objectt]["transformation_list"]
            objectt=self.clean_strs_before_input_into_sql(objectt)
            qualtity_list=self.clean_strs_before_input_into_sql(qualtity_list)
            transformation_list=self.clean_strs_before_input_into_sql(transformation_list)
            current_time=self.clean_strs_before_input_into_sql(current_time)
            # need to make sure not to over write  values here

            self.cur.execute( f""" INSERT INTO auto_problem_table (problem_question_or_task,specific_problem_or_object,qualitity_list,transformations,initial_creation)
                         VALUES ('{str(self.problem_recorded)}','{str(objectt)}','{str(qualtity_list)}','{str(transformation_list)}','{str(current_time)}');""")
        self.conn.commit()
        # what if i want to update this thing? used past functions
        # and always start from scratch by assumption
    
    
    #### PROBLEM TREE FUNCTIONS
    # think of permeant solution here not temp
    # make this work and be useful
        
    def auto_generate_action_space_and_effects(self):
        """ actions are linked to effects"""
        import copy
        automated_problem_galaxy_dic2=copy.deepcopy(self.automated_problem_galaxy_dic)
        self.possible_object_action_effect_list_dic={}#objectttt:[list of actions]
        print(self.automated_problem_galaxy_dic)
        self.strategy_methods_problem_tree_dic={}
        for objectt, objectt_dic in self.automated_problem_galaxy_dic.items():
            self.strategy_methods_problem_tree_dic[objectt]={"action_list":[],"effects_list":[]}
            qualtity_list=self.automated_problem_galaxy_dic[objectt]["qualtity_list"]
            transformation_list=self.automated_problem_galaxy_dic[objectt]["transformation_list"]
            
            for transformation in transformation_list:
                actionnnn=f" {transformation} {objectt}"
                self.strategy_methods_problem_tree_dic[objectt]["action_list"].append(actionnnn)  
                self.strategy_methods_problem_tree_dic[objectt]["effects_list"].append(qualtity_list)  
        return self.automated_problem_galaxy_dic
    ### start of working stratgy functions and problem tree
    def generate_more_context_qualtities_as_necesarry_using_tool_and_questions(self,strategy_dic):
        """ gather as muc context as possible on given action
        use generative model for this
        store results to each questions as qualtites of the action input"""
        # run a model off of big computer to do this?
        # and send data back
        # maybe use gpt for this
        # couple options
        # use all questions and tools
        # cant afford mdoel here? too expensive do this another time
        # or find other solution
        #try an example tool here
        # and an example question
        # just use a improved web search here
    def generate_value_dic_of_how_compareable_actions_are_based_on_effect_lists(self):
        """ compare all actions effects against all other action effects and create a value dic of these comparisons """
        self.matching_values_of_effects_dic={}
        print('starting sort')

        for i1, (objecttt1) in enumerate(self.strategy_methods_problem_tree_dic.keys()):
            possible_action_space_list1=self.strategy_methods_problem_tree_dic[objecttt1]["action_list"]
            effects_list_list1=self.strategy_methods_problem_tree_dic[objecttt1]["effects_list"]
            #print(f"objecttt1 : {objecttt1}")
            #print(f"effects_list_list1 : {effects_list_list1}")
            if effects_list_list1:
                effect_list1=effects_list_list1[0]
            else:
                continue
            for i2, (objecttt2) in enumerate(self.strategy_methods_problem_tree_dic.keys()):
                if i2 % 2 == 1:
                    continue
                possible_action_space_list2=self.strategy_methods_problem_tree_dic[objecttt2]["action_list"]
                effects_list_list2=self.strategy_methods_problem_tree_dic[objecttt2]["effects_list"]
                if effects_list_list2:
                    effects_list2=effects_list_list2[0]
                else:
                    continue
                len_effect_list_2=len(effects_list2)
                effects_found=0
                for iii2, effect2 in enumerate(effects_list2):
                    if effect2 in effect_list1:
                        effects_found +=1
                    else:
                        continue
                if len_effect_list_2==0:
                    weighted_effects_found=0
                else:
                    weighted_effects_found=effects_found/len_effect_list_2
                #print(f"effects_found : {effects_found}")
                #print(f"weighted_effects_found : {weighted_effects_found}")
                for actionn1 in possible_action_space_list1:
                    for actionn2 in possible_action_space_list2:
                        if actionn1 not in self.matching_values_of_effects_dic:
                            self.matching_values_of_effects_dic[actionn1]={}
                        else:
                            self.matching_values_of_effects_dic[actionn1][actionn2]={"weighted_effects_found":weighted_effects_found,
                                                                                     "objecttt1":objecttt1,
                                                                                     "objecttt2":objecttt2,
                                                                                     "action1":actionn1,
                                                                                     "action2":actionn2,
                                                                                     "effect_list1":effect_list1,
                                                                                     "effect_list2":effects_list2} 
    
                                  
        return self.matching_values_of_effects_dic
    def sort_actions_into_strat_by_max_different_effect_score_sub(self):
        """need to rewrite this so no memroy error cant compare every noun it seems so make this more efficent """
        self.strategy_methods_problem_tree_dic_max_difference={"max_different_effect_strategies":[], 
                                                 "max_different_objects_associated_with_action":[],
                                                 "max_different_effect_list":[] }
        # list of list with 10 actions in each list
        #print(self.matching_values_of_effects_dic)
        print('meow')
        current_strategy_list=[]
        used_actions_list=[]
        final_strategy_list=[]
        lowest_score_list=[]
        for action1 in self.matching_values_of_effects_dic.keys():
            final_strategy_list=[]
            objecttt1_list=[]
            objecttt2_list=[]
            actionn1_list=[]
            actionn2_list=[]
            effect_list1_list=[]
            effect_list2_list=[]
            lowest_action_list=[]
            lowest_score_list=[]
            if action1 in used_actions_list:
                continue
            for i8, (action2) in enumerate(self.matching_values_of_effects_dic[action1].keys()):
                if action2 in used_actions_list:
                    continue
               
                weighted_effects_found=self.matching_values_of_effects_dic[action1][action2]["weighted_effects_found"]
                if len(lowest_action_list)<9:
                    lowest_action_list.append(self.matching_values_of_effects_dic[action1][action2])
                    lowest_score_list.append(weighted_effects_found)
                    max_score=max(lowest_score_list)
                    current_highest_saved_score=max_score
                    continue
                if weighted_effects_found<=current_highest_saved_score:
                    current_highest_saved_score_index=lowest_score_list.index(current_highest_saved_score)
                    lowest_action_list[current_highest_saved_score_index]=self.matching_values_of_effects_dic[action1][action2]
                    lowest_score_list[current_highest_saved_score_index]=weighted_effects_found
                    max_score=max(lowest_score_list)
                    current_highest_saved_score=max_score
                else:
                    continue
                    
            for i6, action_info in enumerate(lowest_action_list):
                used_actions_list.append(action_info["action2"])
                #action_info dictionary
                final_strategy_list.append(action_info["action2"])
                objecttt1_list.append(action_info["objecttt2"])
                #objecttt2_list.append(action_info["objecttt2"])
                #actionn1_list.append(action_info["action1"])
                #actionn2_list.append(action_info["action2"])
                effect_list1_list.append(action_info["effect_list2"])
                #effect_list2_list.append(action_info["effect_list2"])
                
            self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_strategies"].append(final_strategy_list) 
            self.strategy_methods_problem_tree_dic_max_difference["max_different_objects_associated_with_action"].append(objecttt1_list)    
            self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_list"].append(effect_list1_list)    

        return self.strategy_methods_problem_tree_dic_max_difference# list of list of strategies
    def sort_actions_into_strat_by_max_different_effect_score(self,strategy_methods_problem_tree_dic):
        """ # iterate through effects lists and assign corresponding values
        # depending on how related each effect list is to each other
        # sort effect lists into strategies using these scoring lists
        #qauntity being being the number of matching qualtites"""
        self.generate_value_dic_of_how_compareable_actions_are_based_on_effect_lists()
        self.sort_actions_into_strat_by_max_different_effect_score_sub()
        return self.strategy_methods_problem_tree_dic 
        
    def consider_effects(self,galaxy_problem_dic):
        """ """
        strategy_methods_problem_tree_dic=self.sort_actions_into_strat_by_max_different_effect_score(self.strategy_methods_problem_tree_dic)
        #create one actions_list with very diverse effects
        #and one with very similar effects
        # divide into strategies of 10
        #action
        #down stream effects 
        # want strategies with 10 actions
        #consider effect spread
        # divide actions using all there 
        #qualtites in various ways
        # and use qualtities of qualtites
        # to decide how you could use it 
        #to divide up the actions
        # how to do this
        # how to save data 
        # group all 
        return self.strategy_methods_problem_tree_dic
    def consider_tools(self):
        """ """
    def cosnider_question_info(self):
     """ """
    def consider_past_problem_data(self):
        """look at time it took toc omplete action and other qualtites"""
            #time
            #get max 20%
            #get min 20%
        #strategy 1 actions most different effects rule
     
    def consider_herusitic_or_general_principles_using_action_context_to_sort_and_select_actions(self,strategy_methods_problem_tree_dic):
        """
        # use  interactions and 
        #ojbects qualtity thermselves to produce strats
        # and if else statements below
        bascially a massive decision tree
        dividng on qualtity and then
        dividing on qualtity of qualtity
        and automating this
        seeing action chosen
        using this and then choosing best categories
        look for general qualitites  for stronger transformations
        # these are effects
        # time
        tool answers
        question answers
        basically try differnet things to get different action lists
        dvidied on qualtites and use the best one to train neural net
        for now just use effects
        eventually turn into nn
        IMPORTANT BELOW
        maybe categorize strategies
        by how they were created
        by what sort of heuristic
        to track later
        and group by 10
        """
        self.consider_effects(self.strategy_methods_problem_tree_dic)
        # will divide actions along these when have time comming
        # up with sorting algorhyim relating to them
        self.consider_tools()
        self.cosnider_question_info()
        self.consider_past_problem_data()# generate this problem data later to use this
        # will build nn out of it
        # problem data might be time
        # and screen shots for each action
        return self.strategy_methods_problem_tree_dic
    def distil_berta_to_produce_word_embedding(self):
        """input actions """
    def ffn_1_cateogrizing_actions_into_types_of_strats(self):
        """input actions
        what categories and why
        basically want to sort actions
        along some critera so we can then 
        choose some over others   for di f ferent reasons
        and also ignore others completely
        used versus unused actions
        qualtites of action data 
        used recorded screen caputre
        to create labels here?
        how to divide up actions into differetn strats
        how to use different data here
        used during probelm sovling
        used versus unused qualtites
        CATEGORIES?
        labels determined using qualtites and
        other data of actions in previous problems
        maybe creative, 
        not creative
        most simialr actions in previous problems
        in previous problems
        most time consuming
        
        """
    def ffn_2_ordering_actions_within_strats(self):
        """output ordered strats using previous action placement in a strat ordering placement 
        use other problem solving data as well here"""

         
    def consider_past_action_data_with_nn_to_choose_and_sort_action(self,strategy_dic):
        """once have exact actions and strats  from heuristic lists we like use nn
        use a neural network here
        create a couple strategies using this approach
        NEED TO DESIGN NEURAL NET
        use data we have
        basically train a policy function
        # neural network which can place based on info in a category
        the given actionn with respect to the problem
        and basically generate where it should be placed or aborted
        subseted o f data label then nn
        if all data then not
        try different ways to group actions"""
        # feed past data in
        # given action categorize it into a certain category
        # in terms of usefulness
        """cons)ider how to use past problem ifnormation use past solutions to guide current solutions """
        distilbert_embedding=self.distil_berta_to_produce_word_embedding()
        chosen_action_group=self.ffn_1_cateogrizing_actions_into_types_of_strats()
        chosen_action_placvement_in_strat=self.ffn_2_ordering_actions_within_strats()
        # leverage patterns in questions to rank actions based on certain tools
        # add to this as we go through actions positioning them based on heurisitcs
        #input layer
        # vision transformer
        # to process images taken
        # while working on problem
        # deberta word embedding for the word action
        # output into strat ffn
        #https://huggingface.co/distilbert/distilroberta-base
        #output to ffn to 
        # ffn output is pick which strategy to place or not place action into
        # actions
        # what does output look like with 16 neurons
        # categorize actions
        # for use in different strategies
        # how to get labels
        # labels are actions we want in each category
        # based on some pattern or heuristic
        # heuristic/ patterns found by nn
        # which uses some input data
        # or something not sure what labels are yet
        #probably given actions chosen when sovling problem
        #output
        #labeled strats we have created or used 
        
        # could use a image transformer

        
    def auto_generate_strats_and_effects(self):
        """strategies 10 actions max
        16 different strats
        so 10 by 10 grid
        # and place action in it
        # choose not to place action
        # using context here
        and heursitcs and past problem data
        20 possible spaces actions could fall"""
        # strategies associated certain questions or tools?
        self.generate_more_context_qualtities_as_necesarry_using_tool_and_questions(self.strategy_methods_problem_tree_dic)
        self.consider_herusitic_or_general_principles_using_action_context_to_sort_and_select_actions(self.strategy_methods_problem_tree_dic)
        self.consider_past_action_data_with_nn_to_choose_and_sort_action(self.strategy_methods_problem_tree_dic)
    
    def store_auto_created_actions_and_strategies_for_problem_tree_sql(self):
        """ """
        import time
        current_time=time.time()
        for i12 in range(len(self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_strategies"])):
            max_different_effect_strategies=self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_strategies"][i12]
            max_different_objects_associated_with_action=self.strategy_methods_problem_tree_dic_max_difference["max_different_objects_associated_with_action"][i12]
            max_different_effect_list=self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_list"][i12]
            
            max_different_effect_strategies=self.clean_strs_before_input_into_sql(max_different_effect_strategies)
            max_different_objects_associated_with_action=self.clean_strs_before_input_into_sql(max_different_objects_associated_with_action)
            max_different_effect_list=self.clean_strs_before_input_into_sql(max_different_effect_list)
            current_time=self.clean_strs_before_input_into_sql(current_time)

            self.cur.execute( f""" INSERT INTO auto_strategy_table (problem_being_solved,objectts,actions,effects,time_found)
                         VALUES ('{str(self.problem_recorded)}','{str(max_different_objects_associated_with_action)}','{str(max_different_effect_strategies)}','{str(max_different_effect_list)}','{str(current_time)}');""")
        self.conn.commit()
    def auto_generate_and_problem_trees_from_problem_galaxy(self):
        """ automcialy generate web from text gathered from duckduckogo"""
        self.auto_generate_action_space_and_effects()
        self.auto_generate_strats_and_effects()
        self.store_auto_created_actions_and_strategies_for_problem_tree_sql()
        return automated_problem_galaxy_dic

    def make_all_this_usable_and_editable(self):
         """ MAKE IT EASY TO SWITCH TO SUB TREE problem when working on an action
         # DOne so you can immedately start labeing that sub tree 
         """
         
         # 2 make auto problem web and tree results loaded in
         # and make use of them
         # 1. show the auto_problem_tree in web_result box
         # auto display problem web blender on record problem
         # also upload problem web to current connected objects list box
         
         # 2. subprocess record problem operations
         # 3. run seleniium in background
         # 4. make all referecnes to probelm table reference 
         # 5. reference auto problem table
         
         # 6. display effects in problem envrionment
         # 4 start recording screen and tracking problem data
         # build nn from problem data

         # 7. fix other errors as we go
         # when loading in web results load in automcially
         # or loading in effects
         # have button to display effects
         #problme tree dictionary value strats
         
         
         
         
         
         

         
         # and the strats i select from auto are uploaded to the actual
         # display auto strats somewhere
         # strat table 
         # DISPLAY autogenerate strats in web results box
         # have option to show them in blender
         # SUBPROCESS THE RECORD PROBLEM OPERATIONS
         # SO CAN USE PROGRAM IN MEAN TIME
         # and make this faster
         # run selenium in the background
         # to fetch website data
         # with problem web just turn it all into auto problem web
         # improve results and use results

         
         #3 display effects in probvlem envrionmnet
         # of a selected strat in strategy table
         # select strat using a key you press
         # otherwise assume newest uploaded strat
        
         
         
    def display_effects_of_strategy_in_problem_enviornment(self):
        """ NEED TO ADD THIS TO THE BLENDER DISPLAY THING"""
        # show the qualitites impacted by a object being used
        #highlight object in use in action and highlight qualtites with different color
   
        
    def start_auto_generating_problem_data_from_recording_screen(self):
        """ WORK ON FUNCTIONS WE CREATED BELOW 
        and create table to record screen data etc
        to automically figure out what proiblem we are working on
        and automcially create and hsow strategies and proiblem envrionment
        for this problem"""
        
        
    def automatically_add_web_search_result_to_problem_web_and_transformations_list(self,problemm):
       """ this function will get results from various search browsers and then upload them to """
       import spacy
       self.automated_problem_galaxy_dic={}
       self.automated_problem_galaxy_dic[self.problem_recorded]= {"qualtity_list":self.problem_recorded[12:].split(" "),"transformation_list":[]}  # need to remove how do i
       self.nlp = spacy.load("en_core_web_sm")
       saved_text_from_website_list=self.retreive_problem_data_from_web(problemm)
       for text in saved_text_from_website_list:
           single_website_text=self.pre_process_text(text)
           final_sentence_list=self.divide_text_into_sentences(single_website_text)
           for sentence in final_sentence_list:
               spacy_dic=self.label_sentence_with_spacy(sentence)
               self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(spacy_dic)
               
       self.store_auto_created_galaxies_and_transformation_for_problem_web_in_sql()
       print(self.automated_problem_galaxy_dic)
       return self.automated_problem_galaxy_dic
    def sort_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(self):
        """ """
        sort_life_dags_dic={}
        
        return sort_life_dags_dic
        
    def auto_create_problem_web_and_galaxy(self,problemmm):
       """ """
       import psycopg2
       self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
       self.cur = self.conn.cursor()
       self.problem_recorded=problemmm
       automated_galaxy_dic=self.automatically_add_web_search_result_to_problem_web_and_transformations_list(problemmm)
       self.auto_generate_and_problem_trees_from_problem_galaxy()
       #sort_life_dags_dic=self.sort_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(strategy_action_space_with_effects_dic)
       #return sort_life_dags_dic

   

   #### PROBLEM TREE FUNCTIONS
   # think of permeant solution here not temp
   # make this work and be useful
   #automated_galaxy_dic=self.automatically_add_web_search_result_to_problem_web_and_transformations_list(self.problem_recorded)
   
   
         

             
         
     