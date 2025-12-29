# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:04:23 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import os
os.chdir(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\problem_solving_project')
import organizing_thoughts_program
idea_object=organizing_thoughts_program.idea_organizer()
directory="phone_notes2"

word_doc_roots=os.listdir(rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\ideas_folder\{directory}")
file_full_list=[]
for file in word_doc_roots:    
    dogd=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\ideas_folder\{directory}" + "\\" + file
    file_full_list.append(dogd)

dog=idea_object.get_word_document_into_string(file_full_list,directory)
woo=idea_object.send_idea_to_database(dog)

    
#dog=idea_object.get_text_doc_into_correct_format(file_full_list)
#print(dog)

#dog=idea_object.fix_text_doc(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Pictures\screen_shots_fixed.txt")   
#idea_object.upload_text_doc(r"woo")
#print(dog)
#idea_object.update_idea_table()



