# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 18:10:36 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
# transmit commands as a json maybe
class fill_single():
    
    def __init__(self):
        """ """
        
    
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
     question_striped=problemmm.strip()
     question_to_search_for=re.sub(r"\?","",question_striped)
     question_to_search_for=re.sub(r"\n"," ",question_striped)
     question_to_search_for=re.sub(r"\s+"," ",question_striped)

     question_to_search_for=question_to_search_for[:80]
     # run it as a subprocess or multi process
     

     #print(question_to_search_for)
     #input('checking whether prompt is ok here')

     #striped_problem=problem_recorded.strip()
     #problem_to_search_for=re.sub(r"\?","",striped_problem)
     firefox_options = FirefoxOptions()
     firefox_options.headless = True
     #try:
     driver= webdriver.Firefox(options=firefox_options)
     #except Exception as E:
     #    print(E)
     # need to fix firefox
     # driver= webdriver.Firefox()
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
                 p_tag_text=soup.get_text()[:700000]
                 #print(p_tag_text)
                 saved_text_from_website_and_link_list.append([str(p_tag_text),link_finals])
             
             except:
                 continue
         driver.quit()
         q.put(saved_text_from_website_and_link_list)
         #return saved_text_from_website_and_link_list
         
if __name__ == '__main__':
    from multiprocessing import Process, Queue
    import sys
    import json
    import re
    import spacy
    import time
    import psycopg2
    import pickle
    table_name="guide_person_positional_info_with_action_info"
    #person_comp_info_dic_with_action_list=sys.argv[1]
    #person_comp_info_dic_with_action_list=json.loads(person_comp_info_dic_with_action_list)
    fill=fill_single()
    fill.nlp = spacy.load("en_core_web_sm")
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
    
    
    problemm=f"what is the history of {link_item_title}"
    hist = Queue()
    p6 = Process(target=retreive_problem_data_from_web, args=(hist,problemm))
    p6.start()
    
    problemm="what is the biography of " + link_item_title
    bio = Queue()
    p7 = Process(target=retreive_problem_data_from_web, args=(bio,problemm))
    p7.start()
    
    problemm="what are the interests of " + link_item_title
    projects_int = Queue()
    p8 = Process(target=retreive_problem_data_from_web, args=(projects_int,problemm))
    p8.start()

    # now we will deal with questions relatingt o each idnivdual action
    for iterr, person_comp_info_dic_with_action in enumerate(person_comp_info_dic_with_action_list):
        
        #duck duck
        problemmm=person_comp_info_dic_with_action["action"]
        duckduck = Queue()
        p = Process(target=retreive_problem_data_from_web, args=(duckduck,problemmm))
        p.start()
        
        
        #get_sub_action_list_data_use_patent_data_and_other
        problemm="what are the steps i would take to " + person_comp_info_dic_with_action["action"]
        sub_action = Queue()
        p1 = Process(target=retreive_problem_data_from_web, args=(sub_action,problemmm))
        p1.start()
             
        #get_placement_of_other_people_places_and_things_related_to_action
        problemm="what are other things i should consider relating to " + person_comp_info_dic_with_action["action"]
        placement = Queue()
        p2 = Process(target=retreive_problem_data_from_web, args=(placement,problemmm))
        p2.start()
        
        # tools
        problemm="what are the tools i would use to " + person_comp_info_dic_with_action["action"]
        tools = Queue()
        p9 = Process(target=retreive_problem_data_from_web, args=(tools,problemmm))
        p9.start()
        
        
        #figure out all things you can use
        problemm="what is the location i would take to " + person_comp_info_dic_with_action["action"]
        locate = Queue()
        p3 = Process(target=retreive_problem_data_from_web, args=(locate,problemmm))
        p3.start()
        
        problemm="what are the resources i would take to " + person_comp_info_dic_with_action["action"]
        resource = Queue()
        p4 = Process(target=retreive_problem_data_from_web, args=(resource,problemmm))
        p4.start()
        print('hi')
        

        problemm="what are the skills that I would take to " + person_comp_info_dic_with_action["action"]
        skil = Queue()
        p5 = Process(target=retreive_problem_data_from_web, args=(skil,problemmm))
        p5.start()
        if iterr==0:
            bio=bio.get()
            hist=hist.get()
            projects_int=projects_int.get()
            p6.join()
            print('join1')
            p7.join()
            print('join2')
            p8.join()  
            print('join3')
               
            bio=fill.process_website_text_and_lemmaize(bio)
            print('bio')
            hist=fill.process_website_text_and_lemmaize(hist)
            print('hist')
            projects_int=fill.process_website_text_and_lemmaize(projects_int)
            print('projects_int')
            
            
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
        print('done all one round')
        
        ### duckduck
        
        person_comp_info_dic_with_action=fill.fill_in_dic_with_duck_duck_go(person_comp_info_dic_with_action,duckduck) #get effects by doing this
        print(person_comp_info_dic_with_action)    
        generalized_action=fill.generalize_action_words_to_make_it_more_applicable_to_people_and_useable(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
        person_comp_info_dic_with_action['generalized_action']=generalized_action
        print(generalized_action)
        
        ### sub action!                           
        person_comp_info_dic_with_action=fill.get_sub_action_list_data_use_patent_data_and_other(person_comp_info_dic_with_action,sub_action)# THIS IS KEY
        print(person_comp_info_dic_with_action)
        print('sub action sub list')
        
        ### placement!                            
        person_comp_info_dic_with_action=fill.get_placement_of_other_people_places_and_things_related_to_action(person_comp_info_dic_with_action,placement)
        print('think mutliple moves ahead')
        print(person_comp_info_dic_with_action)
        
        ### tools!
        print('placement of other people')
                               
        person_comp_info_dic_with_action=fill.identify_tools_to_solve_the_problem(person_comp_info_dic_with_action,tools)

        ### generic ask many question function
        
        person_comp_info_dic_with_action=fill.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,locate,"location_needed_to_take_action")
        
        person_comp_info_dic_with_action=fill.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,resource,"resources_required_to_perform_action")
        person_comp_info_dic_with_action=fill.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,skil,"skills_required_to_perform_action")
        person_comp_info_dic_with_action["work_experience"].insert(0,bio)
        person_comp_info_dic_with_action["work_experience"].insert(0,hist)
        person_comp_info_dic_with_action["projects_interested_in"].insert(0,projects_int)
        
        fill.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        fill.cur = fill.conn.cursor()
        
        fill.store_value_in_sql_table(person_comp_info_dic_with_action,table_name)
        #del fill.conn
        #del fill.cur



