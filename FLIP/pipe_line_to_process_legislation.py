# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:02:30 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

class legislation_vectorizer():
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
        
        
    def get_next_document(self,previous_document_id):
        """ we use this to find the next document in the case_database after the first one and so on""" 
        
                          
        self.cur.execute(f""" SELECT ID, case_name, full_case_text
                          FROM legislation_can
                          WHERE ID <'{int(previous_document_id)}'  
                          ORDER BY ID DESC
                          LIMIT 1;""")
        cur_result4= self.cur.fetchall()
        self.document_name=cur_result4[0][1]
        self.document_id= cur_result4[0][0]
        document_text=cur_result4[0][2]
        #self.document_law=cur_result4[0][3]
        self.database="legislation_can"
        return document_text
    
    
    def pre_process_text(self, document):
        """ what is needed to reduce the size and make the text consistent before it goes in the network"""
        import re
        import unicodedata
        """ remove extra spacing, names, tabs, and other unwanted values"""
        #f= re.sub("\n"," ", document)
        f= re.sub("\t"," ", document)
        f= re.sub("\r"," ", f)
        f=re.sub(r" \s+", r" ", f)
        f= re.sub(r"\\x\S+",r" ",f )
        f= re.sub(r"@", "",f )
        f = unicodedata.normalize("NFKD", f)
        return f
    def divide_doc_into_sections(self, document):
        """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
        from nltk.tokenize import sent_tokenize
        import re
        list_of_sections=[]
        #index_used_list=[]
        self.sentences=[]
        find_word_pattern = re.compile(r"\w+")
        
        return list_of_sections
        
    def tokenize_document(self, section):# this is a single sentence using the contexualized sentnece list
         import re
         self.at_working=0

         #finding_start_of_second_sentence=re.compile(r"1")
         inputs = self.tokenizer(section, return_tensors="pt", truncation=True, return_token_type_ids=True).to("cuda")
         ids_of_tokens=inputs['input_ids'].tolist()
         token_sentence_ids=inputs['token_type_ids'].tolist()
         [token_sentence_ids] = token_sentence_ids
         [ids_of_tokens] = ids_of_tokens
         token_values_of_ids=self.tokenizer.convert_ids_to_tokens(ids_of_tokens)
         self.sentence_info=[token_values_of_ids,ids_of_tokens,token_sentence_ids]
         
         self.sentence_info[0]=self.sentence_info[0][1:-1]
         self.sentence_info[1]=self.sentence_info[1][1:-1]
         self.sentence_info[2]=self.sentence_info[2][1:-1]

         
         self.index_of_sep=self.sentence_info[0].index("[SEP]")
         
         del self.sentence_info[0][self.index_of_sep]
         del self.sentence_info[1][self.index_of_sep]
         del self.sentence_info[2][self.index_of_sep]
         #print('hi')
         return inputs
     
    def generate_embeddings(self, inputs):
         import torch
         import copy
         """ converting text to embeddings using a pre-trained deberta model"""
         new_output = self.model(**inputs)
         new_output=new_output["last_hidden_state"]
         new_output=new_output[0]
         new_output=new_output[1:-1]
         before_sep=new_output[:self.index_of_sep]
         # IF THE EMBEDDINGS DON"T START TO LOOK RIGHT WILL NEED TO CHECK THIS
         after_sep=new_output[self.index_of_sep+1:]
         new_output=torch.cat((before_sep, after_sep), 0)
         self.torch_catche
         
         new_output_list=new_output.tolist()  
        

         self.sentence_info.append(new_output_list)
         self.sentence_info[4]=new_output_list
   
         embedding_information_list=self.sentence_info
         
         return embedding_information_list,new_output
     
        
    
     
    def run_values_thru_unwanted_sentences(self,list_of_document_infos): # we are going to use this  # need to change this to work with updated method     
          """ feed in all sentences in their embedding format and output only sentences that are cleaned and want to work with"""
          returnn="false"
          un_pred=self.unwanted_model.forward(list_of_document_infos[4])
          # 0 represents not wanted, 1 represents wanted
          un_pred=un_pred.tolist()
          un_pred=[pred.index(max(pred))for pred in un_pred]
          count_of_zeros=un_pred.count(0)
          if count_of_zeros==len(list_of_document_infos[0]):
              returnn="true"

          if len(list_of_document_infos[0])>5:
              if count_of_zeros > len(list_of_document_infos[0])*0.63:
                  

                  returnn="true"
         
          return returnn
      
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
          
          for iiiii, predd in enumerate(pos_predictions):
   
              if predd == 1 or predd == 0:
                  #print('hi')
                  counterr+=1
                  #final_sentence_info_list
                  final_word_list.append(list_of_document_infos[0][iiiii]) # words
                  #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech
                  final_embedding_list.append(list_of_document_infos[3][iiiii]) #embeddings
                  final_pos_list.append(predd)# pos                              
          self.final_sentence_info_list.append(final_word_list) # words
          
          self.final_sentence_info_list[0]=str(self.final_sentence_info_list[0]).replace("\'","")
          self.final_sentence_info_list[0]=str(self.final_sentence_info_list[0]).replace("\"","")  
          
          self.final_sentence_info_list.append(final_embedding_list) #embeddings
          #self.final_sentence_info_list[1]=final_embedding_list

          self.final_sentence_info_list.append(final_pos_list)
          # THIS SHOULD THE FIRAC VALUE
          
    def upload_leg_section_to_sentence_embedding_database(self, paragraph_number):
        """ uploading to database with FIRAC labels generated from FIRAC model"""
        
        
        self.cur.execute( f""" INSERT INTO leg_embeddings (id,words,embeddings,pos,firac,document_name,sentence_number,type_of_document)
                    VALUES ('{self.document_id}','{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.final_sentence_info_list[3])}','{str(self.document_name)}','{paragraph_number}','{self.database}');""")
        self.conn.commit()
        
        
    def  upload_embeddings_from_legislation_database_FIRAC_PIPELINE(self,idd):
        """this is to be used when uploading full cases that  have been processed by the FIRAC MODEL"""
        self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number,document_name
                          FROM leg_embeddings 
                          WHERE id = '{idd}' 
                          ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
        cur_result2= self.cur.fetchall()
        print('meow')
        document_type="full_cases"
        return cur_result2 , document_type
    
    
    
    
    def save_cosine_simialrities_leg_FIRAC_PIPELINE(self, seen_num_dic):
       for cos_sentence_key, cos_sentence_value in seen_num_dic.items():
               for average_sim_score,sentence_number2,sim_scores,sentence_1_words,sentence_2_words,document_name_1,document_name_2,database_1,database_2  in zip(cos_sentence_value[0],cos_sentence_value[1],cos_sentence_value[2],cos_sentence_value[3],cos_sentence_value[4],cos_sentence_value[5],cos_sentence_value[6],cos_sentence_value[7],cos_sentence_value[8]):
                   word_assocoiated_list_1=[word[2] for word in sentence_1_words]
                   word_assocoiated_list_2=[word2[2] for word2 in sentence_2_words]
                   word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\'","")
                   word_assocoiated_list_1=str(word_assocoiated_list_1).replace("\"","")
                   word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\'","")
                   word_assocoiated_list_2=str(word_assocoiated_list_2).replace("\"","")
                   
                   self.cur.execute( f""" INSERT INTO embedding_sim_scores_leg (sim_scores,average_sim_score, sentence_1_words,sentence_2_words, sentence_number1,sentence_number2, document_name_1,document_name_2,database_1,database_2)
                               VALUES ('{str(sim_scores)}','{str(average_sim_score)}','{str(word_assocoiated_list_1)}','{str(word_assocoiated_list_2)}','{str(cos_sentence_key)}','{str(sentence_number2)}','{str(document_name_1)}', '{str(document_name_2)}','{str(database_1)}','{str(database_2)}');""")
       self.conn.commit()
     
         
         
             
             
             
             
             

     
     
      
        
             

             
        
    
    
        
        






