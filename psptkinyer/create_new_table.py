# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:40:41 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

from organizing_thoughts_program import idea_organizer
import copy
org=idea_organizer()
#dicc={"":"","":"","":"","":"","":""}
# galaxies_table, ideas_table_3,problem_table
#table_name="ideas_table_3"
#dicc= {"id":"bigserial","sentence":"text","paragraph":"text","paragraph_number":"text","file_name":"text","directory":"text","pos":"text","labels":"text","updated_label":"text","updated_sentence":"text"}
#dicc={"id":"bigserial","problem_question_or_task":"text","galaxies_with_qualities":"text","tool_or_question_used_per_qualitity_connections":"text","Objectives":"text","tool_or_question_used_per_qualitity_method":'text'}

table_name="methods_table"
# at level of indivudla step each step sold seperately
dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}





#table_name="problem_table"
#dicc={"id":"bigserial","problem_question_or_task":"text","specific_problem_or_object":"text","tool_or_question_per_conn_list":"text","qualitity_list":"text" ,"Objectives":"text","time_created_conn":'text'}


org.create_new_table(table_name, dicc)

#INSERT INTO labels_for_idea_program_2 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,labels)
#            VALUES ('{str(idd)}','{sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}');""")

# we need a questions, connections table that records for each problem and a method associated with this quesiton or problem, 
# and objects or galaxies generated during this questioning

# store galaxies seperately but link by id to the orginal question that lead to creation of galaxy
#
# objects or galaxies table

# connections tables

#galaxies table
#table_name="galaxies_table"
#dicc={"id":"bigserial","sentence":"text","problem_or_idea_root":"text","qualities":"text", tool_or_question_used_per_qualitity:'text}


#table_name= "galaxies_table"
#dicc={"id":"bigserial","problem_or_idea_root":"text","qualities":"text", "tool_or_question_used_per_qualitity":'text'}

#table_name="problem_table"
#dicc={"id":"bigserial","problem_question_or_task":"text","galaxies_with_qualities":"text","tool_or_question_used_per_qualitity_connections":"text","Objectives":"text","tool_or_question_used_per_qualitity_method":'text'}
