# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:48:29 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
import sys
from django.db.models import Q
from .models import auto_problem_table
from .models import auto_strategy_table
from .models import code_base_table
from .models import galaxies_table
from .models import ideas_table_3
from .models import problem_tree_table
from .models import problem_table
from .models import methods_table
from .models import strategy_table
from .models import problem_solving_screen_recording_table
from .models import prompt_table
from .models import pyautogui_other_computer_completed_generation_table
from .models import pyautogui_page_action_table_2
from .models import scheduled_pyautogui_scripts
from .models import pyautogui_page_action_table_3
from .models import schedule_task_table

from .models import related_task_table
from .models import task_info_table
from .models import gui_script_table

from .models import user_page_searches
from .models import project_type_table













#p = Person(name="Fred Flintstone", shirt_size="L")
#>>> p.save()
#fruit = Fruit.objects.create(name="Apple")
#>>> fruit.name = "Pear"
#>>> fruit.save()
class extra_functions():
    ''' '''
    def __init__(self):
     ''' '''
    def search_sort_based_on_user_info(self):
        """ """
    def create_characters(self,character_str):# get this to work when we have more energy
        """part 1 of search function """
        import re
        #print(character_str)
        if character_str:
            character_str=character_str.lower()
            character_str = re.sub('[^a-z]',"",character_str)
            charcter_list=list(character_str)
            return charcter_list
        else:
            return []
    
   
    def prompt_letter_comparison_to_line_of_code_character(self,prompt_letter,prompt_letter_list_value,line_of_code_characters):  
        """ part 2 search"""
        import copy
        prompt_single_letter_match_list=[]# check when to use this
        matched_letters=0
       
        orignal_prompt_letter=copy.deepcopy(prompt_letter)
        current_prompt_letter_list_value=prompt_letter_list_value
        
        for line_of_code_letter in line_of_code_characters:
            
            if prompt_letter==line_of_code_letter:
               
                matched_letters+=1
                current_prompt_letter_list_value+=1
                try:
                   prompt_letter=self.prompt_characters[current_prompt_letter_list_value]# next prompt letter
                except Exception as e:
                    print(e)
                    prompt_single_letter_match_list.append(matched_letters) 
                    break
                continue
            else:
                prompt_single_letter_match_list.append(matched_letters) 
                current_prompt_letter_list_value=prompt_letter_list_value
                prompt_letter=orignal_prompt_letter
                matched_letters=0
                continue
        return prompt_single_letter_match_list

    def weigh_character_match_list(self,prompt_single_letter_match_list,final_line_of_code_match_list,weight=5):
        """ part 3  search""" 
        max_match=max(prompt_single_letter_match_list)
        weighted_max_match=weight**max_match# using exponetial 1**2
        final_line_of_code_match_list.append(weighted_max_match) #[1, # each value is a letter
       
        return final_line_of_code_match_list
            
    def create_average_match_line(self,final_line_of_code_match_list):
        """part 4 search  """
        max_line_of_code=max(final_line_of_code_match_list)

        return max_line_of_code
    def line_of_code_sort(self,line_of_code_value_dic):
         """ sort the line of code dictionary"""
         sorted_line_code_match_list=[]
         line_of_code_value_dic_len=len(line_of_code_value_dic)-1
         for i11, (line_of_code, average_match_for_line_of_code_line_of_code_placement) in enumerate(line_of_code_value_dic.items()):
             average_match_for_line_of_code=average_match_for_line_of_code_line_of_code_placement[0]
             line_of_code_placement=average_match_for_line_of_code_line_of_code_placement[1]

             if i11==0:
                 print(average_match_for_line_of_code)
                 sorted_line_code_match_list.append([average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                 continue
             for i,sorted_match_values in enumerate(sorted_line_code_match_list):
                 sorted_match_num=sorted_match_values[0]
                 if average_match_for_line_of_code>=sorted_match_num:
                     # at this position
                     #print(listt)# the thing in that spot shifts right when using insert
                     sorted_line_code_match_list.insert(i,[average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                     break
                 if i==line_of_code_value_dic_len :
                     sorted_line_code_match_list.append([average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                     break
                 
                 #if average_match_for_line_of_code>sorted_match_num:
                 #    sorted_line_code_match_list.append([average_match_for_line_of_code,line_of_code_placement_in_list])

         return sorted_line_code_match_list
     
    def sort_dic_function(self,e):
      return e['prompt_word_count']
    def set_current_task_function(self):
        """ """
  
    def search_sort_gui_scripts(self,psp_search):
        """combine above functions search for the lines of code that you want to display at the top of the search """
        #PART 1 Upload data
        line_of_code_value_dic={}
        final_line_of_code_match_list=[]
        all_generated_processed_scripts_list=[]
        all_generated_scripts_llist= pyautogui_other_computer_completed_generation_table.objects.all("script_name")
        all_pyautogui_page_action_scripts = pyautogui_page_action_table_3.objects.all("action_page_script_name","script_activation_time")
        for gen_scriptt in all_generated_scripts_llist :
            all_generated_processed_scripts_list.append(gen_scriptt["script_name"])             
        still_to_generate_script_list_list=[]
        generated_scripts_list_list=[]
        for un_gen_script_dic in all_pyautogui_page_action_scripts:
            script_name=un_gen_script_dic['script_name']
            if script_name in all_generated_processed_scripts_list:
                script_description=un_gen_script_dic['script_description']  
                generated_scripts_list_list.append([script_name,script_description])
                #gui_scripts_to_schedule_list=gui_script_name,script_description
                continue
            else:
                still_to_generate_script_list_list.append([script_name])
                #scripts_to_generate_list=gui_script_name,script_description
        #PART 2 serarch sort part
        still_to_generate_script_list_list=still_to_generate_script_list_list 
        generated_scripts_list_list=generated_scripts_list_list   
        prompt=psp_search
        score_dic_list=[]     
        # highest matching sequence
        prompt_word_list=prompt.split(" ")
        for generated_scripts in generated_scripts_list_list:
            script_name=generated_scripts['script_name']
            script_description=generated_scripts['script_description']
            prompt_word_count=0
            for prompt_word in prompt_word_list:
                if prompt_word in script_name:
                    prompt_word_count+=1
            score_dic_list.append({"script_name":script_name,"prompt_word_count":prompt_word_count,"script_description":script_description})
        score_dic_list.sort(key=self.sort_dic_function,reverse=True)
        # reupload reordered dic to listbox
        gui_dic_list=score_dic_list
        return gui_dic_list

        #for action_score_dic in score_dic_list:
        #    action=action_score_dic["problem_name"]
        #    self.listboxsub_method.insert(tk.END, f"{action}")        
    def search_sort_tasks(self,psp_search):
        """combine above functions search for the lines of code that you want to display at the top of the search """
        # PART 1 upload data
        line_of_code_value_dic={}
        final_line_of_code_match_list=[]
        strategy_tablee = strategy_table.objects.all("problem_being_solved","actions","effects","objectives")
        #PART 2: Search
        prompt=psp_search
        score_dic_list=[]       
        # highest matching sequence
        prompt_word_list=prompt.split(" ")
        for problem_info in strategy_tablee:
            task_name=problem_info["problem_being_solved"]
            sub_task=problem_info["action"]
            effects=problem_info["effects"]
            typee=problem_info["objectives"]
            prompt_word_count=0
            for prompt_word in prompt_word_list:
                if prompt_word in task_name:
                    prompt_word_count+=1
            score_dic_list.append({"task_name":task_name,"prompt_word_count":prompt_word_count,"sub_task":sub_task,"effects":effects,"typee":typee})
        score_dic_list.sort(key=self.sort_dic_function,reverse=True)
        tasks_dic_list=score_dic_list
        return tasks_dic_list# proble
        # reupload reordered dic to listbox
        # need to reuse this structure
        #for action_score_dic in score_dic_list:
        #    action=action_score_dic["problem_name"]
        #    self.listboxsub_method.insert(tk.END, f"{action}")
        


    def get_user_info(self,user_name,password):
        """ """
        user_info={}
        return user_info
    def subprocess_run_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         subprocess.run(command_list, check=True)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
     #inputs:
     #outputs:
     #packages:
     #chatgpt_prompt:
     #search_prompt:
     #end state: 
     return 
 
    def schedule_pyautogui_action_test_table(self,action_page_script_name,script_activation_time):
        """ """
        schecudled_script_list=[["meow",123],["meow",123],["meow",123]]
        return schecudled_script_list
    
    def sort_scheduled_gui_scripts_by_activation_time(self,all_scheduled_action_scripts):
        """ global time is time.time translate the date time to global time to mqake sorting easier"""
        import copy
        sorted_schduled_gui_list=[]
        sorted_scheduled_gui_time_list=[]
        sorted_scheudled_gui_scripts_copy=[]
        for i,  scheduled_script in enumerate(all_scheduled_action_scripts):
            script_activation_time=scheduled_script["script_activation_time"]
            if i ==0:
                sorted_schduled_gui_list.append(scheduled_script)
                sorted_scheduled_gui_time_list.append(script_activation_time)
                sorted_scheudled_gui_scripts_copy.append(scheduled_script)
                continue
                
            if script_activation_time>=sorted_scheduled_gui_time_list[-1]:
                sorted_schduled_gui_list.append(scheduled_script)
                sorted_scheudled_gui_scripts_copy.append(scheduled_script)
                sorted_scheduled_gui_time_list.append(script_activation_time)
                continue
            else:
                # have to add it earlier in the list and check where to add earlier in list using copy list then insert it
                for i2, sorted_scheudled_gui_scripts in enumerate(sorted_scheudled_gui_scripts_copy):
                    if script_activation_time<=sorted_scheudled_gui_scripts["script_activation_time"]:
                        sorted_schduled_gui_list.insert(i2,scheduled_script)
                        sorted_scheduled_gui_time_list.insert(i2,script_activation_time)
                        break
                #because iteraitng tyhrough copy list have to update it here
                sorted_scheudled_gui_scripts_copy=copy.deepcopy(sorted_scheudled_gui_scripts)
                continue
        return sorted_schduled_gui_list    
      
    def get_script_activation_time_from_time_date(self,activation_time,activation_day):
        """ """         
        import datetime
        date_string=f"{activation_day} {activation_time}"
        # If you have a date string
        print(date_string)
        date_string = "2025-05-14 14:45:00"
        date_format = "%Y-%m-%d %H:%M:%S"
        dt_object2 = datetime.datetime.strptime(date_string, date_format)
        timestamp3 = dt_object2.timestamp()
        print(timestamp3)
        return timestamp3
    def schedule_pyautogui_action(self,action_page_script_name,activation_time,activation_day):
        """start up pyautogui listner on big white with activate_all_apis_and_listeners in business functions
        then have a listener specifically executing the scheudled pyautogui scripts
        # add listener to check for scheudled scripts to execute them execute them
        # have this lsitener running  at all times add to listeners in business functions i guess
        # have option to scejdule scripts at different days of week or speicfic times of day"""        
        # find the closest match in the database to the action, the time probably dont need to worry about     
        # save that the script we want to scehdule
        script_activation_time=self.get_script_activation_time_from_time_date(activation_time,activation_day)
        my_object = scheduled_pyautogui_scripts(action_page_script_name=action_page_script_name, script_activation_time=script_activation_time,time=activation_time,date=activation_day,computer_name="all")
        my_object.save()         
        #upload  upload scheudled scripts back to website
        all_scheduled_action_scripts = scheduled_pyautogui_scripts.objects.all("action_page_script_name","time","date","script_activation_time")
        #execute_sort
        sorted_scheduled_action_scripts=self.sort_scheduled_gui_scripts_by_activation_time(all_scheduled_action_scripts)        
        return sorted_scheduled_action_scripts

        #schecudled_script_list_list=[]
        #for scheduled_scripts in all_scheduled_action_scripts :
        #    action_page_script_name=scheduled_scripts['action_page_script_name']
        #    script_activation_time=scheduled_scripts['script_activation_time']
        #    schecudled_script_list_list.append([action_page_script_name,script_activation_time])        
        #return schecudled_script_list_list
        #schecudled_script_list=[["meow",123],["meow",123],["meow",123]]   
        
    
    def sort_scheduled_task_by_global_time(self,all_scheduled_action_scripts):
        """ global time is time.time translate the date time to global time to mqake sorting easier"""
        import copy
        sorted_schduled_gui_list=[]
        sorted_scheduled_gui_time_list=[]
        sorted_scheudled_gui_scripts_list_copy=[]
        for i,  scheduled_script in enumerate(all_scheduled_action_scripts):
            script_activation_time=float(scheduled_script["global_time"])
            if i ==0:
                sorted_schduled_gui_list.append(scheduled_script)
                sorted_scheduled_gui_time_list.append(script_activation_time)
                sorted_scheudled_gui_scripts_list_copy.append(scheduled_script)
                continue
                
            if script_activation_time<=sorted_scheduled_gui_time_list[-1]:
                sorted_schduled_gui_list.append(scheduled_script)
                sorted_scheudled_gui_scripts_list_copy.append(scheduled_script)
                sorted_scheduled_gui_time_list.append(script_activation_time)
                continue
            else:
                print(sorted_scheudled_gui_scripts_list_copy)
                # have to add it earlier in the list and check where to add earlier in list using copy list then insert it
                for i2, sorted_scheudled_gui_scripts in enumerate(sorted_scheudled_gui_scripts_list_copy):
                    print(sorted_scheudled_gui_scripts)
                    print(script_activation_time)
                    print('marker')
                    other_time=float(sorted_scheudled_gui_scripts["global_time"])
                    if script_activation_time>=other_time:
                        sorted_schduled_gui_list.insert(i2,scheduled_script)
                        sorted_scheduled_gui_time_list.insert(i2,script_activation_time)
                        break
                #because iteraitng tyhrough copy list have to update it here
                sorted_scheudled_gui_scripts_list_copy=copy.deepcopy(sorted_schduled_gui_list)
                continue
        return sorted_schduled_gui_list   
    def retrieve_task_info(self,task_name):
        """ """
    def upload_project_categories_to_project_category_table(self):
        print('meow')
        test="""
        <h3 id="concept"class="text-lg font-semibold">Add projects on the right of the screen where adding people is on instagram so people can easily find them</h3>
        <h3 id="concept"class="text-lg font-semibold">when you click on the proejct it loads in content relevent to the project so everyone can see that page and has pretty images like art and lets you edit and grow the project subject to admin approval</h3>
        <h3 id="concept"class="text-lg font-semibold">think github for public good and all things with a pretty project page and content below it like isntagram</h3>
        <h3 id="concept"class="text-lg font-semibold">charity work netowkring and platform</h3>
        <h3 id="concept"class="text-lg font-semibold">Landing Page Content</h3>
        <h3 id="concept"class="text-lg font-semibold">add key poltistical issues here to solve through  goverment grants</h3>
        <h3 id="concept"class="text-lg font-semibold">Climate Change Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Housing Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Food Insecurity Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Cost Of Living Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Indigenous Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Language Rights Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Arts Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Mental Health generate_childrens_book_related_to_topic</h3>
        <h3 id="concept"class="text-lg font-semibold">Support for the LGBTQ2+ Community</h3>
        <h3 id="concept"class="text-lg font-semibold">Disability Projects</h3>
        <h3 id="concept"class="text-lg font-semibold">Cancer Research</h3>
        <h3 id="concept"class="text-lg font-semibold">Medical Research</h3>
        <h3 id="concept"class="text-lg font-semibold">Access to Justice Projects</h3>
        """
        import time
        project_type_table_list_list=[
            ["Climate Change Projects",],
            ["Housing Projects",],
            ["Food Insecurity Projects",],
            ["Cost Of Living Projects",],
            ["Indigenous Projects",],
            ["Language Rights Projects",],
            ["Arts Projects",],
            ["Mental Health Projects",],
            ["Support for the LGBTQ2+ Community",],
            ["Disability Projects",],
            ["Cancer Research",],
            ["Medical Research",],
            ["Access to Justice Projects",]
            ]
        global_time=time.time()
        project_type_table.objects.all().delete()
        for project_type_list in project_type_table_list_list:
            prohject_type_object = project_type_table(project_type_name=project_type_list[0], project_type_image=project_type_list[1],global_time=global_time)
            prohject_type_object.save()
        return
        
    def find_relevent_connections(self,task_name):
        """ """
        relevent_connections_list=[]
        return relevent_connections_list
    def sort_profile_messages_by_date(self):
        """ """
        sorted_messages_list=["","","","",""]
        return sorted_messages_list
    def load_in_psp_content(self):
        import time
        search_time=time.time()
        username=""
        self.current_task=""
        user_name=""
        password=""
        user_info=self.get_user_info(user_name,password)
        if user_info:
            user_object = user_page_searches(username=username,search_time=search_time)  
            user_object.save()
            # use user info to upload correct values
            
            self.current_task=""
            self.task_info_list=[]
            self.sub_task_list=[]
            self.search_sort_based_on_user_info() 
            strategy_tablee = strategy_table.objects.all()
            for strategy_object in strategy_tablee:
                sub_task_list=[]
                problem_being_solved=strategy_object['problem_being_solved']
                strat_delimiter=strategy_object['strat_delimiter']
                step_delimiter=strategy_object['step_delimiter']
                actions=strategy_object['action']
                effects=strategy_object['effects']
                objectives=strategy_object['type']
                # parse result shere for different tables
                sub_task_list.append([problem_being_solved,actions.effects,objectives])
        else:
            #generic no login or user info
            self.task_info_list_list=[["Search a task!","Search a task!","iterator_1","iterator_2"]]# leave these with a message because no repviosu login
            self.task_info_list_list=[["Search a task!","Search a task!","iterator_1"]]# leave these with a message because no repviosu login

            #task_info_list=task_document, task_document_content
            self.current_task=[["Search a Task!"]] # leave these with a message because no repviosu login
            self.sub_task_list_list=[["Search a Task!","Search a Task!","Search a Task!","Search a Task!","Search a Task!","iterator","iterator"]] # leave these with a message because no repviosu login
            # sub_task_list=group,step,sub_task,effects,type# make step and group very small and under one column like 1.1 for step 1 of group 1

            #strategy_tablee = strategy_table.objects.all("problem_being_solved","actions","effects","objectives")
            sub_task_list=[]
            ### need ot figure out how to integrate this
            column_names_list=["Related_Task","",""]

            
            related_task_tablee = related_task_table.objects.values("problem_being_solved","related_task","id")

            related_task_list_list=[] 
            print(related_task_tablee)
            for i, related_task in enumerate(related_task_tablee):              
                problem_being_solved=related_task['problem_being_solved']
                related_taskk=related_task['related_task']
                idd=related_task['id']
                related_task_iterator=f"related_task:related_task:{idd}"
                row_task_iterator=f"row:related_task:{idd}"

                # parse result shere for different tables
                related_task_list_list.append([related_taskk,related_task_iterator,row_task_iterator])
                #related_task_list=related_task,sub_tasks,effects,type                
            related_task_list_list=related_task_list_list[:100]           
            # upload general website schedule
            scheduled_task_list_list=[] 
            #schedule_tablee = schedule_task_table.objects.all("problem_being_solved","time","date")           
            schedule_tablee = schedule_task_table.objects.values("problem_being_solved","time","date","global_time","id")
            schedule_tablee=self.sort_scheduled_task_by_global_time(schedule_tablee)    

            #column_names_list=["Task","Date","Time","",""]
            if schedule_tablee:
                print('hi')
                print(schedule_tablee)
            else: 
                schedule_tablee=[]
                

            for i, scheduled_task in enumerate(schedule_tablee):
                problem_being_solved=scheduled_task['problem_being_solved']
                time=scheduled_task['time']
                date=scheduled_task['date']
                idd=scheduled_task["id"]
                task_scheduled_task_iterator=f"task:scheduled_task:{idd}"
                row_scheduled_task_iterator=f"row:scheduled_task:{idd}"

                scheduled_task_list_list.append([problem_being_solved,time,date, task_scheduled_task_iterator,
                 row_scheduled_task_iterator ])
                #current_schedule_list=task,sub_tasks,effects,type,time,date            
            #scheduled_pyautogui_scriptss = scheduled_pyautogui_scripts.objects.all()
                #scheduled_gui_script_list=gui_script_name, time,date
            #just check all the values  in row to avoid button issues
            #gui scripts to still generate and scripts generated
            gui_script_list_list=[]
            gui_script_tblee = gui_script_table.objects.values("script_name","script_description","id")
            for i3, gui_script in enumerate(gui_script_tblee):
                script_description=gui_script["script_description"]
                script_name=gui_script["script_name"]
                idd=gui_script["id"]
                scripts_iterator=f"script:scripts|:{idd}"
                scripts_iterator2=f"row:scripts|:{idd}"
                gui_script_list_list.append(script_name,script_description,scripts_iterator,scripts_iterator2)        
        ###create lists
        current_task=self.current_task
        task_info_list=self.task_info_list_list
        sub_task_list=self.sub_task_list_list
        related_task_list=related_task_list_list
        current_schedule_list=scheduled_task_list_list
        gui_scripts_list=gui_script_list_list
        #example columns="""
        #current_task=current_task
        #task_info_list=task_document, task_document_content
        #sub_task_list=group,step,sub_task,effects,type# make step and group very small and under one column like 1.1 for step 1 of group 1
        #related_task_list=related_task,sub_tasks,effects,type
        #current_schedule_list=task,sub_tasks,effects,type,time,date
        #scheduled_gui_script_list=gui_script_name, time,date
        #gui_scripts_to_schedule_list=gui_script_name,script_description
        #scripts_to_generate_list=gui_script_name,script_description"""
        
        # note that type is the eqvualent of objectives
        table_info_dic = {"current_task":current_task,
        "task_info_list":task_info_list,
        "sub_task_list":sub_task_list,
        "related_task_list":related_task_list,
        "current_schedule_list":current_schedule_list,
        "gui_scripts_list":gui_scripts_list}
        return  table_info_dic
    
    def schedule_task(self,task_to_schedule,activation_time,activation_day):
        """start up pyautogui listner on big white with activate_all_apis_and_listeners in business functions
        then have a listener specifically executing the scheudled pyautogui scripts
        # add listener to check for scheudled scripts to execute them execute them
        # have this lsitener running  at all times add to listeners in business functions i guess
        # have option to scejdule scripts at different days of week or speicfic times of day"""        
        # find the closest match in the database to the action, the time probably dont need to worry about     
        # save that the script we want to scehdule
        global_time=self.get_script_activation_time_from_time_date(activation_time,activation_day)
        # generagte task info from psp api
        problem_info_str=self.query_psp_search_api(task_to_schedule)
        actions=problem_info_str
        effects=problem_info_str
        objectives=problem_info_str
        my_object = strategy_table()
        my_object.save()  
        
        my_object = schedule_task_table(problem_being_solved=task_to_schedule,
                                   tasks=actions,
                                   effects=effects,
                                   typee=objectives,
                                   global_time=global_time,
                                   time=activation_time,
                                   date=activation_day)
        my_object.save() 
        
        my_object = strategy_table(problem_being_solved=task_to_schedule,
                                   tasks=actions,
                                   effects=effects,
                                   typee=objectives)
        my_object.save()    
        
        
        #upload  upload scheudled scripts back to website
        scheduled_taskss = schedule_task_table.all("schedule_table","time","date","global_time")
        #execute_sort
        sorted_scheduled_action_scripts=self.sort_scheduled_task_by_global_time(scheduled_taskss)        
        return sorted_scheduled_action_scripts
 
        
         
    def reupload_task_info_to_html(self):
        """ """
        # add to relevent tables on website html
        task_info_tablee = task_info_table.objects.values("document","document_content","id")
        sub_task_tablee = strategy_table.objects.values("problem_being_solved","strat_delimiter","step_delimiter","task","effects","typee","id")


        related_task_tablee = related_task_table.objects.values("problem_being_solved","related_task","id")
        #'save {{ iterator }}'
        #'delete {{ iterator }}'
        button_save_list=["modify_info","submit",["bg-blue-500","text-white","px-4","py-2","rounded-lg","hover:bg-blue-600","focus:outline-none"],"save","save "]
        button_delete_list=["modify_info","submit",["bg-blue-500","text-white","px-4","py-2","rounded-lg","hover:bg-blue-600","focus:outline-none"],"delete","delete "]
        #all_scheduled_task_dic_list = schedule_task_table.objects.all("problem_being_solved","time","date","global_time")
        all_scheduled_task_dic_list = schedule_task_table.objects.values("problem_being_solved","time","date","global_time","id")        
        sorted_scheduled_action_scripts=self.sort_scheduled_task_by_global_time(all_scheduled_task_dic_list)        
        # uphold api response to html
        relevent_table_names=["task_info_table","current_schedule_table","sub_task_table","related_task_table"]
        task_info_list=[]
        px_list=["px-6","px-6","px-1","px-1"]
        py_list=["py-4","py-4","py-1","py-1"]
        column_names_list=["Task_Document","Task_Document_Content","",""]

        onclick_list=['download_document()',"None","None","None"]
        contenteditable_list=["True","None","None","None"]
        #relevent_table_names_list=[relevent_table_names,relevent_table_names]
        button_list=["None","None",button_save_list,button_delete_list]
        for i1, task_info in enumerate(task_info_tablee):
            innerText_list=[task_info["document"],task_info["document_content"],"None","None"]
            # create cell dicitonary then add as key to temp dic dic
            cells_dic_list=[]
            for ii, px in enumerate(px_list):
                py=py_list[ii]
                columnn=column_names_list[ii]
                onclick=onclick_list[ii]
                contenteditable=contenteditable_list[ii]
                button=button_list[ii]
                innerText=innerText_list[ii]
                temp_cell_dic={"px":px,"py":py,"button":button,"button_content":button,"innerText":innerText,"contenteditable":contenteditable,"onclick":onclick}
                cells_dic_list.append(temp_cell_dic)

            temp_dic_dic={"table":"task_info_table",
                               'document':task_info["document"],
                               "document_content":task_info["document_content"],
                               "iterator":f'{columnn}:task_info:{task_info["id"]}',
                               "iterator2":f'{columnn}2:task_info:{task_info["id"]}',

                               "relevent_table_names":relevent_table_names}
            temp_dic_dic["cells"]=cells_dic_list
            task_info_list.append(temp_dic_dic)
        # need to make this a list of dics?
        #'save {{ iterator }}'
        #'delete {{ iterator }}'
        #add to buttons on recreate
        
        scheduled_task_list=[] 
        px_list=["px-6","px-6","px-6","px-1","px-1"]
        py_list=["py-4","py-4","py-4","py-1","py-1"]
        column_names_list=["Task","Date","Time","",""]

        onclick_list=['set_current_task()',"None","None","None","None"]
        contenteditable_list=['True',"True",'True',"None","None"]
        button_list=["None","None","None",button_save_list,button_delete_list]    
        for i2, scheudled_script in enumerate(sorted_scheduled_action_scripts):
            innerText_list=[scheudled_script["problem_being_solved"],scheudled_script["date"],scheudled_script["time"],None,None]
            cells_dic_list=[]
            for ii, px in enumerate(px_list):
                py=py_list[ii]
                onclick=onclick_list[ii]
                columnn=column_names_list[ii]

                contenteditable=contenteditable_list[ii]
                button=button_list[ii]
                innerText=innerText_list[ii]
                temp_cell_dic={"px":px,"py":py,"button":button,"innerText":innerText,"contenteditable":contenteditable,"onclick":onclick}
                cells_dic_list.append(temp_cell_dic)

            temp_dic_dic={"table":"current_schedule_table",
                                    'task':scheudled_script["problem_being_solved"],
                                    "date":scheudled_script["date"],
                                    "iterator":f'{columnn}:scheduled_task:{scheudled_script["id"]}',
                                    "iterator2":f'{columnn}2:scheduled_task:{scheudled_script["id"]}',
                                    "time":scheudled_script["time"],}
            temp_dic_dic["cells"]=cells_dic_list
            scheduled_task_list.append(temp_dic_dic)

        sub_task_list=[]
        px_list=["px-1","px-6","px-6","px-6","px-1","px-1"]
        py_list=["py-1","py-4","py-4","py-4","py-1","py-1"]
        column_names_list=["Step","Sub_Task","Effects","Type","",""]

        onclick_list=["None",'set_current_task()',"None","None","None","None"]
        contenteditable_list=["None",'True',"True",'True',"None", "None"]
        button_list=["None","None","None","None",button_save_list,button_delete_list]
        for i3, actionn in enumerate(sub_task_tablee):
            innerText_list=[actionn['strat_delimiter'],actionn['step_delimiter'],actionn["task"], actionn["effects"],actionn["typee"],None,None]                 
            cells_dic_list=[]
            for ii, px in enumerate(px_list):
                py=py_list[ii]                 
                button=button_list[ii]
                innerText=innerText_list[ii]
                columnn=column_names_list[ii]
                contenteditable=contenteditable_list[ii]
                onclick=onclick_list[ii]
                temp_cell_dic={"px":px,"py":py,"button":button,"innerText":innerText,"contenteditable":contenteditable,"onclick":onclick}
                cells_dic_list.append(temp_cell_dic)
            temp_dic_dic={"table":"sub_task_table",
                              'strat_delimiter':actionn['strat_delimiter'],
                              'step_delimiter':actionn['step_delimiter'],
                              'sub_task':actionn["task"],                         
                              "effects":actionn["effects"],
                              "type":actionn["typee"],
                              "iterator":f'{columnn}:sub_task:{actionn["id"]}',
                             "iterator2":f'{columnn}2:sub_task:{actionn["id"]}',

                              }
            temp_dic_dic["cells"]=cells_dic_list
            sub_task_list.append(temp_dic_dic)
            
        related_task_list=[]
        px_list=["px-6","px-1","px-1"]
        py_list=["py-4","px-1","px-1"]
        column_names_list=["Related_Task","",""]
        button_list=["None",button_save_list,button_delete_list]
        onclick_list=["set_current_task()","None","None"]
        contenteditable_list=['True',"None", "None"]      
        
        for i4,related_taskk in enumerate(related_task_tablee):
            innerText_list=[related_taskk["related_task"],"None","None"]
            cells_dic_list=[]
            for ii, px in enumerate(px_list):
                py=py_list[ii]
                onclick=onclick_list[ii]
                contenteditable=contenteditable_list[ii]
                button=button_list[ii]
                columnn=column_names_list[ii]
                innerText=innerText_list[ii]
                temp_cell_dic={"px":px,"py":py,"button":button,"innerText":innerText,"contenteditable":contenteditable,"onclick":onclick}
                cells_dic_list.append(temp_cell_dic)             
            temp_dic_dic={"table":"related_task_table",
                                  'related_taskk':related_taskk["related_task"],
                                  "iterator":f'{columnn}:related_task:{related_taskk["id"]}',
                                  "iterator2":f'{columnn}2:related_task:{related_taskk["id"]}',

                                  } 
            temp_dic_dic["cells"]=cells_dic_list
            related_task_list.append(temp_dic_dic)

        task_info_list.extend(scheduled_task_list)
        task_info_list.extend(sub_task_list) 
        task_info_list.extend(related_task_list)
        print(task_info_list)
        return task_info_list
    def edit_bash_line_file(self,intital_bash_file_name,final_bash_file_name,mod_line,line_number=0):
        """ """
        with open(intital_bash_file_name,"r") as f3:
            f3_file_str=f3.read()
        f3_file_str_list=f3_file_str.splitlines()
        f3_file_str_list[line_number]=fr'{mod_line}'
        final_file_str=""
        for i, linee in enumerate(f3_file_str_list):
            if i==0:
                final_file_str=f"{linee}"
            else:
                final_file_str+=f"\n{linee}"              
        final_file_str=rf"{final_file_str}"
        with open(final_bash_file_name,"w") as f4:
            f4.write(final_file_str)
        print('change made')
    def generate_pyautogui_files_on_other_computers_from_big_black_using_website(self,action_page_script_name):
        """start up pyautogui listner on big white with activate_all_apis_and_listeners in business functions """
        import time
        timee=time.time()
        completed_table="pyautogui_other_computer_completed_generation_table"
        uncompleted_table="pyautogui_page_action_table_2"
        website_listener_folder_path=r"/home/jross77/Documents/pyauto_gui_listener_website"
        big_black_generate_folder_path=r"/home/jross77/Documents/generate_pyauto_gui_files_remote_linux"
        column_wanted_to_compare_list=["script_name","computer_name"]
        intital_pyauto_generate_bash_file=r"create_pyautogui_file_of_inputs_and_video_bash_intital.sh" # add this to bash
        final_pyauto_generate_bash_file=r"create_pyautogui_file_of_inputs_and_video_bash_final.sh" # add this to bash
        intital_pyauto_generate_bash_file_path=website_listener_folder_path + "/"+intital_pyauto_generate_bash_file
        final_pyauto_generate_bash_path=website_listener_folder_path + "/"+ final_pyauto_generate_bash_file      
        username="jross77"
        host="192.168.2.43"
        script_name_to_use=action_page_script_name# add this to bash
        # find the closest match in the database
        
        print(script_name_to_use)
        input("stopp")
        line_to_sub_value=fr'database_script_name="{script_name_to_use}"'
        self.edit_bash_line_file(intital_pyauto_generate_bash_file_path,final_pyauto_generate_bash_path,line_to_sub_value,line_number=3)  
        print('see if bash file was created')              
        # copying from server to bigblack
        # still not creating the final file after edit need to fixt his
        scp_command_list = [f"scp",f"/home/jross77/Documents/pyauto_gui_listener_website/{final_pyauto_generate_bash_file}",  f"{username}@{host}:{big_black_generate_folder_path}/"]# put the script you want to run here '
        self.subprocess_run_script_remotely(scp_command_list)
        doc2ui = [f"ssh",  f"{username}@{host}","dos2unix",f"{big_black_generate_folder_path}/{final_pyauto_generate_bash_file}"]
        self.subprocess_run_script_remotely(doc2ui)   
        ssh_command = [f"ssh",  f"{username}@{host}","bash",f"{big_black_generate_folder_path}/{final_pyauto_generate_bash_file}"]
        self.subprocess_run_script_remotely(ssh_command)  
        print(" if executing this listener directly on big black just run a single line executing bash instead of uploading bash with the above lines to big black from other server")
        # save that the script was generated
        my_object = pyautogui_other_computer_completed_generation_table(script_name=script_name_to_use, timee=timee,computer_name="all")
        my_object.save()       
        #upload  updagted to gen script info back to website
         # going to do this in views
        #return still_to_generate_script_list_list
    # parse for if not in pyautogui_other_computer_completed_generation_table     
    #to_complete_generation_table_dic={"script_name":script_name_to_use,"timee":timee,computer_name:"all" }     
    #self.upload_data_from_website_database("pyautogui_other_computer_completed_generation_table",to_complete_generation_table_dic)
   # print('format wanted== schecudled_script_list=[["meow",123],["meow",123],["meow",123]]')
    #json_response_list=[["meow",123],["meow",123],["meow",123]]
    def query_psp_search_api(self,psp_search,host,type_of_search="all"):
        """ need to test this to see if host is found
        type of search will be scheudle  pyautogui
        start up api  on big white with activate_all_apis_and_listeners in business functions
        """
        import requests
        all_problem_info_dic={}
        edited_psp_search=psp_search
        url = f"http://{host}:8000/psp_search/"
        params = {
          "search": f"{edited_psp_search}",
          "typee":f"{type_of_search}"}
      # Send GET request to FastAPI server with query parameters
        response = requests.get(url, params=params)
        #print(response.json())
        print(response)

        if response.status_code == 200:
            # Parse and print the response JSON
            all_task_info_dict_list_dic = response.json()
            print(all_task_info_dict_list_dic)
            #task_info_listt=problem_info_str
            #current_task_strats_dic_listt=problem_info_str        
            #related_task_listt=problem_info_str
            # need to access key sent
            all_task_info_dict_list_dic=all_task_info_dict_list_dic["all_task_info_dict_list_dic"]
            # process data here nee in proper form
            print('format wanted== schecudled_script_list=[["meow",123],["meow",123],["meow",123]]')
            print("Response from FastAPI:")
            return all_task_info_dict_list_dic,edited_psp_search
        else:
            print(f"Failed to get response, status code: {response.status_code}") 
            return None, None
        # save data to tables
        
        # upload data from tables 
        
        #return retrieved data in correct format
        
        
    
    

class extra_functions_child():
    ''' '''
    def __init__(self):
     ''' '''
   
    
class extra_functions_gchild(extra_functions_child):
    ''' '''
    def __init__(self):
     ''' '''
     
    
        
    
class extra_functions_g2_child(extra_functions_gchild):
    ''' '''
    def __init__(self):
     ''' '''
     

        
        # copy all the applicable function into here as we transfer them over
    
