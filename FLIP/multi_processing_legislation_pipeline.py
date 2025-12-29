# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:20:35 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
if __name__ == '__main__':
    import psycopg2
    #from pipe_line_to_process_documents6 import document_vectorizer
    #import torch
    #import pickle
    import os
    os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
    import multiprocessing
    from legislation_pipeline_function import processing_pipeline_for_pos
    #from firac_pipe_line_function import processing_pipeline_for_pos
    #document_vectorizer2=document_vectorizer()

    conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
    cur = conn.cursor()





    cur.execute(f""" SELECT ID
                       FROM legislation_can
                       ORDER BY ID DESC
                       ;""")
    result_list =[]                   
    cur_result= cur.fetchall()
    #result_list= cur.fetchall()

    #cur.execute(f""" SELECT DISTINCT ID 
    #                   FROM leg_embeddings
    #                   ORDER BY ID DESC
    #                   ;""")
    
    
    #cur_result2=cur.fetchall()
    #finished_leg=[resulttt[0] for resulttt in cur_result2]
    #result_list=cur_result[0]
    #print(finished_leg)
    for result in cur_result:
        if result[0] not in result_list:
            #if result[0] not in finished_leg:
               result_list.append(result[0])

    multi_result_list=[]
    #result_list_len=len(result_list)
    temp_list=[]
    multi_result_list_piece_list=int(round(len(result_list)/2))
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
            p = multiprocessing.Process(target=processing_pipeline_for_pos, args=(i9,))
            p.start()
            #When we comment out the join method, the main process finishes before the child process.
            #p.join()       
            print("hello world")   

