# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:47:37 2023

@author: doggo777
"""

from pipe_line_to_process_documents6 import document_FIRAC_labeler
import random
docf=document_FIRAC_labeler()
from getting_matching_onca_cases_function import get_matching_cases
import multiprocessing
counterr=0
import psycopg2
conn = psycopg2.connect(dbname="Can_Law_Accessible", user="postgres", password="MeganisGreat")
cur = conn.cursor()


cur.execute(f""" SELECT ID
                   FROM embedding_sentences_firac2
                   ORDER BY ID DESC
                   ;""")
result_list =[]                   
cur_result= cur.fetchall()


#result_list=cur_result[0]
for result in cur_result:
    if result[0] not in result_list:
        result_list.append(result[0])

multi_result_list=[]
#result_list_len=len(result_list)
temp_list=[]
multi_result_list_piece_list=int(round(len(result_list)/7))
print(multi_result_list_piece_list)
print(len(result_list))
for i, num in  enumerate(result_list):
    if len(temp_list) >multi_result_list_piece_list or i ==len(result_list)-1:
        temp_list.append(num)
        multi_result_list.append(temp_list)
        temp_list=[]
        continue
    temp_list.append(num)
print('hi')    
for i9 in multi_result_list:
    if __name__ == '__main__':
        p = multiprocessing.Process(target=get_matching_cases, args=(i9,result_list))
        p.start()
        #When we comment out the join method, the main process finishes before the child process.
        #p.join()       
        print("hello world")     
 
