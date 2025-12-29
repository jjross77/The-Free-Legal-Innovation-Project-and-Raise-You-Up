# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:40:28 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
from pipe_line_to_process_documents import pre_process_text
doc=pre_process_text()
def pos_creator():
    
    
    #python -m spacy download en_core_web_trf
    import spacy
    import psycopg2    
    conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
    cur = conn.cursor()
    nlp = spacy.load("en_core_web_trf")
    import en_core_web_trf
    nlp = en_core_web_trf.load()
    doc = nlp("hello world.")

    print([ (w.text, w.pos_) for w in doc])
    for part_of_speech_parts in doc :

        if part_of_speech_parts.pos_ == "NOUN" or  part_of_speech_parts.pos_ == "PROPN" or part_of_speech_parts.pos_ == "PRON":
            print('hi')
            
        if part_of_speech_parts.pos_ == "VERB":
            print('bye')
        word,starting_position,endding_position  
        verb_list_with_position
        noun_list_with_position
            
    cur.execute( f""" INSERT INTO pos_saved_words (case_name,full_case_text,links,case_date )
                VALUES ('{verb_list_with_position}','{noun_list_with_position}','{document}','');""")
