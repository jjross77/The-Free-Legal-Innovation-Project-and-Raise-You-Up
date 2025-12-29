# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:17:09 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

class document_vectorizer():

    

    def __init__(self):
        from transformers import  DebertaModel
        from transformers import DebertaTokenizerFast
        import psycopg2
        import torch
        import numpy as np
        #from  Pos_model_trainer import network
        super().__init__()
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.contexualzed_sentennce_list = []
        self.model= DebertaModel.from_pretrained("microsoft/deberta-base").to("cuda")
        self.tokenizer = DebertaTokenizerFast.from_pretrained("microsoft/deberta-base",truncation_side="left")
        self.sentence_info = []
        self.pos_word_list= []
        self.document_name = ""
        self.document_verb= []
        self.document_noun=[]
        self.torch_catche= torch.cuda.empty_cache()
        self.document_name = ""
        self.document_id=""
        self.final_sentence_info_list=[]
        self.max_value=1.0
        self.npmax=np.argmax(self.max_value) # find pytorch arg max function
        self.unwanted_characters=[".","?","[","]","(",")"]

        
        self.type_of_document=""
        self.document_law=[]
        
    def init_pos_model(self):
        import torch

        from pos_model_class import network

        self.pos_model=network(768, 586, 3).to("cuda")
        pos_state_dic = torch.load(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\model_pos.pth")
        self.pos_model.load_state_dict(pos_state_dic)
    def init_non_sentence_model(self):
        import torch

        from pos_model_class import network
        
        self.unwanted_model=network(768, 1000, 2).to("cuda")
        un_state_dic = torch.load(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\un_wanted_model.pth")
        self.unwanted_model.load_state_dict(un_state_dic)
    
    def init_law_model(self):
        import torch


        from pos_model_class import network
        
        self.law_model=network(768, 1000, 2).to("cuda")
        law_state_dic = torch.load(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\legislation_model.pth")
        self.law_model.load_state_dict(law_state_dic)
    
    def init_proper_noun_model(self):
        import torch
        from pos_model_class import network
        
        self.proper_noun_model=network(768, 1000, 2).to("cuda")
        proper_noun_state_dic = torch.load(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\proper_noun_model.pth")
        self.proper_noun_model.load_state_dict(proper_noun_state_dic)
        
    
    
        
        
        
            



        #print(self.model.eval())
    def get_next_document(self,previous_document_id):
        """ we use this to find the next document in the case_database after the first one and so on""" 
        
                          
        self.cur.execute(f""" SELECT ID, case_name, full_case_text,cited_cases
                          FROM full_cases
                          WHERE ID <'{int(previous_document_id)}'
                          ORDER BY ID DESC
                          LIMIT 1;""")
        cur_result4= self.cur.fetchall()
        self.document_name=cur_result4[0][1]
        self.document_id= cur_result4[0][0]
        document_text=cur_result4[0][2]
        self.document_law=cur_result4[0][3]

        
        # will need to remove duplicates of sentences at one point


        
        
        return document_text # make sure to instantiate a new class when using this

                          
 

    def decide_which_document_to_upload(self):
        """ Look thru which document we have in the embedding database and start on the list so we don't repeat"""
        self.cur.execute(f""" SELECT ID, document_name,sentence_number
                          FROM embedding_sentences
                          ORDER BY ID DESC 
                          LIMIT 1 ;""")
                         
        cur_result= self.cur.fetchall()
        self.document_name=None

        if cur_result: # not first document
            self.document_name=cur_result[0][1]
            self.document_id= cur_result[0][0]
            


            
        return self.document_name
    # find the last document whcih we have done.

        
        
    def upload_text(self):
        """ Bring the text from the sql database into the python program"""
        
        if self.document_name !=None:
            print(self.document_name)
            self.cur.execute( f""" SELECT ID, case_name, full_case_text,cited_cases
                              FROM full_cases 
                              WHERE case_name ILIKE '{self.document_name}'
                              LIMIT 1;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result2= self.cur.fetchall()

            document_text=cur_result2[0][2]
            self.document_law=cur_result2[0][3]

            
            
        if self.document_name == None: # first document
            self.cur.execute( f""" SELECT ID, case_name, full_case_text,cited_cases
                              FROM full_cases 
                              ORDER BY ID DESC 
                              LIMIT 1 ;""")
            cur_result2= self.cur.fetchall()
            self.document_name=cur_result2[0][1]
            self.document_id= cur_result2[0][0]
            document_text=cur_result2[0][2]
            self.document_law=cur_result2[0][3]
            
           
            


            

   
        return document_text
        




    def pre_process_text(self, document):
        """ what is needed to reduce the size and make the text consistent before it goes in the network"""
        import re
        import unicodedata
        """ remove extra spacing, names, tabs, and other unwanted values"""
        f= re.sub("\n"," ", document)
        f= re.sub("\t"," ", f)
        f= re.sub("\r"," ", f)
        f=re.sub(r" \s+", r" ", f)
        f = unicodedata.normalize("NFKD", f)
        return f
        # repeat for law_document
    def pre_process_law(self):
        """ used to format the law in the document """
        import unicodedata
        import re
        law= re.sub("\n"," ", self.document_law)
        law= re.sub("\t"," ", law)
        law= re.sub("\r"," ", law)
        law=re.sub(r" \s+", r" ", law)
        law = unicodedata.normalize("NFKD", law)
        self.document_law=law
        
        
 
        

    def divide_doc_into_sentences(self, document):
        """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
        from nltk.tokenize import sent_tokenize
        #from nltk.tokenize import word_tokenize
        sentences = sent_tokenize(document)
        
        return sentences
    
    def pre_law_list_creator_0(self):
        import re
        law_list=self.document_law
        #labeled_law_list=[]
        #broken_down_law_list=[]
        labeled_law_dic={}
        #special list for characters like this 13 CPC (4th) 156 seperate into words but only if all are present in the given sentence 
        # can we 

        if law_list:
            law_list=law_list[1:]
            law_list="#0"+law_list+"#1000"
            # only getting odd matches need to fix this
            # better way to seperate the string
            # maybe find someway to double each of the indicators
            
            law_list=re.sub(r"#\d+", r"#12#12",law_list)
            
            law_list=re.findall(r"#\d+ .*?#\d+",law_list)
            #print(law_list)
            
            #take case name perform operation ensure the names do not come up
            
            # what to do if we start geting proper nouns that don't belong to a case, we will need to check the data we are feeding in and make sure when we train the nextwork we don't do this accdientally 

            for iiii, law in enumerate(law_list):
                
                law2=re.sub(r"#\d+",r"",law)
                law2=re.sub(r"\d\d\d\d-\d\d-\d\d", "",law2)
                law2= re.sub(r"\(not available on CanLII\)","",law2)
                law2=re.sub(r"\s\s+", r" ", law2)
                law2=re.sub(r"\(",r"",law2)
                law2=re.sub(r"\)",r"",law2)
                law2=re.sub(r"\[",r"",law2)
                law2=re.sub(r"\]",r"",law2)
                law2=re.sub(r"\.",r"",law2)
                law2=law2.split(",")

                for  iiiii, lawww in enumerate(law2):
                    temp_sequence_list=[]
                    found_num=re.search(r"\d\d",lawww)
                    #print(found_num)
                    if found_num:
                        lawwwww=lawww.split(" ")
                        for word in lawwwww:
                            if word:
                                temp_sequence_list.append(word)

                                
                            #print(word)

                                
                        #broken_down_law_list.append(temp_sequence_list)
                        labeled_law_dic[f"broken{iiii}:{iiiii}"]=temp_sequence_list
 
                        continue
                    lawww=lawww.strip()
                    #labeled_law_list.append(lawww)
                    labeled_law_dic[f"{iiii}:{iiiii}"]=lawww
        return labeled_law_dic
    
    
    
    def generate_contexualized_sentences(self, sentences):
        """ need to keep context for when inputting text into the tokenizer"""
        import re
        find_word_pattern = re.compile(r"\w+")

        for i,  sentence_2 in enumerate(sentences):
            if i ==0:
                existing_sentences= " "

            words_remove_from_sentence = find_word_pattern.findall(existing_sentences)
            finding_words_to_remove_len =len(words_remove_from_sentence)
            #print(finding_words_to_remove_len)
            
            if finding_words_to_remove_len > 440:
                
                
                word_to_be_removed_for_next_iteration= words_remove_from_sentence[-440]
                
                #print(word_to_be_removed_for_next_iteration)
                
                pattern_to_find_word_to_be_kept = re.compile(f"{word_to_be_removed_for_next_iteration}")
                
                identifier_for_removing_from_string=re.search(pattern_to_find_word_to_be_kept, string=existing_sentences)
                
                end_of_word_needed_segment_sentence= identifier_for_removing_from_string.span()[1]
                existing_sentences=existing_sentences[end_of_word_needed_segment_sentence:]
            self.contexualzed_sentennce_list.append([existing_sentences,sentence_2])
            existing_sentences= existing_sentences + " " + f"{sentence_2}"
            

        return self.contexualzed_sentennce_list
            
        
      
    def tokenize_document(self, sentence_3):# this is a single sentence using the contexualized sentnece list
        #import re
        #finding_start_of_second_sentence=re.compile(r"1")
        inputs = self.tokenizer(sentence_3[0], sentence_3[1], return_tensors="pt", truncation=True, return_token_type_ids=True).to("cuda")
        ids_of_tokens=inputs['input_ids'].tolist()
        token_sentence_ids=inputs['token_type_ids'].tolist()
        [token_sentence_ids] = token_sentence_ids
        [ids_of_tokens] = ids_of_tokens
        token_values_of_ids=self.tokenizer.convert_ids_to_tokens(ids_of_tokens)
        #print(token_values_of_ids)
        # need to make sure it's trucating on the left
        #strwoo=(str((inputs['token_type_ids'])))
        #tokens_in_current_sentence= re.findall(finding_start_of_second_sentence, string=strwoo)
        #amount_of_tokens=len(tokens_in_current_sentence)-1  # for final token that will be labeled as 
        self.sentence_info=[token_values_of_ids,ids_of_tokens,token_sentence_ids]
        # goal is to save the embeddings with the values from the tuple
        #count the number of zeroes, and we erase the last value of the 1's and we mark this lists place in the token count and then we run it thru the model and append the vectors of each word to the list
        count_of_first_sentence_length=self.sentence_info[2].count(0)
        self.sentence_info.append(count_of_first_sentence_length)
        
        self.sentence_info[0]=self.sentence_info[0][count_of_first_sentence_length:-1]
        self.sentence_info[1]=self.sentence_info[1][count_of_first_sentence_length:-1]
        self.sentence_info[2]=self.sentence_info[2][count_of_first_sentence_length:-1]

        
        
        #print(amount_of_tokens)
        del inputs["token_type_ids"]
        
        
       
        return inputs, self.sentence_info

       
    

        
        
    
        
    def generate_embeddings(self, inputs):
        #from transformers import  DebertaModel
        #model = DebertaModel.from_pretrained("microsoft/deberta-base").to("cuda")
        """ converting text to embeddings using a pre-trained deberta model"""
        new_output = self.model(**inputs)
        new_output=new_output["last_hidden_state"]
        new_output=new_output[0]
        new_output= new_output[self.sentence_info[3]:-1]
        self.torch_catche
        

        
        
        #print(new_output)
        new_output_list=new_output.tolist()  

        self.sentence_info.append(new_output_list)
        self.sentence_info[4]=new_output_list

        
        embedding_information_list=self.sentence_info
        #del new_output
        #del output
        #del tokenizer_ctrl
        
        
        
        
       # remove the amount at the front and the last token and align embeddings in this way
        return embedding_information_list, new_output
    

                #current_case_name=re.search(r"(.*) v\.? (.*),", self.document_name)

               

                
        
    #exclude document below a certain character count
    def pre_law_data_creator_1(self,sentence_4):
        import re
        """ find all words that correspond to law words before we scrap them for pos and save them as labeled data for training law model"""
        self.document_law
        found_law_in_document=[]
        for mm in re.finditer(r"((\s\(?[A-Z\.,][A-Za-z\.\,\'\&\-.\(\)é]*)+\(?\)?(\s[a-z\.&]+)?\)?\)?\(?(\s[A-Z][a-z\.]*)*\)?\sv\.?(\s*\(?[A-Z\.][A-Za-z\.\'\&\-\’é]*)+\)*(\s[A-Za-z\-]+)*(\s[A-Z]*[\’a-zA-Z\.\'\&-]*)+\)?)",sentence_4):
            #print(mm.group(0))
            in_remover = re.search(r"(.*)(\s?[iI]n)+(\s.*)",mm.group(0)) 
            if in_remover:
                #print(in_remover.group(0))
                #print(in_remover.group(3))

                in_remover=in_remover.group(3)

                leng_of_part_in_doc= int(mm.end())-int(mm.start())
                length_to_remove= leng_of_part_in_doc- len(in_remover)
                #print(length_to_remove)
                
                new_start=int(mm.start())+length_to_remove
                
                if sentence_4[new_start:int(mm.end())]==in_remover:
                    law_words=in_remover.split(' ')
                    #law_words= re.findall("\w+\.?", in_remover)
                    if law_words:
                        for law13 in law_words:
                            if law13:
                                law14=re.sub(r" ", r"" ,law13)
                                found_law_in_document.append(law14)
                                
                            
                        
                        continue
                    #found_law_in_document.append([new_start,int(mm.end()),in_remover])
                    
                continue 

            if sentence_4[int(mm.start()):int(mm.end())]==mm.group(0):
                #law_words= re.findall("\w+\.?", mm.group(0))
                law_words=mm.group(0).split(' ')

                if law_words:
                    for law12 in law_words:
                        if law12:
                            law13=re.sub(r" ", r"" ,law12)
                            found_law_in_document.append(law13)
                        
        return found_law_in_document
                        
                
                #found_law_in_document.append([int(mm.start()),int(mm.end()),mm.group(0)])
                
                

    def pre_law_data_creator_2(self,sentence_4,found_law_in_document, labeled_law_dic):
        import re
        
        for key,value in labeled_law_dic.items():
            
            if "broken" in key: 
                #law_len_2=0
                correct_counter=0
                temp_save_list=[]
                #print(value)
                len_of_word_list=len(value)-1
                #print(len_of_word_list)
                #if len_of_word_list==2:
                #    len_of_word_list=3
                    
                if len_of_word_list==1:
                    len_of_word_list=2
                    #print(len_of_word_list)
                    #law_len_2=1
                    
                #print(len_of_word_list)
                for match in value:
                    law_words3=re.search(rf"{match}",sentence_4)
                    if law_words3:
                        # need to save the law woreds somehow
                        correct_counter+=1
                        #print(match)

                        #print(correct_counter)
                        #print(law_words3.group(0))
                        law_words4=law_words3.group(0)
                        #law_words4=re.sub(r" ", r"" ,law_words4)
                        temp_save_list.append(law_words4)
            #if law_len_2==1:
            #    correct_counter=correct_counter+1

                    
                    
                        
                        
                if correct_counter >= len_of_word_list:
                    #print('counter is greater')
                    #print(f" this the counter amount{correct_counter}")
                    #print(f" this is the len_of_word_list")
                    #print('woooo man')
                    for save in temp_save_list:
                        #print(save)
                        found_law_in_document.append(save) 
                    continue
                continue
            
           
            
            
            else:
                #print(value)
                #print(value)
                law_words1=re.search(rf"{value}",sentence_4)
                #print('meow')

                if law_words1:
                    
                    law_words2=law_words1.group(0)
                    law_words2=law_words2.split(" ")
                    #print(law_words2)
                    for worddd in law_words2:
                        worddd=re.sub(r"\.",r"",worddd)

                        # print(worddd)
                        #print(worddd)
                        found_law_in_document.append(worddd)
 
                    #law_words2=re.sub(r" ", r"" ,law_words2)
                    # need to get rid of side spaces
                    #law_words2= re.findall("\w+\.?",law_words1.group(0))
                    #if law_words2:
                    #found_law_in_document.append([int(m.start()),int(m.end()),law_matches])
                

            
  
        return found_law_in_document
    
    
 
    
    def reduce_gpu_load(self,new_output):
        """use for when running sparrow embeddings thru deberta to ensure vram is not over used"""
        del new_output
    
        
        
    def pos_data_creator(self, sentence_4):
        """ getting pos tags from spacy model to later train a pos tagger that can be used for our deberta model"""
        self.pos_word_list=[]
        proper_noun_list=[]
        #python -m spacy download en_core_web_trf
        #import spacy
        #nlp = spacy.load("en_core_web_trf")
        import en_core_web_trf
        nlp = en_core_web_trf.load()
        pos_unmodified_sentence = nlp(sentence_4)
        #print([ (w.text, w.pos_) for w in doc])
        for part_of_speech_parts in pos_unmodified_sentence:


            if part_of_speech_parts.pos_ == "NOUN": #or  part_of_speech_parts.pos_ == "PROPN": #or part_of_speech_parts.pos_ == "PRON":
                self.pos_word_list.append([part_of_speech_parts.text, "NOUN","No"]) # the position 2 in the list of either no or yes corresponds to whether the word has been designated as a propr noun

                continue
    
            if part_of_speech_parts.pos_ == "VERB":
                self.pos_word_list.append([part_of_speech_parts.text,"VERB","No"])
                continue
            
            if part_of_speech_parts.pos_ == "PROPN":
                self.pos_word_list.append([part_of_speech_parts.text,"OTHER","Yes"])
                continue
            self.pos_word_list.append([part_of_speech_parts.text,"OTHER","No"])

  
        self.sentence_info.append(self.pos_word_list)
        self.sentence_info[5]=self.pos_word_list
        
        return self.sentence_info, pos_unmodified_sentence
    
    
    
    def law_data_creator(self,pos_unmodified_sentence,found_law_in_document): # need to fix this next for law
        """matching tokens with law tags":"""
        
        law_word_list=[]
        #print(found_law_in_document)
        #need to create range_list
        #print(found_law_in_document)
        for part_of_speech_parts in pos_unmodified_sentence:
            #print(f" this is the pos  {part_of_speech_parts.text}")
            label=""
            #print(part_of_speech_parts.text)
            #print(found_law_in_document)
            # need to iteraste thru the list to get it to work
            
            if part_of_speech_parts.text in found_law_in_document:
                label="YES"
                law_word_list.append([part_of_speech_parts.text,label])
                continue
            
            
            if part_of_speech_parts.pos_ == "ADJ" or  part_of_speech_parts.pos_ == "ADP" or  part_of_speech_parts.pos_ == "ADV" or  part_of_speech_parts.pos_ == "AUX" or  part_of_speech_parts.pos_ == "CONJ" or  part_of_speech_parts.pos_ == "CCONJ" or  part_of_speech_parts.pos_ == "DET" or  part_of_speech_parts.pos_ == "INTJ" or  part_of_speech_parts.pos_ == "VERB" or  part_of_speech_parts.pos_ == "SCONJ" or  part_of_speech_parts.pos_ == "PUNCT" or  part_of_speech_parts.pos_ == "PRON" or  part_of_speech_parts.pos_ == "PART" or  part_of_speech_parts.pos_ == "X" :
                label= "NO"
                law_word_list.append([part_of_speech_parts.text,label])
                continue
            
           
            if label =="":
                label="scrap"
                law_word_list.append([part_of_speech_parts.text,label])
   
        return law_word_list
    
    
    def law_matcher_and_uploader(self,law_word_list):
        import copy
        import re
        counterr=0
        #print(law_word_list)
        #print(len(law_word_list))
        #print(len(self.sentence_info[5]))
        # need to check if the word list is coming together correctly
        # checking law_matcher and law_data)creator
        law_word_list_of_only_words= [law_word[0].lower() for law_word in law_word_list]
        un_used_law_list=copy.deepcopy(law_word_list_of_only_words)

        #print(law_word_list_of_only_words)
        #print(len(law_word_list_of_only_words))
        for i, token in enumerate(self.sentence_info[0]):
            if "Ġ" in token:
                token=token.replace("Ġ", "")  
            token=token.lower()
            if token in law_word_list_of_only_words:

                counterr+=1
                index_of_word_law=law_word_list_of_only_words.index(token)
                law_word2=law_word_list[index_of_word_law][0] 
                law_label=law_word_list[index_of_word_law][1] 
                un_used_law_list[index_of_word_law]=""

                if law_label=="scrap":
                    #print(f"this word we are scraping")
                    continue
                #print(law_word)
                #print(law_label)
                #print(token)
                #print(counterr)

                self.cur.execute( f""" INSERT INTO law_labels (word,embedding,law_tag)
                            VALUES ('{str(law_word2)}','{str(self.sentence_info[4][i])}','{str(law_label)}');""")

                continue
            # NEED TO MAKE THIS WORK FOR LAW MATCHER
            else: # need to figure out how to do we breaks so that we don't lose words
            #for not used words
                #print(token)
                solved=0
                for letter in token:
                    if letter in self.unwanted_characters:
                        break
                    if solved==1:
                        break
                    
                    #print(letter)
                    
                    for word_4 in un_used_law_list:
                        
                        if word_4 =="":
                            #print('gotta a blank')
                            continue

                        if letter in word_4:
                            #print(f"{letter} has been matched with{word_1} ")
                            try:
                                token_in_word=re.search(rf"{token}",word_4)
                            except:
                                #print(token)
                                #print('we have a error houston')
                                break
                            if token_in_word:
                                #print(f"{word_1} has token inside of it {token} ")
                                #get initial piece and assign it the proper values 
                                
                                word_part_associated_with_token=word_4[token_in_word.span(0)[0]:token_in_word.span(0)[1]]
                                #print(f"{word_part_associated_with_token} this is the part of the word")
                                # need to think this  thru whether it will find the unused word list correctly
                                # lets test it
                                index_of_law=un_used_law_list.index(word_4)
                                #modify this index and produce an index next to it
                                label=law_word_list[index_of_law][1]
                                #print(pos_tag)
                                
                                #proper_noun_tag=self.sentence_info[5][index_of_word][2]
                                #print(proper_noun_tag)
                                
                                self.cur.execute( f""" INSERT INTO law_labels (word,embedding,law_tag)
                                            VALUES ('{word_part_associated_with_token}','{str(self.sentence_info[4][i])}','{str(label)}');""")
                                

                                # now need to modify the list and apply the labels to this
                                #.append new part and modify existing part this next stage we append the first part we modify
                                # incredibly important to match the i
                                if token_in_word.span(0)[0]==0:
                                    
                                    
                                    
                                    all_letters_to_right_of_match=word_4[token_in_word.span(0)[1]:]
                                    #print(all_letters_to_right_of_match)
                                    law_word_list.append([all_letters_to_right_of_match,label])
                                    law_word_list_of_only_words.append(all_letters_to_right_of_match)
                                    un_used_law_list.append(all_letters_to_right_of_match)
                                    solved=1
                                    break
                                    
                                    
                                    #right of end
                                    
                                if token_in_word.span(0)[0]!=0:
                                    
                                    
                                    #left of start
                                    all_letters_to_left_of_match=word_4[:token_in_word.span(0)[0]]
                                    #print(all_letters_to_left_of_match)
                                    law_word_list.append([all_letters_to_left_of_match,label])
                                    law_word_list_of_only_words.append(all_letters_to_left_of_match)
                                    un_used_law_list.append(all_letters_to_left_of_match)

                                    
                                    #right of start
                                    all_letters_to_right_of_match=word_4[token_in_word.span(0)[1]:]
                                    #print(all_letters_to_right_of_match)
                                    law_word_list.append([all_letters_to_right_of_match,label])
                                    law_word_list_of_only_words.append(all_letters_to_right_of_match)
                                    un_used_law_list.append(all_letters_to_right_of_match)
                                    solved=1
                                    break
                                # how does this interact with the original


                            continue
                        continue

       
                    
        self.conn.commit()
       
                    

    def pos_and_pn_matcher_and_uploader(self): # need to make this more robust to ensure no information is lost in the process
        """ matching tokens with pos tags to generate data for labels and pos ffn, need to match all of these and push to pos match database"""
        import re
        import copy
        #counterr=0
        word_list=[word[0].lower() for word in self.sentence_info[5]]
        un_used_word_list=copy.deepcopy(word_list)
        #print(len(word_list))

        for i, token in enumerate(self.sentence_info[0]):
            #if token in unwanted_characters:
            #    continue
            # need to check if the embedding is lined up
            
        
            if "Ġ" in token:
                token=token.replace("Ġ", "")

            token=token.lower()
            
            if token in word_list:
                index_of_word=word_list.index(token)
                word=self.sentence_info[5][index_of_word][0]
                pos_tag=self.sentence_info[5][index_of_word][1]
                proper_noun_tag=self.sentence_info[5][index_of_word][2]
                un_used_word_list[index_of_word]=""
                
                #print(word)
                #print(pos_tag)
                #print(proper_noun_tag)
                #print(token)
                #counterr+=1
                #print(counterr)

 
                self.cur.execute( f""" INSERT INTO pos_labels (word,embedding,pos_tag)
                            VALUES ('{word}','{str(self.sentence_info[4][i])}','{str(pos_tag)}');""")
                            
                self.cur.execute( f""" INSERT INTO proper_noun_labels (word,embedding,proper_noun_labels)
                            VALUES ('{word}','{str(self.sentence_info[4][i])}','{str(proper_noun_tag)}');""")
                

                continue
            else: # need to figure out how to do we breaks so that we don't lose words
            #for not used words
                #print(token)
                solved=0
                for letter in token:
                    if letter in self.unwanted_characters:
                        break
                    if solved==1:
                        break
                    
                    #print(letter)
                    
                    for word_1 in un_used_word_list:
                        
                        if word_1 =="":
                            #print('gotta a blank')
                            continue

                        
                        if letter in word_1:
                            #print(f"{letter} has been matched with{word_1} ")
                            try:
                                token_in_word=re.search(rf"{token}",word_1)
                            except:
                                #print(token)
                                #print('we have a error houston')
                                break
                            if token_in_word:
                                #print(f"{word_1} has token inside of it {token} ")
                                #get initial piece and assign it the proper values 
                                
                                word_part_associated_with_token=word_1[token_in_word.span(0)[0]:token_in_word.span(0)[1]]
                                #print(f"{word_part_associated_with_token} this is the part of the word")
                                # need to think this  thru whether it will find the unused word list correctly
                                # lets test it
                                index_of_word=un_used_word_list.index(word_1)
                                #modify this index and produce an index next to it
                                pos_tag=self.sentence_info[5][index_of_word][1]
                                #print(pos_tag)
                                
                                proper_noun_tag=self.sentence_info[5][index_of_word][2]
                                #print(proper_noun_tag)
                                
                                self.cur.execute( f""" INSERT INTO pos_labels (word,embedding,pos_tag)
                                            VALUES ('{word_part_associated_with_token}','{str(self.sentence_info[4][i])}','{str(pos_tag)}');""")
                                
                                            
                                self.cur.execute( f""" INSERT INTO proper_noun_labels (word,embedding,proper_noun_labels)
                                            VALUES ('{word_part_associated_with_token}','{str(self.sentence_info[4][i])}','{str(proper_noun_tag)}');""")

                                # now need to modify the list and apply the labels to this
                                #.append new part and modify existing part this next stage we append the first part we modify
                                # incredibly important to match the i
                                if token_in_word.span(0)[0]==0:
                                    
                                    
                                    
                                    all_letters_to_right_of_match=word_1[token_in_word.span(0)[1]:]
                                    #print(all_letters_to_right_of_match)
                                    self.sentence_info[5].append([all_letters_to_right_of_match,pos_tag,proper_noun_tag])
                                    word_list.append(all_letters_to_right_of_match)
                                    un_used_word_list.append(all_letters_to_right_of_match)
                                    solved=1
                                    break
                                    
                                    
                                    #right of end
                                    
                                if token_in_word.span(0)[0]!=0:
                                    
                                    
                                    #left of start
                                    all_letters_to_left_of_match=word_1[:token_in_word.span(0)[0]]
                                    #print(all_letters_to_left_of_match)
                                    self.sentence_info[5].append([all_letters_to_left_of_match,pos_tag,proper_noun_tag])
                                    word_list.append(all_letters_to_left_of_match)
                                    un_used_word_list.append(all_letters_to_left_of_match)

                                    
                                    #right of start
                                    all_letters_to_right_of_match=word_1[token_in_word.span(0)[1]:]
                                    #print(all_letters_to_right_of_match)
                                    self.sentence_info[5].append([all_letters_to_right_of_match,pos_tag,proper_noun_tag])
                                    word_list.append(all_letters_to_right_of_match)
                                    un_used_word_list.append(all_letters_to_right_of_match)
                                    solved=1
                                    break
                                # how does this interact with the original


                            continue
                        continue

       
                    
        self.conn.commit()
        
    def non_sentence_matcher_and_uploader(self,label):
        """ matching tokens with pos tags to generate data for labels and pos ffn, need to match all of these and push to pos match database"""
        for i, token in enumerate(self.sentence_info[0]):
            token=str(token).replace("\'","")
            token=token.replace("\"","") 
            if "Ġ" in token:
                token=token.replace("Ġ", "")

                
            self.cur.execute( f""" INSERT INTO non_sentence_labels (word,embedding,labels)
                        VALUES ('{token}','{str(self.sentence_info[4][i])}','{label}');""")

        self.conn.commit()
    
        
  
        
    def run_values_thru_unwanted_sentences(self,output): # we are going to use this 
         """ feed in all sentences in their embedding format and output only sentences that are cleaned and want to work with"""
         counterrr=0
         returnn="false"
         #print(f" this should be the number of wordss int he sentence {len(output)}")
         for  word_3 in output:
             un_pred=self.unwanted_model.forward(word_3)
             # 0 represents not wanted, 1 represents wanted
             un_pred=un_pred.tolist()
             #prediction=max(pos_predictions)
             prediction=un_pred.index(max(un_pred))
             if prediction == 0:
                 counterrr+=1
             if counterrr==len(output):
                 returnn="true"
         return returnn
        
                 
                 #skip sentence
                     
               
    
        
        

    def run_values_thru_law_model(self,output):
        """run all the token thru network to identify where law is in various sentences to be used for later"""
        self.law_list=[]
        for i, word_2 in enumerate(output):
            pos_predictions=self.law_model.forward(word_2)
            pos_predictions=pos_predictions.tolist()
            #prediction=max(pos_predictions)
            prediction=pos_predictions.index(max(pos_predictions))
            
            #print(prediction)
            if prediction == 1:
                self.law_list.append(self.sentence_info[0][i]) # words
                #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech

            #if prediction==0:
        return self.law_list
    
    def run_values_thru_replace_proper_nouns(self,output):
        """ find the pn in the document passing tokens thru this ffn this is for preprocessing documents"""
        for i, word_2 in enumerate(output):
            pos_predictions=self.proper_nouns_model.forward(word_2)
            pos_predictions=pos_predictions.tolist()
            #prediction=max(pos_predictions)
            prediction=pos_predictions.index(max(pos_predictions))
            
            #print(prediction)
            if prediction == 1:
                # we will change the word to this in the text
                word ="Propernoun"
                #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech

            #if prediction==0:
        return updated_sentence
    
        
                
                
        
        
        
        
    def run_values_thru_pos_model(self,output): 
        """run a sentence embedding output of a transformer thru and remove all none Noun and verb embeddings from the sentence"""
        final_word_list=[]
        final_embedding_list=[]
        final_pos_list=[]
        for iiii, word_2 in enumerate(output):
            pos_predictions=self.pos_model.forward(word_2)
            pos_predictions=pos_predictions.tolist()
            #prediction=max(pos_predictions)
            prediction=pos_predictions.index(max(pos_predictions))
            
            #print(prediction)
            if prediction == 1 or prediction == 0:
                #final_sentence_info_list
                final_word_list.append(self.sentence_info[0][iiii]) # words
                #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech
                final_embedding_list.append(self.sentence_info[4][iiii]) #embeddings
                final_pos_list.append(prediction)
                
        final_word_list=str(final_word_list).replace("\'","")
        final_word_list=final_word_list.replace("\"","")        
        self.final_sentence_info_list.append(final_word_list) # words
        self.final_sentence_info_list[0]=final_word_list
        
        self.final_sentence_info_list.append(final_embedding_list) #embeddings
        self.final_sentence_info_list[1]=final_embedding_list

        self.final_sentence_info_list.append(final_pos_list)
        self.final_sentence_info_list[2]=final_pos_list

         
        del output
            
        #WILL ALSO NEED TO CHECK THIS
        return self.final_sentence_info_list
    def run_values_thru_firac_model():
        """ this value will be used to diagnosis whether a token is a fact issue or analysis sentence."""
        
        
    

    

   

    def upload_sentence_to_sentence_embedding_database(self, sentence_number):
        """EVENTUALLY WILL ADD A COLUMN FOR FIRAC, BUT THIS IS UPLOADING THE EMBEDDINGS WITH THERE POS """
        self.cur.execute( f""" INSERT INTO embedding_sentences (id,words,embeddings,pos,document_name,sentence_number)
                    VALUES ('{self.document_id}','{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.document_name)}','{sentence_number}');""")
        

        #WILL NEED TO CHECK THIS AGAIN TORROOW
        #clean the document here as well
        # 


class document_FIRAC_labeler():
    def __init__(self):
        """ this class will upload embeddings, create sentences matrixes,  cosign simalrity these matrixes, save the results, and label sentences based on these results as fact issue, argument and so on"""
        import psycopg2
        import torch
        from torch.nn import CosineSimilarity

        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        
        self.sim_list= []
        self.cos=CosineSimilarity(dim=0).to('cuda')
        self.verb_dic_comparison_word= {}
        self.noun_dic_comparison_word= {}
        # how to create firac labeler, simple we  upload the embeddings, we mathc them find the highest mathces in the document in between factum and case and case and summary
        # this is how we will create the fact patterns
        # do we do factums now or later we will do them now i think
        # we need to pre-train deberta model
        # we need to get firac labels most important step
        # need to pretrain deberta model to mkae sure embeddings are good, if working directly with embeddings to get matches
        # so next step is train deberta
        # need to create doc to doc model which depends on finidng different sections in factums, need to create argument finder
        #

       

    def case_name_matcher(self, original_case_name, database_to_match_to):
        """get most similar case names from the two databases that are most likely to be related, parsing the unstructured data"""
        import re
        case_name_to_search=re.search(r"",original_case_name ) # we want to find some underlying characteristic that would allow us to find another case
        
        self.cur.execute( f""" SELECT ID, case_name, full_case_text
                          FROM {database_to_match_to} 
                          WHERE document_name ILIKE '{case_name_to_search}'
                          ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
        for results in cur.fetchall():
            print('hi')
        
        
        
    
        
    def upload_embeddings_from_case_database(self, type_of_document_database,  case_name,type_of_document_database_2="", case_name_2=""):
        """upload information of a case, factum, or summary from the sql database"""
        
        if case_name_2 =="":
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number, document_name
                              FROM {type_of_document_database} 
                              WHERE document_name ILIKE '{case_name}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            
            cur_result2= self.cur.fetchall()
            
            return cur_result2


            
           
        
        
        if case_name_2 !="":
            
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name
                              FROM {type_of_document_database} 
                              WHERE document_name ILIKE '{case_name}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result2= self.cur.fetchall()

            #document_embeddings_2=cur_result2[0][2]
            
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name
                              FROM {type_of_document_database_2} 
                              WHERE document_name ILIKE '{case_name_2}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result3= self.cur.fetchall()

            #document_embeddings_3=cur_result3[0][2]
            return cur_result2, cur_result3
            
            
            
  
    def transform_to_pos_format(self,doc):
        import json
        #import re
        # will import the list of all three varabiles embedding, pos, word
        import torch
        doc_noun=[]
        doc_verb=[]
        doc_name=doc[0][4]
        
        for i, sentence in enumerate(doc):
            sentence_noun=[]
            sentence_verb=[]
            verb_matrix= []
            noun_matrix= []
            embeddings=json.loads(sentence[0])
            # embeddings=torch.Tensor(embeddings).to("cuda")
            pos_list=json.loads(sentence[1])
            words_list=sentence[2][1:-1]
            words_list=words_list.replace(",", "")
            words_list=words_list.split()
            #print(len(words_list))
            #print(len(pos_list))
            #print(len(embeddings))

            #sentence_number=int(sentence[3])
            #print(sentence[3])
            for pos,words,embedding in zip(pos_list,words_list,embeddings):
                if pos=="NOUN" or pos==0: 
                    noun_matrix.append(embedding)
                    sentence_noun.append([embedding,pos,words])
                    # add to tensor list

                if pos== "VERB" or pos==1:
                    verb_matrix.append(embedding)
                    sentence_verb.append([embedding,pos,words])
                    
            if noun_matrix and verb_matrix : 
                noun_matrix=torch.tensor(noun_matrix).to('cuda')
                verb_matrix=torch.tensor(verb_matrix).to('cuda')

                doc_noun.append([sentence_noun,sentence[3],noun_matrix])
                doc_verb.append([sentence_verb,sentence[3],verb_matrix])
        doc=[doc_noun,doc_verb,doc_name]


        return doc
    

    def cosine_sim_matrix_dot(self,doc1,doc2,noun_or_verb=0):# 0 for noun 1 for verb
        import torch
        import copy
        doc1_name=doc1[2]
        doc2_name =doc2[2]
        dic_comparison={}
        for  sentence_1 in doc1[noun_or_verb]:
            words_of_first_sentencess=[]
            words_of_first_sentencess=[xxx[2] for xxx in sentence_1[0]]
            #for ii in sentence_1[0]:
                #print(ii[2])
                #words_of_first_sentencess.append(ii[2])
              
            
            #print(words_of_first_sentence)
            #print(words_of_first_sentence)
            
            
            for sentence_2 in doc2[noun_or_verb]:
                words_of_second_sentencess=[]
                #for i in sentence_2[0]:
                #    words_of_second_sentencess.append(i[2])
                words_of_second_sentencess=[xx[2] for xx in sentence_2[0]]
                #print(words_of_second_sentence)
                #print(words_of_second_sentence)
                #if len(sentence_2[0])==0:
                #    continue
                

                #sim_matrix2=torch.matmul(sentence_1[2],sentence_2[2].T).to('cuda')
                sim_matrix2=torch.matmul(sentence_2[2],sentence_1[2].T).to('cuda')

                sim_matrix2=sim_matrix2.detach().cpu()
                sim_matrix44=sim_matrix2.tolist()
                #print(f"matrix{sim_matrix44}")
                for  ii, column in enumerate(sim_matrix44):
                    if ii==0:
                        #print('meow')
                        used_rows=column
                        continue
                    
                    for old, new in zip(used_rows,column):
                        # need to replace one new from old? to get a better distribution
                        #take lowest of old used_rows and replace with corresponding value in new only if 
                        if new>old:
                            old_index=used_rows.index(old)
                            used_rows[old_index]=new
               
                #print(f"row{used_rows}")
                dic_comparison[f"{sentence_1[1]}:{sentence_2[1]}"]= [copy.deepcopy(used_rows), copy.copy(words_of_first_sentencess) , copy.copy(words_of_second_sentencess), doc1_name, doc2_name]
                   
        return dic_comparison  
                            
                            

    def combine_verb_and_noun_cosines(self, noun_cosines, verb_cosines):
        import re
        #document_sim_scores={}
        
        for key_noun, value_noun in noun_cosines.items():
            
            if verb_cosines.get(key_noun):
                
                for sim_score in verb_cosines[key_noun][0]:
                     value_noun[0].append(sim_score)
                     
                for first_word_sentence in verb_cosines[key_noun][1]:
                    value_noun[1].append(first_word_sentence)
                    
                for second_word_sentence in verb_cosines[key_noun][2]:
                     value_noun[2].append(second_word_sentence)
                     
                sentence_simialrity =sum(value_noun[0])/len(value_noun[0])
                
                noun_cosines[key_noun].append(sentence_simialrity)
                # create list_of_highest_matches 
                
                    
                    
                    #limit the matches to having only three and that should do it
                    
                
                
                
                
                
            
            #for key_verb, value_verb in verb_cosines.items():
                #print(value_noun[1])

                #if key_noun == key_verb:
                    #value_noun[0].extend(value_verb[0])
                    #value_noun[1].extend(value_verb[1])
                    #value_noun[2].extend(value_verb[2])                 
                   
                    
                    
                    
                    #document_sim_scores[key_noun]=sentence_simialrity
                    
      
        return noun_cosines
    def find_best_matching_doc_sentences(self,noun_cosines):
         import re

         seen_num_dic={}
         
         for key, value in noun_cosines.items():
             key=str(key)
             sentences_num=re.search(r"(\d+):(\d+)",key)
             first_sentence_num=sentences_num.group(1)
             second_sentence_num=sentences_num.group(2)

             #print(first_sentence_num)
             if seen_num_dic.get(first_sentence_num):
                 if len(seen_num_dic[first_sentence_num][0])<=2:
                     seen_num_dic[first_sentence_num][0].append(value[5])
                     seen_num_dic[first_sentence_num][1].append(second_sentence_num)
                     
                     seen_num_dic[first_sentence_num][2].append(value[0])
                     seen_num_dic[first_sentence_num][3].append(value[1])
                     seen_num_dic[first_sentence_num][4].append(value[2])
                     seen_num_dic[first_sentence_num][5].append(value[3])
                     seen_num_dic[first_sentence_num][6].append(value[4])

                     continue
                 if value[5]>min(seen_num_dic[first_sentence_num][0]):
                     min_index=seen_num_dic[first_sentence_num][0].index(min(seen_num_dic[first_sentence_num][0]))
                     seen_num_dic[first_sentence_num][0][min_index]=value[5]  
                     seen_num_dic[first_sentence_num][1][min_index]=second_sentence_num 
                     
                     seen_num_dic[first_sentence_num][2][min_index]=value[0]  
                     seen_num_dic[first_sentence_num][3][min_index]=value[1]  
                     seen_num_dic[first_sentence_num][4][min_index]=value[2]  
                     seen_num_dic[first_sentence_num][5][min_index]=value[3]  
                     seen_num_dic[first_sentence_num][6][min_index]=value[4]  



                     
                     
                 continue
             
             seen_num_dic[first_sentence_num]=[[value[5]],[second_sentence_num],[value[0]],[value[1]],[value[2]],[value[3]],[value[4]]]
             
             

             
                 
             #print(value[5])
             
         #for keyy, valuee in seen_num_dic.items():
             #seen_num_dic[keyy]=valuee.sort()
         return seen_num_dic
     
        
      
        
    def save_cosine_simialrities_in_firac_labels(self, document_dic_with_cos):
        # need to finish this still
        """ upload the simiarlities score of a given sentence to the database showing which sentences are matched between the two documents, and there FIRAC placement"""
        import re
        for cos_sentence_key, cos_sentence_value in document_dic_with_cos.items():
            for average_sim_score,sentence_number2,sim_scores,sentence_1_words,sentence_2_words,document_name_1,document_name_2  in zip(cos_sentence_value[0],cos_sentence_value[1],cos_sentence_value[2],cos_sentence_value[3],cos_sentence_value[4],cos_sentence_value[5],cos_sentence_value[6]):
                
                sentence_1_words=str(sentence_1_words).replace("\'","")
                sentence_1_words=str(sentence_1_words).replace("\"","")
                sentence_2_words=str(sentence_2_words).replace("\'","")
                sentence_2_words=str(sentence_2_words).replace("\"","")
                self.cur.execute( f""" INSERT INTO embedding_sim_scores (sim_scores,average_sim_score, sentence_1_words,sentence_2_words, sentence_number1,sentence_number2, document_name_1,document_name_2)
                            VALUES ('{str(sim_scores)}','{str(average_sim_score)}','{sentence_1_words}','{sentence_2_words}','{str(cos_sentence_key)}','{str(sentence_number2)}','{str(document_name_1)}', '{str(document_name_2)}');""")
            self.conn.commit()
            
                            #VALUES ('{str(cos_sentence_value[0])}','{str(cos_sentence_value[5])}','{str(cos_sentence_value[1])}','{str(cos_sentence_value[2])}','{str(sentence_1)}','{str(sentence_2)}','{str(cos_sentence_value[3])}', '{str(cos_sentence_value[4])}');""")

                
                

            #sentences_num=re.search(r"(\d+):(\d+)",cos_sentence_key)
            

            #sentence_1=sentences_num.group(1)
            #sentence_2=sentences_num.group(2)
 
            
        

            
       
        
        #save max simialrity scores?
        #basically if the simalarity score is high then we will say that this sentence belong to this category then.
        
  
        
class FIRAC_MODEL():
    # I WILL DO THE TRAINING IN A SEPERATE DOCUMENT
    def train_firac_model_verb():
        # to get here we need to cosign similarity
        """  use verb embeddings in a sentence feed in FFn to produce model too train this model""" # need to figure out how to frame model for this task, verbs will go into one model 
        

        
    def train_firac_model_noun():
        """  use noun embeddings in a sentence feed in FFn to produce model too train this model""" # need to figure out how to frame model for this task, verbs will go into one model and nouns will go into another, this way alikes are compared and model wil


                
                
    def train_law_finder_network(self):
        """find all the mentions of law in the document whether that be case names or names of statutes"""
        #gather data of law in documents, running law found in the column for canlii thru document text to find it
        #save labels to a database somewhere
        # go to cited cases column
      
        
        
        
    def cosine_simairlity_pos_embeddings(doc1, doc2):
        """ check cosine simailirty of all sentences in two  documents comparing nouns against other nouns and verbs against verbs output list of cosine simialrities of each and also sentence level averages"""
        from torch.nn import CosineSimilarity


        
    def doc_to_doc_network(input_judgement_sentence, label_factum_sentence):
        """ converting a judgement embeddings into a factum embeddings and if they retain a high cosine simialrity and are decided to be related based upon this cosine simialrity"""
        # we will be implementing that larger network here
    def fact_pattern_input_for_pipeline():
        """ the fact pattern that we generate form the case we are working on"""

    def find_case_fact_cluster():
        """ compare each fact sentence in a document to another fact sentence in a document on the basis of noun and verbs """

    def find_case_by_fact():
        """ pick a single case from the case cluster based upon the closeest simialirity """
        
    def find_issues():
        """ compare results of fact search choice among issue sentences"""

    def find_argument():
        """ compare results of issue search against the true argument to determine a list of best arguments that might be used in a decision"""
        

    def find_law_in_issue_or_argument():
        """ locate all mentions of law in the document by searching the cases and legislation that is used in the document"""
        
        
    def find_similar_law():
        """find this law to make the argument relevent in the jurisdiction you are working in"""



       
    
