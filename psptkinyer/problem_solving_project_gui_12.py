
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:27:46 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
   
#problem need to display the new database ideas in the right boxes 
# need to be able to access the old database ideas to keep cateogrizing in order to build neural network
# step1 so first upload  new database ideas 
# step2  build a program to acccess old database ideas
# step3 start using method and keep updating old database
# need to fix current connected objects and possible objects
    

#NEED TO WORK ON THIS#problem 2 fix the number thing making it actually record the number and paste it as the name of the step i'm trying
# look at number function
# try using it and modifying the code in it digoaniss where the code is messing up
# fix this part of the code by googling or trying different things understanidng all things invovled like
# packages and everything and creating step by step process to fix
# orginal database name  ideas_table_3 from labels_for_idea_program_2
#ideas2 is just before adding labels to the ideas


#the world is great
#problem 7. ACTUALLY USE THE problem solving process
#Start by making a life diagram and expand out categorizing and then finding tasks within categories 
#and building methods for all of these takss and problems you encounter in life and 
# making this hierarcial .
# every time something comes up i need to use the program
# need to look at sticky notes and make sure i have not missed anything

#problem 8. need to manage ideas and get everything uploaded and make it something i'm happy with
# maybe develop a app for putt ideas into the database from computer and phone

# step 4 develop neural network for future labels to pre-cateogrize or transform for me to perform step 3

# step 3 uploading to ideas_table_3 from labels_for_idea_program_2
# manually do this

# problem 4.	Using method need to access method from database and apply  need to build a seperate app for this
# can access this app on phone or maybe learn node js for this
# use same code to transform idea to fit into a category or to just place in a category


#problem 6. add in button functionality one way to access past method might be a button i can click to reload the
# submethod window to view past methods
# want to access past methods and there components easily


# method being previous methods i have created and needs to actually get attribtues
# access old method steps
# we could past methods info using submethods with

import tkinter as tk
from tkinter import *

import time
import customtkinter
#program_start_time=time.time()
window = tk.Tk()
window.state('zoomed')

window.title('Problem Solving Program')



def increase(lbl_value):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease(lbl_value):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


