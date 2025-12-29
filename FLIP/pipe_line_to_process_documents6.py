# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 04:18:07 2023

@author: doggo777
"""


class document_vectorizer():

    

    def __init__(self):
        import psycopg2
        import torch
        import numpy as np
        #from  Pos_model_trainer import network
        super().__init__()
        self.conn =  psycopg2.connect(dbname="Can_Law_Accessible", user="postgres", password="MeganisGreat")
        self.cur = self.conn.cursor()
        
        self.sentence_info = []
        self.pos_word_list= []
        self.document_name = ""
        self.document_verb= []
        self.document_noun=[]
        self.torch_catche= torch.cuda.empty_cache()
        self.document_id=""
        self.final_sentence_info_list=[]
        self.max_value=1.0
        self.npmax=np.argmax(self.max_value) # find pytorch arg max function
        self.unwanted_characters=[".","?","[","]","(",")"]
        self.database=""

        
        self.type_of_document=""
        self.document_law=[]
    def init_deberta_model(self):
        from transformers import  DebertaModel
        from transformers import DebertaTokenizerFast
        self.model= DebertaModel.from_pretrained(r"C:\Users\doggo777\Documents\model.pth6").to("cuda")
        self.tokenizer = DebertaTokenizerFast.from_pretrained(r"C:\Users\doggo777\Documents\model.pth6",truncation_side="left")
        
        
    def init_pos_model(self):
        import torch

        from unwanted_sentence_model_network import network

        self.pos_model=network(768, 1000, 3).to("cuda")
        pos_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_pos.pth")
        self.pos_model.load_state_dict(pos_state_dic)
    def init_non_sentence_model(self):
        import torch

        from unwanted_sentence_model_network import network
        
        self.unwanted_model=network(768, 1000, 2).to("cuda")
        un_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\un_wanted_model.pth")
        self.unwanted_model.load_state_dict(un_state_dic)
    
    def init_law_model(self):
        import torch


        from unwanted_sentence_model_network import network
        
        self.law_model=network(768, 1000, 2).to("cuda")
        law_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\legislation_model.pth")
        self.law_model.load_state_dict(law_state_dic)
    
    def init_proper_noun_model(self):
        import torch
        from unwanted_sentence_model_network import network
        
        self.proper_noun_model=network(768, 1000, 2).to("cuda")
        proper_noun_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\proper_noun_model.pth")
        self.proper_noun_model.load_state_dict(proper_noun_state_dic)
    def init_FIRAC_model_sentence(self):
        import torch

        from unwanted_sentence_model_network import network
        
        self.FIRAC_model_sentence=network(11520, 400, 3).to("cuda")
        FIRAC_sentence_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_firac_flat.pth")
        self.FIRAC_model_sentence.load_state_dict(FIRAC_sentence_state_dic)
        
    def init_FIRAC_model_word(self):
        import torch

        from unwanted_sentence_model_network import network
        
        self.FIRAC_model_word=network(768, 1000, 3).to("cuda")
        FIRAC_word_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_firac2.pth")
        # firac model 2 is the best firac model
        self.FIRAC_model_word.load_state_dict(FIRAC_word_state_dic)
        
    def init_Holding_model_word(self):
        import torch
        # need to still work on this eon

        from unwanted_sentence_model_network import network
        
        self.FIRAC_model_word=network(768, 1000, 3).to("cuda")
        FIRAC_word_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_firac2.pth")
        # firac model 2 is the best firac model
        self.FIRAC_model_word.load_state_dict(FIRAC_word_state_dic)


        
    
    
        
        
        
            



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
        self.database="full_cases"

        
        # will need to remove duplicates of sentences at one point


        return document_text # make sure to instantiate a new class when using this
    
    
    def upload_summary_for_matching(self,case_name):
        self.cur.execute( f""" SELECT ID, case_name, facts,issues,conclusions,holdings
                          FROM case_summaries 
                          WHERE case_name ILIKE '{case_name}'
                          ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
        cur_result5= self.cur.fetchall()
        if cur_result5:
            self.document_name=cur_result5[0][1]
            self.document_id=cur_result5[0][0]
            self.database="case_summaries"

            divided_text={"facts":cur_result5[0][2],"issues":cur_result5[0][3],"conclusions":cur_result5[0][4],"holdings":cur_result5[0][5]}
        
        return divided_text
    

    def upload_factum_for_matching(self,factum_name,factum_iter):
        
        if factum_iter==0:
            self.cur.execute( f""" SELECT ID, argument_text,case_number,appellent_v_respondent
                              FROM factums 
                              WHERE case_number ILIKE '{factum_name}'
                              limit 1
                              ;""")
            #print('meoww')
            cur_result5= self.cur.fetchall()
            if cur_result5:
                #if len(cur_result5>1:
                       #for factum in cur_result5:
           
                 text=cur_result5[0][1]
                 self.document_id=cur_result5[0][0]
                 self.document_name=cur_result5[0][2]
                 self.database="factums"
                 res_v_appel=cur_result5[0][3]
                 return text,res_v_appel
        if factum_iter!=0:
            self.cur.execute( f""" SELECT ID, argument_text,case_number,appellent_v_respondent
                              FROM factums 
                              WHERE case_number ILIKE '{factum_name}'
                              limit 1 OFFSET {factum_iter}
                              ;""")
            cur_result5= self.cur.fetchall()
            #print('woo')
            if cur_result5:
                #if len(cur_result5>1:
                       #for factum in cur_result5:
           
                 text=cur_result5[0][1]
                 self.document_id=cur_result5[0][0]
                 self.document_name=cur_result5[0][2]
                 self.database="factums"
                 res_v_appel=cur_result5[0][3]
                 return text,res_v_appel
            
        

            
        return "no_text","sorry"
        
        
    def upload_case_for_matching(self, case_name):
        """ Locate the coresponding factum/summary and case since this deals with one document at a time will need to use this once for factum/summary and the other time for full_case """
      
        self.cur.execute( f""" SELECT ID, case_name, full_case_text,cited_cases
                          FROM full_cases 
                          WHERE case_name ILIKE '{case_name}'
                          ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
        cur_result2= self.cur.fetchall()

        if cur_result2: # not first document
            self.document_name=cur_result2[0][1]
            self.document_id= cur_result2[0][0]
            document_text=cur_result2[0][2]
            self.document_law=cur_result2[0][3]
            self.database="full_cases"


        #document_embeddings_3=cur_result3[0][2]
        return document_text

    def decide_which_document_to_upload(self):
        """ Look thru which document we have in the embedding database and start on the list so we don't repeat"""
        #self.cur.execute(f""" SELECT ID, document_name,sentence_number
        #                  FROM embedding_sentences
        #                  ORDER BY ID DESC 
        #                  LIMIT 1 ;""")
                         
        #cur_result= self.cur.fetchall()
        self.document_name=None

        #if cur_result: # not first document
        #    self.document_name=cur_result[0][1]
        #    self.document_id= cur_result[0][0]
        #    self.database="full_cases"

            


            
        #return self.document_name
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
            self.database="full_cases"

            
           
            


            

   
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
        f= re.sub(r"\\x\S+",r" ",f )
        f= re.sub(r"@", "",f )

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
        import re
        index_used_list=[]
        self.sentences=[]
        find_word_pattern = re.compile(r"\w+")

      

        #from nltk.tokenize import word_tokenize
        modifying_sentences = sent_tokenize(document)
        for i7, sentence_15 in enumerate(modifying_sentences):
            if len(modifying_sentences)==1:
                self.sentences.append(sentence_15)
                #print("WOWWW")
                break

            words_in_current_sentence=find_word_pattern.findall(sentence_15)
            
            if len(words_in_current_sentence)<4:
                
                if i7==0:
                    
                   sentence_15=sentence_15 + " " +  modifying_sentences[i7+1]
                   words_in_current_sentence2=find_word_pattern.findall(sentence_15)
                   if len(words_in_current_sentence2)>=4:
                       index_used_list.append(i7+1)
                       
                   if len(words_in_current_sentence2)<4 and len(modifying_sentences)>2:
                       sentence_15= sentence_15 + " " +  modifying_sentences[i7+2]
                       index_used_list.append(i7+1)
                       index_used_list.append(i7+2)
                   else:
                       index_used_list.append(i7+1)

                       

                if i7!=0:
                    #print(i7)
                    #print(i7-1)
                    
                    self.sentences[-1]=self.sentences[-1]+ " "+sentence_15 
                    continue

                    
                    
                    
            if i7 in index_used_list:
                continue 
            #print(sentence_15)
            self.sentences.append(sentence_15)
                  
        return self.sentences
    
    
                    
 
        
    
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
        self.contexualzed_sentennce_list = []
        self.sentence_inside_context_sentence_block=[]


        import re
        import copy
        find_word_pattern = re.compile(r"\w+")
        temp_sentences_used_dic={}
        

        for i, sentence_2 in enumerate(sentences):
            if len(sentences)==1:
                #print('LETS DO IT')
                existing_sentences= " @" 
                temp_sentences_used_dic["zero"]=[i]
                data_generation_sentence=sentence_2
                self.contexualzed_sentennce_list.append([existing_sentences,sentence_2,data_generation_sentence])
                self.sentence_inside_context_sentence_block.append(copy.deepcopy(temp_sentences_used_dic))
                #print(data_generation_sentence)
                break
                
                
            

            if i ==0:
                existing_sentences= sentence_2 +" " + "@"
                temp_sentences_used_dic["single"]=[i]
                continue
                

            words_remove_from_sentence = find_word_pattern.findall(existing_sentences)
            finding_words_to_remove_len =len(words_remove_from_sentence)
            
            #print(finding_words_to_remove_len)
            if temp_sentences_used_dic.get("single"):
                #print('woo')
                temp_sentences_used_dic["single"].append(i)

                
            #if temp_sentences_used_dic.get("double"):
                 #print('meow')
            #     temp_sentences_used_dic["double"].append(i)
                 
                 
            if finding_words_to_remove_len > 300:
                data_generation_sentence=existing_sentences[existing_sentences.index("@")+2:]+ " " +sentence_2
                self.contexualzed_sentennce_list.append([existing_sentences,sentence_2,data_generation_sentence])
                self.sentence_inside_context_sentence_block.append(copy.deepcopy(temp_sentences_used_dic))                
                #words_in_current_sentence=find_word_pattern.findall(sentence_2)
                temp_sentences_used_dic["single"]=[i]
                existing_sentences=sentence_2 + " "+ "@"
                continue
            
            if len(self.contexualzed_sentennce_list)==0 and sentence_2==sentences[-1] :
                temp_sentences_used_dic["zero"]=temp_sentences_used_dic["single"]
                del temp_sentences_used_dic["single"]
                # LOSING A SENTENCE NEEDED HERE WILL NEED TO FIX THIS LATER
                existing_sentences=re.sub(r" @","",existing_sentences)
                existing_sentences=" @"+ existing_sentences
                data_generation_sentence=existing_sentences[existing_sentences.index("@")+1:]+ " " +sentence_2
                #print(data_generation_sentence)
                self.contexualzed_sentennce_list.append([copy.deepcopy(existing_sentences),copy.deepcopy(sentence_2),copy.deepcopy(data_generation_sentence)])
                self.sentence_inside_context_sentence_block.append(copy.deepcopy(temp_sentences_used_dic))                
                #words_in_current_sentence=find_word_pattern.findall(sentence_2)
                temp_sentences_used_dic["single"]=[i]
                existing_sentences=sentence_2 + " "+ "@"
                #print('MEOW')
                continue
                
                
                
                #if len(words_in_current_sentence) <5:
                #    existing_sentences=sentences[i-1]+ " " + f"{sentence_2}" + " "+ "@"
                #    temp_sentences_used_dic["double"]=[i-1,i]
                #    continue
            #print(existing_sentences)
                  
 
            existing_sentences= existing_sentences + " " + f"{sentence_2}"
            
            # mark all the  sentence boundaries in existing sentences
            
            

        return self.contexualzed_sentennce_list,self.sentence_inside_context_sentence_block
    
            
        
      
    def tokenize_document(self, sentence_3,sentences_used):# this is a single sentence using the contexualized sentnece list
        import re
        self.at_working=0

        #finding_start_of_second_sentence=re.compile(r"1")
        inputs = self.tokenizer(sentence_3[0], sentence_3[1], return_tensors="pt", truncation=True, return_token_type_ids=True).to("cuda")
        ids_of_tokens=inputs['input_ids'].tolist()
        token_sentence_ids=inputs['token_type_ids'].tolist()
        [token_sentence_ids] = token_sentence_ids
        [ids_of_tokens] = ids_of_tokens
        token_values_of_ids=self.tokenizer.convert_ids_to_tokens(ids_of_tokens)
        self.sentence_info=[token_values_of_ids,ids_of_tokens,token_sentence_ids]
        # find the token at end
        
        #if sentences_used.get("single"):
        #    sentence_to_remove=self.sentences[sentences_used["single"][0]]

        #if sentences_used.get("double"):
        #    sentence_to_remove=self.sentences[sentences_used["double"][1]]
            
        #sentence_to_remove=sentence_to_remove.split(" ")
        #last_word=sentence_to_remove[-1].lower()
        #find tokens in order
        count_of_first_sentence_length=self.sentence_info[2].count(0)
        self.sentence_info.append(count_of_first_sentence_length)
        
        if "Ġ@" in token_values_of_ids:
            #print("found our thing")
            self.cut_of_token=token_values_of_ids.index("Ġ@")+1
            self.at_working=1
            self.sentence_info[0]=self.sentence_info[0][self.cut_of_token:-1]
            self.sentence_info[1]=self.sentence_info[1][self.cut_of_token:-1]
            self.sentence_info[2]=self.sentence_info[2][self.cut_of_token:-1]
            
            self.index_of_sep=self.sentence_info[0].index("[SEP]")
            
            del self.sentence_info[0][self.index_of_sep]
            del self.sentence_info[1][self.index_of_sep]
            del self.sentence_info[2][self.index_of_sep]
            
                
     
            del inputs["token_type_ids"]
            
            
           
            return inputs
            

        if self.at_working==0:
            #print("not_found")
            self.sentence_info[0]=self.sentence_info[0][1:-1]
            self.sentence_info[1]=self.sentence_info[1][1:-1]
            self.sentence_info[2]=self.sentence_info[2][1:-1]
            #print(self.sentence_info[0])
            #print(self.document_name)
            #print(self.document_id)
            #print(self.database)

            
            self.index_of_sep=self.sentence_info[0].index("[SEP]")
            
            del self.sentence_info[0][self.index_of_sep]
            del self.sentence_info[1][self.index_of_sep]
            del self.sentence_info[2][self.index_of_sep]
            #print('hi')
            return inputs
         
            
        
        
            
                
                
            
            
        
            
            
            
    

       
    

        
        
    
        
    def generate_embeddings(self, inputs):
        import torch
        import copy
        #from transformers import  DebertaModel
        #model = DebertaModel.from_pretrained("microsoft/deberta-base").to("cuda")
        """ converting text to embeddings using a pre-trained deberta model"""
        new_output = self.model(**inputs)
        new_output=new_output["last_hidden_state"]
        new_output=new_output[0]
        #print(new_output)
        #output=copy.deepcopy(new_output[0])
        #print(new_output[self.cut_of_token-1])
        #print(new_output[self.cut_of_token])

        #print(new_output[-1])
        if self.at_working==1:
            
            new_output= new_output[self.cut_of_token:-1]
            
            before_sep=new_output[:self.index_of_sep]
            # IF THE EMBEDDINGS DON"T START TO LOOK RIGHT WILL NEED TO CHECK THIS
            
            after_sep=new_output[self.index_of_sep+1:]
            new_output=torch.cat((before_sep, after_sep), 0)

            self.torch_catche
            

            
            # NEED TO REMEMBER TO DELETE SEP IN PROCESSING 
            #print(new_output)
            new_output_list=new_output.tolist()  
            
            #del new_output_list[self.index_of_sep]

            self.sentence_info.append(new_output_list)
            self.sentence_info[4]=new_output_list

            
            embedding_information_list=self.sentence_info
            #print(len(embedding_information_list))
            #print(len(embedding_information_list[0]))
            #print(len(embedding_information_list[1]))
            #print(len(embedding_information_list[2]))
            #print(len(embedding_information_list[3]))
            #print(len(embedding_information_list[4]))
            #print(len(new_output))

            
            return embedding_information_list,new_output
            
            
            
            
            
        if self.at_working==0:
            #print("DOUBLE POWR")
            new_output=new_output[1:-1]
            before_sep=new_output[:self.index_of_sep]
            # IF THE EMBEDDINGS DON"T START TO LOOK RIGHT WILL NEED TO CHECK THIS
        

            
            after_sep=new_output[self.index_of_sep+1:]
            new_output=torch.cat((before_sep, after_sep), 0)
            self.torch_catche
            

            
            # NEED TO REMEMBER TO DELETE SEP IN PROCESSING 
            #print(new_output)
            new_output_list=new_output.tolist()  
            
            #del new_output_list[self.index_of_sep]

            self.sentence_info.append(new_output_list)
            self.sentence_info[4]=new_output_list
      
            embedding_information_list=self.sentence_info
            #print(len(embedding_information_list[0]))
            #print(len(embedding_information_list[1]))
            #print(len(embedding_information_list[2]))
            #print(len(embedding_information_list[3]))
            #print(len(embedding_information_list[4]))
            #print(len(new_output))
            return embedding_information_list,new_output
            

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
        # doubler check on this law matcher later but should be good
        import re
        law_word_list=[]
        #print(found_law_in_document)
        #need to create range_list
        #print(found_law_in_document)
        for part_of_speech_parts in pos_unmodified_sentence:
            #print(f" this is the pos  {part_of_speech_parts.text}")
            label=""
            marked_as_yes=False
            #print(part_of_speech_parts.text)
            #print(found_law_in_document)
            # need to iteraste thru the list to get it to work
            #print(part_of_speech_parts.text)
            
            
            for worddd in found_law_in_document:
                if part_of_speech_parts.text in self.unwanted_characters:
                    break
                part_of_speech=re.sub(r"[\(\)\[\]\.\?]", "", part_of_speech_parts.text) 
                found_law_match=re.search(f"{part_of_speech}",worddd)
                if found_law_match:
                    label="YES"
                    law_word_list.append([part_of_speech_parts.text,label])
                    marked_as_yes=True
                    break
            if marked_as_yes==True:
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
                                if label=="scrap":
                                    #print(f"this word we are scraping")
                                    continue
                                
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
    def divide_output_into_sentences(self,sentence_inside_context_sentence_block,output):
        import re
        import copy
        self.list_of_document_infos=[]
        existing_tokens=''
        """ this function will find each of the places that the sentences are in the self.sentence_info list"""
        # find the last tokens in the sequence
        # find when the chain or seqence of matches ends
        # what if error with len of sentence? NEED TO ADDRESS THIS
        
        starting_document_info=self.sentence_info[0]
        starting_document_info_num_id=self.sentence_info[1]
        starting_document_info_sentence_id=self.sentence_info[2]
        wrong_num_to_keep_seperation=self.sentence_info[3]
        starting_document_info_embedding=self.sentence_info[4]
        if sentence_inside_context_sentence_block.get("zero"):
            sentences_inside_context =sentence_inside_context_sentence_block["zero"]
            typee=0
            #print('not today')
            


        if sentence_inside_context_sentence_block.get("single"):
            
           sentences_inside_context =sentence_inside_context_sentence_block["single"]
           typee=1
            
        #if sentence_inside_context_sentence_block.get("double"):
        #    sentences_inside_context=sentence_inside_context_sentence_block["double"]
        #    typee=2
        #print(sentences_inside_context)
        #print(sentences_inside_context[typee:])

        for iiii, sentence_index in enumerate(sentences_inside_context[typee:]): 
            #print(sentence_index)
            existing_portion=""
            #print(sentence_index)
            #print(self.sentences)
 
            sentenceee=self.sentences[sentence_index].lower()            
            sentenceee=sentenceee.split(" ")
            #print(sentenceee)
            token_count=[]
            
            
            if len(sentenceee)>2:
                last_words=sentenceee[-2:]
                last_words=last_words[0]+last_words[1]
                mostly_last_words=re.sub("[^a-z\.\,\?\!;:\d\[\]\(\)\-&#@$% ]","",last_words)
                #print(f"this is the string to MATCH {mostly_last_words}")
                #print(last_words)
                #print(starting_document_info)
                for iii, token in enumerate(starting_document_info):
                    if "Ġ" in token:
                        token=token.replace("Ġ","")
                    token=token.lower()  
                    #print(f"this is a token {token}")
                    usable_token=""
                    usable_token=re.search(r"[a-z\.\,\?\!;:\d\[\]\(\)\-&#@$%]",token)
                    if usable_token:
                        if token in mostly_last_words:
                            start_of_found_part_of_word=mostly_last_words.index(token)
                            
                            found_portion= mostly_last_words[start_of_found_part_of_word:start_of_found_part_of_word+len(token)]
                            
                            #print(f"this is a found {found_portion}")
                            #print(f"existing {existing_portion}")
                            if existing_portion!="":
                                existing_portion=existing_portion + found_portion
                                
                            if existing_portion=="":
                                existing_portion=found_portion


                            if existing_portion==mostly_last_words:
                                #print('WOO')
                                 
                                self.list_of_document_infos.append([starting_document_info[:iii+1],starting_document_info_num_id[:iii+1],starting_document_info_sentence_id[:iii+1],starting_document_info_embedding[:iii+1],output[:iii+1]])
                                                                    
                                #print(starting_document_info[:iii+1])
                                starting_document_info=starting_document_info[iii+1:]
                                starting_document_info_num_id=starting_document_info_num_id[iii+1:]
                                starting_document_info_sentence_id=starting_document_info_sentence_id[iii+1:]
                                starting_document_info_embedding=starting_document_info_embedding[iii+1:]
                                output= output[iii+1:]
                                #print(len(starting_document_info[:iii+1]))
                                #print(len(starting_document_info_num_id[:iii+1]))
                                #print(len(starting_document_info_sentence_id[:iii+1]))
                                #print(len(starting_document_info_embedding[:iii+1]))
                                #print(len(output[:iii+1]))

                                
                                

                                
                                break
                            continue
                        existing_portion=""
                        continue
                    
            #if len(sentenceee)<=2:
            #    self.list_of_document_infos[-1].append()
                
                
                
                #to the various lists
                #add the values on to the end of the previous sentence
                #last_word=sentence_to_remove[-1].lower()
        return self.list_of_document_infos
                    
                        
         
   
        
  
        
    def run_values_thru_unwanted_sentences(self,list_of_document_infos): # we are going to use this  # need to change this to work with updated method
    # will need to test the right amount to eliminate more sentences
    
         """ feed in all sentences in their embedding format and output only sentences that are cleaned and want to work with"""
         
         #counterrr=0
         returnn="false"
         #print(f" this should be the number of wordss int he sentence {len(output)}")

         #for inputt in list_of_document_infos[4]:
         #    wooo=self.unwanted_model.forward(inputt)
         #    print(wooo)
         #    wooo=wooo.tolist()
         #    s=wooo.index(max(wooo))
         #    print(s)
             
         un_pred=self.unwanted_model.forward(list_of_document_infos[4])
         # 0 represents not wanted, 1 represents wanted
         un_pred=un_pred.tolist()
         un_pred=[pred.index(max(pred))for pred in un_pred]
         count_of_zeros=un_pred.count(0)


             
         if count_of_zeros==len(list_of_document_infos[0]):
             returnn="true"
             #print(un_pred)
             #print(list_of_document_infos[0])

         if len(list_of_document_infos[0])>5:
             if count_of_zeros > len(list_of_document_infos[0])*0.63:
                 #print(un_pred)
                 #print(list_of_document_infos[0])

                 returnn="true"
             #print(counterrr)          
        
         return returnn
     
        
                 
                 #skip sentence
                     
               
    
        
        

    def run_values_thru_law_model(self,list_of_document_infos):
        """run all the token thru network to identify where law is in various sentences to be used for later"""
        self.law_list=[]
        
        law_predictions=self.law_model.forward(list_of_document_infos[4])
        law_predictions=law_predictions.tolist()
        #prediction=max(pos_predictions)
        law_predictions=[pred.index(max(pred))for pred in law_predictions]
        #print(law_predictions)
        for i, prediction in enumerate(law_predictions):
            if prediction == 0:
                self.law_list.append(list_of_document_infos[0][i])
            

        #prediction=pos_predictions.index(max(pos_predictions))
        
        #print(prediction)
         # words
            #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech

        #if prediction==0:
        return self.law_list
    def pretend_to_be_pos(self,list_of_document_infos):
        self.final_sentence_info_list=[]

        
        self.final_sentence_info_list.append(list_of_document_infos[0]) # words
        #self.final_sentence_info_list[0]=final_word_list
        
        self.final_sentence_info_list.append(list_of_document_infos[3]) #embeddings
        #self.final_sentence_info_list[1]=final_embedding_list
        none_list=[None] *len(list_of_document_infos[3])

        self.final_sentence_info_list.append([none_list])
        self.final_sentence_info_list[0]=str(self.final_sentence_info_list[0]).replace("\'","")
        self.final_sentence_info_list[0]=str(self.final_sentence_info_list[0]).replace("\"","")  
        
    
    
    
   

    def run_values_thru_word_firac_model(self,list_of_document_infos):
        """ this is for if we want to use words rather than the entire sentence"""
        #returnn="false"
        #FIRAC_pred_list=[]
        #print(f" this should be the number of wordss int he sentence {len(output)}")

        #for inputt in list_of_document_infos[4]:
        #    wooo=self.unwanted_model.forward(inputt)
        #    print(wooo)
        #    wooo=wooo.tolist()
        #    s=wooo.index(max(wooo))
        #    print(s)
            
        FIRAC_pred=self.FIRAC_model_word.forward(list_of_document_infos[4])
        # 0 represents not wanted, 1 represents wanted
        FIRAC_pred=FIRAC_pred.tolist()
        FIRAC_pred=[pred.index(max(pred))for pred in FIRAC_pred]
        fact_word_count=FIRAC_pred.count(0)
        issue_word_count=FIRAC_pred.count(1)
        holding_word_count=FIRAC_pred.count(2)
        if issue_word_count>len(FIRAC_pred)/100*20:
            prediction2="issue"
            #FIRAC_pred_list.append(prediction2)  
        else:
            
            word_counts=[fact_word_count,issue_word_count,holding_word_count]
            #print(word_counts)

            prediction= word_counts.index(max(word_counts))
            if prediction==0:
                prediction2="fact"
                #FIRAC_pred_list.append(prediction2)
            if prediction==1:
                prediction2="issue"
                #FIRAC_pred_list.append(prediction2)

            if prediction==2:
                prediction2="holding"
                #FIRAC_pred_list.append(prediction2)
            
        list_of_document_infos.append(prediction2)


            
            #print(counterrr)          
       
        return list_of_document_infos
    
    def run_values_thru_pos_model(self,list_of_document_infos): 
        """run a sentence embedding output of a transformer thru and remove all none Noun and verb embeddings from the sentence"""
        final_word_list=[]
        import torch
        final_embedding_list=[]
        final_pos_list=[]
        usable_embedding_list=""
        #usable_embedding_list=[]
        self.final_sentence_info_list=[]
        pos_predictions=self.pos_model.forward(list_of_document_infos[4])
        pos_predictions=pos_predictions.tolist()
        pos_predictions=[pred.index(max(pred))for pred in pos_predictions]
        counterr=0
        #print(list_of_document_infos[0])
        #print(pos_predictions)
        for iiiii, predd in enumerate(pos_predictions):
 
            if predd == 1 or predd == 0:
                #print('hi')
                counterr+=1
                #final_sentence_info_list
                final_word_list.append(list_of_document_infos[0][iiiii]) # words
                #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech
                final_embedding_list.append(list_of_document_infos[3][iiiii]) #embeddings
                final_pos_list.append(predd)# pos                              
                #list_of_document_infos[4]=torch.cat((before_sep, after_sep), 0)
                #if counterr==1:
                #    usable_embedding_list=list_of_document_infos[4][iiiii]
                    #print(usable_embedding_list.shape)
                #    continue
                #if counterr==2:
                #    usable_embedding_list=torch.stack((usable_embedding_list,list_of_document_infos[4][iiiii]),0)
                    #print(usable_embedding_list.shape)
                #    continue

                #new_embedding= list_of_document_infos[4][iiiii][None,:]
                
                #print(list_of_document_infos[4][iiiii].shape)
                
                #usable_embedding_list=torch.cat((usable_embedding_list,new_embedding),dim=0)# usable embeddings
                #continue
            #else:
                
                #print(iiiii)
                #(len(list_of_document_infos[4]))

                #before_sep=list_of_document_infos[4][:iiiii]
                #print(len(before_sep))
                # IF THE EMBEDDINGS DON"T START TO LOOK RIGHT WILL NEED TO CHECK THIS

                #after_sep=list_of_document_infos[4][iiiii+1:]
                #print(len(after_sep))

                #list_of_document_infos[4]=torch.cat((before_sep, after_sep), dim=0)
                
                #print(len(list_of_document_infos[4]))
                #continue

                
                #del list_of_document_infos[4][iiiii]
                
                
              
        self.final_sentence_info_list.append(final_word_list) # words
        self.final_sentence_info_list[0]=str(self.final_sentence_info_list[0]).replace("\'","")
        self.final_sentence_info_list[0]=str(self.final_sentence_info_list[0]).replace("\"","")  
        #self.final_sentence_info_list[0]=final_word_list
        
        self.final_sentence_info_list.append(final_embedding_list) #embeddings
        #self.final_sentence_info_list[1]=final_embedding_list

        self.final_sentence_info_list.append(final_pos_list)
        # THIS SHOULD THE FIRAC VALUE
        self.final_sentence_info_list.append(list_of_document_infos[5])

        #a_tensor = torch.Tensor(a_list).cuda()

        #self.final_sentence_info_list.append(usable_embedding_list)

        #self.final_sentence_info_list[2]=final_pos_list
        #print(self.final_sentence_info_list)
        #print(len(self.final_sentence_info_list[0]))
        #print(len(self.final_sentence_info_list[1]))
        #print(len(self.final_sentence_info_list[2]))
        #print(len(self.final_sentence_info_list[3]))
        
 
        
    



    def up_load_law_to_temp_sentence_database(self,sentence_number,resvapp=None):
        if self.law_list:
            self.law_list=str(self.law_list).replace("\'","")
            self.law_list=self.law_list.replace("\"","")     
            if resvapp == None:
                self.cur.execute( f""" INSERT INTO temp_law_per_sentence_found (id,words_law,document_name,sentence_number,databasee)
                            VALUES ('{self.document_id}','{str(self.law_list)}','{str(self.document_name)}','{sentence_number}','{self.database}');""")
          
                
            if resvapp!=None:
                self.cur.execute( f""" INSERT INTO temp_law_per_sentence_found (id,words_law,document_name,sentence_number,databasee,resvapp)
                            VALUES ('{self.document_id}','{str(self.law_list)}','{str(self.document_name)}','{sentence_number}','{self.database}','{resvapp}');""")
            self.conn.commit()
    
          
            
            
            


    def upload_sentence_to_sentence_embedding_database_FIRAC_model(self, sentence_number):
        """ uploading to database with FIRAC labels generated from FIRAC model"""
        
        
        self.cur.execute( f""" INSERT INTO embedding_sentences_firac2 (id,words,embeddings,pos,firac,document_name,sentence_number,type_of_document)
                    VALUES ('{self.document_id}','{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.final_sentence_info_list[3])}','{str(self.document_name)}','{sentence_number}','{self.database}');""")
        self.conn.commit()

    
        


    def upload_sentence_to_sentence_embedding_database(self, sentence_number,FIRAC=None,resvapp=None):
            """EVENTUALLY WILL ADD A COLUMN FOR FIRAC, BUT THIS IS UPLOADING THE EMBEDDINGS WITH THERE POS """
        #if len(self.final_sentence_info_list[1])>1:
            if FIRAC==None:
                #print('hi')
                self.cur.execute( f""" INSERT INTO embedding_sentences (id,words,embeddings,pos,document_name,sentence_number,type_of_document)
                            VALUES ('{self.document_id}','{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.document_name)}','{sentence_number}','{self.database}');""")
            if FIRAC!=None:
                #print('hello')
                if resvapp==None:
                    self.cur.execute( f""" INSERT INTO embedding_sentences (id,words,embeddings,pos,document_name,sentence_number,FIRAC,type_of_document)
                                VALUES ('{self.document_id}','{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.document_name)}','{sentence_number}','{FIRAC}','{self.database}');""")
                if  resvapp!=None:
                        #print('woo')
                        self.cur.execute( f""" INSERT INTO embedding_sentences (id,words,embeddings,pos,document_name,sentence_number,FIRAC,type_of_document,appvres)
                                    VALUES ('{self.document_id}','{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.document_name)}','{sentence_number}','{FIRAC}','{self.database}','{resvapp}');""")
                
            self.conn.commit()
            
        
    
        

        #WILL NEED TO CHECK THIS AGAIN TORROOW
        #clean the document here as well
        # 


class document_FIRAC_labeler():
    def __init__(self):
        """ this class will upload embeddings, create sentences matrixes,  cosign simalrity these matrixes, save the results, and label sentences based on these results as fact issue, argument and so on"""
        import psycopg2
        #import torch
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
        for results in self.cur.fetchall():
            print('hi')
            
    def upload_embeddings_from_case_database_FIRAC_PIPELINE_FAST(self,FIRAC="fact"):
        """ upload_all_embeddings_and_sort_after"""
        self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name
                          FROM embedding_sentences_firac 
                          WHERE firac = '{FIRAC}'
                          ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
        doc_list= self.cur.fetchall()
        
            
        document_type="full_cases"
        
        
        return doc_list , document_type
        
    
    
    def upload_embeddings_from_case_database_FIRAC_PIPELINE(self,idd):
        """this is to be used when uploading full cases that  have been processed by the FIRAC MODEL"""
        self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name
                          FROM embedding_sentences 
                          WHERE id = '{idd}' 
                          ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
        cur_result2= self.cur.fetchall()
        print('meow')
        document_type="full_cases"
        return cur_result2 , document_type
    # for doing issue stuff we'll need id of the cases in the fact cluster and then compare them against eachother for sim scores
        

        
    
        
        
        
        
    
        
    def upload_embeddings_from_case_database(self, type_of_document_database,  case_name, appvres=""):
        """upload information of a case, factum, or summary from the sql database"""
        
            
        if type_of_document_database=="factums":
            if appvres=="appellant":
                
                self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name,firac,appvres
                                  FROM embedding_sentences 
                                  WHERE document_name ILIKE '%{case_name}%'  and appvres = 'appellant' ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
                cur_result2= self.cur.fetchall()
                

                
            if appvres=="respondent":
                self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name,firac,appvres
                                  FROM embedding_sentences 
                                  WHERE document_name ILIKE '%{case_name}%' and appvres = 'respondent'
                                  ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
                cur_result2= self.cur.fetchall()
                
            #else:
               #print('you need to enter whether you would like a appellent or respondent factum, as input to the kwarg appvres')

                
            
            
         
            
      
        
        if type_of_document_database=="case_summaries":
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name,firac
                              FROM embedding_sentences 
                              WHERE document_name ILIKE '%{case_name}%' and type_of_document = '{type_of_document_database}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result2= self.cur.fetchall()
            

            
        
        if type_of_document_database=="full_cases":
            
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name
                              FROM embedding_sentences
                              WHERE document_name ILIKE '%{case_name}%' and type_of_document = '{type_of_document_database}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result2= self.cur.fetchall()
            
        document_type=type_of_document_database
            
        
        return cur_result2 , document_type
    def spliting_upload_into_single_cases_before_pos_FIRAC_FAST(self,doc_list):
        """ preprocessing_upload for transform_to_pos"""
        dic_of_cases={}
        docs_to_delete=[]
        for sentence in doc_list:
            doc_name=sentence[4]
            if dic_of_cases.get(doc_name):
                    dic_of_cases[doc_name].append([sentence[0], sentence[1], sentence[2],sentence[3],sentence[4]])
                    continue
  
            dic_of_cases[doc_name]=[[sentence[0], sentence[1], sentence[2],sentence[3],sentence[4]]]

                
        for doc_name, sentences_list in dic_of_cases.items():
            if len(sentences_list)<5:
                docs_to_delete.append(doc_name)
        for deltes in docs_to_delete:
            del dic_of_cases[deltes]
        return dic_of_cases,docs_to_delete
            
        
        

            
        # remove all
        


    
    def transform_to_pos_format(self,doc,document_type):
        try:
            import json
            import time
            # will import the list of all three varabiles embedding, pos, word
            import torch
            doc_noun=[]
            doc_verb=[]
            doc_name=doc[0][4]

            for  sentence in doc:
                
                sentence_noun=[]
                sentence_verb=[]
                verb_matrix= []
                noun_matrix= []
                t1=time.time()


                embeddings=json.loads(sentence[0])
                t2=time.time()
                #print('json time')

                #print(t2-t1)

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
                    t1=time.time()

                    noun_matrix=torch.tensor(noun_matrix).to('cuda')
                    verb_matrix=torch.tensor(verb_matrix).to('cuda')
                    t2=time.time()

                    #print(t2-t1)

                    
                    
                    if document_type=="case_summaries":
                        firac= sentence[5]
                        doc_noun.append([sentence_noun,sentence[3],noun_matrix,firac])
                        doc_verb.append([sentence_verb,sentence[3],verb_matrix,firac]) 
                        continue
                        
                    if document_type=="factums":
                        firac= sentence[5]
                        resvapp=sentence[6]
                        doc_noun.append([sentence_noun,sentence[3],noun_matrix,firac,resvapp])
                        doc_verb.append([sentence_verb,sentence[3],verb_matrix,firac,resvapp])
                        continue

                    doc_noun.append([sentence_noun,sentence[3],noun_matrix])
                    doc_verb.append([sentence_verb,sentence[3],verb_matrix])
            
            t1=time.time()
        
      

            doc=[doc_noun,doc_verb,doc_name,document_type]
            t2=time.time()
            #print(t2-t1)
            #print('doc_time')

            

        except Exception as E:
            print(E)
            


        return doc
    

    def cosine_sim_matrix_dot(self,doc1,doc2,noun_or_verb=0):# 0 for noun 1 for verb
        import torch
        import copy
        doc1_name=doc1[2]
        doc2_name =doc2[2]
        doc_1_type=doc1[3]
        doc_2_type=doc2[3]

        dic_comparison={}
        
        for  sentence_1 in doc1[noun_or_verb]:
            #words_of_first_sentencess=[]
            #words_of_first_sentencess=[wordss[2] for wordss in sentence_1[0]]
            
            #for ii in sentence_1[0]:
                #print(ii[2])
                #words_of_first_sentencess.append(ii[2])
              
            
            #print(words_of_first_sentence)
            #print(words_of_first_sentence)
            
            
            for sentence_2 in doc2[noun_or_verb]:
                #words_of_second_sentencess=[]
                #for i in sentence_2[0]:
                #    words_of_second_sentencess.append(i[2])
                #words_of_second_sentencess=[wordsss[2] for wordsss in sentence_2[0]]
                #print(words_of_second_sentence)
                #print(words_of_second_sentence)
                #if len(sentence_2[0])==0:
                #    continue
                

                #sim_matrix2=torch.matmul(sentence_1[2],sentence_2[2].T).to('cuda')
                sim_matrix2=torch.matmul(sentence_2[2],sentence_1[2].T).to('cuda')

                sim_matrix2=sim_matrix2.detach().cpu()
                sim_matrix44=sim_matrix2.tolist()
                #print(f"matrix{sim_matrix44}")
                #print('hi')
                
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
                if doc_1_type =="case_summaries":
                    dic_comparison[f"{sentence_1[1]}{sentence_1[3][0]}:::{sentence_2[1]}"]= [copy.deepcopy(used_rows), copy.copy(sentence_1[0]) , copy.copy(sentence_2[0]), doc1_name, doc2_name,doc_1_type,doc_2_type,sentence_1[3]]
                    continue
                if doc_2_type =="case_summaries":
                    
                    dic_comparison[f"{sentence_1[1]}:::{sentence_2[1]}{sentence_2[3][0]}"]= [copy.deepcopy(used_rows), copy.copy(sentence_1[0]) , copy.copy(sentence_2[0]), doc1_name, doc2_name,doc_1_type,doc_2_type,sentence_2[3]]
                    continue
                if doc_1_type =="factums":
                    dic_comparison[f"{sentence_1[1]}{sentence_1[3][0]}{sentence_1[4][0]}:::{sentence_2[1]}"]= [copy.deepcopy(used_rows), copy.copy(sentence_1[0]) , copy.copy(sentence_2[0]), doc1_name, doc2_name,doc_1_type,doc_2_type,sentence_1[3],sentence_1[4]]
                    continue

                    
                if doc_2_type =="factums":
                    dic_comparison[f"{sentence_1[1]}:::{sentence_2[1]}{sentence_2[3][0]}{sentence_2[4][0]}"]= [copy.deepcopy(used_rows), copy.copy(sentence_1[0]) , copy.copy(sentence_2[0]), doc1_name, doc2_name,doc_1_type,doc_2_type,sentence_2[3],sentence_2[4]]
                    continue
                

                dic_comparison[f"{sentence_1[1]}:::{sentence_2[1]}"]= [copy.deepcopy(used_rows), copy.copy(sentence_1[0]) , copy.copy(sentence_2[0]), doc1_name, doc2_name,doc_1_type,doc_2_type]

                #dic_comparison[f"{sentence_1[1]}:::{sentence_2[1]}"]= [copy.deepcopy(used_rows), copy.copy(words_of_first_sentencess) , copy.copy(words_of_second_sentencess), doc1_name, doc2_name,doc_1_type,doc_2_type]
                   
        return dic_comparison  
    
                            
                            

    def combine_verb_and_noun_cosines(self, noun_cosines, verb_cosines):
        #import re
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
                
                    
      
        return noun_cosines
    def find_best_matching_doc_sentences_FIRAC_PIPELINE(self,noun_cosines):
        import re
        final_seen_num_dic={}

        seen_num_dic={}
        recording_num_dic={}
        used_second_sentence_dic={}
        
        for key, value in noun_cosines.items():
            key=str(key)
            #sentences_num=re.search(r"(\d+:\d+\w*):::(\d+:\d+\w*)",key)
            sentences_num=re.search(r"(\d+\w*):::(\d+\w*)",key)
            first_sentence_num=sentences_num.group(1)
            second_sentence_num=sentences_num.group(2)
            # trying to ensure no overlap of the sentences
            #print(first_sentence_num)
            #print(second_sentence_num)
            
            if seen_num_dic.get(first_sentence_num):
                
                #check if this sentence is used, if it has we need to use the next best option for the first sentence
                # ensure that the options are of sentences that have not been used
                # how to determine the next best option, store
                
                recording_num_dic[first_sentence_num][0].append(value[7])
                recording_num_dic[first_sentence_num][1].append(second_sentence_num)
                recording_num_dic[first_sentence_num][2].append(value[0])
                recording_num_dic[first_sentence_num][3].append(value[1])
                recording_num_dic[first_sentence_num][4].append(value[2])
                recording_num_dic[first_sentence_num][5].append(value[3])
                recording_num_dic[first_sentence_num][6].append(value[4])
                recording_num_dic[first_sentence_num][7].append(value[5])
                recording_num_dic[first_sentence_num][8].append(value[6])
                
                if value[7]<=seen_num_dic[first_sentence_num][0][0]:
                    #print('meow')
                    continue
                
                
                if value[7]>seen_num_dic[first_sentence_num][0][0]:                    
 
                    if second_sentence_num in used_second_sentence_dic.keys():
                        
                        
                        #print(second_sentence_num)
                        #print(used_second_sentence_dic.keys())
                        # shorter second sentence list deal with this
                        
                        
                        first_sentence_associated_with_second_sentence=used_second_sentence_dic[second_sentence_num]
                        #print(first_sentence_associated_with_second_sentence)

                        #print('this is the first sentence associated with the second sentence in use')

                        # this value might be list so we may need to convert it
                        value_of_first_sentence_second_sentence_pair_in_use = seen_num_dic[first_sentence_associated_with_second_sentence][0][0]
                        #print(value_of_first_sentence_second_sentence_pair_in_use)

                        #print('thi si the value of the first sentence_second sentence pair in use')
                        #print(value[7])

                        # if not then we don't use it   and continue 
                        if value[7]<= value_of_first_sentence_second_sentence_pair_in_use:
                            # if i can't do better just leave everything as it is
                            continue
                    
                        if value[7]> value_of_first_sentence_second_sentence_pair_in_use:
                            # then add this as the second sentence for this particular first sentence
                            #min_index=seen_num_dic[first_sentence_num][0].index(min(seen_num_dic[first_sentence_num][0]))
                            
                            seen_num_dic[first_sentence_num][0][0]=value[7]  
                            seen_num_dic[first_sentence_num][1][0]=second_sentence_num 
                            seen_num_dic[first_sentence_num][2][0]=value[0]  
                            seen_num_dic[first_sentence_num][3][0]=value[1]  
                            seen_num_dic[first_sentence_num][4][0]=value[2]  
                            seen_num_dic[first_sentence_num][5][0]=value[3]  
                            seen_num_dic[first_sentence_num][6][0]=value[4]  
                            seen_num_dic[first_sentence_num][7][0]=value[5]
                            seen_num_dic[first_sentence_num][8][0]=value[6]
                            used_second_sentence_dic[second_sentence_num]=first_sentence_num
                            
                            #now fix the first sentence that has have been updated and keep updating values backpropgating till we get all the second sentence values settled so they are good



                            while True:
                                
                                index_remove_for_second_sentence_not_useful=recording_num_dic[first_sentence_associated_with_second_sentence][0].index(value_of_first_sentence_second_sentence_pair_in_use)
                                # remove this value from all indexes
                                print(index_remove_for_second_sentence_not_useful)
                                print('this is the index of the second sentence in the list for the first sentence')
                                print(recording_num_dic[first_sentence_associated_with_second_sentence][0])
                                print(recording_num_dic[first_sentence_associated_with_second_sentence][1])


                                del recording_num_dic[first_sentence_associated_with_second_sentence][0][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][1][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][2][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][3][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][4][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][5][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][6][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][7][index_remove_for_second_sentence_not_useful]
                                del recording_num_dic[first_sentence_associated_with_second_sentence][8][index_remove_for_second_sentence_not_useful]
                                # find next highest value for this sentence
                                print(recording_num_dic[first_sentence_associated_with_second_sentence][0])
                                print('updated list of values')
                                print(recording_num_dic[first_sentence_associated_with_second_sentence][1])
                                print('updated list of second sentences')


                                index_of_next_highest_value=recording_num_dic[first_sentence_associated_with_second_sentence][0].index(max(recording_num_dic[first_sentence_associated_with_second_sentence][0]))
                                print('this is the new highest value')
                                print(index_of_next_highest_value)
                                # this is the second sentence associated with that value
                                
                                second_sentence_name_for_next_highest_value= recording_num_dic[first_sentence_associated_with_second_sentence][1][index_of_next_highest_value]
                                print(second_sentence_name_for_next_highest_value)
                                print('this is the second sentences name with the highest score')
                                # checking whether it's currently being used
                                if second_sentence_name_for_next_highest_value in used_second_sentence_dic.keys():
                                    print("the second sentence is being used")
                                    print(used_second_sentence_dic.keys())
                                    
                                    stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence=first_sentence_associated_with_second_sentence
                                    # find the value for this second sentence with its first sentence
                                    first_sentence_associated_with_second_sentence=used_second_sentence_dic[second_sentence_name_for_next_highest_value]
                                    value_of_first_sentence_second_sentence_pair_in_use = seen_num_dic[first_sentence_associated_with_second_sentence][0][0]
                                    print('this is the first sentence associated with this sentence')
                                    print(first_sentence_associated_with_second_sentence)
                                    print('this is the value of that first sentence second sentence value pair')
                                    print(value_of_first_sentence_second_sentence_pair_in_use)
                                    
                                    
                                    # where is recording_num_dic_firstence sentence assocaited coming from
                                    print('now we compare this value of the used second sentence against the alternative used value')
                                    print(' the operaiton is if the possilbe use of the second sentence in the original first sentence against the second sentences current use ')
                                    # don't understand this line super important
                                    # the meaning of value_of_first_sentence_second_sentence_pair_in_use is, it is the value of the sentence that is currently using the second sentence value
                                    # simiarly first sentence assocaited now represents this value
                                    # the stored first sentecne asscoaited is the value we should be comparing this value against
                                    # si
                                    if recording_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][0][index_of_next_highest_value]> value_of_first_sentence_second_sentence_pair_in_use:
                                        print('changing how we are using the second sentence would actually be better so we replace the value')
                                        # we can use this value and now we can move on to the next sentence give it an update and if it shit then restart as well
                                        #ERROR HERE
                                        # lets test this
                                        # i think it should be the stored value here and not the updated sentence
                                       
                                        
                                        
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][0][0]=recording_num_dic[first_sentence_associated_with_second_sentence][0][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][1][0]=second_sentence_name_for_next_highest_value 
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][2][0]=  recording_num_dic[first_sentence_associated_with_second_sentence][2][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][3][0]= recording_num_dic[first_sentence_associated_with_second_sentence][3][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][4][0]= recording_num_dic[first_sentence_associated_with_second_sentence][4][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][5][0]=recording_num_dic[first_sentence_associated_with_second_sentence][5][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][6][0]=recording_num_dic[first_sentence_associated_with_second_sentence][6][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][7][0]=recording_num_dic[first_sentence_associated_with_second_sentence][7][index_of_next_highest_value]
                                        seen_num_dic[stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence][8][0]=recording_num_dic[first_sentence_associated_with_second_sentence][8][index_of_next_highest_value]
                                        used_second_sentence_dic[second_sentence_name_for_next_highest_value]=stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence
                                        # the first first_sentence_associated_with_second_sentence will then be moved up to the top
                                        # we will now prepare to set up the first_sentence that was less then this one wiht the second one to go back thru the loop, bascially choosing a new first sentence
                                        print('now we deal with the first sentence whose vlaue we just changed and find it a second sentence')
                                        print(first_sentence_associated_with_second_sentence)
                                        
                                        
                                        continue
                                         
                                        
                                    else:
                                        print('since this value is not greater than the use of the second sentence, we try the next value in orginal stored first sentence ')
                                        # we can't use this value so we need to try the next highest one for this first sentence
                                        # we reintitslize this sentence and try again
                                        first_sentence_associated_with_second_sentence=stored_first_sentence_associated_with_second_sentence_before_comparing_it_to_next_sentence
                                        print(first_sentence_associated_with_second_sentence)
                                        print('we also start by erasing the second sentece we tried from the stored sentence dic and then find the next max sentence')
                                        print('this is that second sentences value')
                                        print(value_of_first_sentence_second_sentence_pair_in_use)
                                        

                                        
                                       

                                        
                                        continue
                                        #try next highest value and restart loop?
                                         
                                    
                                else:
                                    # update value and restart and look at next sentence
                                    print("the second sentence is not being being used")
                                    # so we just update the key with this  value
                                    print(used_second_sentence_dic.keys())


                                    seen_num_dic[first_sentence_associated_with_second_sentence][0][0]=recording_num_dic[first_sentence_associated_with_second_sentence][0][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][1][0]=second_sentence_name_for_next_highest_value 
                                    seen_num_dic[first_sentence_associated_with_second_sentence][2][0]=  recording_num_dic[first_sentence_associated_with_second_sentence][2][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][3][0]= recording_num_dic[first_sentence_associated_with_second_sentence][3][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][4][0]= recording_num_dic[first_sentence_associated_with_second_sentence][4][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][5][0]=recording_num_dic[first_sentence_associated_with_second_sentence][5][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][6][0]=recording_num_dic[first_sentence_associated_with_second_sentence][6][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][7][0]=recording_num_dic[first_sentence_associated_with_second_sentence][7][index_of_next_highest_value]
                                    seen_num_dic[first_sentence_associated_with_second_sentence][8][0]=recording_num_dic[first_sentence_associated_with_second_sentence][8][index_of_next_highest_value]
                                    used_second_sentence_dic[second_sentence_name_for_next_highest_value]=first_sentence_associated_with_second_sentence
                                    break
  
                            continue
                            

                    
                    else:
                        min_index=seen_num_dic[first_sentence_num][0].index(min(seen_num_dic[first_sentence_num][0]))
                        seen_num_dic[first_sentence_num][0][min_index]=value[7]  
                        seen_num_dic[first_sentence_num][1][min_index]=second_sentence_num 
                        seen_num_dic[first_sentence_num][2][min_index]=value[0]  
                        seen_num_dic[first_sentence_num][3][min_index]=value[1]  
                        seen_num_dic[first_sentence_num][4][min_index]=value[2]  
                        seen_num_dic[first_sentence_num][5][min_index]=value[3]  
                        seen_num_dic[first_sentence_num][6][min_index]=value[4]  
                        seen_num_dic[first_sentence_num][7][min_index]=value[5]
                        seen_num_dic[first_sentence_num][8][min_index]=value[6]
                        used_second_sentence_dic[second_sentence_num]=first_sentence_num
                        

                        continue
                        
                   
                
            #if sentences all used up in second doc and with there highest matching sentence break
            # GOING TO NEED TO DEAL WITH THESE and make sure they are dealt with correctly
            
            ############
            # going to need to fix this part
            # one sentence might be off unless we antcipate how these dictionaries might effect the second sentence
            #WE NEED TO FIX why first value in used_second_sentence_is wrong, and delete extra first sentences    
                
                 

            seen_num_dic[first_sentence_num]=[[value[7]],[second_sentence_num],[value[0]],[value[1]],[value[2]],[value[3]],[value[4]],[value[5]],[value[6]]]
            recording_num_dic[first_sentence_num]=[[value[7]],[second_sentence_num],[value[0]],[value[1]],[value[2]],[value[3]],[value[4]],[value[5]],[value[6]]]
            if used_second_sentence_dic.get(second_sentence_num):
                continue
            used_second_sentence_dic[second_sentence_num]=first_sentence_num
            continue
        
        
        for value in used_second_sentence_dic.values():
            final_seen_num_dic[value]=seen_num_dic[value]
            
             
            

        # this deal with a longer second doc deleting the extra keys that have not matched the second sentence
        #for first_sentence in seen_num_dic.keys():
         #   if first_sentence not in used_second_sentence_dic.keys():
                
                
                #del seen_num_dic[first_sentence].keys() not in used_second_sentence_dic.values()
        return final_seen_num_dic,recording_num_dic,used_second_sentence_dic
    # need to solve error with first value of list not matching up
              

            
            
                    
                #print(first_sentence_num)
                
        


        

    def find_best_matching_doc_sentences(self,noun_cosines):
        
         import re

         seen_num_dic={}
         
         for key, value in noun_cosines.items():
             key=str(key)
             sentences_num=re.search(r"(\d+:\d+\w*):::(\d+:\d+\w*)",key)
             first_sentence_num=sentences_num.group(1)
             second_sentence_num=sentences_num.group(2)
             #value
             #print(first_sentence_num)
             #print(second_sentence_num)
             
             if seen_num_dic.get(first_sentence_num):
                 #print(first_sentence_num)
                 
                 
                 if len(value)==8:#full_cases
                 
                     if len(seen_num_dic[first_sentence_num][0])<1:
                         seen_num_dic[first_sentence_num][0].append(value[7])
                         seen_num_dic[first_sentence_num][1].append(second_sentence_num)
                         seen_num_dic[first_sentence_num][2].append(value[0])
                         seen_num_dic[first_sentence_num][3].append(value[1])
                         seen_num_dic[first_sentence_num][4].append(value[2])
                         seen_num_dic[first_sentence_num][5].append(value[3])
                         seen_num_dic[first_sentence_num][6].append(value[4])
                         seen_num_dic[first_sentence_num][7].append(value[5])
                         seen_num_dic[first_sentence_num][8].append(value[6])
                         continue
                     
                     
                     if value[7]>min(seen_num_dic[first_sentence_num][0]):
                         
                         min_index=seen_num_dic[first_sentence_num][0].index(min(seen_num_dic[first_sentence_num][0]))
                         
                         seen_num_dic[first_sentence_num][0][min_index]=value[7]  
                         seen_num_dic[first_sentence_num][1][min_index]=second_sentence_num 
                         seen_num_dic[first_sentence_num][2][min_index]=value[0]  
                         seen_num_dic[first_sentence_num][3][min_index]=value[1]  
                         seen_num_dic[first_sentence_num][4][min_index]=value[2]  
                         seen_num_dic[first_sentence_num][5][min_index]=value[3]  
                         seen_num_dic[first_sentence_num][6][min_index]=value[4]  
                         seen_num_dic[first_sentence_num][7][min_index]=value[5]
                         seen_num_dic[first_sentence_num][8][min_index]=value[6]
                         continue
                     continue
                         
                         
                         
                         
                         
                 
                 
                 if len(value)==9:#case_summaries
                 
                     
                     if len(seen_num_dic[first_sentence_num][0])<1:

                         seen_num_dic[first_sentence_num][0].append(value[8])
                         seen_num_dic[first_sentence_num][1].append(second_sentence_num)
                         seen_num_dic[first_sentence_num][2].append(value[0])
                         seen_num_dic[first_sentence_num][3].append(value[1])
                         seen_num_dic[first_sentence_num][4].append(value[2])
                         seen_num_dic[first_sentence_num][5].append(value[3])
                         seen_num_dic[first_sentence_num][6].append(value[4])
                         seen_num_dic[first_sentence_num][7].append(value[5])
                         seen_num_dic[first_sentence_num][8].append(value[6])
                         seen_num_dic[first_sentence_num][9].append(value[7])

                         continue
                     
                     
                        
                     
                     if value[8]>min(seen_num_dic[first_sentence_num][0]):
                         
                         #print(seen_num_dic[first_sentence_num][0])

                        
                         #print(value[8])
                         #print(min(seen_num_dic[first_sentence_num][0]))
                         min_index=seen_num_dic[first_sentence_num][0].index(min(seen_num_dic[first_sentence_num][0]))
                         
                         seen_num_dic[first_sentence_num][0][min_index]=value[8]  
                         seen_num_dic[first_sentence_num][1][min_index]=second_sentence_num 
                         seen_num_dic[first_sentence_num][2][min_index]=value[0]  
                         seen_num_dic[first_sentence_num][3][min_index]=value[1]  
                         seen_num_dic[first_sentence_num][4][min_index]=value[2]  
                         seen_num_dic[first_sentence_num][5][min_index]=value[3]  
                         seen_num_dic[first_sentence_num][6][min_index]=value[4]  
                         seen_num_dic[first_sentence_num][7][min_index]=value[5]
                         seen_num_dic[first_sentence_num][8][min_index]=value[6]
                         seen_num_dic[first_sentence_num][9][min_index]=value[7]
                         #print(seen_num_dic[first_sentence_num][0])

                         

                         continue
                     continue

                         
 
                         

                 if len(value)==10:#factums
                     if len(seen_num_dic[first_sentence_num][0])<1:
                         
                         seen_num_dic[first_sentence_num][0].append(value[9])
                         seen_num_dic[first_sentence_num][1].append(second_sentence_num)
                         seen_num_dic[first_sentence_num][2].append(value[0])
                         seen_num_dic[first_sentence_num][3].append(value[1])
                         seen_num_dic[first_sentence_num][4].append(value[2])
                         seen_num_dic[first_sentence_num][5].append(value[3])
                         seen_num_dic[first_sentence_num][6].append(value[4])
                         seen_num_dic[first_sentence_num][7].append(value[5])
                         seen_num_dic[first_sentence_num][8].append(value[6])
                         seen_num_dic[first_sentence_num][9].append(value[7])
                         seen_num_dic[first_sentence_num][10].append(value[8])
                         continue
                     
                        
                     if value[9]>min(seen_num_dic[first_sentence_num][0]):
                         
                         min_index=seen_num_dic[first_sentence_num][0].index(min(seen_num_dic[first_sentence_num][0]))
                         seen_num_dic[first_sentence_num][0][min_index]=value[9]  
                         seen_num_dic[first_sentence_num][1][min_index]=second_sentence_num 
                         seen_num_dic[first_sentence_num][2][min_index]=value[0]  
                         seen_num_dic[first_sentence_num][3][min_index]=value[1]  
                         seen_num_dic[first_sentence_num][4][min_index]=value[2]  
                         seen_num_dic[first_sentence_num][5][min_index]=value[3]  
                         seen_num_dic[first_sentence_num][6][min_index]=value[4]  
                         seen_num_dic[first_sentence_num][7][min_index]=value[5]
                         seen_num_dic[first_sentence_num][8][min_index]=value[6]
                         seen_num_dic[first_sentence_num][9][min_index]=value[7]
                         seen_num_dic[first_sentence_num][10][min_index]=value[8]
                         continue
                     continue

                 
             
             if len(value)==8:
                 #full_cases
                 seen_num_dic[first_sentence_num]=[[value[7]],[second_sentence_num],[value[0]],[value[1]],[value[2]],[value[3]],[value[4]],[value[5]],[value[6]]]
                 continue
             
             
             if len(value)==9:
                 #case_summary
                 seen_num_dic[first_sentence_num]=[[value[8]],[second_sentence_num],[value[0]],[value[1]],[value[2]],[value[3]],[value[4]],[value[5]],[value[6]],[value[7]]]
                 continue

                 
             if len(value)==10:
                 #factum
                 seen_num_dic[first_sentence_num]=[[value[9]],[second_sentence_num],[value[0]],[value[1]],[value[2]],[value[3]],[value[4]],[value[5]],[value[6]],[value[7]],[value[8]]]
                 continue

                 
         
         return seen_num_dic
     
        
      
    def save_cosine_simialrities_FIRAC_PIPELINE(self, seen_num_dic):
       for cos_sentence_key, cos_sentence_value in seen_num_dic.items():
               for average_sim_score,sentence_number2,sim_scores,sentence_1_words,sentence_2_words,document_name_1,document_name_2,database_1,database_2  in zip(cos_sentence_value[0],cos_sentence_value[1],cos_sentence_value[2],cos_sentence_value[3],cos_sentence_value[4],cos_sentence_value[5],cos_sentence_value[6],cos_sentence_value[7],cos_sentence_value[8]):
                   word_assocoiated_list_1=[word[2] for word in sentence_1_words]
                   word_assocoiated_list_2=[word2[2] for word2 in sentence_2_words]
                   word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\'","")
                   word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\"","")
                   word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\'","")
                   word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\"","")
                   
                   self.cur.execute( f""" INSERT INTO embedding_sim_scores5 (sim_scores,average_sim_score, sentence_1_words,sentence_2_words, sentence_number1,sentence_number2, document_name_1,document_name_2,database_1,database_2)
                               VALUES ('{str(sim_scores)}','{str(average_sim_score)}','{str(word_assocoiated_list_1)}','{str(word_assocoiated_list_2)}','{str(cos_sentence_key)}','{str(sentence_number2)}','{str(document_name_1)}', '{str(document_name_2)}','{str(database_1)}','{str(database_2)}');""")
       self.conn.commit()
        
        
        


    
    def save_cosine_simialrities_in_firac_labels(self, seen_num_dic):
        """ upload the simiarlities score of a given sentence to the database showing which sentences are matched between the two documents, and there FIRAC placement"""
        
            
        for cos_sentence_key, cos_sentence_value in seen_num_dic.items():

            if len(cos_sentence_value)==9:
                #full_case
                for average_sim_score,sentence_number2,sim_scores,sentence_1_words,sentence_2_words,document_name_1,document_name_2,database_1,database_2  in zip(cos_sentence_value[0],cos_sentence_value[1],cos_sentence_value[2],cos_sentence_value[3],cos_sentence_value[4],cos_sentence_value[5],cos_sentence_value[6],cos_sentence_value[7],cos_sentence_value[8]):
                    
                    word_assocoiated_list_1=[word[2] for word in sentence_1_words]
                    word_embedding_list_1 =[embedding[0] for embedding in sentence_1_words]
                    
                    word_assocoiated_list_2=[word2[2] for word2 in sentence_2_words]
                    word_embedding_list_2 =[embedding2[0] for embedding2 in sentence_2_words]
                    
                    word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\'","")
                    word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\"","")
                    word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\'","")
                    word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\"","")
                    self.cur.execute( f""" INSERT INTO embedding_sim_scores (sim_scores,average_sim_score, sentence_1_words,sentence_2_words,sentence_1_embeddings,sentence_2_embeddings, sentence_number1,sentence_number2, document_name_1,document_name_2,database_1,database_2)
                                VALUES ('{str(sim_scores)}','{str(average_sim_score)}','{str(word_assocoiated_list_1)}','{str(word_assocoiated_list_2)}','{str(word_embedding_list_1)}','{str(word_embedding_list_2)}','{str(cos_sentence_key)}','{str(sentence_number2)}','{str(document_name_1)}', '{str(document_name_2)}','{str(database_1)}','{str(database_2)}');""")
                self.conn.commit()

            if len(cos_sentence_value)==10:
                for average_sim_score,sentence_number2,sim_scores,sentence_1_words,sentence_2_words,document_name_1,document_name_2,database_1,database_2,firac  in zip(cos_sentence_value[0],cos_sentence_value[1],cos_sentence_value[2],cos_sentence_value[3],cos_sentence_value[4],cos_sentence_value[5],cos_sentence_value[6],cos_sentence_value[7],cos_sentence_value[8],cos_sentence_value[9]):
                    word_assocoiated_list_1=[word[2] for word in sentence_1_words]
                    word_embedding_list_1 =[embedding[0] for embedding in sentence_1_words]
                    
                    word_assocoiated_list_2=[word2[2] for word2 in sentence_2_words]
                    word_embedding_list_2 =[embedding2[0] for embedding2 in sentence_2_words]
                    
                    word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\'","")
                    word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\"","")
                    word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\'","")
                    word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\"","")

                   
                    self.cur.execute( f""" INSERT INTO embedding_sim_scores (sim_scores,average_sim_score, sentence_1_words,sentence_2_words,sentence_1_embeddings,sentence_2_embeddings, sentence_number1,sentence_number2, document_name_1,document_name_2,database_1,database_2,firac)
                                VALUES ('{str(sim_scores)}','{str(average_sim_score)}','{str(word_assocoiated_list_1)}','{str(word_assocoiated_list_2)}', '{str(word_embedding_list_1)}','{str(word_embedding_list_2)}','{str(cos_sentence_key)}','{str(sentence_number2)}','{str(document_name_1)}', '{str(document_name_2)}','{str(database_1)}','{str(database_2)}','{str(firac)}');""")
                self.conn.commit()
                #case_summary
                
            if len(cos_sentence_value)==11:
                for average_sim_score,sentence_number2,sim_scores,sentence_1_words,sentence_2_words,document_name_1,document_name_2,database_1,database_2,firac,appvres  in zip(cos_sentence_value[0],cos_sentence_value[1],cos_sentence_value[2],cos_sentence_value[3],cos_sentence_value[4],cos_sentence_value[5],cos_sentence_value[6],cos_sentence_value[7],cos_sentence_value[8],cos_sentence_value[9],cos_sentence_value[10]):
                    
                    word_assocoiated_list_1=[word[2] for word in sentence_1_words]
                    word_embedding_list_1 =[embedding[0] for embedding in sentence_1_words]
                    
                    word_assocoiated_list_2=[word2[2] for word2 in sentence_2_words]
                    word_embedding_list_2 =[embedding2[0] for embedding2 in sentence_2_words]

                    word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\'","")
                    word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\"","")
                    word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\'","")
                    word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\"","")
                    self.cur.execute( f""" INSERT INTO embedding_sim_scores (sim_scores,average_sim_score, sentence_1_words,sentence_2_words,sentence_1_embeddings,sentence_2_embeddings, sentence_number1,sentence_number2, document_name_1,document_name_2,database_1,database_2,firac,appvres)
                                VALUES ('{str(sim_scores)}','{str(average_sim_score)}','{str(word_assocoiated_list_1)}','{str(word_assocoiated_list_2)}','{str(word_embedding_list_1)}','{str(word_embedding_list_2)}','{str(cos_sentence_key)}','{str(sentence_number2)}','{str(document_name_1)}', '{str(document_name_2)}','{str(database_1)}','{str(database_2)}','{str(firac)}','{str(appvres)}');""")
                self.conn.commit()
                #factum


                
                

            
            
                            #VALUES ('{str(cos_sentence_value[0])}','{str(cos_sentence_value[5])}','{str(cos_sentence_value[1])}','{str(cos_sentence_value[2])}','{str(sentence_1)}','{str(sentence_2)}','{str(cos_sentence_value[3])}', '{str(cos_sentence_value[4])}');""")

                
                

            #sentences_num=re.search(r"(\d+):(\d+)",cos_sentence_key)
            

            #sentence_1=sentences_num.group(1)
            #sentence_2=sentences_num.group(2)
 
  
