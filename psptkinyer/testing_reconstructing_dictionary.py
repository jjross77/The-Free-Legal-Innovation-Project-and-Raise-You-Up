# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 07:49:56 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
import psycopg2
import re
conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
cur = conn.cursor()
problem_recorded=" Identify problems by what is going on in life or things I hear and then question this which leads to a problem ;"
cur.execute(f"""SELECT * FROM problem_table WHERE problem_question_or_task = '{problem_recorded}' ORDER BY ID ASC;""")
#self.problem_list_dictionary={self.problem_recorded:[time_created]}
 
problem_list_dictionary={}
problem_entries= cur.fetchall()
print(problem_entries)
for problem_entry in problem_entries:
    for i, row in enumerate(problem_entry):
        print(i)
        print(row)
        
for numm, objectt1 in enumerate(problem_entries):
        if numm==0:
            intital_time_for_object=objectt1[7]
            problem_list_dictionary={problem_recorded:[intital_time_for_object]}
            specfic_object=objectt1[2]
            tool_or_question_used=objectt1[3]
            qual_list=objectt1[4]
            timme=objectt1[6]
            timme=re.split(",",timme[1:-1])
            qual_list=re.split(",",qual_list[1:-1])
            tool_or_question_used=re.split(",",tool_or_question_used[1:-1])
            for tooll,quall,timm in zip(tool_or_question_used,qual_list,timme):
                problem_list_dictionary[specfic_object].append([tooll,quall,timm])
            continue
        
        intital_time_for_object=objectt1[7]
        specfic_object=objectt1[2]
        print('hi')
        problem_list_dictionary[specfic_object]=[intital_time_for_object]
        #specfic_object=problem_entry[2]
        tool_or_question_used=objectt1[3]
        qual_list=objectt1[4]
        timme=objectt1[6]
        timme=re.split(",",timme[1:-1])
        qual_list=re.split(",",qual_list[1:-1])
        tool_or_question_used=re.split(",",tool_or_question_used[1:-1])
        for tooll,quall,timm in zip(tool_or_question_used,qual_list,timme):
            problem_list_dictionary[specfic_object].append([tooll,quall,timm])
        continue
        
        
            
            

                
            #qualitity_list=re.split(",",qualitity_list[1:-1])
            #for each of the entry lists
            # break lists into python recongiziable lists
            #print(tool_or_question_used)
            #print(qual_list)
            #print(timme)

            #problem_list_dictionary[specfic_object].append([tool_or_question_used,qual_list,timme])
            #for i, row in enumerate(objectt1):

            

            
            
            
            
        
            

        
        #problemm_name=problem_entry[1]
        #specfic_object=problem_entry[2]
        #tool_or_question_used=problem_entry[3]
        #qual_list=problem_entry[4]
        #timme=problem_entry[6]
        
        #print(problemm_name)
        ##print(specfic_object)
        #print(tool_or_question_used)
        #print(qual_list)
        #print(timme)
        #print(intital_time_for_object)

        #self.problem_list_dictionary[objectt].append([self.recorded_question_or_tool,quality,time_qualitity_found])   

        #self.problem_list_dictionary[self.current_object_or_problem].append([self.recorded_question_or_tool,quality,time_qualitity_found])
        #self.cur.execute( f""" UPDATE problem_table 
        #                 Set tool_or_question_per_conn_list= '{str(tool_or_question_list)}', qualitity_list = '{str(qualitity_list)}',
        #                 time_created_conn = '{str(time_created_list)}'
        #                 WHERE problem_question_or_task = '{str(self.problem_recorded)}' and specific_problem_or_object = '{str(problem_or_object)}';""")
    

        
    #problem_list_dictionary.appe
        
     

        

           
    
master_tool_or_question_per_conn_list=[]
master_qualitity_str=[]
master_time_created_conn=[]
specific_problem_or_object=""
 