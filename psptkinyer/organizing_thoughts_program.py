# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:26:47 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
# steps
# program goal is to 
#step 0 need to upload everything to python
#step 1 need to create table in database
# how to create tables in python
#step 2 need to make table accessible to program to add to it and have a input option
# step 3 need to find a smart way to input everything into the table such that they have categories and are searchable and accessible in a easy way
# maybe some sort of model is key, this is where the problem sovling strategy should probably come in

from checking_time_function import timer
class idea_organizer():
    def __init__(self):
        import psycopg2

        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
    def create_idea_table(self):
        """create an idea table """
        table_creation = self.cur.execute("""
        CREATE TABLE Ideas2(id bigserial,
                           date date,
                           idea_number_group numeric,
                           idea_category text,
                           key_terms text,  
                           paragraph text,
                           paragraph_number text,
                           file_name text,
                           directory text,
                           sentences text,
                           pos text);""")
        self.conn.commit()
        self.conn.close()
        self.cur.close()
    def update_idea_table(self,column_name):
        self.cur.execute(f"""
                         ALTER TABLE Ideas2 
                         ADD {column_name} text;
                         """)
        self.conn.commit()
        self.conn.close()
        self.cur.close()
        
        
    
    def upload_photos_into_list(self):
        """ bring a photo from your harddrive into python to then work with it"""
        import os
        list_of_photo_link_names=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\ideas_folder\screenshots")
        return list_of_photo_link_names
    def convert_photo_text(self, photo_list):
        """convert the photo into a string"""
        import pytesseract
        from PIL import Image
        image_file_list = []
        text_file =  r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\ideas_folder\screenshot_doc\screenshot_text.txt"
        with open(text_file, "a") as output_file:
            for image_file in photo_list:
                image_file_with_root = r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\ideas_folder\screenshots" + "\\"+ image_file
                text = str(((pytesseract.image_to_string(Image.open(image_file_with_root)))))
                text = text.replace("-\n", "")
 
                output_file.write(text)
    def get_text_doc_into_correct_format(self, directory):
        import re
        from nltk.tokenize import word_tokenize

        from spellchecker import SpellChecker
        spell = SpellChecker()
        output_file= r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Pictures\screen_shots_fixed.txt'
        
        fixed_word_list=[]
        final_para_list=[]
        for text_file in directory:
            with open (text_file,"r") as f:
                text=str(f.read())
                text_list_by_newline=text.split("\n")
                counterr=0
                for i1,textt in enumerate(text_list_by_newline):
                    if i1 == 0:
                        temp_para= textt
                        continue
                    
                    if textt=="":
                        counterr+=1
                    temp_para+= " "+ textt 
                    if counterr==2:
                        final_para_list.append(temp_para)
                        #everything before this two split goes together into a single part of a new list
                        counterr=0
                        temp_para=""

                for i, text_seg in enumerate(final_para_list):
                    word_list=word_tokenize(text_seg)
                    fixed_word_list=[]
                    for word in word_list:
                        
                        word_fixed=re.sub("[^a-z\.]","", word)
                        #print(word_fixed)
                        if word_fixed =="":
                            continue
                        fixed_word = spell.correction(word_fixed)
                        if fixed_word==None:
                            continue
                        
                        fixed_word_list.append(fixed_word)
                    #print(fixed_word_list)
                    if fixed_word_list:
                        #print(fixed_word_list)
                        text_from_doc=" ".join(fixed_word_list)
                        fixed_text_seg= text_from_doc 
                        text_list_by_newline[i]=fixed_text_seg

                # write to text file  
                with open(output_file, "w") as f:
                    for text_line in text_list_by_newline:
                        f.write(text_line)
                        f.write("\n")
                return text_list_by_newline
    def get_word_document_into_string(self, directory_list,directory_name):
        # this is for all word documents and use the implementing_thought_program file
        import docx
        import re
        all_text=[]
        for word_file in directory_list:
            print(word_file)
            doc = docx.Document(word_file)
            fullText = []
            for i, para in enumerate(doc.paragraphs):
                if para.text=="":
                    continue
                paragraph=re.sub('\'',"",para.text)
                paragraph=re.sub('\"',"",paragraph)
                fullText.append([paragraph,word_file,directory_name,i])# [paragraph text, file name, directory name, paragraph number]
            all_text.append(fullText)    
        return all_text
    
    def send_idea_to_database(self,all_text):
        """send the idea to the database with the information to be stored"""
        # this id files from a word document
        for file in all_text:
            for paragraph_list in file:
                text=paragraph_list[0]
                file= paragraph_list[1]
                directory= paragraph_list[2]
                paragraph_number = paragraph_list[3]
                print(text)
                self.cur.execute( f""" INSERT INTO Ideas2 (paragraph,paragraph_number,file_name,directory)
                            VALUES ('{text}','{str(paragraph_number)}','{str(file)}', '{str(directory)}' );""")        
        self.conn.commit()
        self.conn.close()
        self.cur.close()
    def decide_file_type(self, directory):
        """ implement the functions set out above"""
        import get_word_document_into_string
        import get_text_doc_into_correct_format
        import fix_text_doc
        for file_name in directory:
            if "docx" in file_name:
                get_word_document_into_string(file_name)
                continue

            if "txt" in file_name:
                text_document=get_text_doc_into_correct_format(file_name)
                fix_text_doc(text_document)
                
                
                
    def fix_text_doc(self, text_name):
        #remove duplicates
        final_list=[]
        output_file= r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Pictures\screen_shots_fixed2.txt'
        with open(text_name,"r") as f:
            text=f.read()
            split_text=text.split("\n")
            print(split_text)
            temp_list=[]
            for i, textt in enumerate(split_text):
                if i ==0:
                    almost_final_str=""
                if textt in temp_list:
                    continue
                temp_list.append(textt)
                if len(textt) >=9:
                    almost_final_str+= " " + textt
                    continue
                
                final_list.append(almost_final_str)
                almost_final_str=""
                
        with open(output_file, "w") as f:
            for text_line in final_list:
                if len(text_line)<31:
                    continue
                
                
                f.write(text_line)
                f.write("\n")
        return final_list

 
        #return '\n'.join(fullText)
    def upload_text_doc(self,file):
        """ goal would be to once a file is sent from phone upload to database"""
        # send to gmail
        # take text and use upload_text_doc for getting it into database
        import re
        from spellchecker import SpellChecker
        from nltk.tokenize import word_tokenize
        spell = SpellChecker()
        final_split_text=[]
        
        #input_file=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Pictures\screen_shots_fixed2.txt"
        
        with open(file,"r") as f:
            text=f.read()
            split_text=text.split("\n")
            
            for i, text_seg in enumerate(split_text):
                word_list=word_tokenize(text_seg)
                fixed_word_list=[]
                for word in word_list:
                    
                    
                    fixed_word = spell.correction(word)
                    if fixed_word==None:
                        continue
                    
                    fixed_word_list.append(fixed_word)
                #print(fixed_word_list)
                if fixed_word_list:
                    #print(fixed_word_list)
                    text_from_doc=" ".join(fixed_word_list)
                    fixed_text_seg= text_from_doc 
                    final_split_text.append(fixed_text_seg)
   
            for i, paragraph in enumerate(final_split_text):
                paragraph=re.sub('\'',"",paragraph)
                paragraph=re.sub('\"',"",paragraph)
                if paragraph=="":
                    continue

                self.cur.execute( f""" INSERT INTO Ideas2(paragraph,paragraph_number,directory,file_name)
                                 VALUES ('{paragraph}','{str(i)}','{"phone_notes"}', '{str(file)}' );""")
            self.conn.commit()
            #self.conn.close()
            self.cur.close()
    def retrieve_ideas_from_database(self, search):
            """ input prompt to receive values from database"""
            self.cur.execute(f"""SELECT * FROM Ideas2  WHERE paragraph ilike '%{search}%';""")
            cur_result4= self.cur.fetchall()
            return cur_result4
    @timer   
    def upload_all_data_from_database_into_python(self):
            """ upload all database from sql database into python """
            self.cur.execute(f"""SELECT * FROM Ideas2   ;""")
            new_all_idea_in_database_list_format=[]
            all_idea_in_database_list_format= self.cur.fetchall()
            for idea in all_idea_in_database_list_format: 
                new_all_idea_in_database_list_format.append(list(idea))
                continue
            return new_all_idea_in_database_list_format
    @timer   
    def fix_grammar_in_whole_database(self,all_idea_in_database_list_format):
        """run over all grammar in database to fix it automatically every week"""
        from spellchecker import SpellChecker
        from nltk.tokenize import word_tokenize
        spell = SpellChecker()
        fixed_word_list=[]
        for i,idea in enumerate(all_idea_in_database_list_format):
            fixed_word_list=[]
            word_list=word_tokenize(idea[5])
            for word in word_list:
                fixed_word = spell.correction(word)
                if fixed_word==None:
                    continue
                fixed_word_list.append(fixed_word)
            if fixed_word_list:
                text_from_doc=" ".join(fixed_word_list)
                all_idea_in_database_list_format[i][5]= text_from_doc 

        return all_idea_in_database_list_format
    @timer   
    def divide_into_sentences(self,all_idea_in_database_list_format):
        """ this will change the uploaded text into a workable format to be better pre processed after being uploaded from the database """
        from nltk.tokenize import sent_tokenize
        for i,idea in enumerate(all_idea_in_database_list_format):
            sentences=sent_tokenize(idea[5])
            all_idea_in_database_list_format[i].append(sentences)
            
        return all_idea_in_database_list_format
    @timer   
    def get_pos(self,all_idea_in_database_list_format):
        import en_core_web_trf
        nlp = en_core_web_trf.load()
        for i,idea in enumerate(all_idea_in_database_list_format):
            pos_unmodified_sentence = nlp(idea[5])
            temp_sentence_pos_list=[]
            
            for part_of_speech_parts in pos_unmodified_sentence:
                word_with_pos=[part_of_speech_parts,part_of_speech_parts.pos_]
                temp_sentence_pos_list.append(word_with_pos)

                #print(part_of_speech_parts.pos_)
                #print(part_of_speech_parts)

            all_idea_in_database_list_format[i].append(temp_sentence_pos_list)
       
        return all_idea_in_database_list_format
    @timer   
    def count_occurances_of_each_word(self, all_idea_in_database_list_format):
        """ implentation of a function to create keywords for ideas based upon current ideas"""
        # should just use pos to filter this
        master_word_dictionary={}

        for idea in all_idea_in_database_list_format:
            #print(idea[-1])
            pos_list_for_idea=idea[-1]
            
            for pos in pos_list_for_idea:
                word=str(pos[0])
                poss=str(pos[1])
                if poss == "NOUN" or poss == "VERB" :
                    
                    if word in master_word_dictionary.keys():
                        master_word_dictionary[word]+=1
                        
                    else:
                        master_word_dictionary[word]=1 
                continue
        return master_word_dictionary
    @timer   
    def create_key_word_list_for_each_idea(self,master_word_dictionary, all_idea_in_database_list_format):
        mean_value_of_word_counts= sum(master_word_dictionary.values())/len(master_word_dictionary.values())
        for i, idea in enumerate(all_idea_in_database_list_format):
            paragraph=idea[5]
            temp_key_list=[]
            for key,value in master_word_dictionary.items():
                if  key in paragraph and value >= mean_value_of_word_counts:
                    temp_key_list.append(key)
            if temp_key_list:
                all_idea_in_database_list_format[i].append(temp_key_list)
                
        return all_idea_in_database_list_format
    
    @timer   
    def update_database(self,fixed_grammar_sentences_pos):
        import re
        for idea in fixed_grammar_sentences_pos:
            idea[5]=re.sub('\'',"",str(idea[5]))
            idea[5]=re.sub('\"',"",idea[5])
            idea[9]=re.sub('\'',"",str(idea[9]))
            idea[9]=re.sub('\"',"",idea[9])
            idea[10]=re.sub('\'',"",str(idea[10]))
            idea[10]=re.sub('\"',"",idea[10])
            if len(idea)>=12:
                idea[11]=re.sub('\'',"",str(idea[11]))
                idea[11]=re.sub('\"',"",idea[11])
                print(idea)
              
                self.cur.execute(f""" INSERT INTO Ideas2 (id,paragraph_number,file_name,directory,paragraph,sentences,pos,key_terms)
                            VALUES ('{idea[0]}','{idea[6]}','{idea[7]}','{idea[8]}','{idea[5]}','{str(idea[9])}','{str(idea[10])}','{str(idea[11])}');""")
                continue
            
            self.cur.execute(f""" INSERT INTO Ideas2 (id,paragraph_number,file_name,directory,paragraph,sentences,pos)
                        VALUES ('{idea[0]}','{idea[6]}','{idea[7]}','{idea[8]}','{idea[5]}','{str(idea[9])}','{str(idea[10])}');""")
        self.conn.commit()
        self.conn.close()
        self.cur.close()
    def update_database_final(self):
        """ use the combination of methods listed below to update the database"""
        
        
        #upload_all_data_from_database_into_python
        #divide_into_sentences
        #get_pos
        #count_occurances_of_each_word
        #create_key_word_list_for_each_idea
        #update_database
    def merge_two_table(self,table1,table2):
        """upload two tables from the database and merge rows on id """
        self.cur.execute(f"""
        SELECT * 
        FROM ideas2 JOIN labels_for_idea_program 
        ON ideas2.id = labels_for_idea_program.id ;""")
        merged_table=self.cur.fetchall()
        return merged_table
    def identify_patterns(self,merged_table: list[str]) :
        """ look at values in various rows to digangosis a pattern for pre_categorixzer """
        # look at key words save in key word massive list erase duplicates
        # look at length of each sentence and keep a tally for each category
        # look at order of words maybe
        #note the directory and files that were accessed for each and then use this information to build logic 
        # note pos of each noticing maybe frequency of different types of pos used
        key_word_dic={i:[]for i in range(13)}
        len_dic={i:[]for i in range(13)}
        word_dictonary={}
        avg_len_dic={}
        final_word_dictionary={i:[]for i in range(13)}
        
        for row in merged_table:
             paeagraph=row[5]
             idd=row[0]
             try:
                 labels=int(row[11])
             except:
                 continue
             key_words=str(row[4][1:-1])
             lenn=len(paeagraph)
             len_dic[labels].append(lenn)
             key_word_dic[labels].append(key_words)

        for key1, value1 in key_word_dic.items():
            joined_key_words=" ".join(value1)
            key_word_list=joined_key_words.split(",")
            temp_word_list=[]
            for word in key_word_list:
                if word in temp_word_list:
                    continue     
                temp_word_list.append(word)
            word_dictonary[key1]=temp_word_list
 
        for idd, word_list in word_dictonary.items():
            for word in word_list:
                if word in word_dictonary[7]:
                    print(word)
                    continue
                final_word_dictionary[idd].append(word)
        #return len_dic
                
        for key3,value3 in len_dic.items():
            if value3 ==[]:
                continue
            avg_len=sum(value3)/len(value3)
            avg_len_dic[key3]=avg_len
            
        return avg_len_dic, word_dictonary,final_word_dictionary
            

        
        
    def pre_categorize_based_on_key_words_and_other_parameters(self,data: list[int, str])->dict[int:int]:
        """ this function will help us to more quickly create the necessary categories that the neural network will sort data into"""
        #step1 break into categories
        labels_dic={i:[]for i in range(1,13)}
        
        key_words_for_10=["connect", "use", "allow","applie","construct","identfiy","focus","simplify","craft","strateg","method" ]
        for row in data:
            idd=row[0]
            paragraph=row[5]
            paragraph_number=row[6]
            file_name=row[7]
            directory=row[8]
            sentences=row[9][1:-1]# remove the brackets
            sentences=sentences.split(",")        
            pos=row[10]
            
            
            for sentence in sentences:
                #3 trash
                if " " not in sentence or len(sentence)<35:
                    labels_dic[3].append(idd)
                    label=3
                    self.cur.execute( f""" INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,label)
                                VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")
                    
                    continue
                    
                
                idd=row[0]
                paragraph=row[5]
                
                #1 & 12 questions for method, questions for step process 1 and 12
                #if "" in sentence: # need to fix this
                #    label= 1
                #    labels_dic[1].append(idd)
                #    self.cur.execute( f""" INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,label)
                #                VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")
                    
                #    continue
          
                
                # 5 objectives to optimize towards
                if "objective" in sentence:
                    label =5
                    labels_dic[5].append(idd)
                    self.cur.execute( f""" INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,label)
                                VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")
                    
                    continue

                    
                
                # 6 methods created
                # methods are the same as tools 
                # will need to mnaullay outline methods later
                #if "method" in sentence:
                #    label =6
                #    labels_dic[6].append(idd)
                #    self.cur.execute( f""" INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,label)
                #                VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")
                    
                #    continue

        
                # 7 submethods for connections
                # going to have to sort further performing operaitons for these
                
                
                
                #10 tools
                
                if any(x in sentence for x in key_words_for_10): 
                    labels_dic[10].append(idd)
                    label =10
                    self.cur.execute( f""" INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,label)
                               VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")
                   
                    continue
                # 7  problems i want to solve or tasks
                else:
                    label=7

                    labels_dic[7].append(idd)
                    self.cur.execute( f""" INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,label)
                                VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")
                    
               
       
                
            
            
            

        #store data with labels
        # create table
        # store in table
        self.conn.commit()
        self.conn.close()
        self.cur.close()
        #look at results from this and then can fine tune  
        #if no spaces or extremely short throw in garbage
        # catch all category those above a certain length is 7 a prbolem or method i want to solve
        # tool identifies tool paragraphs
        #how might be a key word
        # unique words in each of the categories if there is a conflict , unique lengths settle on a median, and other characersitics and determine all these values for each category
        #using the characeristics attrbitues we have which are things like file and directory and 
        #method for 10,connect, use,allow,applied,construct,identfiying,focusing,simplify
        #
        #10 example of 10  questions to make connections  so my brain can process  allows me to distinguish it from its surroundings and these attributes are various adjectives .'
        
        
       
        # compare all key word lists if a word appears in 7 then we will drop it from the other category
        # look at lengths 
            #if :
                #Label=x
                #then this category
                #store in database2
            
            
        #find all ones that have method and problem solving in it
        #tool
        #other key words too
        # filtering phone notes for mostly examples of problems
        
        # then sort
        
    def create_new_table(self, table_name, dictionary_of_columns_and_datatypes):
        """ create a new table in the can_law_accessbiel database"""
        table_columns_formated=""

        for i, (key,value) in enumerate(dictionary_of_columns_and_datatypes.items()):
            if i == len(dictionary_of_columns_and_datatypes.keys())-1:
                # final input in list
                table_columns_formated+=f"{key} {value}"
                continue 
            table_columns_formated+=f"{key} {value},"
        table_creation = self.cur.execute(f"""
        CREATE TABLE {table_name}({table_columns_formated});""")
        self.conn.commit()
        self.conn.close()
        self.cur.close()
    def pre_sort_the_data(self,):
        """ actually store and sort data by hand if categories misplaced"""
        # do this at the interface step
        # check only ones that are part of problem solving method
        # find pattenrs based upon information we have
        #for ideas in uploaded_ideas:
            # going to use the keywords
            #going to use directory and file name in combiation
            # going to use
            # use all qualtites to sort find patterns
            # pos too use this
            # use length of each idea
            # order of words
        # store all this info into a table with the paragraphs and assoicated labels
        # need to create table 
    def generate_labels(self):
        """ generate labels and upload labels to the database"""
        import json
        #self.cur.execute(f"""SELECT id FROM labels_for_idea_program  WHERE id=(SELECT max(id) FROM labels_for_idea_program);""")
        self.cur.execute(f"""SELECT id FROM labels_for_idea_program;""")
        #max_id= self.cur.fetchall()
        id_list=[]
        id_list_temp= self.cur.fetchall()
        for idd in id_list_temp:
            idd2=int(idd[0])
            id_list.append(idd2)
            
        print(id_list)
        self.cur.execute(f"""SELECT * FROM ideas2  WHERE paragraph ILIKE '{'%prob%'}';""")
        ideas= self.cur.fetchall()
        try:
            for i, row in enumerate(ideas):
                if row[0] in id_list:
                    continue
               
     
                if i % 2 == 0:
                    print("""questions to draft a method = 1 
                  galaxies of existing ideas = 2
                  thing not useful to problem solving = 3
                  questions to form connections = 4
                  objectives to optimize towards = 5
                  methods created = 6
                  problems i want to solve or tasks=7
                  submethods for connections = 8
                  submethods for method creation step = 9
                  Tools, abstraction useful for making ideas easier for brain = 10 
                  ideas on method to construct tasks for problem solving and process = 11
                  web results = 12 """)
                sentences=row[9][1:-1]# remove the brackets
                sentences=sentences.split(",")                 #break on commas

                paragraph=row[5]
                file_name=row[7]
                directory=row[8]
                idd=row[0]
                print(paragraph)
                for sentence in sentences:
                    print(sentence)
                    label=input()
                    self.cur.execute( f""" INSERT INTO labels_for_idea_program (paragraph, id, labels)
                                VALUES ('{sentence}','{str(idd)}','{str(label)}');""")
       
        except:
            self.conn.commit()
            self.conn.close()
            self.cur.close()
            
        # you need atleast one or two examples in each category before uou can apply some sort of presorting
        # and the pre sorting would look at the attribtues of each of these ones that you've categorized
        # and maybe we will change type of categories aftrer
        # 1 find starting point
    def modify_labels_1(self,data_with_labels: list[str,int]) -> list[str,int]:
        """ take the intital categories and subdivide them into more categories and transform into question."""
        # step 1 take data and perform operation to divide into new categories or labels
        # step 2 reupload data into database with updated labels
        
    #def modify_labels_2:
        
  
        
    def train_neural_network(self,dog,cat: str,str) -> list[str,str]:
        """ upload data, train model off data,store model"""
        #step 1 upload labels and values
        #step 2 define and training model
        #step 3 store model

        
    def N_N_to_categorize_ideas(self): # number of categories base upon different things we come up to use in the interface
        """ categroize all the ideas into the different things we will use in the problem solving method"""
        # goal is to turn all the ideas info into the different catrgories we will use in the problme solving process
        # or text from the internet but otherwise if not useful put in garbage category
        #questions for step by step process
        #galaxies of existing ideas
        # question to make connections
        #objectives to optimize
        # methods laid out step by step
        # list of problems that I want to create
        # submethods to make connections, like history
        # tools like abstraction
        #problems or processes I want to solve
        # not useful to problem solving process answers
        # train my brain to only ask these types of questions that can improve my life for takss i might want to do or tasks i do do
    def interface_to_interact_with_data(self, data: list[str,int]):
        """ provide a interface with the different lists from idea database split into relevent categories """
        # going to use tkinyer and hten link up the database to that
        
        
        #step1 create html  which database can connect to
        #step2 create html  which is a connection page
        #step3 create html which is a method creation page
        #step4 save all to method table and connections table
        

        
    def outline_problem(self):
        """ get problems from database of things or methods that I want to develop or things i observe and do in my life i want to work on and"""
    
        
    def make_connections(self):
        """ ask and answer questions and implement sub method, grab info from wifi and process it, look at existing galaxies"""
        
    def webscraper_for_galaxies_and_connection_section(self):
        """ this will retrieve like top google results and academic articles on various subjects"""
        # use the webscraper from canlii and what not
        # use selium to google search and then store every webpage and search those too, search is the question
        # then rpocess this web data to form galaxies and connections 
        
        
    def develop_method(self):
        """ use connections to problem to develop a step by step process which works to optimize optimal outcomes for a given problem""" 
        
    def store_processes(self):
        """ store all this information in various tables like a method table a galaxies table and a problem table"""
    
    def develop_web_interface(self):
        """ implement this interface with web book i am learning to use"""
        
        

    
         
            
       
        
    
    
    
   
     
   
        
        
        
        
        #generate labels using qualities of words like quantity and devleop a better algorhim for sorting in this way
        # grab sorting by word program looking at each word in sentence and then locating most common words in overall database and having key words
        # also could use a 
        # create simialrity metric by simialr words
        #then divide into clusters by smimlairty like 30 categories
        #train neural network using deberta embeddings to categroize them.
        # key words will be our categories
        
   
                
            



    