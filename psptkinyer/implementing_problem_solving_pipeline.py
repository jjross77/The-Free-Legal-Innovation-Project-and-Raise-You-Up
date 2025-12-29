# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 00:30:05 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

from problem_solving_project import problem_solving_pipeline
import en_core_web_trf

prob=problem_solving_pipeline()
all_searches=prob.retrieve_ideas_from_database("tool")
nlp = en_core_web_trf.load()
#print([ (w.text, w.pos_) for w in doc])

for search in all_searches:
    pre_processed_text=prob.pre_process_text(search[5])
    sentenced_text=prob.divide_doc_into_sentences(pre_processed_text)
    for sentence in sentenced_text:
        pos_unmodified_sentence = nlp(sentence)
        for part_of_speech_parts in pos_unmodified_sentence:
            
            print(part_of_speech_parts.pos_)
            print(part_of_speech_parts)
            
            

        
        
        

    
    
# i can sort i can change them to be easier to interact with
#categories are methods, tools, 
#prob.pre_process_text()
#prob.divide_doc_into_sentences()

#prob.run_values_thru_pos_model()
#[argument method, taking notes method during class,]