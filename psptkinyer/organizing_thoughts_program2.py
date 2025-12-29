# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:46:37 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

from checking_time_function import timer
class idea_organizer():
    def __init__(self):
        import psycopg2
        import en_core_web_trf
        self.nlp = en_core_web_trf.load()

        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
    def get_text_doc_into_correct_format(self,input_file):
        """ get the text document into  """
        # save file name
        import re
        from nltk.tokenize import word_tokenize
        from spellchecker import SpellChecker
        spell = SpellChecker()
        counterr=0
        fixed_word_list=[]
        final_para_list=[]
        
        with open (input_file,"r") as f:
            text=str(f.read())    
        paragraph_list=text.split("\n")
        for i, paragraph in enumerate(paragraph_list):
            if paragraph=="":
                continue
            word_list=word_tokenize(paragraph)
            fixed_word_list=[]
            for word in word_list:
                word_fixed=re.sub("[^A-Za-z\.]","", word)
                if word_fixed =="":
                    continue
                fixed_word = spell.correction(word_fixed)
                if fixed_word==None:
                    continue
                fixed_word_list.append(fixed_word)
            if fixed_word_list:
                text_from_doc=" ".join(fixed_word_list)
                final_para_list.append(text_from_doc)
        return final_para_list
    def upload_ideas_to_problem_solving_program(self,input_file):
        #if word document _translate into textdocument then use remainder of pipeline
        @timer
        def get_text_doc_into_correct_format():
            """ get the text document into  """
            # save file name
            import re
            from nltk.tokenize import word_tokenize
            from spellchecker import SpellChecker
            spell = SpellChecker()
            counterr=0
            fixed_word_list=[]
            final_para_list=[]
            
            with open (input_file,"r") as f:
                text=str(f.read())    
            paragraph_list=text.split("\n")
            for i, paragraph in enumerate(paragraph_list):
                if paragraph=="":
                    continue
                word_list=word_tokenize(paragraph)
                fixed_word_list=[]
                for word in word_list:
                    word_fixed=re.sub("[^A-Za-z\.]","", word)
                    if word_fixed =="":
                        continue
                    fixed_word = spell.correction(word_fixed)
                    if fixed_word==None:
                        continue
                    fixed_word_list.append(fixed_word)
                if fixed_word_list:
                    text_from_doc=" ".join(fixed_word_list)
                    final_para_list.append(text_from_doc)
            return final_para_list
        
        
        @timer
        def divide_paragraph_into_sentences(final_para_list : list[str]) -> list[str,str] :
            """ this will change the uploaded text into a workable format to be better pre processed after being uploaded from the database """
            from nltk.tokenize import sent_tokenize
            list_of_sentence_with_applicable_paragraph=[]
            for i,paragraph1 in enumerate(final_para_list):
                self.sentences_list=sent_tokenize(paragraph1)
                for sentence in self.sentences_list:
                    list_of_sentence_with_applicable_paragraph.append([sentence,paragraph1,i])
            return list_of_sentence_with_applicable_paragraph 
        
        @timer
        def get_pos(sentence_with_applicable_paragraph :list[str,str]) -> list[str,str,str] :
            pos_unmodified_sentence = self.nlp(sentence_with_applicable_paragraph)
            temp_sentence_pos_list=[]
            for part_of_speech_parts in pos_unmodified_sentence:
                word_with_pos=[part_of_speech_parts,part_of_speech_parts.pos_]
                temp_sentence_pos_list.append(word_with_pos)
            sentence_with_applicable_paragraph.append(temp_sentence_pos_list)
            return sentence_with_applicable_paragraph
        
        @timer   
        def count_occurances_of_each_word(sentence_with_applicable_paragraph:list[str,str,str]) -> dict[str:int] : # length starting is three
            """ implentation of a function to create keywords for ideas based upon current ideas"""
            # should just use pos to filter this
            master_word_count_dictionary={}
                #print(idea[-1])
            pos_list_for_idea=sentence_with_applicable_paragraph[3]
            for pos in pos_list_for_idea:
                word=str(pos[0])
                poss=str(pos[1])
                if poss == "NOUN" or poss == "VERB" :
                    if word in master_word_count_dictionary.keys():
                        master_word_count_dictionary[word]+=1
                    else:
                        master_word_count_dictionary[word]=1 
                continue
            return master_word_count_dictionary
        @timer   
        def create_key_word_list_for_each_idea(master_word_count_dictionary,sentence_with_applicable_paragraph:list[str,str,str]) -> list[str,str,str,str] : #dict{str:int}
            mean_value_of_word_counts= sum(master_word_count_dictionary.values())/len(master_word_count_dictionary.values())

            # may need to copy this list of lists before iterating
            paragraph=sentence_with_applicable_paragraph[1]
            temp_key_word_list=[]
            for key,value in master_word_count_dictionary.items():
                if  key in paragraph and value >= mean_value_of_word_counts:
                    temp_key_word_list.append(key)
            if temp_key_word_list:
                sentence_with_applicable_paragraph.append(temp_key_word_list)
                
            return sentence_with_applicable_paragraph
        @timer
        def pre_categorize_based_on_key_words_and_other_parameters(sentence_with_applicable_paragraph:list[str,str,str,str]) -> list[str,str,str,str,str] :
            """ this function will help us to more quickly create the necessary categories that the neural network will sort data into"""
            key_words_for_10=["connect", "use", "allow","applie","construct","identfiy","focus","simplify","craft","strateg","method" ]
            sentence2=sentence_with_applicable_paragraph[0]
            if " " not in sentence2 or len(sentence2)<35: #3 trash
                label=3
            if "objective" in sentence2:
                label =5
            if any(x in sentence2 for x in key_words_for_10): 
                label =10
            else:# 7  problems i want to solve or tasks
                label=7
            sentence_with_applicable_paragraph.append(label)
            return sentence_with_applicable_paragraph      
        @timer  
        # put in a neural network at one point to generate better categories once we have more data here and we label enough.
        def update_database(sentence_with_applicable_paragraph: list[str,str,str,str,str]):
             import re
             for i3, item in enumerate(sentence_with_applicable_paragraph):
                 item2=re.sub('\'',"",str(item))
                 item2=re.sub('\"',"",item2)
                 sentence_with_applicable_paragraph[i3]=item2
             sentence=sentence_with_applicable_paragraph[0]
             paragraph=sentence_with_applicable_paragraph[1]
             paragraph_number=sentence_with_applicable_paragraph[2]
             pos=sentence_with_applicable_paragraph[3]
             #key_word= idea[4]
             categories= sentence_with_applicable_paragraph[5]
             #input_file
             self.cur.execute(f""" INSERT INTO labels_for_idea_program_2 (sentence,paragraph,paragraph_number,file_name,pos,label)
                             VALUES ('{sentence}','{paragraph}','{paragraph_number}','{input_file}','{pos}','{categories}');""")  
             self.conn.commit()
             return "hi"
         
            
        final_para_list=get_text_doc_into_correct_format()
        # swap pos and sentence divider when i have energy
        list_of_sentence_with_applicable_paragraph=divide_paragraph_into_sentences(final_para_list)
        for sentence_with_applicable_paragraph in list_of_sentence_with_applicable_paragraph: 
            sentence_with_applicable_paragraph=get_pos(sentence_with_applicable_paragraph)
            master_word_count_dictionary=count_occurances_of_each_word(sentence_with_applicable_paragraph)
            try:
                sentence_with_applicable_paragraph=create_key_word_list_for_each_idea(master_word_count_dictionary,sentence_with_applicable_paragraph)
            except:
                continue
            sentence_with_applicable_paragraph=pre_categorize_based_on_key_words_and_other_parameters(sentence_with_applicable_paragraph)
            update_database(sentence_with_applicable_paragraph)
        self.conn.close()
        self.cur.close()
        return "uploaded"