class buttons_per_quadrant():
    def __init__(self):
        """ """
        import pyperclip
        from ctypes import windll
        import pyautogui
    def subprocess_popen_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         p=subprocess.Popen(command_list)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
         print('ERROR')
     return p
    def mkdir_dir_bash(self,dir_to_make,host,host_name):
      """ """
      import subprocess
      mkdir_bashs=rf"""#!/bin/bash
   # Define the directory path
   DIR="{dir_to_make}"
   # Create the directory
   if [ -d "$DIR" ]; then
    echo "dir exists!"
   else
    echo "dir not exists!"
    mkdir -p "$DIR"
    chmod 777 "$DIR"
    sudo chown jross77 "$DIR"
   fi   """   
      mkdir_local_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\bash.sh"
      with open(mkdir_local_file_name,"w") as f:
          f.write(mkdir_bashs)
      scp_command_list = [f"scp",f"{mkdir_local_file_name}",  f"{host_name}@{host}:/home/jross77/"]# put the script you want to run here 
      self.subprocess_run_script_remotely(scp_command_list)
      #ssh into the 
      doc2ui = [f"ssh","-X",  f"{host_name}@{host}","dos2unix","/home/jross77/bash.sh"]
      self.subprocess_run_script_remotely(doc2ui)  
      ssh_command = [f"ssh",  f"{host_name}@{host}",f"bash /home/jross77/bash.sh"]# put the script you want to run here
      try:
          subprocess.run(ssh_command, check=True,shell=True)
      except subprocess.CalledProcessError as e:
          print(f"Failed to SSH into {host}: {e}")
          
    def subprocess_run_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         subprocess.run(command_list, check=True,shell=True)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
    ##### RECORDING RPOBLEM FUNCTIONS
    
    def screen_record(self,screen_shot_time):
        import pyautogui
        import cv2
        import numpy as np
        import win32gui
        import re
        spacing_to_add=""
        img = pyautogui.screenshot()
        window = win32gui.GetForegroundWindow()
        active_window_name = win32gui.GetWindowText(window)
        active_window_name=re.sub(r"\'","",active_window_name)
        active_window_name=re.sub(r"\"","",active_window_name)
        if self.previous_active_window_name!= active_window_name:
            spacing_to_add="\n#--------------\n#--------------\n#--------------\n"
        self.previous_active_window_name=active_window_name
        
            # add a bunch of new line characters to seperate out strs
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        path_to_frame=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\screenshots\screenshot{screen_shot_time}.png"
        cv2.imwrite(path_to_frame,frame)
        return path_to_frame,active_window_name,spacing_to_add
 
    def mouse_pynput_on_click(self,x, y, button, pressed):
        """record on click elements """
        # get mouse scroll
        from pynput import mouse
        import time 
        query_time= time.time()
        if button == mouse.Button.left:
            print('Screenshot taken!')
            path_to_screenshot,active_window_name,spacing_to_add=self.screen_record(query_time)
            screen_recording_info_dic={"path_to_screenshot":path_to_screenshot,"active_window_name":active_window_name,"timee":query_time}
            self.upload_problem_screen_information_to_sql(screen_recording_info_dic)
    def clean_strs_before_input_into_sql(self,strrr):
         """ """
         import re
         strrr=re.sub('\'',"",str(strrr))
         strrr=re.sub('\"',"",strrr)
         strrr=re.sub('\n',"",strrr)
         return strrr
    def upload_problem_screen_information_to_sql(self,screen_recording_info_dic):
        """ """
        import time
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        path_to_screenshot=screen_recording_info_dic["path_to_screenshot"]
        active_window_name=screen_recording_info_dic["active_window_name"]
        timee=screen_recording_info_dic["timee"]

        path_to_screenshot=self.clean_strs_before_input_into_sql(path_to_screenshot)
        active_window_name=self.clean_strs_before_input_into_sql(active_window_name)
        timee=self.clean_strs_before_input_into_sql(timee)

        # need to make sure not to over write  values here

        self.cur.execute( f""" INSERT INTO problem_solving_screen_recording_table (problem_question_or_task,path_to_screenshot,active_window_name,timee)
                     VALUES ('{str(self.problem_recorded)}','{str(path_to_screenshot)}','{str(active_window_name)}','{str(timee)}');""")
            
        self.conn.commit()
    def display_problem_tree_in_method_window(self,event):
        """press = to reopen method window and display problem_recorded """
        print('hi')
        methods=methods_window_program()
        methods.problem_recorded=self.problem_recorded
        methods.display_current_problem_info()
        # display the specific problem we want
        # and other results in listboxs
        
   
    def code_whole_problem_tree_using_coding_program_create_new_project(self,event):
        """JUST CODE EVERY PROBLEM strategy dont have seperate button
        and engineer every problem strategy
        usee llm to build glossary for all problems and show glossary once it is built
        # use llm to also build problem environemnt through lists of questions
        add in the other related functions for saving problem data here"""
        import sys
        import re
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\business_process_management_functions')
        from business_process_management_functions80 import business_process_management_functions
        business0=business_process_management_functions()
        from business_process_management_functions80 import business_process_management_functions_child
        business1=business_process_management_functions_child()
        from business_process_management_functions80 import business_process_management_functions_gchild
        business2=business_process_management_functions_gchild()
        from business_process_management_functions80 import business_process_management_functions_g2child
        business3=business_process_management_functions_g2child()
        modified_text=self.text_box01.get('1.0', 'end')
        print(modified_text)
        #search_dictionary_term=re.search(r"(.*);",modified_text).group(1)
        #use a seperate compuer for each
        # build coding prbolem tree first
        # then run through mdoels
        # do all this with llamma for now
        # keep it simple get it done by tonight
        # setup quick website
        # add an api to it for the model
        # make the model accessible
        #

        # CODING PROGRAM
        print('THIS IS THE CODING PROGRAM environment')
        business2.chatgpt_gen_pyautogui_program_generate_environment(modified_text)
        business2.llamma_gen_pyautogui_program_generate_environment(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_generate_environment(modified_text)
        
        # consider alternatives  and code them
        print('THIS IS THE CODING PROGRAM strats')
        business2.chatgpt_gen_pyautogui_program_generate_strats(modified_text)
        business2.llamma_gen_pyautogui_program_generate_strats(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_generate_strats(modified_text)
        
        print('THIS IS to actually code the whole problem tree')
        # then code each function in the coding problem tree and alternative approaches
        business2.chatgpt_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.llamma_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        # use specific prompts for these
        
        #repeat by breaking the problem down into strat steps and then code those as well in higher order classes
        # do the whole coding tree here breaking down the task
        self.test_code_created()# in execute file
        self.fix_code_if_errors() # fix code
        # retest code
        self.rewrite_code_to_file() 
        
        
        # problems sovling program
        self.generate_environment()# use questions
        self.generate_strats() # use strats and display and save them in a table
        
        
        
        
        
        # worry about these another day
        # engineering program
        #bbuild special gen ai models for this
        
        
        # investment program
        # build algorhim for this
        
        
        self.llamma_to_generate_environment()
        self.update_and_show_coding_program(modified_text)
        self.query_llm_from_lm_studio(modified_text)
        self.web_searches(modified_text)# check against github
        
        self.create_problem_glossary()
        self.open_problem_glossary()
        self.build_enigneering_project() # then build engineering desing on each query
        self.build_search_for_engineering_pipeline()
        self.build_investmnet_project()
        self.build_supply_chains()      
        self.build_pizza_maker()
        self.build_as_many_useful_physical_thingas_possilbe()# patent them 
        # build the ecommcerce site
        self.build_law_project()
        self.build_search_find_all_free_and_useful_sas_and_projects_to_add_to_psp()
        # https://workik.com/terms-of-service # coding assitant could use 
        self.build_model_to_perform_all_tasks_on_website()# so can access any website forms or services or login
        self.use_models_to_genrate_quesitons_and_all_objects_in_problem_so_efects_and_problems_themselves()
    def handle_click(self, event):
        """ """
        print("The button was clicked!")
        import subprocess
        #subprocess.call('python testing_record_screen.py', shell=True)
        subprocess.Popen(["python", "testing_record_screen.py"])
        #from multiprocessing import Process
        #sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
        #from record_screen_for_additonal_problem_data_and_send_to_sql import record_screen_for_additonal_problem_data_and_send_to_sql_l
        #record_screennn=record_screen_for_additonal_problem_data_and_send_to_sql_l()
        #process = Process(target=record_screennn.record_screen_for_additonal_problem_data_and_send_to_sql_function,args=("",)) 
        #process.start()
        #print('hi')
    def sort_dic_function(self,e):
      return e['prompt_word_count']
   
  
    def method_box_list_search(self,event):
        """ """
        prompt=self.entry_1.get()
        problems_in_listbox= self.listboxsub_method.get(0, tk.END)
        score_dic_list=[]
        
        # highest matching sequence
        prompt_word_list=prompt.split(" ")
        for problem in problems_in_listbox:
            prompt_word_count=0
            for prompt_word in prompt_word_list:
                if prompt_word in problem:
                    prompt_word_count+=1
            score_dic_list.append({"problem_name":problem,"prompt_word_count":prompt_word_count})
        score_dic_list.sort(key=self.sort_dic_function,reverse=True)
        self.listboxsub_method.delete(0, tk.END)
        # reupload reordered dic to listbox
        for action_score_dic in score_dic_list:
            action=action_score_dic["problem_name"]
            self.listboxsub_method.insert(tk.END, f"{action}")

        # get items in listbox
        # rank items by top match
        # access old element to add to it
    def web_results_list_search(self,event):
        """ """
        print('hi')
        prompt=self.entry_2.get()
        problems_in_listbox= self.listbox5.get(0, tk.END)
        score_dic_list=[]
        # highest matching sequence
        prompt_word_list=prompt.split(" ")
        for problem in problems_in_listbox:
            prompt_word_count=0
            for prompt_word in prompt_word_list:
                if prompt_word in problem:
                    prompt_word_count+=1
            score_dic_list.append({"problem_name":problem,"prompt_word_count":prompt_word_count})
        score_dic_list.sort(key=self.sort_dic_function,reverse=True)
        self.listbox5.delete(0, tk.END)
        # reupload reordered dic to listbox
        for action_score_dic in score_dic_list:
            action=action_score_dic["problem_name"]
            self.listbox5.insert(tk.END, f"{action}")
    


    def switch_to_step_building_method(self):
        """ button on top of screen clicked will change the names functions and textboxes used in program"""
        
    def import_tools_problems_or_existing_ideas(self, label,table_name= "public.ideas_table_3",galaxies_table=False,sub_methods_table=False): 
        """  import data to different quadrants on the page """
        import re
        label_list=[]
        label=str(label)
        self.llm_studio_set_up=False
        if sub_methods_table == True:
            problem_dictionary={}
            self.cur.execute(f"""SELECT problem_being_solved,method_step, strategy_action  FROM methods_table ;""")
            all_idea_in_database_list_format= self.cur.fetchall()
            for idea9 in all_idea_in_database_list_format: 
                problem_being_solved=idea9[0]
                method_step_info=idea9[1]
                strategy_action_info=idea9[2]
                if  problem_dictionary.get(problem_being_solved):
                    print('key exists')
                else:
                    problem_dictionary[problem_being_solved]=[]# values of the strategies and actions in one giant list
                    # add in ideas
                problem_dictionary[problem_being_solved].append(method_step_info)
                if strategy_action_info:
                    actions_found=re.split(",",strategy_action_info)
                    for actionss in actions_found:
                        problem_dictionary[problem_being_solved].append(actionss)
                    
                
            for problemmm, strat_act_list in problem_dictionary.items():
                strat_act_list=re.sub(r"[\'\[\]?]","",str(strat_act_list))
                problem_list_to_add=problemmm + ";" + strat_act_list
                label_list.append(problem_list_to_add)

        if galaxies_table == True:
            self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list  FROM problem_table ;""")
            all_idea_in_database_list_format= self.cur.fetchall()
            for idea9 in all_idea_in_database_list_format: 
                objecttt=idea9[0]
                qualtities=idea9[1]
                qualtities=re.split(",",qualtities)
                galaxy=objecttt + ";" + str(qualtities)
                galaxy=re.sub(r"[\'\[\]?]","",galaxy)
                # need to fix upstream problem of  there be weird things in the stream
                #  and be able to work with the string later
                # need to remove the quesitons marks
                label_list.append(galaxy)       
        else:
            self.cur.execute(f"""SELECT updated_sentence FROM {table_name} WHERE updated_label = CAST({label} AS text) ;""")
            all_idea_in_database_list_format= self.cur.fetchall()
            for idea in all_idea_in_database_list_format: 
                label_list.append(str(idea))
                continue
            
            
        return label_list
   
    
    def pre_create_galaxies(self,event):
        """use an objects definitions to create qualtities of an object """
        import re
        def insert_search_term_from_box():
            """ access contents in listbox to  """
            modified_text=self.text_box0.get('1.0', 'end')
            search_dictionary_term=re.search(r"(.*);",modified_text).group(1)
            return search_dictionary_term
        def get_defintion(search_dictionary_term):
            """ search site and process defintion into qualities of a object """
            import requests
            import json # look up docs on this
            from bs4 import BeautifulSoup
            import nltk
            from nltk.corpus import stopwords
            definition_words=[]
            #nltk.download('stopwords')
            api_link_search = r"https://www.merriam-webster.com/dictionary/" + search_dictionary_term
            session = requests.Session()
            headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
            'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
            'Accept':'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/webp,*/*;q=0.8'}
            req = session.get(api_link_search, headers=headers)
            soup = BeautifulSoup(req.text)
            mydivs = soup.find_all("span", {"class": "dtText"})
            p_tag_text=mydivs[0].get_text()
            print(p_tag_text)
            find_word_pattern = re.compile(r"\w+")
            word_list = find_word_pattern.findall(p_tag_text)
            definition_words = [word for word in word_list if word not in stopwords.words('english')]           
            #print(definition_words)
            return definition_words
        def upload_back_to_text_box(definition_words):
            """upload text back to textbox """
            # seperate by commas
            str_to_add_to_textbox=""
            for i, defintion_word in enumerate(definition_words):
                print(defintion_word)
                if i ==len(definition_words)-1:
                    print(i)
                    str_to_add_to_textbox+=defintion_word
                else:
                    str_to_add_to_textbox+= defintion_word+"=" 
            print(str_to_add_to_textbox)
            self.text_box0.insert(tk.END,str_to_add_to_textbox)

        search_dictionary_term=insert_search_term_from_box()
        definition_words=get_defintion(search_dictionary_term)
        upload_back_to_text_box(definition_words)
 
    def add_previous_galaxies_to_problem(self,event): 
        """ press 4 choose to add the qualtites from a previous galaxy with same name to the problem"""
        import re
        import copy
        content=window.selection_get()
        content= re.sub('\d+:','',content) 
        content2=content[:-1]
        time_qualitity_found =time.time()
        
        objectt_and_qualities=re.split(';',content)
        self.objecttt=objectt_and_qualities[0]
        # grab object from database
        self.previous_problem_list_dictionary=copy.deepcopy(self.problem_list_dictionary)

        self.cur.execute(f"""SELECT * FROM problem_table WHERE specific_problem_or_object='{self.objecttt}';""")
        object_entry= self.cur.fetchall()
        
        for numm, objectt1 in enumerate(object_entry):
                intital_time_for_object=objectt1[7]
                specfic_object=objectt1[2]
                print('hi')
                self.problem_list_dictionary[specfic_object]=[intital_time_for_object]
                #specfic_object=problem_entry[2]
                tool_or_question_used=objectt1[3]
                qual_list=objectt1[4]
                timme=objectt1[6]
                timme=re.split(",",timme[1:-1])
                qual_list=re.split(",",qual_list[1:-1])
                tool_or_question_used=re.split(",",tool_or_question_used[1:-1])
                for tooll,quall,timm in zip(tool_or_question_used,qual_list,timme):
                    self.problem_list_dictionary[specfic_object].append([tooll,quall,timm])
                continue 
        #print(self.problem_list_dictionary)
        self.upload_and_download_problem_dictionary()
    
     
    def access_old_object_to_add_further_qualtites(self,event):
         """ click . for this starting adding qualtites to a previous object when you get new ideas to add to this part of the galaxy """
         import re
         import time
         import copy
         content=self.text_box0.get('1.0', 'end')
         self.listbox1.delete(0, tk.END)
         print(content)
         time_qualitity_found =time.time()
         self.previous_problem_list_dictionary=copy.deepcopy(self.problem_list_dictionary)
         if ";" in content:
             objectt_and_qualities=re.split(';',content)
             objectt=objectt_and_qualities[0]
             self.current_object_or_problem=objectt
             qualities_list=re.split('=',objectt_and_qualities[1])
             print(qualities_list)
             for quality in qualities_list:
                 self.problem_list_dictionary[objectt].append([self.recorded_question_or_tool,quality,time_qualitity_found]) 
             print(self.problem_list_dictionary)
             self.upload_and_download_problem_dictionary()
         
   
    
    
    
        
    
    def delete_from_listbox(self, event):
         """ click delete in the current conencted objects listbox and delete from the sql database that variable and in the problem dictionary"""
         # this is still not working
         #step 0 add to listbox
         # maybe only use this on crappy objects then
         # what is another way i can delete stuff from sql
         import re
         import copy
         content=window.selection_get()
         content= re.sub('\d+','',content) 
         #content2=content[:-1]
         print()
         objectt_and_qualities=re.split(';',content)
         objecttt=objectt_and_qualities[0][1:]
         print(objecttt)
         self.previous_problem_list_dictionary=copy.deepcopy(self.problem_list_dictionary)
         for key in self.problem_list_dictionary.keys():
             print(key)
         del self.problem_list_dictionary[objecttt] 
         # need to fix this but can leave it a bit broken because don't really need to delete
         # even though it is cleaner
         self.cur.execute( f""" DELETE FROM problem_table
                          WHERE specific_problem_or_object = '{str(objecttt)}';""")
         # need to make this only delete the first one
         # need to only eli
         #reupload problem dictionary
         self.upload_and_download_problem_dictionary()
         
  
    def find_any_other_words_we_could_add_to_better_define_problem(self):
        """ """
        # develop method to do this
        # can implement this as one of our first methods
        # quesiton you ask determines the answer
        # how do we not miss any words so our web is most accurate
    def start_label_ideas_again(self):
        """ need to label ideas so i can start using them and implementing them into method"""
 
    def put_into_schedule_methods(self):
        """ """
        #Methods would be scheduled into calendar so when performing task 
        #like a meeting or public speaking or exercising or work or coding would automatically open. 
    def automate_input_structure_of_what_method_prompt_looks_like(self):
        """ when opening method window put example of how to create a method in the lower left textbox"""
    def fix_duplicates_in_existing_objects(self):
        """ """
        

        
    def upload_to_web_search_result_for_problem(self, event):
        """ this function will get results from various search browsers and then upload them to """
        # imprvoe later maybe add in divider thing
        # need to make htis faster
        def retreive_problem_data_from_web():
            import re
            import requests
            import pickle
            from selenium import webdriver
            from bs4 import BeautifulSoup
            from selenium.webdriver.common.by import By
            from selenium.webdriver.common.keys import Keys
            import time
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            links_of_dif_docs=[]
            saved_link_list=[]
            saved_text_from_website_list=[]
            link = r"https://html.duckduckgo.com/html/"
            striped_problem=self.problem_recorded.strip()
            problem_to_search_for=re.sub(r"\?","",striped_problem)
            print(problem_to_search_for)
            #striped_problem=problem_recorded.strip()
            #problem_to_search_for=re.sub(r"\?","",striped_problem)
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            driver= webdriver.Firefox(options=firefox_options)
            #driver= webdriver.Firefox()
            session = requests.Session()
            headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
            'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
            'Accept':'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/webp,*/*;q=0.8'}

            driver.get(link) #the pages link must be inserted here
            content = driver.find_element(By.CLASS_NAME, 'search__input')
            content.send_keys(f"{problem_to_search_for}")
            content.send_keys(Keys.ENTER)
            time.sleep(2)
            #print(content)
            html= driver.execute_script("return document.documentElement.outerHTML")
            sel_soup = BeautifulSoup(html, 'html.parser')
            links_of_dif_docs= sel_soup.findAll("a") 
            #print(links_of_dif_docs)
            if links_of_dif_docs:
                #print('hi')
                for link_found in links_of_dif_docs:
                    try:
                        if link_found:
                            final_link=link_found.get('href')
                            if final_link not in saved_link_list:
                                #print(final_link)
                                if final_link:
                                    if "https" in final_link:
                                        saved_link_list.append(final_link)
                                    else:
                                        continue
                    except:
                        continue
                    
                for link_finals in saved_link_list:
                    try:
                        req = session.get(link_finals, headers=headers)
                        soup = BeautifulSoup(req.text)
                        p_tag_text=soup.get_text()
                        #print(p_tag_text)
                        saved_text_from_website_list.append(str(p_tag_text))
                    
                    except:
                        continue
                driver.quit()
                return saved_text_from_website_list
        # process text throw out trash vs non trash
        # divide using sentnece non sentence
        # reuse processing text from project
        # reuse from business class
        def pre_process_text(saved_text_from_website):
            """ what is needed to reduce the size and make the text consistent before it goes in the network"""
            import re
            import unicodedata
            """ remove extra spacing, names, tabs, and other unwanted values"""
            website_data= re.sub("\n"," ", saved_text_from_website)
            website_data= re.sub("\t"," ", website_data)
            website_data= re.sub("\r"," ", website_data)
            website_data=re.sub(r" \s+", r" ", website_data)
            website_data= re.sub(r"\\x\S+",r" ",website_data )
            website_data= re.sub(r"@", "",website_data)

            website_data= unicodedata.normalize("NFKD",website_data)
            return website_data
            # repeat for law_document
        def divide_text_into_sentences(website_data):
            """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
            from nltk.tokenize import sent_tokenize
            # can add neural network here when i feel more comfortable
            # divide into sentence non sentence here
            import re
            index_used_list=[]
            self.sentences=[]
            final_sentence_list=[]
            find_word_pattern = re.compile(r"\w+")
            #from nltk.tokenize import word_tokenize
            modifying_sentences = sent_tokenize(website_data)
            for i7, sentence_15 in enumerate(modifying_sentences):
                words_in_current_sentence=find_word_pattern.findall(sentence_15)
                if len(words_in_current_sentence)<4: 
                    print(sentence_15)
                    continue
                if len(words_in_current_sentence)>60: 
                    print(sentence_15)
                    continue
                if "https" in sentence_15:
                    print(sentence_15)
                    continue
                else:
                    final_sentence_list.append(sentence_15)
            return final_sentence_list
        def add_sentences_to_list_box(final_sentence_list):
            """ add the modified list of sentences into the listbox to get ideas for the problem from"""
            # how am i going to deal with this listbox deleting so that it keeps all the text in
            #self.listbox5.delete(1, tk.END)
            for i9, objecttt in enumerate(final_sentence_list):
                self.listbox5.insert(tk.END, f"{i9}:{objecttt}")

        saved_text_from_website_list=retreive_problem_data_from_web()
        for text in saved_text_from_website_list:
            single_website_text=pre_process_text(text)
            final_sentence_list=divide_text_into_sentences(single_website_text)
            add_sentences_to_list_box(final_sentence_list)
        # need to incorporate web results into sql
        
    def display_problem_web_and_problem_tree_methods_tools_questions_when_solving_problem(self,event):
        """make problem tree and problem  web clickable 
        make problem web into chess board think edward snowden surveillnce how goverment set up there stuff
        suggest different simialr problems using database search
        display methods related to problem and possible methods
        when open problem solving program open life dag and problem web empty file
        have button to change to specific problem"""
        
        
        
        #open 
    # add a trigger to when you select problem
    # either from program or graphic
        
        # TAKE ADVANTAGVE OF WHAT YOU HAVE BUILT
        # so show problem web and problem tree have graphics displayed
        # on other screen while working so can reference them
        #to help you solve problems
        # life dag
        # problem dag
        # sub problem dag
        # all can be displayed
        # how to get this to work in database
        # next question !!!
        # make problem web like a chess board
        # have it open problem web whenever we are using that problem
        # and have it open problem tree when solving the problem
        # and overall problem trees that the problem falls into
        # 
        #TRY TO UPLOAD EVERYTHING I WRITE TO PROIBLEM SOLVING PROGRAM
        #so is data i can use later
    def navigate_life_problem_tree_using_tkinyer(self):
        """
        life dag diagram like a button for back
        file system like press 1 to go down to lower action in life problem tree in strat have option to go back        
        when sleect specific problem then will display and generate
        blender graphics
        blender graphic of  problem envrionment
        blender graphic of possible problem trees
        store list of actions
        expand text on click
        tkinyer listbox
        """
        #step 1
        #step 2
        #step 3
        #step 4
        #step 5

    def set_up_data_strcture_for_life_problem_tree_in_database(self):
        """
        
        """
    def create_strategy_table_and_problem_tree_table(self):
        """ """
        
        
    def add_end_state_to_problem_table_and_method_table(self):
        """ this way can properly create problem tree dag
        and get database ready for problem tree dags
        match end states to changed problem envrionemtn
        in order to connect the problem tree to problem envrionments"""
        # when transferring sql e use these commands from computers
        
    def create_problem_tree_graphic_blender(self):
         """use a program to make this clickable and reload from database based on given problem
         # start at life problem tree and drill down
         have all possible problems being displayed you can solve and first click leads to methods
         blender would make it more fun to look at graphic so use this and skills transferable
         create life problem tree
         add endstate in here"""
         #open to blender network 
         # design blender network
         # show problem tree graphic on problem environment
         # like show in red all dots effected by actions
         # if you use a specific problem tree or strategy
         #interactive site for solving your problems
         #could jump to try different solutions
         
         
    def create_better_problem_web_graphic_blender(self):
        """ create web that is like a chess board or a videogame think goverment snowden level detail on info on people assuming its legal
        use blender and animations to make this more fun to look at
        think like a minecraft world or video game
        use blender for network design
        make it so this graphic can change etc
        basically modles problem envrionment so can see alternative and effects
        create an animation for effects
        view endstate  of environment using a strategy"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
    def upload_everything_to_problem_sovling_program(self):
        """when writing anythign down in word find way to do this in problem solving program instead """
        
    def change_methods_to_make_them_more_usable(self):
        """ need to make it so ia ctually use all the methods ive been creating and make them more readable
        think of things you read like graphics and are memorable and make strats like this"""


        
        
        
        
        
        
        
    def save_web_results_want_to_use_for_method_steps(self):
        """ put these in some sort of lsit so i can access it later when developing method steps """
        
    def all_problems_tasks_could_solve_in_life_minize_unknowns_part_0(self):
        """ list all the actions and problems could solve and list all the effects of solutions in your life"""
        # THIS IS STEP 0
        # this is the known and unkknown problem part of the diagram in life diagram
        # have all problems ever known and minimize unknown could solve and intended effects or endstate of solving probelm
        # or trying to solve problem and unknown effects
        #write in problem or end state when creating a problem
        
        

        # then have inside these problems solutions with the store problem end state and step tree
        # and with problem envrionment and proper methods for each problem with strategies
        #use effects to determine best problems to solve find way to find effects of problems
        #Peeling back the onion put this in a method for creating problems to solve and find more
        #and more valuable problems peeling back the idea of how # for ranking ideas effects
        #You don’t know what you don’t know so this would hsow you all the things you could do
        # and use effects to determine best strategies to use to get to end goal and complete or solve problem or tasks
        # best decision for problem to solve  are subjectives so just have to look at effects
        # reduce unknown problems to solve to zero search for unknowns
        # step 0 choose which problem to solve
        # step 1 create web for problem
        # step 2 create tree for problem to end states/effects goals wanted or other stratgies that will likely 
        # prorduce certain effects
        # make this a box to start off a problem 
        # make it so all problems are displayed with there intended effects of solving/end states
        # when i click the list_problems method
        # require me to state a effect or end state by solving a rpoblem when upload problem?
    def create_problem_web_part_1(self): # this is good
        """ """
        # information on each variable in the problem and connections between variables and broader area of knowledge
        # and eixsting knowledge around each variable is the goal
    
    def create_problem_tree_of_strategies_and_endstates_and_steps_in_a_tree_part_2(self):# button?
        """ be able to write in a problem during a day and traverse dictionary to add sub problem and actions in between"""
        # trying to prgoram the tree in this part of the function and program
        # basically expand existing way we do strategies and actions and make it a viewable tree with effects etc
        
        
        
        #first is problem list of problems you cna choose to solve tab to choose from and write a problem into
        # second is writign in the end state and accessing problem
        # third is preparing strategies for the problem
        # maybe add a button  to insert the end state/effects or outcome wanted into database when first writing in a problem I THINK THSI IS KEY
        # how do i incorporate currently what i have into this short hand
        # where i write the pseudocode strategy to get to end state
        # maybe keep in existing framework but add this tree to the strategy part of problem sovling rpcoess
        # when starting 
        # short hand problem environment 
        # have little window to do this and keeps track of the tree of the problem you are solving
        # for broader strategies use proper problem solving program
        # be able to add to the actions and recourse stating steps to get to a end state for an action
        # make it viewable in some sort of tree format
        # can have multiple end states 
        # multiple different strategies to try to reach the same goal
        #to really under informaiton like need a graph same with a rpoblem to under problem and 
        #how solve need a tree and the differnt strategies or paths you can take
        
        #when building problem solving ttree program to view the problem we are solving and all the sub problems
        #and steps that have devleoped to solve it i need to do this and create a visual
        #the root being orignal problem the end state we want for that the sub steps to get there
        #and the there intedned end states and sub problems if applicable for this tree find way to store steps 
        #maybe could build life idea on top of this
        # move the resutls to sub_methods lsitbox maybe
        #store in database single problem
        #the actions in the strategy you take to get from rproblem to end state may be sub problems
        #that you need strategies and actions to solve as well
        #we need to create the data to then upload to solve the sub problem
        #of uploading the correct issues and facts
        # have the ability to upload multiple different strategies
        #once defined the problem and effect outline variables and then set out your pseudocode or strategy(s) 
        #on how you plan to reach your end state the more variables you define and tools you consider 
        #more options you have and more words you use to define the problem easier it is to
        #find tools and variables because more context and can grow web faster
        #write down sub problems as you code solve them and then reference back to orignal problem
        #once have solved all the sub problems that manifest within it and get have multiple layers
        #need to add this to coding method and make a tree as you go down solving each sub problem or bug in the code
        #add a button to the problem window where you can store the hierarchy of problems that you
        #have solved with that day which you can refer to later which is stored in the database under date which
        #you reference back to later
        #think of all the things you could use do a pseudo or lightweight version of problem solving program
        #in this case consider all the different possible variables or coding things you could do to upload the files
        #like using a pickle or a csv or using a python script directly and write these different possible 
        #tools/variables down and then write down different strategies to apply them to solving the problem this
        #is a strategy I should use when solving coding problems and problems more broadly that don’t require me to build 
        #a complete method for them basically process is define problem define desired outcome or end state set 
        #out tools could use to solve problem in case of coding all the coding  variables involved like pickle
        #csv python script among others and then think f ways could apply these through transformations 
        #to solve the problem we call these strategies
        #Refer to past solutions later for guidance on how you might solve future problems or
        #construct future strategies maybe make it automatically suggest a step by step solution
        #we must also conisder the effects of different strategies An expert solution is a strategy
        #that uses variables in a smarter way to get to a  more efficient solution because the effects are better
        #to an alternative solution;s#27[s] 



        
    def find_ways_to_work_with_web_results_easier(self):
        """ """
        # so we can add them as just actions or strategies
        
        

    def add_in_button_functions(self):
        """  """
        #for retriveal
        # will need to save sub method in a particular way
        
    def identify_problem_with_current_approach(self):
        """ """
        # identify approach
        #build into method steps to solve these problems.
        
    def grab_key_words_from_problem_and_add_them_as_qualtites(self):
        """ """
        
    def show_steps_in_sub_method(self,event):
        """ when clicking 1 in submethod window will show the sub steps of a particualr sub-method"""
        #leaving thename of submethod at the top and rest of to copy if needed into the method or 
        # need to save sub-methods in special way in idea database to be able to do this
    def build_neural_network_to_label_idea(self):
        """ """
        # reuse code when working on revamping website to make it work
    def create_pop_up_for_when_idea_successfully_added_to_database(self):
        """pop up to know the idea worked so i don't need to check it everytime """
        
    def labeling_ideas(self):
        """ upload ideas to label them and to transport them into window where i can work with them """
        # need to access the previous idea database and label the ideas into categories until i have enough
        #data to create a neural network to do this
        # maybe insert these into sub method box to work with these ideas and continue to label them
        # selecting sub method box is stored in causes other function which displays the things to label
        
    def nearest_defintion_to_phrase_used_in_web(self):
         """ """
         #Find nearest definition if not a word used in web like a phrase used instead
         #see if it could fit in for it based upon used in dictionary 
         # BRILLIANT IDEA this way only words in web
         
    
        
    def revert_back_to_show_all_sub_methods(self,event):
        """ when clicked relist all the relevent sub-methods whether for conn window or method window"""
        # add as one of the buttons under the sub method listbox
    def list_possible_actions_on_objects(self):
        """ """
    def expected_effects_or_alternatives_to_an_actions(self):
        """ outoine the effects or alternative there might be to taking a certain action"""
    def produce_easier_way_to_access_completed_methods(self):
        """ produce simple web app on phone to access these methods and integrate in calender"""
    def create_search_function_for_list_box(self):
        """help to find object or questions in the listbox """
    def rename_strategy_to_reflect_use_reorder_strategy(self):
        """ """
    def look_for_key_subjects_in_websearch_results_these_will_be_objects(self):
        """need to build function to automcially create objects from web search results using object of sentences found because of context """
    def make_it_easier_to_view_and_work_with_objects_and_questions_less_scrolling(self):
        """keep on scrolling to find things in objects need to find solution to this """
        # what are other ways i can save time when solving a probelm
    def make_methods_easier_to_edit_and_to_access_and_view(self):
        """ """
    def pre_generate_words_around_problem_to_add(self):
        """ """ 
        #automatically add them just not fill in there qualitites
        # find way to get qualtites automatically
    def web_not_generating_for_one_method_figure_out_why(self):
        """ fix web generation"""
    
    def make_easier_to_access_specific_steps_to_methods_i_think_i_could_add_to_current_method(self):
        """ make it so that when i am building a method and the steps i can more easily select steps from other methods in the window"""
        # like previous objects
        # make them more viewable 
    
   
    def make_it_easier_to_determine_number_value_of_items_in_web_for_quick_key(self):
        """ """
        # need to modify how items shown putting numbers at beginning of each row
        # and putting numbers ahead of each qualtiity
    def put_into_schedule_methods(self):
        """ """
        #step 0 grab method strategy and action
        #step 1 build api to send information figure out how to do this
        #step 2  build a 
        
        #Methods would be scheduled into calendar so when performing task 
        #like a meeting or public speaking or exercising or work or coding would automatically open. 
    def figure_out_how_to_best_format_and_create_methods_and_access_methods(self):
        """create and access methods """
    
        
    def scrap_galaxy_table_just_use_problem_table(self):
        """ need to replace uploading stuff for existing objects from current problem webbs"""
        # currently its not updating correctly
    
    def function_for_each_question_or_tool_automate_these(self):
        """ """
        #create. a function for each question or tool used like a function
        #to add all words in the problem as qualities and then get there defintions and extract nouns as qualtiries
        #   becayse questions will have a determijsitic outcome question determines the answer
    def find_a_way_to_scroll_list_box_to_see_all_questions(self):
        """ """
    def need_to_get_rid_of_number_sign_when_making_method_step(self):
        """ """
    def build_calender_build_in_for_actions_with_time(self,event):
        """ update calender to use methods at different times opening them up on phone or compouter """
        # when a task i want to or plan to complete it that day have the program
        # open the steps or a window to complete that method
        # need to learn a bit of shell here
        # better to encourage
    def display_sub_method(self):
         """select a submethod from the submethod window and display its steps of questions or tools to use to form conn or come up with a step or steps """
         #display it in the submethod listbox
    def sort_in_order_the_dictionary_inserted_into_methods_viewing_box(self):
         """ need to add a function to view the methods steps in order"""
 
    def edit_or_remove_steps_from_method(self):
         """ """
    def choose_combiniation_of_strategy_action_to_use(self):
         """ final nerual network chosing which actions or strategies shoudl go together"""
         # maybe have option to add this to your calender
         # choose which actions or strategies you want to use in combinaiton 
         #weighing pros and cons, consider the effects consider the alternatives
         # final neural netowrk and adding them to calender
         # or finding other ways to access them when i might use them maybe
         # like a notes file open on start up to easily access them
    def build_in_function_to_auto_update_when_labeling(self):
        """ """
        # update the questions i add so i can use them when building connections or my method
    def improve_websearch_to_include_academic_journals(self):
        """ academic journals probably have better knowledge"""
    def backup_database_to_stuff_drive(self):
        """ so not all data is lost """
        # try to automate this for later
    def automate_qualities_of_this_thing_question(self):
        """ automatically grab dicitonary defintion and add the question used as qualtites of this thing"""
        # eventually automate all questions lookiing at their transformations and the things they produce given the word used

    def need_to_find_a_better_way_to_engage_with_qualtities(self):
        """ maybe automarically make them blank objects to add to once i add them as qualtites so save time"""
        # put these objects in a lower positon in the list though so we can see the real ones we have put thought into
    def figure_out_a_sweet_spot_for_number_of_qualtites_to_making_viewing_web_easier(self):
        """ build some sort of function to remind me when building a object i am addingt o many qualtites can should move on """
        # maybe limit it to like 10
    def change_objectives_window_to_effects_window_and_build_shortcut_for_effectives_in_text_box(self):
        """ build this is in as soon as possilbe """
    def build_something_in_to_prevent_deleting_objects_accdientally_in_conn_window(self):
        """ keep deleting objects and wasting my time from a web need to keep these """
    def make_problem_not_erase_from_top_listbox(self):
        """when i'm building my method the problem keeps erasing from top listbox make it stop doing that """
    def make_easier_to_access_past_methods(self):
        """currently once i have a method step completed don't know whats in it need to make it easier to see this """
    def make_easier_to_use_problem_web_or_change_process(self):
        """ """
        
        #### DO THIS NEXT BELOW AUTOMATE WHOLE PROCESS AND MAKE SURE TO RECORD DATA FOR NEURAL NETWORK
    def make_problem_word_seperation_stage_automatic_and_qualtities_make_web_search_stage_automatic(self):
        """ """
        #green washing
        #how can i do this better, what am i doing here at this stage of working with web results
        # need to consider bi grame and tri grams here and grab nouns or idenitfy what words in the sentence i am grabbing
        #wha tis the part of speech i keep turning into objects and what are the parts of speech i am turning into qualtities
        #then how can i automate this
        #when breaking apart the results and elimainting oens that dont work
        #how am i going to record the differences that I make
        # look to past objects for suggestions on qualitites
        #do the same thing with notes
        # goal is to reproduce existing solutions i have made
        # need to find a way to record good existing solutions
        
        # goal is to make the web as large as possible for most possible vatirables but not too large
        #where you have completely useless stuff or stuff that might throw off what actions you are creating
        # is there a better way to do the web stage here
        # web search is limiting need to consider other way of doing this that might yield a better result
        # create some objects you always connect to the problem regardless depending like perspective ones, like certain questions you always ask
        # the results of certain questions could be things that you always add
        # connect some objects only if intital qualtites in web
        
    def create_way_to_show_overall_effect_wanted_from_solving_problem(self):
        """create a way to both store and view the overall effect related to a given problem""" 
        
    def next_automate_the_questions_stage_of_building_web(self):
        """ after done with web results automate the questioning stage to produce more variables with tools and questions"""
        # should we just do gpt model try everything and see what sticks in first stage
        #
    def automate_creation_of_building_strats_with_web_objects_and_questions_and_tools(self):
        """build neural network to take web and produce possible strategies and action """
        # record transformation performed when using a given question and varible used and try to create
        # something that can do the same 
    def automate_creation_of_effects_or_objectives(self):
        """ automate the create of what effects we intend an action to have"""
        #we will use effects to determine which actions we should take to combat a certain problem
        #Cost benefit analysis: determine a set of weighting factors for benefits
        #and a set of weighing factors for risks. 
        #Look at examples of approaches in the past
        #that have maxmized benefits 
        # each action should have its own expected effects
        # therefore need to add this in and put this into the database when creating data
        # use to create legislation or take any action for solving any problem
        # all the variables invovled and there qualtities
    def feed_method_strategies_into_calender(self):
        """ """
    def automate_paper_review_summarize(self):
        """ for new paper review on AI and carbon capture run them through model to make them easier, create database for this"""
        # web spider to find up to date journals
        # set up automated scraping for key paper sites and then summarize papers
        # still need to learn the math to implement papers
        # eventually pipeline to implement papers automatically in part
        # https://arxiv.org/list/cs.AI/recent
        # https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=34
        # may need to update list every once in a while
        #https://ietresearch.onlinelibrary.wiley.com/journal/17519640
    def automate_conference_grab_info(self):
        """ for main fields working in carbon capture,AI"""
        # make a list of all conferecnes on ai
        # update list with web spider
        #attend as many of these as you can to see new ideas in the field
        
    def figure_out_other_areas_that_might_be_useful_to_track_in_the_field(self):
        """ """
    def automate_grant_finder_and_writer(self):
        """ """
    def build_platform_for_transforming_idea_into_summarized_format(self):
        """ """
        # use other computer for web spider
        # need to buy a wifi card for both main computer and smaller computers
        #regularizing all the data
        # always ask how can i do htis more efficently and faster
    
        
        
    def change_selected_problem(self,event):
        """  press 4 in the submethods listbox to set the given content as the recorded problem"""
        content=window.selection_get()
        self.problem_recorded=content
        self.upload_and_process_problem_table_data_for_specific_problem()
        # need to still edit some stuff here
        
    
    
    def revert_back_to_show_previous_methods_to_reuse_to_add_to_method(self,event):
        """ make the elements appear in the listbox with other method steps and actions so i don't repeat them """
        import re
        problem_dictionary={}
        self.cur.execute(f"""SELECT problem_being_solved,method_step, strategy_action  FROM methods_table ;""")
        all_idea_in_database_list_format= self.cur.fetchall()
        for idea9 in all_idea_in_database_list_format: 
            problem_being_solved=idea9[0]
            method_step_info=idea9[1]
            strategy_action_info=idea9[2]
            if  problem_dictionary.get(problem_being_solved):
                print('key exists')
            else:
                problem_dictionary[problem_being_solved]=[]# values of the strategies and actions in one giant list
                # add in ideas
            problem_dictionary[problem_being_solved].append(method_step_info)
            if strategy_action_info:
                actions_found=re.split(",",strategy_action_info)
                for actionss in actions_found:
                    problem_dictionary[problem_being_solved].append(actionss)
                
        self.listboxsub_method.delete(0, tk.END)

        for i3, (problemmm, strat_act_list) in enumerate(problem_dictionary.items()):
            strat_act_list=re.sub(r"[\'\[\]?]","",str(strat_act_list))
            problem_list_to_add=problemmm + ";" + strat_act_list
            problem_list_to_add=problem_list_to_add[2:-2]
            self.listboxsub_method.insert(tk.END, f"{i3}:{problem_list_to_add}")

           


    def upload_ideas(self,event):
        """ inserts into listboxsubmethod """
        import re
      # get all database of ideas sentences and paragraphs, maybe paste paragraph in top right box
      # need names of everything to do this like textboxs, database name and then perform transformations and possible actions
        #self.text_box2 # paste pa
        #self.text_box01 # paste paragraph and clear first
        edited_ideas_list=[]
        self.listboxsub_method.delete(0, tk.END)
        self.cur.execute(f"""SELECT * FROM labels_for_idea_program_2 ;""")
        idea_entries= self.cur.fetchall()
        idea_entries=list(idea_entries)
        self.cur.execute( f""" SELECT * FROM ideas_table_3;""")
        search_result_from_new_database= self.cur.fetchall()
        for ideass in search_result_from_new_database:
            # grab edited sentences
            edited_ideas_list.append(ideass[1])
        for i9, objecttt in enumerate(idea_entries):
            sentence= objecttt[1]
            if sentence in edited_ideas_list:
                print(sentence)
                continue
            self.listboxsub_method.insert(tk.END, f"{i9}:{sentence}")
        # need to edit transport idea to idea editing window
        # print self.object_list
        
  
  
    def starcraft_hotkey_method_textbox(self,event):# this for strategy_action
        """ quick access to the various listboxs in the method window"""
        import re
        r_found=False
        list_of_listboxes={1:self.listbox1,2:self.listbox2,3: self.listbox3, 4:self.listbox4, 6:self.listbox5,  5:self.listboxsub_method}
        list_of_listboxes_box={self.listbox1:1,self.listbox2:2, self.listbox3:3, self.listbox4:4, self.listbox5:6,  self.listboxsub_method:5}
        modified_text=self.text_box1.get('1.0', 'end')
        numbers_search_list=re.search(r"\d\d[^\[].*",modified_text).group(0)
        #r"\d\d.*"
        
        print(numbers_search_list)
        modified_text=str(modified_text).split(numbers_search_list)
        listbox_number=int(numbers_search_list[0])
        listbox_name=list_of_listboxes[listbox_number]
        list_box_content=listbox_name.get(0, tk.END)
        numbers_search_list2=numbers_search_list[1:]
        if "r" in numbers_search_list2:
            r_found=True
        #print(list_box_content)
        numbers_search_list2=numbers_search_list2.replace("r","")
        print(numbers_search_list)
        # need to fix root finding
        if listbox_number== list_of_listboxes_box[self.listbox1]: # objects and  DONE
            numbers_search_list2=numbers_search_list2.split(",")
            listbox_item_number=int(numbers_search_list2[0])
            quality_in_listbox_number= int(numbers_search_list2[1])
            objectt_and_qualities=re.split(';',list_box_content[listbox_item_number])
            objecttt=objectt_and_qualities[0]
            qualities_list=re.split(',',objectt_and_qualities[1])
            seelect_specific_qualities= qualities_list[quality_in_listbox_number]
            if r_found == True:
                seelect_specific_qualities=objecttt
                seelect_specific_qualities=re.sub(r"\d*:","",seelect_specific_qualities)
                # r being getting the object
            modified_text= modified_text[0] +" " + seelect_specific_qualities.strip()
            seelect_specific_qualities=re.sub("\n","", seelect_specific_qualities)
            self.ideas_list_for_method.append(seelect_specific_qualities)
            print(self.ideas_list_for_method)
           
        if listbox_number== list_of_listboxes_box[self.listbox2]: # need to redo this one maybe not upload method
           print('still need to deal with this')
        if listbox_number== list_of_listboxes_box[self.listbox3] or listbox_number== list_of_listboxes_box[self.listbox4]: # questions and tool
            # differeny operation here
            listbox_item_number=int(numbers_search_list2)
            list_box_itemm=list_box_content[listbox_item_number]
            list_box_itemm= re.sub('\d+:','',list_box_itemm) 
            self.recorded_question_or_tool=list_box_itemm 
            self.recorded_question_or_tool=re.sub("\n","", self.recorded_question_or_tool)
            self.recorded_question_or_tool_for_method_list.append(self.recorded_question_or_tool)
            print(self.recorded_question_or_tool_for_method_list)
            modified_text=modified_text[0].strip()

        if listbox_number== list_of_listboxes_box[self.listboxsub_method]:  # this will include the sub-method so may have to add additonal functionality
            # add to the 
            print(list_box_content)

            numbers_search_list2=numbers_search_list2.split(",")
            listbox_item_number=int(numbers_search_list2[0])
            quality_in_listbox_number= int(numbers_search_list2[1])
            objectt_and_qualities=re.split(';',list_box_content[listbox_item_number])
            objecttt=objectt_and_qualities[0]
            qualities_list=re.split(',',objectt_and_qualities[1])
            seelect_specific_qualities= qualities_list[quality_in_listbox_number]
            if r_found == True:
                seelect_specific_qualities=objecttt
                seelect_specific_qualities=re.sub(r"\d*:","",seelect_specific_qualities)
                # r being getting the object   
            modified_text= modified_text[0] +" " + seelect_specific_qualities.strip()
            seelect_specific_qualities=re.sub("\n","", seelect_specific_qualities)
            # add problem here to a stored string called past problem connection
            self.past_problemm=objecttt
            # now i need to add to this thing that force it to display the submethod action and strategies
            def upload_previous_problem_to_view_method_steps():
                """ this puts in the submethod listbox the previous problem that I have included in the problem i am working on"""   
                method_step_name_dic={}
                action_step_name_dic={}
                final_method_list=[]
                final_action_list=[]
                final_value_order_list=[]
                self.listboxsub_method.delete(0, tk.END)
                problem_to_search_for=objecttt.strip()
                problem_to_search_for=re.sub(r"\d+:","",problem_to_search_for)
                problem_to_search_for="??"+ problem_to_search_for
                print(problem_to_search_for)
                self.cur.execute(f"""SELECT * FROM methods_table WHERE problem_being_solved = '{problem_to_search_for}' ;""")
                methods_worked_on= self.cur.fetchall()
                method_list_str=""
                for  method_object in methods_worked_on:
                    method_step_name=method_object[2]
                    step_number=method_object[6]
                    step_number=re.sub(r"\n","",step_number)
                    step_number=int(step_number)
                    actions_for_step=method_object[8]
                    if actions_for_step:
                        actions_for_step=re.sub("[\[\]{}]","",actions_for_step)
                        actions_for_step=re.split(",",actions_for_step)
                    action_or_strategy_label=method_object[9]
                    print(action_or_strategy_label)
                    #print('meow')
                    action_step_name_dic[step_number]=[]
                    method_step_name_dic[step_number]=[]
                    
                    if action_or_strategy_label=="[action]" :
                        action_step_name_dic[step_number].append(method_step_name)
                        if actions_for_step:
                            action_step_name_dic[step_number].append(actions_for_step)
                            continue 
                        continue
                    else:
                        
                        method_step_name_dic[step_number].append(method_step_name)
                        #print(method_step_name_dic)
                        if actions_for_step:
                            action_step_name_dic[step_number].append(actions_for_step)
                            #print(method_step_name_dic)
                            continue
                        continue
                keys_list=action_step_name_dic.keys()
                max_value=max(keys_list)+1
                empty_action_list= [None] * max_value
                empty_method_list= [None] * max_value
                for ii1, (key, action) in enumerate(method_step_name_dic.items()):
                     keyyy=int(key)
                     empty_method_list[keyyy]=[keyyy, action]        
                for ii1, (key, action) in enumerate(action_step_name_dic.items()):
                     keyyy=int(key)
                     empty_action_list[keyyy]=[keyyy, action]
                if method_step_name_dic:
                    for methoddd in empty_method_list:
                        if methoddd==None:
                            continue
                        insert_value1=f"{methoddd[0]}: {methoddd[1]}"
                        insert_value1=re.sub("[\[\]{}\']","",insert_value1)
                        self.listboxsub_method.insert(tk.END, insert_value1) 
                if action_step_name_dic:
                    self.listboxsub_method.insert(tk.END, "Actions---------")    
                    
                    for actionn in empty_action_list:
                        if actionn==None:
                            continue
                        insert_value2=f"{actionn[0]}: {actionn[1]}"
                        insert_value2=re.sub("[\[\]{}\']","",insert_value2)
                        self.listboxsub_method.insert(tk.END, insert_value2)  
            print('submethod')
            upload_previous_problem_to_view_method_steps()
        if listbox_number== list_of_listboxes_box[self.listbox5]:  #objectives
            # add as an objective to the dictionary
            listbox_item_number=int(numbers_search_list2)
            list_box_itemm=list_box_content[listbox_item_number]
            list_box_itemm= re.sub('\d+:','',list_box_itemm) 
            recorded_objective=re.sub("\n","", list_box_itemm)
            self.objective_list_for_method.append(recorded_objective)
            print(self.objective_list_for_method)
            
            modified_text=modified_text[0].strip()
  
        self.text_box1.delete('1.0', 'end')
        self.text_box1.insert(tk.END,modified_text)


    def starcraft_hotkey_conn_textbox(self,event):
        """ quick access to the list boxes in the conn window"""
        # gotta fix how this operates so can type in step number value when making method
        # and it does not fuck up the thing
        import re
        r_found=False
        list_of_listboxes={1:self.listbox1,2:self.listbox2,3: self.listbox3, 4:self.listbox4, 6:self.listbox5,  5:self.listboxsub_method}
        list_of_listboxes_box={self.listbox1:1,self.listbox2:2, self.listbox3:3, self.listbox4:4, self.listbox5:6,  self.listboxsub_method:5}
        modified_text=self.text_box0.get('1.0', 'end')
        #numbers_search_list=re.search(r"\d\d.*",modified_text).group(0)
        numbers_search_list=re.search(r"\d\d[^\[].*",modified_text).group(0)
        #r"\d\d[^\[].*"
        modified_text=str(modified_text).split(numbers_search_list)
        # split everything up
        listbox_number=int(numbers_search_list[0])
        listbox_name=list_of_listboxes[listbox_number]
        list_box_content=listbox_name.get(0, tk.END)
        numbers_search_list2=numbers_search_list[1:]
        if "r" in numbers_search_list2:
            r_found=True
        numbers_search_list2=numbers_search_list2.replace("r","")
        print(list_box_content)
        print(numbers_search_list)
        if listbox_number== list_of_listboxes_box[self.listbox1] or listbox_number== list_of_listboxes_box[self.listbox2]:
            numbers_search_list2=numbers_search_list2.split(",")
            listbox_item_number=int(numbers_search_list2[0])
            quality_in_listbox_number= int(numbers_search_list2[1])
            objectt_and_qualities=re.split(';',list_box_content[listbox_item_number])
            objecttt=objectt_and_qualities[0]
            qualities_list=re.split(',',objectt_and_qualities[1])
            seelect_specific_qualities= qualities_list[quality_in_listbox_number]
            if r_found == True:
                seelect_specific_qualities=objecttt
                seelect_specific_qualities=re.sub(r"\d*:","",seelect_specific_qualities)
                # r being getting the object
            if len(modified_text[0]) ==0: # object
                modified_text=seelect_specific_qualities.strip()+";"
            else: # qualtity
                modified_text=modified_text[0]+ "="+ seelect_specific_qualities.strip()
        if listbox_number== list_of_listboxes_box[self.listbox3] or listbox_number== list_of_listboxes_box[self.listbox4]:
            listbox_item_number=int(numbers_search_list2)
            list_box_itemm=list_box_content[listbox_item_number]
            list_box_itemm= re.sub('\d+:','',list_box_itemm) 
            self.recorded_question_or_tool=list_box_itemm[:-1]  
            self.recorded_question_or_tool=re.sub("\n","", self.recorded_question_or_tool)
            modified_text=modified_text[0].strip()
            print(self.recorded_question_or_tool)  
        if listbox_number== list_of_listboxes_box[self.listboxsub_method]:  # this will include the sub-method so may have to add additonal functionality

            print('submethod') 
        if listbox_number== list_of_listboxes_box[self.listbox5]:  # web results when we get there
            print('web-search')
        self.text_box0.delete('1.0', 'end') 
        self.text_box0.insert(tk.END,modified_text)


        
        
    def erase_button_click_value(self):
         self.text_box0.delete(len(self.text_box0.get())-1,END, Tk.END)
         # still need to implement this
            
            # delete after the fact the  symbol we typed
        

    def divide_problem_into_pos_from_main_box(self, sentence):
        import en_core_web_trf
        nlp = en_core_web_trf.load()
        for i,idea in enumerate(all_idea_in_database_list_format):
            pos_unmodified_sentence = nlp(idea[5])
            temp_sentence_pos_list=[]
            
            for part_of_speech_parts in pos_unmodified_sentence:
                word_with_pos=[part_of_speech_parts,part_of_speech_parts.pos_]
                temp_sentence_pos_list.append(word_with_pos)

            all_idea_in_database_list_format[i].append(temp_sentence_pos_list)
       
        return all_idea_in_database_list_format
    def highlight_text(self):
        """ perform an operation on the text within the white box like highlighting or performing some function"""
        self.text_box.tag_add('red_fg', '1.0', 'end')
        self.text_box.tag_configure("red_fg", foreground="blue")
    def bring_idea_tool_or_problem_to_a_center_box_to_work_with(self,event):
        """ bring one of the items in a list to a center box to better see and perform trnasofmrations on or connect to"""
        #from ctypes import windll
        #import pyautogui
        import time
        #import pyperclip
        import copy
        import re 
        self.starting_time_idea=time.time()
        try: 
            content=window.selection_get()
            content= re.sub('\d+:','',content) 
            content2=content[:-1]
            self.text_box2.insert(tk.END, content2)
            #windll.user32.EmptyClipboard()
            global stored_copy_object  
            self.stored_copy_object=copy.deepcopy(content)
            self.carry_information_about_copied_text()
            #print(self.object_list)
        except Exception as e:
            print(e)
        # space before word and a space after considers it part of word
        # different center boxes will have different purposes and differnet functions available to each of them and different things you can do to the text
    def carry_information_about_copied_text(self,table_name= "labels_for_idea_program_2"):
        #print(self.stored_copy_object)
        print(self.stored_copy_object)
        self.cur.execute(f"""SELECT * FROM {table_name} WHERE sentence = '{self.stored_copy_object}';""")
        specific_entry= self.cur.fetchall()
        print(specific_entry)
        self.object_list=""
        for first_entry in specific_entry: 
            self.object_list=list(first_entry)
            break
        return self.object_list   
    def export_idea_to_new_table(self,event):
        """ export data to different tables  """
        # need to apparently use semi colon to mark entry here
        import re
        import time
        finish_time_idea=time.time()
        modified_text=self.text_box2.get('1.0', 'end')
        try:
            modified_text= re.sub("-", "", modified_text)
            updated_label_grouped= re.search("(\d+);",modified_text)
            updated_label=updated_label_grouped.group(1)
            updated_text_grouped = re.search("(\d+);(.*)",modified_text)
            updated_sentence=updated_text_grouped.group(2) 
            print(updated_label)
            print(updated_sentence)
        except Exception as e:
            print(e) 
        if "]" in updated_sentence:
            updated_sentence= re.sub("]", "", updated_sentence)
            self.cur.execute( f""" INSERT INTO ideas_table_3 (updated_label,updated_sentence)
                        VALUES ('{str(updated_label)}','{str(updated_sentence)}');""")
            self.conn.commit()
            return "from brain"

        idd=self.object_list[0]
        original_sentence=self.object_list[1]
        paragraph=self.object_list[2]
        paragraph_number=self.object_list[3]
        file_name=self.object_list[4]
        directory=self.object_list[5]
        pos=self.object_list[6]
        label=self.object_list[7]
        self.cur.execute( f""" INSERT INTO ideas_table_3 (id,sentence,paragraph,paragraph_number,file_name,directory,pos,labels,updated_label,updated_sentence,finish_time,start_time)
                    VALUES ('{str(idd)}','{original_sentence}','{paragraph}','{str(paragraph_number)}','{str(file_name)}','{str(directory)}','{str(pos)}','{str(label)}','{str(updated_label)}','{str(updated_sentence)}','{str(finish_time_idea)}','{str(self.starting_time_idea)}');""")
        self.conn.commit()
        self.text_box2.delete('1.0', 'end')

        
        return "from idea database"
    # bring it to that specfiic textbox from whereever 
    #edit it
    # and then when ready function to upload it
    # find way to record label
    def list_possble_problems(self,event):
        """ take problems from ideas_data_base and list them in the main text box to solve or reconfigure in bottom left textbox"""
        self.text_box.delete('1.0', 'end')
        list_of_problems=self.import_tools_problems_or_existing_ideas(7)
        for i3, problem in enumerate(list_of_problems):
            problem=problem[2:-3]
            self.text_box.insert(tk.END, f"{problem}\n")
    def import_problem(self,event):
        """ if getting problem from a list of problems I want to pick it from the list of problems and erase all the others"""
        # remove any numbers
        import time
        self.start_time_problem=time.time()
        contentt=window.selection_get()
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, f"{contentt}") 
        self.problem_recorded=contentt
        return ""
        # need to make a button to list possible problems in main textbox
    def record_problem_and_create_problem_dictionary(self,event):
        """ if we wrote the problem manually we will automically save it after a minute"""
        #look at top textbox and then 
        import time
        import re
        import subprocess
        import os
        from multiprocessing import Process


        self.start_problem_time=time.time()
        self.method_list_dictionary={}
        self.strategy_list=[]
        self.recorded_question_or_tool_for_method_list=[]
        self.objective_list_for_method=[]
        self.ideas_list_for_method=[]
        self.actions_for_method=[]
        self.strategy_or_method_label_for_methods=[]
        self.past_problemm=""
        # for tecording whole time it took to make conenctions for game like envrionment
        #program_start_time# if 2 minutes has passed and text in the problem window then save as problem_object
        #DO THIS if problem_dictionary_already_exists then 
        #save it before starting a new one
        self.problem_recorded=self.text_box.get('1.0', 'end')
        self.problem_recorded=re.sub('\n',"",self.problem_recorded)
        #print( self.problem_recorded)
        self.problem_recorded="?? "+ self.problem_recorded
        
        time_created =time.time()
        self.problem_list_dictionary={self.problem_recorded:[time_created]}
        #print(self.problem_list_dictionary)
        # this is the thing that makes sure that we can add qualtities to the project  
        import sys
        # Add your directory to the Python path
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
        #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
        # going to affect them when they age
        #from Problems_functions import problems_functions
        #from Problems_functions import methods_window_program
        from create_auto_create_problem_tree_and_web import create_auto_create_problem_tree_and_web
        #from problem_solving_project_gui_10 import buttons_per_quadrant
        #buttons=buttons_per_quadrant()
        auto_prob_web_tree=create_auto_create_problem_tree_and_web()
        process = Process(target=auto_prob_web_tree.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        process.start()
        print('hi')
        
        #subprocess.Popen(["cmd.exe","python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer\create_auto_problem_tree_and_web.py", self.problem_recorded ],  text=True)
   
        #automated_galaxy_dic=self.automatically_add_web_search_result_to_problem_web_and_transformations_list(self.problem_recorded)
        #self.auto_generate_and_problem_trees_from_problem_galaxy()
        
    ### AUTO GENERATE EFFECTS WEB AND TREE
    def generate_blender_effect_problem_web_for_strat_and_problem_tree(self,event):
        """ """
        import re
        from multiprocessing import Process
        import sys
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
        #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
        # going to affect them when they age
        #from Problems_functions import problems_functions
        #from Problems_functions import methods_window_program
        from generate_and_open_blender_problem_web_and_tree import generate_and_open_blender_problem_web_and_tree_functions
        #from problem_solving_project_gui_10 import buttons_per_quadrant
        #buttons=buttons_per_quadrant()
        self.strategy_recorded=window.selection_get()

        genn_blend_functions=generate_and_open_blender_problem_web_and_tree_functions()
        process = Process(target=genn_blend_functions.generate_blender_effect_problem_web_for_strat_and_problem_tree_f,args=(self.problem_recorded,self.strategy_recorded,))
        #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        process.start()
        
        
        

        
        #print('hi')
        #self.open_blender()
        #self.get_access_to_blender_terminal()
        #self.generate_blender_commands_problem_web(effects_web=True,methods_problem_recorded=self.problem_recorded,strategy_list=self.strategy_recorded_list)
        #self.execute_blender_command_list()
        
        # generate tree will modify tree to display mutliple levels next
        #self.open_blender()
        #self.get_access_to_blender_terminal()
        #self.generate_blender_commands_problem_tree_2()
        #self.execute_blender_command_list()
        
        
        
    ### AUTO GENERATE PROBLEM WEB FUNCTIONS 
    

        
    def retreive_problem_data_from_web(self,problemmm):
        import re
        import requests
        import pickle
        from selenium import webdriver
        from bs4 import BeautifulSoup
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import time
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        links_of_dif_docs=[]
        saved_link_list=[]
        saved_text_from_website_list=[]
        link = r"https://html.duckduckgo.com/html/"
        question_striped=problemmm.strip()
        question_to_search_for=re.sub(r"\?","",question_striped)
        print(question_to_search_for)

        #striped_problem=problem_recorded.strip()
        #problem_to_search_for=re.sub(r"\?","",striped_problem)
        firefox_options = FirefoxOptions()
        #firefox_options.headless = True
        driver= webdriver.Firefox(options=firefox_options)
        #driver= webdriver.Firefox()
        session = requests.Session()
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept':'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/webp,*/*;q=0.8'}

        driver.get(link) #the pages link must be inserted here
        content = driver.find_element(By.CLASS_NAME, 'search__input')
        content.send_keys(f"{question_to_search_for}")
        content.send_keys(Keys.ENTER)
        time.sleep(2)
        #print(content)
        html= driver.execute_script("return document.documentElement.outerHTML")
        sel_soup = BeautifulSoup(html, 'html.parser')
        links_of_dif_docs= sel_soup.findAll("a") 
        #print(links_of_dif_docs)
        if links_of_dif_docs:
            #print('hi')
            for link_found in links_of_dif_docs:
                try:
                    if link_found:
                        final_link=link_found.get('href')
                        if final_link not in saved_link_list:
                            #print(final_link)
                            if final_link:
                                if "https" in final_link:
                                    saved_link_list.append(final_link)
                                else:
                                    continue
                except:
                    continue
                
            for link_finals in saved_link_list:
                try:
                    req = session.get(link_finals, headers=headers)
                    soup = BeautifulSoup(req.text)
                    p_tag_text=soup.get_text()
                    #print(p_tag_text)
                    saved_text_from_website_list.append(str(p_tag_text))
                
                except:
                    continue
            #driver.quit()
            return saved_text_from_website_list
    # process text throw out trash vs non trash
    # divide using sentnece non sentence
    # reuse processing text from project
    # reuse from business class
    
    def pre_process_text(self, saved_text_from_website):
        """ what is needed to reduce the size and make the text consistent before it goes in the network"""
        import re
        import unicodedata
        """ remove extra spacing, names, tabs, and other unwanted values"""
        website_data= re.sub("\n"," ", saved_text_from_website)
        website_data= re.sub("\t"," ", website_data)
        website_data= re.sub("\r"," ", website_data)
        website_data=re.sub(r" \s+", r" ", website_data)
        website_data= re.sub(r"\\x\S+",r" ",website_data )
        website_data= re.sub(r"@", "",website_data)

        website_data= unicodedata.normalize("NFKD",website_data)
        return website_data
        # repeat for law_document
    def divide_text_into_sentences(self,website_data):
        """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
        from nltk.tokenize import sent_tokenize
        # can add neural network here when i feel more comfortable
        # divide into sentence non sentence here
        import re
        index_used_list=[]
        self.sentences=[]
        final_sentence_list=[]
        find_word_pattern = re.compile(r"\w+")
        #from nltk.tokenize import word_tokenize
        modifying_sentences = sent_tokenize(website_data)
        for i7, sentence_15 in enumerate(modifying_sentences):
            words_in_current_sentence=find_word_pattern.findall(sentence_15)
            if len(words_in_current_sentence)<4: 
                print(sentence_15)
                continue
            if len(words_in_current_sentence)>60: 
                print(sentence_15)
                continue
            if "https" in sentence_15:
                print(sentence_15)
                continue
            else:
                final_sentence_list.append(sentence_15)
        return final_sentence_list 
    def label_sentence_with_spacy(self,sentence): 
        #a1_1_1.1.1.1_1
        """ generate spacy information for a sentnece"""
        sentence=sentence.replace("?","").replace(",","")
        doc = self.nlp(sentence)
        noun_chunks = [chunk.text.lower() for chunk in doc.noun_chunks]
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        sentences = [sent.text for sent in doc.sents]
        lemmatized_tokens = [token.lemma_ for token in doc]
        pos_tags = [(token.text.lower(), token.pos_) for token in doc]
        pos_only_tags = [(token.pos_) for token in doc]
        text_only_tags = [(token.text.lower()) for token in doc]
        # lower everything
        return {
            "noun_chunks": noun_chunks,
            "entities": entities,
            "sentence": sentence,
            "lemmatized_tokens": lemmatized_tokens,
            "pos_tags": pos_tags,
            "pos_only_tags":pos_only_tags,
            "text_only_tags":text_only_tags
            }
    
    def get_objects_and_qualitites_of_objects_in_sentence(self,spacy_dic):
        """get the intital objects and qualtites in the sentnece """
        import re
        cleaned_noun_chunk_list=[]
        for noun_chunk_number, noun_chunk in enumerate(spacy_dic["noun_chunks"]):
            words_in_noun_chunk=re.split(r" ",noun_chunk)
            cleaned_noun_chunk=""
            for word_placement_value, worddd in enumerate(words_in_noun_chunk):
                
                try:
                    index_of_word=spacy_dic["text_only_tags"].index(worddd)
                except:
                    print(f"{worddd} NOT FOUND")
                    continue    
                poss=spacy_dic["pos_only_tags"][index_of_word]
                if poss =="NOUN" or poss =="PROPN":
                    cleaned_noun_chunk+=f"{worddd} "       
            cleaned_noun_chunk=cleaned_noun_chunk.strip()            
            if cleaned_noun_chunk=="":
                continue
            # only grab last word in noun chink here which is a noun
            # and use a lemma
            cleaned_noun_chunk_list.append(cleaned_noun_chunk)
            
            # create qualtities of object here
            # add subsequent noun chunk
            if cleaned_noun_chunk not in self.automated_problem_galaxy_dic:
                self.automated_problem_galaxy_dic[cleaned_noun_chunk]={"qualtity_list":[],"transformation_list":[]}
            if noun_chunk_number!=len(spacy_dic["noun_chunks"])-1:
                # if last noun chunk then dont add qualtity
                if spacy_dic["noun_chunks"][noun_chunk_number+1] in self.automated_problem_galaxy_dic[cleaned_noun_chunk]["qualtity_list"]:
                    continue
                else:
                    self.automated_problem_galaxy_dic[cleaned_noun_chunk]["qualtity_list"].append(spacy_dic["noun_chunks"][noun_chunk_number+1])# noun chunk after this one
        return self.automated_problem_galaxy_dic,cleaned_noun_chunk_list
              
    def get_transformation_of_objects_in_sentence(self,spacy_dic,cleaned_noun_chunk_list):
        """using the dictionary we created to get qual and object now get verbs or transformations for each object """
        current_noun_chunk=""
        #print(spacy_dic)
        #print(cleaned_noun_chunk_list)
        if cleaned_noun_chunk_list:
            for i2, word_tag in enumerate(spacy_dic["pos_tags"]):# skip how do i is why we start at 3 
                # find associated noun chunk
                word=word_tag[0]
                pos=word_tag[1]
                # determine current noun chunk
                if pos =="NOUN" or pos =="PROPN":
                    word_prior=None
                    word_after=None
                    current_word=None
                    noun_chunk_score_list=[]
                    current_word=spacy_dic["text_only_tags"][i2]
                    if i2!=len(spacy_dic["text_only_tags"])-1:
                        word_prior=spacy_dic["text_only_tags"][i2+1]
                    if i2!=0:
                        word_after=spacy_dic["text_only_tags"][i2-1] 
                    for noun_chunkk in cleaned_noun_chunk_list:
                        noun_chunk_score=0
                        if current_word in  noun_chunkk:
                             noun_chunk_score+=1
                        if word_prior !=None and word_prior in noun_chunkk:
        
                              noun_chunk_score+=1 
                        if word_after !=None and word_after in noun_chunkk:
                              noun_chunk_score+=1
                        noun_chunk_score_list.append(noun_chunk_score)
                    #print(noun_chunk_score_list)
                    max_noun_chunk_value=max(noun_chunk_score_list)
                    max_noun_chunk_index=noun_chunk_score_list.index(max_noun_chunk_value)
                    current_noun_chunk=cleaned_noun_chunk_list[max_noun_chunk_index] 
                    #current_noun_chunk=cleaned_noun_chunk_list[current_noun_chunk_index]
                    
                if pos == "VERB" and current_noun_chunk!="":
                    self.automated_problem_galaxy_dic[current_noun_chunk]["transformation_list"].append(word)    
                    
        return self.automated_problem_galaxy_dic               

            
        
    def create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(self,spacy_dic):
        """ """
        import re
        import copy
        #orignal sentence saved so if want to modify algorhim later i can
        saved_word_word_chunk_cross_reference_dic={}
        cleaned_noun_chunk_list=[] 
        automated_problem_galaxy_dic,cleaned_noun_chunk_list=self.get_objects_and_qualitites_of_objects_in_sentence(spacy_dic) 
        automated_problem_galaxy_dic=self.get_transformation_of_objects_in_sentence(spacy_dic,cleaned_noun_chunk_list) 
        return automated_problem_galaxy_dic
    
    def clean_strs_before_input_into_sql(self,strrr):
        """ """
        import re
        strrr=re.sub('\'',"",str(strrr))
        strrr=re.sub('\"',"",strrr)
        strrr=re.sub('\n',"",strrr)
        return strrr
        
    def store_auto_created_galaxies_and_transformation_for_problem_web_in_sql(self):
        """ """
        #auto_problem_table columns
        import time
        current_time=time.time()
        for objectt, objectt_dic in self.automated_problem_galaxy_dic.items():
            qualtity_list=self.automated_problem_galaxy_dic[objectt]["qualtity_list"]
            transformation_list=self.automated_problem_galaxy_dic[objectt]["transformation_list"]
            objectt=self.clean_strs_before_input_into_sql(objectt)
            qualtity_list=self.clean_strs_before_input_into_sql(qualtity_list)
            transformation_list=self.clean_strs_before_input_into_sql(transformation_list)
            current_time=self.clean_strs_before_input_into_sql(current_time)
            # need to make sure not to over write  values here

            self.cur.execute( f""" INSERT INTO auto_problem_table (problem_question_or_task,specific_problem_or_object,qualitity_list,transformations,initial_creation)
                         VALUES ('{str(self.problem_recorded)}','{str(objectt)}','{str(qualtity_list)}','{str(transformation_list)}','{str(current_time)}');""")
        self.conn.commit()
        # what if i want to update this thing? used past functions
        # and always start from scratch by assumption
    
    def automatically_add_web_search_result_to_problem_web_and_transformations_list(self,problemm):
        """ this function will get results from various search browsers and then upload them to """
        import spacy
        self.automated_problem_galaxy_dic={}
        self.automated_problem_galaxy_dic[self.problem_recorded]= {"qualtity_list":self.problem_recorded[12:].split(" "),"transformation_list":[]}  # need to remove how do i
        self.nlp = spacy.load("en_core_web_sm")
        saved_text_from_website_list=self.retreive_problem_data_from_web(problemm)
        for text in saved_text_from_website_list:
            single_website_text=self.pre_process_text(text)
            final_sentence_list=self.divide_text_into_sentences(single_website_text)
            for sentence in final_sentence_list:
                spacy_dic=self.label_sentence_with_spacy(sentence)
                self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(spacy_dic)
                
        self.store_auto_created_galaxies_and_transformation_for_problem_web_in_sql()
        print(self.automated_problem_galaxy_dic)
        return self.automated_problem_galaxy_dic
    #### PROBLEM TREE FUNCTIONS
    # think of permeant solution here not temp
    # make this work and be useful
        
    def auto_generate_action_space_and_effects(self):
        """ actions are linked to effects"""
        import copy
        automated_problem_galaxy_dic2=copy.deepcopy(self.automated_problem_galaxy_dic)
        self.possible_object_action_effect_list_dic={}#objectttt:[list of actions]
        print(self.automated_problem_galaxy_dic)
        self.strategy_methods_problem_tree_dic={}
        for objectt, objectt_dic in self.automated_problem_galaxy_dic.items():
            self.strategy_methods_problem_tree_dic[objectt]={"action_list":[],"effects_list":[]}
            qualtity_list=self.automated_problem_galaxy_dic[objectt]["qualtity_list"]
            transformation_list=self.automated_problem_galaxy_dic[objectt]["transformation_list"]
            
            for transformation in transformation_list:
                actionnnn=f" {transformation} {objectt}"
                self.strategy_methods_problem_tree_dic[objectt]["action_list"].append(actionnnn)  
                self.strategy_methods_problem_tree_dic[objectt]["effects_list"].append(qualtity_list)  
        return self.automated_problem_galaxy_dic
    ### start of working stratgy functions and problem tree
    def generate_more_context_qualtities_as_necesarry_using_tool_and_questions(self,strategy_dic):
        """ gather as muc context as possible on given action
        use generative model for this
        store results to each questions as qualtites of the action input"""
        # run a model off of big computer to do this?
        # and send data back
        # maybe use gpt for this
        # couple options
        # use all questions and tools
        # cant afford mdoel here? too expensive do this another time
        # or find other solution
        #try an example tool here
        # and an example question
        # just use a improved web search here
    def generate_value_dic_of_how_compareable_actions_are_based_on_effect_lists(self):
        """ compare all actions effects against all other action effects and create a value dic of these comparisons """
        self.matching_values_of_effects_dic={}
        print('starting sort')

        for i1, (objecttt1) in enumerate(self.strategy_methods_problem_tree_dic.keys()):
            possible_action_space_list1=self.strategy_methods_problem_tree_dic[objecttt1]["action_list"]
            effects_list_list1=self.strategy_methods_problem_tree_dic[objecttt1]["effects_list"]
            #print(f"objecttt1 : {objecttt1}")
            #print(f"effects_list_list1 : {effects_list_list1}")
            if effects_list_list1:
                effect_list1=effects_list_list1[0]
            else:
                continue
            for i2, (objecttt2) in enumerate(self.strategy_methods_problem_tree_dic.keys()):
                if i2 % 2 == 1:
                    continue
                possible_action_space_list2=self.strategy_methods_problem_tree_dic[objecttt2]["action_list"]
                effects_list_list2=self.strategy_methods_problem_tree_dic[objecttt2]["effects_list"]
                if effects_list_list2:
                    effects_list2=effects_list_list2[0]
                else:
                    continue
                len_effect_list_2=len(effects_list2)
                effects_found=0
                for iii2, effect2 in enumerate(effects_list2):
                    if effect2 in effect_list1:
                        effects_found +=1
                    else:
                        continue
                if len_effect_list_2==0:
                    weighted_effects_found=0
                else:
                    weighted_effects_found=effects_found/len_effect_list_2
                #print(f"effects_found : {effects_found}")
                #print(f"weighted_effects_found : {weighted_effects_found}")
                for actionn1 in possible_action_space_list1:
                    for actionn2 in possible_action_space_list2:
                        if actionn1 not in self.matching_values_of_effects_dic:
                            self.matching_values_of_effects_dic[actionn1]={}
                        else:
                            self.matching_values_of_effects_dic[actionn1][actionn2]={"weighted_effects_found":weighted_effects_found,
                                                                                     "objecttt1":objecttt1,
                                                                                     "objecttt2":objecttt2,
                                                                                     "action1":actionn1,
                                                                                     "action2":actionn2,
                                                                                     "effect_list1":effect_list1,
                                                                                     "effect_list2":effects_list2} 
    
                                  
        return self.matching_values_of_effects_dic
    def sort_actions_into_strat_by_max_different_effect_score_sub(self):
        """need to rewrite this so no memroy error cant compare every noun it seems so make this more efficent """
        self.strategy_methods_problem_tree_dic_max_difference={"max_different_effect_strategies":[], 
                                                 "max_different_objects_associated_with_action":[],
                                                 "max_different_effect_list":[] }
        # list of list with 10 actions in each list
        #print(self.matching_values_of_effects_dic)
        print('meow')
        current_strategy_list=[]
        used_actions_list=[]
        final_strategy_list=[]
        lowest_score_list=[]
        for action1 in self.matching_values_of_effects_dic.keys():
            final_strategy_list=[]
            objecttt1_list=[]
            objecttt2_list=[]
            actionn1_list=[]
            actionn2_list=[]
            effect_list1_list=[]
            effect_list2_list=[]
            lowest_action_list=[]
            lowest_score_list=[]
            if action1 in used_actions_list:
                continue
            for i8, (action2) in enumerate(self.matching_values_of_effects_dic[action1].keys()):
                if action2 in used_actions_list:
                    continue
               
                weighted_effects_found=self.matching_values_of_effects_dic[action1][action2]["weighted_effects_found"]
                if len(lowest_action_list)<9:
                    lowest_action_list.append(self.matching_values_of_effects_dic[action1][action2])
                    lowest_score_list.append(weighted_effects_found)
                    max_score=max(lowest_score_list)
                    current_highest_saved_score=max_score
                    continue
                if weighted_effects_found<=current_highest_saved_score:
                    current_highest_saved_score_index=lowest_score_list.index(current_highest_saved_score)
                    lowest_action_list[current_highest_saved_score_index]=self.matching_values_of_effects_dic[action1][action2]
                    lowest_score_list[current_highest_saved_score_index]=weighted_effects_found
                    max_score=max(lowest_score_list)
                    current_highest_saved_score=max_score
                else:
                    continue
                    
            for i6, action_info in enumerate(lowest_action_list):
                used_actions_list.append(action_info["action2"])
                #action_info dictionary
                final_strategy_list.append(action_info["action2"])
                objecttt1_list.append(action_info["objecttt2"])
                #objecttt2_list.append(action_info["objecttt2"])
                #actionn1_list.append(action_info["action1"])
                #actionn2_list.append(action_info["action2"])
                effect_list1_list.append(action_info["effect_list2"])
                #effect_list2_list.append(action_info["effect_list2"])
                
            self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_strategies"].append(final_strategy_list) 
            self.strategy_methods_problem_tree_dic_max_difference["max_different_objects_associated_with_action"].append(objecttt1_list)    
            self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_list"].append(effect_list1_list)    

        return self.strategy_methods_problem_tree_dic_max_difference# list of list of strategies
    def sort_actions_into_strat_by_max_different_effect_score(self,strategy_methods_problem_tree_dic):
        """ # iterate through effects lists and assign corresponding values
        # depending on how related each effect list is to each other
        # sort effect lists into strategies using these scoring lists
        #qauntity being being the number of matching qualtites"""
        self.generate_value_dic_of_how_compareable_actions_are_based_on_effect_lists()
        self.sort_actions_into_strat_by_max_different_effect_score_sub()
        return self.strategy_methods_problem_tree_dic 
        
    def consider_effects(self,galaxy_problem_dic):
        """ """
        strategy_methods_problem_tree_dic=self.sort_actions_into_strat_by_max_different_effect_score(self.strategy_methods_problem_tree_dic)
        #create one actions_list with very diverse effects
        #and one with very similar effects
        # divide into strategies of 10
        #action
        #down stream effects 
        # want strategies with 10 actions
        #consider effect spread
        # divide actions using all there 
        #qualtites in various ways
        # and use qualtities of qualtites
        # to decide how you could use it 
        #to divide up the actions
        # how to do this
        # how to save data 
        # group all 
        return self.strategy_methods_problem_tree_dic
    def consider_tools(self):
        """ """
    def cosnider_question_info(self):
     """ """
    def consider_past_problem_data(self):
        """look at time it took toc omplete action and other qualtites"""
            #time
            #get max 20%
            #get min 20%
        #strategy 1 actions most different effects rule
     
    def consider_herusitic_or_general_principles_using_action_context_to_sort_and_select_actions(self,strategy_methods_problem_tree_dic):
        """
        # use  interactions and 
        #ojbects qualtity thermselves to produce strats
        # and if else statements below
        bascially a massive decision tree
        dividng on qualtity and then
        dividing on qualtity of qualtity
        and automating this
        seeing action chosen
        using this and then choosing best categories
        look for general qualitites  for stronger transformations
        # these are effects
        # time
        tool answers
        question answers
        basically try differnet things to get different action lists
        dvidied on qualtites and use the best one to train neural net
        for now just use effects
        eventually turn into nn
        IMPORTANT BELOW
        maybe categorize strategies
        by how they were created
        by what sort of heuristic
        to track later
        and group by 10
        """
        self.consider_effects(self.strategy_methods_problem_tree_dic)
        # will divide actions along these when have time comming
        # up with sorting algorhyim relating to them
        self.consider_tools()
        self.cosnider_question_info()
        self.consider_past_problem_data()# generate this problem data later to use this
        # will build nn out of it
        # problem data might be time
        # and screen shots for each action
        return self.strategy_methods_problem_tree_dic
    def distil_berta_to_produce_word_embedding(self):
        """input actions """
    def ffn_1_cateogrizing_actions_into_types_of_strats(self):
        """input actions
        what categories and why
        basically want to sort actions
        along some critera so we can then 
        choose some over others   for di f ferent reasons
        and also ignore others completely
        used versus unused actions
        qualtites of action data 
        used recorded screen caputre
        to create labels here?
        how to divide up actions into differetn strats
        how to use different data here
        used during probelm sovling
        used versus unused qualtites
        CATEGORIES?
        labels determined using qualtites and
        other data of actions in previous problems
        maybe creative, 
        not creative
        most simialr actions in previous problems
        in previous problems
        most time consuming
        
        """
    def ffn_2_ordering_actions_within_strats(self):
        """output ordered strats using previous action placement in a strat ordering placement 
        use other problem solving data as well here"""

         
    def consider_past_action_data_with_nn_to_choose_and_sort_action(self,strategy_dic):
        """once have exact actions and strats  from heuristic lists we like use nn
        use a neural network here
        create a couple strategies using this approach
        NEED TO DESIGN NEURAL NET
        use data we have
        basically train a policy function
        # neural network which can place based on info in a category
        the given actionn with respect to the problem
        and basically generate where it should be placed or aborted
        subseted o f data label then nn
        if all data then not
        try different ways to group actions"""
        # feed past data in
        # given action categorize it into a certain category
        # in terms of usefulness
        """cons)ider how to use past problem ifnormation use past solutions to guide current solutions """
        distilbert_embedding=self.distil_berta_to_produce_word_embedding()
        chosen_action_group=self.ffn_1_cateogrizing_actions_into_types_of_strats()
        chosen_action_placvement_in_strat=self.ffn_2_ordering_actions_within_strats()
        # leverage patterns in questions to rank actions based on certain tools
        # add to this as we go through actions positioning them based on heurisitcs
        #input layer
        # vision transformer
        # to process images taken
        # while working on problem
        # deberta word embedding for the word action
        # output into strat ffn
        #https://huggingface.co/distilbert/distilroberta-base
        #output to ffn to 
        # ffn output is pick which strategy to place or not place action into
        # actions
        # what does output look like with 16 neurons
        # categorize actions
        # for use in different strategies
        # how to get labels
        # labels are actions we want in each category
        # based on some pattern or heuristic
        # heuristic/ patterns found by nn
        # which uses some input data
        # or something not sure what labels are yet
        #probably given actions chosen when sovling problem
        #output
        #labeled strats we have created or used 
        
        # could use a image transformer

        
    def auto_generate_strats_and_effects(self):
        """strategies 10 actions max
        16 different strats
        so 10 by 10 grid
        # and place action in it
        # choose not to place action
        # using context here
        and heursitcs and past problem data
        20 possible spaces actions could fall"""
        # strategies associated certain questions or tools?
        self.generate_more_context_qualtities_as_necesarry_using_tool_and_questions(self.strategy_methods_problem_tree_dic)
        self.consider_herusitic_or_general_principles_using_action_context_to_sort_and_select_actions(self.strategy_methods_problem_tree_dic)
        self.consider_past_action_data_with_nn_to_choose_and_sort_action(self.strategy_methods_problem_tree_dic)
    
    def store_auto_created_actions_and_strategies_for_problem_tree_sql(self):
        """ """
        import time
        current_time=time.time()
        for i12 in range(len(self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_strategies"])):
            max_different_effect_strategies=self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_strategies"][i12]
            max_different_objects_associated_with_action=self.strategy_methods_problem_tree_dic_max_difference["max_different_objects_associated_with_action"][i12]
            max_different_effect_list=self.strategy_methods_problem_tree_dic_max_difference["max_different_effect_list"][i12]
            
            max_different_effect_strategies=self.clean_strs_before_input_into_sql(max_different_effect_strategies)
            max_different_objects_associated_with_action=self.clean_strs_before_input_into_sql(max_different_objects_associated_with_action)
            max_different_effect_list=self.clean_strs_before_input_into_sql(max_different_effect_list)
            current_time=self.clean_strs_before_input_into_sql(current_time)

            self.cur.execute( f""" INSERT INTO auto_strategy_table (problem_being_solved,objectts,actions,effects,time_found)
                         VALUES ('{str(self.problem_recorded)}','{str(max_different_objects_associated_with_action)}','{str(max_different_effect_strategies)}','{str(max_different_effect_list)}','{str(current_time)}');""")
        self.conn.commit()
    def auto_generate_and_problem_trees_from_problem_galaxy(self):
        """ automcialy generate web from text gathered from duckduckogo"""
        self.auto_generate_action_space_and_effects()
        self.auto_generate_strats_and_effects()
        self.store_auto_created_actions_and_strategies_for_problem_tree_sql()

    def make_all_this_usable_and_editable(self):
         """ MAKE IT EASY TO SWITCH TO SUB TREE problem when working on an action
         # DOne so you can immedately start labeing that sub tree 
         """
         
         # 2 make auto problem web and tree results loaded in
         # and make use of them
         # 1. show the auto_problem_tree in web_result box
         # auto display problem web blender on record problem
         # also upload problem web to current connected objects list box
         
         # 2. subprocess record problem operations
         # 3. run seleniium in background
         # 4. make all referecnes to probelm table reference 
         # 5. reference auto problem table
         
         # 6. display effects in problem envrionment
         # 4 start recording screen and tracking problem data
         # build nn from problem data

         # 7. fix other errors as we go
         # when loading in web results load in automcially
         # or loading in effects
         # have button to display effects
         #problme tree dictionary value strats
         
         
         
         
         
         

         
         # and the strats i select from auto are uploaded to the actual
         # display auto strats somewhere
         # strat table 
         # DISPLAY autogenerate strats in web results box
         # have option to show them in blender
         # SUBPROCESS THE RECORD PROBLEM OPERATIONS
         # SO CAN USE PROGRAM IN MEAN TIME
         # and make this faster
         # run selenium in the background
         # to fetch website data
         # with problem web just turn it all into auto problem web
         # improve results and use results

         
         #3 display effects in probvlem envrionmnet
         # of a selected strat in strategy table
         # select strat using a key you press
         # otherwise assume newest uploaded strat
        
         
         
    def display_effects_of_strategy_in_problem_enviornment(self):
        """ NEED TO ADD THIS TO THE BLENDER DISPLAY THING"""
        # show the qualitites impacted by a object being used
        #highlight object in use in action and highlight qualtites with different color
   
        
    def start_auto_generating_problem_data_from_recording_screen(self):
        """ WORK ON FUNCTIONS WE CREATED BELOW 
        and create table to record screen data etc
        to automically figure out what proiblem we are working on
        and automcially create and hsow strategies and proiblem envrionment
        for this problem"""
        
        
        
    # FUTURE
    def auto_choose_problem_to_solve_with_best_effects(self):
        """ """
        # go through problems list we have created
        # auto generate strategies related to certain category
        # get effects
        # categroize problems based on effects k clustering
        # have ability to choose which problems to solve
        #Stage 3 Automate the creation of all possilbe effects
        # step1 have a list of questions to ask to determine effects like write action and ask what are the effects of this action
        # I need to find a better way to do this
        #
        # generate effects apply web and then write down things this action should touch in a list the nouns and adjectives
        # an effect is the environment you are thrown into when taking an action
        # so list the future environment  anticpated if action is taken and then loop
        # something aobut the things related to this action change is the effects of a action
        #
        # step 2 make a list of the results and parse.
        # step 3 treat the action as a new prolbem to build a web around and ask questions to produce actions
        # use past effects here to build on context and make a list of possible effect questions to ask
        # the actions it generates after this first action are the effects which is what the action enables you do, and the environment of the new action
        # Reinforcement learning component to reason trhough the taking of that action as a additonal problem
        # treat  the action as a new problem and then create environment or web of problem
        # and keep doing this down each sequence of actions and have these as effects and the envrionments they produce
        # step 1 one effect is it will put you in a new environment with new decisions to make
        # and can look through the list of actions you can take if you went down the path and try to see the end result
        # looking at each subseqent environment you can expect and actions you can take to see the outcome of taking a certain action
        # this is reinforment leanring in a netshell
        
        
        
 
    def record_question_or_tool_used(self,event: str)-> str:
        """ record the question/tool that led to a thought saving it as a object to save in the database or thought you think caused an idea"""
        # when 2 is clicked on one of the side panels  this happens
        import re
        from ctypes import windll
        content=window.selection_get()
        # if its not a question you have already written in the database have option to write it down 
        print('hi')
        content= re.sub('\d+:','',content) 
        self.recorded_question_or_tool=content[:-1]  
        self.recorded_question_or_tool=re.sub("\n","", self.recorded_question_or_tool)
        print(self.recorded_question_or_tool)
        
    def record_idea_used_for_method(self,event: str)-> str:
        import re
        from ctypes import windll
        content=window.selection_get()
        print('hi')
        content= re.sub('\d+:','',content) 
        recorded_objective=content[:-1]  
        recorded_objective=re.sub("\n","", recorded_objective)
        self.ideas_list_for_method.append(recorded_objective)
        print(self.ideas_list_for_method)
    def record_action_strategey_for_methd(self,event:str)-> str:
        self.strategy_action_for_method
        #strategy_action
 
 
    def transport_object_from_object_window(self,event):
        """ take a object from one of the side panels and place it and its qualities in the left top center textbox"""
        import re
        from ctypes import windll
        import time
        # need to edit this  one to make sure that it transports objects correctly to edit
        # need to think through how to move objects more closely and to work witht hem to make sure information is not lost
        self.starting_time_object=time.time()
        content=window.selection_get()
        content= re.sub('\d+:','',content) 
        content=content[:-1]
        self.text_box0.insert(tk.END, content)
        windll.user32.EmptyClipboard()
    def add_object_to_problem_dictionary(self):
        """ this function takes what is in textbox0 and adds it to problem dictionary """
        import re
        import time
        import copy
        content=self.text_box0.get('1.0', 'end')
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
    def upload_and_download_problem_dictionary(self):
        """put problem dictionary into sql and update listbox """
        import re
        #print(self.problem_list_dictionary)
        # add_previous_galaxies_to_problem
        # need to fix this
        #for add_previous_galaxies_to_problem
        #what is going wrong here
        # this is currently not working for 9

       

        for problem_or_object, list_of_qualities in self.problem_list_dictionary.items():
            tool_or_question_list=[]
            qualitity_list=[]
            time_created_list=[]
            #print('meow')
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
            print(tool_or_question_list)
            
            if self.previous_problem_list_dictionary.get(problem_or_object) and len(self.previous_problem_list_dictionary[self.problem_recorded])>1:
                #print("7")
                #print('hello')
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
        self.listbox1.delete(0, tk.END)
        for i20, objecttt in enumerate(problem_entries):
            problem_question_or_task= objecttt[1]
            specific_problem_or_object= objecttt[2]
            objectt_string=f"{i20} {specific_problem_or_object};"
            objectt_string=re.sub("[?]","",objectt_string)
            objectt_string=objectt_string.replace("\n","")
            qualitity_list = str(objecttt[4])
            if qualitity_list:
                qualitity_list=qualitity_list.replace("\n","")
                qualitity_list=qualitity_list.replace("\\","")
                #print(qualitity_list)
                qualitity_list=re.split(",",qualitity_list[1:-1])
                for i6, qualities_of_entry in enumerate(qualitity_list):
                    if i6==0:
                        objectt_string+=f"{qualities_of_entry}"
                    else:
                        objectt_string+=f",{qualities_of_entry}"

                self.listbox1.insert(tk.END, objectt_string)
 
    
  
    def add_qualitites_expand_current_qualtity_or_problem_dictionary(self,event): 
        """ press certain key to add to the list of lists in the key of a dictionary with first 
        item being tool or question used and second being qualtity being assigned to the
        given problem or key object"""
        self.add_object_to_problem_dictionary()
        self.upload_and_download_problem_dictionary()
        
        
    def reupload_problem_to_view_in_listbox(self,problem_recorded):
        """ grab the objects associated with a problem from the database and upload it"""
        import re
        self.listbox1.delete(1, tk.END)
        self.cur.execute(f"""SELECT * FROM problem_table WHERE problem_question_or_task = '{problem_recorded}';""")
        problem_entries= self.cur.fetchall()
        master_tool_or_question_per_conn_list=[]
        master_qualitity_str=[]
        master_time_created_conn=[]
        specific_problem_or_object=""
        for i16,objecttt in enumerate(problem_entries):
            problem_question_or_task= objecttt[1]
            specific_problem_or_object= objecttt[2]
            objectt_string=f"{i16} {specific_problem_or_object};"
            qualitity_list = objecttt[4]
            if qualitity_list:
                qualitity_list=re.sub("\n","",qualitity_list)
                qualitity_list=re.sub("\\n","",qualitity_list)
                qualitity_list=re.split(",",qualitity_list[1:-1])
                for i6, qualities_of_entry in enumerate(qualitity_list):
                    if i6==0:
                        objectt_string+=f"{qualities_of_entry}"
                    else:
                        objectt_string+=f",{qualities_of_entry}"
                        # add number to know which one
                        
                self.listbox1.insert(tk.END, objectt_string) 
    def ghost_list(self, sql_list):
        print(sql_list)
        for i,s in enumerate(sql_list):
            print(i)
            print(s)  
    def switch_to_previous_galaxy(self,event):
        """ """ 
        import re
        content=self.listbox1.selection_get()
        object_and_list=re.split(";",content)
        self.current_object_or_problem=object_and_list[0]

    def list_past_problems(self,event):
        """ print out a list of problems we have already worked on to then copy and reupload its galaxy"""
        self.cur.execute(f"""SELECT * FROM problem_table ;""")
        self.text_box.delete('1.0', 'end')
        problems_worked_on= self.cur.fetchall()
        list_of_problems=[]
        problem_list_str=""
        for problemm1 in problems_worked_on:
            problemmm=problemm1[1]
            if problemmm not in list_of_problems:
                problem_list_str+= f"{problemmm}\n"  
                list_of_problems.append(problemmm)
        self.text_box.insert(tk.END, problem_list_str) 
    def upload_and_process_problem_table_data_for_specific_problem(self):
        """ """
        import re
        self.cur.execute(f"""SELECT * FROM auto_problem_table WHERE problem_question_or_task = '{self.problem_recorded}';""")# will need to test this
        self.problem_list_dictionary={}
        problem_entries= self.cur.fetchall()
        self.current_object_or_problem=self.problem_recorded
        for numm, objectt1 in enumerate(problem_entries):
                intital_time_for_object=objectt1[7]
                specfic_object=objectt1[2]
                tool_or_question_used=objectt1[3]
                qual_list=objectt1[4]
                timme=objectt1[6]
                timme=re.split(",",timme[1:-1])
                qual_list=re.split(",",qual_list[1:-1])
                tool_or_question_used=re.split(",",tool_or_question_used[1:-1])
                self.problem_list_dictionary[specfic_object]=[intital_time_for_object]
                #specfic_object=problem_entry[2]
                for tooll,quall,timm in zip(tool_or_question_used,qual_list,timme):
                    self.problem_list_dictionary[specfic_object].append([tooll,quall,timm])
                continue 
        
    def upload_past_problem_to_keep_expanding_network(self,event):
        """ press 0 and then - query sql database for past problem and upload its conns to the program """
        #need to modify this so that i can upload the correct problem
        import re
        self.method_list_dictionary={}
        self.strategy_list=[]
        self.recorded_question_or_tool_for_method_list=[]
        self.objective_list_for_method=[]
        self.ideas_list_for_method=[]        
        self.actions_for_method=[]
        self.strategy_or_method_label_for_methods=[]
        self.past_problemm=""
        problem_to_reupload=self.text_box.get('1.0', 'end')
   
        # split on zero?0- to grab problem
        #problem_to_reupload_split2=re.split("0\n",problem_to_reupload)
        problem_to_reupload_split2=re.split("\n",problem_to_reupload)
        for problems_solved in problem_to_reupload_split2:
            #print(problems_solved)
            if "0" in problems_solved:
                problems_solved=re.sub(r"0","",problems_solved)
                self.problem_recorded=problems_solved
                break
        self.upload_and_process_problem_table_data_for_specific_problem()
        #self.problem_recorded=problem_to_reupload_split[0]
        #print(self.problem_list_dictionary)
        self.reupload_problem_to_view_in_listbox(self.problem_recorded)
    def generate_problem_webb(self):
        """ create the nodes and edges for the problem web """
        import copy
        import networkx as nx
        import matplotlib.pyplot as plt
        from PIL import ImageTk, Image
        self.node_name_list=[]
        self.color_map=[]
        self.edge_map=[]
        self.node_number_list=[]
        color_levels_list=["#A0CBE2","yellow","orange","pink","red","#A0CBE2"]
        # grab problem right away
        #self.problem_list_dictionary.items()
        problemmm=self.problem_recorded
        self.node_name_list.append(problemmm)
        self.color_map.append(color_levels_list[0])
        #print(self.problem_list_dictionary)
        for i9, quality1 in enumerate(self.problem_list_dictionary[problemmm]):     
            if i9==0:
                continue
            qualitityy=quality1[1]
            if len(qualitityy)> 15:
                qualitityy=qualitityy[:12]
            self.edge_map.append((problemmm,qualitityy))
            self.node_name_list.append(qualitityy)
            self.color_map.append(color_levels_list[1])
        print('hello!!')
        print(len(self.color_map))  
        print(len(self.node_name_list))
            
        for objecttt,list_of_qualities in self.problem_list_dictionary.items():
            if "?? " in objecttt:
                continue
            #print('START')
            #print(self.edge_map)
            #print(self.node_name_list)
            #print(self.color_map)

            if objecttt not in self.node_name_list:
                self.node_name_list.append(objecttt)
                self.color_map.append(color_levels_list[1])
                self.edge_map.append((problemmm,objecttt))
                
                
            #print(f"this is the color map {len(self.color_map)}")  
            #print(f"this is the node name list {len(self.node_name_list)}")  

            for i10, qualityy2 in enumerate(list_of_qualities):
                if i10==0:
                    continue
                qualitityy=qualityy2[1]
                if len(qualitityy)> 20:
                    qualitityy=qualitityy[:15]   
                self.edge_map.append((objecttt,qualitityy))
                if qualitityy not in self.node_name_list:
                    self.node_name_list.append(qualitityy) 
                    root_index=self.node_name_list.index(objecttt)
                    root_color=self.color_map[root_index] 
                    current_color_index=color_levels_list.index(root_color)
                    self.color_map.append(color_levels_list[current_color_index+1]) 
                    continue

        self.node_number_list=list(range(len(self.node_name_list)))
        #print(f"this is the color map {len(self.color_map)}")  
        #print(f"this is the node name list {len(self.node_name_list)}")  
        #print(f"this is the edge list name list {len(self.edge_map)}")  

        G=nx.Graph()
        G.add_nodes_from(self.node_name_list)
        G.add_edges_from(self.edge_map)
        plt.figure(figsize=(15,12),dpi=80)
        nx.draw_networkx(G, with_labels=True, node_color=self.color_map, font_weight='bold',edge_color='#A0CBE2',font_color='black',node_size=100,font_size=8)
        plt.savefig(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Images\problem_web\web.png',format="PNG",bbox_inches='tight' )
    


    def change_names_of_textboxes(self):
        """ change names of all the boxes"""
        # store previous methods under submethods
        frames={self.frame2:1,self.frame4:10,self.frame5:5,self.frame7:9,self.frame3:15}# self.frame1:13  is connecte dobjectds
        self.label1.config(text="Web Result Edit")
        self.label2.config(text="Strategy display =,`coding engineer /,law all,investment all")
        self.label3.config(text="Current Method Step")
        self.label4.config(text="Idea-Tool Editing")
        for  frame, category in frames.items():
            for widget in frame.winfo_children():
                widget.destroy()  
            if category ==15:
                # related to a specific box because of frame and specific category of information to load in
                self.generate_side_lists_method_design(frame,category, title_of_text="Current Method Steps",conn=False)#3
                continue
            if category ==5:
                self.generate_side_lists_method_design(frame,category, title_of_text="Objectives",conn=False)#5
                continue
            if category == 9:
                self.generate_side_lists_method_design(frame,category, title_of_text="4 Problem Change Sub-Methods",conn=False,sub_method=True)#7 #
                continue
            if category == 1:
                self.generate_side_lists_method_design(frame,category, title_of_text="Questions",conn=False)#2
                
            if category ==10:
                self.generate_side_lists_method_design(frame,category, title_of_text="Tools",conn=False)#4
        print("""questions to draft a method = 1
          galaxies of existing ideas = 2
          thing not useful to problem solving = 3
          questions to form connections = 4
          objectives to optimize towards = 5
          methods created = 6 
          problems i want to solve or tasks=7
          submethods for connections = 8
          submethods for method creation step = 9
          Tools, abstraction useful for making ideas easier for brain = 10 
          ideas on method to construct tasks for problem solving and process = 11
          question for step process = 12
          possible object=15
          web results = 18
          quesitons for strategy creation = 19""")
    def upload_method_dictionary_to_box(self):
        """upload the method steps if there are any to the box for methods here """
        self.cur.execute(f"""SELECT * FROM methods_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        self.listbox2.delete(0, tk.END)
        method_entries= self.cur.fetchall()
        # still need to remove  question marks
        # need to delete all previous entries
        #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
        for objecttt in method_entries:
            #id 0 #problem 1 # step name 2 #tool 3 #ideas 4 # optimize 5 # order 6 #time 7
            problem_being_solved= objecttt[1]
            method_step= str(objecttt[2])
            temporal_placement = str(objecttt[6])
            self.method_step_str = temporal_placement + " "+method_step + "\n"
            self.listbox2.insert(tk.END, f"{self.method_step_str}") 
            

    def switch_to_method_window(self,event):
        """ left click button to switch from connections window to building method window on selected problem"""
   
        self.change_names_of_textboxes()
        try:
            self.generate_problem_webb()
        except:
            print("error")
        self.upload_method_dictionary_to_box()
        
        
        # need to find a way to use the problem web at one point
        #display_method_dicitonary_on_start_up_if_there_is_one() # and make a new one
        # want to add the rest here
    # need to insert these into the methods
    def record_question_or_tool_idea_used_for_method(self,event: str)-> str: # need to fix these things
        """ record the question/tool that led to a thought saving it as a object to save in the database or thought you think caused an idea"""
        import re
        from ctypes import windll
        content=window.selection_get()
        print('hi')
        content= re.sub('\d+:','',content) 
        self.recorded_question_or_tool_for_method=content[:-1]  
        self.recorded_question_or_tool_for_method=re.sub("\n","", self.recorded_question_or_tool_for_method)
        self.recorded_question_or_tool_for_method_list.append(self.recorded_question_or_tool_for_method)
        print(self.recorded_question_or_tool_for_method_list)
    def record_objective_used_for_method(self,event: str)-> str:
        import re
        from ctypes import windll
        content=window.selection_get()
        print('hi')
        content= re.sub('\d+:','',content) 
        recorded_objective=content[:-1]  
        recorded_objective=re.sub("\n","", recorded_objective)
        self.objective_list_for_method.append(recorded_objective)
        print(self.objective_list_for_method)
        
        
    def list_web_in_editing_window_to_access(self,event):
        """ get access to elements of the web record as question or tool used"""
         # need to develop a better way to do this.
         
         
    def transport_to_method_window(self,event):
        """ take a object from one of the side panels and place it ain the bottom left textbox"""
        import re
        from ctypes import windll
        import time
        # need to edit this  one to make sure that it transports objects correctly to edit
        # need to think through how to move objects more closely and to work witht hem to make sure information is not lost
        self.starting_time_object=time.time()
        content=window.selection_get()
        content= re.sub('\d+:','',content) 
        content=content[:-1]
        self.text_box1.insert(tk.END, content) # need to change the textbox
        windll.user32.EmptyClipboard()
    def transport_to_idea_editing_window_method(self,event):
        """ when pressing 1 send whatever selected test in a side listbox to the bottom right window to edit and import to ideabase or to just view""" 
        # press one key
        import re
        from ctypes import windll
        import time
        self.starting_time_object=time.time()
        content=window.selection_get()
        content= re.sub('\d+:','',content) 
        content=content[:-1]
        self.text_box2.insert(tk.END, content) # need to change the textbox
        windll.user32.EmptyClipboard()
    # how to edit an existing step that I have created, answer just make another and keep it don't throw info away
    def add_step_or_modify(self,event): 
        """ press certain key to add to the list of lists in the key of a dictionary with first 
        item being tool or question used and second being qualtity being assigned to the
        given problem or key object"""
        """ I need to add  add_whether_need_to_solve_another_problem_and_what_this_problem_is"""
        #column to add to sql problem_preventing_action
        # how do i make it stop breaking here
        # i add it once and then it does not work anymore to update the listbox

        def create_dict_or_modify(): 
            """ update dictionary adding new step or  modifying existing step """
            import re
            import time
            import copy
            time_method_found =time.time()
            self.cancel=False
            self.delimiter_dicitonary_for_method= {"#":"placement", "=":"idea_web",  "[": "action_strategy_label", "/":"effects","]":"actions_content","\'":"problem_preventing_action" }
            self.placement_dictionary= {"placement":3,"idea_web":1,"action_strategy_label":5,"effects":2,"actions_content":6,"problem_preventing_action":8}
            #unwanted_terms_str = "/#=\]\["
            self.previous_method_list_dictionary=copy.deepcopy(self.method_list_dictionary)
            content=self.text_box1.get('1.0', 'end') # textbox1 is the method window
            if ";" in content: # new step
                objectt_and_qualities=re.split(';',content)
                step_name=objectt_and_qualities[0]
                self.method_list_dictionary[step_name]=[time_method_found]
                self.method_list_dictionary[step_name].append([[],[],[],0,[],[],[],[],[]]) # problem # 1 is there because it is the second entry in this steps list of lists
                self.current_step=step_name
                content=re.split(r"([/#=\]\[\'])",objectt_and_qualities[1])
            else:
                content=re.split(r"([/#=\]\[\'])",content)   
            stored_delimiter=""
            print(content)
            for qual3 in content:
                qual3=re.sub("\n","",qual3)
                if  qual3 in "/#=][\'":
                    stored_delimiter=qual3
                    continue
                
                else:
                    if stored_delimiter =="":
                        continue
                    method_quality_type=self.delimiter_dicitonary_for_method[stored_delimiter]
                    location_in_dictionary_list_for_qual=self.placement_dictionary[method_quality_type]
                    if stored_delimiter=="[":
                        if qual3== "a":
                            self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append("action")
                        if qual3 =="s":
                            self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append("strategy")
                            print('strat')
                            
                        if qual3 =="as" or qual3 == "sa":
                            self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append("strategy action")
                            
                    if stored_delimiter=="]": # this a strategy
                        self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append(qual3)
                        print('act')
                    if stored_delimiter=="#":
                        self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual]=qual3
                        print('found')
                        
                    if stored_delimiter=="\'":
                        self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual]=qual3
                        print('problem stopping us!')
                        
                    if stored_delimiter=="/":
                        self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append(qual3)
                        print('objective or effect')
                        
                    #if stored_delimiter!="#":
                    #    if qual3 not in unwanted_terms_str:
                    #        self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append(qual3) 
            # make sure these blockers are working
            # make sure that dictionary still updating correctly
            #print(self.method_list_dictionary[step_name][1][6])
            #print(self.method_list_dictionary[step_name][1][5])
            
            if self.method_list_dictionary[step_name][1][5]==["strategy"]  and   self.method_list_dictionary[step_name][1][6]==[]:# the actions content is empty
                # if no action specifed but using strategy, need to always have action if strategy
                self.text_box01.delete("1.0", "end")  # need to check if this is the right textbox
                self.add_action_text="You need to add an action here!"
                self.text_box01.insert(tk.END, f"{self.add_action_text}") 
                self.cancel=True
                return "re do this"
            self.text_box.delete('1.0', 'end')

            
            
            if self.method_list_dictionary[step_name][1][5]==[]:
                self.text_box01.delete("1.0", "end")  # need to check if this is the right textbox
                self.add_action_text="You need to add an label here click!"
                self.text_box01.insert(tk.END, f"{self.add_action_text}") 
                self.cancel=True

                return "re do this"
            self.method_list_dictionary[step_name][1][4].append(time_method_found)
            self.method_list_dictionary[step_name][1][0].extend(self.recorded_question_or_tool_for_method_list)
            self.method_list_dictionary[step_name][1][1].extend(self.ideas_list_for_method)
            self.method_list_dictionary[step_name][1][2].extend(self.objective_list_for_method)
            self.method_list_dictionary[step_name][1][7].append(self.past_problemm)
            
            
            print(self.past_problemm)
            print(self.method_list_dictionary[step_name])
            
            #self.method_list_dictionary[step_name][1][5].extend(self.actions_for_method)
            #self.method_list_dictionary[step_name][1][6].extend(self.strategy_or_method_label_for_methods)
            
            self.recorded_question_or_tool_for_method_list=[]
            self.objective_list_for_method=[]
            self.ideas_list_for_method=[]
            self.actions_for_method=[]
            self.strategy_or_method_label_for_methods=[]
            self.past_problemm=""
            print(self.method_list_dictionary)
            return self.method_list_dictionary
        
        def save_method_dictionary_to_database() :
            """ take the method list dictitonary and bring it to database for methods disassembling it and uploading it""" 
            import re
            if self.cancel==True:
                print('hi')
                return "cancelled"
            
            for step_name, list_of_list_qualities in self.method_list_dictionary.items():
                for i6,qualtity in enumerate(list_of_list_qualities):
                    if i6==0:
                        time_object_or_problem_created= qualtity
                        continue
                    tool_or_question_list=qualtity[0]
                    idea_web_list=qualtity[1]
                    objective_list=qualtity[2]
                    placement_int=qualtity[3]
                    time_found_list=qualtity[4]
                    action_related_to_strategy=qualtity[5]
                    strategy_or_method_label_for_methods=qualtity[6]
                    past_problemm=qualtity[7]
                    problem_preventing_action=qualtity[8]
                    print(problem_preventing_action)
                    
                    problem_preventing_action=re.sub('\'',"",str(problem_preventing_action))
                    problem_preventing_action=re.sub('\"',"",problem_preventing_action)
                    problem_preventing_action=re.sub('\n',"",problem_preventing_action)

                    
                    print(past_problemm)
                    
                    past_problemm=re.sub('\'',"",str(past_problemm))
                    past_problemm=re.sub('\"',"",past_problemm)
                    past_problemm=re.sub('\n',"",past_problemm)

                    action_related_to_strategy=re.sub('\'',"",str(action_related_to_strategy))
                    action_related_to_strategy=re.sub('\"',"",action_related_to_strategy)
                    action_related_to_strategy=re.sub('\n',"",action_related_to_strategy)
                    
                    strategy_or_method_label_for_methods=re.sub('\'',"",str(strategy_or_method_label_for_methods))
                    strategy_or_method_label_for_methods=re.sub('\"',"",strategy_or_method_label_for_methods)
                    strategy_or_method_label_for_methods=re.sub('\n',"",strategy_or_method_label_for_methods)
                    

                    
                    tool_or_question_list=re.sub('\'',"",str(tool_or_question_list))
                    tool_or_question_list=re.sub('\"',"",tool_or_question_list)
                    tool_or_question_list=re.sub('\n',"",tool_or_question_list)
                    
                    idea_web_list=re.sub('\'',"",str(idea_web_list))
                    idea_web_list=re.sub('\"',"",idea_web_list)
                    idea_web_list=re.sub('\n',"",idea_web_list)
                    
                    objective_list=re.sub('\'',"",str(objective_list))
                    objective_list=re.sub('\"',"",objective_list)
                    objective_list=re.sub('\n',"",objective_list)
                    
                    time_found_list=re.sub('\'',"",str(time_found_list))
                    time_found_list=re.sub('\"',"",time_found_list)
                    time_found_list=re.sub('\n',"",time_found_list)
                    
                    
                    step_name=re.sub('\'',"",str(step_name))
                    step_name=re.sub('\"',"",step_name)
                    step_name=re.sub('\n',"",step_name)
                    
                    
                    
                    
                    if self.previous_method_list_dictionary.get(step_name) and len(self.previous_method_list_dictionary)>=1: #need
                        #print("7")
                        #strategy_action is the label
                        self.cur.execute( f""" UPDATE methods_table 
                                         Set question_or_tool_for_method= '{str(tool_or_question_list)}', ideas_from_web = '{str(idea_web_list)}',
                                         objectives_maxmized = '{str(objective_list)}', time_method_found = '{str(time_found_list)}',strategy_action ='{str(strategy_or_method_label_for_methods)}',action_related_to_strategy ='{str(action_related_to_strategy)}', past_problem_connection='{str(past_problemm)}', problem_preventing_action='{str(problem_preventing_action)}'
                                         WHERE problem_being_solved = '{str(self.problem_recorded)}' and method_step = '{str(step_name)}';""")
                    else:
                        self.cur.execute( f""" INSERT INTO methods_table (problem_being_solved,method_step ,question_or_tool_for_method,ideas_from_web,objectives_maxmized,temporal_placement,time_method_found,strategy_action,action_related_to_strategy,past_problem_connection,problem_preventing_action)
                                 VALUES ('{str(self.problem_recorded)}','{str(step_name)}','{str(tool_or_question_list)}','{str(idea_web_list)}','{str(objective_list)}','{str(placement_int)}','{str(time_found_list)}','{str(strategy_or_method_label_for_methods)}','{str(action_related_to_strategy)}','{str(past_problemm)}','{str(problem_preventing_action)}');""")
                    

                self.conn.commit()  
        
        def reupload_method_dictionary():
            """ take the method list dictitonary and bring it back into the program  from sql database"""
            self.cur.execute(f"""SELECT * FROM methods_table WHERE problem_being_solved = '{self.problem_recorded}';""")
            self.listbox2.delete(0, tk.END)
            method_entries= self.cur.fetchall()
            # still need to remove  question marks
            # need to delete all previous entries
            #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
            for objecttt in method_entries:
                #id 0 #problem 1 # step name 2 #tool 3 #ideas 4 # optimize 5 # order 6 #time 7
                problem_being_solved= objecttt[1]
                method_step= str(objecttt[2])
                temporal_placement = str(objecttt[6])
                self.method_step_str = temporal_placement + " "+method_step + "\n"
                self.listbox2.insert(tk.END, f"{self.method_step_str}") 
 
        create_dict_or_modify()
        save_method_dictionary_to_database()
        reupload_method_dictionary()
        # can get rid of semicolon maybe so don't need to inseet it
    def use_methods(self,event):
        """ click this to view all methods and access their steps """
        methods=methods_window_program()


    def list_past_methods(self,event):
        """ print out a list of problems we have already worked on to then copy and reupload its galaxy"""
        self.cur.execute(f"""SELECT * FROM methods_table ;""")
        self.text_box.delete('1.0', 'end')
        methods_worked_on= self.cur.fetchall()
        list_of_problems=[]
        method_list_str=""
        for problemm1 in methods_worked_on:
            problemmm=problemm1[1]
            if problemmm not in list_of_problems:
                method_list_str+= f"{problemmm}\n"  
                list_of_problems.append(problemmm)
        self.text_box.insert(tk.END, method_list_str) 

    def upload_previous_methods_to_use_there_variables(self,event): ### next problem to solve
        """ reassemble previous methods from sql database and import into previous steps listbox """    
        #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
        import re
        final_method_str=""
        self.method_entries_dic={2:"step_name", 1:"problem_being_solved",3:"method_step",4:"question_or_tool_for_method",5:"ideas_from_web",6:"objectives_maxmized",7:"temporal_placement","time_method_found":8}
        self.reentry_dic = {"question_or_tool_for_method":0,"ideas_from_web":1,"objectives_maxmized":2,"time_method_found": 4}
        problem_to_reupload=self.text_box.get('1.0', 'end')
        problem_to_reupload_split=re.split("\n",problem_to_reupload)
        time_method_found =time.time()
        self.problem_recorded=problem_to_reupload_split[0]
        self.cur.execute(f"""SELECT * FROM methods_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        self.method_list_dictionary={}
        method_steps= self.cur.fetchall()
        self.current_object_or_problem=self.problem_recorded        
        for numm, method_entry in enumerate(method_steps):
            step_name = method_entry[1]
            temporal_placement = method_entry[7]
            self.temp_method_list_dictionary={}
            self.temp_method_list_dictionary[step_name]=[time_method_found]
            self.temp_method_list_dictionary[step_name].append([[],[],[],temporal_placement,[]]) # problem # 1 is there because it is the second entry in this steps list of lists
            self.current_step=step_name            
            for i8, qual5 in enumerate(method_entry):
                qualitity_name=self.method_entries_dic.get(i8)
                if qualitity_name==None:
                        continue
                if qualitity_name=="temporal_placement":
                    continue
                if qualitity_name=="step_name": 
                    continue  
                else: 
                    qualitity4=str(qualitity4)
                    qualitity4=re.split(",",qualitity4[1:-1])
                list_placement_for_qual=self.reentry_dic.get(qualitity_name)
                for qual7 in qualitity4:
                    self.temp_method_list_dictionary[step_name][list_placement_for_qual].append(qual7)
        for step,list_of_steps_qualitiies in  self.temp_method_list_dictionary.items():
            self.reentry_dic = {"question_or_tool_for_method":0,"ideas_from_web":1,"objectives_maxmized":2,"time_method_found": 4}
            step_number= list_of_steps_qualitiies[3]
            question_or_tool_for_method= list_of_steps_qualitiies[0]
            ideas_from_web=list_of_steps_qualitiies[1]
            objectives_maxmized= list_of_steps_qualitiies[2]
            previous_method_str=step_number + ":" + " " + step + " \n" + question_or_tool_for_method + "\n" + ideas_from_web +  "\n" + objectives_maxmized + "\n"
            final_method_str+= previous_method_str
        self.text_box2.insert(tk.END, final_method_str)
      
    
    def change_back_to_conn_window(self,event): 
         """ save everything that has been written in the methods box and in the current methods dicitonary then go back to conn window"""
         # will need to change the categories and the names of thing
         # may need to fix the categories of these different cases here
         frames={self.frame2:4,self.frame4:10,self.frame5:18,self.frame7:9000,self.frame3:15}# 9000 is submethods
         self.label1.config(text="Object and Qualities of Selected Object")
         self.label2.config(text="Strategy display =,`coding engineer /,law all,investment all")
         self.label3.config(text="Edit-or-Create-Sentences")
         self.label4.config(text="Develop-Sub-Method")
         for  frame, category in frames.items():
             for widget in frame.winfo_children():
                 widget.destroy()  
             if category ==15:
                 self.generate_side_lists_method_design(frame,category, title_of_text="Possible Objects",button_color="#1d8acf",conn=True)
                 continue
             if category ==18:
                 self.generate_side_lists_method_design(frame,category, title_of_text="Web-Results",button_color="#1d8acf",conn=True)
                 continue
             if category==10:
                 self.generate_side_lists_method_design(frame,category, title_of_text="Tools",button_color="#1d8acf",conn=True)
                 continue
 
             if category == 9000:
                 self.generate_side_lists_method_design(frame,category, title_of_text="4 Problem Change Sub-Methods",button_color="#1d8acf",conn=True)
                 continue
             
             if category == 4: # need to add a tools thing here
                 self.generate_side_lists_method_design(frame,category, title_of_text="Questions",button_color="#1d8acf",conn=True)
                 continue
             
             if category == 4:
                 self.generate_side_lists_method_design(frame,category, title_of_text="Questions",button_color="#1d8acf",conn=True)
                 continue
             else:
                 self.generate_side_lists_method_design(frame,category,button_color="#1d8acf",conn=True)
                 continue
         print("""questions to draft a method = 1
           galaxies of existing ideas = 2
           thing not useful to problem solving = 3
           questions to form connections = 4
           objectives to optimize towards = 5
           methods created = 6 
           problems i want to solve or tasks=7
           submethods for connections = 8
           submethods for method creation step = 9
           Tools, abstraction useful for making ideas easier for brain = 10 
           ideas on method to construct tasks for problem solving and process = 11
           question for step process = 12
           possible object=15
           web results = 18
           quesitons for strategy creation = 19""")## will need to make this happen
    def import_from_problem_table_for_method_building(self):
        """ import problem data into a way so that you can add it to a method as actions related to a strategy"""
        import re
        label_list=[]
        label=str(label)

        if galaxies_table == True:
            self.cur.execute(f"""SELECT problem_or_idea_root,qualities  FROM galaxies_table ;""")
            all_idea_in_database_list_format= self.cur.fetchall()
            for idea9 in all_idea_in_database_list_format: 
                problem_or_idea_root=idea9[0]
                #print(problem_or_idea_root)
                qualities=idea9[1]
                qualities=re.split(",",qualities)
                #qualities=re.split(",",qualities[1:-1])

                print(qualities)
                problem_or_idea_root
                problem_or_idea_root=re.sub(r"[;]","",problem_or_idea_root)
                galaxy=problem_or_idea_root + ";" + str(qualities)
                #galaxy=problem_or_idea_root + ";" + str(qualities[1:-1])

                galaxy=re.sub(r"[\'\[\]?]","",galaxy)
                # need to fix upstream problem of  there be weird things in the stream
                #  and be able to work with the string later
                # need to remove the quesitons marks
                label_list.append(galaxy)
            
                
                
                
        else:
            self.cur.execute(f"""SELECT updated_sentence FROM {table_name} WHERE updated_label = CAST({label} AS text) ;""")
            all_idea_in_database_list_format= self.cur.fetchall()
            for idea in all_idea_in_database_list_format: 
                label_list.append(str(idea))
                continue
            
            
        return label_list
    
        
        # will need to build in 
        return # list of problems with their actions and strategies in a format I can work with to add to another method
    def open_coding_base(self,event):
        """ """
        import sys
        import re
        import time
        import psycopg2
        from multiprocessing import Process
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\tkyinter_gui_glossary_master_code a 1.1.1.1.1')
        from tkinter_gui_glossary_master_code_functions import tkinter_gui_glossary_master_code_functions
        from tkinter_gui_glossary_master_code_functions import tkinter_gui_glossary_master_code_functions_child
        from tkinter_gui_glossary_master_code_functions import tkinter_gui_glossary_master_code_functions_gchild
        gui=tkinter_gui_glossary_master_code_functions()
        guic=tkinter_gui_glossary_master_code_functions_child()
        guigc=tkinter_gui_glossary_master_code_functions_gchild()
        data2=guic.load_in_gui()
    def change_names_of_textboxes_strategy(self):
        """ """
        """ change names of all the boxes"""
        # store previous methods under submethods
        frames={self.frame2:19,self.frame4:10,self.frame5:20,self.frame7:9,self.frame3:15}# self.frame1:13  is connecte dobjectds
        self.label1.config(text="Web Result Edit")
        self.label2.config(text="Strategy display =,`coding engineer /,law all,investment all")
        self.label3.config(text="Current Method Step")
        self.label4.config(text="Idea-Tool Editing")
        for  frame, category in frames.items():
            for widget in frame.winfo_children():
                widget.destroy()  
            if category ==15:
                # related to a specific box because of frame and specific category of information to load in
                self.generate_side_lists_method_design(frame,category, title_of_text="Actions",conn=False)#3
                continue
            if category ==20:
                self.generate_side_lists_method_design(frame,category, title_of_text="Effects",conn=False)#5
                continue
            if category == 9:
                self.generate_side_lists_method_design(frame,category, title_of_text="4 Problem Change Sub-Methods",conn=False,sub_method=True)#7 #
                continue
            if category == 19:
                self.generate_side_lists_method_design(frame,category, title_of_text="Questions",conn=False)#2
                
            if category ==10:
                self.generate_side_lists_method_design(frame,category, title_of_text="Tools",conn=False)#4
        print("""questions to draft a method = 1
          galaxies of existing ideas = 2
          thing not useful to problem solving = 3
          questions to form connections = 4
          objectives to optimize towards = 5
          methods created = 6 
          problems i want to solve or tasks=7
          submethods for connections = 8
          submethods for method creation step = 9
          Tools, abstraction useful for making ideas easier for brain = 10 
          ideas on method to construct tasks for problem solving and process = 11
          question for step process = 12
          possible object=15
          web results = 18
          quesitons for strategy creation = 19
          effects = 20""")
    def upload_strategy_dictionary_to_box(self):
        """ edit this to pull from strategy table when ready"""
        self.cur.execute(f""" SELECT problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions From strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        self.listbox2.delete(0, tk.END)
        strategy_entries= self.cur.fetchall()
        # still need to remove  question marks
        # need to delete all previous entries
        #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
        for objecttt in strategy_entries:
            #id 0 #problem 1 # step name 2 #tool 3 #ideas 4 # optimize 5 # order 6 #time 7
            problem_being_solved=objecttt[0]
            question_or_tool_for_strategy=objecttt[1]
            problem_web_variables=objecttt[2]
            effects=objecttt[3]
            time_found=objecttt[4]
            actions=objecttt[5]
            
            self.listbox2.insert(tk.END, f"{actions}") 
            
            
        ########
        
        
            
    
    def generate_random_id(self):
        """genereate a random username and random password with certain parameters """
        import random
        import re
        import string
        num_dic={}
        character_dic={n:ch  for n, ch in enumerate(string.ascii_lowercase)}
        #create_password
        id_str=" ###"
        for i in range(20): 
            random_int=random.randint(0,25)
            character=str(character_dic[random_int])
            remainder=i % 2
            if remainder:
                find_if_character=re.search(r"[a-z]",character)
                if find_if_character:
                    character=character.upper()      
            id_str+=character
        id_str+=""
        return id_str
    def change_to_strategy_window(self,event):
        """this will change when the 3:strategy is pressed """
        print('hi')
        
        self.change_names_of_textboxes_strategy()
        try:
            self.generate_problem_webb()
        except:
            print("error")
        self.upload_strategy_dictionary_to_box()
    
    def create_strategy_dict_or_modify(self): 
            """ update dictionary adding new step or  modifying existing step """
            import re
            import time
            import copy
            time_method_found =time.time()
            self.cancel=False
            self.delimiter_dicitonary_for_method= {"#":"placement", "=":"idea_web",  "[": "action_strategy_label", "/":"effects","]":"actions_content","\'":"problem_preventing_action" }
            self.placement_dictionary= {"placement":3,"idea_web":1,"action_strategy_label":5,"effects":2,"actions_content":6,"problem_preventing_action":8}
            #unwanted_terms_str = "/#=\]\["
            self.strategy_list=[]# need to double check thisss
            self.previous_strategy_list=copy.deepcopy(self.strategy_list)
            content=self.text_box01.get('1.0', 'end') # textbox01 is the strategy window need to test this
            self.strategy_list=[time_method_found,[],[],[],[],[]] # problem # 1 is there because it is the second entry in this steps list of lists
            content=re.split(r"([/=\]])",content)# will need to test this
            stored_delimiter=""
            print(content)
            for qual3 in content:
                qual3=re.sub("\n","",qual3)
                if  qual3 in "/]":
                    stored_delimiter=qual3
                    continue
                else:
                    if stored_delimiter=="]": # this a strategy
                        id_str=self.generate_random_id()# will need to test this
                        qual3=f"?? how do i {str(qual3)}?"
                        qual3=qual3+id_str
                        self.strategy_list[1].append(qual3)
                        print('action')

                    if stored_delimiter=="/":
                        self.strategy_list[2].append(qual3)
                        print('objective or effect')
                    if stored_delimiter=="":
                        id_str=self.generate_random_id()# will need to test this
                        qual3=f"?? how do i {str(qual3)}?"
                        qual3=qual3+id_str
                        self.strategy_list[1].append(qual3)
                        print('action')
            #self.strategy_list[3].append(self.ideas_list_for_method)
            #self.strategy_list[4].extend(self.recorded_question_or_tool_for_method_list)# will need to check this
            #self.strategy_list[5].append(self.past_problemm)

            #self.method_list_dictionary[step_name][1][5].extend(self.actions_for_method)
            #self.method_list_dictionary[step_name][1][6].extend(self.strategy_or_method_label_for_methods)            
            self.recorded_question_or_tool_for_method_list=[]
            self.objective_list_for_method=[]
            self.ideas_list_for_method=[]
            self.actions_for_method=[]
            self.strategy_or_method_label_for_methods=[]
            self.past_problemm=""
            return self.strategy_list
     
        
        
    def save_strategy_dictionary_to_database(self) :
            """ take the method list dictitonary and bring it to database for methods disassembling it and uploading it""" 
            import re
            from multiprocessing import Process
            import sys
            sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')

            if self.cancel==True:
                print('hi')
                return "cancelled"
            time_found_list=self.strategy_list[0]
            action_related_to_strategy=self.strategy_list[1]
            objective_list=self.strategy_list[2]
            idea_web_list=self.strategy_list[3]
            tool_or_question_list=self.strategy_list[4]
            past_problemm=self.strategy_list[5]
            time_found_list_list=[time_found_list]
            
            time_found_list_list=re.sub('\'',"",str(time_found_list_list))
            time_found_list_list=re.sub('\"',"",time_found_list_list)
            time_found_list_list=re.sub('\n',"",time_found_list_list)
            
            time_found_list=re.sub('\'',"",str(time_found_list))
            time_found_list=re.sub('\"',"",time_found_list)
            time_found_list=re.sub('\n',"",time_found_list)
            
            
            action_related_to_strategy=re.sub('\'',"",str(action_related_to_strategy))
            action_related_to_strategy=re.sub('\"',"",action_related_to_strategy)
            action_related_to_strategy=re.sub('\n',"",action_related_to_strategy)
            
            objective_list=re.sub('\'',"",str(objective_list))
            objective_list=re.sub('\"',"",objective_list)
            objective_list=re.sub('\n',"",objective_list)
            
            idea_web_list=re.sub('\'',"",str(idea_web_list))
            idea_web_list=re.sub('\"',"",idea_web_list)
            idea_web_list=re.sub('\n',"",idea_web_list)
            
            tool_or_question_list=re.sub('\'',"",str(tool_or_question_list))
            tool_or_question_list=re.sub('\"',"",tool_or_question_list)
            tool_or_question_list=re.sub('\n',"",tool_or_question_list)
            
            past_problemm=re.sub('\'',"",str(past_problemm))
            past_problemm=re.sub('\"',"",past_problemm)
            past_problemm=re.sub('\n',"",past_problemm)

            
            if  len(self.previous_strategy_list)>=1: #need
                #print("7")
                #strategy_action is the label
                self.cur.execute( f""" UPDATE strategy_table 
                                 Set question_or_tool_for_strategy= '{str(tool_or_question_list)}', problem_web_variables = '{str(idea_web_list)}',
                                 effects = '{str(objective_list)}', time_found = '{str(time_found_list)}',actions ='{str(action_related_to_strategy)}', 
                                 WHERE problem_being_solved = '{str(self.problem_recorded)}' ;""")
            else:
                self.cur.execute( f""" INSERT INTO strategy_table (problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions)
                         VALUES ('{str(self.problem_recorded)}','{str(tool_or_question_list)}','{str(idea_web_list)}','{str(objective_list)}','{str(time_found_list)}','{str(action_related_to_strategy)}');""")
            
            
            
            for action in self.strategy_list[1]:# need to test this
                action=re.sub('\'',"",str(action))
                action=re.sub('\"',"",action)
                action=re.sub('\n',"",action)# check this
                # multiprocess this shit
                self.cur.execute( f""" INSERT INTO auto_problem_table (problem_question_or_task,specific_problem_or_object,tool_or_question_per_conn_list,qualitity_list,time_created_conn,initial_creation)
                         VALUES ('{str(action)}','{str(action)}','{str([])}','{str([])}','{str(time_found_list_list)}','{str(time_found_list)}');""")
                print('TEST')
                #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
                # going to affect them when they age
                #from Problems_functions import problems_functions
                #from Problems_functions import methods_window_program
                from create_auto_create_problem_tree_and_web import create_auto_create_problem_tree_and_web
                #from problem_solving_project_gui_10 import buttons_per_quadrant
                #buttons=buttons_per_quadrant()
                auto_prob_web_tree=create_auto_create_problem_tree_and_web()
                process = Process(target=auto_prob_web_tree.auto_create_problem_web_and_galaxy,args=(action,))
                #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))              
                process.start()
            self.conn.commit() 
            # clear strategy list so dont write multiple same strategy twice
            self.strategy_list=[]         
        
    def reupload_strategy_dictionary(self):
            """ take the method list dictitonary and bring it back into the program  from sql database"""
            self.cur.execute(f""" SELECT problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions From strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
            self.listbox2.delete(0, tk.END)
            strategy_entries= self.cur.fetchall()
            # still need to remove  question marks
            # need to delete all previous entries
            #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
            for objecttt in strategy_entries:
                #id 0 #problem 1 # step name 2 #tool 3 #ideas 4 # optimize 5 # order 6 #time 7
                problem_being_solved=objecttt[0]
                question_or_tool_for_strategy=objecttt[1]
                problem_web_variables=objecttt[2]
                effects=objecttt[3]
                time_found=objecttt[4]
                actions=objecttt[5]     
                self.listbox2.insert(tk.END, f"{actions}") 
    
    def upload_prompts(self,prompt_type):
       """ use questions in """
       return
       sql_str=f"SELECT * FROM prompt_table WHERE prompt_type='{prompt_type}';"
       try:
           self.cur.execute(sql_str)
       except Exception as E:
           print(E)    
       sql_data_list_list= self.cur.fetchall()
    def create_prompts(self,action,prompt_list):
     '''NEED TO START FAST API ON BIGBLACK WITH'''
     out_prompt_list=[]
     for action in self.strategy_list[1]:# need to test this
             action=re.sub('\'',"",str(action))
             action=re.sub('\"',"",action)
             action=re.sub('\n',"",action)# check this
             #edit action to get rigth prompt
             prompt=action+stuff
     return out_prompt_list
     
    def query_website_and_api_running_llamma(self,prompt):
     ''' '''    
     import requests
     # USE THESE COMMANDS TO START API
     #http://192.168.2.200:8000 # big black
     #ssh desktop-s7na8dm\doggo777@192.168.2.214
     #http://192.168.2.214:8000/# big white 
     #>ssh desktop-s7na8dm\doggo777@192.168.2.214
     #cd Documents\psp_api
     #.\venv\Scripts\activate
     #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     url = "http://192.168.2.214:8000/items/"
     params = {
       "prompt": "{prompt}",
       "price": 999.99}
   # Send GET request to FastAPI server with query parameters
     response = requests.get(url, params=params)
     # Send POST request to FastAPI server
     print(response.json())
     # Check if the request was successful
     if response.status_code == 200:
         # Parse and print the response JSON
         response_data = response.json()
         response_str=response_data['name']['content']
         # process data here
         print("Response from FastAPI:")
         print(response_str)         
     else:
         print(f"Failed to get response, status code: {response.status_code}")   
     return response_str
 

    def llama_generate_coding_environment(self,strategy_list):
        """generate_coding_environment
        going to skip this till i can get gpu to run faster
        """
        import re
        coding_environment_dic={}
        self.upload_prompts("")
        prompt_list=["what does {ACTION} mean in the context of coding in python","when is {ACTION} important in coding",]
        prompt_list=self.create_prompts()
        for actionn in strategy_list:
            for promptt in prompt_list:
                final_query=re.sub(r"ACTION",actionn,promptt)
                response_str =self.query_website_and_api_running(final_query) 
                # parse this and create prompt
                self.automated_coding_psp_info_dic["intital_env_prompts_list"].append(final_query)
                self.automated_coding_psp_info_dic["intital_action_list"].append(actionn)
                self.automated_coding_psp_info_dic["intital_env_response_str_list"].append(response_str)

                
                coding_environment_dic[final_query]={"actionn":actionn,"response_str":response_str,}
        return coding_environment_dic

    def llama_generate_coding_strats(self,coding_environment_dic):
        """ generate_coding_environment"""
        import re
        prompt_action_list_dic={}
        self.upload_prompts("")
        # repeat this for each step to create tree
        prompt_templates_coding_strat_list=["what are the steps i would take to ACTION"]
        #prompt_list=self.create_prompts()
        for final_query_key in coding_environment_dic.keys():
            actionn=coding_environment_dic[final_query_key]["actionn"]
            for prompt_template in prompt_templates_coding_strat_list:
                action_list_prompt=re.sub(r"ACTION",actionn,prompt_template)
            response_str =self.query_website_and_api_running_llamma(action_list_prompt)
            # break up actions in strategy
            action_list=re.split(r"[\.\?0-9]",response_str)# find best delimter here
            prompt_action_list_dic[action_list_prompt].append(action_list)
            
            self.automated_coding_psp_info_dic["intital_action_list_prompt_list"].append(action_list_prompt)
            self.automated_coding_psp_info_dic["intital_generated_action_list"].append(action_list)

        return prompt_action_list_dic
       
        
       
    def llama_generate_coding_script(self,prompt_action_list_dic):
        """generate_coding_environment """
        import re
        # write each response to a single coding file
        action_function_data_dic={}
        #self.upload_prompts("")
        prompt_templates_function_creation_list=["write a python function to ACTION"]
        prompt_list=self.create_prompts()
        for strategy in prompt_action_list_dic:
            for action in prompt_action_list_dic:
                for prompt_function_template in prompt_templates_function_creation_list:
                    input_prompt=re.sub(r"ACTION",prompt,prompt_function_template)
                function =self.query_website_and_api_running_llamma(prompt)
                action_function_data_dic[action].append(function)
                
                self.automated_coding_psp_info_dic["intital_funciton_prompt_list"].append(action)
                self.automated_coding_psp_info_dic["intital_generated_function_list"].append(function)
        return action_function_data_dic
    def create_auto_code_file_str(self,action_function_data_dic,problem_name):
        """ """
        coding_file_str=rf"""# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy
class {problem_name}():
 def __init__(self):
     print('start_pyautogui_class')""" 
        for action,function in action_function_data_dic.items():
            #write file str
            coding_file_str+=f"\n {function}"
        return coding_file_str
    def create_auto_code_file_str_test(self,action_function_data_dic,problem_name):
        """ """
        coding_file_str=rf"""# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy
class {problem_name}():
 def __init__(self):
     print('start_pyautogui_class')""" 
        for action_name,action_info in action_function_data_dic.items():
            fixed_function_code=action_info["fixed_function_code"]
            #write file str
            coding_file_str+=f"\n {fixed_function_code}"
        return coding_file_str
    
    def create_new_python_file(self,python_file_str,code_file_name):
        """create a python script with the values we just created """
        with open(f"{code_file_name}","w" ,encoding="utf-8") as f2:
            f2.write(python_file_str)  
    def create_new_input_file(self):
        """ """
        
        if update_file==True:
            file_name=problem_folder_path+f"\inputs"+f"\{building_function_name}"+f"{highest_file_number+1}"+".py"      
        if update_file==False:
            file_name=problem_folder_path+f"\inputs" +f"\{building_function_name}0.py"
        
    def process_coding_file(self,coding_file_name,coding_file_dic):
        """this function takes a coding file and divdes it into its line of code then organizes it so we can constrcut prompts to ask chatgpt or any generative model"""
        import re
        import time
        class_function_line_dic={"class_defined_line_number":[],
                           "class_name":[],
                           "function_defined_line_number":[],
                                              "function_name":[]}
        
        time_stamp = time.time()
        saved_class_line=""
        saved_function_line=""
        python_code_line_list=[]
        stored_glossary_code_dic={}
        whole_functions_dic={}
        function_defined_line_number=None
        class_line_number=None
        function_number_list_for_in_line_code={}
        package_to_describe=re.compile(r"\(.*?\)")
        re.compile("")
        with open(rf"{coding_file_name}", "r",encoding="utf8") as f:
            try:
                coding_file=str(f.read())
            except:
                print(' FAILED TO  FIND CODING  FILE')
                return coding_file_dic, class_function_line_dic

        python_script_split_lines=coding_file.splitlines()
        function=False
        # first run to get whole functions
        for line_number,line in enumerate(python_script_split_lines):
            docstring=""
            function_str_test=line.strip()
            function_search=False
            if function_str_test[:3]=="def":
                saved_function_name_line=line
                current_function_lines=f"{line}\n"
                function=True
                continue
            if function==True:
                current_function_lines+=f"{line}\n"
                whole_functions_dic[saved_function_name_line]=current_function_lines
            #save the functions 
        function=False
        for line_number,line in enumerate(python_script_split_lines):
            line_number= line_number +1
            class_function_str_test=line.strip()
            function_search=False
            if class_function_str_test[:5]=="class":
                print(f"class_line: {line}")
                try:
                    class_name=re.search(r"class (.*)\(",line).group(1)
                    saved_class_line=line
                    class_line_number=line_number
                except:
                    continue
                class_function_line_dic["class_defined_line_number"].append(line_number)
                class_function_line_dic["class_name"].append(class_name)


                
                continue 
            if class_function_str_test[:3]=="def":
                try:
                    function_name=re.search(r"def (.*)\(",line).group(1)# may need to rewrite this
                except:
                    print('NOT REAL FUNCTION')
                    continue


                function_search=True 
                #function_name=f"{line}"
                class_function_line_dic["function_name"].append(function_name)
                class_function_line_dic["function_defined_line_number"].append(line_number)
                function_defined_line_number=line_number
                #class_function_line_dic["function_name"].append(function_name)
                #class_function_line_dic["function_defined_line_number"].append(line_number)
            #class_search=re.search(r"class[\s]+[a-zA-Z].*:",line)
            #function_search=re.search(r"[\s\t]+def .*:",line)
            if function_search:
                saved_function_name_line=line
                line_number_of_doc_string=line_number
                try:
                    docstring=python_script_split_lines[line_number_of_doc_string]
                except Exception as E: 
                    print(E)
                function=True
                continue
            if function==True:
                is_a_package_to_describe=re.search(package_to_describe,line)
                if  is_a_package_to_describe:
                    line_of_code=line.strip()
                    coding_file_dic["function_name"].append(function_name)
                    if function_defined_line_number:
                        coding_file_dic["function_defined_line_number"].append(function_defined_line_number)
                    else:
                        coding_file_dic["function_defined_line_number"].append(line_number)
                    if class_line_number:
                        coding_file_dic["class_created_line_number"].append(class_line_number)
                    else:
                        coding_file_dic["class_created_line_number"].append(line_number)
                    coding_file_dic["docstring"].append(docstring)
                    coding_file_dic["line_of_code"].append(line_of_code)
                    coding_file_dic["code_base_function"].append(whole_functions_dic[saved_function_name_line])
                    coding_file_dic["code_file_name"].append(coding_file_name)
                    coding_file_dic["class_name"].append(saved_class_line)
                    coding_file_dic["line_number_in_file"].append(line_number)
                    coding_file_dic["time_stamp"].append(time_stamp)
                    
        return coding_file_dic, class_function_line_dic
    def create_input_function_file_str(self,code_file_name_only,problem_function_folder_path,problem_name,function_name):
        """ """
        import time
        import os
        import re
        from datetime import date
        todayy=date.today()
        timeee=time.time()  
        words_in_function_file_name=problem_name.split("_")
        first_word_in_function_file_name=words_in_function_file_name[0]
        class_init_str="" 
        inputt_file_str=rf"# -*- coding: utf-8 -*-\n"+f"Created on {todayy} {timeee}  @author: yyyyyyyyyyyyyyyyyyyy"
        inputt_file_str+="\nif __name__ == '__main__':"
        inputt_file_str+="\n import sys"
        inputt_file_str+=f"\n sys.path.append(r'{problem_function_folder_path}')"
        inputt_file_str+=f"\n from {code_file_name_only} import {problem_name}"
        class_init_name =f"{first_word_in_function_file_name}"
        inputt_file_str+=f"\n {class_init_name}={problem_name}()" 
        # figure out inputs as well later when i have energy
        inputt_file_str+=f"\n {class_init_name}.{function_name}()" 

       
        #if len(building_file_dic["inputs"])>1:
        #    inputt_listt=[]
        #    for inputt in building_file_dic["inputs"]:
        #        if inputt=="self":
        #            continue
        #        inputt_file_str+= f"\n {inputt}="
        #        inputt_listt+=f"{inputt},"
        #else:
        #    inputt_listt=""
        return inputt_file_str
    
    
    def write_auto_coding_file_and_dir(self,action_function_data_dic,first_action,testt=False):
        """ """
        import time
        import os
        import re
        from datetime import date
        input_function_file_name_to_test_dic={}
        root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\auto_created_code"
        auto_code_file_dir_list=os.listdir(root_folder)
        # get the name of the folder to hold the file
        # if there is a problem use that
        # otherwise use 
        if self.problem_recorded:
            problem_name=self.problem_recorded
        else: 
            # use the first action if starting from scratch
            problem_name=first_action
        problem_name=re.sub(r"[^a-zA-Z0-9 ]", "", problem_name)# check this
        problem_name=re.sub(r"[ -]","_",problem_name)     
        self.dir_to_store_script=root_folder+"\\"+problem_name  
        self.dir_to_store_script_linux=r"/home/jross77/Documents/Coding/auto_created_code/"+problem_name
        self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
        self.dir_to_store_script_linux=re.sub(r"[ -]","_",self.dir_to_store_script_linux)
        problem_inputs_folder=self.dir_to_store_script+"\inputs"
        Problem_building_folder=self.dir_to_store_script+"\building"
        if problem_name not in auto_code_file_dir_list:
            os.mkdir(self.dir_to_store_script)
            # create sub buidling and input folders
            os.mkdir(problem_inputs_folder)
            os.mkdir(Problem_building_folder)  
        # create str for the file
        if testt==True: 
            python_file_str=self.create_auto_code_file_str_test()
        else:
            python_file_str=self.create_auto_code_file_str(action_function_data_dic,problem_name)    
        # create exe files
        # create file name for differnet files
        # look to coding program for gudiance on how to do this
        # need to create input folder
        todayy=date.today()
        timeee=time.time()    
        code_file_name_only=problem_name+str(todayy)+ "  "+str(timeee)
        code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
        code_file_name_path=self.dir_to_store_script+"\\"+ code_file_name_only+".py"
        code_file_name_no_path_for_function_import=code_file_name_only
        self.create_new_python_file(python_file_str,code_file_name_path)
        coding_file_dic={
        "line_of_code": [], 
        "code_base_function": [],
        "code_file_name":[] , 
        "class_name":[],
        "line_number_in_file":[],
        "docstring":[],
        "time_stamp":[],
        "function_name":[],
        "function_defined_line_number":[],
        "class_created_line_number":[] }
        coding_file_dic,class_function_line_dic=self.process_coding_file(code_file_name_path,coding_file_dic)
        used_function_name_list=[]
        for function_name in coding_file_dic["function_name"]:
            if function_name not in used_function_name_list:
                inputt_file_str=self.create_input_function_file_str(code_file_name_only,self.dir_to_store_script,problem_name,function_name)
                input_function_file_name=function_name+str(todayy)+ "  "+str(timeee)
                code_file_name_only=re.sub(r"[ -\.]","_",input_function_file_name)                
                input_function_file_name_with_path=problem_inputs_folder+"\\"+ input_function_file_name+".py"
                self.create_new_python_file(inputt_file_str,input_function_file_name_with_path)
                used_function_name_list.append(function_name)
                input_function_name_input_file_name_dic[function_name]=input_function_file_name_with_path
                
        return input_function_name_input_file_name_dic,problem_name
    

                

    def test_code_created(self,input_function_name_input_file_name_dic):
        """run the code in terminal if there is a error add to fix code if errors list"""
        #; activate virtual envrionment then run manage.py runserver
        import copy
        input_function_name_input_file_name_dic_with_errors=copy.deepcopy(input_function_name_input_file_name_dic)
        for function_name, function_input_file_name in input_function_name_input_file_name_dic.items():
            run_script_input = [f"python",f"{function_input_file_name}"]
            # need to locate function code here
            # and use it to 
            function_code=""
            try:
                subprocess.run(run_script_input, check=True,shell=True,capture_output=True, text=True)
                stdout = result.stdout
                stderr = result.stderr
                print("Standard Output:", stdout)# standard ouytput
                print("Standard Error:", stderr) # error message
                if stderr:
                    self.errorrr=True
                    self.automated_coding_psp_info_dic["testing_intital_function_name_list"].append(function_name)
                    self.automated_coding_psp_info_dic["testing_intital_function_code_list"].append(function_code)
                    self.automated_coding_psp_info_dic["testing_intital_function_error_list"].append(stderr)

                   
                    input_function_name_input_file_name_dic2[function_name] ={'error':stderr,'function_code':function_code}      
            except subprocess.CalledProcessError as e:
                print(e)         
        return input_function_name_input_file_name_dic_with_errors
        # if its a install error just pip install the package automatically build this in
        # retreive output of the code
        # if there is a error 
        # add to fix code error list
        #
    def fix_code_if_errors(self,input_function_name_input_file_name_dic_with_errors):
        """ just use write code to fiel for this one"""
        import re
        # write each response to a single coding file
        prompt_templates_function_creation_list=["Fix this error {ERROR} in this function {FUNCTION_CODE}"]
        action_fixed_error_function_dic={}
        for function_name,error_path_code_dic  in input_function_name_input_file_name_dic_with_errors.items():
           error=error_path_code_dic['error']
           function_code=error_path_code_dic['function_code']
        prompt_list=self.create_prompts()
        for strategy in prompt_action_list_dic:
            for action in prompt_action_list_dic:
                for prompt_function_template in prompt_templates_function_creation_list:
                    input_prompt=re.sub(r"ERROR",error,prompt_function_template)
                    input_prompt=re.sub(r"FUNCTION_CODE",function_code,input_prompt)
                    fixed_function =self.query_website_and_api_running_llamma(input_prompt)
                    self.automated_coding_psp_info_dic["testing_fixed_funciton_code_list"].append(fixed_function)
                    self.automated_coding_psp_info_dic["testing_input_prompt_list"].append(input_prompt) 
                    function_name_fixed_funciton_content_dic[function_name]={"fixed_function_code":fixed_function,
                                                                   "og_function_code":function_code,
                                                                   "function_name":function_name,
                                                                   "input_prompt":input_prompt,
                                                                   "error":error}    
        # add these to the existing file project and create a new coding file str
        return action_fixed_error_function_dic
    
    # insert output into a new coding file
    def write_to_auto_coding_dir(self,input_function_name_input_file_name_dic_with_errors):
        """ just use write code to fiel for this one"""
        import re

    ##### psp
    def generate_psp_environment(self,strategy):
        """generate_coding_environment going to skip this till i can get gpu to run faster"""
        import re
        problem_environment_psp={}
        self.upload_prompts("")
        psp_enviornment_prompt_list=["what does OBJECT mean in the context of this question action ACTIONN"]
        for actionn in strategy_list:
            actionn_word_list=re.split(" ",actionn)
            for action_word in actionn_word_list:# will need to use spacy for his
              for prompt_env in psp_enviornment_prompt_list:
                 prompt_env= re.sub(r"OBJECT",action_word,prompt_env )
                 response_str =self.query_website_and_api_running_llamma(prompt_env)
                 self.automated_psp_info_dic["prompt_env_list"].append(prompt_env)
                 self.automated_psp_info_dic["env_response_str_list"].append(response_str)

                 problem_environment_psp[prompt_env] = response_str
                 self.automated_psp_info_dic
        return problem_environment_psp 
    
    def genrate_psp_glossary(self,problem_environment_psp):
         """generate_coding_environment """
         import re
         psp_glossary_dic={}
         self.upload_prompts("")
         psp_glossary_prompt_list=["what is the definiton of OBJECT  in the context of CONTEXT "]
         prompt_list=self.create_prompts()
         for prompt_env,context_of_prompt in problem_environment_psp.items():
             response_data=re.split(" ",response_data)
             for action_word in actionn_word_list:# will need to use spacy for his
               for prompt_g in psp_glossary_prompt_list:
                   final_prompt_g= re.sub(r"OBJECT",action_word,prompt_g )
                   final_prompt_g= re.sub(r"OBJECT",context_of_prompt,final_prompt_g )
                   response_data =self.query_website_and_api_running_llamma(final_prompt_g)
                   self.automated_psp_info_dic["prompt_glossary_list"].append(prompt_g)
                   self.automated_psp_info_dic["glossary_response_str_list"].append(response_data)

                   psp_glossary_dic[prompt_g].append(response_data)                 
         return psp_glossary_dic 
         
    def generate_psp_strats(self,problem_environment_psp):
        """generate_coding_environment """
        import re
        prompt_strat_data_dic={}
        self.upload_prompts("")
        for prompt_env,response_str in  problem_environment_psp.items():
            psp_strats_prompt_list=["what are steps i would take to ACTIONN"]
            #prompt_list=self.create_prompts()
            response_str_list=re.split(" ",response_str)
            for action_word in response_str_list:# will need to use spacy for his
                for prompt_strat in psp_strats_prompt_list:
                    prompt_strat= re.sub(r"ACTIONN",action_word,prompt_strat )
                    #final_prompt_g= re.sub(r"OBJECT",context_of_prompt,final_prompt_g )
                    strat_str =self.query_website_and_api_running_llamma(prompt_strat)
                    response_data_dic[prompt_strat]=strat_str
                    self.automated_psp_info_dic["prompt_strat_list"].append(prompt_strat)
                    self.automated_psp_info_dic["strat_response_str_list"].append(strat_str)

        return psp_prompt_strat_data_dic 
        
    def upload_to_remote_server_postgres(self,table_name,dictionary_of_values):
        """ find tables that should be added to and add the code  """
        import psycopg2
        import re
        from psycopg2 import sql
        host = '192.168.2.209'  # E.g., '192.168.1.100' or 'your-database-server.com'
        port = '5432'  # Default PostgreSQL port
        dbname = 'canlawaccessible'  # E.g., 'myprojectdb'
        user = 'jross77'  # E.g., 'myuser'
        password = 'MeganisGreat'  # E.g., 'mypassword'
        try:
            self.conn = psycopg2.connect(host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password)
            
            self.cur = self.conn.cursor() 
            
            print("Connection successful!")
            for i, (table_column, column_value) in enumerate(dictionary_of_values.items()):
                column_value=str(column_value)
                column_value=column_value.replace("\'","")
                column_value=column_value.replace("\"","")
                column_value=column_value.replace(","," ")
                column_value=column_value.replace("'","")
                column_value=re.sub("\"","",column_value)
                if i ==0:
                    table_columns =  f"{table_column}"
                    values_string = f"'{column_value}'"
                    continue
                else:
                    table_columns=  table_columns+f",{table_column}"
                    values_string= values_string+f",'{column_value}'"
                    continue
            sql_str=f"INSERT INTO {table_name} ({table_columns}) VALUES ({values_string});"
            try:
                self.cur.execute(sql_str)
            except Exception as E:
                print(E)
                
            self.conn.commit()
        except Exception as e:
                print(f"Error: {e}")
                
        self.cur.close()
        self.conn.close()
        print("Connection closed.")
        
        
    def upload_sql_data_from_remote_server(self, column_value,column_name,table_name):
        """ show al the webpages we opened, show the information in a nice format that we can use to solve a problem"""
        # send queires to upload from various tables
        self.auto_problem_info_dic={}
        import psycopg2
        import select
        import time
        import re 
        host = '192.168.2.209'# ip address here
        port = '5432'
        dbname = 'canlawaccessible'
        user = 'jross77'
        password = 'MeganisGreat' 
        newest_pyautogui_light_table=self.find_newest_pyautogui_light_table()
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password)  
        self.cur = self.conn.cursor()      
        print("connection started")      
        sql_str_pyauto_gui_light=f"SELECT* FROM {table_name} WHERE {column_name}={column_value}"
        sql_str_pyauto_gui_used_id=f"SELECT used_my_id_value FROM used_id_pyautogui_table"# dont need to interact with master
        self.cur = self.conn.cursor()# create new cursor          
        self.cur.execute(sql_str_pyauto_gui_used_id)                
        pyauto_gui_light_data_list_list= self.cur.fetchall() 
        return pyauto_gui_light_data_list_list
    
        
    def add_strategy(self,event):
        #create_dict_or_modify()      
        strategy_list=self.create_strategy_dict_or_modify()
        self.save_strategy_dictionary_to_database() # NEED TO  open internet tabs i visit so i can see them for each problem
        self.reupload_strategy_dictionary() 
        
        # coding program actions: GET THIS DONE TONIGHT AND RUNNING
        # add a delimiter to distiguish?
        # wont be able to use import sql functions on this do i want that
        # or store two seperate tables
        # how do i store this best
        self.automated_coding_psp_info_dic={
        "problem_name":self.problem_recorded,
            
            
        "intital_env_prompts_list":[],
        "intital_action_list":[],
        "intital_env_response_str_list":[],
        
        "intital_generated_action_list_list":[],
        "intital_action_list_prompt_list":[],
        
        
        "intital_funciton_prompt_list":[],
        "intital_generated_function_list":[],

       
        #test related data try to fix errors mutliple times in functions
        # and have procedures to fix these errors
        # test all functions to get them to work in venv?        
        "testing_intital_function_name_list":[],
        "testing_intital_function_code_list":[],
        "testing_intital_function_error_list":[],
        "testing_fixed_funciton_code_list":[],
        "testing_input_prompt_list":[],       
        # make a list of functions that are working on a single iteration?
        }# final entry in testing will be final good code str
        # delimit with #####?
        # one entry to table per run through this
        coding_problem_environment_prompts=self.llama_generate_coding_environment(strategy_list)
        prompt_action_list_dic=self.llama_generate_coding_strats(coding_problem_environment_prompts)
        action_function_data_dic=self.llama_generate_coding_script(prompt_action_list_dic)
        input_function_name_input_file_name_dic,problem_name=self.write_auto_coding_file_and_dir(action_function_data_dic,strategy_list[0])
        # created intital coding file  
        # test and fix any errors using science principles
        self.tests=0
        while True: # recurse until all functions run in code keep track of function
            self.errorrr=False       
            input_function_name_input_file_name_dic_with_errors=self.test_code_created(input_function_name_input_file_name_dic)# in execute file            
            function_name_fixed_funciton_content_dic=self.fix_code_if_errors(input_function_name_input_file_name_dic_with_errors) # fix code retrieve error from console  
            input_function_name_input_file_name_dic,problem_name=self.write_auto_coding_file_and_dir(function_name_fixed_funciton_content_dic,strategy_list[0], testt=True)
            # need to change this to be action as key so it fits into this function
            #updated_python_file_str=self.create_auto_code_file_str_test(function_name_fixed_funciton_content_dic,problem_name)
            #self.update_problem_auto_coding_files_dir(updated_python_file_str)
            self.tests+=1
            print(self.errorrr)
            # if its a import issue then automaitcally write bash script to import
            # and fix problems to make this work as they come up
            if self.errorrr==True and self.tests<=5:
                continue            
            else:
                self.write_final_coding_file_info_to_sql(self.automated_coding_psp_info_dic,updated_python_file_str,file_name)        
                break            
        # write updated coding file data to database        
        #self.send_coding_program_llama_info_to_sql(self.automated_coding_psp_info_dic)
        self.upload_to_remote_server_postgres("automated_psp_coding",self.automated_coding_psp_info_dic)# use listneer to retrieve data
        #self.upload_to_local_server_postgres("automated_psp_coding",self.automated_coding_psp_info_dic)# use listneer to retrieve data
        ### problems sovling program
        self.automated_psp_info_dic={
            "problem_name":self.problem_recorded,          
            "prompt_env_list":[],
            "env_response_str_list":[],
            "prompt_glossary_list":[],
            "glossary_response_str_list":[],
            "prompt_strat_list":[],
            "strat_response_str_list":[] }
        problem_environment_psp=self.generate_psp_environment(strategy_list)# use questions
        psp_glossary_dic=self.genrate_psp_glossary(problem_environment_psp) # open this once generated
        psp_prompt_strat_data_dic=self.generate_psp_strats(problem_environment_psp) # use strats and display and save them in a table 
        self.upload_to_remote_server_postgres("auto_psp_table",self.automated_psp_info_dic) 
        # GET THIS TO RUN AS DJANGO SITE to manage all these pages, run as local host, and from remote server
        # open show psp problem content for engineering and everythng else
        subprocess.Popen(["python", "show_all_psp_problem_content_from_remote_server.py",f"{self.problem_recorded}"])
        
        psp_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        auto_coding_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        engineer_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        investment_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        business_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        law_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        negoiation_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        self.open_show_glossary(psp_problem_data)
        self.open_show_webpages()
        self.open_show_problem_window()
        self.open_show_coding_program(auto_coding_problem_data)
        self.open_show_final_coding_file()
        self.open_show_engineering_files_and_window(engineer_problem_data)
        self.open_show_investment_finance_window(investment_problem_data)
        self.open_show_business_window(business_problem_data)
        self.open_show_law_window(law_problem_data)
        self.open_show_all_sas_apps()
        #change this to show this in django site

        
        #self.show_all_psp_problem_content_from_remote_server(self.problem_recorded)  
        # incorporate pyautogui
        # engineering problem solving pipeline
        # use this on all crowd funding sites and anywhere else where engineers work 
        #crowd funding site to pull this off?
        # finish pypi coding program
        # need to actually upload results to 
        
        ### Engineering pipeline
        self.automated_engineer_info_dic={
            
            }
        
        self.build_enigneering_project() # then build engineering desing on each query 
        things_to_build="""
        BUILD PIZZA MAKER pizza lives matter
         build and lautch satltite
         build robotic arms
         buld co2 capture tech 
         build heart thing for brett
         build brain thing for mom
         build robot so dad doesnt have to feed birds in morning
         build large 3d printer
         robotic hand for using mouse
         build things that help the most people
         build things that make the most money
         need finance model to calcualte best materials and things to build
         combine it all so the product is affordable and scalble
         find all uses for things
        # build api with pyautogui this is not considered automated querying if just sneidn in text typed manually, but dont auto generate prmpts and send them in
        #### build all high value things with this which investors want
        financial, legal, medical/health, or related professional practices
        In a regulated area, including providing legal,
        financial, or medical advice or services,
        political campaigning or lobbying, 
        determining eligibility for financial products or creditworthiness,
        housing (leases and home loans), employment, or more generally for governmental decision-making, 
        such as law enforcement or immigration decisions."""
        ### recurse a million times
        # build something that builds every end product a engineer prodcues
        self.build_every_possible_type_of_business_you_can_build_ever()
        self.automatically_design_and_build_finance_and_engineering_models_from_open_source_course_and_text_book_data()
        self.learn_everything_in_buiness_and_finance_field_to_do_this_better()
        self.generate_business_ideas_program_that_will_beat_competitors_generate_most_revennue_and_types_of_revenue_streams_and_help_most_people() 
        self.do_market_research()# to figure out what should be built, and hwat people will buy and who can buy and who has money
        self.identify_business_revneue_streams() # where will you get money
        self.generate_revenue_projections_based_on_market_research()
        self.find_problme_people_want_solved()# find all possible ones
        self.generate_patent_design()# million differnet ones
        self.generate_cad_model() #million differnet ones
        self.generate_code_to_build_object_using_arms()# get all materials on hand
        self.send_code_to_use_robotic_arms_and_3d_printer_to_produce_prototype()# starcraft sort of
        self.generate_electirc_board_design()
        self.setup_possible_supply_chain_based_on_materials_in_design() 
        self.generate_manufacturing_equipment_required_to_build_find_best_route()
        self.find_cheapest_alternative_online_for_each_product()
        self.compare_alternative_patent_and_cad_product_generated_to_solve_problem_and_ensure_design_chosen_is_informed_by_finance_and_manufacturing_models_to_ensure_its_cheap_and_affordable_to_make_and_scale()
        self.setup_marketing_of_product() # in this case co2 cpature and other life saving products
        self.setup_ecommerce_website_crowd_funded()
        self.setup_business_website()
        self.delegation_program()
        self.generate_busienss_plan()# maybe propectus
        self.generate_prospectus() # this will show how the business will make money
        self.generate_balance_sheet_and_other_financial_documents()
        self.raising_money_crowd_funding()
        self.build_factory_purchase_manufacturing_equipment_with_money()
        self.find_buyers_and_sell()# marketing
        self.sell_product()
        self.model_to_automatically_do_science()
        self.gen_moleuclar_creator_and_finder()# for materials could figure out how to produce industrial equipment from trash metals this way  
        self.generate_energy_generation_business_or_electronics()
        self.use_recycled_metal_transform_into_industrial_robotics_systems() # hire someone to pick up metal and contract with dumps
        self.plan_all_steps_ahead_to_best_build_engineer()

        # make it write arguments
        # build model that takes input of aciton you want osmeone to take
        # and what you have to do to make them take that action like thought input
        # THIS IS ESSENTIALLY THE LAW MODEL
        self.build_negoiation_argument_model()# use fia nn
        self.scrape_all_possible_arguments()
        self.prompt_possible_arguments_model()
        self.generate_script_for_negoiaitons_bargaining_ranges_most_perusaive_psychology()
        
        # find all possible arguments
        # always do the right thing with all of this and help people
        #meaning improving your physical and mental health maybe give them more property
        
        # find things being ar
        # neogitiate with banks if bettyer alternartive in crypto do it
        # Build a neogtiaiton/legal program to get best price:
        # essenitally build a program to complete any task
        # so i cna do it better
        # when try to supply model onto a demand product
        #youtube demand model, your input are the signals that drive the output
        # broadcasting policy objectives
        #solve for a percentage a quota natural origin of the user
        # privacy and secruity issues
        # cyber security something to encourage
        self.build_investment_project()
        ### build investing project FINAICIAL MODEL
       
        # use the stuff i learn in the course here
        # Build model to figure out best monetary way to invest time and energy
        # figure out best investment actions to take
        # make list of all possible htings to invest in ror actions you could do with youre money and time
        # figure out cost and benefits to investing in them given data
        # predict return on investment
        #add other indicators and model the investments
        #fixed income securities debt that pay interest over time
        self.gather_list_of_all_possible_actions_you_could_invest_time_or_money_in()# stock trading business or just selling antiques
        self.assess_time_and_risk_only_reaosn_finance_industry_exists()
        self.measure_return_on_invesmtent_model()
        self.accounting_program_profit_revenues_loss()#assets liaiblties
        self.create_model_to_suggest_based_on_someone_current_assets_and_other_indicators_outputs_actions_could_take_to_invest() # THIS IS ONLY FOR PERSONAL USE
        self.create_map_of_all_alternative_physical_locations_and_alternative_websites_categorize_websites_compare_alternatives()
        self.look_at_all_alternative_investment_for_certain_action_and_effects_using_map()
        self.build_crypto_exchange_app() # cross site tracking for psp check legality of this\
        concepts_to_integrate_into_finance_model="""
        # follow the mit lectures to build this program
        https://www.youtube.com/watch?v=HdHlfiOAJyE
        https://finotor.com/10-most-important-finance-equations/
        #income statement
        Framework finanical analysis:
        Assets: cash,captial,intangibles = some value
        Liaiblities: equity debt= some value
        corproate financial decisions
        cash raised from ivnestors, cash invested in real assets(tangible and intangible)
        cash generated by operations
        cash reinvested
        cash returned to investors
        management
        risk management
        objective create and maxmize shareholder value
        financing 
        factors that make finance challenging
        use historical data
        time
        #how to model temporal differences
        risk
        #how to model unknowns
        Income statmeent 
        sources of funds = uses of funds     
        six principles of finance
        no such thing as free lunch
        other htings equal indivsuals prefer more money to less, money now vs later
        prefer to avoid risk
        self interestyed
        financil markets equalize supply and demand
        financiaql markets are highly adaptive and competwetive
        risksharing and friciotns are cental to innovation
        measuring risk
        how are financial assets valued
        how should finacnial assets be valued
        how do markets determine assets value
        how dwell do financial markets work
        how much should i save/spend
        what should i buy/sell
        how should i finance the transaction
        balance sheet and income 
        ensure democracy
        reputation
        asset is simply a sequence of current and future cash flows
        knwoledge, reputation, goodwill all considered assets
        hard part is figuring out what thos ecash flows are
        supply demand dictate difference betewen 1 dollar to day and 1 dollar later, exhcnage rate show this
        fact that us goverment stands behind pieces of papers that explains why stockmarket goes up because market environment has been stablaized
        things that are negative present value you sell them
        A negative net present value (NPV) means that a project or investment is unprofitable and should not be pursued. This is because the costs of the project exceed the cash flows it generates
        time value of money
        Cost and benefits associated with each decision
Risk:Reward
Books on risk
use this for legal risk with more factyors like time involved
An investor can calculate a risk-reward ratio by dividing the amount they could profit, or the reward, by the amount they stand to lose, or the risk. Cost and benefits
Formula is factors that would benefit you: Factors that would not benefit you
Formula: Divide the potential loss by the potential gain
Example: If an investor buys a stock for $100 and plans to sell it for $200, the risk/reward ratio is 1:1
        """
        # use th3e internet in order to pull this one off and find best things to invest in
        #quantitative investment management company      
        # extra functions
        self.build_search_find_all_free_and_useful_sas_and_projects_to_add_to_psp()
        # add these to this pipeline visiting thw site and filling in and using it
        # or on click add these to the click option of the problem solving program
        self.build_self_repairing_pyautogui_program_so_when_gets_stuck_tries_to_repair()
        self.build_model_to_perform_all_tasks_on_website()# so can access any website forms or services or login assuming its legal
        self.use_models_to_genrate_quesitons_and_all_objects_in_problem_so_efects_and_problems_themselves() # self build problem sovling program
        self.categorized_websites_then_perform_paritcluar_operations_on_them()
        # as long as its legal only take things you can but i think ideas can be taken just fixed form that you cant under copy right
        self.build_program_to_find_all_best_ideas_from_people_and_things_to_incorproate_into_program()
        self.build_program_to_incorporate_ideas_into_program()
        self.build_auto_stealing_idea_program_from_all_things_like_geist_website_or_other_company_websites_or_products_convert_idea_into_text_then_incorproate_into_psp()
        self.copy_everything_successful_people_have_done_steal_all_ideas_incoprorate_them_into_this_more_is_key()
        self.start_insurance_company()
        self.input_information_create_thought_create_action()
        self.deicison_making_understander()# essentially markeitng
        # what input inofrmation produces certain thoughts which produce certain acitons by people
        # only do this if its legal get people to do what you want what goes into a deicsion, what to say or do to get people to make a deicsion you want like deciding to give you money# generate actions that let you do this
        self.law_checker_to_make_sure_action_is_legal()
        self.start_insurance_company()
        self.start_a_sub_stack_website()
        self.build_auto_repairing_pyautogui_program()
        self.figure_out_what_is_going_into_someone_decisions()
        self.open_bank()
        self.build_
        
        self.pyautogui_duckduck_go_ai_search()
        self.create_gen_ai_model_to_do_science_in_fields()
        self.build_automatic_idea_finder_program()
        self.auto_create_all_elements_of_problem_solving_program_self_improving()
        self.look_up_strats_in_risk_like_divide_and_conquer_and_historical_strats_to_win()
        self.autoamte_finding_tools_like_access_information_request_by_searching_websites_and_incorporate_in_psp()
        self.use_mit_course_materials_to_build_expert_models_related_to_the_couse_subject_area_that_perform_special_expert_actions_like_invest_or_build_robotics_system_taught_in_the_course()
        law_checker_build_guide=""" 
# build this so you can automate this process in the future in tfhe problem solving program
Action 1: find all applicable laws and reuglation and make a long list#scrape this
Action 2: figure out which laws in this law list apply to a given action
Action 3: figure out whether you would contravene or not contravene any of these laws through the action(effects) always try to maximize effects
Action 4: suggest all alternative actions if this action would contravene a law, and do not take illegal action

        """
        self.build_law_compiler_model()
        self.display_appicable_laws_might_contravene_or_should_be_aware_of_by_action_for_different_strats()
        self.risk_calculation()
        self.find_all_possible_data_could_train_dif_modles_with() # in public domain
        
        
        
        
        
        
        
        
        
        
      
        
      
        
        # how to best use your money
        # rate of return on investment but risk is lower
        # some factors in detemrining bes tway to use the money
        # for solving this problem 
        #have a genral best investment mewtric 
        # and have a 
        
        
        
        
        # when you steal everything and dont learn how to do things you will lose
        # program to generate business ideas
       
        
        # figure out which stuff is worth building a buisness around
        #or if im better off putting my money 
        # look at finished products and copy these reverse engineer them
        # then use them to make investment decision
        # so a list of best stocks and anticpated returns on investment
        # and same for startign a busines
        # either invest in stock
        # or build the business yourself using prospoectus
        # setting up supply chain and building all the tech\
        # make decision based on metrcis
        # look at return on investmentr
        
        
        
        
        
        
        # train gen ai model for building stuff
        # scrape all data from 
        #https://grabcad.com/library?page=11&time=all_time&sort=popular&categories=aerospace
        # use psp environment to generate context on each model
        # output design for product
        # use data frem the web
        # patents
        # cad designs
        # anything we can think of
        # use this to design co2 cpature program
        # want to link text to 3d model generated?
        # how would we do this and why has it not been done
        # coding program to code a solution
        # stracking neural network
        # covluntal neural networks
        #make list of all different things you could build
        # make pipeline choose one
        # and generate design of that one within some range
        # maybe categorize and take ideas idk
        #how do we build something
        # train on expired google patents
        # train on 3d modeling data
        # figure out all finished products and thingd engineers produce 
        # and use like methods and tests, ask dad and other procedures
        # so patents and cad
        # and build model to generate this for any given problem
        # then set up supply chain for this to build it as cheaply as possible
        
        # so input is strategy text output is a patent, and 3d model to model and solve the problem
        # and design supply chain to manufaure the good
        # andf the manufaturing equipment you would need
        # and how tyou would market it
        # basically everything you would need to build and then sell the product
        # all in one button click
        
        ### AUTOMATICALLY START WHOLE BUSINESS
        # all steps to design build and mass produce a product
        # model to produce patents, supply chain to produce device, 3d model of object
        # and have ready to go marketing , and other stuff to start the business
        # only thing to doing is protoybe with 3d printer and robotics arms, assembly included
        # build software ofr this
        # robotic arms build and 3d print stuff to do the prototpying automcially 
        
        
        #self.build_search_for_engineering_pipeline()

        
        
        #
        #self.automatically_contact_investors()

       
        
        
        # build sateltites, build co2 capture
        # get goverment funding using proven track record

        # use llama 3.1 to train this model
        #or gen ai model of similar size
        
        # investment problem solving pipeline
        
        
        
        # make long list of all possible things you coud invest in
        #then build program to measure effects of investing in those things
        # effects in terms of different indicators
        # then depedning on what you have will input how you should invest it
        # liek stock business
        # consider return on investment
        # investment in temrs of time and money
        # build investment program
        
        
        # supply chain program
        
        
        
        

        # worry about these another day
        # engineering program use coding program to build
        #bbuild special gen ai models for this
        # generate every task that a engineer does like shcemiatics patents etc
        
        
        
        # investment program use coding program to build
        
        # build algorhim for this   
        self.build_law_project()# use fia nn
        self.build_law_sensor_and_action_program_so_have_sensors_on_laws_triggered_when_take_actions()
        
        
        
        
        import sys
        import re
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\business_process_management_functions')
        from business_process_management_functions80 import business_process_management_functions
        business0=business_process_management_functions()
        from business_process_management_functions80 import business_process_management_functions_child
        business1=business_process_management_functions_child()
        from business_process_management_functions80 import business_process_management_functions_gchild
        business2=business_process_management_functions_gchild()
        from business_process_management_functions80 import business_process_management_functions_g2child
        business3=business_process_management_functions_g2child()
        
        #search_dictionary_term=re.search(r"(.*);",modified_text).group(1)
        #use a seperate compuer for each
        # build coding prbolem tree first
        # then run through mdoels
        # do all this with llamma for now
        # keep it simple get it done by tonight
        # setup quick website
        # add an api to it for the model
        # make the model accessible
        #
        
        # ask certian questions and send the data back
        #tcp ip ,allows internet to function way it does

 
        # CODING PROGRAM
        # this deal with pyautogui
        print('THIS IS THE CODING PROGRAM environment')
        business2.chatgpt_gen_pyautogui_program_generate_environment(modified_text)
        business2.llamma_gen_pyautogui_program_generate_environment(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_generate_environment(modified_text)
        
        # consider alternatives  and code them
        print('THIS IS THE CODING PROGRAM strats')
        business2.chatgpt_gen_pyautogui_program_generate_strats(modified_text)
        business2.llamma_gen_pyautogui_program_generate_strats(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_generate_strats(modified_text)
        
        print('THIS IS to actually code the whole problem tree')
        # then code each function in the coding problem tree and alternative approaches
        business2.chatgpt_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.llamma_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        # use specific prompts for these
        
        #repeat by breaking the problem down into strat steps and then code those as well in higher order classes
        # do the whole coding tree here breaking down the task
        
        
        
        
        
        
        
        
        
        
        
        self.llamma_to_generate_environment()
        self.update_and_show_coding_program(modified_text)
        self.query_llm_from_lm_studio(modified_text)
        self.web_searches(modified_text)# check against github
        
        self.create_problem_glossary()
        self.open_problem_glossary()
        self.build_enigneering_project() # then build engineering desing on each query
        self.build_search_for_engineering_pipeline()
        self.build_investmnet_project()
        self.build_supply_chains()      
        self.build_pizza_maker()
        self.build_as_many_useful_physical_thingas_possilbe()# patent them help people 
        # build the ecommcerce site
        self.build_law_project()
       
    
    
        
        
 
         
class quadrants_of_program(buttons_per_quadrant):
    def __init__(self):
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.background_label_color='grey'
        self.problem_recorded=None
    
    def side_lists(self, title_of_text,label_list,frame_name,i,j, galaxies_table= False ):
        """display a list of exisitng galaxies from database, this is the one on the sides of the screen """
        frame_name.grid(row=i, column=j, padx=0, pady=0)
        frame_name.configure(bg='white')
         ### will need to see if this breaks other stuff
        
        #list_box_name_dic={self.listbox1:"Current Connected Objects",self.listbox2:"Current Connected Objects",self.listbox3:"Current Connected Objects",self.listbox4:"Current Connected Objects",self.listbox5:"Current Connected Objects",self.listbox6:"Current Connected Objects"}
        # redo side list just give each a name like listbox1 listbox2 listbox3 etc
        self.current_listbox=""
        label = tk.Label(master=frame_name,text=title_of_text, fg="black", bg=self.background_label_color)
        label.grid(row=0, columnspan=3)
        label.config(font=('Times New Roman',10),bg='white')
        if title_of_text == "Current Connected Objects":
            self.listbox1 = tk.Listbox(frame_name,width=60) 
            self.listbox1.grid(row=1,column=0, columnspan=3)
            self.listbox1.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
            self.listbox1.bind("2",self.record_question_or_tool_used)
            self.listbox1.bind('3',self.transport_object_from_object_window)
            self.listbox1.bind("4",self.switch_to_previous_galaxy)
            self.listbox1.bind("9",self.delete_from_listbox)
            

            
            self.current_listbox=self.listbox1
            for i2, idea in enumerate(label_list):
                ideaa=idea
                self.listbox1.insert(tk.END, f"{i2}:{ideaa}")
            entry=tk.Entry(master=frame_name)
            entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
            button_list=[decrease,increase,decrease]
            text_list=["Open Code Base","3:Strategy-Design"]
            for ii, button_type,textt in zip(range(2),button_list,text_list):
                update_galaxies = customtkinter.CTkButton(master=frame_name, text=textt)
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                if textt=="Open Code Base":
                    update_galaxies.bind("<Button-1>", self.open_coding_base)
                if textt=="3:Strategy-Design":
                    update_galaxies.bind("<Button-1>",self.change_to_strategy_window )
                    #create this
                
            return 'hi'

            
        if title_of_text == "Possible Objects":
            self.listbox2 = tk.Listbox(frame_name,width=60) 
            self.listbox2.grid(row=1,column=0, columnspan=3)

            self.listbox2.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
            self.listbox2.bind("2",self.record_question_or_tool_used)
            self.listbox2.bind('3',self.transport_object_from_object_window)
            self.listbox2.bind("4",self.add_previous_galaxies_to_problem)
            self.current_listbox=self.listbox2
            for i2, idea in enumerate(label_list): 
                 ideaa=idea
                 self.current_listbox.insert(tk.END, f"{i2}:{ideaa}")
            entry=tk.Entry(master=frame_name)
            entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
            button_list=[decrease,increase,decrease]
            text_list=["update","Form-Conn"]
            for ii, button_type,textt in zip(range(2),button_list,text_list):
                update_galaxies = customtkinter.CTkButton(master=frame_name, text=textt)
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                if textt=="Access-Strategy":
                    update_galaxies.bind("<Button-1>", self.change_to_strategy_window)
                    continue
                update_galaxies.bind("<Button-1>", self.handle_click)
            return "hi"

            
        if title_of_text == "Questions":
             self.listbox3 = tk.Listbox(frame_name,width=60) 
             self.listbox3.grid(row=1,column=0, columnspan=3)

             self.listbox3.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
             self.listbox3.bind("2",self.record_question_or_tool_used)
             self.listbox3.bind('3',self.transport_object_from_object_window)
             self.current_listbox=self.listbox3
             entry=tk.Entry(master=frame_name)
             entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
             

             
        if title_of_text == "Tools":
             self.listbox4 = tk.Listbox(frame_name,width=60)
             self.listbox4.grid(row=1,column=0, columnspan=3)

             self.listbox4.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
             self.listbox4.bind("2",self.record_question_or_tool_used)
             self.listbox4.bind('3',self.transport_object_from_object_window)
             self.current_listbox=self.listbox4
             entry=tk.Entry(master=frame_name)
             entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
             
             
             
        if title_of_text == "Web-Results":
             self.listbox5 = tk.Listbox(frame_name,width=60) 
             self.listbox5.grid(row=1,column=0, columnspan=3)
             self.listbox5.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
             self.listbox5.bind("2",self.record_question_or_tool_used)
             self.listbox5.bind('3',self.transport_object_from_object_window)
             self.current_listbox=self.listbox5
             self.entry_2=tk.Entry(master=frame_name)
             self.entry_2.grid(row=2, column=0,columnspan=3, sticky="nsew")
             self.entry_2.bind('<Return>', self.web_results_list_search)
             if self.problem_recorded:
                 self.cur.execute(f"""SELECT actions FROM auto_strategy_table WHERE problem_being_solved = "{self.recorded_problem}" ;""")
                 self.listbox5.delete(0, tk.END)
                 strategy_list= self.cur.fetchall()
                 for i2, strategy in enumerate(strategy_list): 
                      strategy=strategy[2:-2]
                      self.listbox5.insert(tk.END, f"{strategy}")
             

             
        for i2, idea in enumerate(label_list): 
             ideaa=idea[2:-2]
             self.current_listbox.insert(tk.END, f"{i2}:{ideaa}")
             
             
        


        button_list=[decrease,increase,decrease]
        text_list=["1:Update-text","record screen"]
        for ii, button_type,textt in zip(range(2),button_list,text_list):
            
            if title_of_text == "Web-Results" and ii==0:
                update_galaxies = customtkinter.CTkButton(master=frame_name, text="Web Search")
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                update_galaxies.bind("<Button-1>", self.upload_to_web_search_result_for_problem)
                continue
            
            
            update_galaxies = customtkinter.CTkButton(master=frame_name, text=textt)
            update_galaxies.grid(row=3, column=ii, sticky="nsew")
            update_galaxies.bind("<Button-1>", self.handle_click)
            
    def generate_side_lists_method_design(self, frame_name,category,title_of_text="", button_color="orange", conn=False,sub_method=False):
            # import from problem table
            # get sub_method data into correct format
        if sub_method==True:
            
            label_list=self.import_tools_problems_or_existing_ideas(category,sub_methods_table=True)

        if sub_method==False:
            label_list=self.import_tools_problems_or_existing_ideas(category)


        label = tk.Label(master=frame_name,text=title_of_text, fg="black", bg=self.background_label_color)
        label.grid(row=0, columnspan=3)
        label.config(font=('Times New Roman',10),bg='white')
        # need to bind all the buttons correctly
        #how do i do this
        # need to divide up windows maybe
        # if conn vs if method design
        # if method
        
        if conn==True:
            # do this for listbox 1 current connected objects
            if self.problem_recorded:
                self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{self.problem_recorded}' ;""")
                self.listbox1.delete(0, tk.END)
                object_qual_list= self.cur.fetchall()
                for i2, object_qual in enumerate(object_qual_list): 
                    objectt=object_qual[0]
                    qualtity_list=object_qual[1]
                    final_str=f"{objectt} ; {qualtity_list}"
                    self.listbox1.insert(tk.END, f"{final_str}")
                    
            if title_of_text == "Possible Objects" or title_of_text == "Current Method Steps" :
                self.listbox2 = tk.Listbox(frame_name,width=60) 
                self.listbox2.grid(row=1,column=0, columnspan=3)

                self.listbox2.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                self.listbox2.bind("2",self.record_question_or_tool_used)
                self.listbox2.bind('3',self.transport_object_from_object_window)
                self.current_listbox=self.listbox2
                entry=tk.Entry(master=frame_name)
                entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
     
            if title_of_text == "Questions":
                 self.listbox3 = tk.Listbox(frame_name,width=60) 
                 self.listbox3.grid(row=1,column=0, columnspan=3)

                 self.listbox3.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox3.bind("2",self.record_question_or_tool_used)
                 self.listbox3.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox3
                 entry=tk.Entry(master=frame_name)
                 entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
                 
            if title_of_text == "4 Problem Change Sub-Methods":
                
                self.listboxsub_method = tk.Listbox(frame_name,width=60) 
                self.listboxsub_method.grid(row=1,column=0, columnspan=3)
                self.listboxsub_method.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                self.listboxsub_method.bind("2",self.record_question_or_tool_idea_used_for_method)
                self.listboxsub_method.bind('3',self.transport_to_method_window)
                self.listboxsub_method.bind('4',self.change_selected_problem)
                self.cur.execute(f"""SELECT problem_question_or_task FROM auto_problem_table ;""")
                problem_entries= self.cur.fetchall()
                used_problem_list=[]
                for problemmm in problem_entries:
                    problemmm=problemmm[0]
                    if problemmm in used_problem_list:
                        continue
                    else:
                        self.listboxsub_method.insert(tk.END, str(problemmm)) 
                    used_problem_list.append(problemmm)

                

                self.current_listbox=self.listboxsub_method
                self.entry_1=tk.Entry(master=frame_name)
                self.entry_1.grid(row=2, column=0,columnspan=3, sticky="nsew")
                self.entry_1.bind('<Return>', self.method_box_list_search)

                

                 
            if title_of_text == "Tools":
                 self.listbox4 = tk.Listbox(frame_name,width=60)
                 self.listbox4.grid(row=1,column=0, columnspan=3)

                 self.listbox4.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox4.bind("2",self.record_question_or_tool_used)
                 self.listbox4.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox4
                 entry=tk.Entry(master=frame_name)
                 entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 

                 
            if title_of_text == "Objectives":
                 self.listbox5 = tk.Listbox(frame_name,width=60) 
                 self.listbox5.grid(row=1,column=0, columnspan=3)
                 self.listbox5.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox5.bind("2",self.record_objective_used_for_method)
                 self.listbox5.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox5
                 entry=tk.Entry(master=frame_name)
                 entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
                 
            if title_of_text == "Web-Results":
                 self.listbox5 = tk.Listbox(frame_name,width=60) 
                 self.listbox5.grid(row=1,column=0, columnspan=3)
                 self.listbox5.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox5.bind("2",self.record_question_or_tool_idea_used_for_method)
                 self.listbox5.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox5
                 self.entry_2=tk.Entry(master=frame_name)
                 self.entry_2.grid(row=2, column=0,columnspan=3, sticky="nsew")
                 self.entry_2.bind('<Return>', self.web_results_list_search)
                 if self.problem_recorded:
                     self.cur.execute(f"""SELECT actions FROM auto_strategy_table WHERE problem_being_solved = '{self.problem_recorded}' ;""")
                     self.listbox5.delete(0, tk.END)
                     strategy_list= self.cur.fetchall()
                     for i2, strategy in enumerate(strategy_list): 
                         strategy=strategy[0]
                         strategy=strategy[2:-2]
                         strategy=strategy.split(",")
                         if strategy[0]!="":# will need to clean this up
                             self.listbox5.insert(tk.END, f"{strategy}")
                             
                         
                     
                     

            
        if conn ==False:
            # listbox 1 stuff
            if self.problem_recorded:
                self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{self.problem_recorded}' ;""")
                self.listbox1.delete(0, tk.END)
                object_qual_list= self.cur.fetchall()
                for i2, object_qual in enumerate(object_qual_list): 
                    objectt=object_qual[0]
                    qualtity_list=object_qual[1]
                    final_str=f"{objectt} ; {qualtity_list[2:-2]}"
                    self.listbox1.insert(tk.END, f"{final_str}")
                    
            if title_of_text == "Possible Objects" or title_of_text == "Current Method Steps" or title_of_text ==  "Actions":
                self.listbox2 = tk.Listbox(frame_name,width=60) 
                self.listbox2.grid(row=1,column=0, columnspan=3)

                self.listbox2.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                self.listbox2.bind("2",self.record_idea_used_for_method)
                self.listbox2.bind('3',self.transport_object_from_object_window)
                self.current_listbox=self.listbox2
                entry=tk.Entry(master=frame_name)
                entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
                
                
     
        
            if title_of_text == "Questions":
                 self.listbox3 = tk.Listbox(frame_name,width=60) 
                 self.listbox3.grid(row=1,column=0, columnspan=3)

                 self.listbox3.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox3.bind("2",self.record_question_or_tool_idea_used_for_method)
                 self.listbox3.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox3
                 entry=tk.Entry(master=frame_name)
                 entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
                 
            if title_of_text == "4 Problem Change Sub-Methods":
                
                self.listboxsub_method = tk.Listbox(frame_name,width=60) 
                self.listboxsub_method.grid(row=1,column=0, columnspan=3)
                self.listboxsub_method.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                self.listboxsub_method.bind("2",self.record_question_or_tool_idea_used_for_method)
                self.listboxsub_method.bind('3',self.transport_to_method_window)
                self.listboxsub_method.bind('4',self.change_selected_problem)
                self.entry_1=tk.Entry(master=frame_name)
                self.entry_1.grid(row=2, column=0,columnspan=3, sticky="nsew")
                self.entry_1.bind('<Return>', self.method_box_list_search)

                

                self.current_listbox=self.listboxsub_method
            if title_of_text == "Tools":
                 self.listbox4 = tk.Listbox(frame_name,width=60)
                 self.listbox4.grid(row=1,column=0, columnspan=3)
                 self.listbox4.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox4.bind("2",self.record_question_or_tool_idea_used_for_method)
                 self.listbox4.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox4
                 entry=tk.Entry(master=frame_name)
                 entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 

                 
            if title_of_text == "Objectives" or title_of_text ==  "Effects":
                 self.listbox5 = tk.Listbox(frame_name,width=60) 
                 self.listbox5.grid(row=1,column=0, columnspan=3)
                 self.listbox5.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox5.bind("2",self.record_objective_used_for_method)
                 self.listbox5.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox5
                 entry=tk.Entry(master=frame_name)
                 entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
                 if self.problem_recorded:
                     self.cur.execute(f"""SELECT actions FROM auto_strategy_table WHERE problem_being_solved = '{self.problem_recorded}' ;""")
                     self.listbox5.delete(0, tk.END)
                     strategy_list= self.cur.fetchall()
                     for i2, strategy in enumerate(strategy_list): 
                         strategy=strategy[0]
                         strategy=strategy[2:-2]
                         strategy=strategy.split(",")
                         if strategy[0]!="":# will need to clean this up
                             self.listbox5.insert(tk.END, f"{strategy}")
                 
            if title_of_text == "Web-Results":
                 self.listbox5 = tk.Listbox(frame_name,width=60) 
                 self.listbox5.grid(row=1,column=0, columnspan=3)
                 self.listbox5.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
                 self.listbox5.bind("2",self.record_question_or_tool_idea_used_for_method)
                 self.listbox5.bind('3',self.transport_object_from_object_window)
                 self.current_listbox=self.listbox5
                 self.entry_2=tk.Entry(master=frame_name)
                 self.entry_2.grid(row=2, column=0,columnspan=3, sticky="nsew")
                 self.entry_2.bind('<Return>', self.web_results_list_search)
                 

                 
            
 
             
        for i2, idea in enumerate(label_list): 
             ideaa=idea[2:-2]
             self.current_listbox.insert(tk.END, f"{i2}:{ideaa}")
             

        
        button_list=[decrease,increase,decrease]
        text_list=["1:Update-text","Form-Conn"]
        for ii, button_type,textt in zip(range(4),button_list,text_list):
            if title_of_text == "4 Problem Change Sub-Methods" and ii==0:
                update_galaxies = customtkinter.CTkButton(master=frame_name, text="ideas",fg_color=button_color,text_color='white')
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                update_galaxies.bind("<Button-1>", self.upload_ideas)
                continue
            if title_of_text == "4 Problem Change Sub-Methods" and ii==1:
                update_galaxies = customtkinter.CTkButton(master=frame_name, text="Access Methods",fg_color=button_color,text_color='white')
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                update_galaxies.bind("<Button-1>", self.use_methods)
                continue
            if title_of_text == "Web-Results" and ii==0:
                update_galaxies = customtkinter.CTkButton(master=frame_name, text="Web Search",fg_color=button_color,text_color='white')
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                update_galaxies.bind("<Button-1>", self.upload_to_web_search_result_for_problem)
                continue
            if title_of_text == "Questions" and ii==0:
                update_galaxies = customtkinter.CTkButton(master=frame_name, text="Reuse Methods",fg_color=button_color,text_color='white')
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                update_galaxies.bind("<Button-1>", self.revert_back_to_show_previous_methods_to_reuse_to_add_to_method)
                continue
            
                
                

            update_galaxies = customtkinter.CTkButton(master=frame_name, text=textt,fg_color=button_color,text_color='white')
            update_galaxies.grid(row=3, column=ii, sticky="nsew")
            update_galaxies.bind("<Button-1>", self.handle_click) 
            
    def main_problem_window(self,i,j):
        """ """
        self.frame8.grid(row=i, column=j)#padx=5, pady=5
        self.frame8.config(bg="white")
        button_list=[decrease,increase,decrease,decrease,decrease,decrease,decrease]
        text_list=["1:Conns-Design","2:Steps-Design","List-Past-Problems","List-Problems","Record_Problem"]
        #"Web-Grab" # add this to web box instead
        for ii, button_type,textt in zip(range(7),button_list,text_list):
            button = customtkinter.CTkButton(master= self.frame8, text=textt,fg_color="green")
            #command=self.highlight_text,
            button.grid(row=0,column=ii , sticky="nsew")
            #button.config(font=('Times New Roman',10),bg='green')
            if textt=="1:Conns-Design":
                button.bind("<Button-1>",self.change_back_to_conn_window)
            if textt=="List-Past-Problems":
                button.bind("<Button-1>",self.list_past_problems)
            if textt=="List-Problems":
                button.bind("<Button-1>",self.list_possble_problems)
            if textt=="Record_Problem":
                button.bind("<Button-1>",self.record_problem_and_create_problem_dictionary)#record_problem_and_create_problem_dictionary
            if textt=="2:Steps-Design":
                button.bind("<Button-1>",self.switch_to_method_window)
        self.text_box = tk.Text(master=self.frame8)#width=100
        self.text_box.grid(row=1,columnspan = 9)  #columnspan = 9
        self.text_box.bind(';',self.import_problem)
        self.text_box.bind('-',self.upload_past_problem_to_keep_expanding_network)
        #self.text_box.bind('2',self.text_box.tag_add( background= "black", foreground= "white") )
    def qualitites_boxes(self, text_box_1_title,text_box_2_title,i,j,level=0):
        if level==0:
            self.frame6.grid(row=i, column=j, padx=5, pady=5)
            self.frame6.config(bg='white')
            self.label1 = tk.Label(master=self.frame6,text=text_box_1_title,fg="black",bg=self.background_label_color)
            self.label1.grid(row=0,column=0)
            self.label1.config(font=('Times New Roman',10),bg='white')
            self.label2 = tk.Label(master=self.frame6,text=text_box_2_title,fg="black",bg=self.background_label_color)
            self.label2.grid(row=0,column=1)
            self.label2.config(font=('Times New Roman',10),bg='white')
            self.text_box0 = tk.Text(self.frame6,width=50)
            self.text_box0.grid(row=1,column=0)
            self.text_box0.bind("`",self.starcraft_hotkey_conn_textbox)
            #self.text_box0.bind("-",self.export_object_to_new_table)   
            self.text_box0.bind("-",self.add_qualitites_expand_current_qualtity_or_problem_dictionary)
            self.text_box0.bind("\'",self.pre_create_galaxies)
            self.text_box0.bind(".",self.access_old_object_to_add_further_qualtites)
            
            self.text_box01 = tk.Text(self.frame6,width=50)
            self.text_box01.grid(row=1,column=1)  
            self.text_box01.bind("-",self.add_strategy)### this is what we will modify
            self.text_box01.bind("=",self.display_problem_tree_in_method_window)### this is what we will modify
            self.text_box01.bind("`",self.code_whole_problem_tree_using_coding_program_create_new_project)

            

        else:
            self.frame.grid(row=i, column=j, padx=5, pady=5)
            self.frame.config(bg='white')
            self.label3 = tk.Label(master=self.frame,text=text_box_1_title,fg="black",bg=self.background_label_color)
            self.label3.grid(row=0,column=0)
            self.label3.config(font=('Times New Roman',10),bg='white')
            self.label4 = tk.Label(master=self.frame,text=text_box_2_title,fg="black",bg=self.background_label_color)
            self.label4.grid(row=0,column=1)
            self.label4.config(font=('Times New Roman',10),bg='white')
            self.text_box1 = tk.Text(self.frame,width=50)
            self.text_box1.grid(row=1,column=0)
            self.text_box1.bind("-",self.add_step_or_modify)
            self.text_box1.bind("`",self.starcraft_hotkey_method_textbox)
            #self.text_box1.bind('-',self.export_idea_to_new_table)
            self.text_box2 = tk.Text(self.frame,width=50)
            self.text_box2.grid(row=1,column=1)
            self.text_box2.bind('-',self.export_idea_to_new_table)

            

        #btn_increase = tk.Button(master=frame, text="+", command=increase)

        #btn_increase.grid(row=1, column=2, sticky="nsew")

    def sub_method_box_1(self,frame,i,j): 
        """ will outline sub-method of questioning to perform, this is the one on the middle right of the screen"""
        frame.grid(row=i, column=j, padx=5, pady=5)
        frame.config(bg='white')

        label1 = tk.Label(master=frame,text="4 Problem Change Sub-Methods",fg="black",bg="white")
        label1.grid(row=0,columnspan=2)
        label1.config(font=('Times New Roman',10))

        #frame.grid(row=i, column=j, padx=5, pady=5)
        self.entry_1=tk.Entry(master=frame)
        self.entry_1.grid(row=1,columnspan=2, sticky="nsew") 
        #column=0,columnspan=3
        self.entry_1.bind('<Return>', self.method_box_list_search)

        
        button_list=[decrease,increase,decrease,decrease]
        text_list=["conn","update"]
        # add this to textlist if we want more buttons import",
        

        self.listboxsub_method = tk.Listbox(frame,width=60,background='white',height=10) 
        self.listboxsub_method.grid(row=2,columnspan=2)#column=0, columnspan=4
        self.listboxsub_method.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
        self.listboxsub_method.bind('4',self.change_selected_problem)

        #self.listboxsub_method.bind('4',self.show_steps_in_sub_method)


        #label_listt=self.import_tools_problems_or_existing_ideas(8)
        #upload problems here instead
        self.cur.execute(f"""SELECT problem_question_or_task FROM auto_problem_table ;""")
        problem_entries= self.cur.fetchall()
        used_problem_list=[]
        for problemmm in problem_entries:
            problemmm=problemmm[0]
            if problemmm in used_problem_list:
                continue
            else:
                self.listboxsub_method.insert(tk.END, str(problemmm)) 
            used_problem_list.append(problemmm)


            
        text_list=["1:Ideas","2:Access Methods"]
        for ii, textt in zip(range(2),text_list):
            update_galaxies = customtkinter.CTkButton(master=frame, text=textt,fg_color="#1d8acf",text_color='white')
            update_galaxies.grid(row=3, column=ii, sticky="nsew")
            if ii==0:
                update_galaxies.bind("<Button-1>", self.upload_ideas)
                continue
            if ii==1:
                update_galaxies.bind("<Button-1>", self.use_methods)

                

            #update_galaxies.bind("<Button-1>", self.handle_click) 
            
class quadrants_method_window(buttons_per_quadrant):   
        def __init__(self):
            import psycopg2
            self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
            self.cur = self.conn.cursor()
            self.background_label_color='grey'   
            
class methods_window_program(quadrants_of_program):
    def __init__(self):
        import psycopg2 
        self.init_problems_window()
        self.init_problems_frame()
        self.init_problems_list_box()
        self.init_problems_label()
        self.init_problems_search_bars()
        self.init_problems_button()
        self.bind_problems_functions_list_boxs()
        self.bind_problem_functions_buttons()
        self.bind_problems_functions_search_bars()
        methods_worked_on=self.upload_sql_method_data()
        self.process_method_data(methods_worked_on)
        self.upload_problem_data_to_listbox()
        
        strategy_worked_on=self.upload_sql_strategy_data()
        self.process_strategy_data_convert_to_problem_tree_data(strategy_worked_on)
        self.upload_problem_tree_data_to_listbox()
    def init_problems_window(self):
       """create main tkinyer window """
       self.window_methods = tk.Tk()
       self.window_methods.config(bg="white")
       self.window_methods.title('Problems Window')
       self.window_methods.state('zoomed')
       self.window_methods.columnconfigure(0, weight=1, minsize=75)
       self.window_methods.rowconfigure(0, weight=1, minsize=50) 
       self.screen_width= self.window_methods.winfo_screenwidth()
       self.screen_height = self.window_methods.winfo_screenheight()
       self.screen_width_characters=self.screen_width*0.125
       self.screen_height_characters=self.screen_height*0.125
       
      
       
       
       
    def init_problems_frame(self,bg_color="blue"):
        """ """
        self.main_frame1_methods = tk.Frame(master=self.window_methods, relief=tk.RAISED, borderwidth=1)
        self.main_frame1_methods.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame2_methods = tk.Frame(master=self.window_methods, relief=tk.RAISED, borderwidth=1)
        self.main_frame2_methods.grid(row=0,column=1)
        
        self.main_frame3_methods = tk.Frame(master=self.window_methods, relief=tk.RAISED, borderwidth=1)
        self.main_frame3_methods.grid(row=1,column=0)
        
        self.main_frame4_methods = tk.Frame(master=self.window_methods, relief=tk.RAISED, borderwidth=1)
        self.main_frame4_methods.grid(row=1,column=1)
        
        self.main_frame5_methods = tk.Frame(master=self.window_methods, relief=tk.RAISED, borderwidth=1)
        self.main_frame5_methods.grid(row=0,column=2)
        
        self.main_frame6_methods = tk.Frame(master=self.window_methods, relief=tk.RAISED, borderwidth=1)
        self.main_frame6_methods.grid(row=1,column=2)
        
        
    def generate_button_list_widget(self,text):
         """ generate button list widget"""
         self.scrollbar = tk.Scrollbar(self.window_methods,orient='vertical')
         self.scrollbar.grid()#row=1,column=0, columnspan=3 #column=5,row=0,rowspan=4
         self.scrollbar.config(command=self.yview)
         #return list_of_button_widgets
    def init_problems_list_box(self,font_size=10,font_type='Microsoft YaHei'):
       """ add listboxs to application"""
       font_type_and_size= (font_type,font_size)
       self.listbox_width=int(round(int(self.screen_width_characters)/3))
       self.listbox_height=int(round(self.screen_height_characters/6))
       self.listboxxy1_methods = tk.Listbox(self.main_frame1_methods,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy1_methods.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy1_methods.config(font=font_type_and_size)
       
       self.listboxxy2_methods = tk.Listbox(self.main_frame2_methods,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy2_methods.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy2_methods.config(font=font_type_and_size)
       
       self.listboxxy3_methods = tk.Listbox(self.main_frame3_methods,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy3_methods.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy3_methods.config(font=font_type_and_size)
       
       self.listboxxy4_methods = tk.Listbox(self.main_frame4_methods,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy4_methods.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy4_methods.config(font=font_type_and_size)
       
       self.listboxxy5_methods = tk.Listbox(self.main_frame5_methods,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy5_methods.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy5_methods.config(font=font_type_and_size)
       
       self.listboxxy6_methods = tk.Listbox(self.main_frame6_methods,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy6_methods.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy6_methods.config(font=font_type_and_size)
       
       
    def init_problems_label(self):
       """ add labels to application"""
       label = tk.Label(master= self.main_frame1_methods,text="Strategy-Problem MUST press 1 to create self.problem_recorded", fg="black", bg="blue")
       label.grid(row=0,column=0)
       label.config(font=('Times New Roman',10),bg='white')
       
       label = tk.Label(master= self.main_frame2_methods,text="Actions-List", fg="black", bg="blue")
       label.grid(row=0,column=0)
       label.config(font=('Times New Roman',10),bg='white')
       
       label = tk.Label(master= self.main_frame3_methods,text="Actions", fg="black", bg="blue")
       label.grid(row=0,column=0)
       label.config(font=('Times New Roman',10),bg='white')
       
       label = tk.Label(master= self.main_frame4_methods,text="Effects", fg="black", bg="blue")
       label.grid(row=0,column=0)
       label.config(font=('Times New Roman',10),bg='white')
       
       label = tk.Label(master= self.main_frame5_methods,text="Methods High Level", fg="black", bg="blue")
       label.grid(row=0,column=0)
       label.config(font=('Times New Roman',10),bg='white')
       
       label = tk.Label(master= self.main_frame6_methods,text="list of all possible life actions, dags sorted by objective choose objective", fg="black", bg="blue")
       label.grid(row=0,column=0)
       label.config(font=('Times New Roman',10),bg='white')
       
    def init_problems_search_bars(self):
         """add search bar to application """
         self.entry_1_methods=tk.Entry(self.main_frame1_methods)
         self.entry_1_methods.grid(row=2,columnspan=1, sticky="nsew") 
         # create a search bar
         
         self.entry_2_methods=tk.Entry(self.main_frame2_methods)
         self.entry_2_methods.grid(row=2,columnspan=1, sticky="nsew") 
         
         self.entry_3_methods=tk.Entry(self.main_frame3_methods)
         self.entry_3_methods.grid(row=2,columnspan=1, sticky="nsew") 
         
         self.entry_4_methods=tk.Entry(self.main_frame4_methods)
         self.entry_4_methods.grid(row=2,columnspan=1, sticky="nsew") 
         
         self.entry_5_methods=tk.Entry(self.main_frame5_methods)
         self.entry_5_methods.grid(row=2,columnspan=1, sticky="nsew") 
         
         self.entry_6_methods=tk.Entry(self.main_frame6_methods)
         self.entry_6_methods.grid(row=2,columnspan=1, sticky="nsew") 
   
    def init_problems_button(self):
       """add buttons to application """
       self.button_1_websites = customtkinter.CTkButton(master= self.main_frame1_methods, text="access_something",text_color='white')
       self.button_1_websites.grid(row=3, column=0, sticky="nsew")
       
       self.button_2_websites = customtkinter.CTkButton(master= self.main_frame2_methods, text="access_something",text_color='white')
       self.button_2_websites.grid(row=3, column=0, sticky="nsew")
       
       self.button_3_websites = customtkinter.CTkButton(master= self.main_frame3_methods, text="access_something",text_color='white')
       self.button_3_websites.grid(row=3, column=0, sticky="nsew")
       
       self.button_4_websites = customtkinter.CTkButton(master= self.main_frame4_methods, text="display Best Problem to solve Effects",text_color='white')
       self.button_4_websites.grid(row=3, column=0, sticky="nsew")
       
       self.button_5_websites = customtkinter.CTkButton(master= self.main_frame5_methods, text="choose objective function",text_color='white')
       self.button_5_websites.grid(row=3, column=0, sticky="nsew")
       
       self.button_6_websites = customtkinter.CTkButton(master= self.main_frame6_methods, text="choose objective function",text_color='white')
       self.button_6_websites.grid(row=3, column=0, sticky="nsew")


    def bind_problems_functions_list_boxs(self):
       """add buttons functions to listboxs """
       #self.listboxxy3.bind('1', self.view_glossary_websites)
       self.listboxxy1_methods.bind('1', self.display_strategies_of_selected_problem_strategy)
       self.listboxxy1_methods.bind('3', self.generate_and_open_blender_problem_web_and_tree)

       self.listboxxy2_methods.bind('1', self.display_individual_action_steps_for_specific_problem)
       self.listboxxy2_methods.bind('3', self.generate_blender_effect_problem_web_for_strat_and_problem_tree)



       self.listboxxy5_methods.bind('1', self.show_method_steps)
       
       #self.listboxxy2.bind('1', self.show_problemss)
       #self.listboxxy3.bind('1', self.show_problemss)
       # open up a window with values for database
       # expand on glossary defintions open new window
    def bind_problem_functions_buttons(self):
        """add button functions to buttons """
        #self.button_1.bind("<Button-1>", self.line_of_code_search_sort_and_upload)
        #self.button_2.bind("<Button-1>", self.glossary_search_sort_and_upload)
        #self.button_3.bind("<Button-1>", self.update_code_base)
    def bind_problems_functions_search_bars(self):
        """add button functions to search bars """
        self.entry_1_methods.bind('<Return>', self.search_sort_upload_methods)
        #self.entry_2.bind('1', self.show_problemss)
        
        
    def upload_sql_method_data(self):
        """ """
        import psycopg2
        main_method_window=quadrants_method_window()
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor() 
        self.cur.execute(f"""SELECT * FROM methods_table ;""")
        methods_worked_on= self.cur.fetchall()
        return methods_worked_on
    def process_method_data(self,methods_worked_on):
        """ """
        self.list_of_problems=[]
        method_list_str=""
        for problemm1 in methods_worked_on:
            problemmm=problemm1[1]
            if problemmm not in self.list_of_problems:
                method_list_str+= f"{problemmm}\n"  
                self.list_of_problems.append(problemmm)
        return self.list_of_problems 
    def upload_problem_data_to_listbox(self):
        """ """
        for problemmmm in self.list_of_problems:
            self.listboxxy5_methods.insert(tk.END, problemmmm) 
            
      
    def search_sort_upload_methods(self):
        """dont need the search function """
 
         
    ### problem tree functions and
    #buttons to work with data and strategies
    # and to display the strategies
    def upload_sql_strategy_data(self):
        """ """
        import psycopg2
        main_method_window=quadrants_method_window()
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor() 
        self.cur.execute(f"""SELECT problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions FROM strategy_table ;""")
        strategy_worked_on= self.cur.fetchall()
        return strategy_worked_on
    def process_strategy_data_convert_to_problem_tree_data(self,strategy_worked_on):
        """ this creates the problem tree dag structure {problem:[[actions]]"""
        import re
        self.life_problem_tree_dag={}
        #{problem:{strategy:[action_list],strategy:}action(another prooblem):{strategy:[action_list],strategy:}}
        method_list_str=""
        for strategy in strategy_worked_on:
            problem_being_solved=strategy[0]
            question_or_tool_for_strategy=strategy[1]
            problem_web_variables=strategy[2]
            effects=strategy[3]# 4 is time found not interested
            actions=strategy[5]
            actions=re.split(",",actions[1:-1])
            print(actions)
            if problem_being_solved in self.life_problem_tree_dag:
                self.life_problem_tree_dag[problem_being_solved].append(actions) 
            else:                # create new key
                self.life_problem_tree_dag[problem_being_solved]=[actions]       
        return self.life_problem_tree_dag 
    def upload_problem_tree_data_to_listbox(self):
        """ """
        print(self.life_problem_tree_dag )
        for problemmmm,strategies_list_list in self.life_problem_tree_dag.items() :
            self.listboxxy1_methods.insert(tk.END, problemmmm) 
            #for strategy in strategies_list_list:
            #    print(strategy)
            #    self.listboxxy1_methods.insert(tk.END, problemmmm) 

                #
                #self.listboxxy3_methods.insert(tk.END, problemmmm) 
    def upload_past_strategy_problem_to_keep_expanding_network(self,content):
        """ """
        import re
        self.method_list_dictionary={}
        self.strategy_list=[]
        self.recorded_question_or_tool_for_method_list=[]
        self.objective_list_for_method=[]
        self.ideas_list_for_method=[]        
        self.actions_for_method=[]
        self.strategy_or_method_label_for_methods=[]
        self.past_problemm=""
        self.problem_recorded=content# test
    
        self.upload_and_process_problem_table_data_for_specific_problem()
        #self.problem_recorded=problem_to_reupload_split[0]
        #print(self.problem_list_dictionary)
        #self.reupload_problem_to_view_in_listbox(self.problem_recorded)
        # need to sort out reupload if it seems important at one point
    def upload_blender_problem_tree_data_from_sql_method_window(self):
        """ """
        import re
        import copy
        import time
        self.temp_all_strategy_action_list_dictionary={}
        
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table ;""")
        all_strategy_table_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(all_strategy_table_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if problem_being_solved==self.problem_recorded:
                continue# this ensures that we accdinteally double up
            if action_list:
                action_list2=[]
                action_list=re.split(",",action_list[1:-1])
                for actionnnn in action_list:
                    actionnnn=actionnnn.strip()
                    action_list2.append(actionnnn) 
                action_list=action_list2
            if problem_being_solved not in self.temp_all_strategy_action_list_dictionary:
                self.temp_all_strategy_action_list_dictionary[problem_being_solved]=[] 
            self.temp_all_strategy_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available  
        #
        
        # repeat this process recursing each action
        # as deep as necessary until certain there are no other strategies witht hat aciton name
        # in the given tree
        print(self.temp_all_strategy_action_list_dictionary['?? how do i  create a expert problem environment? ###dJeOxUuRhSyStFuVfHjR'])
        print('HIIIII')
        self.problem_tree_problem_strat_list_action_list_dictionary={}
        time_qualitity_found =time.time()
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        specific_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(specific_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if action_list:
                action_list2=[]
                action_list=re.split(",",action_list[1:-1])
                for actionnnn in action_list:
                    actionnnn=actionnnn.strip()
                    action_list2.append(actionnnn) 
                action_list=action_list2
            if problem_being_solved not in self.problem_tree_problem_strat_list_action_list_dictionary:
                self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved]=[] 
            self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available 
            if action_list:
                action_list_list2=[]
                action_list_list2.append(action_list)
                while True: 
                    print(action_list_list2)
                    print('ACTION LIST_LIST')
                    if action_list_list2==[]:
                        break
                    action_list_list=action_list_list2
                    action_list_list2=[]
                    for action_listtt in action_list_list:
                        for actionnn in action_listtt:
                            print(actionnn)
                            if actionnn =='?? how do i  create a expert problem environment? ###dJeOxUuRhSyStFuVfHjR':
                                print('HOW TO CREATE FOUND')
                            #print('ACTION LIST')
                            #print(action_listtt)
                            #print('ACTION ')
                            # make it so that
                            # it adds to the intital strat line block as seperate tree

                            #print(actionnn)
                            if actionnn in self.temp_all_strategy_action_list_dictionary:# check if problem key for the action
                                if actionnn not in self.problem_tree_problem_strat_list_action_list_dictionary:
                                    self.problem_tree_problem_strat_list_action_list_dictionary[actionnn]=[] 
                                action_list2=self.temp_all_strategy_action_list_dictionary[actionnn]
                                if action_list2:
                                    for actionn_mini_list in action_list2:
                                        #print(actionn_mini_list)
                                        self.problem_tree_problem_strat_list_action_list_dictionary[actionnn].append(actionn_mini_list)# list of list of strats available 
                                        action_list_list2.append(actionn_mini_list)
                                
                            
        #[problem]=[strats[actions]]
        # first get all sub actions
        # then with this list check through other strategy
        # data and if they have sub trees add these in as
        # strats below these strats
        # find sub strategy trees
        # repeat this process as necessary
        # because could be multiple trees deep
        print(self.temp_all_strategy_action_list_dictionary)
        print(self.problem_tree_problem_strat_list_action_list_dictionary)
        return self.problem_tree_problem_strat_list_action_list_dictionary
        # broader principles guding action are in methods table
        #actual actiosn are in strategies table
        #self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM methods_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
        #methods_info= self.cur.fetchall()                                    
                                        
                                    
        
    def display_current_problem_info(self):
        """ """
        import re
        self.problem_info_qualitity_dictionary={}
        strategies_list_list=self.life_problem_tree_dag[self.problem_recorded]
        self.listboxxy2_methods.delete(0, tk.END)
        for strategy in strategies_list_list:
            self.listboxxy2_methods.insert(tk.END, str(strategy))
        # update listbox 3
        used_values=[]
        used_values_prob_name=[]
        # upload auto_problem_info to get effects finish this later
        self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
        problem_objects_and_qualtity_list= self.cur.fetchall()
        for i16,objecttt in enumerate(problem_objects_and_qualtity_list):
            specific_problem_or_object= objecttt[0]
            qualitity_list= objecttt[1]
            if qualitity_list:
                qualitity_list=re.split(",",qualitity_list[1:-1])
            if specific_problem_or_object not in self.problem_info_qualitity_dictionary:
                self.problem_info_qualitity_dictionary[specific_problem_or_object]=[]  
            for i10, qualityy2 in enumerate(qualitity_list):
                if qualityy2 in self.problem_info_qualitity_dictionary[specific_problem_or_object]:
                    continue
                else:
                    self.problem_info_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   




        problem_tree_problem_strat_list_action_list_dictionary=self.upload_blender_problem_tree_data_from_sql_method_window()
        # how to upload the values to the listbox
        #print(problem_tree_problem_strat_list_action_list_dictionary)
        #print('PROBLEM TREE DICX')
        #print(problem_tree_problem_strat_list_action_list_dictionary)
        for i3, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary.items()):
            
            if problem_name_key in used_values:
                continue
            self.listboxxy3_methods.insert(tk.END, str(f"PROBLEM: {problem_name_key}"))
            self.listboxxy4_methods.insert(tk.END, str(f""))

            used_values.append(problem_name_key)
            used_values_prob_name.append(problem_name_key)
            self.sub_value="_1"
            for i4, action_listt in enumerate(strategy_list):
                
                self.listboxxy3_methods.insert(tk.END, str(f"STRATEGY {i4}: {problem_name_key}"))
                self.listboxxy4_methods.insert(tk.END, str(f""))

                action_list_list2=[]
                action_list_list2.append([problem_name_key,action_listt])
                while True:
                    #print(action_list_list2)
                    if action_list_list2==[]:
                        break
                    action_list_list=action_list_list2
                    action_list_list2=[]
                    for action_listtt in action_list_list:
                        #self.listboxxy3_methods.insert(tk.END, str(f"{action_list_list}"))
                        prob_name=action_listtt[0]
                        action_listtt=action_listtt[1]
                        if prob_name not in used_values_prob_name:
                            self.listboxxy3_methods.insert(tk.END, str(f"PROBLEM{self.sub_value}: {prob_name}"))
                            self.listboxxy4_methods.insert(tk.END, str(f""))

                            used_values_prob_name.append(prob_name) 
                        #self.listboxxy3_methods.insert(tk.END, str(f"strategy {i4}"))
                        for actionnn in action_listtt:
                            # insert effect for actionn in listbox 4!!!
                            #print(actionnn)
                            effects_str=""
                            actionnn_word_list=actionnn.split(" ")
                            for wordd in actionnn_word_list:
                                #print(actionnn_word_list)
                                #print(wordd)
                                if wordd in self.problem_info_qualitity_dictionary:
                                    wordd_qual_list=self.problem_info_qualitity_dictionary[wordd]
                                    #print(wordd)
                                    #print(wordd_qual_list)
                                    
                                    effects_str+= f"{str(wordd_qual_list)[1:-1]}"
                            self.listboxxy4_methods.insert(tk.END, str(f"{effects_str}"))
                            self.listboxxy3_methods.insert(tk.END, str(f"{actionnn}"))                                   
                            if actionnn in self.problem_tree_problem_strat_list_action_list_dictionary:# check if problem key for the action
                                action_list2=self.problem_tree_problem_strat_list_action_list_dictionary[actionnn]
                                used_values.append(actionnn)
                                if action_list2:
                                    for actionn_mini_list in action_list2:
                                        #self.listboxxy3_methods.insert(tk.END, str(f"{actionn_mini_list}"))
                                        #print(actionn_mini_list)
                                        action_list_list2.append([actionnn,actionn_mini_list])
                            #else:
                            #    self.listboxxy3_methods.insert(tk.END, str(f"{actionnn}"))

                                
  
    def display_strategies_of_selected_problem_strategy(self,event):
          """ press 1 to display strategies for a selected problem and set the problem to the current problem being worked on"""
          # get selection
          content=window.selection_get()
          self.problem_recorded=content
          #self.upload_past_strategy_problem_to_keep_expanding_network(content)#change_current_selected_problem_in_psp need to test
          strategies_list_list=self.life_problem_tree_dag[content]
          self.listboxxy2_methods.delete(0, tk.END)
          for strategy in strategies_list_list:
              self.listboxxy2_methods.insert(tk.END, str(strategy)) 
            
              
       
    def display_individual_action_steps_for_specific_problem(self,event):
        """ this will indivudally display action steps in the third listbox
        press 1 to display this press)ing 1 in second list box"""
        import re
        content=window.selection_get()
        action_list=re.split(",",content[1:-1])
        self.listboxxy3_methods.delete(0, tk.END)
        for action in action_list:
            self.listboxxy3_methods.insert(tk.END, str(action)) 

    #def change_current_selected_problem_in_psp(self):
    #    """ press 2 to select this as the new for problem solving program"""
    #    upload_past_problem_to_keep_expanding_network
    def make_actions_new_problems(self):
        """ """
    def search_for_problem(self):
        """output results at top with most same characters """
    def move_to_higher_problem(self):
        """ press 2 to move back to higher problem of current problem"""
        
        
    def check_for_template(self,template_location):
        """we will save the screenshot to disk and then upload it using cv2 imread """
        import cv2
        import numpy as np
        import pyautogui
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
        screenshot.save(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png")
        img_rgb = cv2.imread(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png")
        template = cv2.imread(template_location)
        h, w = template.shape[:-1] # get the first two dimensions
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)# match the tewmplate against the image to find all images # the matching formula we are using is tm coeff normed it basically miinus two matrix to see differences # and then norms them
        threshold = .9 # threshold amount of match of image on other image in this case 90
        location_of_template = np.where(res >= threshold) # this gets us any point that has a .9 or above
        return location_of_template ,h, w 
    def scroll_up_whole_page(self):
        """ """
        import pyautogui
        import time
        from PIL import ImageGrab
        import numpy as np
        import pytesseract
        for i in range(30):# test this and done
                pyautogui.moveTo(1919, 212)
                pyautogui.scroll(1000)# scroll to the top
                print("scroll")
            
    def wait_till_template_present(self,template_path):
         import pyautogui
         import time
         from PIL import ImageGrab
         import numpy as np
         import pytesseract
         try:
             while True:
              time.sleep(1)
              #pyautogui.click(1700, 971)# this will un highlight a button this is the problem because it moves the cursor
              template_present_value,h, w=self.check_for_template(template_path)
              print(template_present_value)
              if template_present_value[0].any():
               pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))           
               break
              else:
               continue
             time.sleep(0.25)
         
         except:
            input("input here and move to next click needed so skip buttons that screw parts of script up so no restart")
            
    def click_button_once_found(self,template_path):
          """ """
          import pyautogui
          import time
          from PIL import ImageGrab
          import numpy as np
          import pytesseract
          while True:
           pyautogui.click(1700, 971)
           pyautogui.scroll(-1000)
           template_present_value,h, w=self.check_for_template(template_path)#template
           print(template_present_value)
           if template_present_value[0].any():
            pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
            template_present_value,h, w=self.check_for_template(template_path)#template
            if template_present_value[0].any():
                pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
                break
            else:
                break
           else:
            continue      
    def open_blender(self):
         """ """
         import subprocess
         import os
         file_path=r"C:\temp\hi.blend"
         blender_exe_path=r"C:\Program Files\Blender Foundation\Blender 4.1"
         os.chdir(blender_exe_path)
         subprocess.Popen(["blender.exe", r"C:\temp\hi.blend"])
         #subprocess.run(["cd", "C:\Program Files\Blender Foundation\Blender 4.1"])
         #open blender
         #C:\Program Files\Blender Foundation\Blender 4.1
         # this is where blender execute is
         #import subprocess
         #“blender.exe your_file_path. blend”.
         # add script to clipboard generated
         # paste script into console
         # save file
         #bpy.ops.wm.save_as_mainfile(filepath=file_path)# save blender file
         #bpy.ops.wm.open_mainfile(filepath=r"C:\temp\hi.blend")
    def get_access_to_blender_terminal(self):
         """ """
         import pyautogui
         import time
         from PIL import ImageGrab
         import numpy as np
         import pytesseract
         pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
         saved_screen_shots_text_list=[]
         time.sleep(1.044762420654297)
         pyautogui.moveTo(1179, 1072)
         pyautogui.moveTo(41, 834)
         time.sleep(0.9368200302124023)
         print('Pressed(41, 834): 3')
         print('hi [C:\temp\hi.blend] - Blender 4.1')
         self.wait_till_template_present(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\pyautogui_script_106\template1729648676.2845876.png')
    
    def make_it_easier_to_start_working_on_sub_problem_action_in_problem_tree_in_tkinyer(self):
        """make it so you can write into this problem right away """
    
    # blender problem tree functions
   
    def upload_blender_problem_tree_data_from_sql(self):
        """ problem_tree_problem_strat_list_action_list_dictionary : # key[problem]=[strats[actions]] list of list strats and actions"""
        import re
        import copy
        import time
        self.temp_all_strategy_action_list_dictionary={}
        
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table ;""")
        all_strategy_table_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(all_strategy_table_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if problem_being_solved==self.problem_recorded:
                continue# this ensures that we accdinteally double up
            if action_list:
                action_list=re.split(",",action_list[1:-1])
            if problem_being_solved not in self.temp_all_strategy_action_list_dictionary:
                self.temp_all_strategy_action_list_dictionary[problem_being_solved]=[] 
            self.temp_all_strategy_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available  
        #
        
        # repeat this process recursing each action
        # as deep as necessary until certain there are no other strategies witht hat aciton name
        # in the given tree
        self.problem_tree_problem_strat_list_action_list_dictionary={}
        time_qualitity_found =time.time()
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        specific_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(specific_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if action_list:
                action_list=re.split(",",action_list[1:-1])
            if problem_being_solved not in self.problem_tree_problem_strat_list_action_list_dictionary:
                self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved]=[] 
            self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available 
            if action_list:
                action_list_list2=[]
                action_list_list2.append(action_list)
                while True: 
                    if action_list_list2==[]:
                        break
                    action_list_list=action_list_list2
                    action_list_list2=[]
                    for action_listtt in action_list_list:
                        for actionnn in action_listtt:
                            print('ACTION LIST')
                            print(action_listtt)
                            print('ACTION ')
                            # make it so that
                            # it adds to the intital strat line block as seperate tree

                            print(actionnn)
                            if actionnn in self.temp_all_strategy_action_list_dictionary:# check if problem key for the action
                                if actionnn not in self.problem_tree_problem_strat_list_action_list_dictionary:
                                    self.problem_tree_problem_strat_list_action_list_dictionary[actionnn]=[] 
                                action_list2=self.temp_all_strategy_action_list_dictionary[actionnn]
                                if action_list2:
                                    for actionn_mini_list in action_list2:
                                        print(actionn_mini_list)
                                        self.problem_tree_problem_strat_list_action_list_dictionary[actionnn].append(actionn_mini_list)# list of list of strats available 
                                        action_list_list2.append(actionn_mini_list)
                                
                            
                                            
                                        
                                    
                                
                                
   
        #[problem]=[strats[actions]]
        # first get all sub actions
        # then with this list check through other strategy
        # data and if they have sub trees add these in as
        # strats below these strats
        # find sub strategy trees
        # repeat this process as necessary
        # because could be multiple trees deep
        print(self.temp_all_strategy_action_list_dictionary)
        print(self.problem_tree_problem_strat_list_action_list_dictionary)
        return self.problem_tree_problem_strat_list_action_list_dictionary
        # broader principles guding action are in methods table
        #actual actiosn are in strategies table
        #self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM methods_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
        #methods_info= self.cur.fetchall()
    # NEED TO MODIFY ALL OF THESE FOR PROBLEM TREE
   
    def generate_spacing_list_around_cube_problem_tree(self,current_cube_location):
        """ this list will be used as guidance to place other cubes around intital cube"""
        #import random
        possible_cube_placement_list=[]
        #current_cube_location=(1,2,3)
        current_x=current_cube_location[0]
        current_y=current_cube_location[1]
        current_z=current_cube_location[2]
        #x_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        #y_range_list=list(range(0,self.range_cube_distance_list_generation_value,3)) # 0 to 10
        #z_range_list=list(range(0,self.range_cube_distance_list_generation_value,3)) # 0 to 10
        
        x_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        y_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        z_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10



        for x_coridinate in x_range_list:
            for y_coridinate in y_range_list:
                for z_coridinate in z_range_list:
                    possible_future_x=current_x+x_coridinate
                    possible_future_y=current_y+y_coridinate
                    possible_future_z=current_z+z_coridinate
                    possible_cube_placement_list.append((possible_future_x,possible_future_y,possible_future_z))
                    
        #random.shuffle(possible_cube_placement_list) 
        return possible_cube_placement_list
    
    def find_where_to_place_cube_in_blender_problem_tree(self,possible_cube_placement_list,current_cube_location=[0,0,0]):# test this
        """ this will take the possible cube placement list and select a value that works from it
        NEED TO TEST THIS to these if recursion works here"""
        #print(possible_cube_placement_list)
        for i21, cube_placement in enumerate(possible_cube_placement_list):
            if i21==len(possible_cube_placement_list)-1:# this is in case that there is not enough space in the list of positions to place objects    #and this will create more space
                self.range_cube_distance_list_generation_value+=20
                #ERROR IS HERE need to make this function work generating more spaces 
                # WOO!
                # need to think this one out
                possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)
                current_cube_location=self.find_where_to_place_cube_in_blender(possible_cube_placement_list) # this should recurse is necessary
                return current_cube_location
            if cube_placement in self.used_square_location_list:
                continue
            else:
                current_cube_location=cube_placement   
                break
        return current_cube_location
    
    def find_which_cube_to_attach_to_in_current_web_problem_tree(self,action_placement_in_list):
        """figure out how and where to connect """
        action_placement_in_list=int(action_placement_in_list)
        cube_to_attached_to__in_current_web_location=None
        if action_placement_in_list==0:
            cube_to_attached_to__in_current_web_location=(0,0,0)# need to change these names 
            return self.problem_recorded, cube_to_attached_to__in_current_web_location
        else:
            for intital_cube_text in self.blender_problem_tree_dictionary.keys():
                intital_cube_location=self.blender_problem_tree_dictionary[intital_cube_text]["current_cube_location"]
                if intital_cube_text== self.action_listttt[action_placement_in_list-1]:
                    cube_to_attached_to__in_current_web_location=intital_cube_location# need to change these names 
                    return intital_cube_text,cube_to_attached_to__in_current_web_location 
        
    ## NEED TO MODIFY THESE
    def find_intital_cube_to_attach_to_in_current_web_problem_tree(self,problem_name_key):
        """ need to test this"""
        cube_to_attached_to__in_current_web_location=None

        for intital_cube_text in self.blender_problem_tree_dictionary.keys():
            intital_cube_location=self.blender_problem_tree_dictionary[intital_cube_text]["current_cube_location"]
            if problem_name_key == intital_cube_text:
                cube_to_attached_to__in_current_web_location=intital_cube_location# need to change these names
                return problem_name_key, cube_to_attached_to__in_current_web_location
                break        
        intital_cube_location=self.blender_problem_tree_dictionary[self.problem_recorded]["current_cube_location"]
        cube_to_attached_to__in_current_web_location=(0,0,0)
        return self.problem_recorded,cube_to_attached_to__in_current_web_location
         
    def generate_blender_commands_problem_tree_sub(self,problem_name_key,action_listtt):
         """ self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}"""
         import copy
         self.action_listttt=action_listtt
         action_listtt2=copy.deepcopy(action_listtt)
         #print(f"action list: {action_listtt}")
         # find intital cube to attach to of the proibelm being solved
         cube_to_attach_to_name,cube_to_attached_to__in_current_web_location=self.find_intital_cube_to_attach_to_in_current_web_problem_tree(problem_name_key)
         current_cube_location=cube_to_attached_to__in_current_web_location
         for i82, action in zip(range(len(action_listtt2)),action_listtt2):
             shortened_action_name=action[13:]
             shortened_action_name=shortened_action_name[:20]
             # use the placement of the cube we determined witht he inttial placement function for first go
             possible_cube_placement_list=self.generate_spacing_list_around_cube_problem_tree(current_cube_location)  
             current_cube_location=self.find_where_to_place_cube_in_blender(possible_cube_placement_list)
             self.upload_blender_cube_and_text(current_cube_location,action,problem_treee=True,shortened_action_name=shortened_action_name)
             self.upload_blender_cube_edge_connection(action,cube_to_attach_to_name,cube_to_attached_to__in_current_web_location,current_cube_location,problem_treee=True)
             cube_to_attach_to_name=action
             self.used_object_name_list.append(action)

         #if cube_to_attach_to_name==self.problem_recorded:
                 #shortened_problem_name=problem_name_key[13:]
                 #shortened_problem_name=shortened_problem_name[:20]
                 #print(shortened_problem_name)
                 #possible_cube_placement_list=self.generate_spacing_list_around_cube(cube_to_attached_to__in_current_web_location)
                 #current_cube_location=self.find_where_to_place_cube_in_blender(current_cube_location=cube_to_attached_to__in_current_web_location)# fix this
                 #self.upload_blender_cube_and_text(current_cube_location,problem_name_key,problem_treee=True,shortened_action_name=shortened_problem_name)
                 
                 #self.upload_blender_cube_edge_connection(problem_name_key,cube_to_attach_to_name,cube_to_attached_to__in_current_web_location,current_cube_location,problem_treee=True)
                 #self.used_object_name_list.append(problem_name_key)
                 #cube_to_attach_to_name=problem_name_key
                 #possible_cube_placement_list=self.generate_spacing_list_around_cube_problem_tree(cube_to_attached_to__in_current_web_location)

                 
             
             
         #else:
         #    current_cube_location=cube_to_attached_to__in_current_web_location
         #    cube_to_attach_to_name=problem_name_key


        
                 # use intital attachement location and then iterate on rest
             # find how to attach subseqent cubes
             # change for where to attach and then 
             # reuse old algo
             #print(f"action list: {action_listtt}")
             #current_cube_location=self.find_where_to_place_cube_in_blender_problem_tree(possible_cube_placement_list)

   
                
             
    def generate_blender_commands_problem_tree_2(self):
        """ """
        import copy
        self.problem_tree_problem_strat_list_action_list_dictionary=self.upload_blender_problem_tree_data_from_sql()# creates self qualtity dictionary as welll
        self.blender_problem_tree_dictionary={} # leaving as blender problem web dictionary to avoiud other problems
        self.range_cube_distance_list_generation_value=6# test changing this
        self.used_square_location_list=[]
        self.used_objectt_list=[]
        saved_edge_locaiton_list=[]
        # this delete adds to command str to delete allitems currently in the scene
        self.blender_command_str_list=[]
        edge_value_tuple=(0,1)
        self.blender_command_str_list.append(f"import bpy, bmesh\nfaces = []\nname = 'Text Color'\ntext_from_cube_distance=2\nfor ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() ")
        self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
        self.blender_command_str_list.append(f'\nmaterial = bpy.data.materials.new(name+"_material")')
        self.blender_command_str_list.append(f'\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)')
        self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
        self.blender_command_str_list.append("\ncol_name='Collection'")
        self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")       
        # create color material for text
        
        # upload an intital cube named after the problem as root to blender command list
        current_cube_location=(0,0,0)
        self.upload_blender_cube_and_text(current_cube_location,self.problem_recorded,problem_treee=True,shortened_action_name=self.problem_recorded[10:])
        self.used_object_name_list.append(self.problem_recorded)
        # upload intital problem to blender and add to problem dicitonary
        # end state== cubes are added and connected to an existing strategy
        # rather than added from zero sort of like with problem web
        for i3, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary.items()):
            for action_listt in strategy_list:
                self.generate_blender_commands_problem_tree_sub(problem_name_key,action_listt)
  
        
    def generate_blender_commands_problem_tree(self):
        """ """
        import copy
        self.problem_tree_problem_strat_list_action_list_dictionary=self.upload_blender_problem_tree_data_from_sql()# creates self qualtity dictionary as welll
        self.blender_problem_tree_dictionary={} # leaving as blender problem web dictionary to avoiud other problems
        self.range_cube_distance_list_generation_value=6# test changing this
        self.used_square_location_list=[]
        self.used_objectt_list=[]
        saved_edge_locaiton_list=[]
        # this delete adds to command str to delete allitems currently in the scene
        self.blender_command_str_list=[]
        self.blender_command_str_list.append("import bpy, bmesh\nfor ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() ")
        self.blender_command_str_list.append("\nedges_list = [{edge_value_tuple}]")
        
        # create color material for text
        
        # upload an intital cube named after the problem as root to blender command list
        current_cube_location=(0,0,0)
        self.upload_blender_cube_and_text(current_cube_location,self.problem_recorded,problem_treee=True,shortened_action_name=self.problem_recorded[10:])
        # upload intital problem to blender and add to problem dicitonary
        # end state== cubes are added and connected to an existing strategy
        # rather than added from zero sort of like with problem web
        self.problem_tree_problem_strat_list_action_list_dictionary2=copy.deepcopy(self.problem_tree_problem_strat_list_action_list_dictionary)
        
        
        
        
        
        
        
        for i, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary2.items()):
            for i6, action_listt in enumerate(strategy_list):
                for i2,actionnnn in enumerate(action_listt):
                    self.problem_tree_problem_strat_list_action_list_dictionary[problem_name_key][i6][i2]=f"{i2}: {actionnnn}"    
        
        for i3, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary.items()):
            for action_listt in strategy_list:
                self.generate_blender_commands_problem_tree_sub(action_listt)
 
    ### Blender web functions
    def upload_blender_cube_and_text(self,cube_location,intital_cube_text,problem_treee=False,shortened_action_name=""):
        """ create cube and store information in blender problem dictionary"""
         #self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}
        ### clear selection
        #self.blender_command_str+="\nfor obj in bpy.data.collections['MonkeyCollect'].all_objects:"
        #self.blender_command_str+=f"\n obj.select_set(False)"
        ## data storage part
        if problem_treee==False:
            text_from_cube_distance=2
            #self.blender_command_str_list.append("\nimport bpy, bmesh")
            self.blender_command_str_list.append(f"\ncube=bpy.ops.mesh.primitive_cube_add(location={cube_location})")
            self.blender_command_str_list.append(f"\nbpy.data.objects['Cube.001'].name='{intital_cube_text}_cube'")
            #self.blender_command_str_list.append("\ntext_from_cube_distance=2")
            self.blender_command_str_list.append('\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")')
            self.blender_command_str_list.append(f'\nmyFontOb = bpy.data.objects.new("{intital_cube_text}",myFontCurve,)')
            self.blender_command_str_list.append(f'\nmyFontOb.data.body = "{intital_cube_text}"')
            self.blender_command_str_list.append('\nbpy.context.collection.objects.link(myFontOb)')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].location.x = {cube_location[0]+text_from_cube_distance}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].location.y = {cube_location[1]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].location.z = {cube_location[2]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].rotation_euler[0] = 1.5')
            #self.blender_command_str_list.append('\nname = "Text Color"')
            self.blender_command_str_list.append('\nmyFontCurve.materials.append(material)')


            self.used_square_location_list.append(cube_location)
            self.blender_problem_web_dictionary[intital_cube_text]={"current_cube_location":cube_location}
            self.blender_problem_web_dictionary[intital_cube_text]["edge_information"]={}
            
        if problem_treee==True:
            text_from_cube_distance=2
            self.blender_command_str_list.append("\nimport bpy, bmesh")
            self.blender_command_str_list.append(f"\ncube=bpy.ops.mesh.primitive_cube_add(location={cube_location})")
            self.blender_command_str_list.append(f"\nbpy.data.objects['Cube.001'].name='{intital_cube_text}_cube'")
            self.blender_command_str_list.append("\ntext_from_cube_distance=2")
            self.blender_command_str_list.append('\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")')
            self.blender_command_str_list.append(f'\nmyFontOb = bpy.data.objects.new("{shortened_action_name}",myFontCurve,)')
            self.blender_command_str_list.append(f'\nmyFontOb.data.body = "{intital_cube_text}"')
            self.blender_command_str_list.append('\nbpy.context.collection.objects.link(myFontOb)')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].location.x = {cube_location[0]+text_from_cube_distance}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].location.y = {cube_location[1]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].location.z = {cube_location[2]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].rotation_euler[0] = 1.5')
            self.blender_command_str_list.append('\nname = "Text Color"')
            self.blender_command_str_list.append('\nmaterial = bpy.data.materials.new(name+"_material")')
            self.blender_command_str_list.append('\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)')
            self.blender_command_str_list.append('\nmyFontCurve.materials.append(material)')
            self.used_square_location_list.append(cube_location)
            self.blender_problem_tree_dictionary[intital_cube_text]={"current_cube_location":cube_location}
            self.blender_problem_tree_dictionary[intital_cube_text]["edge_information"]={}





            #self.blender_command_str+="\nimport bpy, bmesh"
            #self.blender_command_str+=f"\ncube=bpy.ops.mesh.primitive_cube_add(location={cube_location})"
            #self.blender_command_str+=f"\nbpy.data.objects['Cube.001'].name='{shortened_action_name}_cube'"
            #self.blender_command_str+="\ntext_from_cube_distance=2"
            ##### LEAVE THIS
            # now get text to work
            #self.blender_command_str+='\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")'
            
            

            
            #self.blender_command_str+=f'\nmyFontOb = bpy.data.objects.new("{shortened_action_name}",myFontCurve,)'


            #self.blender_command_str+=f'\nmyFontOb.data.body = "{intital_cube_text}"'
            #self.blender_command_str+='\nbpy.context.collection.objects.link(myFontOb)'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].location.x = {cube_location[0]+text_from_cube_distance}'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].location.y = {cube_location[1]}'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].location.z = {cube_location[2]}'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].rotation_euler[0] = 1.5'
            
            
            
            # add color to the text
            #self.blender_command_str+='\nname = "Text Color"'
            #self.blender_command_str+='\nmaterial = bpy.data.materials.new(name+"_material")'
            #self.blender_command_str+='\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)'
            #self.blender_command_str+='\nmyFontCurve.materials.append(material)'
            #self.blender_command_str+='\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")'

            
            #name = "Poly Line"
            #material = bpy.data.materials.new(name+"_material")
            #material.diffuse_color = (10.0,2.0,0.0,10.0)
            #myFontCurve.materials.append(material)
            #myFontCurve.bevel_depth = 0.2


            #bpy.context.object.rotation_euler[0] = 0.401426

            
            
        
        
        # deselect all objects
       

        #self.blender_command_str+="\n "

        #for obj in bpy.context.selected_objects:
        #for obj in bpy.data.collections['MonkeyCollect'].all_objects:
        #    obj.select_set(False)
                
        #self.blender_command_str+=f"\n bpy.data.objects[obj].select = False"

        # PROBLEM YTOMORROW FIND WAY TO ADD CUBE IN SO CAN NAME IT

        #bpy.data.objects["Cube.001"].name="haha"
        #self.blender_command_str+=f"\nbpy.data.objects[-2].name='{intital_cube_text}'"

        
        #new_obj = bpy.data.objects.new('new_obj', None) 
        #new_obj.location = (x[index],y[index],z[index])
        #bpy.context.scene.objects.link(new_obj)
        #object = bpy.data.objects.get('OldName')
        
        #self.blender_command_str+=f"\nobject = bpy.data.objects.get('Cube.001')"
        #self.blender_command_str+=f"\nobject.name = '{intital_cube_text}'"
        #self.blender_command_str+=f"\nobject.location = {cube_location}"


        
        #self.blender_command_str+=f"\ncube = bpy.context.selected_objects[0]"
        #self.blender_command_str+=f"\ncube.name = '{intital_cube_text}'"
        ####
        
        
        #for obj in bpy.data.collections['MonkeyCollect'].all_objects:
        #    obj.select_set(False)
        #self.blender_command_str+="\nfor obj in bpy.context.selected_objects:"
        #self.blender_command_str+=f"\n bpy.data.objects[obj].select = False"
        #self.blender_command_str+=f"\nbpy.data.objects['{intital_cube_text}'].select = False"

        
        
        #self.blender_command_str+="\nimport bpy, bmesh"
        #self.blender_command_str+=f"\nbpy.ops.mesh.primitive_cube_add()"
        #self.blender_command_str+=f"\ncube = bpy.context.selected_objects[-1]"
        #self.blender_command_str+=f"\ncube.name = '{intital_cube_text}'"
        #self.blender_command_str+=f"\ncube.location = {cube_location}"


        
        
        #cube = bpy.context.selected_objects[0]
        #cube.name = "MyLittleCube

        
        
        
        ### super important do not erase this!
        #import bpy, bmesh
        #bpy.ops.mesh.primitive_cube_add(location=cube_location)
        #text_from_cube_distance=2
        #bpy.ops.object.text_add(location=(x+text_from_cube_distance,y,z))
        #ob=bpy.context.object
        #ob.data.body = object_text
        #self.blender_command_str+="\nbpy.ops.object.text_add(location=(x+text_from_cube_distance,y,z))"
        #self.blender_command_str+="\nob=bpy.context.object"
        #self.blender_command_str+=f"\nob.data.body = '{intital_cube_text}'"
    def upload_blender_cube_edge_connection(self,intital_cube_text,attached_cube_text,intital_cube_location,attached_cube_location,problem_treee=False):
        """record_names of lines in blender problem dcitionary created to modify later to show effects of actions """
         #self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}
         ## upload to blender part
        # need to deal with
        
        # data storage part
        edge_value_tuple=(0,1)
        if problem_treee==False:
            #self.blender_command_str_list.append("\nimport bpy, bmesh")
            #self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
            self.blender_command_str_list.append(f"\nvertices_list=[{intital_cube_location},{attached_cube_location}]")
            #self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
            #self.blender_command_str_list.append("\nfaces = []")
            self.blender_command_str_list.append("\nnew_mesh = bpy.data.meshes.new('new_mesh')")
            self.blender_command_str_list.append("\nnew_mesh.from_pydata(vertices_list, edges_list, faces)")
            #self.blender_command_str_list.append("\nnew_mesh.update()")
            self.blender_command_str_list.append(f"\nnew_line = bpy.data.objects.new(f'edge', new_mesh)")
            #self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")
            self.blender_command_str_list.append("\ncol.objects.link(new_line)")
            self.blender_problem_web_dictionary[intital_cube_text]["edge_information"][attached_cube_text]={"edge_object_name":f'edge{intital_cube_text}:::{attached_cube_text}',"intital_cube_text":intital_cube_text, "attached_cube_text":attached_cube_text,"intital_cube_location":intital_cube_location,"attached_cube_location":attached_cube_location}
        if problem_treee==True:
            self.blender_command_str_list.append("\nimport bpy, bmesh")
            self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
            self.blender_command_str_list.append(f"\nvertices_list=[{intital_cube_location},{attached_cube_location}]")
            self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
            self.blender_command_str_list.append("\nfaces = []")
            self.blender_command_str_list.append("\nnew_mesh = bpy.data.meshes.new('new_mesh')")
            self.blender_command_str_list.append("\nnew_mesh.from_pydata(vertices_list, edges_list, faces)")
            self.blender_command_str_list.append("\nnew_mesh.update()")
            self.blender_command_str_list.append(f"\nnew_line = bpy.data.objects.new(f'edge{intital_cube_text}:::{attached_cube_text}', new_mesh)")
            self.blender_command_str_list.append("\ncol_name='Collection'")
            self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")
            self.blender_command_str_list.append("\ncol.objects.link(new_line)")
            self.blender_problem_tree_dictionary[intital_cube_text]["edge_information"][attached_cube_text]={"edge_object_name":f'edge{intital_cube_text}:::{attached_cube_text}',"intital_cube_text":intital_cube_text, "attached_cube_text":attached_cube_text,"intital_cube_location":intital_cube_location,"attached_cube_location":attached_cube_location}

            
            
            #self.blender_command_str+="\nimport bpy, bmesh"
            #self.blender_command_str+="\nedge_value_tuple=(0,1)"
            #self.blender_command_str+=f"\nvertices_list=[{intital_cube_location},{attached_cube_location}]"
            #elf.blender_command_str+=f"\nedges_list = [{edge_value_tuple}]"
            #self.blender_command_str+="\nfaces = []"
            #self.blender_command_str+="\nnew_mesh = bpy.data.meshes.new('new_mesh')"
            #self.blender_command_str+="\nnew_mesh.from_pydata(vertices_list, edges_list, faces)"
            #self.blender_command_str+="\nnew_mesh.update()"
            #self.blender_command_str+=f"\nnew_line = bpy.data.objects.new(f'edge{intital_cube_text}:::{attached_cube_text}', new_mesh)"
            #self.blender_command_str+="\ncol_name='Collection'"
            #self.blender_command_str+="\ncol = bpy.data.collections.get(col_name)"
            #self.blender_command_str+="\ncol.objects.link(new_line)"
            
            # add color STILL NEED TO FIGURE OUT HOW TO GIVE MESH COLO%
            #self.blender_command_str+='\nname = "Text Color"'
            #self.blender_command_str+='\nmaterial = bpy.data.materials.new(name+"_material")'
            #self.blender_command_str+='\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)'
            #self.blender_command_str+='\nnew_mesh.materials.append(material)'
            
  
            
            
            

            
        #### this is super important do not erase this
        #import bpy, bmesh
        #edge_value_tuple=(0,1)# this connect the first and second vertics in the list  line vertices list
        #vertices_list=[intital_cube_placement,current_cube_location]
        #edges_list = [edge_value_tuple]# numbers refer to the vertice location in the list i think
        #faces = []
        #new_mesh = bpy.data.meshes.new('new_mesh')
        #new_mesh.from_pydata(line_vertices, edges_list, faces)
        #new_mesh.update()
        #new_line = bpy.data.objects.new(f'edge{i}', new_mesh)
        #col_name="Collection"
        #col = bpy.data.collections.get(col_name)  
        #col.objects.link(new_line) # this links to an existing collection
    def genereate_blender_node_and_edge_lists(self,amount_of_node_to_displayed=1000,effects_web=False,methods_problem_recorded="",strategy_list=[]):# amount of node displayed is to deal with overloading blender
        """use auto problem table here instead now """
        import re
        import copy
        import time
        self.node_qualitity_dictionary={}
        time_qualitity_found =time.time()
        node_counter=0
        if effects_web==True:
            self.problem_recorded=methods_problem_recorded
            # may need to change this not keep same problem
            print('EFFECT WEB')
            print(methods_problem_recorded)
            print(strategy_list)
            self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{methods_problem_recorded}';""")
            problem_objects_and_qualtity_list= self.cur.fetchall()
            self.strategy_recorded
            for i16,objecttt in enumerate(problem_objects_and_qualtity_list):
                specific_problem_or_object= objecttt[0]
                qualitity_list= objecttt[1]
                #print('obect and qual')
                #print(specific_problem_or_object)
                #print(qualitity_list)
                if specific_problem_or_object==self.problem_recorded:# need to make sure add intital probelm and qualtites
                    print(qualitity_list)
                    if qualitity_list:
                        qualitity_list=re.split(",",qualitity_list[1:-1])
                        
                    self.node_qualitity_dictionary[specific_problem_or_object]=[]  
                    for i10, qualityy2 in enumerate(qualitity_list):# limiting to 10 for now add more as necessary
                        node_counter+=1
                        if qualityy2 in self.node_qualitity_dictionary[specific_problem_or_object]:
                            continue
                        else:
                            self.node_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   
                    continue  
                for actionnn in strategy_list:
                    if specific_problem_or_object not in actionnn:
                        continue
                    else:
                        #print("object found in action")
                        #print(specific_problem_or_object)
                        #print(actionnn)
                        #if node_counter>=amount_of_node_to_displayed:# need to test this
                        #    break
                        if qualitity_list:
                            qualitity_list=re.split(",",qualitity_list[1:-1])
                        if specific_problem_or_object not in self.node_qualitity_dictionary:
                            node_counter+=1
                            self.node_qualitity_dictionary[specific_problem_or_object]=[]  
                        for i10, qualityy2 in enumerate(qualitity_list[:20]):# limiting to 10 for now add more as necessary
                            node_counter+=1
                            if qualityy2 in self.node_qualitity_dictionary[specific_problem_or_object]:
                                continue
                            else:
                                self.node_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   
                        break
                    
                        

            
        if effects_web==False:# starting from probelm recorded
            print(f"problem recroded {self.problem_recorded}")
            #?? how do i improve the problem solving program'
            # add intital problem object when creating objects for auto_problem_table
            self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
            problem_objects_and_qualtity_list= self.cur.fetchall()
            #print(problem_objects_and_qualtity_list)
            # what now
            for i16,objecttt in enumerate(problem_objects_and_qualtity_list):
                print(node_counter)

                if node_counter>=amount_of_node_to_displayed:
                    break
                specific_problem_or_object= objecttt[0]
                qualitity_list= objecttt[1]
                node_counter+=1 # objectt
                if qualitity_list:
                    qualitity_list=re.split(",",qualitity_list[1:-1])
                if specific_problem_or_object not in self.node_qualitity_dictionary:
                    self.node_qualitity_dictionary[specific_problem_or_object]=[]  
                for i10, qualityy2 in enumerate(qualitity_list):
                    node_counter+=1
                    #qualitityy=qualityy2[1]
                    if qualityy2 in self.node_qualitity_dictionary[specific_problem_or_object]:
                        continue
                    else:
                        self.node_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   
            
        
        print(self.node_qualitity_dictionary)
        return self.node_qualitity_dictionary
    def generate_spacing_list_around_cube(self,current_cube_location):
        """ this list will be used as guidance to place other cubes around intital cube"""
        import random
        #rand_list=[]
        #n=10
        #for i in range(n):
        #    rand_list.append(random.randint(3,9))
        #print(rand_list)
        self.possible_cube_placement_list=[]
        current_x=current_cube_location[0]
        current_y=current_cube_location[1]
        current_z=current_cube_location[2]
        x_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,4))# -10 to 10
        y_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,4))# -10 to 10
        z_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,4))# -10 to 10
        for x_coridinate in x_range_list:
            for y_coridinate in y_range_list:
                for z_coridinate in z_range_list:
                    possible_future_x=current_x+x_coridinate
                    possible_future_y=current_y+y_coridinate
                    possible_future_z=current_z+z_coridinate
                    self.possible_cube_placement_list.append((possible_future_x,possible_future_y,possible_future_z))
                            
        random.shuffle(self.possible_cube_placement_list) 
        return self.possible_cube_placement_list
    
    # THESE TWO FUNCTION NEED TO WORK ON  
    def find_where_to_place_cube_in_blender(self,current_cube_location=[0,0,0]):
        """ this will take the possible cube placement list and select a value that works from it
        NEED TO TEST THIS to these if recursion works here"""
        #print(possible_cube_placement_list)
        for i21, cube_placement in enumerate(self.possible_cube_placement_list):
            if cube_placement not in self.used_square_location_list:
                current_cube_location=cube_placement   
                break
            if i21==len(self.possible_cube_placement_list)-1:# this is in case that there is not enough space in the list of positions to place objects    #and this will create more space
                self.range_cube_distance_list_generation_value+=10
                self.possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)
                current_cube_location=self.find_where_to_place_cube_in_blender() # this should recurse is necessary
                return current_cube_location
            
            
        return current_cube_location
    def retrieve_data_from_website_database(self,table_name,where_string):
     ''' add button? and timer?''' 
     import psycopg2
     from psycopg2 import sql
     host = '192.168.0.16'  # E.g., '192.168.1.100' or 'your-database-server.com'
     port = '5432'  # Default PostgreSQL port
     dbname = 'canlawaccessible'  # E.g., 'myprojectdb'
     user = 'jross77'  # E.g., 'myuser'
     password = 'MeganisGreat'  # E.g., 'mypassword'
     try:
         self.conn = psycopg2.connect(host=host,
         port=port,
         dbname=dbname,
         user=user,
         password=password) 
         self.cur = self.conn.cursor() 
         sql_str=f"SELECT * FROM {table_name}{where_string};"
         try:
             self.cur.execute(sql_str)
         except Exception as E:
             print(E)
         sql_data_list_list= self.cur.fetchall()
         
         self.conn.commit()
     except Exception as e:
             print(f"Error: {e}")     
     self.cur.close()
     self.conn.close()
     print("Connection closed.")
     return  sql_data_list_list
 
    def retrieve_data_from_pyautogui_website_database(self):
        """ """
        table_name="pyautogui_content"
        where_string=""
        sql_data_list_list=self.retrieve_data_from_website_database(table_name,where_string)
        print(sql_data_list_list)
        return column_name_data_type_dic
    
    
    
    
    
    
    def find_which_cube_to_attach_to_in_current_web(self,objecttt,qualtity_list):
        """figure out how and where to connect """
        cube_to_attached_to__in_current_web_location=None
        for intital_cube_text in self.blender_problem_web_dictionary.keys():
            intital_cube_location=self.blender_problem_web_dictionary[intital_cube_text]["current_cube_location"]
            if objecttt == intital_cube_text:
                cube_to_attached_to__in_current_web_location=intital_cube_location# need to change these names  
                break
                
           
        if cube_to_attached_to__in_current_web_location:
            return objecttt, cube_to_attached_to__in_current_web_location 
        else:
            intital_cube_location=self.blender_problem_web_dictionary[self.problem_recorded]["current_cube_location"]
            cube_to_attached_to__in_current_web_location=(0,0,0)
            return self.problem_recorded,cube_to_attached_to__in_current_web_location
        
        
        #intital_cube_text=edge_cube_names[intital_cube_text]["edge_information"]["intital_cube_text"]
        #current_cube_text=edge_cube_names[intital_cube_text]["edge_information"]["current_cube_text"]
        #intital_cube_location=self.blender_problem_web_dictionary[edge_cube_names][intital_cube_text]["edge_information"]["intital_cube_location"]
        #current_cube_location=edge_cube_names[intital_cube_text]["edge_information"]["current_cube_location"]
        # need to create blender dicitonary
        # have to create blender problem web dicitonary first
        #self.blender_problem_web_dictionary[intital_cube_text]={"current_cube_location":cube_location}
        #self.blender_problem_web_dictionary[intital_cube_text]["edge_information"][edge_cube_text]={"intital_cube_text":intital_cube_text, "current_cube_text":current_cube_text,"intital_cube_location":intital_cube_location,"current_cube_location":current_cube_location}
        
        #existing_cube_location=blender_problem_web_dictionary[cube_to_attach_to_text]["current_cube_location"]
        
        
       # for existing_cube_text in blender_problem_web_dictionary.keys():
        #    existing_cube_location=blender_problem_web_dictionary[objecttt]["current_cube_location"]
        #    
         #   blender_problem_web_dictionary[existing_cube_text]["edge_information"]
          #  self.node_qualitity_dictionary()
            

        
        #cube_location=blender_problem_web_dictionary[current_objecttt]["current_cube_location"]
        # connect to the first cube that it would be a qualtity, and if no qualtity then just connect to og problem web
        # eventually need to add connections to the proper cubes though        
        # if no match found

    def upload_objectts_and_qual_to_blenderr_and_modify_blender_problem_dictionary(self,objecttt,qualtity_list):
         """ self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}"""
         
         if objecttt==self.problem_recorded:# this is hte root of the web
             current_cube_location=(0,0,0)
             self.upload_blender_cube_and_text(current_cube_location,objecttt)
             self.used_object_name_list.append(objecttt)
             
         if objecttt in self.used_object_name_list:
             print('hi')
             cube_to_attach_to_name,current_cube_location=self.find_which_cube_to_attach_to_in_current_web(objecttt,qualtity_list)
             
         else:
             cube_to_attach_to_name=self.problem_recorded
             cube_to_attached_to__in_current_web_location=(0,0,0)
             self.possible_cube_placement_list=self.generate_spacing_list_around_cube(cube_to_attached_to__in_current_web_location)
             current_cube_location=self.find_where_to_place_cube_in_blender()
             self.upload_blender_cube_and_text(current_cube_location,objecttt)
             self.upload_blender_cube_edge_connection(cube_to_attach_to_name,objecttt,cube_to_attached_to__in_current_web_location,current_cube_location)
             self.used_object_name_list.append(objecttt)
             edge_str=f"{cube_to_attach_to_name}:{objecttt}"
             self.used_edge_name_list.append(edge_str)

   
         for qualitityy in qualtity_list:
             if qualitityy in self.used_object_name_list:
                 #print('meow')
                 edge_str=f"{objecttt}:{qualitityy}"
                 edge_str_reverse=f"{qualitityy}:{objecttt}"
                 cube_to_attach_to_name,qual_cube_location=self.find_which_cube_to_attach_to_in_current_web(qualitityy,qualtity_list)
                 self.upload_blender_cube_edge_connection(objecttt,qualitityy,current_cube_location,qual_cube_location)
                 self.used_edge_name_list.append(edge_str)
                 if edge_str_reverse in self.used_edge_name_list:# check if edge in blender already exists
                     print('hio')
                     continue
                 
 
             else:
                 self.possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)
                 qual_cube_location=self.find_where_to_place_cube_in_blender(current_cube_location=current_cube_location)
                 self.upload_blender_cube_and_text(qual_cube_location,qualitityy)
                 self.upload_blender_cube_edge_connection(objecttt,qualitityy,current_cube_location,qual_cube_location)
                 self.used_object_name_list.append(qualitityy)
                 edge_str=f"{objecttt}:{qualitityy}"
                 self.used_edge_name_list.append(edge_str)
      
                 
             #print(qualitityy)
             #edge_str_reverse=f"{qualitityy}:{objecttt}"
             #if edge_str_reverse in self.used_edge_name_list:# check if edge in blender already exists
             #    print('hio')
             #    continue
             #if edge_str in self.used_edge_name_list:
             #    print('hio')
             #    continue
             #else:
             
            
    def generate_blender_commands_problem_web(self, effects_web=False,methods_problem_recorded="",strategy_list=[]):
        """ """
        #self.problem_recorded=problem_recorded
        print(f" problemee {self.problem_recorded}")
        self.node_qualitity_dictionary=self.genereate_blender_node_and_edge_lists(amount_of_node_to_displayed=100,effects_web=effects_web,methods_problem_recorded=methods_problem_recorded,strategy_list=strategy_list)# creates self qualtity dictionary as welll
        #import bpy, bmesh
        #from random import randint
        #used_object_list=[]
        self.blender_problem_web_dictionary={}
        self.range_cube_distance_list_generation_value=6# test changing this
        current_cube_location=(0,0,0)
        #self.possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)#
        self.used_square_location_list=[]
        self.used_object_name_list=[]
        self.used_edge_name_list=[]
        saved_edge_locaiton_list=[]
        # this delete adds to command str to delete allitems currently in the scene
        self.blender_command_str_list=[]
        edge_value_tuple=(0,1)
        self.blender_command_str_list.append(f"import bpy, bmesh\nfaces = []\nname = 'Text Color'\ntext_from_cube_distance=2\nfor ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() ")
        self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
        self.blender_command_str_list.append(f'\nmaterial = bpy.data.materials.new(name+"_material")')
        self.blender_command_str_list.append(f'\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)')
        self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
        self.blender_command_str_list.append("\ncol_name='Collection'")

        self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")

        
        
        # upload intital problem to blender and add to problem dicitonary
        intital_problem_qualtity_list=self.node_qualitity_dictionary[self.problem_recorded]
        print(intital_problem_qualtity_list)
        self.upload_objectts_and_qual_to_blenderr_and_modify_blender_problem_dictionary(self.problem_recorded,intital_problem_qualtity_list)
        for i, (objectt,qualitity_list) in enumerate(self.node_qualitity_dictionary.items()):
            if objectt==self.problem_recorded:
                continue
            print(i)
            #print(objectt)
            #print(qualitity_list)
            self.upload_objectts_and_qual_to_blenderr_and_modify_blender_problem_dictionary(objectt,qualitity_list)
            #remove all used values
            #for i21, cube_placement in enumerate(self.possible_cube_placement_list):
            #    if cube_placement not in self.used_square_location_list:
            #        self.possible_cube_placement_list=self.possible_cube_placement_list[i21:]
            #        break
                    
            
            
        
        # run this as a script basically in blender
        #intital_cube_problem_location=(0,0,0)
        #for ob in bpy.data.objects:
        #    print(ob.name)
        #    ob.select_set(True)
        #    bpy.ops.object.delete()     
    
        
    def execute_blender_command_list(self):
           """ """
           import pyautogui
           import pyperclip
           import time
           #self.blender_command_str="for ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() "
           self.blender_command_str="".join(self.blender_command_str_list)
           print(len(self.blender_command_str_list))
           pyperclip.copy(self.blender_command_str)
           pyautogui.hotkey("ctrl","v")
           pyautogui.press("enter")
           pyautogui.press("enter")

           
           #pyperclip.copy(rf"filename = r'{python_script_name}'")
           #pyautogui.hotkey("ctrl","v")
           #pyautogui.press("enter")
           ## copy the problem to clipboard
           #pyperclip.copy(rf"problem_name = {self.problem_recorded}")
           #pyautogui.hotkey("ctrl","v")
           #pyautogui.press("enter")
           # run a script
           #time.sleep(0.5)
           #pyautogui.write("exec(compile(open(filename).read(), filename, 'exec'))")
           #pyautogui.press("enter")
           #exec(compile(open(filename).read(), filename, 'exec'))
           #pyperclip.copy(r"\\nexec(compile(open(filename).read(), filename, 'exec'))")
           #pyautogui.hotkey("ctrl","v")
           #pyautogui.press("enter")     
     # get the data problem tree dic and problem web dic
     # perform necessary operations on each object generate the web
     # placing it in the blender file accordingly
        
    def generate_and_open_blender_problem_web_and_tree(self,event):
        """ press 3 on first listbox  to generate problem tree and web DONE"""
        # run this externally?
        from multiprocessing import Process
        import sys
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
        #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
        # going to affect them when they age
        #from Problems_functions import problems_functions
        #from Problems_functions import methods_window_program
        from generate_and_open_blender_problem_web_and_tree import generate_and_open_blender_problem_web_and_tree_functions
        #from problem_solving_project_gui_10 import buttons_per_quadrant
        #buttons=buttons_per_quadrant()
        self.problem_recorded=window.selection_get()
        genn_blend_functions=generate_and_open_blender_problem_web_and_tree_functions()
        process = Process(target=genn_blend_functions.generate_and_open_blender_problem_web_and_tree_f,args=(self.problem_recorded,))
        #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        process.start()
        # generate web
        #self.open_blender()
        #self.get_access_to_blender_terminal()
        #self.generate_blender_commands_problem_web()
        #self.execute_blender_command_list()
        #problem_web_script=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Building\tkinyer_building\genereate_problem_web.py"
        #self.execute_command_to_execute_python_script(problem_web_script)

        
        # generate tree
        #self.open_blender()
        #self.get_access_to_blender_terminal()
        #self.generate_blender_commands_problem_tree_2()
        #self.execute_blender_command_list()
        
       

        #self.execute_command_to_execute_python_script()
        ### add these following ones to a script to execute
        #self.generate_and_open_blender_problem_web_and_tree_sub_script()
        #self.generate_blender_problem_tree()
        #self.generate_blender_problem_web()
        #self.open_blender_problem_web()
        #self.open_blender_problem_tree()
        
   
         
     
    def show_effects_of_strategy_in_problem_web(self):
         """ change color of the edges associated with certain objects in problem web"""
         self.blender_problem_web_dictionary[intital_cube_text]={"cube_location":cube_location}
         self.blender_problem_web_dictionary[intital_cube_text]["edge_information"][edge_cube_text]={"intital_cube_text":intital_cube_text, "current_cube_text":current_cube_text,"intital_cube_location":intital_cube_location,"current_cube_location":current_cube_location}
    
    
   
         
                                              
          
                                              
          
                                              
    
         
    
    
    
    
    # 
    def record_key_strokes_and_screen_location_and_upload_to_database_to_record_problems_solved_in_a_day_and_time_taken_to_solve_problem(self):
        """ how will i use this data to then solve problems faster"""
       
 
    def init_methods_window(self,problem_text):
        """create main tkinyer window """
        self.window_methods2 = tk.Tk()
        self.window_methods2.state('zoomed')
        self.window_methods2.config(bg="white")
        self.window_methods2.title(problem_text)
        self.window_methods2.columnconfigure(0, weight=1, minsize=75)
        self.window_methods2.rowconfigure(0, weight=1, minsize=50) 
     
    def init_methods_frames(self,bg_color="blue"):
        """ add frames to application"""
        self.main_frame2_methods = tk.Frame(master=self.window_methods2, relief=tk.RAISED, borderwidth=1)
        self.main_frame2_methods.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
        self.main_frame3_methods = tk.Frame(master=self.window_methods2, relief=tk.RAISED, borderwidth=1)
        self.main_frame3_methods.grid(row=0,column=1)#column=0, columnspan=4 #row=2,columnspan=2
    def init_methods_text_box(self,font_size=10,font_type='Microsoft YaHei'):
        """ methods for textbox"""
        self.screen_width_characters=self.screen_width*0.125
        self.screen_height_characters=self.screen_height*0.125
        font_type_and_size= (font_type,font_size)
        self.text_box1_methods = tk.Text(self.main_frame2_methods,bd=1,height=self.listbox_height,width=int(round(35*self.screen_width_characters/100)))#width=100
        self.text_box1_methods.config(font=font_type_and_size)
        self.text_box1_methods.grid(row=1,column=0)  #columnspan = 9#row=iterator
        #self.text_box.config(state="disabled",font=font_type_and_size)
        self.text_box2_methods = tk.Text(self.main_frame3_methods,bd=1,height=self.listbox_height,width=int(round(65*self.screen_width_characters/100)))#width=100
        self.text_box2_methods.config(font=font_type_and_size)
        self.text_box2_methods.grid(row=1,column=0)  #columnspan
    def init_methods_labels(self):
        """ add labels to application"""
        label = tk.Label(master= self.main_frame2_methods,text="Strategies", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')
        label = tk.Label(master= self.main_frame3_methods,text="Actions", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')
    def init_methods_buttons(self):
        """add buttons to application """
        self.button_2_websites = customtkinter.CTkButton(master= self.main_frame2_methods, text="access_something",text_color='white')
        self.button_2_websites.grid(row=2, column=0, sticky="nsew")
        self.button_3_websites = customtkinter.CTkButton(master= self.main_frame3_methods, text="access_something",text_color='white')
        self.button_3_websites.grid(row=2, column=0, sticky="nsew")
    def show_method_steps(self,event):
        """show the actions and strategies for a given problem """
        import re
        method_step_name_dic={}
        action_step_name_dic={}
        final_method_list=[]
        final_action_list=[]
        final_value_order_list=[]
        content=window.selection_get()
        content2=re.sub("[\[\]{}]","",content)
        title_text=content2[:30]
        #self.listboxxy1_methods.delete(0, tk.END)
        self.init_methods_window(title_text)
        self.init_methods_frames()
        self.init_methods_text_box()
        self.init_methods_labels()
        self.init_methods_buttons()

        self.cur.execute(f"""SELECT * FROM methods_table WHERE problem_being_solved = '{content2}' ;""")
        methods_worked_on= self.cur.fetchall()
        method_list_str=""
        for  method_object in methods_worked_on:
            method_step_name=method_object[2]
            step_number=method_object[6]
            step_number=re.sub(r"\n","",step_number)
            step_number=int(step_number)
            actions_for_step=method_object[8]
            if actions_for_step:
                actions_for_step=re.sub("[\[\]{}]","",actions_for_step)
                actions_for_step=re.split(",",actions_for_step)
            action_or_strategy_label=method_object[9]
            print(action_or_strategy_label)
            #print('meow')
            action_step_name_dic[step_number]=[]
            method_step_name_dic[step_number]=[]
            
            if action_or_strategy_label=="[action]" :
                action_step_name_dic[step_number].append(method_step_name)
                if actions_for_step:
                    action_step_name_dic[step_number].append(actions_for_step)
                    continue 
                continue
            else:
                
                method_step_name_dic[step_number].append(method_step_name)
                #print(method_step_name_dic)
                if actions_for_step:
                    action_step_name_dic[step_number].append(actions_for_step)
                    #print(method_step_name_dic)
                    continue
                continue
        keys_list=action_step_name_dic.keys()
        max_value=max(keys_list)+1
        empty_action_list= [None] * max_value
        empty_method_list= [None] * max_value
        for ii1, (key, action) in enumerate(method_step_name_dic.items()):
             keyyy=int(key)
             empty_method_list[keyyy]=[keyyy, action]        
        for ii1, (key, action) in enumerate(action_step_name_dic.items()):
             keyyy=int(key)
             empty_action_list[keyyy]=[keyyy, action]
        if method_step_name_dic:
            for i4, methoddd in enumerate(empty_method_list):
                if methoddd==None:
                    continue
                if i4==0:
                    insert_value1=f"{methoddd[0]}: {methoddd[1]}"
                    insert_value1=re.sub("[\[\]{}\']","",insert_value1)
                    self.text_box1_methods.insert(tk.END, f"{insert_value1}") 
                    continue  
                insert_value1=f"{methoddd[0]}: {methoddd[1]}"
                insert_value1=re.sub("[\[\]{}\']","",insert_value1)
                self.text_box1_methods.insert(tk.END, f"\n--------------------------------------\n{insert_value1}") 
                continue
        if action_step_name_dic:
            for i5,actionn in enumerate(empty_action_list):
                if actionn==None:
                    continue
                if i5==0:
                    insert_value2=f"{actionn[0]}: {actionn[1]}"
                    insert_value2=re.sub("[\[\]{}\']","",insert_value2)
                    self.text_box2_methods.insert(tk.END, f"{insert_value2}")   
                    continue 
                insert_value2=f"{actionn[0]}: {actionn[1]}"
                insert_value2=re.sub("[\[\]{}\']","",insert_value2)
                self.text_box2_methods.insert(tk.END, f"\n------------------------------------------------------------------------------------\n{insert_value2}")   
                continue

    def show_problemss(self,event):
        """ go back to orignal listed problem window """

        self.cur.execute(f"""SELECT * FROM methods_table ;""")
        methods_worked_on= self.cur.fetchall()
        list_of_problems=[]
        method_list_str=""
        for problemm1 in methods_worked_on:
            problemmm=problemm1[1]
            if problemmm not in list_of_problems:
                method_list_str+= f"{problemmm}\n"  
                list_of_problems.append(problemmm)
        self.listboxxy1.delete(0, tk.END)
        self.listboxxy2.delete(0, tk.END)
        self.listboxxy1.insert(tk.END, method_list_str) 
    def subprocess_popen_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         p=subprocess.Popen(command_list)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
         print('ERROR')
     return p
    def subprocess_run_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         subprocess.run(command_list, check=True,shell=True)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
   
    def insert_other_problem_method_into_current_problem_strategy(self):
        """have a button to  inset a problem inot a current method to connect htem like a strategy into a method"""
        
        # step 2
        #get values of past problems into window and there sub step components
        # step 3 
        # get the values working in hotkeys and when we add them add them to method dictionary into actions box as a list and
        # either add entire problem or add a sub part of problem  using comma system
        # add the problem name in past problem connection
        
        
        
        
        # find way to add these methods and sub components
        #to a given step or an existing step?, no just erase rather than modify or add another step
        # post them automatically in sub methods box on start up of method
        # find sub method box load up part and then just load past problems instead
        # semi colon and then method steps divided by commas to 
        # follow same strcture as current connected objects
        # need to add this to starcraft hotkeys for uploading this step
        
        
        
        # step 4
        # add values to step dictionary
        # and add that this came from this past problem into the past_problem_connection column 
        
        # step 5 
        #access these in the  window like any other method and make it easier to see even its super long
 
        # step 6
        # past_problem_connection column used for writing in switch past problem is connected to this method step
        
        
        # should strategies be just questions we ask ourselves, in order to proompt actions when using a method

        
        

        

class problem_solving_program(quadrants_of_program):
    # need to fix labeling strcture of everything
    # to implement the starcraft thing more easily
    def __init__(self):
        if __name__ == "__main__":
            #window.bind("`",self.starcraft_hotkey_access_elements)
            quad = quadrants_of_program()
            
            #import os
            # start obs studio automaitcally add this in
            #os.system("python testing_record_screen.py")
            import subprocess
            #NEED TO FIX THIS TOMORROW
            
            #subprocess.Popen(["python", "record_screen_for_additonal_problem_data_and_send_to_sql_and_update_psp.py"])
            # turn record screen into completely seperate process
            print('TURN BACK ON PYAUTOGUI CREATION PROGRAAM THIS AS SOON AS I HAVE SPACE ON COMPUTER')
            subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Inputs\pyautogui\init_pyauto_gui_creation_script_program.py"])
            
            subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Inputs\Tkinyer_gui_master_code_inputs\load_in_gui2.py"])
            
            
            
            # NEEDT TO WRITE TGESE TWO
            
            #update databases with all local content
            print('STILL NEED TO TEST if backup of  values locally to remotely is working AT ONE POINT')

            subprocess.run(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\upload_local_pyauto_scripts_not_on_website_database.py"])
            print('upload_local_pyauto_scripts_not_on_website_database')

            
            # this is the back up funciton to big black to tempeoraly back up the database on start up so dont lose anything still need to write this
            # will need to run this remotely on website server
            print('STILL NEED TO TEST if backup of  values on website back up to big black  AT ONE POINT')

            subprocess.run(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\backup_both_pyauto_action_and_usable_table_to_big_black_from_website_among_oher_tables.py"])
            print('backup_both_pyauto_action_and_usable_table_to_big_black_from_website_among_oher_tables')

            
            #process = Process(target=record_screennn.record_screen_for_additonal_problem_data_and_send_to_sql_function,args=("",)) 
            #process.start()
            #window.mainloop()
            for i in range(3):
                window.columnconfigure(i, weight=1, minsize=75)
                window.rowconfigure(i, weight=1, minsize=50)
                for j in range(0, 3):
                    # create a indivudal label for each 
                    if i==0 and j==0:# existing galaxies to draw on  # on left side all the way down
                        quad.frame1 = tk.Frame(master=window,  borderwidth=1)#relief=tk.RAISED
                        # keep blank but jsut reuse same function to save on changes
                        current_galaxies_connected_list=quad.import_tools_problems_or_existing_ideas(111)
                        quad.side_lists("Current Connected Objects",current_galaxies_connected_list,quad.frame1,i,j)
                        continue
                    if i==0 and j==1:
                        quad.frame8 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        quad.main_problem_window(i,j)
                        continue
                    if i==0 and j ==2: # questions I need to ask to form connections
                        quad.frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        questions_list=quad.import_tools_problems_or_existing_ideas(4)
                        quad.side_lists("Questions",questions_list,quad.frame2,i,j)
                        continue
                    if i==1 and j==0:# existing galaxies to draw on  # on left side all the way down
                        quad.frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        existing_objects_in_database_list=quad.import_tools_problems_or_existing_ideas(7,table_name="galaxies_table",galaxies_table=True)
                        # need to upload different data here from object database
                        # so need special upload function instead of import_tools_or_problems
                        quad.side_lists("Possible Objects",existing_objects_in_database_list,quad.frame3,i,j,galaxies_table=True)
                        # will have to set function values somehow
                        continue
                    if i ==1 and j==1:
                        quad.frame6 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        quad.qualitites_boxes("Object and Qualities of Selected Object","Strategy display =,`coding engineer /,law all,investment all",i,j,level=0)
                        continue
                    if i==1 and j ==2:
                        quad.frame7 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        quad.sub_method_box_1(quad.frame7,i,j)   
                    if i ==2 and j==0:
                        quad.frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        tools_list=quad.import_tools_problems_or_existing_ideas(10)
                        quad.side_lists("Tools",tools_list,quad.frame4,i,j)
                        continue
                    if i ==2 and j==1:
                        quad.frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        quad.qualitites_boxes("Edit-or-Create-Sentences","Develop-Sub-Method",i,j,level=1 )
                        continue
                    if i==2 and j==2:
                        quad.frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                        objectives_list=quad.import_tools_problems_or_existing_ideas(14) # need to make this work
                        quad.side_lists("Web-Results",objectives_list,quad.frame5,i,j)
                        continue
                    #if i == 2 and j ==2:
                        # replacing this method now
                    #frame.grid(row=i, column=j, padx=5, pady=5)
                    #label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                    #label.pack(padx=5, pady=5)
            
            #window.mainloop()# this is just temporary here to load psp
            
            #### START OF LISTENER RELATED CONTENT
            
            
            print('START WORKING ON THE WEBSITE TOMORROW make it viewable on psp website the data being uploaded on remote server')
            print(r' this is listener file to run on website which talks to big black C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer\pyautogui_website_computer_creation_listener_exe.py')
            print('big black then executes everything and sends things back to website')
            print('remember the pyauotgui generation file 7 for big black is in a seperate dirctroy from the one running on laptop')
            # might be safer to do this locally
            # copy over the updated create_pyautogui_file_of_inputs_and_video file directly into big_black
            
            # create generate_pyauto_gui_files_remote_linux on big black
            print(' WE USE SEPERATE FOLDER HERE TO ISOLATE THE GENERATIVE pyautogui code to protect ip')
            username="jross77"
            host="192.168.2.43"
            create_pyautogui_file_of_inputs_and_video_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\generate_pyauto_gui_files_remote_linux"
            scp_command_list = [f"scp","-r",f"{create_pyautogui_file_of_inputs_and_video_folder}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
            self.subprocess_run_script_remotely(scp_command_list)
            
            # create pyauto_gui_listener on website will use this in generate pyautogui files
            username="jross77"
            host="192.168.2.209"
            listneer_foleder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website"
            scp_command_list = [f"scp","-r",f"{listneer_foleder}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
            self.subprocess_run_script_remotely(scp_command_list)
            
            # restart and activate_all_apis_and_listeners
            print('REACTIVATE BELOW WHEN READY this has all the apis and listeners')
            #subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\activate_all_apis_and_listeners.py"])
            # execute listener on website which talks to big black DO THIS ON BIG WHITE NOW
            #doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/pyauto_gui_listener_website/pyauto_listener_bash.sh"]
            #self.subprocess_run_script_remotely(doc2ui)         
            #ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/pyauto_gui_listener_website/pyauto_listener_bash.sh"]# put the script you want to run here
            #self.subprocess_popen_script_remotely(ssh_command)
            window.mainloop()
            print(r"""key funcitons in  pyautogui listneer 
                  this is the listener copied over by laptop to website computer and then monitored on laptop while running on website computer
                  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website\pyautogui_website_computer_creation_listener3.py
                  # the listener executes on bigblack the  generate_pyautogui_files_on_other_computers_from_big_black function
                  which is inside
                  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\generate_pyauto_gui_files_remote_linux\pyautogui_for_generative_model_access_functions_remote_linux_3.py                
                  #the script in the above folder are  copied  by laptop to big black and runs on big black
                  
                  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\generate_pyauto_gui_files_remote_linux\pyautogui_for_generative_model_access_functions_remote_linux_3.py
                  # the script above run on big black creates and copies pyautogui generation files into other local computers on network 
                  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\generate_pyauto_gui_files_remote_linux\pyautogui_script_functions_remote.py  
                  the script above is added to scripts created on big black which are added on other computers to generate pyautogui files  and executed on other computers on the local network
                  
                  the  script below runs the inttial test function to execute script on big black to create and execute pyautogui generaiton files on other computers on local network
                  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\business_process_management_functions\business_process_management_functions179.py
                  test_generate_pyautogui_files_on_other_computers_from_big_black""")

            #input("execute script")
            
            # need to copy over create_pyautogui_file_of_inputs_ to big black
            #then need to copy over the bash to website to edit
            # how do i best do this
            #scp_command_list = [f"scp",f"{bash_script_path}",  f"{username}@{host}:/home/jross77/Documents/bash"]# put the script you want to run here 
            #self.subprocess_run_script_remotely(scp_command_list)



            # execute this seperately
            #subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\pyautogui_table_listner_to_convert_into_coding_problem_solving_info0.py"])
            #pyautogui_table_listner_to_convert_into_coding_problem_solving_info
            # automatically start up api on big white if possible
            #subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Inputs\pyautogui\init_pyauto_gui_creation_script_program_temp.py"])
            #subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\pyautogui_website_computer_creation_listener.py"])
            



            
            #add database coding listener to convert any incoming data into code from the various searches and what not 
            #subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\pyautogui_table_listner_to_convert_into_coding_problem_solving_info0.py"])
            # get this listneder working ocne i have the otherf parts done in pyautogui 5

            
            
            # add listneder that check for  updates to database
            # add other listenders to check for updates to other things and perform operations so we 
            #will reuse this code
            # how to set this up
            # create listneder for database in business functions
            # have it check for updates
            # store the last time listner was updated
            
            #every 30 seconds?
            # and upload the data into the coding program
            #use listneder for seeing updates to goverment websites


            


            #from multiprocessing import Process
            #sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
            #from record_screen_for_additonal_problem_data_and_send_to_sql import record_screen_for_additonal_problem_data_and_send_to_sql_l
            #record_screennn=record_screen_for_additonal_problem_data_and_send_to_sql_l()

            #process = Process(target=record_screennn.record_screen_for_additonal_problem_data_and_send_to_sql_function,args=("",)) 
            #process.start()
            

            
            
problem_solving_program()

