# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:43:21 2023

@author: doggo777
"""
from pipe_line_to_process_documents6 import document_FIRAC_labeler
import random
import time
docf=document_FIRAC_labeler()
#counterr=0
def get_matching_cases(result_list,whole_result_list):
        #n= int(round(len(result_list)/25)) # we are only comparing it to  a few cases now if we want to do them all remove this   
        result_list2=whole_result_list
        for result in result_list:
                print('woo')
                t1=time.time()

                case, case_type= docf.upload_embeddings_from_case_database_FIRAC_PIPELINE(result)
                t2=time.time()
                print(t2-t1)
                #if len(case)>10:
                #    case=case[:20]
                


                if len(case)<5:
                    print('wee')
                
                print('meowwww')
                t1=time.time()

                doc_1=docf.transform_to_pos_format(case,case_type)
                t2=time.time()
                print(t2-t1)
                print(result)
                print('hehehe')
                for result2 in result_list2:
                        print(result2)
                        print('nooo')
                        #if result==result2:
                        #    continue
                        print('hiiiiiiii')
                        case2,case_type2= docf.upload_embeddings_from_case_database_FIRAC_PIPELINE(result2)    
                        if len(case2)<5:
                            print('yo')
                            continue
                        if len(case2)>10:
                            case2=case2[:20]
                            
                            
                        t1=time.time()

                        doc_2=docf.transform_to_pos_format(case2,case_type2)  
                        t2=time.time()
                        print(t2-t1)
                        print('doc 2 in')

                        verb_dog=docf.cosine_sim_matrix_dot(doc_2,doc_1,noun_or_verb=1)
                        noun_dog=docf.cosine_sim_matrix_dot(doc_2,doc_1,noun_or_verb=0)
                        ultimate_dog=docf.combine_verb_and_noun_cosines(noun_dog,verb_dog)
                        t1=time.time()
                        highest_matches=docf.find_best_matching_doc_sentences_FIRAC_PIPELINE(ultimate_dog)
                        t2=time.time()
                        print(t2-t1)
                        return highest_matches,ultimate_dog
                        docf.save_cosine_simialrities_FIRAC_PIPELINE(highest_matches)
                        
counterr=0
import psycopg2
conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
cur = conn.cursor()


cur.execute(f""" SELECT ID
                   FROM embedding_sentences
                   ORDER BY ID DESC
                   LIMIT 1000000
                   ;""")
result_list =[]                   
cur_result= cur.fetchall()


#result_list=cur_result[0]
for result in cur_result:
    if result[0] not in result_list:
        result_list.append(result[0])

multi_result_list=[]
#result_list_len=len(result_list)
print('hi')
temp_list=[]
dogg,dogg2=get_matching_cases(result_list,result_list)
                    

