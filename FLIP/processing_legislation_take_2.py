# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:19:49 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

class legislation_vectorizer():
    def __init__(self):
        import psycopg2
        import torch
        import numpy as np
        #from  Pos_model_trainer import network
        super().__init__()
        self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
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
        self.model= DebertaModel.from_pretrained(r"C:\Users\\yyyyyyyyyyyyyyyyyyyy\Documents\model.pth6").to("cuda")
        self.tokenizer = DebertaTokenizerFast.from_pretrained(r"C:\Users\\yyyyyyyyyyyyyyyyyyyy\Documents\model.pth6",truncation_side="left")
        
        
    def init_pos_model(self):
        import torch
        from unwanted_sentence_model_network import network

        self.pos_model=network(768, 1000, 3).to("cuda")
        pos_state_dic = torch.load(r"C:\Users\\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\model_pos.pth")
        self.pos_model.load_state_dict(pos_state_dic)
    
        
        
    def get_next_document(self,previous_document_id):
        """ we use this to find the next document in the case_database after the first one and so on""" 
        
                          
        self.cur.execute(f""" SELECT ID, case_name, full_case_text
                          FROM legislation_can
                          WHERE ID = '{int(previous_document_id)}'  
                         ;""")
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
        f= re.sub("\n"," ", document)
        f= re.sub("\t"," ", f)
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
        import copy
        list_of_sections=[]
        index_used_list=[]
        self.sentences=[]
        find_word_pattern = re.compile(r"\w+")
        amount_of_words=re.findall(find_word_pattern,document)
        #print('hi')
        if len(document)<=400:
            return "too short"
        #print('meowww')
        
        
        #modifying_sentences=document.split('\n\d')
        paragraphs_divided_by_num=re.finditer(r"\n\d+",document)
        paragraphs_divided_by_num_for_len=re.findall(r"\n\d+",document)

        #list_of_paras_for_len=[para for para in paragraphs_divided_by_num]
       
        
       
        # for those without line breaks and tned to get clumped 
        
        if len(paragraphs_divided_by_num_for_len)<=5:
            
            for paraa in paragraphs_divided_by_num_for_len:
                modifying_sentences = sent_tokenize(document)
                
                for i7, sentence_15 in enumerate(modifying_sentences):
                    if len(modifying_sentences)==1:
                        self.sentences.append(sentence_15)
                        break

                    words_in_current_sentence=find_word_pattern.findall(sentence_15)
                    
                    if len(words_in_current_sentence)<20:
                        
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
                           
                            self.sentences[-1]=self.sentences[-1]+ " "+sentence_15 
                            continue

                            
                            
                            
                    if i7 in index_used_list:
                        continue 
                    #print(sentence_15)
                    self.sentences.append(sentence_15)
                          
            return self.sentences
 
        stored_para_index=""
        final_list_of_sections=[]
        previous_index_appended_to=0
        

  
        for i, section in zip(range(len(paragraphs_divided_by_num_for_len)),paragraphs_divided_by_num):
 
            if i==0:
                
                start_of_match=section.span(0)[0]
                temp_paragraph_to_append=document[:start_of_match]
                final_list_of_sections.append(temp_paragraph_to_append)
                previous_index_appended_to=len(final_list_of_sections)-1
                stored_para_index=start_of_match
                continue
            
            #print('seee')
            
            
            start_of_match=section.span(0)[0]
            
            temp_paragraph_to_append=document[stored_para_index:start_of_match]
            stored_para_index= start_of_match
            
            
            
            #print(stored_para_index)
            
            
            amount_of_words=re.findall(find_word_pattern,temp_paragraph_to_append)

              
            if len(amount_of_words)<40:
                  amount_of_words2=re.findall(find_word_pattern,final_list_of_sections[previous_index_appended_to])
                  #print(amount_of_words2)
                  if len(amount_of_words2)>250:
                      final_list_of_sections.append(temp_paragraph_to_append)
                      previous_index_appended_to=len(final_list_of_sections)-1
                      continue
                  #print('hi')

                  final_list_of_sections[previous_index_appended_to]=final_list_of_sections[previous_index_appended_to]+ " " + temp_paragraph_to_append
                  continue
              
              
              
            final_list_of_sections.append(temp_paragraph_to_append)
            
            previous_index_appended_to=len(final_list_of_sections)-1
 
        return final_list_of_sections