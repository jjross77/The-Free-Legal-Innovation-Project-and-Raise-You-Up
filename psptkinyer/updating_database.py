# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:06:00 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from organizing_thoughts_program import idea_organizer

import copy
org=idea_organizer()
data=org.upload_all_data_from_database_into_python()
print('hi')
updated_data= org.fix_grammar_in_whole_database(data)
print('hi')

sentences=org.divide_into_sentences(data)
print('hi')

pos=org.get_pos(sentences)
print('hi')

#print(pos)
key_words=org.count_occurances_of_each_word(pos)
print('hi')

final_list=org.create_key_word_list_for_each_idea(key_words,pos)
print('hi')
#for item in final_list:
#    for i, it in enumerate(item):
#        print(i)
#        print(it)

#print(final_list[2][12])
org.update_database(final_list)
print('hi')
