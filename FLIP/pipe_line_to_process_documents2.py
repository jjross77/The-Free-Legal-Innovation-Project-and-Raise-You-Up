# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:58:12 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

# list all functions in the project
# do we want to do a single dcoument at a time?
class document_vectorizer():

    

    def __init__(self):
        from transformers import  DebertaModel
        from transformers import DebertaTokenizerFast
        from pos_model_class import network
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
        self.pos_model=network(768, 586, 3).to("cuda")
        pos_state_dic = torch.load(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova\model_pos.pth")
        self.pos_model.load_state_dict(pos_state_dic)
        self.type_of_document=""



        #print(self.model.eval())
    def get_next_document(self,previous_document_id):
        """ we use this to find the next document in the case_database after the first one and so on""" 
        
                          
        self.cur.execute(f""" SELECT ID, case_name, full_case_text
                          FROM full_cases
                          WHERE ID <'{int(previous_document_id)}'
                          ORDER BY ID DESC
                          LIMIT 1;""")
        cur_result4= self.cur.fetchall()
        self.document_name=cur_result4[0][1]
        self.document_id= cur_result4[0][0]
        document_text=cur_result4[0][2]
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
            self.cur.execute( f""" SELECT ID, case_name, full_case_text
                              FROM full_cases 
                              WHERE case_name ILIKE '{self.document_name}'
                              LIMIT 1;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result2= self.cur.fetchall()

            document_text=cur_result2[0][2]
            
            
        if self.document_name == None: # first document
            self.cur.execute( f""" SELECT ID, case_name, full_case_text
                              FROM full_cases 
                              ORDER BY ID DESC 
                              LIMIT 1 ;""")
            cur_result2= self.cur.fetchall()
            self.document_name=cur_result2[0][1]
            self.document_id= cur_result2[0][0]
            document_text=cur_result2[0][2]

            

   
        return document_text
        




    def pre_process_text(self, document):
        # what do i want the text to look like before i put it into the network bascially
        import re
        import unicodedata
        """ remove extra spacing, names, tabs, and other unwanted values"""
        f= re.sub("\n"," ", document)
        f= re.sub("\t"," ", f)
        f= re.sub("\r"," ", f)
        f=re.sub(r" \s+", r" ", f)
        f = unicodedata.normalize("NFKD", f)
        return f
        #break corpus into sentences
        

    def divide_doc_into_sentences(self, document):
        """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
        from nltk.tokenize import sent_tokenize
        #from nltk.tokenize import word_tokenize
        sentences = sent_tokenize(document)
        
        return sentences
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
            
        
      
    def tokenize_document(self, sentence_3):
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
    #exclude document below a certain character count
    
    def law_data_creator(self,sentence_4):
        """ find all words that correspond to law words before we scrap them for pos and save them as labeled data for training law model"""
        # we want a neural network to run thru each word and identify whether it is law or not
        #identify law in document and then check so documents for where the law came from and the sentnece that might belong to the other document
        # to see how that decision actually impacted the arugment etc.
        # I HAVE JUST COPIED THE FUNCTION FROM BELOW HERE HERE
        for part_of_speech_parts in doc:

            if part_of_speech_parts.pos_ == "NOUN" or  part_of_speech_parts.pos_ == "PROPN": #or part_of_speech_parts.pos_ == "PRON":
                self.pos_word_list.append([part_of_speech_parts.text, "NOUN"])
                continue

                
                
            if part_of_speech_parts.pos_ == "VERB":
                self.pos_word_list.append([part_of_speech_parts.text,"VERB"])
                continue
            self.pos_word_list.append([part_of_speech_parts.text,"OTHER"])
        self.sentence_info.append(self.pos_word_list)
        self.sentence_info[5]=self.pos_word_list
        return self.sentence_info
    def law_matcher_and_uploader(self):
        """matching tokens with law tags":"""

    
    
    
    
    
    def pos_data_creator(self, sentence_4):
        """ getting pos tags from spacy model to later train a pos tagger that can be used for our deberta model"""
        
        
        #python -m spacy download en_core_web_trf
        #import spacy
        #nlp = spacy.load("en_core_web_trf")
        import en_core_web_trf
        nlp = en_core_web_trf.load()
        doc = nlp(sentence_4)
        #print([ (w.text, w.pos_) for w in doc])
        for part_of_speech_parts in doc:

            if part_of_speech_parts.pos_ == "NOUN" or  part_of_speech_parts.pos_ == "PROPN": #or part_of_speech_parts.pos_ == "PRON":
                self.pos_word_list.append([part_of_speech_parts.text, "NOUN"])
                continue

                
                
            if part_of_speech_parts.pos_ == "VERB":
                self.pos_word_list.append([part_of_speech_parts.text,"VERB"])
                continue
            self.pos_word_list.append([part_of_speech_parts.text,"OTHER"])
        self.sentence_info.append(self.pos_word_list)
        self.sentence_info[5]=self.pos_word_list
        return self.sentence_info
    
    def pos_matcher_and_uploader(self):
        """ matching tokens with pos tags to generate data for labels and pos ffn, need to match all of these and push to pos match database"""
        for i, token in enumerate(self.sentence_info[0]):
            if "Ġ" in token:
                token=token.replace("Ġ", "")
            for word in self.sentence_info[5]:
                if token== word[0]:
                    #print(f"{token},{word[0]}")
                    #embedding_made_to_list=self.sentence_info[4][i].tolist()  
                    
                    #print(embedding_made_to_list)
                    self.cur.execute( f""" INSERT INTO pos_labels (word,embedding,pos_tag)
                                VALUES ('{self.sentence_info[0][i]}','{str(self.sentence_info[4][i])}','{word[1]}');""")

                    break
        
        self.conn.commit()
        
    
        
   
        
       
        
    def remove_unwanted_sentences(self,output): # we are going to use this 
        
         #going to use mean here to create data for this
         
         # using labels from sparrow to clean data
         #running embeddings thru feed forward network to get rid of unwanted sentences
         #maybe use the cosine here
         
         """ feed in all sentences in their embedding format and output only sentences that are cleaned and want to work with"""
         
         #shit that is not useful for deberta embeddings
         
     # we only these functions once we have finished everything before this  
    
    
    def run_values_thru_law_model(self,output):
        """run all the token thru network to identify where law is in various sentences to be used for later"""
        
    def run_values_thru_pos_model(self,output): 
        """run a sentence embedding output of a transformer thru and remove all none Noun and verb embeddings from the sentence"""
        final_word_list=[]
        final_embedding_list=[]
        final_pos_list=[]
        for i, word_2 in enumerate(output):
            pos_predictions=self.pos_model.forward(word_2)
            pos_predictions=pos_predictions.tolist()
            #prediction=max(pos_predictions)
            prediction=pos_predictions.index(max(pos_predictions))
            
            #print(prediction)
            if prediction == 1 or prediction == 0:
                #final_sentence_info_list
                final_word_list.append(self.sentence_info[0][i]) # words
                #self.final_sentence_info_list.append(self.sentence_info[6][i]) # part of seech
                final_embedding_list.append(self.sentence_info[4][i]) #embeddings
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
    

    

   

    def upload_sentence_to_sentence_embedding_database(self, sentence_number):
        """EVENTUALLY WILL ADD A COLUMN FOR FIRAC, BUT THIS IS UPLOADING THE EMBEDDINGS WITH THERE POS """
        self.cur.execute( f""" INSERT INTO embedding_sentences (words,embeddings,pos,document_name,sentence_number,type_of_document)
                    VALUES ('{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.document_name)}','{sentence_number}', '{self.type_of_document}');""")
        

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
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number
                              FROM {type_of_document_database} 
                              WHERE document_name ILIKE '{case_name}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            
            cur_result2= self.cur.fetchall()
            
            return cur_result2


            
           
        
        
        if case_name_2 !="":
            
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number
                              FROM {type_of_document_database} 
                              WHERE document_name ILIKE '{case_name}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result2= self.cur.fetchall()

            document_embeddings_2=cur_result2[0][2]
            
            
            self.cur.execute( f""" SELECT embeddings, pos, words,sentence_number
                              FROM {type_of_document_database_2} 
                              WHERE document_name ILIKE '{case_name_2}'
                              ;""") #OFFSET 20 is telling Postgres to skip the first 20 records.
            cur_result3= self.cur.fetchall()

            document_embeddings_3=cur_result3[0][2]
            return cur_result2, cur_result3
            
            
            
  
    def transform_to_pos_format(self,doc):
        import json
        import re
        # will import the list of all three varabiles embedding, pos, word
        import torch
        doc_noun=[]
        doc_verb=[]
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
                    
            if noun_matrix: 
                noun_matrix=torch.tensor(noun_matrix).to('cuda')
                verb_matrix=torch.tensor(verb_matrix).to('cuda')

                doc_noun.append([sentence_noun,sentence[3],noun_matrix])
                doc_verb.append([sentence_verb,sentence[3],verb_matrix])
        doc=[doc_noun,doc_verb]


        return doc
    

    def cosine_sim_matrix_dot(self,doc1,doc2,noun_or_verb=0):# 0 for noun 1 for verb
        import torch
        import copy
        dic_comparison={}
        for  sentence_1 in doc1[noun_or_verb]:
            words_of_first_sentence=[x[2] for x in sentence_1[0]]
            for sentence_2 in doc2[noun_or_verb]:
                words_of_second_sentence=[x[2] for x in sentence_2[0]]

                sim_matrix2=torch.matmul(sentence_1[2],sentence_2[2].T).to('cuda')
                sim_matrix2=sim_matrix2.detach().cpu()
                sim_matrix44=sim_matrix2.tolist()
                print(f"matrix{sim_matrix44}")
                for  ii, column in enumerate(sim_matrix44):
                    if ii==0:
                        print('meow')
                        used_rows=column
                        continue
                    
                    for old, new in zip(used_rows,column):
                        # need to replace one new from old? to get a better distribution
                        #take lowest of old used_rows and replace with corresponding value in new only if 
                        if new>old:
                            old_index=used_rows.index(old)
                            used_rows[old_index]=new
               
                print(f"row{used_rows}")
                dic_comparison[f"{sentence_1[1]}:{sentence_2[1]}"]= [copy.deepcopy(used_rows),words_of_first_sentence,words_of_second_sentence]
                   
        return dic_comparison  
                            
                            

    def combine_verb_and_noun_cosines(noun_cosines, verb_cosines):
        document_sim_scores={}
        for key_noun, value_noun in noun_cosines.items():
            for key_verb, value_verb in verb_cosines.items():
                if key_noun == key_verb:
                    value_noun.extend(value_verb)
                    sentence_simialrity =sum(value_noun)/len(value_noun)
                    document_sim_scores[key_noun]=sentence_simialrity
                    continue
      
        return document_sim_scores
    
       
        
    def save_cosine_simialrities_in_firac_labels(self, document_sim_scores):
        # need to finish this still
        """ upload the simiarlities score of a given sentence to the database  showing which sentences are matched between the two documents, and there FIRAC placement"""
        
        self.cur.execute( f""" INSERT INTO embedding_simarlities (words,embeddings,pos,document_name,sentence_number1,sentence_number2, document1,document2)
                    VALUES ('{self.final_sentence_info_list[0]}','{str(self.final_sentence_info_list[1])}','{str(self.final_sentence_info_list[2])}','{str(self.document_name)}','{sentence_number}', '{self.type_of_document}');""")
        
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



       
    
