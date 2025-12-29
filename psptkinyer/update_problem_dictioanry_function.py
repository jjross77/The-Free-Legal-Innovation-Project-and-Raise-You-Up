# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:38:59 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

#do this either by event or timer once i can get a multiprocessing script running
# this is once we have connected some thing directly to the problem
# there must be atleast a = sign or a ;
# we would make whatever we have viewable in the current connected objects window
# we should also make a quick mouse scroll option to get questions or whatever
# may be like shift key and number of question to pick a specific one  
# update the dictionary
import re
import time
import copy
#if multiple qualtities then add mutliple times to the dictionary window:  
content=self.text_box0.get('1.0', 'end')
self.listbox1.delete(0, tk.END)
time_qualitity_found =time.time()
#self.problem_list_dictionary={self.problem_recorded:[time_created]}
self.previous_problem_list_dictionary=copy.deepcopy(self.problem_list_dictionary)
if ";" in content:
    objectt_and_qualities=re.split(';',content)
    objectt=objectt_and_qualities[0]
    self.problem_list_dictionary[objectt]=[time_qualitity_found]
    self.current_object_or_problem=objectt
    qualities_list=re.split('=',objectt_and_qualities[1])
    for quality in qualities_list:
        self.problem_list_dictionary[self.problem_recorded]
        self.problem_list_dictionary[objectt].append([self.recorded_question_or_tool,quality,time_qualitity_found])   
    #self.problem_list_dictionary={self.problem_recorded:[time_created]}    
else:
    qualities=re.split("=",content)
    for quality in qualities:
        self.problem_list_dictionary[self.current_object_or_problem].append([self.recorded_question_or_tool,quality,time_qualitity_found])

for problem_or_object, list_of_qualities in self.problem_list_dictionary.items():
    tool_or_question_list=[]
    qualitity_list=[]
    time_created_list=[]
    
    for i5,qualtity in enumerate(list_of_qualities):
        if i5==0:
            time_object_or_problem_created= qualtity
            continue
        tool_or_question=qualtity[0]
        qualitityy=qualtity[1]
        time_created1=qualtity[2]
        
        tool_or_question_list.append(tool_or_question)
        qualitity_list.append(qualitityy)
        time_created_list.append(time_created1)
        # remove commas and unwanted stuff from these
        #dicc={"id":"bigserial","problem_question_or_task":"text","specific_problem_or_object":"text","tool_or_question_per_conn_list":"text","qualitity_list":"text" ,"Objectives":"text","time_created_conn":'text'}
    tool_or_question_list=re.sub('\'',"",str(tool_or_question_list))
    tool_or_question_list=re.sub('\"',"",tool_or_question_list)
    tool_or_question_list=re.sub('\n',"",tool_or_question_list)
    qualitity_list=re.sub('\'',"",str(qualitity_list))
    qualitity_list=re.sub('\"',"",qualitity_list)
    qualitity_list=re.sub('\n',"",qualitity_list)
    time_created_list=re.sub('\'',"",str(time_created_list))
    time_created_list=re.sub('\"',"",time_created_list)
    time_created_list=re.sub('\n',"",time_created_list)
    if self.previous_problem_list_dictionary.get(problem_or_object) and len(self.previous_problem_list_dictionary[self.problem_recorded])>1:
        #print("7")
        self.cur.execute( f""" UPDATE problem_table 
                         Set tool_or_question_per_conn_list= '{str(tool_or_question_list)}', qualitity_list = '{str(qualitity_list)}',
                         time_created_conn = '{str(time_created_list)}'
                         WHERE problem_question_or_task = '{str(self.problem_recorded)}' and specific_problem_or_object = '{str(problem_or_object)}';""")
    else:
        #print("5")
        self.cur.execute( f""" INSERT INTO problem_table (problem_question_or_task,specific_problem_or_object,tool_or_question_per_conn_list,qualitity_list,time_created_conn,initial_creation)
                 VALUES ('{str(self.problem_recorded)}','{str(problem_or_object)}','{str(tool_or_question_list)}','{str(qualitity_list)}','{str(time_created_list)}','{str(self.problem_list_dictionary[self.current_object_or_problem][0])}');""")
                 
        self.cur.execute( f""" INSERT INTO galaxies_table (problem_or_idea_root,qualities,tool_or_question_used_per_qualitity,finish_time)
                 VALUES ('{problem_or_object}','{qualitity_list}','{tool_or_question_list}','{time_created_list}');""")
self.conn.commit()   
self.cur.execute(f"""SELECT * FROM problem_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
problem_entries= self.cur.fetchall()
master_tool_or_question_per_conn_list=[]
master_qualitity_str=[]
master_time_created_conn=[]

specific_problem_or_object=""

for i20, objecttt in enumerate(problem_entries):
    problem_question_or_task= objecttt[1]
    specific_problem_or_object= objecttt[2]
    objectt_string=f"{i20} {specific_problem_or_object};"
    objectt_string=re.sub("[?]","",objectt_string)
    objectt_string=objectt_string.replace("\n","")
    qualitity_list = str(objecttt[4])
    if qualitity_list:
        qualitity_list=qualitity_list.replace("\n","")
        print(qualitity_list)
        qualitity_list=re.split(",",qualitity_list[1:-1])
        for i6, qualities_of_entry in enumerate(qualitity_list):
            if i6==0:
                objectt_string+=f"{qualities_of_entry}"
            else:
                objectt_string+=f",{qualities_of_entry}"

        self.listbox1.insert(tk.END, objectt_string) 