class CAN_LAW_ACCESSIBLE_network():
    def __init__(self):
        import psycopg2
        import torch
        import numpy as np
        #from  Pos_model_trainer import network
        super().__init__()
        self.conn =  psycopg2.connect(dbname="Can_Law_Accessible", user="postgres", password="MeganisGreat")
        self.cur = self.conn.cursor()
        
        self.sentence_info = []
        self.pos_word_list= []
        self.document_name = ""
        self.document_verb= []
        self.document_noun=[]
        self.torch_catche= torch.cuda.empty_cache()
        self.document_id=""
        self.final_sentence_info_list=[]
        self.max_value=1.0
        self.npmax=np.argmax(self.max_value) # find pytorch arg max function
        self.unwanted_characters=[".","?","[","]","(",")"]
        self.database=""
    
    def init_fact_cluster_model(self):
        import torch

        from unwanted_sentence_model_network import network
        
        self.FIRAC_model_word=network(768, 1000, 500).to("cuda")
        FIRAC_word_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_fact_cluster.pth")
        self.FIRAC_model_word.load_state_dict(FIRAC_word_state_dic)

        
    def init_issue_cluster_model(self):
        import torch

        from unwanted_sentence_model_network import network
        
        self.FIRAC_model_word=network(768, 1000, 120).to("cuda")
        FIRAC_word_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_issue_cluster.pth")
        self.FIRAC_model_word.load_state_dict(FIRAC_word_state_dic)
        
    def init_holding_cluster_model(self):
        import torch

        from unwanted_sentence_model_network import network
        
        self.FIRAC_model_word=network(768, 1000, 120).to("cuda")
        FIRAC_word_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_holding_cluster.pth")
        self.FIRAC_model_word.load_state_dict(FIRAC_word_state_dic)
    def init_law_cluster_model(self):
        import torch

        from unwanted_sentence_model_network import network
        # not sure of the dimensions yet
        self.FIRAC_model_word=network(768, 1000, 120).to("cuda")
        FIRAC_word_state_dic = torch.load(r"C:\Users\doggo777\Documents\Kimlichcova\model_law_cluster.pth")
        self.FIRAC_model_word.load_state_dict(FIRAC_word_state_dic)
        
        
        
    def upload_case_text(self,data_base_with_sim_scores, type_of_cluster="fact"):
        #document_info_dic={}
        import copy
        import pickle
        import json
        clustered_by_fact_dic={}
        clustered_by_fact_dic_without_average={}
        central_tendency_finder_list=[]
       # embedding_sim_scores4=embedding_sim_scores4
       # we are going to try to  use the whole sim_score list instead of the average
       
        self.cur.execute( f""" SELECT document_name_2, sim_scores,document_name_1
                         FROM {data_base_with_sim_scores}
                         ORDER BY ID DESC
                         """) 
        
        document_information_list= self.cur.fetchall()
        
        for document_info in document_information_list:
            document_2_name=document_info[0]
            sim_score_list=json.loads(document_info[1])
            #average_sim_score=float(document_info[1])
            document_1_name=document_info[2]
            if clustered_by_fact_dic_without_average.get(f"{document_1_name}::{document_2_name}"):
                for word_comparsion_score in sim_score_list:
                    clustered_by_fact_dic_without_average[f"{document_1_name}::{document_2_name}"].append(word_comparsion_score)
                    central_tendency_finder_list.append(word_comparsion_score)
                    continue                        
            clustered_by_fact_dic_without_average[f"{document_1_name}::{document_2_name}"]=sim_score_list

             
            continue
        #<3 eliminate all mentions of it
            #print('we')
        central_tendency=sum(central_tendency_finder_list)/len(central_tendency_finder_list)
        #print(len(central_tendency_finder_list))
        #print(central_tendency)
        for k,temp_doc_sim_score_list in clustered_by_fact_dic_without_average.items():
            average_doc_relationship_without=sum(temp_doc_sim_score_list)/len(temp_doc_sim_score_list)
            print(f"normal {average_doc_relationship_without}")

            #print(k)
            #print(temp_doc_sim_score_list)
            #print(len(temp_doc_sim_score_list))
            

            len_temp_sim_score_list=len(temp_doc_sim_score_list)
            percentage_impact_per_num=100/len_temp_sim_score_list
            #print(percentage_impact_per_num)
            weighted_list=[abs(central_tendency-word_sim_score_in_doc_sim_score)*percentage_impact_per_num*0.009 + percentage_impact_per_num for word_sim_score_in_doc_sim_score in temp_doc_sim_score_list]
            #print(weighted_list)
            total_weight_count=sum(weighted_list)
            #print(total_weight_count)
            values_for_determining_mean_list=[word_sim_score_in_doc_sim_score*weight for word_sim_score_in_doc_sim_score, weight in zip(temp_doc_sim_score_list,weighted_list)]
            #print(values_for_determining_mean_list)

            average_doc_relationship=sum(values_for_determining_mean_list)/total_weight_count
            print(f"new {average_doc_relationship}")

            clustered_by_fact_dic[k]=average_doc_relationship

            #percentage_list=100/len(temp_doc_sim_score_list)
            #percentage must add to add
            #decrease some and increase others
            
            #for temp_doc_sim_score_list:
                #get intital percentages of each into a list
                #then 
                # distance from central_tendenncy will increase its weight and 
            
            # updating average
            
            # this is where we solve the averaging problem
                

               #temp_clustered_fact_dic_for_single_doc[k]=[average_doc_relationship,temp_doc_sim_score_list]
           #print(temp_clustered_fact_dic_for_single_doc)
        #clustered_by_fact_dic[k]=copy.deepcopy(clustered_by_fact_dic_without_average)
        #print('hi')
        
        
        
        
        embedding_file_name= f"clustered_dictionary_by_{type_of_cluster}.pickle"
        embedding_path_name= r"C:\Users\doggo777\Documents\Kimlichcova" + "\\" + embedding_file_name
        with open(embedding_path_name,"wb") as f10:
           pickle.dump(clustered_by_fact_dic, f10, pickle.HIGHEST_PROTOCOL)       
        return clustered_by_fact_dic
    
    
    def sort_into_clusters_0(self,type_of_cluster="fact"):# averaging the sentences
        import pickle
        import re
        clustered_by_fact_dic_without_average={}
        #dict of sentence_2->dict of document_1, with its sim score as a key 
        
        embedding_file_name= f"clustered_dictionary_by_{type_of_cluster}.pickle"
        embedding_path_name= r"C:\Users\doggo777\Documents\Kimlichcova" + "\\" + embedding_file_name
        with open(embedding_path_name,"rb") as f10:
           clustered_by_fact_dic=pickle.load( f10)    
        
        for doc1_name_doc_2_name,average_sim_score in clustered_by_fact_dic.items():
             doc_names=re.search(r"(.*)::(.*)",doc1_name_doc_2_name )
             doc1_name=doc_names.group(1)
             doc2_name=doc_names.group(2)
             #print(doc1_name)
             #print(doc2_name)
             #print(average_sim_score)
             
             if clustered_by_fact_dic_without_average.get(doc1_name):
                 clustered_by_fact_dic_without_average[doc1_name][doc2_name]= float(average_sim_score)
                 continue                        
                 
             clustered_by_fact_dic_without_average[doc1_name]={doc2_name :float(average_sim_score)}
             continue
        return clustered_by_fact_dic_without_average
    
    
    def sort_into_clusters_1(self,clustered_by_fact_dic_without_average):
        """ this will take the sims scores and will require us to sum them and then sort them into the correct categories they should be in"""

        import pickle
        import re
        #scores_of_each_case_valeus_to_ensure_working_correctly=[]
        clustered_by_fact_dic_with_hierarchy_list={}
        for doc1_name, document_list in clustered_by_fact_dic_without_average.items():
            scores_of_each_case=[]
            for doc_2_name, value in document_list.items():
                    scores_of_each_case.append(value)
            
            scores_of_each_case.sort(reverse=True)
            
            # get cases names that correspond to the case
            for doc_2_name2, value2 in document_list.items():
                if value2 in scores_of_each_case:
                    value_index=scores_of_each_case.index(value2)
                    scores_of_each_case[value_index]=doc_2_name2
                    #scores_of_each_case_valeus_to_ensure_working_correctly.append(value2)
                    
            clustered_by_fact_dic_with_hierarchy_list[doc1_name]=scores_of_each_case
        return clustered_by_fact_dic_with_hierarchy_list#,scores_of_each_case_valeus_to_ensure_working_correctly 
                


    def sort_into_clusters_2(self,clustered_by_fact_dic,clustered_by_fact_dic_with_hierarchy_list,number_in_cluster=60):
        
        """ this is where we adjust the dictionary to include all the cases positions in a list or more atleast""" 
        import copy
        import random
        clustered_by_fact_dic_with_hierarchy_list_for_mods=copy.deepcopy(clustered_by_fact_dic_with_hierarchy_list)
        
        for doc1_name,hierarhcial_case_list in clustered_by_fact_dic_with_hierarchy_list.items():
            # these are the cases that doc2_name was compared agaisnt, within this hierachcal_case_list
            # if we get bad results, this one might be responsible
            if len(hierarhcial_case_list)>number_in_cluster:
                for i, case in enumerate(hierarhcial_case_list[:15]):

                        #print(index_of_case_being_compared_against)

                        match_list=[casee for casee in hierarhcial_case_list if casee in list(clustered_by_fact_dic[case].keys())]
                        # the matches here are when we find a common case in the lists that have been compared to a case in the intital comparsion list
                        if len(match_list)>0:
                                for matched_case_name in match_list:
                                    if case == matched_case_name:
                                        continue
                                    index_of_case_being_compared_against=clustered_by_fact_dic_with_hierarchy_list_for_mods[doc1_name].index(case)
                                    index_in_adjcent_case_list=clustered_by_fact_dic_with_hierarchy_list_for_mods[case].index(matched_case_name)
                                    index_of_matched_case_in_current_case_list=clustered_by_fact_dic_with_hierarchy_list_for_mods[doc1_name].index(matched_case_name)
        
                                    if index_of_case_being_compared_against<index_of_matched_case_in_current_case_list:# this ensures that the cases are never put above above the top one being compared
                                        if index_in_adjcent_case_list!=0:
                                            #if index_in_adjcent_case_list>10:
                                            #    index_in_adjcent_case_list=random.randint(0,5)
                                                #index_in_adjcent_case_list=1
                                                # will have ot check this
                                            for case_name_from_adj_list in clustered_by_fact_dic_with_hierarchy_list_for_mods[case][:index_in_adjcent_case_list]:
                                                #case_name_from_adj_list= clustered_by_fact_dic_with_hierarchy_list_for_mods[case][index_in_adjcent_case_list]
                                                if case_name_from_adj_list not in list(clustered_by_fact_dic[doc1_name].keys()):
                                                    case_name_index_value=f"above {matched_case_name}"
                                                    clustered_by_fact_dic_with_hierarchy_list_for_mods[doc1_name].insert(index_of_matched_case_in_current_case_list,case_name_from_adj_list)
                                                    clustered_by_fact_dic[doc1_name][case_name_from_adj_list]=case_name_index_value

          
        return clustered_by_fact_dic_with_hierarchy_list_for_mods, clustered_by_fact_dic
    
    
    def save_whole_database_clusters(self,clustered_by_fact_dic_with_hierarchy_list_for_mods):
        """ load the case dictionary and there clusters to sql database"""
        for document,hierarchy_list in clustered_by_fact_dic_with_hierarchy_list_for_mods.items():
            hierarchy_list=str(hierarchy_list).replace("\'","")
            hierarchy_list=str(hierarchy_list).replace("\"","")
            hierarchy_list=str(hierarchy_list).replace("\'","")
            hierarchy_list=str(hierarchy_list).replace("\"","")
            self.cur.execute( f""" INSERT INTO whole_clusters_by_fact (document_name,document_hierarchy_list)
                        VALUES ('{str(document)}','{str(hierarchy_list)}');""")
                        
                        
        self.conn.commit()
        
    def sort_into_clusters_3(self,clustered_by_fact_dic_with_hierarchy_list_for_mods,number_of_clusters=500, number_in_cluster=60):
        """ this is where we try the comibnation of cases that has the best diversity"""
        #cases_list=[]
        chosen_fact_clusters={}
        #points_list=[]
        density_dicc={}
        import random
        counterr=-1
        for document,hierarchy_list in clustered_by_fact_dic_with_hierarchy_list_for_mods.items():
            if len(hierarchy_list)>number_in_cluster:# for the first 500 inputs
              if len(chosen_fact_clusters)<number_of_clusters:
                      counterr+=1
                      #print(len(chosen_fact_clusters))
                      chosen_fact_clusters[counterr]=[case for case in hierarchy_list]
                      
                      
                      if len(chosen_fact_clusters)==number_of_clusters:
                          print(len(chosen_fact_clusters))
                          for case_list2 in chosen_fact_clusters.values():
                              for caseeee in case_list2:
                                  if density_dicc.get(caseeee):
                                      density_dicc[caseeee]+=1
                                      continue
                                  density_dicc[caseeee]=1
                          continue
                      continue            
                         

              # for after the cluster_list_is_formed exists
              #return density_dicc,chosen_fact_clusters
              #print(number_of_clusters)
              #print(len(chosen_fact_clusters))


              if len(chosen_fact_clusters)>=number_of_clusters:
                  values_of_changing_case_cluster_to_new_case_cluster=[] # higher value means more valuable
                  # will need to check if the cases are being found here
                  for cluster_number, case_list in chosen_fact_clusters.items():
                      #print(case_list)
                      # WILL NEED TO CHECK THIS PART WHEN I CAN
                      
                      cases_in_density_dic_list=[density_dicc[case4] for case4 in hierarchy_list if case4 in case_list] # this will get the cases value
                      number_of_new_cases=len(hierarchy_list)-len(cases_in_density_dic_list)
                      value_of_new_cases_in_change_list=number_of_new_cases*200
                      changing_this_cluster_value=sum(cases_in_density_dic_list)+value_of_new_cases_in_change_list
                      values_of_changing_case_cluster_to_new_case_cluster.append(changing_this_cluster_value)
                      continue
                  #print(values_of_changing_case_cluster_to_new_case_cluster)
  
                  # use the values_list of exchanging a cluster value, to determine which cluster to exchange and exchange it
                  if max(values_of_changing_case_cluster_to_new_case_cluster)>60:
                      
                      if max(values_of_changing_case_cluster_to_new_case_cluster)==number_in_cluster*200:
                          while True:
                              random_index=random.randint(0,number_of_clusters-1)
                              
                              if values_of_changing_case_cluster_to_new_case_cluster[random_index]==number_in_cluster*200:
                                  index_of_cluster_to_change=random_index
                                  randd=1
                                  break
                                                   
                      if randd!=1:
                          index_of_cluster_to_change=values_of_changing_case_cluster_to_new_case_cluster.index(max(values_of_changing_case_cluster_to_new_case_cluster))
                      #print(index_of_cluster_to_change)
                      for case7 in chosen_fact_clusters[index_of_cluster_to_change]:
                          density_dicc[case7]-=1
                          if density_dicc[case7]==0:
                              del density_dicc[case7]
                      print(len(density_dicc))
                          # this removes from the density dic
                          
                      for case9 in hierarchy_list[:number_in_cluster]:
                          if density_dicc.get(case9):
                              density_dicc[case9]+=1
                              continue
                          density_dicc[case9]=1
                          continue
                      chosen_fact_clusters[index_of_cluster_to_change]=[caseeeeeee for caseeeeeee in hierarchy_list[:number_in_cluster]]
                      randd=0
                      # this is to add the new cluster to the main chosen_fact_clusters 
                      

                      
            else:
                continue
                
        return chosen_fact_clusters, density_dicc
            
  
    
    def save_fact_clusters(self,chosen_fact_clusters):
        """this is where we will save our 500 fact clusters and the cases we have decided to have inside them"""
        
        for document,hierarchy_list in chosen_fact_clusters.items():
            hierarchy_list=str(hierarchy_list).replace("\'","")
            hierarchy_list=str(hierarchy_list).replace("\"","")
            hierarchy_list=str(hierarchy_list).replace("\'","")
            hierarchy_list=str(hierarchy_list).replace("\"","")

            self.cur.execute( f""" INSERT INTO final_fact_clusters (document_name,document_hierarchy_list)
                        VALUES ('{str(document)}','{str(hierarchy_list)}');""")
                        
                        
        self.conn.commit()




             
    def get_issue_clusters(self):
        """ from the sorted fact clusters get the coressponding issue clusters"""
        
        
  
        
    def get_argument_clusters(self):
        """ from the sorted fact clusters get the coressponding issue clusters"""
        
        
    def save_hierarical_clusters(self):
        """ this function will save the structure of facts issues and arguments and what clusters they fall into for a database"""
    
    
    
    #def app_v_res_modifications_to_fact_input(self):
    #    """ before feeding in fact we would apply this classifer to the model to change the output to get variation and see different results and different ways to characerize the facts"""
    #    # perhaps we can use a 
    # need to train models to apply these steps
  
 
    def find_case_fact_cluster(self,fact_pattern):
        """ compare each fact sentence in a document to another fact sentence in a document on the basis of noun and verbs """

        
    def find_issues(self,fact_cluster_number):
        """ compare results of fact search choice among issue sentences"""

    def find_holding(self,issue_cluster_number):
        """ compare results of issue search against the true argument to determine a list of best arguments that might be used in a decision"""
        
            
        
    def find_law_in_issue_or_argument(self, issue_cluster_number,argument_cluster_number):
        """ locate all mentions of law in the issue sentences, and argument_cluster by searching the cases and legislation that is used in the document"""
        #pin_point the legilsaiton
        
        #once cases located based on argument simalritiy identify law in case
        
        #return law_in_cases
    #predict which words are important
    #predict which words would likely be used in a factum vs a decision
    # start with an intital fact pattern, and labels how the sentence has changed whcih words to omit
    # then we next time we run a fact pattern thru it can decide on the basis of the embeddings which words
    # might be changed which words might not be changed in order to sort of recharacrize the fact scenario
    #goal of the model is to find a different way to state the issues
    def locate_law_in_law_doc(self):
        """once we figure out what law we should be looking at find its closest other documents depending on the section"""
        # run law thru to convert to embedding_form
        # cosine sim law of argument against law in document
        # locate which section of doc that argument best matches
        # if we can pin point would be great, will depend on the document
        # then we cluster passages in legislation by similarity
        # we then cluster with the same prcess we have here
        # argument -> label which is passage in clusters of passages
    #network will depend on
 
    def find_similar_law(self, country, province=""):
        """find this law to make the argument relevent in the jurisdiction you are working in"""
        
        
        
        