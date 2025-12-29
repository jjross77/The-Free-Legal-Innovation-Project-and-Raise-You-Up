# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:48:29 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

class search_functions():
    ''' '''
    def __init__(self):
     ''' '''
     self.sql_switch=0
     self.spacy_switch=0
     import psycopg2
     self.conn = psycopg2.connect(dbname='psp_search', user='postgres', password='MeganisGreat')
     self.cur = self.conn.cursor()
    
    def psp_window(request):
        base_view="hi"
class search_functions_child():
    ''' '''
    def __init__(self):
     ''' '''
     self.sql_switch=0
     self.spacy_switch=0
     import psycopg2
     self.conn = psycopg2.connect(dbname='psp_search', user='postgres', password='MeganisGreat')
     self.cur = self.conn.cursor()
     
     
     #PART 2: sort
     #PART 3: upload        
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
                   #print(e)
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
                #print(average_match_for_line_of_code)
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
     
     
    def code_base_function_search_sort_and_upload(self,event):
         """combine above functions search for the lines of code that you want to display at the top of the search """
         #PART 1: Search
         line_of_code_value_dic={}
         final_line_of_code_match_list=[]
         line_of_code_list=self.search_data_dic["line_of_code"]
         glossary_definiton_list=self.search_data_dic["glossary_definiton"]
         code_base_function_list=self.search_data_dic["code_base_function"]
         code_base_file_name_list=self.search_data_dic["code_file_name"]
         #print(line_of_code_list)
         prompt=self.entry_1.get()
         self.prompt_characters=self.create_characters(prompt)
         for line_of_code_placement_in_list, line_of_code in enumerate(code_base_function_list):
             #print(f"line_of_code:{line_of_code}")
             self.used_prompt_letters=[]
             final_line_of_code_match_list=[]
             line_of_code_characters=self.create_characters(line_of_code)
             for prompt_letter_list_value, prompt_letter in enumerate(self.prompt_characters):
                 prompt_single_letter_match_list=[]
                 prompt_single_letter_match_list=self.prompt_letter_comparison_to_line_of_code_character(prompt_letter,prompt_letter_list_value,line_of_code_characters)
                 if prompt_single_letter_match_list=="used_letter":
                     continue
                 if prompt_single_letter_match_list:
                     final_line_of_code_match_list=self.weigh_character_match_list(prompt_single_letter_match_list,final_line_of_code_match_list)
             if final_line_of_code_match_list:
                 average_match_for_line_of_code=self.create_average_match_line(final_line_of_code_match_list)
                 line_of_code_value_dic[line_of_code]=[average_match_for_line_of_code,line_of_code_placement_in_list] 
            
              #PART 2: sort 

         sorted_line_code_match_list=self.line_of_code_sort(line_of_code_value_dic)
         #PART 3: upload
         
         self.add_data_to_listbox(self.listboxxy1,sorted_line_code_match_list,code_base_function_list)
         self.add_data_to_listbox(self.listboxxy2,  sorted_line_code_match_list,line_of_code_list)
         self.add_data_to_listbox(self.listboxxy3,sorted_line_code_match_list,glossary_definiton_list)
         self.add_data_to_listbox(self.listboxxy4,sorted_line_code_match_list,code_base_file_name_list)
         
    def create_words(self,words_string):
           """ creates a list of words splitng on spaces"""
           import re
           words_string= re.sub(r"\s\s+",r" ", words_string )
           words_string=words_string.lower()
           words_list=words_string.split(" ")
           return words_list

    def glossary_search(self,glossary_definiton_list_list,prompt_word_list):
        """search throught he combined paragraphs to find amount of matching words to words to prompt """
        import re
        glossary_definition_values_dic={}
        glossary_definiton_list_list=self.search_data_dic["glossary_definiton"]
        for glossary_placement_in_list, combined_glossary_definition in enumerate(glossary_definiton_list_list):
            total_matched_words=0
            combined_glossary_definition=combined_glossary_definition.lower()
            for  prompt_word in prompt_word_list:
                prompt_word_found_in_glossary_list=re.findall(rf'{prompt_word}', combined_glossary_definition)
                number_of_matched_words=len(prompt_word_found_in_glossary_list)
                total_matched_words+=number_of_matched_words
            glossary_definition_values_dic[combined_glossary_definition]=[total_matched_words,glossary_placement_in_list] 
        return glossary_definition_values_dic
    
    
    def glossary_sort(self,glossary_definition_values_dic):
        """ sort the results from the glossary search correspeonding to highest words found"""
        sorted_glossary_match_list=[]
        glossary_definition_values_dic_len=len(glossary_definition_values_dic)-1
        for i11, (line_of_code, average_match_for_line_of_code_line_of_code_placement) in enumerate(glossary_definition_values_dic.items()):
            average_match_for_line_of_code=average_match_for_line_of_code_line_of_code_placement[0]
            line_of_code_placement=average_match_for_line_of_code_line_of_code_placement[1]
            if i11==0:
                #print(average_match_for_line_of_code)
                sorted_glossary_match_list.append([average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                continue
            for i,sorted_match_values in enumerate(sorted_glossary_match_list):
                sorted_match_num=sorted_match_values[0]
                if average_match_for_line_of_code>=sorted_match_num:
                    sorted_glossary_match_list.insert(i,[average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                    break
                if i==glossary_definition_values_dic_len :
                    sorted_glossary_match_list.append([average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                    break
        return sorted_glossary_match_list


    def glossary_search_sort_and_upload(self,event):
        """search by glossary values will write a different search for this """
        line_of_code_list=self.search_data_dic["line_of_code"]
        glossary_definiton_list_list=self.search_data_dic["glossary_definiton"]
        code_base_function_list=self.search_data_dic["code_base_function"]
        code_base_file_name_list=self.search_data_dic["code_file_name"]
        prompt=self.entry_1.get()
        self.prompt_word_list=self.create_words(prompt)
        # check word list against each combined glossary defintion
        glossary_definition_values_dic=self.glossary_search(glossary_definiton_list_list,self.prompt_word_list)
        #PART 2: sort
        sorted_glossary_match_list=self.glossary_sort(glossary_definition_values_dic)
        #PART 3: upload        
        self.add_data_to_listbox(self.listboxxy1,sorted_glossary_match_list,code_base_function_list)
        self.add_data_to_listbox(self.listboxxy2,sorted_glossary_match_list,line_of_code_list )
        self.add_data_to_listbox(self.listboxxy3,sorted_glossary_match_list,glossary_definiton_list_list)
        self.add_data_to_listbox(self.listboxxy4,sorted_glossary_match_list,code_base_file_name_list)
    def upload_sql_strategy_data(self):
         """ """
         import psycopg2
         self.conn = psycopg2.connect(dbname="psp_search", user="postgres", password="Meganiscute")
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
           #print(actions)
            if problem_being_solved in self.life_problem_tree_dag:
                self.life_problem_tree_dag[problem_being_solved].append(actions) 
            else:                # create new key
                self.life_problem_tree_dag[problem_being_solved]=[actions]       
        return self.life_problem_tree_dag 
    def upload_problem_tree_data_to_listbox(self):
        """ """
        import tk
       #print(self.life_problem_tree_dag )
        for problemmmm,strategies_list_list in self.life_problem_tree_dag.items() :
            self.listboxxy1_methods.insert(tk.END, problemmmm) 
            #for strategy in strategies_list_list:
            #   #print(strategy)
            #    self.listboxxy1_methods.insert(tk.END, problemmmm) 

                #
                #self.listboxxy3_methods.insert(tk.END, problemmmm) 
    def upload_sql_method_data(self):
         """ """
         import psycopg2
         main_method_window=quadrants_method_window()
         self.conn = psycopg2.connect(dbname="psp_search", user="postgres", password="MeganisGreat")
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
        #self.text_box.insert(tk.END, method_list_str) 
    # GENERIC PSP FUNCTIONS START
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
    def create_strategy_dict_or_modify(self,content): 
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
            self.action_only_list=[]
            self.previous_strategy_list=copy.deepcopy(self.strategy_list)
            self.strategy_list=[time_method_found,[],[],[],[],[]] # problem # 1 is there because it is the second entry in this steps list of lists
            action_list=re.split(r"([/=\]])",content)# will need to test this
            

            stored_delimiter=""
           #print(action_list)
            for qual3 in action_list:
                qual3=re.sub("\n","",qual3)
                if  qual3 in "/]":
                    stored_delimiter=qual3
                    continue
                else:
                    if stored_delimiter=="]": # this a strategy
                        id_str=self.generate_random_id()# will need to test this
                        self.action_only_list.append(qual3)
                        qual3=f"?? how do i {str(qual3)}?"
                        qual3=qual3+id_str
                        self.strategy_list[1].append(qual3)

                       #print('action')

                    if stored_delimiter=="/":
                        self.strategy_list[2].append(qual3)
                       #print('objective or effect')
                    if stored_delimiter=="":
                        id_str=self.generate_random_id()# will need to test this
                        self.action_only_list.append(qual3)
                        qual3=f"?? how do i {str(qual3)}?"
                        qual3=qual3+id_str
                        self.strategy_list[1].append(qual3)
                       #print('action')
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
            return self.strategy_list,self.action_only_list
     
        
        
    def save_strategy_dictionary_to_database(self,strategy_list):
            """ take the method list dictitonary and bring it to database for methods disassembling it and uploading it""" 
            import re
            from multiprocessing import Process
            import sys
            sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')

            if self.cancel==True:
               #print('hi')
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
            # convert these to models
            # so adds to database models instead of sql directly
            #p = Person(name="Fred Flintstone", shirt_size="L")
            #>>> p.save()
            #fruit = Fruit.objects.create(name="Apple")
            #>>> fruit.name = "Pear"
            #>>> fruit.save()
            

            
            if  len(self.previous_strategy_list)>=1: #need
               print("PREVIOUS STRAtragy list")
                #strategy_action is the label
                #.cur.execute( f""" UPDATE strategy_table 
                #                 Set question_or_tool_for_strategy= '{str(tool_or_question_list)}', problem_web_variables = '{str(idea_web_list)}',
                #                 effects = '{str(objective_list)}', time_found = '{str(time_found_list)}',actions ='{str(action_related_to_strategy)}', 
                #                 WHERE problem_being_solved = '{str(self.problem_recorded)}' ;""")
            else:
                strategyy=strategy_table(problem_being_solved=f'{str(self.problem_recorded)}',question_or_tool_for_strategy=f'{str(tool_or_question_list)}',problem_web_variables=f'{str(idea_web_list)}',effects=f'{str(objective_list)}',time_found=f'{str(time_found_list)}',actions=f'{str(action_related_to_strategy)}')
                strategyy.save()
                
                #self.cur.execute( f""" INSERT INTO strategy_table (problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions)
                #         VALUES ('{str(self.problem_recorded)}','{str(tool_or_question_list)}','{str(idea_web_list)}','{str(objective_list)}','{str(time_found_list)}','{str(action_related_to_strategy)}');""")
            
            
            
            for action in self.strategy_list[1]:# need to test this
                action=re.sub('\'',"",str(action))
                action=re.sub('\"',"",action)
                action=re.sub('\n',"",action)# check this
                # multiprocess this shit
                auto_problemm=auto_problem_table(problem_question_or_task=f'{str(action)}',specific_problem_or_object=f'{str(action)}',tool_or_question_per_conn_list=f'{str([])}',qualitity_list=f'{str([])}',time_created_conn=f'{str(time_found_list_list)}',initial_creation=f'{str(time_found_list)}')
                auto_problemm.save()

                #self.cur.execute( f""" INSERT INTO auto_problem_table (problem_question_or_task,specific_problem_or_object,tool_or_question_per_conn_list,qualitity_list,time_created_conn,initial_creation)
                #         VALUES ('{str(action)}','{str(action)}','{str([])}','{str([])}','{str(time_found_list_list)}','{str(time_found_list)}');""")
               #print('TEST')
                #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
                # going to affect them when they age
                #from Problems_functions import problems_functions
                #from Problems_functions import methods_window_program
                from create_auto_create_problem_tree_and_web import create_auto_create_problem_tree_and_web
                #from problem_solving_project_gui_10 import buttons_per_quadrant
                #buttons=buttons_per_quadrant()
                auto_prob_web_tree=create_auto_create_problem_tree_and_web()
                # going to tempoary disable this
                process = Process(target=auto_prob_web_tree.auto_create_problem_web_and_galaxy,args=(action,))
                #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))              
                process.start()
            self.conn.commit() 
            # clear strategy list so dont write multiple same strategy twice
            self.strategy_list=[]         
        
    def reupload_strategy_dictionary(self):
            """ take the method list dictitonary and bring it back into the program  from sql database"""
            strategy_table_actions_list=strategy_table.objects.values_list('actions') # value_list produces it as a list
            return strategy_table_actions_list

            #self.cur.execute(f""" SELECT problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions From strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
            # need to upload these to listbox in django
            #self.listbox2.delete(0, tk.END)
            #strategy_entries= self.cur.fetchall()
            # still need to remove  question marks
            # need to delete all previous entries
            #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
            #for objecttt in strategy_entries:
            #    #id 0 #problem 1 # step name 2 #tool 3 #ideas 4 # optimize 5 # order 6 #time 7
            #    problem_being_solved=objecttt[0]
            ##    question_or_tool_for_strategy=objecttt[1]
            #    problem_web_variables=objecttt[2]
             #   effects=objecttt[3]
              #  time_found=objecttt[4]
               # actions=objecttt[5]     
                #self.listbox2.insert(tk.END, f"{actions}")
    ### CODING PROGRAM START 
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
     import re
     return
     out_prompt_list=[]
     for action in self.strategy_list[1]:# need to test this
             action=re.sub('\'',"",str(action))
             action=re.sub('\"',"",action)
             action=re.sub('\n',"",action)# check this
             #edit action to get rigth prompt
             prompt=action+stuff
     return out_prompt_list
    def query_single_computer_running_llamma_api(self,host):
        """ need to test this to see if host is found"""
        url = f"http://{host}:8000/items/"
        params = {
          "prompt": f"{prompt}",
          "price": 999.99}
      # Send GET request to FastAPI server with query parameters
        response = requests.get(url, params=params)
        # Send POST request to FastAPI server
       #print(response.json())
        # Check if the request was successful
        if response.status_code == 200:
            # Parse and print the response JSON
            response_data = response.json()
            response_str=response_data['name']['content']
            # process data here
           #print("Response from FastAPI:")
           #print(response_str)         
        else:
           print(f"Failed to get response, status code: {response.status_code}")   
        return response_str
        
    
 
 
 
    def query_a_computer_to_process_prompt(self,prompt):
     ''' # set up api for big black copy everything done on big white
     # need to ssh into both to get this to work
     # set up pyautogui for corsair and and acer using business funcitons guides
     #setup_computer_to_run_pyautogui
     # use both below functions in buisness to set these up
     @setup_computer_to_run_fast_api
     #setup_website_and_api_to_run_llamma  
     # setup ssh certifiate as well
     #update_computer_to_run_ssh_certificate_with_other_computer
     # acer 192.168.2.233
     #corsair : 192.168.2.213
     #hp : 28
     # USE THESE COMMANDS TO START API need to make this automatic
     #BIGBLACK
     #ssh jross77@192.168.2.200
     #cd /home/jross77/Documents/psp_api2
     #source env/bin/activate
     #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     #http://192.168.2.200:8000/ # big black
     #http://192.168.2.200:8000/items/     
     #BIG WHITE
     #ssh desktop-s7na8dm\doggo777@192.168.2.214
     #>ssh desktop-s7na8dm\doggo777@192.168.2.214
     #cd Documents\psp_api
     #.\venv\Scripts\activate
     #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     #http://192.168.2.214:8000/items/# big white 
     # run pyautogui on all computers
     # use update_computer_to_run_ssh_certificate_with_other_computer to fix key errors
     # add two more tomorrow
     # acer 192.168.2.233
     #corsair : 192.168.2.213
     #hp : 28
     #BIGBLACK
     #ssh jross77@192.168.2.200
     #BIG WHITE
     #ssh desktop-s7na8dm\doggo777@192.168.2.214
     coding assistant tips
     big problem break dow smaller problem n use debugging
     for more challenging things come up wth test case know if it wokrd if it passes these tests
     this is  test case keep iteratign till solve test case
     keep iterating till solve test case
     '''    
     import requests
     import subprocess
     # specify host computer as first arg
     # do every computer on network
     subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\law_society_practice_script0.py", "192.168.2.207"])# hp laptop
     subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\law_society_practice_script0.py", "192.168.2.233"]) #acer
     subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\law_society_practice_script0.py", "192.168.2.213"])#corsair
     subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\law_society_practice_script0.py", "192.168.2.28"])#hp server
     subprocess.Popen(["python", r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\law_society_practice_script0.py", "192.168.2.200"])# big black

     # redo everything on big black if necessary if and need more pyautogui for now leave it
     #for now focus on getting open hands set up
     # run as many instances as you can
     big_black_host="192.168.2.200"
     big_white_host="192.168.2.214"
     # will want to subprocess this
     response_str_black=self.query_single_computer_running_llamma_api(big_black_host)
     response_str_white=self.query_single_computer_running_llamma_api(big_white_host)
     return response_str_white
 #import sys
 #from multiprocessing import Process
 #sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\business_process_management_functions')
 #from business_process_management_functions98 import business_process_management_functions
 #business0=business_process_management_functions()
 #from business_process_management_functions98 import business_process_management_functions_child
 #business1=business_process_management_functions_child()
 #from business_process_management_functions98 import business_process_management_functions_gchild
 #business2=business_process_management_functions_gchild()
 #from business_process_management_functions98 import business_process_management_functions_g2child 
 #business3=business_process_management_functions_g2child()
 #process = Process(target=business2.law_society_practice_script)
 #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,)) 
 
     # big black 192.168.2.200
     #process.start()
     #business2.law_society_practice_script()
     # executer as sepeate script
     # execute as multiprocess
     # execute it as a seperate script? instead of mutlirpcoess
     # benefits multiprocess
      
 
         
    def llama_generate_coding_environment(self,strategy_list):
        """generate_coding_environment
        going to skip this till i can get gpu to run faster
        """
        import re
        coding_environment_dic={}
        self.upload_prompts("")
        prompt_list=["what does {ACTION} mean in the context of coding in python","when is {ACTION} important in coding",]
        #prompt_list=self.create_prompts(strategy_list,prompt_list)
        self.create_prompts(strategy_list,prompt_list)
        for actionn in strategy_list:
           #print(f"actionn {actionn}")
            for promptt in prompt_list:
                final_query=re.sub(r"ACTION",actionn,promptt)
                response_str =self.query_a_computer_to_process_prompt(final_query) 
                # parse this and create prompt
                self.automated_coding_psp_info_dic["intital_env_prompts_list"].append(final_query)
                self.automated_coding_psp_info_dic["intital_action_list"].append(actionn)
                self.automated_coding_psp_info_dic["intital_env_response_str_list"].append(response_str)

                
                coding_environment_dic[final_query]={"actionn":actionn,"response_str":response_str,}
                # this is temp
                return coding_environment_dic

        return coding_environment_dic

    def llama_generate_coding_strats(self,coding_environment_dic):
        """ generate_coding_environment"""
        import re
        prompt_action_list_dic={}
        self.upload_prompts("")
        # repeat this for each step to create tree
        prompt_templates_coding_strat_list=["what are the steps i would take to ACTION"]
        prompt_list=self.create_prompts("", "")
        for final_query_key in coding_environment_dic.keys():
            actionn=coding_environment_dic[final_query_key]["actionn"]
            for prompt_template in prompt_templates_coding_strat_list:
                action_list_prompt=re.sub(r"ACTION",actionn,prompt_template)
                response_str=self.query_a_computer_to_process_prompt(action_list_prompt)
                # break up actions in strategy
                action_list=re.split(r"[\.\?0-9]",response_str)# find best delimter here
                if action_list_prompt in prompt_action_list_dic:
                    prompt_action_list_dic[action_list_prompt].append(action_list) 
                else:
                    prompt_action_list_dic[action_list_prompt]=[action_list]
                self.automated_coding_psp_info_dic["intital_action_list_prompt_list"].append(action_list_prompt)
                self.automated_coding_psp_info_dic["intital_generated_action_list_list"].append(action_list)
                # this is temp
                return prompt_action_list_dic

            

                #print('HIII MY NAME IS CHRIS')
                #print(action_list)
                #input()
            
        return prompt_action_list_dic
       
        
       
    def llama_generate_coding_script(self,prompt_action_list_dic):
        """generate_coding_environment """
        import re
        # write each response to a single coding file
        action_function_data_dic={}
        #self.upload_prompts("")
        prompt_templates_function_creation_list=["write a python function to ACTION"]
        prompt_list=self.create_prompts("", "")
       #print(prompt_action_list_dic)
        #input()
        for intital_typed_action, generated_strategy_list_list in prompt_action_list_dic.items():
            for single_strategy_list in generated_strategy_list_list:
                for action in single_strategy_list:
                    for prompt_function_template in prompt_templates_function_creation_list:
                        input_prompt=re.sub(r"ACTION",action,prompt_function_template)
                        function =self.query_a_computer_to_process_prompt(input_prompt)
                        if input_prompt in prompt_action_list_dic:
                            action_function_data_dic[action].append(function) 
                        else:
                            action_function_data_dic[action]=[function]
                        #action_function_data_dic[action].append(function)
                        self.automated_coding_psp_info_dic["intital_funciton_prompt_list"].append(input_prompt)
                        self.automated_coding_psp_info_dic["intital_generated_function_list"].append(function) 
                        # this is temp
                        return action_function_data_dic
                        
        return action_function_data_dic
    def create_auto_code_file_str(self,action_function_data_dic,problem_name):
        """ """
        # rermove all text thats not function
        import re
        
        coding_file_str=rf"""# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy
class {problem_name}():
 def __init__(self):
    #print('start_pyautogui_class')""" 
        for action,function_list in action_function_data_dic.items():
            for function in function_list:
                # this is to parse the str from the ai model
                # transforming it so the code is runnable
                #write file str
                # to simply find code in a str
                # and put it in the right format
                #use model?
                # use funciton we wrote to sort code syntax using : and other symbols
                # use a compiler
                # model to sort code and non code put # if is not code or use regex
                # read error and if error add # to the code line
                # so need to fix all errors
                # have model working with
                #
                funciton_found=re.search(r"def(.|\n)*",function)
                if funciton_found:
                    #print(funciton_found)
                    funciton_end_found=re.search(r"(.|\n)*return.*",funciton_found.group(0))
                    if funciton_end_found:
                        function_str=funciton_end_found.group(0)
                       #print(funciton_end_found.group(0))
                        coding_file_str+=f"\n {function_str}"
                        
                    
                    
                #funciton_found=re.search(r"def.*return",function)
                #if result:
                #    funciton_found=funciton_found.group(0)
                #    coding_file_str+=f"\n {funciton_found}"
                    
                
                
           
        return coding_file_str
    def create_auto_code_file_str_test(self,action_function_data_dic,problem_name):
        """ """
        coding_file_str=rf"""# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy
class {problem_name}():
 def __init__(self):
    #print('start_pyautogui_class')""" 
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
               #print(' FAILED TO  FIND CODING  FILE')
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
               #print(f"class_line: {line}")
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
                   #print('NOT REAL FUNCTION')
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
        input_function_name_input_file_name_dic={}
        root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\psp_website\psp\auto_created_code"
        auto_code_file_dir_list=os.listdir(root_folder)
        # get the name of the folder to hold the file
        # if there is a problem use that
        # otherwise use 
        problem_name=self.problem_recorded
        if self.problem_recorded=="":
           #print(action_function_data_dic)           
            for action in action_function_data_dic.keys():
                problem_name=action
                break 
           #print(problem_name)
            #print('hiiii')
            self.problem_recorded=problem_name
            #input()

        #    
        #else: 
            # use the first action if starting from scratch
        #    problem_name=first_action
        problem_name=re.sub(r"[^a-zA-Z0-9 ]", "", problem_name)# check this
        problem_name=re.sub(r"[ -]","_",problem_name)  
        problem_name=str(problem_name[:20])
       #print(f"problem_NAMEE: {problem_name}")
        self.dir_to_store_script=root_folder+"\\"+problem_name  
        self.dir_to_store_script_linux=r"/home/jross77/Documents/Coding/auto_created_code/"+problem_name
        self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
        self.dir_to_store_script_linux=re.sub(r"[ -]","_",self.dir_to_store_script_linux)
        problem_inputs_folder=self.dir_to_store_script+r"\\inputs"
        Problem_building_folder=self.dir_to_store_script+r"\\building"
        if problem_name not in auto_code_file_dir_list:
            os.mkdir(self.dir_to_store_script)
            # create sub buidling and input folders
            os.mkdir(problem_inputs_folder)
            os.mkdir(Problem_building_folder)  
            #input()

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
        import subprocess
        input_function_name_input_file_name_dic_with_errors=copy.deepcopy(input_function_name_input_file_name_dic)
        for function_name, function_input_file_name in input_function_name_input_file_name_dic.items():
            run_script_input = [f"python",f"{function_input_file_name}"]
            # need to locate function code here
            # and use it to 
            function_code=""
            try:
                result=subprocess.run(run_script_input, check=True,shell=True,capture_output=True, text=True)
                stdout = result.stdout
                stderr = result.stderr
               #print("Standard Output:", stdout)# standard ouytput
               #print("Standard Error:", stderr) # error message
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
        # need to 
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
                    fixed_function =self.query_a_computer_to_process_prompt(input_prompt)
                    self.automated_coding_psp_info_dic["testing_fixed_funciton_code_list"].append(fixed_function)
                    self.automated_coding_psp_info_dic["testing_input_prompt_list"].append(input_prompt) 
                    function_name_fixed_funciton_content_dic[function_name]={"fixed_function_code":fixed_function,
                                                                   "og_function_code":function_code,
                                                                   "function_name":function_name,
                                                                   "input_prompt":input_prompt,
                                                                   "error":error}    
        # add these to the existing file project and create a new coding file str
        return action_fixed_error_function_dic
    
    ##### AUTO psp functions
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
                 response_str =self.query_a_computer_to_process_prompt(prompt_env)
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
                   response_data =self.query_a_computer_to_process_prompt(final_prompt_g)
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
                    strat_str =self.query_a_computer_to_process_prompt(prompt_strat)
                    response_data_dic[prompt_strat]=strat_str
                    self.automated_psp_info_dic["prompt_strat_list"].append(prompt_strat)
                    self.automated_psp_info_dic["strat_response_str_list"].append(strat_str)

        return psp_prompt_strat_data_dic 
    ### FINANCE MODEL FUNCTIONS
    def gather_list_of_all_possible_actions_you_could_invest_time_or_money_in(self):
        """ """
    def assess_time_and_risk_only_reaosn_finance_industry_exists(self):
        """ """
    def measure_return_on_invesmtent_model(self):
        """ """
    def accounting_program_profit_revenues_loss(self):
        """ """
    def create_model_to_suggest_based_on_someone_current_assets_and_other_indicators_outputs_actions_could_take_to_invest(self):
        """ """
    def create_map_of_all_alternative_physical_locations_and_alternative_websites_categorize_websites_compare_alternatives(self):
        """ """
    def look_at_all_alternative_investment_for_certain_action_and_effects_using_map(self):
        """ """
        
    
        
        
        
    
    
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
            
           #print("Connection successful!")
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
    
    # insert output into a new coding file
    

        

    
        
    
class search_functions_gchild(search_functions_child):
    ''' '''
    def __init__(self):
     ''' '''
     self.sql_switch=0
     self.spacy_switch=0
     #import psycopg2
     #self.conn = psycopg2.connect(dbname='psp_search', user='postgres', password='MeganisGreat')
     #self.cur = self.conn.cursor()
     
    def use_mit_course_materials_to_build_expert_models_related_to_the_couse_subject_area_that_perform_special_expert_actions_like_invest_or_build_robotics_system_taught_in_the_course(self):
        """ """
        base_view="hi"
    
    
    def law_checker_to_make_sure_action_is_legal(self):
        """ """
    def generate_sub_problem_tree_within_intital_problem(self):
        """ generate all of the sub prbolem trees for the problem and the files associated with these
        or sub searches that would need to be carried out to solve the problem on google and questions to be asked"""
        
    def input_information_create_thought_create_action(self):
        """ deicison_making_understander
        figure_out_what_is_going_into_someone_decisions"""
        base_view="hi"
    def generate_music_from_audio_to_help_you_learn_and_study(self):
        """ """
    
    def copy_everything_successful_people_have_done_steal_all_ideas_incoprorate_them_into_this_more_is_key(self):
        """ build_auto_stealing_method_program_from_all_things_like_geist_website_or_other_company_websites_or_products_convert_idea_into_text_then_incorproate_into_psp"""
        base_view="hi" 
        
    def build_auto_repairing_pyautogui_program(self):
        """ deicison_making_understander"""
        base_view="hi"
    def autoamte_finding_tools_like_access_information_request_by_searching_websites_and_incorporate_in_psp(self):
        """ deicison_making_understander"""
        base_view="hi"
    def schedule_and_exe_pyautogui(self):
        """ this will replace pyautogui scehdule api on server and add it to psp api"""
    
     
 
    def search_ideas_table(self,problem,ideas_table_3_e):
        """
        updated label
        updated_sentence
        tools 10
        questions 4
        """
       #print(problem)
       #print(ideas_table_3_e)
        # specific sql queries might be more reuseable
        # better to make specific queries or to process it downsteeam?
        # store data in better way?
        # put in evidence post filing in europe
        # just do model search
        #change upstream search
        
        input()
        #return list for downsteam
        #search
        #download
        tools=[]
        questions=[]
        ideas_table_search_results = [{"table":"updatetable1",'problem': tool} for tool in tools]  
        questions_table_search_results = [{"table":"updatetable2",'problem': question} for question in questions]        
        ideas_table_search_results.extend(questions_table_search_results)

        return ideas_table_search_results

    def search_auto_strategy_table(self,problem,auto_strategy_table_e):
        """ """
        #search
        #download
        self.cur.execute(f"""SELECT problem_being_solved,question_or_tool_for_strategy,problem_web_variables,effects,time_found,actions FROM strategy_table ;""")
        self.process_strategy_data_convert_to_problem_tree_data(auto_strategy_table_e)
        self.upload_problem_tree_data_to_listbox()
        auto_strategy_search_results = [{"table":"updatetable3",'problem': question} for question in questions]        

        return  auto_strategy_search_results

    def search_strategy_table(self,problem,auto_strategy_table_e):
        """ copy auto stategy table stuff here"""
        strategy_search_results = [{"table":"updatetable4",'problem': question} for question in questions]        

        #search
        #download
        
        return strategy_search_results

    def search_auto_problem_table_e(self,problem,auto_problem_table_e):
        """ """
       #print(auto_problem_table_e)

        #search
        #download
        auto_problem_search_results = [{"table":"updatetable5",'problem': question} for question in questions]        

        
        return auto_problem_search_results

    def search_problem_table(self,problem,problem_list):
        """copy auto problem stuff here
        subsume 7 in ideas table into problem table if possible as higher order problems without info
        7 other problems"""
        #search
        #download
        problem_table_search_results = [{"table":"updatetable6",'problem': question} for question in questions]        

        
        return problem_table_search_results

    def search_methods_table(self,problem,methods_table_e):
        """ """
        #search
        #download
        self.reupload_method_dictionary()
        self.list_past_methods()
        methods_table_search_results = [{"table":"updatetable7",'problem': question} for question in questions]        

        
        return methods_table_search_results

    def search_problem_solving_screen_recording_table(self,problem,problem_solving_screen):
        """ """
        #search
        #download
        problem_solving_screen_recording_search_results = [{"table":"updatetable8",'problem': question} for question in questions]        

        
        return problem_solving_screen_recording_search_results

    
    def search_prompt_table(self,problem,prompt_table_e):
        """ """
        # upload values from sql
        #search
        #download
        prompt_table_search_results = [{"table":"updatetable9",'problem': question} for question in questions]        

        
        return prompt_table_search_results
    def fia_nn_law_model_search(self):
        """ """

    def search_code_base_table(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    
    def do_market_research(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def identify_business_revneue_streams(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_revenue_projections_based_on_market_research(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def find_problme_people_want_solved(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_patent_design(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_cad_model(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_code_to_build_object_using_arms(self,problem,code_base_table_e):
        """send_code_to_use_robotic_arms_and_3d_printer_to_produce_prototype """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def send_code_to_use_robotic_arms_and_3d_printer_to_produce_prototype(self,problem,code_base_table_e):
        """send_code_to_use_robotic_arms_and_3d_printer_to_produce_prototype """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    
    def generate_electirc_board_design(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def setup_possible_supply_chain_based_on_materials_in_design(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_manufacturing_equipment_required_to_build_find_best_route(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def find_cheapest_alternative_online_for_each_product(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def compare_alternative_patent_and_cad_product_generated_to_solve_problem_and_ensure_design_chosen_is_informed_by_finance_and_manufacturing_models_to_ensure_its_cheap_and_affordable_to_make_and_scale(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def setup_marketing_of_product(self,problem,code_base_table_e):
        """create info graphics on canva and generate cartoons for business and artwork """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def setup_ecommerce_website_crowd_funded(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def setup_business_website(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def create_delegation_program_plan(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    
        
        return code_base_search_results
    def generate_busienss_idea(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_busienss_plan(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_prospectus(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_balance_sheet_and_other_financial_documents(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def raising_money_crowd_funding(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def build_factory_purchase_manufacturing_equipment_with_money(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def find_buyers_and_sell(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def sell_product(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def model_to_automatically_do_science(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def gen_moleuclar_creator_and_finder(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_energy_generation_business_or_electronics(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def use_recycled_metal_transform_into_industrial_robotics_systems(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def plan_all_steps_ahead_to_best_build_engineer(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def build_negoiation_argument_model(self,problem,code_base_table_e):
        """ 
        when arguing forward a conclusion that will put you in the best possible position based on the effects
        it gives and then support this conclusion with evidence
        in the problem environment if you cant support the conclusion with evidence change to next best conclusion you can with evidence that will give you the next best effects-
        Figure out whats important for them and phrase your ask in a way that they will say yes you get what you want"""
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def scrape_all_possible_arguments(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def prompt_possible_arguments_model(self,problem,code_base_table_e):
        """
        when arguing forward a conclusion that will put you in the best possible position based on the effects
        it gives and then support this conclusion with evidence
        in the problem environment if you cant support the conclusion with evidence change to next best conclusion you can with evidence that will give you the next best effects
        Figure out whats important for them and phrase your ask in a way that they will say yes you get what you want"""
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def generate_script_for_negoiaitons_bargaining_ranges_most_perusaive_psychology(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def gather_list_of_all_possible_actions_you_could_invest_time_or_money_in(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def assess_time_and_risk_only_reaosn_finance_industry_exists(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]  
        
    def generate_related_problem_list_from_current_postion_and_problem_info(self,search,positional_info_dic,objective="help the most people"):
        """ """
        example=[{"problem_being_solved":search,
                                   "related_task":related_task,
                                   }]
        return sorted_related_dags_dic_list
        

        
        return code_base_search_results
    def measure_return_on_invesmtent_model(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def accounting_program_profit_revenues_loss(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def create_model_to_suggest_based_on_someone_current_assets_and_other_indicators_outputs_actions_could_take_to_invest(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def create_map_of_all_alternative_physical_locations_and_alternative_websites_categorize_websites_compare_alternatives(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def look_at_all_alternative_investment_for_certain_action_and_effects_using_map(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    
    def build_crypto_exchange_app(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    
    ###finance functions
    def top_possible_investments(self):
        """ """        
    def companies(self):
        """ """
    def risk_and_time(self):
        """ """
    def return_on_investment(self):
        """ """
    def profit_and_revenue(self):
        """ """
    def map_info(self):
        """ """
    def historical_data(self):
        """ """
    def propspectus(self):
        """ """
    def slide_deck(self):
        """ """
    def balance_sheet(self):
        """ """
    def manufacturing_equipment(self):
        """ """
    def tax_consequences(self):
        """ """
    def accounting(self):
        """ """
    def cash_flows_time_value_of_money(self):
        """ """
    def opprounity_cost(self):
        """ """
    def predict_future_asset_value_over_time(self):
        """ """
    def predict_future_ROI(self):
        """ """
    def how_to_store_money(self):# for future investing
        """ """
    def product_market_fit(self):
        """ """
    def alternative_investments(self):
        """ """
    
        
    ### journalist functions
    def news_article(self):
        """ """
    def story_title(self):
        """ """
    def story_content(self):
        """ """
    def lobbying(self):
        """ """
    def conference_name(self):
        """ """
    def negoiation_arguments(self):
        """ """
    def internships(self):
        """ """
    def factum(self):
        """ """
    def negoitaiton_script(self):
        """ """
    def memo(self):
        """ """
    def argument(self):
        """ """
    def courses(self):
        """ """
    def adminsistration_task(self):
        """ """
    def community_event(self):
        """ """
    def social_media_post(self):
        """ """
    def social_media_post_image(self):
        """ """
    def podcast_audio(self):
        """ """
    ### engineering functions
    def cad_image(self):
        """ """
    def history_and_stories(self):
        """ """
    def molecular_data(self):
        """ """
    def material_cost_info(self):
        """ """
    def alternative_material_cost_info(self):
        """ """
    def factory_equipment_info(self):
        """ """
    def revenue_streams_for_product(self):
        """ """
    def market_research(self):
        """ """
    def legal_considerations_betnween_alternatives(self):
        """ """
    def PCB_design(self):
        """ """
    def cheapest_alternative_prouducts(self):
        """ """
    def business_website_code(self):
        """ """
    def task_delegation_plan(self):
        """ """
    def robotic_arm_code(self):
        """ """
    def patent_text(self):
        """ """
    def patent_images(self):
        """ """
    def supply_chain_info(self):
        """ """
    def arguments_for_product(self):
        """ """
    def cost_of_product(self):
        """ """
    def laws_implicated(self):
        """ """
    def prospectus(self):
        """ """
    def possible_client_list(self):
        """ """
    def business_plan(self):
        """ """
    def factory_code_to_produce_product(self):
        """ """
    def product_revenue_projections_over_time(self):
        """ """
    def engineering_book_journal_content(self):
        """ """     
    def crowd_funding_site_text(self):
        """ """
    def crowd_funding_site_image(self):
        """ """
    def alternative_business_formats(self):
        """ """
    def factory_design_skmathics(self):
        """ """
    def negoiation_arguments(self):
        """ """
    def materials(self):
        """ """
    def point_5_CNC_milling(self):
        """ """
    def use_all_engineering_related_sas_apps(self):
        """ """
    ###LAWYER FUNCTIONS
    def factum(self):
        """ """
    def memo(self):
        """ """
    def will(self):
        """ """
    def cause_of_action(self):
        """ """
    def statement_of_defense(self):
        """ """
    def application(self):
        """ """
    def cross_claim(self):
        """ """
    def counter_claim(self):
        """ """
    def motion_for_particulars(self):
        """ """
    def motion_for_default_judgement(self):
        """ """
    def summary_judgement(self):
        """ """
    def motion_determine_issue_before_trail(self):
        """ """
    def third_party_claim(self):
        """ """
    def discovery(self):
        """ """
    def offers_to_settle(self):
        """ """
    def expert_report(self):
        """ """
    def witnesses(self):
        """ """
    def jury_selection_info(self):
        """ """      
    def trial_strategy(self):
        """ """
    def trial_transcript(self):
        """ """
    def appeals(self):
        """ """
    def real_estate_document(self):
        """ """      
    def lobbying(self):
        """ """
    def judicial_review(self):
        """ """
    def conference_name(self):
        """ """
    def organization_name(self):
        """ """
    def conference_info(self):
        """ """
        
    
    
    
    
    def build_search_find_all_free_and_useful_sas_and_projects_to_add_to_psp(self,problem,code_base_table_e):
        """https://github.com/OpenBB-finance/OpenBB?tab=readme-ov-file """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def build_model_to_perform_all_tasks_on_website(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def argument_generator_most_persusaive_based_on_position_to_get_different_outcomes(self):
        """
        when arguing forward a conclusion that will put you in the best possible position based on the effects
        it gives and then support this conclusion with evidence
        in the problem environment if you cant support the conclusion with evidence change to next best conclusion you can with evidence that will give you the next best effects
        Figure out whats important for them and phrase your ask in a way that they will say yes you get what you want"""
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
    def use_models_to_genrate_quesitons_and_all_objects_in_problem_so_efects_and_problems_themselves(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def categorized_websites_then_perform_paritcluar_operations_on_them(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def build_program_to_find_all_best_ideas_from_people_and_things_to_incorproate_into_program(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def build_program_to_incorporate_ideas_into_program(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def build_auto_stealing_idea_program_from_all_things_like_geist_website_or_other_company_websites_or_products_convert_idea_into_text_then_incorproate_into_psp(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def law_checker_to_make_sure_action_is_legal(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def figure_out_what_is_going_into_someone_decisions(self,problem,code_base_table_e):
        """
        # what input inofrmation produces certain thoughts which produce certain acitons by people
        # only do this if its legal get people to do what you want what goes into a deicsion, what to say or do to get people to make a deicsion you want like deciding to give you money# generate actions that let you do this
        #search"""
        # what input inofrmation produces certain thoughts which produce certain acitons by people
        # only do this if its legal get people to do what you want what goes into a deicsion, what to say or do to get people to make a deicsion you want like deciding to give you money# generate actions that let you do this
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def auto_create_all_elements_of_problem_solving_program_self_improving(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def autoamte_finding_tools_like_access_information_request_by_searching_websites_and_incorporate_in_psp(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def use_mit_course_materials_to_build_expert_models_related_to_the_couse_subject_area_that_perform_special_expert_actions_like_invest_or_build_robotics_system_taught_in_the_course(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def risk_calculation(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def find_all_possible_data_could_train_dif_modles_with(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def open_bank(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions]        

        
        return code_base_search_results
    def invention_business_idea_generator(self,problem,code_base_table_e):
        """ """
        #search
        #download
    def invention_business_management_idea_generator(self,problem,code_base_table_e):
        """ generate ideas like peel back onion method
        or ask what feauture or qualtity makes this business great or make me feel good and then reverse engineer this thing and add it to your business
        idea is a set of words  likely a method so build method generator
        and idea has certain effects so find ideas with similar effects to the ones above
        
        need to reverse engineer methods like getting ideas like the below in research functions
        like use all books big powerful ideas how to build something to generate these
        like extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate
        or
        combine_all_concepts_tools_and_info_from_other_field_into_current_field
        or 
        automatically_find_and_add_new_qulaitites_to_finance_profession_info_dic
        """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions] 
    def build_newspaper(self,problem,code_base_table_e):
        """ """
        #search
        #download
        code_base_search_results = [{"table":"updatetable10",'problem': question} for question in questions] 

        
        return code_base_search_results
    def create_the_market_for_the_product(self):
        """ """
    def generate_person_indivdual_life_dag_history_of_tasks_completed_and_effects_on_others(request):
     #print('publish news articles comics aqnd use every median of communication to show person tasks and the effects of their tasks on the world and others throughout their life ')
     #print('generate strategies people could use to stop people from doing harm and discourage hurting people like law suit or mitigate negastive effects of tasks person completes ')
     #print('only publish about rich people and people above a certain net worth like 200k a year so people could change their behaviour and make them use their money for good')
     #print('this is to prevent lying or omissions or distortions and focuses on what people do rather than who they are and therefore can stop bad tasks and encourage good tasks and not be discriminatory')
     print("""prevent evil and people lying or distorting reality by people like nethanyu or israel by 
            creating a indivduals life dag track the tasks they complete daily and publish this publicly if its not private info] 
            use different medians to document these people tasks like comics or news articles and keep a running history of tasks
            they do like hurting people or helping people and show effects of each task on the world] 
            use information in this running life dag to prosecute people for destroying the world or hurting people or reward people 
            for helping people] use this to stop evil and encourage good behaviour-""")
      
    def get_on_every_social_media_platform(self):
        """ """
    def identify_methods_people_follow_based_on_the_patterns_they_have_over_examples(self):
        """one way to identify methods people follow based on the patterns they have over
        examples  """
    def build_every_concept_function_in_every_field(self):
        """ like find every concept in finance and build function to conisder it
        NEED TO DO THIS
        need to first find every concept in every field 
        second then need to build every concept in every field
        like roi or prospectsu"""
    def use_all_coding_related_sas_apps_and_load_content(self):
        """ """
    def use_all_psp_related_sas_apps_and_load_content(self):
        """ """
        
    def get_values_associated_with_value_found_in_key(self,dictionary_to_search,value_to_find_in_key_of_dictionary,column_list, column_name="link"):
        """go through the dictionary uploaded from upload sql values and parse so only has specific rows in dictionary keys with a specific row value in a single column """
        # still need to check and test if this works
        specfied_key_value_dic={}
        for column in column_list:
            specfied_key_value_dic[column]=[] 
        column_search_values_list=dictionary_to_search[column_name]     
        for i2,column_value in enumerate(column_search_values_list):
            if column_value==value_to_find_in_key_of_dictionary:
                for column in column_list:
                    specfied_key_value_dic[column].append(dictionary_to_search[column][i2]) 
   
        return specfied_key_value_dic  
    def create_table_sql(self,column_name_data_type_dic,table_name="code_base"):
         """ """
         import psycopg2
         self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
         self.cur = self.conn.cursor() 
         create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
         end_create_table_str = ");"
         for column_name,data_type in column_name_data_type_dic.items():
             create_table_str+=f",{column_name} {data_type}"
         create_table_str+=end_create_table_str
        #print(create_table_str)
         self.cur.execute(create_table_str)
         self.conn.commit()
         
    def delete_table_sql(self,table_name="code_base"):# still need to test this
         """delete a sql table """
         import psycopg2
         self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
         self.cur = self.conn.cursor() 
         self.cur.execute( f""" DROP TABLE {table_name};""")
         self.conn.commit()
         
    def open_selenium(self,link): # will need to moidfy this to use a different generative model
        """ access chatgpt using an intital prompt a path to store the information and a indicatory of a unique value to give the pickle file"""
        import re
        import requests
        import pickle
        import os
        from selenium import webdriver
        from bs4 import BeautifulSoup
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import time
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        cwd = os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Pickles") 
        FirefoxOptions = FirefoxOptions()
        FirefoxOptions.add_argument("--headless")
        #chrome_options.headless = True # also works

        driver= webdriver.Firefox(options=FirefoxOptions)
        session = requests.Session()
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept':'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/webp,*/*;q=0.8'}
        try:
            driver.get(link) #the pages link must be inserted here
        except:
            driver.quit()
        return driver, session, headers
         
    def upload_sql_values(self, table_name="pypi_table",column_list=None):
          """do a sql query to see if any of the values are already in codebase and if so remove them from glossary list """
          import psycopg2
          table_columns=""
          values_string=""
          where_string=""
          column_str=""
          if self.sql_switch==0:
              self.sql_switch=self.init_sql()
          for i2, column in enumerate(column_list):
              if i2==0:
                  column_str+=column
                  continue
              else:
                  column_str+=f",{column}"
         #print(column_str)
          if column_list:
              sql_str=f"SELECT {column_str} FROM {table_name}{where_string};"    
          else:
              sql_str=f"SELECT * FROM {table_name}{where_string};"
          try:
              self.cur.execute(sql_str)
          except Exception as E:
             print(E)    
          sql_data_list_list= self.cur.fetchall()
          return sql_data_list_list
    def process_sql_data_for_searches(self,sql_data_list_list,column_list):
          """ bring data  from database """
          self.search_data_dic={}
          column_list_len=len(column_list)
          for column in column_list:
              self.search_data_dic[column]=[] 
          for sql_data_list in sql_data_list_list:
              for column, sql_data in zip(column_list,sql_data_list):
                  # this should solve hte problem of code not being super usable because
                  # we subbed out commas and such to store it
                  sql_data=str(sql_data)
                  sql_data=sql_data.replace("^","\'")
                  sql_data=sql_data.replace("&","\"")
                  sql_data=sql_data.replace("~",",")
                  sql_data=sql_data.replace("?","'")
                  self.search_data_dic[column].append(sql_data) 
          return self.search_data_dic
    def get_pypi_package_info(self,html):
        """  this will retrieve all the information on the pypi package"""
        from bs4 import BeautifulSoup
        # store the packages name get it from the intital page
        pypi_package_info_dic={"package_name":"","package_link":""}
        sel_soup = BeautifulSoup(html, 'html.parser')
        # parse beautiful soup for pypi package info
        page_text=sel_soup.text
        return pypi_package_info_dic
           

         
    
    def create_list_of_dictionary_to_upload_to_sql(self,column_list):
        """ dict{table_column: column_value}"""
        # lets write this
        for column in column_list:
            [column]=column_value
        list_of_code_base_line_to_upload_to_sql=[]
        current_code_lines_without_glossary_dic={
        "line_of_code": [], 
        "code_base_function": [],
        "code_file_name":[] , 
        "class_name":[],
        "line_number_in_file":[],
        "docstring":[],
        "time_stamp":[]}
        for result in listt:
            code_base_line_to_upload_to_sql={"glossary_definiton": code_stored_in_sql_all_versions["glossary_definiton"][sql_code_line_index],
            "glossary_website":code_stored_in_sql_all_versions["glossary_website"][sql_code_line_index],
            "line_of_code": code_base_search_result["line_of_code"][i2], 
            "class_name":code_base_search_result["class_name"][i2],
            "line_number_in_file":code_base_search_result["line_number_in_file"][i2],
            "docstring":code_base_search_result["docstring"][i2],
            "time_stamp":current_time,
            "code_base_function":code_base_search_result["code_base_function"][i2],
            "code_file_name":code_base_search_result["code_file_name"][i2]}
            list_of_code_base_line_to_upload_to_sql.append(code_base_line_to_upload_to_sql)  
        return list_of_code_base_line_to_upload_to_sql
    
    def retreive_question_or_tool_data_from_web(self,question):
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
         question_striped=question.strip()
         question_to_search_for=re.sub(r"\?","",question_striped)
        #print(question_to_search_for)
         #striped_problem=problem_recorded.strip()
         #problem_to_search_for=re.sub(r"\?","",striped_problem)
         firefox_options = FirefoxOptions()
         firefox_options.headless = True
         driver= webdriver.Firefox(options=firefox_options)
         driver= webdriver.Firefox()
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
             driver.quit()
             return saved_text_from_website_list
    
    
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
       #print(self.automated_problem_galaxy_dic)
        return self.automated_problem_galaxy_dic
    #### PROBLEM TREE FUNCTIONS
    # think of permeant solution here not temp
    # make this work and be useful
        
    def auto_generate_action_space_and_effects(self):
        """ actions are linked to effects"""
        import copy
        automated_problem_galaxy_dic2=copy.deepcopy(self.automated_problem_galaxy_dic)
        self.possible_object_action_effect_list_dic={}#objectttt:[list of actions]
       #print(self.automated_problem_galaxy_dic)
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
    
    
    def init_spacy(self):
          """load in fthe spec fied spacy model """
          import spacy
          self.nlp = spacy.load("en_core_web_sm")
          return 1
    


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
               #print(sentence_15)
                continue
            if len(words_in_current_sentence)>60: 
               #print(sentence_15)
                continue
            if "https" in sentence_15:
               #print(sentence_15)
                continue
            else:
                final_sentence_list.append(sentence_15)
        return final_sentence_list 
    def label_text_with_spacy(self,website_text): 
     """ generate spacy information for a sentnece"""
     import spacy
     sentence=website_text.replace("'","").replace(",","")
     if self.spacy_switch==0:
         self.nlp = spacy.load("en_core_web_sm")
         self.spacy_switch=1
         #https://github.com/explosion/spaCy/issues/12659
         #python -m pip install -U pydantic spacy
         #python -m spacy download en_core_web_sm

     doc = self.nlp(sentence)
     noun_chunks = [chunk.text for chunk in doc.noun_chunks]
     entities = [(ent.text, ent.label_) for ent in doc.ents]
     sentences = [sent.text for sent in doc.sents]
     lemmatized_tokens = [token.lemma_ for token in doc]
     pos_tags = [(token.text, token.pos_) for token in doc]
     return {
         "noun_chunks": noun_chunks,
         "entities": entities,
         "sentence": sentence,
         "lemmatized_tokens": lemmatized_tokens,
         "pos_tags": pos_tags}

        
    def retrieve_glossary_data_from_web_and_post_process_tkinyer(self,code_line_dic2, table_name):
      """ retrieve glossary data from the internet and process it and store it into a sql database of code """
      glossary_word_count_list_of_words_we_want={}
      saved_text_from_websites_and_link_dic_temp={}
      glossary_prompt=code_line_dic2["glossary_prompt"]
      line_of_code= code_line_dic2["line_of_code"]
      code_base_function= code_line_dic2["code_base_function"]
      code_file_name= code_line_dic2["code_file_name"]
      class_name= code_line_dic2["class_name"]
      line_number_in_file= code_line_dic2["line_number_in_file"]
      docstring= code_line_dic2["docstring"]
      time_stamp= code_line_dic2["time_stamp"]
      website_dic={}
      website_dic["website_links"]=""
      website_dic["website_paragraphs"]=""          
      driver, session, headers=self.open_selenium(r"https://html.duckduckgo.com/html/")
      saved_text_from_websites_and_link_dic=self.retreive_glossary_data_from_web(glossary_prompt, driver, session, headers)
      for website_link, website_text in saved_text_from_websites_and_link_dic.items():
          try:
              single_website_text=self.pre_process_text(website_text)
              single_website_text,website_text_sentence_list=self.remove_short_and_long_sentences_and_create_sentence_list(single_website_text)
              saved_text_from_websites_and_link_dic_temp[website_link]=website_text_sentence_list# we watn to use the new single webpage text that has been edited
              spacy_dic_website_text=self.label_text_with_spacy(single_website_text)# here we are getting spacy info to get verb and noun count info
              glossary_word_count_list_of_words_we_want=self.get_nouns_and_verb_counts_in_web_text_retrieved(spacy_dic_website_text,glossary_word_count_list_of_words_we_want) 
              final_noun_verb_dic_to_keep=self.find_highest_count_words(glossary_word_count_list_of_words_we_want)
          except Exception as E:
             #print(E)
              continue
      for website_link2, website_text_sentence_list2, in saved_text_from_websites_and_link_dic_temp.items():# here we are using verb noun count info to parse for more sentences
          glossary_paragraph=self.create_final_glossary_paragraph(final_noun_verb_dic_to_keep,website_text_sentence_list2)
          glossary_paragraph_word_list=self.create_words(glossary_paragraph)
          glossary_paragraph_word_list=glossary_paragraph_word_list[:350]
          glossary_paragraph=" ".join(glossary_paragraph_word_list)
          website_dic["website_links"]+=website_link2+ "@@@"
          website_dic["website_paragraphs"]+=glossary_paragraph +"@@@" 
          # use a delimiter @@@
      code_base_line_to_upload_to_sql={"glossary_definiton": website_dic["website_paragraphs"],
      "line_of_code": line_of_code, 
      "glossary_website":website_dic["website_links"],
      "class_name":class_name,
      "line_number_in_file":line_number_in_file,
      "docstring":docstring,
      "time_stamp":time_stamp,
      "code_base_function":code_base_function,
      "code_file_name":code_file_name
      }
      self.store_value_in_sql_table(code_base_line_to_upload_to_sql,"code_base_table")

    def upload_pickle(self,path_to_pickle):
         """load in a pickle file into python as specfied by path to pickle  """
         import pickle
         import os
         if os.path.exists(path_to_pickle) == True:
             with open(path_to_pickle,"rb") as f1:
                 pickle_file=pickle.load(f1) 
         return pickle_file
     
    def create_pickle(self, path_to_pickle,pickle_info):
     """specify path to the particular place and name you want to give pickle file and the list or dictionary you want to store """
     import pickle
     import os
     if os.path.exists(path_to_pickle) == False:
         with open(path_to_pickle,"wb") as f6: #1
             pickle.dump(pickle_info, f6, pickle.HIGHEST_PROTOCOL)  
    def download_link_html_requests(self,link):
        """ download the html from a requested link"""
        import requests
        session = requests.Session()
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept':'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/webp,*/*;q=0.8'}
        html = session.get(link, headers=headers)
        return html.text,session
    def retrieve_links_on_page(self,sel_soup,website_root,intital_link,used_link_list):
        """retrieve list of links on the page
        COULD IMPROVE THIS BY USING  NEURAL NETOWKR INSTEAD OF SPACY
        still making errors by miss dividing phrases like democratci party and then not adding it but for now this works
        in future if this becaquse a business add neural netowkr for this"""
        from bs4 import BeautifulSoup
        import re
        link_none_dic={}
        link_pattern_dic={}
        link_pattern_dic_single={}
        link_retrieved_dics={}
        print(' need to add in re patterns to search for if psosible for links to get better links but right now dont think we can get better')
        re_person_org_link_patterns_list=[".*",
            ]
        continuee2=False
        unwanted_link_list=["https://en.wikipedia.org#",
                            "https://en.wikipedia.org/wiki/Main_Page",
                            'https://en.wikipedia.org#bodyContent',
                            "https://en.wikipedia.org/wiki/Wikipedia:Contents",
                            "https://en.wikipedia.org/wiki/Portal:Current_events",
                            'https://en.wikipedia.org/wiki/Special:Random',
                            'https://en.wikipedia.org/wiki/Wikipedia:About',
                            'https://en.wikipedia.org//en.wikipedia.org/wiki/Wikipedia:Contact_us',
                             'https://en.wikipedia.org/wiki/Help:Contents',
                             'https://en.wikipedia.org/wiki/Help:Introduction'
                             , 'https://en.wikipedia.org/wiki/Wikipedia:Community_portal'
                             , 'https://en.wikipedia.org/wiki/Special:RecentChanges', 
                             'https://en.wikipedia.org/wiki/Wikipedia:File_upload_wizard',
                             'https://en.wikipedia.org/wiki/Special:SpecialPages',
                             'https://en.wikipedia.org/wiki/Special:Search' ,
                             'https://en.wikipedia.org/wiki/Help:Category',
                             'https://en.wikipedia.org/wiki/Category:Container_categories',
                             'https://en.wikipedia.org/wiki/Wikipedia:Categorization#Subcategorization',
                             "https://en.wikipedia.org/wiki/Wikipedia:FAQ/Categorization#Why_might_a_category_list_not_be_up_to_date?",
                            "https://en.wikipedia.org/wiki/Category:Short_description_is_different_from_Wikidata",
                            'https://en.wikipedia.org/wiki/Category:All_articles_to_be_split',
                            'https://en.wikipedia.org/wiki/Category:Articles_with_short_description',
                            'https://en.wikipedia.org/wiki/Category:Lists_of_lists_with_listcat_specified',
                            "https://en.wikipedia.org/wiki/Category:Wikipedia_semi-protected_project_pages",
                            "https://en.wikipedia.org/wiki/Wikipedia:Protection_policy#semi", 
                            'https://en.wikipedia.org/wiki/Wikipedia:Requests_for_page_protection',
                            'https://en.wikipedia.org/wiki/Wikipedia:Lists_of_protected_pages',
                            'https://en.wikipedia.org/wiki/Wikipedia:PP_(disambiguation)',
                            'https://en.wikipedia.org/wiki/Wikipedia:PROTECT_(disambiguation)', 
                            'https://en.wikipedia.org/wiki/Wikipedia:Policies_and_guidelines',
                            'https://en.wikipedia.org/wiki/Wikipedia:Ignore_all_rules',
                            'https://en.wikipedia.org/wiki/Wikipedia:PGCHANGE',
                            'https://en.wikipedia.org/wiki/Wikipedia:Shortcut',
                            "https://en.wikipedia.org/wiki/Wikipedia:Splitting",
                            "https://en.wikipedia.org/wiki/Category:Articles_to_be_split_from_July_2021",
                            "https://en.wikipedia.org/wiki/Wikipedia:Content_assessment",
                            'https://en.wikipedia.org/wiki/Wikipedia:WikiProject',
                            'https://en.wikipedia.org/wiki/File:Text-x-generic.svg',
                            'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Lists',
                            'https://en.wikipedia.org/wiki/Wikipedia:Stand-alone_lists',
                            'https://en.wikipedia.org/wiki/Wikipedia_talk:WikiProject_Lists',
                            'https://en.wikipedia.org/wiki/Category:Unknown-importance_List_articles',
                            'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Lists/Assessment#Importance_scale', 
                            'https://en.wikipedia.org/wiki/Category:All_article_disambiguation_pages',
                            "https://en.wikipedia.org/wiki/Category:Commons_category_link_is_on_Wikidata", 
                            'https://en.wikipedia.org/wiki/User:CleanupWorklistBot', 
                            'https://en.wikipedia.org/wiki/Category:Template-Class_List_pages', 
                            'https://en.wikipedia.org/wiki/Category:NA-importance_List_pages', 
                            'https://en.wikipedia.org/wiki/Category:WikiProject_Lists_articles', 
                            'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Countries', 
                            'https://en.wikipedia.org/wiki/Wikipedia_talk:WikiProject_Countries',
                            'https://en.wikipedia.org/w/index.php?title=Wikipedia%3AWikiProject_Countries%2Fto_do&action=edit', 
                            'https://en.wikipedia.org/w/index.php?title=Wikipedia%3AWikiProject_Countries%2Fto_do&action=history', 
                            'https://en.wikipedia.org/w/index.php?title=Wikipedia%3AWikiProject_Countries%2Fto_do&action=watch',
                            'https://en.wikipedia.org/w/index.php?title=Wikipedia%3AWikiProject_Countries%2Fto_do&action=purge',
                            'https://en.wikipedia.org/wiki/Category:WikiProject_Countries_articles',
                            "https://en.wikipedia.org/wiki/Special:EditPage/Template:List_resources",
                            ]
        #sel_soup = BeautifulSoup(html, 'html.parser')
        #use neural network
        # and mix these
        # its good for now 
        # there are sometime whee spacy messed up could fix if had time but for now this is good enough
        all_links_no_html_list=[]
        links_of_dif_docs= sel_soup.findAll("a")
        key_word_list=["list","lists","people","protestors","activists",
                       "scholars","activist"]
        uwanted_str_seq_list=["=edit&redlink","action=edit&section","wiki/File:","#(Top)","&redirect=no",
                              "wiki/Talk:","&action=","index.php?title=Template_talk:","index","countries","wiki/Special:EditPage"]
        

        # other wise make sure ti is a name or a orgnaizaion
        continuee3=False
        person_corp_links_list=[]
        all_link_item_titles_list=[]
        all_links_no_html_list=[]
       #print('treat it as a article link and praese it to find people only and maybe companies')
        temp_person_org_dic={}  
        temp_person_org_dic["Name_ORG"]=[]
        for link_with_html in links_of_dif_docs: 
            if link_with_html: 
               #print('meow')               
                link=link_with_html.get('href')
               #print(link)
                if link:                    
                    if "https://" not in  link:
                       #print(link)
                        link=website_root+link
                        
                        if link in unwanted_link_list:
                            continue
                        for unwanted_str_seq in uwanted_str_seq_list:
                            if unwanted_str_seq in link:
                                continuee2=True
                                break
                        if continuee2 ==True:
                            continuee2=False
                            continue
                        
                        if link ==intital_link:
                            continue
                        
                        if link in used_link_list:
                            continue
                        
                        if link in link_none_dic:
                            link_none_dic[link].append([])
                            continue
                        # if key word in link then just add it
                        link_lower=link.lower()
                        for key_word in key_word_list:
                            if key_word in link_lower:
                                link_none_dic[link]=[]
                                continuee3=True
                                break
                        if continuee3==True:
                            continuee3=False
                            continue 
                        #otherwise add to the check for name list
                       #print(link)
                        single_link_list=re.split(r"/",link)
                        all_links_no_html_list.append(link)
                        link_item_title=single_link_list[-1]
                        all_link_item_titles_list.append(link_item_title)
                        
        # chekc for name and other info to make sure it is a good link            
        all_link_item_titles_str=".  ".join(all_link_item_titles_list)
        all_link_item_titles_str=re.sub("_"," ",all_link_item_titles_str)   
       #print(all_link_item_titles_str)
        # only grab orgs and persons
        doc = self.nlp(all_link_item_titles_str) 
        # find the associated link after
        for ent in doc.ents:
           #print(f"{ent.text},{ent.label_}")
            if "." in ent.text:
                textt_list=re.split("  .",ent.text)
                textt=re.sub(" ","_",textt_list[-1])
            else:
                textt=re.sub(" ","_",ent.text)
            if ent.label_ == "PERSON":
                
                temp_person_org_dic["Name_ORG"].append([textt,ent.label_])
            if ent.label_ == "ORG":
                temp_person_org_dic["Name_ORG"].append([textt,ent.label_])
            
            continue 
       #print('ALL ORG AND NAMES FOUND')
        #print(temp_person_org_dic)           
        ## find associated link to the spacy output            
        for name_or_org in temp_person_org_dic["Name_ORG"]:
            for i,link_title in enumerate(all_link_item_titles_list): 
                  
                if name_or_org[0] in link_title:
                    #find associated link
                    link_wanted=all_links_no_html_list[i]
                    link_none_dic[link_wanted]=[]
                    
        link_retrieved_dics={"link_none_dic":link_none_dic,"link_pattern_dic":link_pattern_dic,"link_pattern_dic_single":link_pattern_dic_single}
        #print(link_none_dic)
        return link_retrieved_dics
        
        
        #else: # normal page link
        # merge the other search into this one and add in key words we are lookong for in addition to the names
        # fix the output coming from this so it gets the right results
            # if key word in link then add it
            
        
        # need to avoid getting links on pages i dont want   
        # like on the 
        #https://en.wikipedia.org/wiki/Religion
        #how do i deal with this and crawl this better
        # want to differentiate between concepts and people and orgainizaions
        # just use spacy?
        # only want name links and orgnaizaion links
        # and list links
        #list
        # and not anything else
        # must have one of these terms the or formats
        # just use spacy
        #on link
        #
        #if catrgory page then grab everything
        # if it sa article page then be more specific
        # and only grab names and dont process data 
        # keep it simple just grab peoples name links on none category pages
        
        ### want to match the text with the link
 
        #name_pattern=re.search(r"")
        #if name_pattern:         
        #two captial words
        
        
    def process_link_pattern_dic(self):
        """ """
        
    def retrieve_specific_link_in_html(self,pattern):
        """ """
        # if above certain github stars otherwise dont downlod the repo?
        # bascially parse html to find a specific pattern or link
        # in tis case a pypi 

   
    def create_website_text_dic_pypi_data(self,saved_text_from_websites_and_link_dic):
          """ """
          for website_link, website_text in saved_text_from_websites_and_link_dic.items():
              try:
                  single_website_text=self.pre_process_text(website_text)
                  single_website_text,website_text_sentence_list=self.remove_short_and_long_sentences_and_create_sentence_list(single_website_text)
                  saved_text_from_websites_and_link_dic_temp[website_link]=website_text_sentence_list# we watn to use the new single webpage text that has been edited
                  spacy_dic_website_text=self.label_text_with_spacy(single_website_text)# here we are getting spacy info to get verb and noun count info
                  glossary_word_count_list_of_words_we_want=self.get_nouns_and_verb_counts_in_web_text_retrieved(spacy_dic_website_text,glossary_word_count_list_of_words_we_want) 
                  final_noun_verb_dic_to_keep=self.find_highest_count_words(glossary_word_count_list_of_words_we_want)
              except Exception as E:
                 #print(E)
                  continue
          for website_link2, website_text_sentence_list2, in saved_text_from_websites_and_link_dic_temp.items():# here we are using verb noun count info to parse for more sentences
              glossary_paragraph=self.create_final_glossary_paragraph(final_noun_verb_dic_to_keep,website_text_sentence_list2)
              glossary_paragraph_word_list=self.create_words(glossary_paragraph)
              glossary_paragraph_word_list=glossary_paragraph_word_list[:350]
              glossary_paragraph=" ".join(glossary_paragraph_word_list)
              website_dic["website_links"]+=website_link2+ "@@@"
              website_dic["website_paragraphs"]+=glossary_paragraph +"@@@" 
              # use a delimiter @@@
          code_base_line_to_upload_to_sql={"glossary_definiton": website_dic["website_paragraphs"],
          "line_of_code": line_of_code, 
          "glossary_website":website_dic["website_links"],
          "class_name":class_name,
          "line_number_in_file":line_number_in_file,
          "docstring":docstring,
          "time_stamp":time_stamp,
          "code_base_function":code_base_function,
          "code_file_name":code_file_name
          }
          return code_base_line_to_upload_to_sql
          self.store_value_in_sql_table(code_base_line_to_upload_to_sql,"code_base_table")
 
    def store_value_in_sql_table_2(self,dictionary_of_values,table_name):
        """key are row names, value is the values that go in the rows """
        testing=False
        if testing==True:
            import psycopg2
            self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
            self.cur = self.conn.cursor() 
        import re
        table_columns=""
        values_string=""
        #if self.sql_switch==0:
        #    self.sql_switch=self.init_sql()
        for i, (table_column, column_value) in enumerate(dictionary_of_values.items()):
            
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
    
    def store_value_in_sql_table(self,dictionary_of_values,table_name):
        """key are row names, value is the values that go in the rows """
        testing=False
        if testing==True:
            import psycopg2
            self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
            self.cur = self.conn.cursor() 
        import re
        table_columns=""
        values_string=""
        #if self.sql_switch==0:
        #    self.sql_switch=self.init_sql()
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
    

    def command_selenium_grab_page_info_pypi(self,driver):
        """ """
        from selenium import webdriver
        from bs4 import BeautifulSoup
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "Element_to_be_found")) #This is a dummy element
            )
        except:
            driver.quit()
        EC.presence_of_element_located((By.ID, "Element_to_be_found")) #This is a dummy element

        import time
        links_of_dif_docs=[]
        saved_link_list=[]
        saved_text_from_websites_and_link_dic={}
        content = driver.find_element(By.CLASS_NAME, 'search__input')
        content.send_keys(f"{web_prompt}")
        content.send_keys(Keys.ENTER)
        time.sleep(2)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html= driver.execute_script("return document.documentElement.outerHTML")
        content = driver.find_element(By.CLASS_NAME, 'search__input')
        content = driver.find_element(By.ID, 'prompt-textarea')
        return html
    

    def process_pypi_package_search_data(self):
        """ take all information gained from web crawlers and searchs and make it inputtable into pypi table"""
        # we will save by codeline i think
        current_code_lines_without_glossary_dic={
        "line_of_code": [], 
        "code_base_function": [],
        "code_file_name":[] , 
        "class_name":[],
        "line_number_in_file":[],
        "docstring":[],
        "time_stamp":[]}
        list_of_code_base_line_to_upload_to_sql=[]
        coding_file_dic_without_used_values_list=[]
        current_time=time.time()
        sql_line_of_code_list=code_stored_in_sql_all_versions["line_of_code"]
        code_base_line_of_code_list=code_base_search_result["line_of_code"]
        ### find matchs
        for i2,code_line in enumerate(code_base_line_of_code_list ):
            #matchign function
            #match_result=re.search()
            # reuse a matching function if this does not work and place this where code line in is 
            # if very similar then can use glossary
            if code_line in sql_line_of_code_list:# might need to rewrite this if it is not working # be a regex or a 80 percent match in character reuse a matching function we wrote
                sql_code_line_index=sql_line_of_code_list.index(code_line)# still need to test this
                code_base_line_to_upload_to_sql={"glossary_definiton": code_stored_in_sql_all_versions["glossary_definiton"][sql_code_line_index],
                "glossary_website":code_stored_in_sql_all_versions["glossary_website"][sql_code_line_index],
                "line_of_code": code_base_search_result["line_of_code"][i2], 
                "class_name":code_base_search_result["class_name"][i2],
                "line_number_in_file":code_base_search_result["line_number_in_file"][i2],
                "docstring":code_base_search_result["docstring"][i2],
                "time_stamp":current_time,
                "code_base_function":code_base_search_result["code_base_function"][i2],
                "code_file_name":code_base_search_result["code_file_name"][i2]}
                list_of_code_base_line_to_upload_to_sql.append(code_base_line_to_upload_to_sql)
                continue
            else:
                # put it inot proper format
                coding_file_dic_without_used_values={"line_of_code": code_base_search_result["line_of_code"][i2], 
                "code_base_function": code_base_search_result["code_base_function"][i2],
                "code_file_name":code_base_search_result["code_file_name"][i2], 
                "class_name":code_base_search_result["class_name"][i2],
                "line_number_in_file":code_base_search_result["line_number_in_file"][i2],
                "docstring":code_base_search_result["docstring"][i2],
                "time_stamp":current_time}
                coding_file_dic_without_used_values_list.append(coding_file_dic_without_used_values)    
                continue

    def process_pypi_code_line_search_data(self):
        """ take all information gained from web crawlers and searchs and make it inputtable into pypi table"""
        # we will save by codeline i think
        current_code_lines_without_glossary_dic={
        "line_of_code": [], 
        "code_base_function": [],
        "code_file_name":[] , 
        "class_name":[],
        "line_number_in_file":[],
        "docstring":[],
        "time_stamp":[]}
        list_of_code_base_line_to_upload_to_sql=[]
        coding_file_dic_without_used_values_list=[]
        current_time=time.time()
        sql_line_of_code_list=code_stored_in_sql_all_versions["line_of_code"]
        code_base_line_of_code_list=code_base_search_result["line_of_code"]
        ### find matchs
        for i2,code_line in enumerate(code_base_line_of_code_list ):
            #matchign function
            #match_result=re.search()
            # reuse a matching function if this does not work and place this where code line in is 
            # if very similar then can use glossary
            if code_line in sql_line_of_code_list:# might need to rewrite this if it is not working # be a regex or a 80 percent match in character reuse a matching function we wrote
                sql_code_line_index=sql_line_of_code_list.index(code_line)# still need to test this
                code_base_line_to_upload_to_sql={"glossary_definiton": code_stored_in_sql_all_versions["glossary_definiton"][sql_code_line_index],
                "glossary_website":code_stored_in_sql_all_versions["glossary_website"][sql_code_line_index],
                "line_of_code": code_base_search_result["line_of_code"][i2], 
                "class_name":code_base_search_result["class_name"][i2],
                "line_number_in_file":code_base_search_result["line_number_in_file"][i2],
                "docstring":code_base_search_result["docstring"][i2],
                "time_stamp":current_time,
                "code_base_function":code_base_search_result["code_base_function"][i2],
                "code_file_name":code_base_search_result["code_file_name"][i2]}
                list_of_code_base_line_to_upload_to_sql.append(code_base_line_to_upload_to_sql)
                continue
            else:
                # put it inot proper format
                coding_file_dic_without_used_values={"line_of_code": code_base_search_result["line_of_code"][i2], 
                "code_base_function": code_base_search_result["code_base_function"][i2],
                "code_file_name":code_base_search_result["code_file_name"][i2], 
                "class_name":code_base_search_result["class_name"][i2],
                "line_number_in_file":code_base_search_result["line_number_in_file"][i2],
                "docstring":code_base_search_result["docstring"][i2],
                "time_stamp":current_time}
                coding_file_dic_without_used_values_list.append(coding_file_dic_without_used_values)    
                continue

        # maybe throw in spacy here
        # link data could be useful
        #we want code from the pages
        # we want
        #anything with text directly after period these should be modules we want to copy
        # this is the unique pattern for code
        # get context around torch. before to a certain point
        # assume everythign before  or after is talking about the code on the page of the docs
        # so grab this text and store it 
        
        ### process crawler data
    def check_if_multiple_value_in_str(self,code_lines_in_code_chunk,value_to_check_list=["www","https","e.g", ".txt",".org",".net",".co",".com",".sh",".docker",".readthedocs","i.e"]):
            final_temp_code_line_in_chunk_list=[]
            value_found=False
            for code_lines in code_lines_in_code_chunk:
                #print(f"these are code lines: {code_lines}")
                value_found=False
                for value_to_check in value_to_check_list:
                    if value_to_check in code_lines:
                        #print(value_to_check)
                        #print('HEHEHEHEHE')
                        value_found=True
                        break
                if value_found==True:
                    continue
                else:
                    final_temp_code_line_in_chunk_list.append(code_lines)
                    #print(f"final_temp_code_line_in_chunk_list : {final_temp_code_line_in_chunk_list}")
            return final_temp_code_line_in_chunk_list

    def check_code_line_patterns(self,page_line_text,last_page_line_type,find_code_imports,temp_code_lines_in_code_chunk,temp_code_chunk):
            """ """
            import re
            coding_line_indicator_list=[r"\):","import",r"class",r"[a-zA-Z0-9]+\.[a-zA-Z0-9]+", "def","=",r"[a-zA-Z]+\(","[a-zA-Z0-9]+_[a-zA-Z0-9]+","\)","return","[\[\]\{\}]","#","else:"]

            #cleaned_code_lines_in_code_chunk=[]
            for pattern in coding_line_indicator_list:
                code_line_result=re.search(pattern,page_line_text)
                if code_line_result and last_page_line_type=="text":
                    code_lines_in_code_chunk=re.findall(find_code_imports,page_line_text)
                    cleaned_code_lines_in_code_chunk=self.check_if_multiple_value_in_str(code_lines_in_code_chunk)
                    temp_code_chunk=page_line_text
                    if cleaned_code_lines_in_code_chunk==[]:
                        break
                    temp_code_lines_in_code_chunk.extend(cleaned_code_lines_in_code_chunk)
                    break
                if code_line_result and last_page_line_type=="code":
                    code_lines_in_code_chunk=re.findall(find_code_imports,page_line_text)
                    temp_code_chunk+="\n"+page_line_text# will have to chekc this
                    cleaned_code_lines_in_code_chunk=self.check_if_multiple_value_in_str(code_lines_in_code_chunk)
                    #print(f"cleaned_code_lines_in_code_chunk meow: {cleaned_code_lines_in_code_chunk}")
                    if cleaned_code_lines_in_code_chunk==[]:
                        break
                    temp_code_lines_in_code_chunk.extend(cleaned_code_lines_in_code_chunk)
                    break
            return code_line_result, temp_code_lines_in_code_chunk, temp_code_chunk
    def add_uniform_data_to_dictionary(self,data_retrieved_dic,input_dic):
        """ we will use this as generic way to upload uniform values across a dictionary"""
        for key in data_retrieved_dic.keys():
            if key in input_dic:
                data_retrieved_dic[key].append(input_dic[key])
            else:
                data_retrieved_dic[key].append(None)
        return data_retrieved_dic

    def process_crawl_data_generate_function_list(self,sel_soup,data_retrieved_dic,pypi_doc_name,file_name=None,repo_name=None):
            """ """
            
            non_space_matcher=r"[^ \t]+"
            page_text=sel_soup.text
            page_line_list=page_text.splitlines()
            code_chunk_end_line_number_list=[]
            temp_code_lines_in_code_chunk=[]
            temp_code_chunk=""
            last_page_line_type="text"
            for page_line_number,page_line_text in enumerate(page_line_list):
                non_space_match=re.search(non_space_matcher,page_line_text)
                if non_space_match:# has characters in line
                    if page_line_text=="":
                        continue
                    code_line_result,temp_code_lines_in_code_chunk,temp_code_chunk=self.check_code_line_patterns(page_line_text,last_page_line_type,find_code_imports,temp_code_lines_in_code_chunk,temp_code_chunk)
                else:
                    continue 
                if code_line_result:
                    last_page_line_type="code"
                    continue
                if temp_code_chunk=="":
                    continue
                if temp_code_lines_in_code_chunk==[]:
                    continue
                input_dic={"code_base_function":temp_code_chunk,
                "code_lines_in_function":temp_code_lines_in_code_chunk,
                "pypi_doc_name":pypi_doc_name,
                "time_stamp":time_stamp ,
                "pypi_file_name":file_name,
                "repo_name":repo_name}
                data_retrieved_dic=self.add_uniform_data_to_dictionary(data_retrieved_dic,input_dic)
                code_chunk_end_line_number_list.append(page_line_number)
                temp_code_chunk=""    
                temp_code_lines_in_code_chunk=[]
                last_page_line_type="text"
                #data_retrieved_dic,code_chunk_end_line_number_list,temp_code_chunk,temp_code_lines_in_code_chunk,last_page_line_type=self.add_uniform_data_to_dictionary(data_retrieved_dic,code_chunk_end_line_number_list,temp_code_chunk,temp_code_lines_in_code_chunk,pypi_doc_name,time_stamp,page_line_number)
                
            return   data_retrieved_dic,code_chunk_end_line_number_list,page_line_list
        
        
    def order_and_divide_actions_into_action_lists(self,person_comp_info_dic_with_action_list):
        """ this we will use qualtiies of actions and dic to create action lists and order actions probably using some sort of context        
        the person_comp_info_dic_with_action_list is filled in here so use all the qualtites to sort and divide up the actions maybe build a NN to do it
        """
        return person_comp_info_dic_with_action_list
        print('USE THE BELOW FUNCTION TO DIVIDE UP ACTIONS INTO sub tasks and different strategies and order strategies because it uses the context with three outputs')
        self.search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved()
        for person_comp_info_dic_with_action in person_comp_info_dic_with_action_list.items():
            actionn=person_comp_info_dic_with_action['action']
            print(actionn)
            
            
            
        
        # if context seems the same group those actions maybe
        # if other text seems to make those text fit together do those actions
        
    def label_website_text_with_spacy(self,website_text): 
        #a1_1_1.1.1.1_1
        """ generate spacy information for a sentnece"""
        website_text=website_text.replace("?","").replace(",","")
        doc = self.nlp(website_text)
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
            "sentence": website_text,
            "lemmatized_tokens": lemmatized_tokens,
            "pos_tags": pos_tags,
            "pos_only_tags":pos_only_tags,
            "text_only_tags":text_only_tags
            }
    
    
            
    def create_sub_action_list(self,single_website_text):
        """need to parse website text to create the sub action list for an action """
        sub_action_list=[]
        doc = self.nlp(single_website_text)      
        action_sentence=False 
        sentence_action_type_dic={}
        sentence=""
        counterr=0
        action_sentence_value="not action sentence"
        entity_text_dic={}
        for ent in doc.ents:
            #print(f"{ent.text},{ent.label_}")
            #print('hehe')
            textt=ent.text
            labell=ent.label_
            if " " in textt:
                textt_list=textt.split()
            else:
                textt_list=[textt]
            for textt in textt_list:
                if ent.label_ == "PERSON":
                    entity_text_dic[ent.text]="PERSON"
                if ent.label_ == "ORG":
                    entity_text_dic[ent.text] = "ORG"                
                if ent.label_ == "DATE":
                    entity_text_dic[ent.text] = "DATE"
                if ent.label_ == "MONEY":
                    entity_text_dic[ent.text] = "MONEY"         
                continue 
            
        for token in doc:
            #print(token.text, token.pos_)
            if token.text in entity_text_dic:
                token_label=entity_text_dic[token.text]
                if token_label=="PERSON" or token_label=="ORG":
                    action_sentence_value=="action sentence"  
                    
            if sentence != "":
                sentence+=f" {token.text}"
            else:
                sentence=f"{token.text}"  
                
            if token.text==".":
                #print(token.text)
                #print(f"sentence: {sentence}")
                #print('meow')
                if action_sentence_value=="action sentence":
                    counterr+=1
                    sub_action_list.append(sentence)
                    #person_comp_info_dic_with_action["action"]=sentence
                    #person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=counterr
                    #person_comp_info_dic_with_action["link"]=intital_link
                    #person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                    # clear the dicitonary
                    #person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)
                sentence="" 
                action_sentence_value="not action sentence"                           
            if token.pos_== "PRON":
                action_sentence_value="action sentence"
                # action sentence
                action_sentence=True
                #print('hi')
                continue
       #print(sub_action_list)
        #input("hi my name is jeff")
        return sub_action_list
    
        # use this info to create the sub action list
    def sub_proper_noun_from_pronoun(self,sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,pronoun_iter_in_sub_list):
        """ find the mention of org and sub it into sentence"""
        proper_noun_found=False
        proper_noun_phrase_list=["--REFFERENTIAL PHRASE--"]
        pos_phrase_list=["PROPN"]
        current_sentence_word_list=sentence_word_list[current_sent_iter]
        current_sentence_pos_list=token_pos_list[current_sent_iter]
        previous_sentence_word_sub_list=sentence_word_list[current_sent_iter-minus_current_sen_iter]
        previous_sentence_token_pos_list=token_pos_list[current_sent_iter-minus_current_sen_iter]
        for i13, possss in enumerate(previous_sentence_token_pos_list):   
            if possss=="PROPN":
                proper_noun_found=True              
                proper_noun_word=previous_sentence_word_sub_list[i13]
                proper_noun_phrase_list.append(proper_noun_word)
                pos_phrase_list.append(possss)
                continue
            if proper_noun_found==True:# rthis will prevent us getting proper nouns that are not related
                break
        if proper_noun_found==True:
            # adding 1 here ot remove the word being subbed over the pronoun word
            current_sentence_word_list=current_sentence_word_list[:pronoun_iter_in_sub_list]+proper_noun_phrase_list+current_sentence_word_list[pronoun_iter_in_sub_list+1:]
            current_sentence_pos_list=current_sentence_pos_list[:pronoun_iter_in_sub_list]+pos_phrase_list+current_sentence_pos_list[pronoun_iter_in_sub_list+1:]
            
            #current_sentence_word_list.insert(pronoun_iter_in_sub_list,proper_noun_phrase_list) 
        return  current_sentence_word_list,current_sentence_pos_list, proper_noun_found
    
    def get_intital_action_info_from_page(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """ # first divide up text into sentences
        # second run through each sentence find all instances of noun chunk verb object 
        # sub pronoun for proper nouns and make notes of this all referential phrases 2-3 sentences ahead
        # store these approrpiately in dicitonaries if they have this info

        # then store all of them in dic based on qualities to divide up all actions into next actions and sub actions
        # using order and sub action function"""
        import re
        import copy
        import spacy
        import time
        from nltk.corpus import stopwords     
        cleaned_noun_chunk_list=[]
        person_comp_info_dic_with_action={         
            "action":"",
            "action_temporal_placement_in_life_list":"#",
            
            "noun_and_verb_chunk_list":[],
            "noun_and_verb_chunk_pos_list":[],
             
            ### action qualities
            "user_time_past_use_of_action_list":[],
            
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],
            "intital_page_text":[],
            "object":[],

            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[], }
        
        
        sentence_list=[]
        sentence_word_list=[]
        iter_list=[]
        token_label_list=[]
        token_pos_list=[]
        iter_sub_list=[]
        token_sub_label_list=[]
        token_pos_sub_list=[]
        sentence_word_sub_list=[]
        entity_text_dic={}
        chunk_span_sub_list=[]       
        saved_noun_chunk_list=[]
        saved_noun_chunk_sub_list=[]       
        sentence=""
        # clean the text  
        page_text=sel_soup.text
        page_text=re.sub("[\[\]{}\'\(\)]","",page_text) 
        page_text=re.sub("  ", " ", page_text)
        page_text=re.sub("-", " ", page_text)
        #spacy_dic=self.label_website_text_with_spacy(website_text)
        doc = self.nlp(page_text)
        for ent in doc.ents:
            #print(f"{ent.text},{ent.label_}")
            #print('hehe')
            textt=ent.text
            labell=ent.label_
            if " " in textt:
                textt_list=textt.split()
            else:
                textt_list=[textt]
            for textt in textt_list:
                if ent.label_ == "PERSON":
                    entity_text_dic[ent.text]="PERSON"
                if ent.label_ == "ORG":
                    entity_text_dic[ent.text] = "ORG"                
                if ent.label_ == "DATE":
                    entity_text_dic[ent.text] = "DATE"
                if ent.label_ == "MONEY":
                    entity_text_dic[ent.text] = "MONEY"         
                continue 
            
            
            
        #input("meow")
        # noun chunks must be in order 
        
        ### LOOP 1        
        used_noun_chunk_iter_list=[]
        used_noun_chunk_sub_iter_list=[]         
        used_word_sentence_iter_list=[]       
        used_word_sentence_sub_iter_list=[]  
        used_word_iter_list=[]
        #empty_noun_chunk_word_matching_list=[None for iterr in range(len(doc))]
        empty_noun_chunk_word_matching_list=[[str(token.text),None] for token in doc]

        
        noun_chunk_words_found=0
        used_noun_chunk_iter_dic={}
        noun_chunk_iter=0       
        all_noun_chunk_list=[]
        
        for noun_chunk in doc.noun_chunks:
            new_noun_chunkkk=""
            noun_chunkk=str(noun_chunk).split()
            for wordddd in noun_chunkk:
                #print(wordddd)            
                if wordddd!="":
                    if new_noun_chunkkk =="":
                        #print('hi')
                        new_noun_chunkkk=f"{wordddd}"
                    else:
                        new_noun_chunkkk+=f" {wordddd}"
            all_noun_chunk_list.append(str(new_noun_chunkkk)) 
            #nounn_chunk_list=str(noun_chunk).split(" ")  
        all_noun_chunk_list_len=len(all_noun_chunk_list)
   
        noun_chunkkk=all_noun_chunk_list[noun_chunk_iter]
        nounn_chunk_list=noun_chunkkk.split(" ")
        noun_chunk_list_len=len(nounn_chunk_list)  
        for word_iter, tokenn in enumerate(doc):
            if word_iter in used_word_iter_list:
                continue
            wordd=tokenn.text  
            #print(wordd)
            #print(noun_chunk_iter)
            #print(nounn_chunk_list)
            if wordd in nounn_chunk_list:
                #print("word in")               
                if noun_chunk_iter not in used_noun_chunk_iter_dic:
                    used_noun_chunk_iter_dic[noun_chunk_iter]=[]                   
                used_noun_chunk_iter_dic_len=len(used_noun_chunk_iter_dic[noun_chunk_iter])  
                # want to check if next word in noun chunk is the word and add it to the used word list
                # also want to see if noun chunk list is long enough to check this
                print(f"used_noun_chunk_iter_dic_len {used_noun_chunk_iter_dic_len}")
                if nounn_chunk_list[used_noun_chunk_iter_dic_len]==wordd:
                            used_noun_chunk_iter_dic[noun_chunk_iter].append(wordd)
                            empty_noun_chunk_word_matching_list[word_iter][1]=noun_chunk_iter
                else:
                    continue
                if used_noun_chunk_iter_dic[noun_chunk_iter]==nounn_chunk_list:
                    print('lists match')
                    noun_chunk_iter+=1
                    print(noun_chunk_iter)
                    if noun_chunk_iter==all_noun_chunk_list_len:# this avoids the error where last value tries to grab a value not in noun chunk list
                        break
                    else:
                        noun_chunkkk=all_noun_chunk_list[noun_chunk_iter]
                        nounn_chunk_list=noun_chunkkk.split(" ")
                        noun_chunk_list_len=len(nounn_chunk_list)  
                        continue                          
        #print(all_noun_chunk_list)
        #print(used_noun_chunk_iter_dic)
        #print(empty_noun_chunk_word_matching_list)                          
        #input() 
          
        ### LOOP 2
        # need to sub numbers and non word characters out of noun chunks
        # like periods brackets and [] and slashes
        # have sentence a key and pos values and text and noun chunk values all included
        # get noun chunk related to work
        # mark noun chunk components as used and words as used to avoid getting duplicates
        # once you find a matching word for a noun chunk consider the length of noun chunk and try to find the remainer in the sentence
        # that way
        ## aux could be verb as well or ahelping verb
        #sentence_assocaited_chunk_list=[] 
        #sentence_assocaited_sub_chunk_list=[]
        # going to move this before the other loop and make this loop one
        #noun_chunk_list=[]
        #noun_chunk_sub_list=[]
        for i8, token in enumerate(doc):
            noun_chunk_group=empty_noun_chunk_word_matching_list[i8]
            token_label=None
            if token.text in entity_text_dic:
                token_label=entity_text_dic[token.text]
                
            if sentence != "":
                text_len=len(token.text)
                sentence+=f" {token.text}"
                iter_sub_list.append(i8)
                token_sub_label_list.append([token.text,token_label])
                token_pos_sub_list.append(token.pos_)
                sentence_word_sub_list.append(token.text)
                saved_noun_chunk_sub_list.append(noun_chunk_group)
                
                    
            else:
                text_len=len(token.text)
                sentence=f"{token.text}" 
                iter_sub_list.append(i8)
                token_sub_label_list.append([token.text,token_label])
                token_pos_sub_list.append(token.pos_)
                sentence_word_sub_list.append(token.text)
                saved_noun_chunk_sub_list.append(noun_chunk_group)


                
            if "." in token.text :# will need to test htis one
              sentence=re.sub(r"[\n\r]"," ",sentence)
              sentence=re.sub(r"\s\s+","  ",sentence)
              sentence_list.append(sentence)
              iter_list.append(iter_sub_list)
              token_label_list.append(token_sub_label_list)
              token_pos_list.append(token_pos_sub_list)
              sentence_word_list.append(sentence_word_sub_list)
              saved_noun_chunk_list.append(saved_noun_chunk_sub_list)
              sentence="" 
              iter_sub_list=[]
              token_sub_label_list=[]
              token_pos_sub_list=[]
              sentence_word_sub_list=[]
              saved_noun_chunk_sub_list=[]
        #for i in range(len(sentence_list)):
            #print(i)
            #print(sentence_list[i])
            #print('------')
            #print(token_label_list[i])
            #print('------')

            ##print(token_pos_list[i]) 
            #print('------')

            #print(saved_noun_chunk_list[i])
            #print('------')
        #print('stop')
        #print(saved_noun_chunk_list)
        #input(used_noun_chunk_iter_dic)
        ### LOOP 3   
        # match the chunk words with the words in the sentnece
        # so you know each word that goes with each chunk so you can match verb against noun chunk
        # and fiue out the action part of the sentence
        # create the action sentences here
        # use this to fill in the action dicitionary
        
        # sub out pronouns now for referential phrases
        temporal_counter=0
        for current_sent_iter, sentenceee in enumerate(sentence_list):
            temp_chunk_str_dic={}
            noun_chunk2_number=None
            last_chunk=None
            add_next_noun_chunk=False
            token_sub_label_list=token_label_list[current_sent_iter]
            token_pos_sub_list=token_pos_list[current_sent_iter]
            sentence_word__sub_list=sentence_word_list[current_sent_iter]
            sentence_assocaited_sub_chunk_list=saved_noun_chunk_list[current_sent_iter]
            person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
            verb_counter=0
            if "VERB" in token_pos_sub_list or "AUX" in token_pos_sub_list:
                for pos_iter, posss in enumerate(token_pos_sub_list):                   
                    verb_wordddd=sentence_word__sub_list[pos_iter]
                    posss=posss
                    # if verb followed by other verb in between noun chunks
                    # group these as a verb chunk
                    # then done
                    #who work  the rights
                    #who protect  the rights
                    #because getting this error now
                    #should jusrt be work to protect the rights
                    # sub out referentisal phrase
                    # for referntial phrases add
                    # if referential phrase sub in last referecned noun chunk
                    #before the current noun chunk
                    # if pronoun sub in proper noun
                    # if followed by a aux 
                    
                    current_chunk_number=None
                    chunk_str=""
                    if posss == "VERB" or posss == "AUX":
                         verb_counter+=1# this makes sure we only sub out PRON in intital noun chunk and no others in setnece
                         # find noun chunk before find noun chunk after
                         for chunkk_iter, chunk_word in enumerate(sentence_assocaited_sub_chunk_list):                             
                             wordd=chunk_word[0]
                             chunkk=chunk_word[1]
                             if chunkk!=None:
                                 current_chunk_number=chunkk
                                 chunk_iter=chunkk_iter
                             
                             # want the chunk iterr to line up                          
                             if chunkk_iter==pos_iter and current_chunk_number!=None :
                                 chunk_text1=" ".join(used_noun_chunk_iter_dic[current_chunk_number])
                                 #chunk_str=chunk_text1 + f" {verb_wordddd}  "
                                 #first_chunk_iter=chunkk_iter
                                 first_chunk_number=current_chunk_number
                                 first_chunk_end_iter=chunk_iter
                                 continue
                             if chunkk_iter>pos_iter and chunkk!=None:
                                 #this is the next chunk
                                 #print(f"first chunk {used_noun_chunk_iter_dic[first_chunk_number]}")
                                 first_chunk_len_minus_1=len(used_noun_chunk_iter_dic[first_chunk_number])-1

                                 second_chunk_len_minus_1=len(used_noun_chunk_iter_dic[current_chunk_number])
                                 #print(f"second chunk {used_noun_chunk_iter_dic[current_chunk_number]}")

                                 # will hopedully get us to the end of the chunk
                                 #chunk_text2=" ".join(used_noun_chunk_iter_dic[current_chunk_number]) 
                                 #find the end of the second second chunk segement
                                 second_chunk_end_iter=chunkk_iter   
                                 #print(f"sentence_word__sub_list {sentence_word__sub_list}")
                                 #action_segment=" ".join(sentence_word__sub_list[first_chunk_end_iter-first_chunk_len_minus_1:second_chunk_end_iter+second_chunk_len_minus_1])# but by adding this value here hopefully will get us to the end of the chunk                                
                                 #sub out in first chunk using pos any pronouns for proper nouns
                                 #and other referential phrases for their given referenced nouns
                                 # or likely referecned nouns
                                 first_chunk_pos=token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1:first_chunk_end_iter+1]
                                 #print("first_chunk_pos")
                                 #print(first_chunk_pos)
                                 #input() 
                                 if verb_counter<=1:
                                     # do this only for the first chunk of a sentence and first verb of sentence
                                     # dont sub out pronouns in second half of sentence
                                     for iter_pos_noun_chunk_1, posssss in enumerate(first_chunk_pos):
                                         if posssss=="PRON":
                                             # need to locate htis iter in the token_pos_list
                                             token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1:first_chunk_end_iter+1]
                                             current_poss_in_sub_list=token_pos_sub_list[first_chunk_end_iter-first_chunk_len_minus_1+iter_pos_noun_chunk_1]
                                             current_poss_in_sub_list_iter=first_chunk_end_iter-first_chunk_len_minus_1+iter_pos_noun_chunk_1
                                             #print(f"current_poss_in_sub_list {current_poss_in_sub_list}")
                                             #print('FOUND PRON')
                                             #print(posssss)
                                             #print(f"current_sent_iter {current_sent_iter}")

                                             if current_sent_iter>3:#  look back 3 at intitally 2 1 0
                                                 for minus_current_sen_iter in range(1,4):
                                                     sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)
                                                     #print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                     #print(f"proper_noun_found {proper_noun_found}")  
                                                     if proper_noun_found==True:
                                                         break                                                    
                                                 continue
                                             if current_sent_iter==2:# only look back 2  
                                                 for minus_current_sen_iter in range(1,3):
                                                     sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)  
                                                     #print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                     #print(f"proper_noun_found {proper_noun_found}")
                                                     if proper_noun_found==True:
                                                         break      
                                                 continue                       
                                             if current_sent_iter==1:# only look back 1
                                                 for minus_current_sen_iter in range(1,2):
                                                     sentence_word__sub_list,token_pos_sub_list,proper_noun_found=self.sub_proper_noun_from_pronoun(sentence_word_list,token_pos_list,current_sent_iter,minus_current_sen_iter,current_poss_in_sub_list_iter)
                                                     #print(f"sentence_word__sub_list {sentence_word__sub_list}")  
                                                     #print(f"proper_noun_found {proper_noun_found}")
                                                     if proper_noun_found==True:
                                                         break
                                                 continue                      
                                             if current_sent_iter==0:# dont look back
                                                 continue                                    
    
                                 action_segment=" ".join(sentence_word__sub_list[first_chunk_end_iter-first_chunk_len_minus_1:])# but by adding this value here hopefully will get us to the end of the chunk
                                 #print(f"action_segment {action_segment}")                                
                                 #chunk_str=chunk_str+chunk_text                                                        
                                 #print('object')
                                 #print(chunk_text1)    
                                 person_comp_info_dic_with_action_copy['action']= action_segment
                                 person_comp_info_dic_with_action_copy['object']= chunk_text1  
                                 person_comp_info_dic_with_action_copy['other_things_effected'].append(sentence_word__sub_list[chunkk_iter:])
                                 person_comp_info_dic_with_action_copy['transformations'].append(sentence_word__sub_list[first_chunk_end_iter+1:chunkk_iter])
                                 temporal_counter+=1
                                 person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
                                 person_comp_info_dic_with_action_copy["intital_page_text"]=page_text
                                 person_comp_info_dic_with_action_copy["link"]=intital_link
                                 
                                 #print('effects')
                                 #print(sentence_word__sub_list[chunkk_iter:])
                                 #print('transs')
                                 #print(sentence_word__sub_list[first_chunk_end_iter+1:chunkk_iter])
                                 #input()
                                 chunk_str=""
                                 break          
                         #print(person_comp_info_dic_with_action_copy['action'])
                         person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
                         person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                         # create action
                    else:
                         continue
        
        return person_comp_info_dic_with_action_list
    
    def get_intital_action_info_from_page_2(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """ get verbs in sentence and identify intital noun and cut from there for actions"""
        import re
        import copy
        import spacy
        import time
        from nltk.corpus import stopwords     
        cleaned_noun_chunk_list=[]
        person_comp_info_dic_with_action={         
            "action":"",
            "action_temporal_placement_in_life_list":"#",               
            ### action qualities
            "noun_and_verb_chunk_list":[],
            "noun_and_verb_chunk_pos_list":[],
            
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],

            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[], }
        
        sentence_list=[]
        sentence_word_list=[]
        iter_list=[]
        token_label_list=[]
        token_pos_list=[]
        iter_sub_list=[]
        token_sub_label_list=[]
        token_pos_sub_list=[]
        sentence_word_sub_list=[]
        entity_text_dic={}
        chunk_span_sub_list=[]       
        saved_noun_chunk_list=[]
        saved_noun_chunk_sub_list=[] 
        
        
        person_comp_info_dic_with_action_list=[]
        # clean the text       
        website_text=sel_soup.text
 
        website_text=re.sub("[\[\]{}\'\(\)]","",website_text) 
        website_text=re.sub("  ", " ", website_text)
        website_text=re.sub("-", " ", website_text)
        
        #website_text=""
        #from nltk.tokenize import sent_tokenize
        #sentences = sent_tokenize(website_text)
        #print('sentences')
        #input(sentences)
        #spacy_dic=self.label_website_text_with_spacy(website_text)
        # need to divid
        # want a verb
        finished_noun_chunk=False
        noun_chunk_segment=False
        verb_found=False
        keep_sentence=False
        keep_sentence1=False
        keep_sentence2=False
        noun_chunk=""
        transformations=""
        action_sentence=""

        person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
        temporal_counter=1
        doc = self.nlp(website_text)      
        for token in doc:
            textt=token.text
            poss=token.pos_
            #print(f"poss {poss}")
            #print(f"textt {textt}")   
            if poss=="PRON" or poss=="PROPN" or poss=="NOUN":
                #print('found first noun chunk')
                
                if finished_noun_chunk==True:
                    action_sentence+=f" {textt}"                   
                    continue
                else:
                    keep_sentence1=True
                    noun_chunk+=f" {textt}"
                    action_sentence+=f" {textt}"
                    continue
                
            if poss=="AUX" or poss=="VERB":
                #print('end of first noun chunk')# append rest of sentence
                keep_sentence2=True
                #save the verb word
                action_sentence+=f" {textt}"
                print('finished noun chunkk!!!!')
                    
                finished_noun_chunk=True
                    # merge the rest of the sentences
                transformations+=f" {textt}"
                   # then add the remainder of the sentence
                person_comp_info_dic_with_action_copy['object']= noun_chunk 
                print(noun_chunk)
                continue
                
            if finished_noun_chunk ==False and keep_sentence2==False:
                if noun_chunk=="":
                    continue
                else:
                    noun_chunk+=f" {textt}"
                    #input(f"noun_chunk {noun_chunk} ")
                    
     
            if keep_sentence1==True or keep_sentence2 ==True:
                action_sentence+=f" {textt}"
                
                
            if "." in textt:
                if keep_sentence2==False or keep_sentence1==False:
                    #print('starting new sentence add all previous after noun chunk to dictionary')
                    # clear the dictionary
                    person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                    print(f"action_sentence {action_sentence}")
                    print('fail')
                    #print(f"transformations {transformations}")
                    #print(f" noun_chunk {noun_chunk}")
                    finished_noun_chunk=False
                    noun_chunk_segment=False
                    verb_found=False
                    noun_chunk=""
                    transformations=""
                    action_sentence=""
                    keep_sentence1=False
                    keep_sentence2=False
                    continue
                    
                
            if keep_sentence2==True and keep_sentence1==True:
                if "." in textt: 
                   print('sentence end')
                   print('success')
                   print(action_sentence)
                   # save action keep the remainder of the sentence
                   person_comp_info_dic_with_action_copy['action']= action_sentence
                   person_comp_info_dic_with_action_copy['transformations'].append(transformations)
                   person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
               
                   person_comp_info_dic_with_action_copy['link']=intital_link 
                   person_comp_info_dic_with_action_copy['intital_page_text']=website_text 
                   
                   temporal_counter+=1                       
                   #print('starting new sentence add all previous after noun chunk to dictionary')
                   person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
                   # clear the dictionary
                   person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                   print(f"action_sentence {action_sentence}")
                   print(f"transformations {transformations}")
                   print(f" noun_chunk {noun_chunk}")
                   finished_noun_chunk=False
                   noun_chunk_segment=False
                   verb_found=False
                   noun_chunk=""
                   transformations=""
                   action_sentence=""
                   keep_sentence1=False
                   keep_sentence2=False
                   #input(action_sentence)
                
        return person_comp_info_dic_with_action_list
    def get_intital_action_info_from_page_3(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """ get verbs in sentence and identify intital noun and cut from there for actions"""
        import re
        import copy
        import spacy
        import time
        from nltk.corpus import stopwords     
        cleaned_noun_chunk_list=[]
        person_comp_info_dic_with_action={         
            "action":"",
            "action_temporal_placement_in_life_list":"#",               
            ### action qualities
            "noun_and_verb_chunk_list":[],
            "noun_and_verb_chunk_pos_list":[],
            
            
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],

            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[], }
        
        sentence_list=[]
        sentence_word_list=[]
        iter_list=[]
        token_label_list=[]
        token_pos_list=[]
        iter_sub_list=[]
        token_sub_label_list=[]
        token_pos_sub_list=[]
        sentence_word_sub_list=[]
        entity_text_dic={}
        chunk_span_sub_list=[]       
        saved_noun_chunk_list=[]
        saved_noun_chunk_sub_list=[] 
        
        
        person_comp_info_dic_with_action_list=[]
        # clean the text       
        website_text=sel_soup.text
 
        website_text=re.sub("[\[\]{}\'\(\)]","",website_text) 
        website_text=re.sub("  ", " ", website_text)
        website_text=re.sub("-", " ", website_text)
        website_text=re.sub("\n", " ", website_text)
        #website_text=""
        from nltk.tokenize import sent_tokenize
        sentences_list = sent_tokenize(website_text)
        #print('sentences')
        #input(sentences_list)
        #spacy_dic=self.label_website_text_with_spacy(website_text)
        # need to divid
        # want a verb
        finished_noun_chunk=False
        noun_chunk_segment=False
        verb_found=False
        keep_sentence=False
        keep_sentence1=False
        keep_sentence2=False
        noun_chunk=""
        transformations=""
        action_sentence=""
        noun_and_verb_chunk_list=[]
        noun_and_verb_chunk_pos_list=[]
        position_list=[]
        sentece_word_list_index=[]
        used_words_list=[]
        action_sentence_list=[]
        found_noun=False
        entity_text_dic={}
        
        person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
        temporal_counter=1
        for i, sentence in enumerate(sentences_list):
            sentence = self.nlp(sentence)
            proper_noun_or_pronoun_found=False
            verb_found=False
            found_noun=False
            sentence_word_list=[]  
            entity_text_dic={}
            ###ents part
            for ent in sentence.ents:
                #print(f"{ent.text},{ent.label_}")
                #print('hehe')
                textt=ent.text
                labell=ent.label_                
                if " " in textt:
                    textt_list=textt.split()
                else:
                    textt_list=[textt]
                for textt in textt_list:
                    if ent.label_ == "PERSON":
                        entity_text_dic[textt]="PERSON"
                    if ent.label_ == "ORG":
                        entity_text_dic[textt] = "ORG" 
            #input(f"entity_text_dic {entity_text_dic}")
      
            for i2,token in enumerate(sentence):
                textt=token.text
                poss=token.pos_
                #sentece_word_list_index(i2)
                
                if poss=="PRON" or poss=="PROPN":
                    proper_noun_or_pronoun_found=True  
                    noun_chunk +=f" {textt}"
                    
                    noun_and_verb_chunk_list.append(textt)
                    noun_and_verb_chunk_pos_list.append(poss)
                    position_list.append(i2)                
                    if textt in entity_text_dic:
                        sentence_word_list.append(entity_text_dic[textt])
                        #print('found one')
                    else:
                        sentence_word_list.append(poss)   
                    continue
                    
                if poss=="AUX" or poss=="VERB":
                    
                    noun_and_verb_chunk_list.append(textt)
                    noun_and_verb_chunk_pos_list.append(poss)
                    position_list.append(i2)
                    verb_found=True
                    transformations+=f" {textt}"
                    if proper_noun_or_pronoun_found==True:
                        sentence_word_list.append(textt)
                    continue
  
                if proper_noun_or_pronoun_found==True:
                    sentence_word_list.append(textt)
                

                    
                if i2==len(sentence)-1:              
                  if proper_noun_or_pronoun_found==True and verb_found==True:
                      #print(f"sentence_word_list {sentence_word_list}")
                      sentence_word_list=sentence_word_list[:16]
                      print(f" sentence_word_list {sentence_word_list}")
                      sentence_word_list= " ".join(sentence_word_list)
                      person_comp_info_dic_with_action_copy['action']= str(sentence_word_list)
                      person_comp_info_dic_with_action_copy['transformations'].append(transformations)
                      person_comp_info_dic_with_action_copy['action_temporal_placement_in_life_list']=temporal_counter 
                      person_comp_info_dic_with_action_copy['noun_and_verb_chunk_list']=noun_and_verb_chunk_list
                      person_comp_info_dic_with_action_copy['noun_and_verb_chunk_pos_list']=noun_and_verb_chunk_pos_list
                      person_comp_info_dic_with_action_copy['link']=intital_link 
                      person_comp_info_dic_with_action_copy['intital_page_text']=website_text                                      
                      temporal_counter+=1                       
                      #print('starting new sentence add all previous after noun chunk to dictionary')
                      person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action_copy)
                      
                      
                      person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
                     
                      #print(f"transformations {transformations}")
                      #print(f" noun_chunk {noun_chunk}")
                      proper_noun_or_pronoun_found=False
                      verb_found=False 
                      sentence_word_list=[]
                      noun_and_verb_chunk_list=[]
                      noun_and_verb_chunk_pos_list=[]
                      used_word_list=[]
                      position_list=[]
                      noun_chunk=""
                      transformations=""
                      action_sentence=""
                      keep_sentence1=False
                      keep_sentence2=False    
        return person_comp_info_dic_with_action_list # need to generalize actions
    
    
    def process_crawl_data_3(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page_3(sel_soup,person_comp_info_dic_with_action_list,intital_link)
        #person_comp_info_dic_with_action_list=self.order_and_divide_actions_into_action_lists(person_comp_info_dic_with_action_list)# it is filled in here so use all the qualtites to sort and divide up the adrtion
        return person_comp_info_dic_with_action_list
    
    
    def process_crawl_data_2(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page_2(sel_soup,person_comp_info_dic_with_action_list,intital_link)
        #person_comp_info_dic_with_action_list=self.order_and_divide_actions_into_action_lists(person_comp_info_dic_with_action_list)# it is filled in here so use all the qualtites to sort and divide up the adrtion
        return person_comp_info_dic_with_action_list
    
    
    def process_crawl_data(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        person_comp_info_dic_with_action_list=self.get_intital_action_info_from_page(sel_soup,person_comp_info_dic_with_action_list,intital_link)
        #person_comp_info_dic_with_action_list=self.order_and_divide_actions_into_action_lists(person_comp_info_dic_with_action_list)# it is filled in here so use all the qualtites to sort and divide up the adrtion
        return person_comp_info_dic_with_action_list
    
    
        
        
        
    def pro_OLD_cess_OLD_crawl_OLD_data(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
            """ """
            import re
            import time
            import copy
            print(f"intital_link {intital_link}")
            person_comp_info_dic_with_action={         
                "action":"",
                
                "action_temporal_placement_in_life_list":"#", 
                "noun_and_verb_chunk_list":[],
                "noun_and_verb_chunk_pos_list":[],
                ### action qualities
                "user_time_past_use_of_action_list":[],
                "user_past_actions_list":[],
                "action_geo_locations":[],
                "time_to_complete_action":0,
                "other_losses":[],
                "other_gains":[],
                "monetary_cost_of_action":0,
                "monetary_gain_of_action":0,
                "risk_of_failing":[],
                "expected_roi":[],
                "tools_needed":[],
                "legality":[],
                "action_objects":{},
                "number_of_people_impacted":[],
                "object":[],
                "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
                # run through all info in action dic to better choose actions


                "tools_required_to_perform_action":[],
                "skills_required_to_perform_action":[],
                "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
                "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
                "other_things_effected":[],
                "transformations":[], # that can be applied to action besides current 1
                "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
                "alternative_next_action_lists":[],
                "intital_page_text":[],


                "sub_steps_to_complete_actions":[] ,
                "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

                "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
             # use concepts from different fileds to rank action
               # like in _allnce or engineering or law
               # sequentally go through each action in your head, look at factors/qualtities of actions
               #then assign a score for that action
               #then based on scored actions choose an action to take
                ### guide perosnal info qualities during action 
                "organization_or_human":[],
                "age":[],
                 "height":[],
                 "date":[],
                  "birth_date":[],
                  "property":[],
                  "personalty":[],
                  "connections":[],
                  "followers":[],
                  "messages":[],
                  "skills":[],           
                  "work_experience":[],
                  "degrees":[],
                  "books_read":[],
                  "marriage_status":[],
                  "skills":[],
                  "life_actions":[],
                  "search_history":[],
                  "assets":[],# like money etc
                  "liaibities":[],
                  "glasses":[],
                  "race":[],
                  "gender":[],
                  "education":[],
                  "friends_and_there_qualities":[],
                  "employment_history":[],
                  "photo":[],
                  "pronouns":[],
                  "email":[],
                  "places_lived":[],#  geolocation as value
                  "profile_photo":[],
                  "photos":[],
                  "licenses_certificates":[],
                  "volunteering":[],
                  "skills":[],
                  "honours_and_awards":[],
                  "interests":[],
                  "groups":[],
                  "newsletters":[],
                  "about_paragraph":[],
                  "projects_worked_on":[],
                  "projects_interested_in":[],
                  "personality_type":[],
                  "family_members_and_family_members_qualities":[],
                  "phone_info_phone_numbers_contacts":[],
                  "other_social_media_info":[],
                  "phone_info_phone_numbers_contacts":[],
                  "pets":[],
                  "animals":[],
                  "money":[],
                  "plants":[],
                  "buying_history":[],
                  "selling_history":[],
                  "financial_history":[],
                  "profile_views_info":[],
                  "people_who_searched_info":[],
                  "physical_disability":[],
                  "mental_disability":[],
                  "religion":[],
                  "web_search_history":[],
                  "age":[],
                  "record_of_offenses":[],
                  "nationality":[],
                  "income":[],
                  "link":[], }
            #print(' make sure the first noun group/subject of sentence or pronoun is a person or organzaion if i do that im good or if atleast a proper noun is in the sentence ')
            #print('use qualtites from spacy in whatever way necessary to get best result so noun groups whatever works or using parsing trees')
            # edit the below at one point
            #print(' need to add in re patterns to search for if psosible for action sentneces to get better action sentences and if not do a neural net')
            #print('key is parsing action sentences let do it boys and do referential phrasing sentecnes and fix these')
            re_action_sentence_patterns_list=[".*",
                ]
            person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
            page_text=sel_soup.text
            doc = self.nlp(page_text) 
            #so alogrhim will go
            # check first noun chink
            # if noun chunk has person/org  or pronoun good 
            # else not action senetece unless
            # has a proper noun somewhere esle
            
            
            #for chunk in doc.noun_chunks:
            #    print(chunk.text, chunk.root.text, chunk.root.dep_,
            #            chunk.root.head.text)
            #for token in doc:
            #    print(token.text, token.dep_, token.head.text, token.head.pos_,
            #            [child for child in token.children])
                
                
    
            action_sentence=False 
            sentence_action_type_dic={}
            sentence=""
            counterr=0
            action_sentence_value="not action sentence"
            pos_list=[]
            pos_dic={}
            entity_text_dic={}
            #for token in doc:
            #    pos_dic.append({token.text:token.pos_})
            #    pos_list.append(token.pos_)
            for ent in doc.ents:
                #print(f"{ent.text},{ent.label_}")
                #print('hehe')
                textt=ent.text
                labell=ent.label_
                if " " in textt:
                    textt_list=textt.split()
                else:
                    textt_list=[textt]
                for textt in textt_list:
                    if ent.label_ == "PERSON":
                        entity_text_dic[ent.text]="PERSON"
                    if ent.label_ == "ORG":
                        entity_text_dic[ent.text] = "ORG"                
                    if ent.label_ == "DATE":
                        entity_text_dic[ent.text] = "DATE"
                    if ent.label_ == "MONEY":
                        entity_text_dic[ent.text] = "MONEY"         
                    continue                
            for token in doc:
                #print(token.text, token.pos_)
                # if there is pronoun in sentence
                if token.text in entity_text_dic:
                    token_label=entity_text_dic[token.text]
                    if token_label=="PERSON" or token_label=="ORG":
                        if token.pos_=="PROPN" or token.pos_=="PRON":
                            action_sentence_value="action sentence"
 
                if sentence != "":
                    sentence+=f" {token.text}"
                else:
                    sentence=f"{token.text}"  
                #if token.text=="."  # may want to change back to this one
                if "." in token.text :# will need to test htis one
                    if action_sentence_value=="action sentence":
                        for pattern in re_action_sentence_patterns_list:
                            result=re.search(pattern,sentence)
                            if result:
                                # need to remove footnotes
                                counterr+=1
                                # if scraper takes too long need to cancel it
                                #print('checking actions sentences gathered to improve process crawll data function')
                                #print(entity_text_dic)
                                sentence=re.sub(r"[\n\r]"," ",sentence)
                                sentence=re.sub(r"\s\s+","  ",sentence)
                                #sentence=sentence[:200]# may need to change this
                                sentence=sentence# may need to change this
                                #input(f"{sentence}")
                                person_comp_info_dic_with_action["action"]=sentence
                                person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=counterr
                                person_comp_info_dic_with_action["link"]=intital_link
                                person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                                # clear the dicitonary
                                person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)
                                break
                            else:
                                continue

                    sentence="" 
                    action_sentence_value="not action sentence"                           
                if token.pos_== "PRON":
                    action_sentence_value="action sentence"
                    # action sentence
                    #action_sentence=True
                    #print('hi')
                    continue
           
            print(' add this function for sub action data  to get all action space self.OLD_generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_OLD()')
            print(' self.OLD_generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_OLD()')
            print(person_comp_info_dic_with_action_list)
            input()

            return person_comp_info_dic_with_action_list
        # will reduce down the pattern space soon
        # if can ge thtis to work can get sub action to work
        # patterns to exclude or patterns to exclude which is easier
        # maybe just identify subject verb object
        # and then accept all senteces which have a specfic object we want
        # if the subhect of the sentence is something wew ant keep the sentence
        # i want the subject of the sentence to be a  person or organizaion 
        # if i can get that pattern i am good
        
        # so figure out a way to identify that
        # so first couple words in sentence need to a organizaion or person
        # so the first noun group should be a person or organizaion
        
        
        # so figure out a way to do that
        #  noun_chunks_list = [chunk.text for chunk in doc.noun_chunks]
        # so in this noun chunk should be a person or orgnaizaion
        # if proper noun at end though its fine
        # BAD Articles are intended to consist primarily of prose , though they may contain some lists .
        #Fashion activism was coined by Celine Semaan.
        # good
        # BAD Science activism may include efforts to better communicate the benefits of science or ensure continued funding for scientific research
        # maybe just swap out noun group and it works
        #print(person_comp_info_dic_with_action_list)
        #input("hi my name is jeff")
        #print(token.text)
        #print(f"sentence: {sentence}")
        #print('meow')
                                            
                        #print('for pattern in re_action_sentence_patterns_list:')
                        #print('')
                        #print('')
                        #print('if action sentnece pattern not in pattern list continue')
   
        #page_line_list=page_text.splitlines()
        #code_chunk_end_line_number_list=[]
        #temp_code_lines_in_code_chunk=[]
        #temp_code_chunk=""
        #last_page_line_type="text"
        #for page_line_number,page_line_text in enumerate(page_line_list):
        #    non_space_match=re.search(non_space_matcher,page_line_text) 
    def list_python_and_other_files_in_dir(self,dir_to_start_walk):
        """ """
        import os
        python_file_list=[]
        other_file_list=[]
        repo_read_me_file_list=[]
        for (root,dirs,files) in os.walk(dir_to_start_walk, topdown=True):
                if files:
                    for file in files:
                        if  file=="README.md":
                           #print('meow')
                            repo_read_me_file=root +"\\" +file
                            repo_read_me_file_list.append(repo_read_me_file)
                            continue
                        file_endding=file[-3:]
                        if file_endding==".py":
                            path_to_python_file=root +"\\" +file
                            python_file_list.append(path_to_python_file)
                            continue
                        else:
                            path_to_python_file=root +"\\" +file
                            other_file_list.append(path_to_python_file)
                            continue
                            
        return python_file_list, repo_read_me_file_list,other_file_list
    def get_coding_file_info(self,coding_file_name,coding_file_dic,repo_name):
        """this function takes a coding file and divdes it into its line of code then organizes it so we can constrcut prompts to ask chatgpt or any generative model"""
        import re
        import time
        time_stamp = time.time()
        saved_class_line=""
        saved_function_line=""
        python_code_line_list=[]
        stored_glossary_code_dic={}
        whole_functions_dic={}
        find_code_imports = re.compile(r"[a-zA-Z]+\.[a-zA-Z_]+")
        function_number_list_for_in_line_code={}
        package_to_describe=re.compile(r"\(.*?\)")
        with open(rf"{coding_file_name}", "r",encoding="utf8") as f:
            coding_file=str(f.read())
        python_script_split_lines=coding_file.splitlines()
        function=False
        # first run to get whole functions
        for line_number,line in enumerate(python_script_split_lines):
            docstring=""
            function_str_test=line.strip()
            function_search=False
            if function_str_test[:3]=="def":
                function_search=True   
            #function_search=re.search(r"[\s\t]+def .*:",line)
            if function_search:
                saved_function_name_line=line
                current_function_lines=f"{line}\n"
                function=True
                continue
            if function==True:
                current_function_lines+=f"{line}\n"
                whole_functions_dic[saved_function_name_line]=current_function_lines
        for line_number,line in enumerate(python_script_split_lines):
            line_number= line_number +1
            class_function_str_test=line.strip()
            function_search=False
            if class_function_str_test[:5]=="class":
                saved_class_line=line
                continue 
            if class_function_str_test[:3]=="def":
                function_search=True 
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
                    if whole_functions_dic[saved_function_name_line] in coding_file_dic["code_base_function"]:
                        continue
                    else:
                        final_code_lines_in_code_chunk=[]
                        class_name_search=re.search(r"([a-zA-Z_0-9]+)\(.*\)",saved_class_line)
                        code_lines_in_code_chunk=re.findall(find_code_imports,whole_functions_dic[saved_function_name_line])
                        for code_line in code_lines_in_code_chunk:
                            if "self." in code_line:
                                if class_name_search:
                                    class_name=class_name_search.group(1)+"."
                                    code_line=re.sub("self\.",class_name,code_line)
                                else:
                                    code_line=re.sub("self\.",saved_class_line,code_line)
                            final_code_lines_in_code_chunk.append(code_line)
                        input_dic={"code_lines_in_function":final_code_lines_in_code_chunk, 
                            "code_base_function": whole_functions_dic[saved_function_name_line],
                            "class_name":saved_class_line,
                            "time_stamp":time_stamp,
                            "pypi_file_name":coding_file_name,
                            "line_number_in_file":line_number,
                            "pypi_doc_name":repo_name
                            }
                        coding_file_dic=self.add_uniform_data_to_dictionary(coding_file_dic,input_dic)

                        #coding_file_dic["code_lines_in_function"].append(final_code_lines_in_code_chunk)
                        #coding_file_dic["code_base_function"].append(whole_functions_dic[saved_function_name_line])
                        #coding_file_dic["pypi_file_name"].append(coding_file_name)
                        #coding_file_dic["class_name"].append(saved_class_line)
                        #coding_file_dic["line_number_in_file"].append(line_number)
                        #coding_file_dic["time_stamp"].append(time_stamp)
                        
        return coding_file_dic
    def open_selenium(self,link): # will need to moidfy this to use a different generative model
        """ access chatgpt using an intital prompt a path to store the information and a indicatory of a unique value to give the pickle file"""
        import re
        import requests
        import pickle
        import os
        from selenium import webdriver
        from bs4 import BeautifulSoup
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import time
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        cwd = os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Pickles") 
        FirefoxOptions = FirefoxOptions()
        FirefoxOptions.add_argument("--headless")
        #chrome_options.headless = True # also works

        driver= webdriver.Firefox(options=FirefoxOptions)
        session = requests.Session()
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept':'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/webp,*/*;q=0.8'}
        try:
            driver.get(link) #the pages link must be inserted here
        except:
            driver.quit()
        return driver, session, headers
    def retreive_glossary_data_from_web(self, web_prompt,driver, session, headers):
        """ get the glossary data from duck duckgo page and retrieve all the html"""
        # we want to make this only retrive the top 3 search results or links
        from selenium import webdriver
        from bs4 import BeautifulSoup
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import time
        links_of_dif_docs=[]
        saved_link_list=[]
        saved_text_from_websites_and_link_dic={}
        content = driver.find_element(By.CLASS_NAME, 'search__input')
        content.send_keys(f"{web_prompt}")
        content.send_keys(Keys.ENTER)
        time.sleep(2)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html= driver.execute_script("return document.documentElement.outerHTML")
        sel_soup = BeautifulSoup(html, 'html.parser')
        links_of_dif_docs= sel_soup.findAll("a") 
        if links_of_dif_docs:
            for link_found in links_of_dif_docs:
                try:
                    if link_found:
                        final_link=link_found.get('href')
                        if final_link not in saved_link_list:
                            if final_link:
                                if "https" in final_link:
                                    
                                    if len(saved_link_list)>4:
                                        # limit this to five
                                        break
                                    saved_link_list.append(final_link)
                                else:
                                    continue
                except Exception as e:
                   #print(e)
                    continue
            for link_finals in saved_link_list:
                try:
                    req = session.get(link_finals, headers=headers)
                    soup = BeautifulSoup(req.text)
                    p_tag_text=soup.get_text()
                    saved_text_from_websites_and_link_dic[link_finals]=str(p_tag_text)
                
                except Exception as e1:
                   #print(e1)
                    continue
            driver.quit()
            return saved_text_from_websites_and_link_dic
        
    def pre_process_text(self,website_text):
        """ remove extra spacing, names, tabs, and other unwanted values"""
        import re
        import unicodedata
        import copy
        website_data= re.sub("\n"," ", website_text)
        website_data= re.sub("\t"," ", website_data)
        website_data= re.sub("\r"," ", website_data)
        website_data=re.sub(r" \s+", r" ", website_data)
        website_data= re.sub(r"\\x\S+",r" ",website_data )
        website_data= re.sub(r"@", "",website_data)
        website_data= unicodedata.normalize("NFKD",website_data)
        return website_data
       
    def remove_short_and_long_sentences_and_create_sentence_list(self,website_data):
         """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
         from nltk.tokenize import sent_tokenize
         import re
         website_text=""
         website_text_sentence_list=[]
         word_num_pattern=re.compile(r"[^a-zA-Z0-9,; ]*")
         find_word_pattern = re.compile(r"\w+")
         #from nltk.tokenize import word_tokenize
         modifying_sentences = sent_tokenize(website_data)
         for i7, sentence_15 in enumerate(modifying_sentences):
             words_in_current_sentence=find_word_pattern.findall(sentence_15)
             if len(words_in_current_sentence)<4: 
                 #print(sentence_15)
                 continue
             if len(words_in_current_sentence)>60: 
                 #print(sentence_15)
                 continue
             if "https" in sentence_15:
                 #print(sentence_15)
                 continue
             else:
                 sentence_15=re.sub(word_num_pattern,"",sentence_15)
                 website_text+= sentence_15+ " "
                 website_text_sentence_list.append(sentence_15)
                 
         return website_text,website_text_sentence_list
     
    def label_text_with_spacy(self,website_text): 
         """ generate spacy information for a sentnece"""
         import spacy
         sentence=website_text.replace("?","").replace(",","")
         if self.spacy_switch==0:
             self.nlp = spacy.load("en_core_web_sm")
             self.spacy_switch=1
             #https://github.com/explosion/spaCy/issues/12659
             #python -m pip install -U pydantic spacy
             #python -m spacy download en_core_web_sm

         doc = self.nlp(sentence)
         noun_chunks = [chunk.text for chunk in doc.noun_chunks]
         entities = [(ent.text, ent.label_) for ent in doc.ents]
         sentences = [sent.text for sent in doc.sents]
         lemmatized_tokens = [token.lemma_ for token in doc]
         pos_tags = [(token.text, token.pos_) for token in doc]
         return {
             "noun_chunks": noun_chunks,
             "entities": entities,
             "sentence": sentence,
             "lemmatized_tokens": lemmatized_tokens,
             "pos_tags": pos_tags}
    def get_nouns_and_verb_counts_in_web_text_retrieved(self,spacy_dic,noun_verb_dic_counts):# this can apply formula we are looking for
         """this will create a new list of questions from an orignal quesiton by changing the first verb of the sentence"""
         wanted_pos_list=["VERB","NOUN","PROPN"]
         for i2, word_tag in enumerate(spacy_dic["pos_tags"]):# skip how do i is why we start at 3 
             word=word_tag[0]
             pos=word_tag[1]
             if pos in wanted_pos_list:
                 if word in noun_verb_dic_counts.keys():
                     noun_verb_dic_counts[word]+=1
                 else:
                     noun_verb_dic_counts[word]=1
         return noun_verb_dic_counts
    def find_highest_count_words(self,noun_verb_dic_counts):
         """ find sentences with highest count of words and use this in create final paragraph to seperate paragraphs we want to keep vs we dont want to keep """
         final_noun_verb_dic_to_keep={}
         glossary_word_count_list=list(noun_verb_dic_counts.values())
         glossary_word_count_list_len=len(glossary_word_count_list)
         #sort the dictionary
         percentage_to_keep_in_list=round(glossary_word_count_list_len*50/100)# 80 percent # may need to change tis value
        #print(percentage_to_keep_in_list)
         glossary_word_count_list.sort(reverse = True)
         glossary_word_count_list_cut=glossary_word_count_list[percentage_to_keep_in_list:]
         value_to_cut_on=glossary_word_count_list_cut[-1]
         for word,word_count in noun_verb_dic_counts.items():
             if word_count>value_to_cut_on:
                 final_noun_verb_dic_to_keep[word]=word_count
         return final_noun_verb_dic_to_keep
                     
 
    def create_final_glossary_paragraph(self,final_noun_verb_dic_to_keep,final_web_sentence_list):
        """ create final glossary paragraph"""
        final_sentence_list_temp=[]
        for sentence1 in final_web_sentence_list: 
            for word,word_count in final_noun_verb_dic_to_keep.items():
                if word in sentence1:
                    final_sentence_list_temp.append(sentence1)
                    break  
        glossary_paragraph=" ".join(final_sentence_list_temp)
        return glossary_paragraph 
    
    def create_words(self,words_string):
           """ creates a list of words splitng on spaces"""
           import re
           words_string= re.sub(r"\s\s+",r" ", words_string )
           words_list=words_string.split(" ")
           return words_list
  

    
    
        
        
        
    def duckduckgo_grab_searched_sites_html(self,glossary_prompt,queue_value_to_return):
        """ """
        glossary_word_count_list_of_words_we_want={}
        saved_text_from_websites_and_link_dic_temp={}
        website_dic={}
        website_dic["website_links"]=""
        website_dic["website_paragraphs"]=""       
        driver, session, headers=self.open_selenium(r"https://html.duckduckgo.com/html/")
        saved_text_from_websites_and_link_dic=self.retreive_glossary_data_from_web(glossary_prompt, driver, session, headers) 
        if queue_value_to_return!="":
            queue_value_to_return.put(saved_text_from_websites_and_link_dic)
        else:
            return saved_text_from_websites_and_link_dic
        
   # def process_crawl_data(self,html,data_retrieved_dic,pypi_doc_name,file_name=None):
   #     """ what crawl data do we want and how are we going to store it"""
    #    data_retrieved_dic,code_chunk_end_line_number_list,page_line_list=self.process_crawl_data_generate_function_list(html,data_retrieved_dic,pypi_doc_name,file_name=file_name) 

     #   data_retrieved_dic=self.process_crawl_data_generate_glossary(data_retrieved_dic,code_chunk_end_line_number_list,page_line_list,file_name=None) 
      #  return data_retrieved_dic

    def get_text_file_glossary_info(self,read_me_file, coding_file_dic,repo_name):
        """ """
        # need to modify this slightly
        with open(read_me_file,"r")as f:
            text=f.read()
        coding_file_dic=self.process_crawl_data(text,coding_file_dic,repo_name,file_name=read_me_file)
        return coding_file_dic

    def check_site_does_not_block_requests(self,link):
         """ this will sned a request to a website and see if all the content is rendered when the request is sent and not stopped by javascript if it is stopped by javascript it will return false else true """
         html,session=self.download_link_html_requests(link)
         # what indicator would be the text is above a certain length   
    def init_sql(self):
        """ """
        import psycopg2
        import torch
        import numpy as np
        #from  Pos_model_trainer import network
        super().__init__()
        self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        return 1
    def create_pypi_table(self):# still need to do this
        """ the columns that go into the pypi table given the data we are gathering"""
        column_name_data_type_dic={"glossary_definiton":"text",
                                    "line_of_code":"text",
                                    "code_base_function":"text",
                                    "code_file_name":"text",
                                    "glossary_website":"text",
                                    "class_name":"text",
                                    "line_number_in_file":"BIGINT",
                                    "commented_function":"text",
                                    "docstring":"text",
                                    "time_stamp":"FLOAT",
                                    "glossary_definition_gpt":"text"
                                   }
        self.create_table_sql(column_name_data_type_dic,table_name="pypi_table")  
    def create_intital_link_seed_list_pickle(self):
        """
        https://www.wikidata.org/wiki/Wikidata:Main_Page
        https://query.wikidata.org/#SELECT%20%3Fperson%20WHERE%20%7B%20%3Fperson%20wdt%3AP31%20wd%3AQ5%20%7D%0Alimit%20100%0A
        
        https://query.wikidata.org/ # get all info off of this for additonal stats
        then query wiki to get actions 
        https://en.wikipedia.org/wiki/Wikipedia:Contents/People_and_self
        https://en.wikipedia.org/wiki/List_of_Germans
        
        https://en.wikipedia.org/wiki/Lists_of_people_by_occupation
        https://en.wikipedia.org/wiki/Lists_of_people_by_nationality
        https://en.wikipedia.org/wiki/Khassan_Baiev
        
        https://en.wikipedia.org/wiki/Lists_of_people_by_occupation
        
        https://en.wikipedia.org/wiki/Wikipedia:Contents/People_and_self#Lists
        https://en.wikipedia.org/wiki/Category:Activists
        
        https://en.wikipedia.org/wiki/Lists_of_people_by_nationality
        https://en.wikipedia.org/wiki/Lists_of_people_by_belief
        
        https://en.wikipedia.org/wiki/Lists_of_people_by_occupation
        
        # create my own categories sort of?
        # because maybe activst may have taken an action that would make money
        # or musician
        # use the search to sort actions using context in objective against other context
        
        # divide people by birth year as well
        
        # maybe look at actions of organizations too 
        
        # make a organization search and incprorate htis in?
        https://en.wikipedia.org/wiki/Category:Organizations
        https://en.wikipedia.org/wiki/Category:Organizations_by_subject_and_date_of_establishment
        https://en.wikipedia.org/w/index.php?title=Category:Organizations_by_year_of_establishment&subcatfrom=1783%0AOrganizations+established+in+1783#mw-subcategories
        
        https://en.wikipedia.org/wiki/Wikipedia:Contents/Categories
        
        # this for making most money objective
        https://en.wikipedia.org/wiki/List_of_entrepreneurs
        https://en.wikipedia.org/wiki/List_of_Internet_entrepreneurs
        https://en.wikipedia.org/wiki/Lists_of_people_by_net_worth
        
        # this for helping the most people objective
        https://en.wikipedia.org/wiki/Lists_of_activists
        https://en.wikipedia.org/wiki/List_of_civil_rights_leaders
        https://en.wikipedia.org/wiki/Category:Internet_activists
        https://query.wikidata.org/ 
        https://en.wikipedia.org/wiki/Special:Statistics
        # get all the peoples data by year
        # then get 
        Do the query of wiki data then grow from there
        using the other links
        #just crawl the above link and grab all the data and parse it
        
        scrape linekdin data
        how to get intital list of people
        
        
        # maybe just look at peoples lives
        
        """
        path_to_pickle=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Pickles\intital_link_seed_list.pickle"
        
        links_to_pypi_packages=[]
        # stilln eed to write this
        
        self.create_pickle(path_to_pickle,links_to_pypi_packages)      
        return links_to_pypi_packages
        #self.delete_table_sql(table_name="pypi_table")  
   
        #html=self.command_selenium_grab_page_info_pypi(driver)
        #link_link_category_dic=self.process_html_to_find_link_pypi(html)
        #link_link_category_dic=self.categorize_links
    #def web_crawl_selenium(self,link,pattern_list):
    #    """ """
    #    self.command_selenium_grab_page_info_pypi()
    #      
    #   #print('meow')
   
                 
    def download_and_find_github_repo_info(self,link,coding_file_dic):
        """crawl the whole site and store the information by dividing out code found and information realted to code if possible versus entire package """
        import subprocess
        import os
        import re
        dir_to_repo=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Music"
        os.chdir(dir_to_repo)
        git_repo_command=["git", "clone",link]
        subprocess.run(git_repo_command)
        repo_component_list=re.findall("/([a-zA-Z.]+)",link)
        repo_name=rf"\{repo_component_list[-1]}"
        dir_to_start_walk=dir_to_repo+repo_name
        python_file_list,repo_read_me_file_list, other_file_list=self.list_python_and_other_files_in_dir(dir_to_start_walk)

        if repo_read_me_file_list:
            for read_me_file in repo_read_me_file_list:
               #print(read_me_file)
                coding_file_dic=self.get_text_file_glossary_info(read_me_file,coding_file_dic,repo_name)
                # this needs to be first because of how we strcutred process information which relies on having a empty dictionary to start
        for python_file in python_file_list:
            coding_file_dic=self.get_coding_file_info(python_file,coding_file_dic,repo_name)                                                
        return coding_file_dic # fix results for this now so all the box are lines up

    def web_crawl_requests(self,intital_link,website_root,clean_link_root,person_comp_info_dic_with_action_list,used_link_list,wait_for_process_finish_list,wait_for_dic_creation_to_finish=False,current_process_number=0):# crawl the whole site and store the 
        """ crawl the whole site and store the information by dividing out code found and information realted to code if possible versus entire package"""
        import requests
        import re 
        import pickle
        from subprocess import Popen, PIPE, STDOUT
        from bs4 import BeautifulSoup
        add_page_to_action_dic=True
        if intital_link in used_link_list:
            return used_link_list, person_comp_info_dic_with_action_list
        used_link_list.append(intital_link)
        pattern_list=[]
        # this terms_not_in_link_list is the categories links that i will not get action data from
        # but will tretrieve links from using retrive links on page and then crawl
        # need to add a re pattern here
        terms_not_in_link_list=["/wiki/Category:","/wiki/List","/wiki/Lists","w/index.php?title=Category",
                                "/w/index.php?title=Lists","Wikipedia:Categories","WikiProject_List",
                                "Template:","User:","Wikipedia:List_of_","/User_talk:",
                                "Wikipedia:Featured_lists","Wikipedia:Featured_list",
                                "Wikipedia:Maintenance","wiki/Wikipedia:"
                                ,"Wikipedia_talk:","Template_talk:","wiki/Portal:","Federated_state"
                                ]  
        
        if "/wiki" in intital_link:# may need to check this so can get more links but keep this for now
        #if "wiki" in intital_link: 
            html,session=self.download_link_html_requests(intital_link)
        else:
            return used_link_list,person_comp_info_dic_with_action_list
        sel_soup = BeautifulSoup(html, 'html.parser') 
        body_page=sel_soup.find('div', id="bodyContent")
        
        add_page_to_action_dic=True
        #search_result=re.search("wiki/",intital_link)
        #if search_result:
        #    add_page_to_action_dic=False
            
        for termm in terms_not_in_link_list:           
            if termm in intital_link:
                add_page_to_action_dic=False
                break 
        if add_page_to_action_dic==True:    
            #if link_type=="person_and_org_word_in_link":
                print(intital_link)
                #print("this link we will run the process crawl data on")
                print('processing page')
                current_process_number+=1
                print(f"current prcoessign number {current_process_number} ")
                #if link is person or organizaion then process the link:
                person_comp_info_dic_with_action_list=self.process_crawl_data_3(sel_soup,person_comp_info_dic_with_action_list,intital_link) 
                #print('checking actions sentences gathered to improve process crawll data function')
                #input(f"{person_comp_info_dic_with_action_list}")
                picklee=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api\person_comp_info_dic_with_action_list.pickle"
                with open(picklee,"wb") as f19:
                           pickle.dump(person_comp_info_dic_with_action_list, f19, pickle.HIGHEST_PROTOCOL)
                p = Popen(["python",r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api\fill_and_save_dic_without_spacy_processing.py'])
                print('you can remove this on a bigger computer but right now crashes unless i keep communicate here so dont remove it so it only runs 1 because seems to crash from not enough ram for selenium')
                print('seems ram issue only going to fix it by running on another computer with nmore ram give up for now ')
                out, err = p.communicate()# this only allows one process to run at ocne but we can monitor it
                print(f"{out}, {err}")
                if wait_for_dic_creation_to_finish==True:
                    print('we have been stopped')
                    return_code = p.wait()
                #print(f"Process finished with exit code: {return_code}")
                #self.fill_single_website_action_dic_list_and_save_to_table(person_comp_info_dic_with_action_list)
                person_comp_info_dic_with_action_list=[]
                # website by page to table and fill dic in one sec  
                # want to exclude certain links from being processed  in web crawler
               
                 
           #
                        
        link_retrieved_dics=self.retrieve_links_on_page(body_page,website_root,intital_link,used_link_list)
       #print(used_link_list)
       # need to changew how i am doing the wait_for_process_list
       # only ever run 4 at a time
       # will change enveutally       
        for  link5, link_type_list in  link_retrieved_dics["link_none_dic"].items():
            if  current_process_number in wait_for_process_finish_list:
                wait_for_dic_creation_to_finish=True
                print('stopp is true')
            else:
                wait_for_dic_creation_to_finish=False
                print('stopp is false')
                
            if link5 in used_link_list:# need to check if used link is working
                continue
            else:
                used_link_list,person_comp_info_dic_with_action_list=self.web_crawl_requests(link5,website_root,intital_link,person_comp_info_dic_with_action_list,used_link_list,wait_for_process_finish_list,wait_for_dic_creation_to_finish=wait_for_dic_creation_to_finish,current_process_number=current_process_number)
                continue
        return used_link_list,person_comp_info_dic_with_action_list
    #print(person_comp_info_dic_with_action_list)
    # make it so it will not conitnue forever
    
    # so we atleast save results every maybe
    # maybe each page we go on will save to table 
    # so that way we are good and dont lost all the data
    # and add the thing where we dont go to links we already have saved
    # in the table
    # so add these two things in and this will fix everything
    
    
    
    #input()
    #print(link_retrieved_dics["link_none_dic"])
    #print('THIS IS TEMPORARY to test database upload')
    #continuee=True
    #print(intital_link)
    #print('THIS IS TEMPORARY to test database upload')
    #return used_link_list,person_comp_info_dic_with_action_list  
    #input("this is the none dic and info for running web crawl 1 time through")  

  
    def generate_glossary_duck_duck_go(self,repo_name,data_retrieved_dic,multiprocess=False):
        """ WILL NEED TO REMEMBBER TO MAKE SEARCHES BETTER FOR CODE LINES WITH MORE CONTEXT% LIKE PACKAGE NAME ETC"""
        from multiprocessing import Process, Queue
        queue_value_to_return=""
        if multiprocess==True:# code lines still need to write this correctly
            glossary_word_count_list_of_words_we_want={}
            saved_text_from_websites_and_link_dic_temp={}
            if __name__ == '__main__':
                prompt_data=self.change_create_glossary_promp_using_pypi_data(data_retrieved_dic)# still need to write this once probably modfying the below function
                #full_glossary_prompt
                #coding_file_dic_without_used_values_list_with_glossary=self.create_glossary_prompt_tkinyer_sub(data_retrieved_dic,full_glossary_prompt)
                #glossary_code_dic_len=len(coding_file_dic_without_used_values_list_with_glossary)
                code_line_list=[]
                list_of_values_to_stop_at=list(range(6,code_line_list,6))
                for i3,coding_line_information_with_prompt in enumerate(code_line_list):
                        queue_value_to_return = Queue()
                        p = Process(target=self.duckduckgo_grab_searched_sites_html(), args=(queue_value_to_return,))
                        p.start()
                        saved_text_from_websites_and_link_dic=queue_value_to_return.get() 
                        for website_link, website_text in saved_text_from_websites_and_link_dic.items():
                            data_retrieved_dic=self.process_crawl_data_3(website_text,data_retrieved_dic,repo_name)
                        if i3 in list_of_values_to_stop_at:
                            p.join() 
                return data_retrieved_dic    
        if multiprocess==False: #packages 
            full_glossary_prompt=f"what is the purpose of the the python package {repo_name}  "
            saved_text_from_websites_and_link_dic=self.duckduckgo_grab_searched_sites_html(full_glossary_prompt,queue_value_to_return)
            for website_link, website_text in saved_text_from_websites_and_link_dic.items():
                data_retrieved_dic=self.process_crawl_data(website_text,data_retrieved_dic,repo_name,file_name=website_link)
            return data_retrieved_dic
       
    def search_on_github_for_package_implementation(self,repo_name,data_retrieved_dic,multiprocess=False):# also search for package repo if possible
         """ copy everything we create for intital github search and build on it"""
         # we are going to auto email and account creation first 
         # and see if we can beat capcha as well
         # then we will finish this
         
         
         #then can integrate them all into tkinyer application
         # can edit this so can use same function for live api search of github
         # or very similar same with code lines or chatgpt or glossary search
         self.open_selenium(link)
         self.get_coding_file_info(coding_file_name,coding_file_dic,repo_name)
         self.search_on_github_for_package_implementation(data_retrieved_dic)
         data_retrieved_dic=self.process_crawl_data(website_text,data_retrieved_dic,repo_name,file_name=website_link)

        
         
    def search_on_github_for_code_line_implementation(self):
        """ copy everything we create for intital github search and build on it"""
        self.open_selenium(link)
        self.get_coding_file_info(coding_file_name,coding_file_dic,repo_name)
        self.search_on_github_for_package_implementation(data_retrieved_dic)
        data_retrieved_dic=self.process_crawl_data(website_text,data_retrieved_dic,repo_name,file_name=website_link)

           
    def search_copilot_and_chatgpt_for_package_info(self):
         """we will use our pyautogui and other code we wrote for this and import it  """
         data_retrieved_dic["glossary_crawl"].append(pypi_doc_name)
         data_retrieved_dic["glossary_duck"].append(saved_class_line)
         data_retrieved_dic["glossary_git"].append(line_number)
         data_retrieved_dic["time_stamp"].append(time_stamp)
         data_retrieved_dic["glossary_gen"].append(time_stamp)    
         if __name__ == '__main__':
             import sys
             import re
             import time
             import psycopg2
             from multiprocessing import Process
             sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_for_generative_model_access a1.1.1.1.1.1')
             from pyautogui_for_generative_model_access_functions import pyautogui_for_generative_model_access_functions
             from pyautogui_for_generative_model_access_functions import pyautogui_for_generative_model_access_functions_child
             from pyautogui_for_generative_model_access_functions import pyautogui_for_generative_model_access_functions_gchild
             pyauto=pyautogui_for_generative_model_access_functions()
             pyautoc=pyautogui_for_generative_model_access_functions_child()
             # we will need to use the pyautogui to create the scraping of chatgpt
             
    def retreive_data_from_web_pypi(self,link,search_type="repo"):
           """ get the glossary data from duck duckgo page and retrieve all the html"""
           import re
           used_link_list=[]
           # store the packages name get it from the intital page
           repo_component_list=re.findall("/([a-zA-Z.]+)",link)
           repo_name=rf"{repo_component_list[-1]}"
           if search_type=="repo":
               pattern_list=[r"Homepage",r"Documentation"]
               
               data_retrieved_dic={
               "code_lines_in_function": [], 
               "code_base_function": [],
               "pypi_doc_name":[] , 
               "glossary_crawl":[],
               "glossary_duck":[],
               "glossary_git":[],
               "glossary_gen":[],    
               "time_stamp":[],
               "pypi_file_name":[],
               "line_number_in_file":[],
               "class_name":[],
               }
               documentation_and_homepage_link_dic={}
               html,session=self.download_link_html_requests(link)
               pypi_package_info_dic=self.get_pypi_package_info(html)# this will have package name etc
               link_pattern_dic__with_none,link_pattern_dic_only_pattern_list_values_list,link_pattern_dic_only_pattern_list_values_single=self.retrieve_links_on_page(html,pattern_list=pattern_list)
               for link3, link_type_list in  link_pattern_dic_only_pattern_list_values_single.items():
                   link_root=re.search(r"https://(.*\..*)/",link3)# need to test this
                   link_root=link_root.group(1).replace(r".","\.")
                   clean_link_root=link_root.replace("\\","")
                   link_type=link_type_list[0]# we will have to test to see if this is working correctly
                   if "github" in link:
                       coding_file_dic=self.download_and_find_github_repo_info(link,data_retrieved_dic)   
                   else:
                       used_link_list, self.data_retrieved_dic=self.web_crawl_requests(link3,link_root,clean_link_root,data_retrieved_dic,used_link_list,wait_for_process_finish_list) # crawl the whole repo site  
                   data_retrieved_dic=self.generate_glossary_duck_duck_go(repo_name,data_retrieved_dic,multiprocess=False)
                   data_retrieved_dic=self.search_on_github_for_package_implementation()                
                   data_retrieved_dic=self.search_copilot_and_chatgpt_for_package_info()# this will use the pyautogui script
                   #data_retrieved_dic[link_type]=[repo_web_crawl_data,duck_duck_go_data,git_hub_imps_founds,copilot_chat_gpt_data]
               return data_retrieved_dic
           
           if search_type=="code_line":
               data_retrieved_dic={
               "code_lines_in_function": [], 
               "code_base_function": [],
               "pypi_doc_name":[] , 
               "glossary_crawl":[],
               "glossary_duck":[],
               "glossary_git":[],
               "glossary_gen":[],    
               "time_stamp":[],
               "pypi_file_name":[],
               "line_number_in_file":[]
               }
               repo_web_crawl_data=[]
               duck_duck_go_data=self.generate_glossary_duck_duck_go(table_name="pypi_code_line")
               git_hub_imps_founds=self.search_on_github_for_code_line_implementation()                
               copilot_chat_gpt_data=self.search_copilot_and_chatgpt_for_package_info()# this will use the pyautogui script
               data_retrieved_dic[link_type]=[repo_web_crawl_data,duck_duck_go_data,git_hub_imps_founds,copilot_chat_gpt_data]
               return data_retrieved_dic
           
            
        
    def github_and_pypi_info_search_and_download(self):
        """build a script to download all of pypi """
        column_list_pypi_repo=["line_of_code","code_file_name","line_number_in_file","link_to_repo"]
        column_list_pypi_code_line=["line_of_code","code_file_name","line_number_in_file","link_to_repo"]
        pypi_link_repo_pickle_list=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Pickles\pypi_link_repo_list"
        pypi_links=self.upload_pickle(pypi_link_repo_pickle_list)
        pypi_last_uploaded_repo_code_line_dic=self.upload_pickle(pypi_link_repo_pickle_list)
        last_repo_uploaded=list(pypi_last_uploaded_repo_code_line_dic.keys())[0]
        last_uploaded_repo_code_line_list=pypi_last_uploaded_repo_code_line_dic[last_repo_uploaded]
        glossary_prompt=""
        current_pypi_repo_data=self.upload_sql_values(column_list_pypi_repo)
        pypi_repo_data_dic=self.process_sql_data_for_searches(current_pypi_repo_data)
        saved_pypi_repo_link_list=pypi_repo_data_dic["pypi_link"]
        current_pypi_code_line_data=self.upload_sql_values(column_list_pypi_code_line)
        pypi_code_line_dic=self.process_sql_data_for_searches(current_pypi_code_line_data)
        saved_pypi_code_line_list=pypi_code_line_dic["code_lines"]
        for link_to_repo in pypi_links:
            if link_to_repo in saved_pypi_repo_link_list:
                if link_to_repo==last_repo_uploaded:
                    dictionary_with_only_row_with_link_to_repo=self.get_values_associated_with_value_found_in_key(pypi_code_line_dic,link_to_repo,column_list_pypi_code_line, column_name="link_to_repo")
                    current_uploaded_code_lines_list_in_sql=dictionary_with_only_row_with_link_to_repo["code_lines"]
                    for code_line2 in last_uploaded_repo_code_line_list:
                        if code_line2 in current_uploaded_code_lines_list_in_sql:
                            continue
                        else:
                            pypi_web_search_data=self.retreive_data_from_web_pypi(code_line2,search_type="code_line")
                            dictionary_to_upload_to_pypi_code_line=self.process_pypi_code_line_search_data(pypi_web_search_data)
                            self.store_value_in_sql_table(dictionary_to_upload_to_pypi_code_line,"pypi_code_line") # glossary data will be stored in each table
                    continue                    
                else:
                    continue
                # will need to test this in building # this might make the program too slow will need to test it
            else:
                pypi_web_search_data=self.retreive_data_from_web_pypi(link_to_repo,search_type="repo")
                dictionary_to_upload_to_pypi_repo=self.process_pypi_package_search_data(pypi_web_search_data)
                self.store_value_in_sql_table(dictionary_to_upload_to_pypi_repo,"pypi_repo")
                repo_code_lines_list=dictionary_to_upload_to_pypi_repo["code_lines"].split("@@")
                self.create_pickle(self,r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Pickles\last_uploaded_repo_code_lines.pickle",repo_code_lines_list)
                for code_line3 in repo_code_lines_list:
                    if code_line3 in saved_pypi_code_line_list:
                        continue
                    else:
                        pypi_web_search_data=self.retreive_data_from_web_pypi(code_line3,search_type="code_line")
                        dictionary_to_upload_to_pypi_code_line=self.process_pypi_code_line_search_data(pypi_web_search_data)
                        self.store_value_in_sql_table(dictionary_to_upload_to_pypi_code_line,"pypi_code_line") # glossary data will be stored in each table
                
    
                    
                    #deal with pypi repo code lines
                    # assume th
                    
    def use_all_finance_related_sas_apps_and_load_content(self):
        """ """
    
        
    def automatically_keep_growing_and_adding_ideas_and_functions_like_these_to_psp(self):
        """  funcitons like the ideas that i have come up with above like finance model"""
    def find_all_possible_grants_and_investments(self):
        """ """
    def tax_accounting_program(self):
        """ """
    def auto_generate_and_improve_prompts_model_and_automatically_train_and_build_other_models(self):
        """ will automcially send prompts to other model look at results and improve its promps
        it will also train and test different models to get proper results will need
        to have a objective function to improve it
        will look at all avialable modles and test and change model being used
        use while loop
        self training system using internet
        check newest journal articles and build models
        and newest articles always to keep up to date
        https://en.wikipedia.org/wiki/List_of_military_strategies_and_concepts
        in all fields
        like war or video games"""
    def fix_relationships_heal_relationships_tips(self):
        """ """
    def extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate(self):
        """# for example think roi in finance or final product like prospectus
        #extract from books qualtiies or concepts related to professions that i could generate
        #and final products could build in the professions 
        also extract ideas like different ideas of how people behave
        and there methods so you can get there effects
        like knowing about journalism"""
        
        
    def combine_all_concepts_tools_and_info_from_other_field_into_current_field(self):
        """ find all cocnepts in other fiedls and things you coudl use and apply to current problem or field"""
        
    def client_list_finder_creator_and_contacter(self):
        """ find the client list for the prospective company and contact these indivduals
        and get them to invest in the business generating relevnet marketing documents
        or buy the product"""
    def find_other_business_methods_successful_business_copy_success(self):
        """ learn from history
        how did greatest companies start and try to emulate htier sucesss
        look at effects and look at alternatives"""
    def find_tech_used_by_military_and_finance_or_most_advanced_newest_tech_fields(self):
        """copy these fileds ideas and apply them to other fields
        figure out what goldmansachs is doing right now
        and companies worth the most, and copy there methods
        look to the stock exchange and find everything you can on these buisnesses
        and steal all there ideas assuming its legal from prospectus and videos 
        # build program to search web and build like profile of business from everyhting you can
        sort of like detectives building profile on a person
        always try to be two steps ahead"""
    def people_ignore_problem_not_visible_make_them_visible_to_make_them_care_so_they_will_solve_prblem(self):
        """how to make people care, and then work to solve problems put them in the position of the person suffering
        unger book, all excuses we give for not helping people letting other people die
        https://www.amazon.ca/Living-High-Letting-Die-Innocence/dp/0195108590
        philospical issues related to physiological issues
        meaninglessness or loss of purpose
        dont think of people who dont write 100 dollar check as evil"""
    def find_category_a_things_belongs_to_find_all_other_things_might_use_in_same_way_like_reverse_engineering(self):
        """then integrate these categories into psp data to view
        or find people who are great and find category these people flal into to find other ideas"""
    def reverse_enigneer_all_current_products_or_services(self):
        """ add these to the problem solivng rpgoram"""
    def reverse_enigneer_and_build_ontop_of_all_current_products_or_services(self):
        """ add these to the problem solivng rpgoram"""
    def tax_sale_database_in_all_countries_in_all_cities(self):
        """ """
    def possible_legal_claims_to_bring_based_on_facts_benefit_of_bringing_claim_and_risk_calculator(self):
        """ """
    
    def create_feeds_into_google_research_and_other_tech_companies_fintech_companies(self):
        """autobuild papers and integrate into workflow """
    def figure_out_persons_method_how_of_doing_something_then_cut_them_out(self):
        """ peel bakc onion of methods how did they do that thing
        find other peoples methods like sentdex method for getting newest up to date software project 
        information and then use this method to cut out intermeidatory and start doing it yourself read the textbook
        pepling back the onion of methods methods as much as possible"""
    def build_next_step_method_which_predicts_next_step_in_technology_using_history(self):
        """ like knowing the histyory of how computers devleoped and so know history of how ai will devleop
        or other fields and using this history to be 2 steps ahead of current field and other resources
        like sci fi books
        like for example progression from (1)single purpose nn to (2)multi purpose gpt to (3)ai agents to (4) whatever is next
        and knowing what is next trying to anticptiate this and be multiple steps ahead
        ask dad for advice for being multiple steps ahead
        like progressing from (1) building single satatlite simple(2) complex satltiete(3) to satltite consetellation(4) statltie produciton line like car prodiciton line using 3d printing
        always be on step ahead of competeitors in field
        FOCUS EVERYTHING ON BUILDING SINGLE PRODUCT
        increase in complexity to keep ahead of competietors for e engineer put everything in this 
        like improving cad design and patent design and mateiral calculations and test data and science data 
        and give  out earier iterations so its worthless what competeitors have done like google does"""
        return
    def generate_blender_file(self):
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
        #self.strategy_recorded=window.selection_get()
        genn_blend_functions=generate_and_open_blender_problem_web_and_tree_functions()
        process = Process(target=genn_blend_functions.generate_blender_effect_problem_web_for_strat_and_problem_tree_f,args=(self.problem_recorded,self.strategy_recorded,))
        #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        process.start()
        
    def build_obs_video_intake_model_from_pyautogui_program_to_simulate_keyboard_and_mouse_clicks(self):
        """SUPER IMPROTANT """
    def add_ideas_and_capital_from_other_fields_and_businesses_into_business_constantly_updating(self):
        """ add as many other ideas and cpatial into business to makew ti more valuable
        apply ideas from other field into current field"""
    def automatically_build_captial_building_functions_for_business_that_build_functions_to_build_captial_or_build_captial(self):
        """ also try to build and work on things that automcailly add more capital to your business
        if building a product to sell useless
        need to build captial or even captial building captial"""
    def generate_childrens_book_related_to_topic(self):
        """ """
    def search_through_all_books_in_world_for_useful_ideas_could_use_to_solve_problem(self):
        """ look behind walls"""
    def search_through_all_journal_articles_in_world_for_useful_ideas_could_use_to_solve_problem(self):
         """ look behind walls"""
    def generate_a_fund_raising_campaign_story(self):
        """people love stories tell a story to solve the problem """
    def argument_generator_most_persusaive_based_on_position_to_get_different_outcomes(self):
        """ show alternative arguments based on outcomes you want
        when arguing forward a conclusion that will put you in the best possible position based on the effects
        it gives and then support this conclusion with evidence
        in the problem environment if you cant support the conclusion with evidence change to next best conclusion you can with evidence that will give you the next best effects
        generate all possible arguments"""
    def all_finished_products_of_other_websites_add_to_generated_file_from_psp_search(self):
        """ """
    def all_types_of_files_generated_like_images_or_code(self):
        """ """
    def all_files_or_forms_created_by_a_lawyer(self):
        """ """
    def generate_other_ideas_functions_to_build_like_those_in_psp_api(self):
        """ """
    def all_final_documents_of_all_given_profession(self):
        """ think prospectus or factum"""
        
    def automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model(self):
        """ this will automatically add new data to find relevent to finance like prospectus or slide deck
        bascially things that you might want for finacne
        # this is super important to automcially build this adding new qualtires to the  engineering dic
        probably mostly final products that these indivudals produce automatically generate them
"""
    def automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically(self):
        """ this will autom
        probably mostly final products that these indivudals produce automatically generate them"""
    def automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products(self):
        """a function to generate other funcitons like the ones from the list below  that automcailly build and improve a product
        automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        """
    
        
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
         saved_text_from_website_and_link_list=[]
         link = r"https://html.duckduckgo.com/html/"
         question_striped=problemmm.strip()
         question_to_search_for=re.sub(r"\?","",question_striped)
         question_to_search_for=re.sub(r"\n"," ",question_striped)
         question_to_search_for=re.sub(r"\s+"," ",question_striped)

         question_to_search_for=question_to_search_for[:80]
         # run it as a subprocess or multi process
         

         #print(question_to_search_for)
         #input('checking whether prompt is ok here')

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
                     saved_text_from_website_and_link_list.append([str(p_tag_text),link_finals])
                 
                 except:
                     continue
             driver.quit()
             return saved_text_from_website_and_link_list
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
                #print(sentence_15)
                 continue
             if len(words_in_current_sentence)>60: 
                #print(sentence_15)
                 continue
             if "https" in sentence_15:
                #print(sentence_15)
                 continue
             else:
                 final_sentence_list.append(sentence_15)
         return final_sentence_list
    def get_website_text_lemmas(self,single_website_text):
        """ """
        lemma_str=""
        doc = self.nlp(single_website_text)
        for token in doc:
            lemma_str+=" "+token.lemma_           
        #lemmatized_tokens = [token.lemma_ for token in doc]
        return lemma_str
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
     
    def get_objects_and_qualitites_of_objects_in_sentence(self,spacy_dic,person_comp_info_dic_with_action):
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
                    #print(f"{worddd} NOT FOUND")
                     continue    
                 poss=spacy_dic["pos_only_tags"][index_of_word]
                 if poss =="NOUN" or poss =="PROPN":
                     cleaned_noun_chunk+=f"{worddd} "       
             cleaned_noun_chunk=cleaned_noun_chunk.strip()            
             if cleaned_noun_chunk=="":
                 continue
             cleaned_noun_chunk_list.append(cleaned_noun_chunk)
             
             # create qualtities of object here
             # add subsequent noun chunk
             if cleaned_noun_chunk not in person_comp_info_dic_with_action["action_objects"]:
                 person_comp_info_dic_with_action["action_objects"][cleaned_noun_chunk]={"qualtity_list":[],"transformation_list":[]}
             if noun_chunk_number!=len(spacy_dic["noun_chunks"])-1:
                 # if last noun chunk then dont add qualtity
                 if spacy_dic["noun_chunks"][noun_chunk_number+1] in person_comp_info_dic_with_action["action_objects"][cleaned_noun_chunk]["qualtity_list"]:
                     continue
                 else:
                     person_comp_info_dic_with_action["action_objects"][cleaned_noun_chunk]["qualtity_list"].append(spacy_dic["noun_chunks"][noun_chunk_number+1])# noun chunk after this one
         return person_comp_info_dic_with_action,cleaned_noun_chunk_list
               
    def get_transformation_of_objects_in_sentence(self,spacy_dic,cleaned_noun_chunk_list,person_comp_info_dic_with_action):
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
                     person_comp_info_dic_with_action["action_objects"][current_noun_chunk]["transformation_list"].append(word)    
                     
         return person_comp_info_dic_with_action
     
    def create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(self,spacy_dic,person_comp_info_dic_with_action):
        """ """
        import re
        import copy
        #orignal sentence saved so if want to modify algorhim later i can
        saved_word_word_chunk_cross_reference_dic={}
        cleaned_noun_chunk_list=[] 
        person_comp_info_dic_with_action,cleaned_noun_chunk_list=self.get_objects_and_qualitites_of_objects_in_sentence(spacy_dic,person_comp_info_dic_with_action) 
        person_comp_info_dic_with_action=self.get_transformation_of_objects_in_sentence(spacy_dic,cleaned_noun_chunk_list,person_comp_info_dic_with_action) 
        return person_comp_info_dic_with_action
   
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
    
    
    #### PROBLEM TREE FUNCTIONS
    # think of permeant solution here not temp
    # make this work and be useful
        
    def auto_generate_action_space_and_effects(self):
        """ actions are linked to effects"""
        import copy
        automated_problem_galaxy_dic2=copy.deepcopy(self.automated_problem_galaxy_dic)
        self.possible_object_action_effect_list_dic={}#objectttt:[list of actions]
       #print(self.automated_problem_galaxy_dic)
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
       #print('starting sort')

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
       #print('meow')
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

        
    def auto_generate_strats_and_effects(self,automated_problem_galaxy_dic):
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
        return self.strategy_methods_problem_tree_dic_max_difference
    
    def store_auto_created_actions_and_strategies_for_problem_tree_sql(self,strategy_methods_problem_tree_dic_max_difference):
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
        automated_problem_galaxy_dic=self.auto_generate_action_space_and_effects()
        strategy_methods_problem_tree_dic_max_difference=self.auto_generate_strats_and_effects(automated_problem_galaxy_dic)
        self.store_auto_created_actions_and_strategies_for_problem_tree_sql(strategy_methods_problem_tree_dic_max_difference)
        return strategy_methods_problem_tree_dic_max_difference

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
      #print(self.automated_problem_galaxy_dic)
       return self.automated_problem_galaxy_dic
   
    def create_words(self,words_string):
           """ creates a list of words splitng on spaces"""
           import re
           words_string=str(words_string)
           #print(words_string)
           #words_string=words_string.encode('ascii', 'ignore')
           words_string= re.sub(r"\s\s+",r" ", words_string )
           words_string=words_string.lower()
           words_list=words_string.split(" ")
           return words_list

        
        
    def create_document_similarity_score(self,doc1,doc2,typee=""):
        """ WORK ON FUNCTIONS WE CREATED BELOW
        comapre against context of action list effects against objective context
        comparing frequency of words and mathcing words
        get as many qualtiies of thing as possible to increase the context
        store scores where possible to make the search faster
        """
        import re
        from nltk.stem import PorterStemmer
        ps = PorterStemmer()
        #stop_words = set(stopwords.words('english'))
        objective=""
        doc1=doc1.lower()
        doc2=doc2.lower() 
        doc1=re.sub(r"\\"," ",doc1)
        doc2=re.sub(r"\\"," ",doc2)
        doc1=re.sub(r"/"," ",doc1)
        doc1=re.sub(r'[\n\t]', '', doc1)
        doc2=re.sub(r'[\n\t]', '', doc2)
        
        doc1=re.sub(r'[\[\]\(\)]', '', doc1)
        doc2=re.sub(r'[\[\]\(\)]', '', doc2)
        doc1=re.sub(r"/"," ",doc1)
        doc2=re.sub(r"/"," ",doc2)
        doc1=doc1.strip()
        doc2=doc2.strip()
        #print(f"doc1 {doc1[:80]}")
        #print(f"doc2 {doc2[:80]}")
        #print(len(doc1))
        if doc1=="" or doc2=="" :
            total_matched_words=0
            return total_matched_words




        #doc1=doc1.encode('ascii', 'ignore')
        #doc2=doc2.encode('ascii', 'ignore')

        doc1_list=self.create_words(doc1)
        doc2_list=self.create_words(doc2)
        #doc1_list = [token for token in doc1_list if token not in stop_words]
        #doc2_list = [token for token in doc2_list if token not in stop_words]  
        if typee=="get_action_list_score_for_objective":
            if objective=="money":
               print('focus on the finance aspects for this one')
        final_doc1_list=[]
        for word1 in doc1_list:
            stemed_word=ps.stem(word1)
            final_doc1_list.append(stemed_word)
            
        final_doc2_list=[]  
        for word2 in doc2_list:
            stemed_word=ps.stem(word2)
            final_doc2_list.append(stemed_word)        
        # do the word counting part   
        matched_word_dicc={}
        final_doc1=" ".join(final_doc1_list)
        total_matched_words=0
        for  doc2_wordd in final_doc2_list:
            #print(doc2_wordd)
            
            doc2_word_found_in_doc_1=re.findall(rf'{doc2_wordd}', final_doc1)
            number_of_matched_words=len(doc2_word_found_in_doc_1)
            total_matched_words+=number_of_matched_words
        matched_word_dicc[doc1]=total_matched_words                     
        return total_matched_words
        
        
    
    def consider_factors_such_as_time_to_complete_action_monetary_roi_cost_of_action_and_action_effects(self,time_to_complete_action,monetary_cost_of_action):
        """this is a numeric one """
        if time_to_complete_action=="[]":
            time_to_complete_action=0
        if monetary_cost_of_action=="[]":
            monetary_cost_of_action=0
        time_to_complete_action=float(time_to_complete_action)
        monetary_cost_of_action=float(monetary_cost_of_action)
        monetary_weight=80
        time_weight=10
        time_to_cmplete_action_score=time_to_complete_action*time_weight
        money_to_complete_action_score=monetary_cost_of_action*monetary_weight
        
        return money_to_complete_action_score,time_to_cmplete_action_score
        
    
    def use_patterns_in_strategies_help_rank_action(self,user_past_actions_list,user_time_past_use_of_action_list,life_action):
        """what does this mean it means we want to use things we note in strateies we use
        to help rnak future strategies
        this will likely be a numeric value
        so may be slightly different than create document simialrity score
        where do i get past strategy data        
        For past patterns of strategies look at past uses number of past uses of an action and
        look at  How about action relates to other actions or the specific action being considered 
        and how far away it is given it to contacts from other action       
        what are the patterns
        past uses of action numbers like time date it happened
        past time user works on action
        how this action related to the current action
        # goal is to create factor score using input data
        
        incorporate problem search into life action dag search save on work
        
        or find a way to better parse action sentrences to only incldue actions by peole or orgnaizaions
        maybe use neaurl network for this
        use referalnal phrasing app
        
        """
        import time
        time=time.time()      
        times_action_completed_list=[]
        proxmity_of_action_to_other_past_used_action_score=0
        time_from_last_use_of_action_score=0
        numer_of_last_use_of_action_score=0
        user_number_of_past_use_of_action=0
        if len(user_past_actions_list)>0:
            return numer_of_last_use_of_action_score,time_from_last_use_of_action_score,proxmity_of_action_to_other_past_used_action_score
        for i, past_action in enumerate(user_past_actions_list):
            if life_action ==past_action:
                user_number_of_past_use_of_action+=1
                times_action_completed_list.append(user_time_past_use_of_action_list[i])
        numer_of_last_use_of_action_score=user_number_of_past_use_of_action
        user_past_actions_context=str(user_past_actions_list[1:-1])
        time_from_last_use_of_action_score= time-float(times_action_completed_list[0])
        proxmity_of_action_to_other_past_used_action_score=self.create_document_similarity_score(user_past_actions_context,current_action_context,typee="proxmity_of_action_to_other_past_used_actions")
        print('use all times when possible')
        print('use context of past used actions by person compare against current action context to score')
        return numer_of_last_use_of_action_score,time_from_last_use_of_action_score,proxmity_of_action_to_other_past_used_action_score
    # look at past use of this action
    # look at its relationship to other actions person has taken        
   #proxmity_of_action_to_other_past_used_action_score=proxmity_of_action_to_other_past_used_actions
    

#rank based upon the simialrity of the context 
    
    def use_info_about_other_people_when_action_was_taken_to_help_rank_action(self):
        """ """
        return info_about_other_people_score
    
    def consider_distance_of_resources_you_have_avilable_to_you_vs_resources_required_to_take_action(self,resources_required_for_action_context,user_resources_context):
        """just doing text to text here
        # if domt have resoruces to complete actiom then reduce value because need ot take extra action to get resources
        # compare resources context against life action resoruces  context and higheter score if more common resoruces or words
        # because easier to take action
        For resources and others consider the  Proximity of that resources that are needed for the action
        to the resources you have in your positonality dic  
        # more simlar resources we have the higher score
        # because can more eaisly complete action
        and that is how we rank that resource of relations 
        of the problem or action being considered"""
        print('try to not just matcvh on words try to get distane of words in context and measure that way i think i ahve a alogrhim to do that')
        print('higher score is better here')
        resources_score=self.create_document_similarity_score(user_resources_context,resources_required_for_action_context,typee="consider_distance_of_resources_you_have_avilable_to_you_vs_resources_required_to_take_action")       
        return resources_score
    def consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action(self,current_action_list_context,user_position_context,person_organizaion_position_list_dic,person_organizaion_action_list_dic):
        """how to conisder peoples avialble actions
        get people available actions based on life dags
        need to look at their tools
        # if certain simialr available actions lower score       
        """
        other_people_postiion_score=0
        other_people_available_action_score=0
        print('make avialable action of other people inversely related to action so action more valuable if other people or organizaions cant do it')
        for person_organizaion_position_context in person_organizaion_position_list_dic.values():
            position_score=self.create_document_similarity_score(user_position_context,str(person_organizaion_position_context),typee="consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action")     
            other_people_postiion_score+=position_score
        for person_organizaion_action_list_context in person_organizaion_action_list_dic.values():
            action_avilable_score=self.create_document_similarity_score(current_action_list_context,str(person_organizaion_action_list_context),typee="consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action")   
            other_people_available_action_score+=action_avilable_score
        return other_people_postiion_score,other_people_available_action_score
   
    def consider_numeric_distances_and_placement_of_other_people_places_and_things_when_choosing_action_use_map(self,action_locations_data_list,user_location_data_list):
        """just doing text here
        For the distances function yet the distances were Geo locations of all items and calculate based on distances how far away it is from the given person and use this as the function
        Iterate through a list of locations of things and get their values in relation to the given thing and then based upon those values
        rank actions that involve those locations
        trying to rank action
        factor in as input geolocation placeement of things when choosing action
        if online no distance
        want to consider placement of people and things in relation to completing action
        if really high score for distance of location of things related then lower score
        
        have the location as element in list then have
        
        """
        print('making distance score negative because if high distance of things away related to action then dont want to complete this action necsarily')
        distance_place_of_people_and_things_score=0
        print(action_locations_data_list)
        print(user_location_data_list)
        if len(user_location_data_list)>0:
            for action_geo_location in action_locations_data_list:
                distance_from_action=action_geo_location-user_location_data_list[0]# places lives
                place_of_people_and_things_score+=distance_from_action       
        return distance_place_of_people_and_things_score
    def use_all_qualtities_of_input_data_strategies_and_personal_info_in_different_ways_to_help_rank_action(self):
        """probsably just more text to text """
        return other_qualities_score
        
    def search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(self,all_guide_life_action_list_with_effects_dic,user_positional_info_dic,objective,search_type="life_dag",problem_search=""):
        """refer to methods in problem solving tkinyter program for guaince on how to build this
        ?? how do i sort actions using various objectives like amount of people impacted most money most people help which look at the alternative actions effects and objects involved? ###fYoKuAhEsPaNrAtDoIfJ
        THIS IS HOW I WILL SORT ACTIONS SUPER IMPORTANT
        problem solving program
        need to also build a life action tree from this to take best actions
        THIS IS KEY
        self.action_space_with_effects_dic
        the action space
        is actions and there effects
        objects and effects
        so we will sort and search this space using the effects as context
        and the positonal info dic and objectives will be key in finding actions in this space using these effects
        so how do we do that
        Build FFNN?
        make sure that qualities of object are associated with specific transformations  
        
        strategy_methods_problem_tree_dic=
        self.sort_actions_into_strat_by_max_different_effect_score(self.strategy_methods_problem_tree_dic)
        
        how do you integrate the objective and  positional info into the search and choice of actions
        self.consider_past_problem_data() to search and sort actions
        
        # use nn maybe to rank actions amd 
        maybe make the search much faster with nn
        
        search will be two for loops
        each qualtity of personal information run against all actions to rank actions
        or to search for best action
        then return actions to take
        
        use peoples lives to collect data about possible actions 
        to train nn and so can better know effects
        
        convert objective into something useful
        compare each perosnal ifnormation qualtity against 
        for personal_qualtity in objective_personal_qualtity_dic:# and o
            for actionn in actionn_dic:
                #give action a ranking for this personal qualtiy some pattern or relationship between them
                # use data to determine this relationship
                #then use objective as a additianl critiera that is more heavily weighted
                 then add all the values up to a number to determine actions rank
                 then sort list
                 
        # issue is we dont have the labels of best action based on objective/position so maybe nn not best choice
        # OR USE NN
        input is all personal qualities and objective values
        out put is action chocie based on those values
        
        history repeats itself is the idea
        
        so the same or similar actions should have same or simlar effects 
        if another person takes it
        
        ###
        use exmaples of peoples lives because it will elminate all actions in action space that are not possible and those that never have been done before ( but assuming we make ones found generic enough this is ok)
        and then make the actions more generic to allow for creativty and more useful so can think around
        like for example invent something rather than invent car if that is what a person did
        more example the strategies or action_sets are peoples actual lives who were successful like mlk
        or greta thunberg or elon musk
        or dad or mom
        
        using people lives will get us actions worth doing and the effects of such action
        and we can cateogrize peoples lives related to an objective
        
        so for example greta thunberg life_action_set would be under helping most people and in that area
        
        


        the effects are what the person ended up with at the end of there life and got by completing a different action
        see if i can get effects for each aciton rahter than each whole life_action_list for a person
        
        so suggest these action sets based on peoples perosnal information put in to get different objectives like help most people or make the most money
        
        if complete action should get simialr effects and similar future possible actions
        
        
        look at the actions these people take will allow you to create action space
        
        ###
        so when i log on it will display trunciated life_action_list to use to maxmize different objectives
        and will rotate the ones shown so build this in too
        but will show specific life_action_list based on current position and perosnal info inputted
        
        ------------------------
        
        LEFT OFF HERE how to write this function to sort/search life_action_lists
        so how do i  divide life action on objective MAYBE use personal qualitites of persons life_action_list we are using , maybe use effects words of actions and there relationship to objective words   
        # then rank each actions and life_action_lists relationship to the objective and how well it achevies it
         
        #use personal characeristic of persons who I get the life_action_lists from to figure out how to rank/suggest life_action_lists to a  user  based on an users perosnal info dic
        so for example greta thunber is a women who is young sweidsh etc so would suggest for a user who is swedish and a young woman and at greta age a truncated life dag to the women current age
        under the objective category of making the world better
        
        so for
        maybe 3 deep neural network
        LEFT OFF HERE
        SO  for each life_action_list create scores for each category of objective which take the objective and perosnal characeritcs into account
        
        then display these strats
        takign perosnal characeritic into consideration
        
        
        
        #score based on objective and 
        
        
        # then would cateogrize greta life dag under helping most people giving it a high rank
        
        # note how the person is simialr to them on what dimensions 


        #
        so if greta thunberg then put in helping people

        and how do i divide on perosnal characeristics so i know how much of life_action_list to display 
        and which life_action_list to display
        ###
        what informaiton do i need to scrape to sort and or search the life_action_lists based on objective and perosnal information
        look at peoples lives
        look at people who helped the most people
        look at people who made the most moeny
        and the actions they took to get to where they are
        and then train model using these people actions or histories life_action_list
        inputting their personal characeritisc and then the action they took
        to recommend to someone in a simialr simualr the best action they could take to accomplish objective
        use biographies and books and linkeind etc
                    self.keep_updating_and_stealing_existing_business_methods_and_final_product_funnel_work_into_problem_environment_to_solve_problem()
        """
        import numpy as np
        sorted_life_dags_dic_list=[]
        final_all_sorted_life_action_for_objective_dic_list=[
            ]       
        # use objective as a prompt and get more context for the objective
        prompt_objectives_to_score_list=["helping the most people Helping others is an important part of life, giving you a sense of purpose and boosting your happiness. In fact, acts of kindness can boost feelings of confidence, control, happiness, and optimism, says the Mental Health Foundation.Supporting others has a positive effect on the world around you. Kind acts may also encourage others to repeat the good deeds they’ve experienced themselves, contributing to a more positive community.If you want to help others more but aren’t sure where to start, look no further. Whether you’re looking for ways to help friends and family or give back to your community, keep reading for a list of ideas to get you started helping others.Where can I find ways to help others?First, focus on your passion when considering ways to help others. Your passion for helping others can be the foundation for your giving. Helping someone in need isn’t about how much you give but how much love you put into it.Inspiration for how to help others in need can happen anywhere. Small acts of kindness, like holding the door or offering a compliment, can have a significant impact. Helping people can include more substantial efforts, like making donations — whether of time or money — or giving items to help someone in need.Here are some ideas for finding ways to help others that will bring you joy and a sense of connection.Ask community leaders, friends, and family how you can help. Explain to them how you hope to help others and why you desire to help and see what they suggest. The opportunities for helping someone in need may surprise you!Look for opportunities to help and lend a hand without being asked to find out the best way to help. For example, hold the elevator door for a colleague or offer to take a photo for a group of tourists if they’re struggling with a selfie stick.1. Be proactive, not reactive.Many lives are lost to health emergencies that could have been managed through learning lifesaving skills Knowledge of cardiopulmonary resuscitation (CPR) and first aid help in emergencies at home, in public, or at work by providing immediate care, reducing injury severity, promoting safety, providing reassurance, and increasing workplace safety.Becoming trained in CPR and first aid is one of the best ways to support others and the community, helping others in need.American Red Cross Training Services offers a variety of CPR and first aid training programs, which you can take online, in person, or in combination to help everyone, whether your neighbors, colleagues, family, or friends. Find a CPR and first aid training program that fits your schedule.Find a ClassCPRFamily sharing a meal.Benefits of Taking a CPR, AED or First Aid CourseBe prepared: Protect your loved onesBe confident: Act with hands-on trainingPeace of mind: Know how to handle emergenciesHelp your community: Use lifesaving skills when neededTake a CPR Class2. Give your time.The gift of time is valuable and satisfying. It also makes giving accessible since we don’t all have the same amount of money, but we all have the same amount of time.Here are some ways to give your time and help people in need.Teach: Offer to teach friends and family members struggling with a skill you know well. Learn how to become a CPR Instructor! Teach people outside your social circle, too — try tutoring a student in math, for example, or showing your coworker how to use the office copier.Support: Be the first to offer condolences when someone you care about is suffering. Do what you can to comfort them, whether they need a hug, a shoulder to cry on, or a helping hand. Talk to them with empathy and compassion and ask if there is anything you can do to help.Listen: Not everybody seeks hands-on help or a solution to their problems; they might simply need to express their feelings while a supportive friend listens.Compliment: While giving compliments might not be what you traditionally picture when you think of helping people, it does help. Offer compliments to everyone around you, giving sincere praise while celebrating their successes and qualities you admire the most.Volunteer: Find a charity you’d like to support, like a shelter or soup kitchen, and spend time there doing whatever needs to be done. Not only will this help others, but it’ll also give you a newfound appreciation for all the good things in your life — and it’ll make you a more compassionate person.3. Donate to a worthy cause.Monetary donations are a great way to help others but aren’t the only way to donate to help those in need.Here are a few ideas for donating to worthy causes and supporting others.Donate furniture and clothing to a local shelter.Donate unopened spices, canned soups, or beans to a local food bank.Donate toys to local shelters and food banks.Donate blood if you can.Donate the opportunity for holiday and birthday gifts. Ask friends and family to make donations to charities instead of getting you gifts.Donate your car.4. Send a thoughtful note or care package.Sometimes, helping others is as simple as letting them know that you care. When people feel isolated or cut off from their friends or family, even a small gesture can help them feel more connected and brighten their day.Send handwritten cards and even care packages with special treats inside.Write a friendly email or letter and casually mention why you like the recipient.5. Express appreciation.Receiving thanks is another way to help each other and help our community. Plus, showing gratitude not only helps others feel appreciated but makes you happier too!Express appreciation when someone does something nice for you. Let your loved ones know how much you appreciate them, even when there’s nothing specific to thank them for.Practice gratitude by creating a list of things you’re grateful for and sharing it with others.Share a social media post about how much you appreciate someone’s support as you change careers or tell a friend how proud you are that they ran a whole marathon.Compliment underappreciated people, like the person bagging your groceries or bussing your table at a restaurant.Thank frontline health workers and first responders.Be neighborly. Check on neighbors, especially those who live alone, are elderly, have health or mobility issues, or care for children.Finally, helping other people should not equal a guilt trip. We have all felt the dread that comes from being coerced into helping others. When considering ways to help others, think about what you have excess — time, money, or unused items — and how that may help others in need.Now that you have the tools and inspiration to help others, it's time to put them into action. Together, we can make a positive impact on the world!",
                                         "making the most money The 6 figure income in your teens is the way outlier. The 9-5 is the path to comfort for the vast majority. The secret to fast easy money can be a couple things, incredible talent, large up front investment, a great idea, fraud, or dynamic charisma all coupled with the largest single factor, luck. You are comparing yourself to the top .001% or just liars. It's not worth it to hunt for a secret. It is worth it to better yourself, try and increase your worth and find someone willing to pay you what you're worth. It is worth it to be as happy and content as you can with what you have. It is certainly worth it to live on less than you make and sacrifice for the future. Side hustles are popular, and possible. What you need is a good idea and the motivation to make it happen.25 ways to make moneyWe turned 25 ways, complete with need-to-know details, to inspire you to earn. While most people want to make money fast, don’t discount the “slow” gigs, as they may pay more in the long run.How to make money onlineHow to make money from homeHow to make money offlineFor sections with input from Redditors: We sifted through Reddit forums to get a pulse check on how users feel about certain side hustles. We used an AI tool to help analyze the feedback and then summarized insight. People post anonymously, so we cannot confirm their individual experiences or circumstances.How to make money online1. Pick up freelance work onlineMake money online through websites such as Upwork, Fiverr and Freelancer.com. These sites offer opportunities to do a variety of freelance jobs, like writing, programming, design, marketing, data entry and being a virtual assistant.A report from Freelancer.com found that computer security jobs had the fastest growth in listings on its site in the second quarter of 2024, up 27.1%.Jobs involving writing skills are also in high demand. Although generative artificial intelligence (AI) is being used more for content creation, it can’t fully do the work of human writers.Companies are looking for writers who know how to edit AI content and who have at least a basic understanding of search engine optimization — learning or beefing up SEO skills could be a lucrative side hustle.No matter what freelancing you do, keep track of the going rate for the kind of work you provide so you know what to charge. Some freelancers are charging $100 an hour or more for their freelance writing services.Expert take: Soraya Ivette is a content marketing strategist who offers services on Fiverr. She started freelancing part time when she was home with her young children, and has done well.Once I set up my profile on Fiverr, I started getting job requests within a couple of weeks and I started taking on more jobs and making regular money consistently every month, she said in an email interview.Total time: It can take a while to get your first gig.Setup: 24-48 hours.How easy to start: Easy, if you have the expertise.Age threshold: Typically 16 to 18+.How fast you'll get paid: Varies by site.Need to knowIt takes Upwork up to 48 hours to approve your profile. Keep in mind it can also take time to land your first freelance gig.Payment varies by site. On Upwork the timeline for receiving earnings depends on the type of payment. Hourly contracts have a weekly billing cycle and you can withdraw funds 10 days later. Fixed-price contracts have a five-day waiting period after reaching a milestone. On Fiverr, you're paid when the work order is complete, but you can't withdraw funds for 14 days. (The waiting time is shorter for Top Rated Sellers.)RequirementsUpwork and Fiverr require users to be at least 18 to sell work. Fiverr allows users age 13 and older to use a parent or guardian’s account, with permission. And Freelancer.com requires users to be at least 16.2. Test websites and appsAnother way to make money from home is on sites like UserTesting.com. You get paid for your thoughts on how well — or not so well — certain websites and apps work. You’ll have to complete a short test to be accepted by UserTesting, then you’ll be paid depending on the test type.Total time: Approval can take a few days.Setup: Less than an hour.How easy to start: Easy, if you have the tech gear and complete a sample test.Age threshold: 18+.How fast you'll get paid: Usually after 14 days.Need to knowYou need to complete a sample test as part of the UserTesting application process.You will start receiving testing opportunities after your application is approved.The timeline for approval can vary.Payment amounts vary based on the length of the tests. You get paid 14 days after completing a website or app test via PayPal.RequirementsYou need to be at least 18.You need a device that meets UserTesting’s requirements, internet connection and microphone.The practice test and most user testing requires English, German or French; some test opportunities may be in additional languages.3. Learn to use AI toolsGenerative artificial intelligence is so hot right now. Research from PwC estimates that the North American economy will see a $3.7 trillion impact by 2030, thanks to the AI market.It's a good time to learn how to make money by using AI tools. Some AI-related side hustles include:Integrating AI tools as a freelancer, to help you create digital products or to edit AI content for a client.Improving your advertising, marketing efforts and management of your existing small business.Teaching others to use AI tools.Total time: Depends on demand.Setup: Around 24-48 hours if using a site like Upwork or Freelancer.com.How easy to start:  If you’re already familiar with AI tools, it will be easier to get started.Age threshold: 16+ for Freelancer.com and 18 for Upwork.How fast you'll get paid: Varies by client or the number of products you sell and your chosen platform.Need to knowGive yourself time to get familiar with using AI tools.You’ll need to meet the requirements of the freelance gig site you choose.Payment will depend on your client and the site’s terms and conditions.RequirementsYou’ll need a computer and an internet connection.4. Take surveys for moneyYou can make money from home by taking online surveys, but don’t expect to earn a lot. Survey sites don’t typically offer a big payoff, and many sites are more useful for earning gift cards than cash.Some of the more popular survey sites include Swagbucks and Survey Junkie. Read about how little we made with survey sites to find out which one might be best suited for you.Total time: It will take a while.Setup: Just minutes.How easy to start: Very. Just register and begin.Age threshold: 13 to 18+, depending on the site.How fast you'll get paid: Varies by site.Need to knowSurvey sites could be an option for how to make money online for beginners because you can register with a site and start taking surveys in a matter of minutes.The time it takes to get paid depends on the survey site and how much time you dedicate to taking surveys.Some sites let you cash out only after you hit a minimum earnings threshold.Other survey sites issue points, which can be redeemed for cash (via PayPal) or gift cards.RequirementsMost survey sites have a minimum age requirement, which ranges from 13 to 18 (depending on the site) making these sites one idea for teens to make money online.Individual surveys may have specific requirements. Don't be surprised if you are disqualified from a survey without much explanation.5. Make money from your blog with affiliate linksIf you’re a blogger who gets decent traffic, you could make money by joining an affiliate network. Affiliates get paid when someone clicks through from the website to the partner site and buys something there.Some bloggers make a lot of money this way, particularly those who do affiliate marketing full-time. You can use social media or a platform like Pinterest to drive traffic to your blog. Read more about affiliate marketing and other ways to make money blogging.Total time: It can take quite a while to build an audience.Setup: With blog templates, building a site is easy.How easy to start: While getting started can be easy, creating regular content may be another matter.Age threshold: Varies.How fast you'll get paid: A month or two, on average.Need to knowFirst, you need a blog, social media account or other online presence that draws a healthy number of visitors each month.Then, you need to apply for and be approved by an affiliate marketing network like CJ, ShareASale, FlexOffers, Rakuten Advertising or Amazon Associates.Payment schedules and thresholds vary by affiliate network, but expect to wait at least a month or two for your first paycheck.Amazon Associates pays out earnings 60 days after the end of the calendar month in which they were earned.ShareASale disburses earnings monthly.RequirementsA blog, social media account or other online presence that attracts a steady stream of visitors.6. Sell your wares on EtsyHave a penchant for woodworking, jewelry-making, embroidery or pottery? Sell your crafts on Etsy, the go-to site for artisans selling home goods, art and knickknacks. According to Etsy, the company has more than 95 million active buyers. Learn more about how to make money on Etsy.Total time: It might take quite a while for customers to find you.Setup: Can be quite involved.How easy to start: Leaning toward hard on the difficulty meter.Age threshold: 13+.How fast you'll get paid: Daily, weekly, biweekly or monthly, depending on your preference.Need to knowOpening an Etsy shop is the easy part. It can be done in a few hours.You need merchandise to sell, photos and descriptions to post, a name for your shop and a business plan to help you succeed. Once that’s done, you’ll still need to find customers.Once you sell an item, payment is deposited into your Etsy Payments account first, then to your bank account depending on your desired deposit schedule.RequirementsIf you’re over 13 years old but under 18, you can sell on Etsy but would be considered a minor and must follow extra policies.You need to have all necessary intellectual property rights to the merchandise sold in your shop.7. Self-publish an e-bookWriting a good book is tough, but the internet makes it easy to bring it to market. If you’re a writer who can churn out pages, you can use Amazon’s Kindle Direct Publishing to sell your books(s) on the Kindle store. It’s free to publish a book, and you can earn up to 70% of each sale in royalties. Write your book, enter a clear description and the details to be displayed and upload your manuscript. Set the price and see if it sells.Total time: How fast can you type? We don’t have to tell you writing a book can be a slog.Setup: Quick and easy on KDP once the book is ready.How easy to start: Just start writing.Age threshold: 18+, but parents and guardians can use their accounts to sell minors’ books.How fast you’ll get paid: Monthly. You'll need to meet a $100 threshold for wire or check payments.Need to knowJust because it’s simple to self-publish doesn’t mean your book will sell. Competition is high with millions of e-book titles on the Kindle Store.Choose one of two royalty options: 70% or 35%. You’ll have to price your book between $2.99 and $9.99 if you select the 70% option. You have more pricing flexibility when you pick 35%.RequirementsYou need to create a Kindle Direct Publishing account to get started.Proper formatting is important. Amazon says most Microsoft Word documents convert to e-books easily, but other formats are also supported.Take control of your finances with the NerdWallet appOur app tracks your spending, credit score, net worth and more — so you have a clear view of your day-to-day and long-term finances.8. Get advertising revenue from your blog or YouTube channelIf your YouTube videos or blog posts draw an audience, you may be able to make money from advertising. YouTube sets 1,000 subscribers as the benchmark for applying to the YouTube Partner Program if you want to place ads on your channel.You can apply with 500 subscribers for other monetizing features like channel memberships. You can also use Google’s AdSense, the same ad platform on YouTube, to put relevant ads on your blog or website for earning potential. Read more about how to make money on YouTube and Google AdSense.Total time: It can take several weeks to get up and running.Setup: Fairly easy.How easy to start: Depends on how good you are at producing interesting videos.Age threshold: 18+.How fast you'll get paid: Could take a long while to earn the first payout; then monthly.Need to knowSigning up for Google AdSense is pretty easy, but to use AdSense with YouTube, you’ll need to be part of the Partner Program.You can use AdSense on a website or blog with fewer eligibility requirements.Allow at least two months for ad revenue to start trickling in.You need to earn at least $100 before you're eligible for a payout.Once you hit the $100 threshold, earnings are issued between the 21st and 26th of the following month.RequirementsYour own website that has been active for at least six months.For YouTube, you need at least 1,000 subscribers and to meet requirements related to views or watch hours.You must be at least 18.9. Become an Instagram influencerCompanies are using Instagram influencers — people with large, dedicated followings on the platform — to rep their products. You can get in on the action by applying for opportunities via a marketing platform like Open Influence or Aspire, or by contacting the brands you want to work with. You can also make money on TikTok this way.Total time: You'll need to stick with it.Setup: Quick and easy.How easy to start: Not that easy. Read: Must build following to gain influence.Age threshold: 13+.How fast you'll get paid: Varies on partnerships.Need to knowCreating an Instagram account is quick, but building a following can take months or even years.Once you have the numbers, you'll need to find paid opportunities. You can do this via affiliate networks or by pitching brands you want to work with.The time to receive your payment will depend on the terms of your agreement, but affiliate networks typically pay out earnings the month after a campaign is completed.RequirementsAn Instagram account with a dedicated, engaged following.You'll also need to meet the requirements of any affiliate network.10. Monetize your Twitch channelGaming could be a way to make money from home if you have a steady following on Twitch, the go-to site for gamers. Streamers can receive money from viewers’ virtual cheers, or “Bits,” and even get a share of subscription and ad revenue if they reach Affiliate or Partner status. Learn more about how to make money on Twitch.Total time: This can be a long game.Setup: Quick and easy.How easy to start: Easy to start; takes a while to build a following.Age threshold: 13+.How fast you'll get paid: Monthly.Need to knowYou can launch a Twitch channel and start streaming in a day, but it will take weeks or even months to build a following.Subscription and ad revenue earned as a Twitch Partner or Affiliate is paid out around the 15th of every month, and you must have a balance of at least $50 for most payout methods (it's $100 for wire transfers).RequirementsYou need to hit certain viewership and broadcast milestones to become a Twitch Affiliate or Partner and qualify for a share of game sales, ads and subscription revenue.» MORE: How to make money as a kid11. Sell your photographyTurn your photographs into cash via sites like Fine Art America, which lets you upload your images to sell as prints, T-shirts, phone cases and more. Other marketplaces for photographers include SmugMug, 500px and PhotoShelter. Some sites require a subscription but may provide features ranging from cloud storage to password-protected galleries and a customized website.What the Redditors say: Success selling photos requires both high-quality content and a bit of business savvy around rights management and pricing. A general theme is that you may do better by forming direct relationships with buyers than purely relying on stock sites.Total time: Buyers need to find you — and like your work.Setup: Just a few hours.How easy to start: If you have a library of photos, you're on the way.Age threshold: Varies.How fast you'll get paid: Depends on your sales platform.Need to knowYou can set up a profile with sites like SmugMug, PhotoShelter or Fine Art America in a few hours, assuming you have a body of original work.Payment varies widely depending on the site.Fine Art America: Payment issued after 30-day return window expires. Sent on the 15th of each month.PhotoShelter: Payment issued at time of sale to your chosen payment method (PayPal, Stripe, etc.).SmugMug: You can request payment be issued the following month if you have a balance of at least $5.RequirementsRequirements vary by site, but you need to have all necessary rights to the images you sell.How to make money from homeSome side hustles don't even require you to leave the house. Or if they do, it might just be a short walk around the block with a furry friend. Working from home requires a little creativity and a stick-to-it spirit. Here are some excellent ideas for side gigs from home:12. Become a dog walker with Rover or WagLove dogs? Choose dog walking as a beginner's way to make money. Apps like Wag and Rover offer on-demand dog walking, so you can pick up walks when your schedule allows. If you have space (and your landlord’s permission, if you rent), you could offer overnight dog boarding. Read the fine print if you sign up for these services.What Redditors say: There's potential to earn an extra $300+ per month with a gig service like Rover when you have regular clientele, but success can depend heavily on location and market. Are dogs trending in your town?Total time: Building a client base may take some time.Setup: Can take a few weeks to be approved.How easy to start: Love pets? You're good to go.Age threshold: 18+.How fast you'll get paid: Two days to a week.Need to knowIt takes about 5 to 10 business days for your Rover profile to be reviewed and approved.The application process for Wag takes about two weeks and you must pass a background check and pet care quiz.RequirementsFor Rover or Wag, you’ll need to live in an area where the service operates.If you want to pet-sit in your own home, you’ll need an apartment or house that allows pets.You’ll have to pass a background check.13. Sell unused gift cardsMake extra money by selling unused or partially used gift cards on a site like CardCash or GiftCash. CardCash notes it will pay you up to 92% of the card’s value, or you can trade in your card for one you’ll use. Read more about what to do with unwanted gift cards.Total time: In minutes if your gift card is for a popular store.Setup: Easy.How easy to start: The more gift cards you have to sell, the better.Age threshold: 18+.How fast you'll get paid: A few days to about two weeks.Need to knowYou can get an instant offer or quote via sites like CardCash and GiftCash.You can sell gift cards at kiosks and participating retail locations to get cash the same day, or try to sell them online. The latter takes longer, but you may get a better offer for your gift card.RequirementsYour gift card may need to meet a minimum balance to be resold. Not all cards will generate offers.Gift cards with expiration dates may not be eligible.14. List your spare bedroom on AirbnbRenting out your home or spare bedroom on vacation rental sites is another way to make extra money. Be prepared to spend some money to clean and keep up the property, replace home goods and pay toward service fees. And scrutinize your rental agreement, HOA rules and zoning or other restrictions before you get started. Learn more about how to start an Airbnb business.Total time: Demand drives success, and that depends on your location.Setup: A listing can be created and live in hours.How easy to start: If you have a place to rent, it's a simple process.Age threshold: 18+.How fast you'll get paid: A day or more after check-in.Need to knowYou can create a listing and start accepting reservations on the same day.Payment is typically disbursed about 24 hours after your guest’s scheduled check-in time, but processing time for that payment depends on the payout method.RequirementsComply with any rules governing short-term or vacation rentals in your property, including city ordinances and rules issued by your landlord, condo board or homeowners association.How to make money offlineThere's online and at-home ways to make extra money — and then there's a third alternative: offline. This version of the gig economy may require more work, but the upside can be substantial. Since there’s no escaping the internet these days, some of these offline methods do have online components:15. Sell your gently used clothesA woman makes extra money by selling her clothes.Selling clothes you no longer wear is a quick way to make some money. Start with local consignment shops to make money quicker or use sites like ThredUp and Poshmark to find buyers. When listing items online, be sure to take clear, well-lit photos of your pieces and research similar items to set competitive prices. Get tips on how to sell your clothing.Total time: Varies by sales channel.Setup: Easy and fast. You can simply go to a consignment shop or fill a box with clothes and send it in.How easy to start: Easy. Cleaning out the closet may be the hardest part.Age threshold: 13+.How fast you'll get paid: Varies by sales channel.Need to knowYou can sell used clothing and accessories several ways, but they're all pretty quick to start.Fast: A brick-and-mortar consignment store like Plato's Closet will give you cash on the spot.Medium: Other in-person and online consignment shops pay you when your items sell, or when they receive and inspect your items. Either way, allow at least a month for your payout.RequirementsGently worn shoes, clothing and accessories.Items will go through various inspections before being accepted. For example, ThredUp checks items for pilling, fading, shrinkage, missing parts (like buttons) and stains.16. Trade in old phones, electronics for cashHave an old phone, iPad, laptop or gaming system lying around? Sell it on a site like Swappa, Gazelle or Facebook Marketplace. Check out Amazon’s trade-in program, which pays participants in Amazon gift cards — and eBay, too. If you’re in a rush, try an ecoATM kiosk, which offers cash on the spot for your device.Total time: Lots of options, so your time spent will vary.Setup: A breeze.How easy to start: Easy, especially if your device is in good shape.Age threshold: Typically 18; check terms of service.How fast you'll get paid: Varies by where you sell.Need to knowSelling directly (Swappa, OfferUp, Facebook Marketplace): In most cases, you take photos of the phone, verify the electronic serial number is clean and post your listing. Some sites review and approve postings, but the time is minimal. Fees vary. Swappa, for example, charges a 3% seller fee.Selling to reseller (Gazelle): Answer a few questions online for an instant quote. Then send in your device and get paid once the company confirms its condition is as described.Selling directly: When you get paid depends on how quickly your phone or device sells. Once the item sells, payment is fast.RequirementsA used phone, laptop, gaming system, etc.Cell phones: You need to verify the phone is not stolen or under a repayment plan. Check terms of service for additional requirements, such as no activation lock.17. Get a babysitting gigEveryone from college students to recent retirees can make money by watching other people’s children. Word-of-mouth referrals from friends and family are still a great way to get started, but you can also create a profile for free on Care.com or Sittercity to expand your reach. Note any specialized skills, such as CPR certifications, to make yourself more marketable.Total time: Online setup takes minutes; neighborhood referrals may take a while.Setup: Just minutes.How easy to start: Getting the word out is the main thing.Age threshold: Very young if you're using referrals. 18+ online.How fast you'll get paid: When the parents come home.Need to knowYou can create a profile on Care.com or Sittercity in a matter of minutes.You typically get paid when you complete your gig, whether by a service or direct from the customer.RequirementsYou need to be at least 18 to list as a caregiver on Care.com and Sittercity.Clients may request a background check.18. Rent out your carCity-dwellers often don’t use their cars for days or weeks at a time. That idle time can translate to extra money with services like Getaround and Turo, which let you rent out your car by the hour or day. You take home the majority of those earnings, while Getaround or Turo takes a cut for protecting your car while it’s being rented.Total time: Demand for your car will depend on the local market.Setup: It takes about a half hour to set up an account.How easy to start: With an appropriate vehicle, it's easy.Age threshold: 21+ with a valid driver's license for Turo; Getaround does not list an age requirement.How fast you'll get paid: Varies by site.Need to knowYou can create a listing on Turo or Getaround in under 30 minutes.Turo initiates payment within three hours of the end of the rental, but you can expect it to take a few days for your bank to process the deposit. (This is the case for all trips after the first one, which takes a few days for Turo to send.)Getaround rental earnings accrue daily or monthly. Payments are made via direct deposit.RequirementsIf you lease your car, check the terms of your agreement and financing documents to make sure you’re allowed to share it.Your car must meet certain requirements (make/model/year/mileage) and satisfy maintenance and safety standards. You may also be asked to agree not to list on other platforms.19. Sign up for TaskRabbitIf you actually enjoy putting together Ikea furniture or standing in long lines, you may be cut out for doing tasks for others. Websites like TaskRabbit can connect you with people who need help with a variety of things, such as moving, cleaning, delivery and handyman services. The site also offers several virtual and online tasks, such as helping with a research project or data entry. Read about how to make money with TaskRabbit.What Redditors say: This is a flexible side hustle that can be good for a couple hundred bucks of supplemental income per month. But, like with other gig service sites, your success is dependent on location and demand.Total time: Local demand for your skills will determine the time you spend.Setup: A couple of hours, then some time for approval.How easy to start: Easy, though you'll need to do some research.Age threshold: 18+.How fast you'll get paid: A few days after a job.Need to knowYou can set up your profile and register in a matter of hours, but can't start accepting tasks until your profile is approved by TaskRabbit. This may take a few days.Once approved, you need to pay a $25 fee, so you may first want to research your market and the value of your skills to determine if that fee is worth it to you.You're paid after the task is completed through direct deposit to a checking account. Payment typically takes a few days to appear in your account.RequirementsYou need to be at least 18 to start working with TaskRabbit.Prospective Taskers must also pass a background check.20. Become a private tutorParlay your math, science, foreign-language or test-prep expertise into a lucrative side gig by becoming a private tutor. You can tutor people online or in-person.What you charge can depend on your experience, expertise and what’s in demand. To get started, see what types of tutors are needed on Craigslist, or create a profile on sites like Tutor.com or Care.com. You can also advertise your services at local schools and community centers.Total time: Varies by subject matter. Some companies might require a minimum availability per week (e.g., Tutor.com requires 5 hours).Setup: Can be a bit involved.How easy to start: Students will have to find you, and that might take a while.Age threshold: Any.How fast you'll get paid: Depends on the platform; check the terms of service.Need to knowStartup time depends on demand in your area. It could take a while before you get your first student.If you haven't tutored before, you'll want to allow for time to prep so students feel like they're getting the most out of their time with you.How quickly you get paid depends on whether you tutor via a platform or in-person; either way, it likely won't take long.RequirementsYou'll need deep knowledge in an area that people need help understanding, like mathematics, a foreign language or test prep.Educational requirements might apply. Some tutors might be required to be currently enrolled in a four-year university or have at least a bachelor's degree from an accredited four-year university.21. Drive for Uber, LyftJoin Uber or Lyft (or both) and make money by driving passengers around. Just don’t forget to factor in gas and maintenance costs. You need an eligible car in good condition and must agree to a background check and a review of your driving history. Learn how to become an Uber driver or how to make money as a Lyft driver.Total time: Depends on your market demand.Setup: A few weeks.How easy to start: Not difficult, but you'll need the right type of vehicle.Age threshold: Varies by region from 21-25.How fast you'll get paid: Very fast. Either instantly or within days.Need to knowAllow some time for the application process, background check and car inspection.Lyft and Uber can pay you instantly through a debit card or transfer earnings to your bank account pretty quickly.RequirementsA car with four doors. It must also meet other requirements, such as year, physical condition, etc.Depending on your state, you may need to have at least one year of licensed driving experience to drive for Lyft. Uber requires at least one year of licensed driving experience in the U.S. (or three years if you’re under 25).Let your car insurance company know of your plans before you start driving.Nerdy PerspectiveDriving for Uber was not my favorite side hustle, but it was accessible and the little money I made over a week-long test came quickly. I'd be worried about gas costs, wear and tear on my car, and lots of awkward silence if I were to do it long term, though. I was happier when I delivered food and groceries. I delivered with DoorDash and became a full-service Instacart shopper for short stints in 2024, and found these driving gigs to be less stressful than doing rideshare. Trips were shorter, I spent less time in the car and it was easy to get started, even in my small town.Profile photo of Tommy TindallTommy TindallI've tried driving gigs22. Make deliveries for Amazon, Uber EatsTake advantage of the growing delivery trend and sign up for a service like Instacart, Uber Eats, Postmates, DoorDash or Amazon Flex. You get paid per delivery, in most cases, and can even earn tips. A car isn’t always required — Postmates and DoorDash let you use a bike or scooter to make deliveries in some cities. However, a background check is almost always part of the deal. Learn more about how to get started with Amazon Flex, Uber Eats and Instacart.Total time: Depends on your market demand.Setup: About a week.How easy to start: Easy, if you have dependable transportation.Age threshold: Varies by the service, but at least 18.How fast you'll get paid: Varies by vendor.Need to knowThe background check can take a few days, and timing can vary.Payments from these services also vary, but are generally issued weekly or quicker.RequirementsYou'll need a way to deliver items. It could be a car, scooter or bike, depending on the service.A smartphone is necessary to accept and process jobs.Each delivery service has a minimum age requirement, but it varies by service.23. Find work as a housesitterIf you’re willing to watch someone’s home — and maybe feed the pets, water the plants and take out the garbage — become a housesitter. Tap your personal network for referrals or try out HouseSitter.com, which connects homeowners with housesitters.Total time: Depends on your market demand.Setup: Minutes — or more if you try to drum up business by referrals.How easy to start: That can depend on the need in your area.Age threshold: Varies by site.How fast you'll get paid: Typically at the end of a gig; make arrangements with clients.Need to knowYou can create a profile on HouseSitter.com in a matter of minutes, though it may take time to secure your first housesitting gig.You typically get paid by the homeowner when you complete your gig.RequirementsMost sites have an age requirement.24. Sign up to be a mystery shopperBusinesses often want to know how they’re performing from a customer’s perspective. Sign up to be their eyes and ears. You can apply online via sites like IntelliShop, BestMark and Sinclair Customer Metrics. Just beware of scams and do thorough research before signing on.Total time: Varies by site.Setup: Applying takes little time, but approval can take a while.How easy to start: Relatively easy if you have required transportation and tech.Age threshold: May vary by site.How fast you'll get paid: Varies by company.Need to knowThe application process is typically quick, but then it's in the company's hands. It can take days, or more, to assess your application, depending on demand.Payout timing and method vary by company. BestMark, for example, issues payments monthly.RequirementsMost mystery shopping services have an age requirement. You have to be at least 18 to shop for BestMark.Depending on the service, you may need internet access.25. Put your drone to workSome of the best camera drones can cost less than $500 — and you can use that investment to make money. Real estate agents turn to drone pilots to generate aerial photos of a home's exterior, and even neat fly-through videos of interiors, which can translate to a relatively easy money-making venture.If you're willing to learn more advanced skills, like drone mapping, you can often charge more for clients seeking aerial inspections and land mapping.You need to pass a test to become a drone pilot and register your drone with the Federal Aviation Administration. Then, you can apply for flying gigs.Total time: Depends on demand.Setup: You'll need to make time to pass a test, and then find clients.How easy to start: If you already have a drone, you're likely qualified.Age threshold: 16+.How fast you'll get paid: Varies by company.",
                                  "producing activism Activism consists of efforts to promote, impede, direct or intervene in social, political, economic or environmental reform with the desire to make changes in society toward a perceived common good. Forms of activism range from mandate building in a community (including writing letters to newspapers), petitioning elected officials, running or contributing to a political campaign, preferential patronage (or boycott) of businesses, and demonstrative forms of activism like rallies, street marches, strikes, sit-ins, or hunger strikes.Activism may be performed on a day-to-day basis in a wide variety of ways, including through the creation of art (artivism), computer hacking (hacktivism), or simply in how one chooses to spend their money (economic activism). For example, the refusal to buy clothes or other merchandise from a company as a protest against the exploitation of workers by that company could be considered an expression of activism. However, the term commonly refers to a form of collective action, in which numerous individuals coordinate an act of protest together.[1] Collective action that is purposeful, organized, and sustained over a period of time becomes known as a social movement.[2]Historically, activists have used literature, including pamphlets, tracts, and books to disseminate or propagate their messages and attempt to persuade their readers of the justice of their cause. Research has now begun to explore how contemporary activist groups use social media to facilitate civic engagement and collective action combining politics with technology.[3][4] Left-wing and right-wing online activists often use different tactics. Hashtag activism and offline protest are more common on the left. Working strategically with partisan media, migrating to alternative platforms, and manipulation of mainstream media are more common on the right (in the United States).[5] In addition, the perception of increased left-wing activism in science and academia may decrease conservative trust in science and motivate some forms of conservative activism, including on college campuses.[6] Some scholars have also shown how the influence of very wealthy Americans is a form of activism.[7][8]Separating activism and terrorism can be difficult and has been described as a 'fine line",
                                  ]# treat this as a document
        if problem_search:
            print('for problem searches instead of life dag search just add problem as an additonal objective to search for and weight stuff more heavily')
            prompt_objectives_to_score_list=prompt_objectives_to_score_list=problem_search     
        
        # create person_organizaion_action_context_list
        # will prolly change this at one pointt o name rather than link
        print('this is retrieivng the info for consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action ')
        user_position_context= str(user_positional_info_dic['places_lived'])
        user_position_context= user_position_context+ " "+str(user_positional_info_dic['work_experience'])
        person_organizaion_action_list_dic={}   
        
        for i2, actionn in enumerate(all_guide_life_action_list_with_effects_dic["action"]):
            linkkk=all_guide_life_action_list_with_effects_dic["link"][i2]
            if linkkk in person_organizaion_action_list_dic:
                person_organizaion_action_list_dic[linkkk].append(actionn)
            else:
                person_organizaion_action_list_dic[linkkk]=[actionn]
                
        person_organizaion_position_list_dic={}        
        for i3, position_words in enumerate(all_guide_life_action_list_with_effects_dic["position_of_other_people_places_and_things"]):
            linkkkk=all_guide_life_action_list_with_effects_dic["link"][i3]
            #print(f"linkkkk {linkkkk}")
            if linkkk in person_organizaion_position_list_dic:
                person_organizaion_position_list_dic[linkkkk].append(position_words)
            else:
                person_organizaion_position_list_dic[linkkkk]=[position_words]
     
        
        for obejctive_doc in prompt_objectives_to_score_list:
            sorted_life_action_dic_for_objective={}
            # need to get life action list
            # maybe store in database life action list
            # real estate invest and poltiics
            for iterr, life_action in enumerate(all_guide_life_action_list_with_effects_dic['action']):               
                life_sub_action_lists=all_guide_life_action_list_with_effects_dic["sub_steps_to_complete_actions"][iterr]
                linkkkkk=all_guide_life_action_list_with_effects_dic["link"][iterr]
                work_experience=all_guide_life_action_list_with_effects_dic["work_experience"][iterr]# use this to rank life_action_list in respect of objective give it a score
                projects_interested_in=all_guide_life_action_list_with_effects_dic["projects_interested_in"][iterr]# use this to rank life_action_list in respect of objective give it a score
                guide_person_personal_info_context=work_experience + " "+projects_interested_in

                effects=all_guide_life_action_list_with_effects_dic["other_things_effected"][iterr]# use this to rank life_action_list in respect of objective give it a score
                life_action_context=life_action+ " "+life_sub_action_lists+" "+effects
                user_positional_info_context=str(user_positional_info_dic["property"])# use this to rank life_action_list in respect of objective give it a score
                user_positional_info_context=user_positional_info_context+str(user_positional_info_dic["skills"])
                user_positional_info_context=user_positional_info_context+str(user_positional_info_dic["connections"])
                
                print("incorporate problem search_type into life action dag search save on work")
               #print('we are limited by qualaites of input data so only get use these in choosing functions to sort actions so probably best way to incporrate game theory is considering other people involved in action/ environment of action')
                guide_person_life_action_list_score=self.create_document_similarity_score(guide_person_personal_info_context,obejctive_doc,typee="get_guides_life_action_list_score_for_objective")
                user_personal_info_score=self.create_document_similarity_score(user_positional_info_context,obejctive_doc,typee="get_user_perosnal_info_score_for_objective")
                #print(guide_person_personal_info_context)
                #print(user_positional_info_context)
                user_compared_to_guide_score=self.create_document_similarity_score(user_positional_info_context,guide_person_personal_info_context,typee="get_user_perosnal_info_score_for_guide_personal_info")
                action_with_respect_to_objective_score=self.create_document_similarity_score(life_action_context,obejctive_doc,typee="get_action_list_score_for_objective")
                print('STILL NEED TO WRITE THIS ONE use random qualtities we have')
                other_qualities_score=self.create_document_similarity_score(life_action_context,obejctive_doc,typee="use_all_qualtities_of_input_data_strategies_and_personal_info_in_different_ways_to_help_rank_action")
                # dont wan tto remove option want to just reduce using some factor 
                # would rathe have exact distances for resource you have are proxmitate to other resources
                # where do i get numeric distance data
                
                print('numeric')
                time_to_complete_action=all_guide_life_action_list_with_effects_dic["time_to_complete_action"][iterr]
                monetary_cost_of_action=all_guide_life_action_list_with_effects_dic["monetary_cost_of_action"][iterr]      
                money_to_complete_action_score,time_to_cmplete_action_score=self.consider_factors_such_as_time_to_complete_action_monetary_roi_cost_of_action_and_action_effects(time_to_complete_action,monetary_cost_of_action)# like know enemy can do x actions so to avoid getting back stabbed do y
                # done is the one one above
                
                user_location_data_list=user_positional_info_dic["places_lived"]
                print('may need to split this list at one point for now we good though')
                #user_location_data_list=user_location_data_list[1:-1].split(",")

                action_location_data_dic_list=all_guide_life_action_list_with_effects_dic["action_geo_locations"][iterr]
                action_location_data_dic_list=action_location_data_dic_list[1:-1].split(",")
                place_of_people_and_things_score=self.consider_numeric_distances_and_placement_of_other_people_places_and_things_when_choosing_action_use_map(action_location_data_dic_list,user_location_data_list)
                # done the above
                print('use lemma and make it so good for exaxct word matches works need to write these algorhim and gahter the data ')               
                # look at all the actions past data stuff
                user_past_actions_list=all_guide_life_action_list_with_effects_dic["user_past_actions_list"][iterr]
                user_past_actions_list=user_past_actions_list[1:-1].split(",")

                user_time_past_use_of_action_list=all_guide_life_action_list_with_effects_dic["user_time_past_use_of_action_list"][iterr]
                user_time_past_use_of_action_list=user_time_past_use_of_action_list[1:-1].split(",")
                numer_of_last_use_of_action_score,time_from_last_use_of_action_score,proxmity_of_action_to_other_past_used_action_score=self.use_patterns_in_strategies_help_rank_action(user_past_actions_list,user_time_past_use_of_action_list,life_action)# like previous strategies data used etc 
                
                
                #done still need to write it but idea is there
                resources_required_for_action_context=str(all_guide_life_action_list_with_effects_dic["resources_required_to_perform_action"][iterr])
                personal_resources_context=str(all_guide_life_action_list_with_effects_dic["assets"][iterr])
                resources_score=self.consider_distance_of_resources_you_have_avilable_to_you_vs_resources_required_to_take_action(resources_required_for_action_context,personal_resources_context)
                # other peoples available actions are all their life action lists
                # create life action context for each indivudal person/org/link
                # link is key        
                print(' the inputs are generaqted up top for this function consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action')
                current_life_action_list=person_organizaion_action_list_dic[linkkkkk]
                other_people_postiion_score,other_people_available_action_score=self.consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action(str(current_life_action_list), user_position_context,person_organizaion_position_list_dic,person_organizaion_action_list_dic)                    
                weights = [14.424, 14.421, 14.417,11.324,11.324,11.324,11.324,-2.324,100.324,100.324,100.324,100.324,100.324]
                # make the distance of things score negative
                # money and time most valuable factors
                amount = [guide_person_life_action_list_score, 
                          user_personal_info_score, 
                          action_with_respect_to_objective_score,
                          user_compared_to_guide_score,
                          numer_of_last_use_of_action_score,
                          time_from_last_use_of_action_score,
                          proxmity_of_action_to_other_past_used_action_score,
                          other_people_postiion_score,
                          other_people_available_action_score,
                          resources_score,
                          place_of_people_and_things_score,
                          money_to_complete_action_score,
                          time_to_cmplete_action_score]
                weighted_avg_score = np.average(amount, weights=weights,axis=0)
                # need to create sub lists
                print('need to create proper life_sub_action_lists to get this to work')
                sorted_life_action_dic_for_objective[weighted_avg_score]=[life_action,life_sub_action_lists,effects,obejctive_doc]  
                #print(sorted_life_action_dic_for_objective[weighted_avg_score])
                # will need to write the below functions later
                

                print('''super imporant to consider other plahyers moves! think sc2 and civ pro
                      by anticipating other peoples moves then limit their future moves with your moves you can better precift their future move
                      then can counter this move and beat them''')
                      
                      
                
                
                    
                          
            #print(sorted_life_action_dic_for_objective)   
            #input()
            print('each tuple output of sorted is the key as item zero and then values in values as subsequent items')
            
            sorted_life_action_tuple_for_objective=sorted(sorted_life_action_dic_for_objective.items(),reverse=True)   

            sorted_life_action_tuple_for_objective=sorted_life_action_tuple_for_objective[:20]# show top 10 hits
            print(sorted_life_action_tuple_for_objective)
            for i, sorted_life_action_tuple in enumerate(sorted_life_action_tuple_for_objective):
                #print(sorted_life_action_tuple[1])
                key_value_score_of_og_dic=sorted_life_action_tuple[0]#key value of the orignal diciotnary              
                value_tuple_of_og_dic=sorted_life_action_tuple[1]# value list of the orignal dictionary key
                testing=True
                print('need to remove testing here and fix sub tasks')
                if testing==False:
                    sub_task_list=value_tuple_of_og_dic[1].split(",")
                    for i2, sub_actionn in enumerate(sub_task_list):
                        if sub_actionn:
                            temp_dic={"strat_delimiter":i,
                                "step_delimiter":i2,
                                "task":value_tuple_of_og_dic[0],
                                "sub_task":sub_actionn,                        
                                "effects":value_tuple_of_og_dic[2],
                                "typee":value_tuple_of_og_dic[3]}   # typee is objective  
                            print(temp_dic)

                
                if testing==True:
                    temp_dic={"strat_delimiter":i,
                        "step_delimiter":i2,
                        "task":value_tuple_of_og_dic[0],
                        "sub_task":value_tuple_of_og_dic[1],                        
                        "effects":value_tuple_of_og_dic[2],
                        "typee":value_tuple_of_og_dic[3]}   # typee is objective  
                    print(temp_dic)
                    final_all_sorted_life_action_for_objective_dic_list.append(temp_dic)                   

                    
               
                    final_all_sorted_life_action_for_objective_dic_list.append(temp_dic)                   
        return final_all_sorted_life_action_for_objective_dic_list
            #print(sorted_life_action_tuple_for_objective[0][0])
            #print(sorted_life_action_tuple_for_objective[1][0])#  first value is the key, 0 is key value 1 is values value
            #input()

            #print(sorted_life_action_tuple_for_objective[0])
            #input()
            #print(sorted_life_action_tuple_for_objective[1])
            #input()

            #print(sorted_life_action_tuple_for_objective[1][0])
            #input()

            #print(sorted_life_action_tuple_for_objective[1][1][0])
            #input()

            #print(sorted_life_action_tuple_for_objective[1][2])

            #input()
            # tuple
            # list 

            #values is 1
            #print(sorted_life_action_tuple_for_objective[0][1][1])#subaction
            #print(sorted_life_action_tuple_for_objective[0][1][2])#effects

            #print(sorted_life_action_tuple_for_objective[0][1][3])#objective
            #print(sorted_life_action_tuple_for_objective[0][1][0])#action

            #print(sorted_life_action_tuple_for_objective[0][2])
            #print(sorted_life_action_tuple_for_objective[0][3])
            #print(sorted_life_action_tuple_for_objective[0][4])
            #life_sub_action_lists=sorted_life_action_tuple[1].split(",")


    #print('# trying to inciprorate game theory with this function below')
    #print('consider other people places and things position info to ancticpate their possible action so the action we choose anticpates these factors and counters them thinking moves ahead')
#HOW DO I DO THIS DIFFERENTLY neeed to figure out attribute of these to rank so can find best action rather than most similar
# well best is probably personal so use personal info dic to figure out best to maxmize objecvvie
# placement of other people and things should be numerical like distances               
# compare resources context against life action resoruces  context and higheter score if more common resoruces or words
# because easier to take action
# can have multiple scores or weights
   #print('please write this roi one and start to consider factors/qualitites of action as input function and think of choice of action as output in nn')
   # THESE TWO WILL BE NUMERIC FUNCTIONS THAT WE EWILL USE THEY ARE SUPER IMPORTANT WILL BE WEIGHYED HEAVILY
    
    #print('keep buildign functions using the below funciton idea super powerful use input data qualtities in different ways to rnak actions')
    #info_about_other_people_score=self.use_info_about_other_people_when_action_was_taken_to_help_rank_action()# trying to inciprorate change theory with this
    #other_people_postiion_score=self.consider_other_peoples_and_orgnaizaions_positionality_and_there_avilable_actions_to_best_pick_your_action()# like know enemy can do x actions so to avoid getting back stabbed do y
    #resources_score=self.consider_what_resources_you_have_avilable_to_you_to_use_to_take_action_and_rank_action()# like know enemy can do x actions so to avoid getting back stabbed do y
    #place_of_people_and_things_score=self.consider_placement_of_other_people_places_and_things_when_choosing_action()
    #print('the way to incorporate game theory into choosing/ranking action is by conisdering other people and environment when aciton was taken')
       #print('we are limited by qualaites of input data so only get use these in choosing functions to sort actions so probably best way to incporrate game theory is considering other people involved in action/ environment of action')
        #self.use_all_books_and_artcles_and_websites_on_game_theory_and_strategy_history_of_conflict_and_world_to_choose_actions_or_create_functions_to_choose_actions()
        #self.use_all_books_and_artcles_and_websites_in_game_theory_category_to_choose_actions_or_create_more_functions_to_choose_actions()
        #self.use_model_world_and_game_theory_to_choose_best_action_anticipating_other_players_moves_and_world_and_generate_strategy()
        #self.use_patterns_from_examples_to_build_strats_and_acquire_powerful_info()

        # by anticpating other peoles moves limit their future options with your move so you win
#sort into correct order    
#example = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
#want distances or proxmity for a couple of word ones rather than exact word matches what if just use synonyms so exact word matches gets better
# use action context for this # if certain simialr available actions lower score
#info_about_other_people_score=self.create_document_similarity_score(life_action_context,obejctive_doc,typee="use_info_about_other_people_when_action_was_taken_to_help_rank_action")
#other_qualities_score=self.use_all_qualtities_of_input_data_strategies_and_personal_info_in_different_ways_to_help_rank_action()# trying to inciprorate change theory with this

     
    
                # ranked it in respec tto personal info
                # then ranked seperatly with respect to objective
                
                # how do you take into account both
                # average
                # do weighted averages
                
                
                # how do i gert labels
                #without lables does not work
                # score comes out for that particular objective
                
                # use nn here maybe for speed      
                
            # take the objective itself and its relationship to the life_action_list
            # and the perosnal characeristic of the perosn into account
            
            #create scores for each category of objective which take the objective and perosnal characeritcs into account
            #then upload the top results for each category  
            
        ###fYoKuAhEsPaNrAtDoIfJ 
        # limit action space to those you can complete given your podsitonality or resources you currently have access to
        #then sort most relevent actions to complete the objective of these possible actions
        # mask invalid actions first thing
        # tree search
        #sort or search the action space
        # to find the best action
        # might just have one search function isntead of two for problem dag
        if search_type=="life_dag":
            for actionn in action_space_with_effects_dic:
                # choose specific actions based on positionality               
                # use these to search and sort the actions
                positional_info_dic
                objective   
                current_action_value=""
                action_good=""
                if action_good:  
                    # place actionn in the dic list that will be displayed on website
                    for i11, stored_actionn in enumerate(sort_life_dags_dic_list):
                        if current_action_value>stored_actionn["valuee"] and i11!=len(sort_life_dags_dic_list):
                           #print('hi')
                            sort_life_dags_dic_list.insert(i11,current_action_value)
                            break
                        if i11==len(sort_life_dags_dic_list):
                            sort_life_dags_dic_list.append(current_action_value)  
                            break
                        if current_action_value<=stored_actionn["valuee"]:                           
                            continue                        
                else:
                    continue
     
                
  
        if search_type=="problem_dag":
            for actionn in action_space_with_effects_dic:
                positional_info_dic
                objective                
                if action_good:
                    #sort action in list based on its value
                    for i11, (line_of_code, average_match_for_line_of_code_line_of_code_placement) in enumerate(line_of_code_value_dic.items()):
                        average_match_for_line_of_code=average_match_for_line_of_code_line_of_code_placement[0]
                        line_of_code_placement=average_match_for_line_of_code_line_of_code_placement[1]

                        if i11==0:
                           #print(average_match_for_line_of_code)
                            sort_life_dags_dic_list.append([average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                            continue
                        for i,sorted_match_values in enumerate(sorted_line_code_match_list):
                            sorted_match_num=sorted_match_values[0]
                            if average_match_for_line_of_code>=sorted_match_num:
                                # at this position
                                #print(listt)# the thing in that spot shifts right when using insert
                                sort_life_dags_dic_list.insert(i,[average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                                break
                            if i==line_of_code_value_dic_len :
                                sort_life_dags_dic_list.append([average_match_for_line_of_code,line_of_code_placement,line_of_code[:20]])
                                break
    
                    
                    
                else:
                    continue
                
           #print('hi')
            
        
        example= [{"problem_being_solved":"problem", "document":"document","document_content":"document_content"}] 
        #sort_life_dags_dic_list.append(example)
        
        
        return sort_life_dags_dic_list

    def fill_in_dic_with_copilot_and_chatgpt(self,person_comp_info_dic_with_action):
        """ """
    def fill_in_dic_with_duck_duck_go(self,person_comp_info_dic_with_action):
       """ this function will get results from various search browsers and then upload them to """
       import spacy
       import time
       # spacy should be loaded now
       #testing=True
       #if testing==True:
       #    self.nlp = spacy.load("en_core_web_sm")
       problemm=person_comp_info_dic_with_action["action"]
      #print(problemm)
       self.problem_recorded=problemm
       self.automated_problem_galaxy_dic={}
       # run this as a subprocess or multiprocess the values
       # for retrieve problem data from web
       # run timer on this
       #start_time=time.time()
       saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
       #end_time=time.time()
       #change=end_time- start_time
       #print(change)
      #print('retrieving link data')
       for text_link in saved_text_from_website_and_link_list:
           #start_time=time.time()
           single_website_text=self.pre_process_text(text_link[0])
           final_sentence_list=self.divide_text_into_sentences(single_website_text)
           #start_time=time.time()
           for sentence in final_sentence_list:
               spacy_dic=self.label_sentence_with_spacy(sentence)
               person_comp_info_dic_with_action=self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(spacy_dic,person_comp_info_dic_with_action)
           #end_time=time.time()
           #change=end_time- start_time
           #print(change)
           #print('processing single link data')
       #print(self.automated_problem_galaxy_dic)
       return person_comp_info_dic_with_action
    def generalize_action_words_to_make_it_more_applicable_to_people_and_useable(self,actionn):
        """ run spacy over the action and if any entites show up replace hte eneitty with the gneeric entity value
        like if a name is in the action replace the name with NAME etc"""
        import re
        import time
        import copy
        import spacy
        #testing=True
        #if testing==True:
        #    self.nlp = spacy.load("en_core_web_sm")
        doc = self.nlp(actionn)
        generalized_action=copy.deepcopy(actionn)
        #actionn_word_list=actionn.split(" ")
        for ent in doc.ents:
           #print(f"{ent.text},{ent.label_}")
           #print('hehe')
            textt=ent.text
            labell=ent.label_
            if ent.label_ == "PERSON":
                generalized_action=re.sub(textt,"person",generalized_action)                     
            if ent.label_ == "ORG":
                generalized_action=re.sub(textt,"organizaion",generalized_action)  
            if ent.label_ == "DATE":
                generalized_action=re.sub(textt,"date",generalized_action)
            if ent.label_ == "MONEY":
                generalized_action=re.sub(textt,"money",generalized_action)        
            continue 
          
            continue     
        return generalized_action    
    #matched_word=re.search(textt,actionn)
    #if matched_word:                        
        #matched_word_span=matched_word.span()
        #actionn.insert([matched_word_span[0]:matched_word_span[1]]) 
            
    def get_sub_action_list_data_use_patent_data_and_other(self,person_comp_info_dic_with_action):
        """#https://data.uspto.gov/bulkdata/datasets/ptgraps?fileDataFromDate=1976-01-06&fileDataToDate=2001-12-25
        use this script to get more patent data in busienss fucntons in getting_patent_data"""
        #just look through other actions and suggest action lists as sub actions
        # upload all possible action_lists
        #upload patent data as actions if possible
        #then figure top possible sub actions lists that could be used for this action
        #how to incorporate patent # patent will be not a sub task so skip this for now       
        #for action_list in all_possible_action_list_list:          
        # do a duckduckgo search to find  sub action data how do i
        import spacy
        # spacy should be loaded now
        #testing=True
        #if testing==True:
        #    self.nlp = spacy.load("en_core_web_sm")
        self.search_through_patents_to_get_sub_actions()
       #print('still need to write this function')
        problemm="what are the steps i would take to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0])
            sub_action_list=self.create_sub_action_list(single_website_text)
            person_comp_info_dic_with_action["sub_steps_to_complete_actions"].append([sub_action_list,text_link[1]]) 
        return person_comp_info_dic_with_action
     #for action_list in action_sentence_list_list:
    #final_sentence_list=self.divide_text_into_sentences(single_website_text)          
    #for sentence in final_sentence_list:
        #spacy_dic=self.label_sentence_with_spacy(sentence)        
        #model off of these
        #action_sentence_list_list=self.process_crawl_data(sentence)
        #person_comp_info_dic_with_action=self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(spacy_dic,person_comp_info_dic_with_action)
        # parse for action sentnece
        # then savve as sub step        
        #person_comp_info_dic_with_action=self.create_galaxies_and_transformations_from_text_for_problem_using_pos_in_sentences_ADP_noun_relationship(spacy_dic,person_comp_info_dic_with_action)
#print(self.automated_problem_galaxy_dic)
        # parse patent data and add something relevent from it to dic, maybe just get more methods from it
        # and have it as a seperate thing
    def get_placement_of_other_people_places_and_things_related_to_action(self,person_comp_info_dic_with_action):
        """sub actions to complete task are essentially 
        go to do a duckdcukgo search with a specific parameter
        then going to save the text as context 
        do i parse ?
        I think i only save snetneces maybe we will see"""
        import spacy
        problemm="what are other things i should consider relating to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)            
            person_comp_info_dic_with_action["position_of_other_people_places_and_things"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
        return person_comp_info_dic_with_action
    

    def figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(self,person_comp_info_dic_with_action,website_already_searched=False):
        """ask many more questions to send to duckduckgo here 
        figure_out_all_things_you_can_use_ask_many_questions_on_objects_in_problem_words_in_problem_and_qualtites_to_generate_expert_problem_environment"""
       #print(' upload a ton of questions of a database and use these')
       #print(' ask questions on all qualtiites of problem dic in relation to question')
       #print(' ask questions about problem words, objects in the prboelm envrionment and their qualtiies about everytrhing and max out the context')
        import re
        import spacy
        ### question 1 to ask
        problemm="what is the location i would take to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
            person_comp_info_dic_with_action["location_needed_to_take_action"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
       #print('questio1n!')
        ### question 2 to ask
        problemm="what are the resources i would take to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
            person_comp_info_dic_with_action["resources_required_to_perform_action"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma token
       #print('questio2n!')
   
        ### question 3 to ask
        problemm="what are the skills that I would take to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
            person_comp_info_dic_with_action["skills_required_to_perform_action"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
       #print('questio3n!')
    
        # ask questions about  the person or thing being discussed on wiki
        if website_already_searched==False:
           #print('# only do these for the intital run through so dont waste compute vbecause they have to do with teh link not the specific action')       
            wiki_thing_being_discussed=person_comp_info_dic_with_action["link"]
            single_link_list=re.split(r"/",wiki_thing_being_discussed)
            link_item_title=single_link_list[-1]
            #all_link_item_titles_str=".  ".join(all_link_item_titles_list)
            link_item_title=re.sub("_"," ",link_item_title)   
           #print(link_item_title)
           #print('questio4n!')
            
            ### question 4 to ask
            problemm=f"what is the history of {link_item_title}"
            self.problem_recorded=problemm
            self.automated_problem_galaxy_dic={}
            saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
            for text_link in saved_text_from_website_and_link_list:
                single_website_text=self.pre_process_text(text_link[0]) 
                lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
                person_comp_info_dic_with_action["work_experience"].append([lemmaized_text_str,text_link[1]]) 
                # parse website text to create text left over we want
                # get lemma tokens
           #print('questio5n!')
            ### question 5 to ask
            problemm="what is the biography of " + link_item_title
            self.problem_recorded=problemm
            self.automated_problem_galaxy_dic={}
            saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
            for text_link in saved_text_from_website_and_link_list:
                single_website_text=self.pre_process_text(text_link[0]) 
                lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
                person_comp_info_dic_with_action["work_experience"].append([lemmaized_text_str,text_link[1]]) 
                # parse website text to create text left over we want
                # get lemma tokens
           #print('questio6n!')

            ### question 6 to ask
            problemm="what are the interest of " + link_item_title
            self.problem_recorded=problemm
            self.automated_problem_galaxy_dic={}
            saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
            for text_link in saved_text_from_website_and_link_list:
                single_website_text=self.pre_process_text(text_link[0]) 
                lemmaized_text_str=self.get_website_text_lemmas(single_website_text)          
                person_comp_info_dic_with_action["projects_interested_in"].append([lemmaized_text_str,text_link[1]]) 
                # parse website text to create text left over we want
                # get lemma tokens
            
        
        return person_comp_info_dic_with_action

            
            
        
        
    def identify_tools_to_solve_the_problem(self,person_comp_info_dic_with_action):
        """ask many more questions to send to duckduckgo here 
        figure_out_all_things_you_can_use_ask_many_questions_on_objects_in_problem_words_in_problem_and_qualtites_to_generate_expert_problem_environment"""
        import spacy
        problemm="what are the tools i would use to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)            
            person_comp_info_dic_with_action["tools_required_to_perform_action"].append([lemmaized_text_str,text_link[1]]) 
            # parse website text to create text left over we want
            # get lemma tokens
        return person_comp_info_dic_with_action


            
            
    def look_through_books_journals_and_other_websites_everything_have_access_to_improve_dic(self,person_comp_info_dic_with_action):
        """ask many more questions to send to duckduckgo here 
        FOR NOW WONT WE USING NTIS WHEN HAVE ACCESS TO MRORE BOOKS I WILL
        figure_out_all_things_you_can_use_ask_many_questions_on_objects_in_problem_words_in_problem_and_qualtites_to_generate_expert_problem_environment"""
        import spacy
        problemm="what are the steps i would take to " + person_comp_info_dic_with_action["action"]
        self.problem_recorded=problemm
        self.automated_problem_galaxy_dic={}
        saved_text_from_website_and_link_list=self.retreive_problem_data_from_web(problemm)
        for text_link in saved_text_from_website_and_link_list:
            single_website_text=self.pre_process_text(text_link[0]) 
            lemmaized_text_str=self.get_website_text_lemmas(single_website_text)
            # parse website text to create text left over we want
            # get lemma tokens
            person_comp_info_dic_with_action["position_of_other_people_places_and_things"].append([lemmaized_text_str,text_link[1]]) 
        return person_comp_info_dic_with_action
    def search_through_patents_to_get_sub_actions(self):
        """ will need to write htis later """
    # need to find a way to execute this in a way so they all run at once
    # and once i do that im done
    # want to run it faster like grab all the website data with selenium at once and then
    # send ti all back and prcoess it
        #from multiprocessing import Process
        #def worker_function(queue_obj, data_in):
       #result = data_in * 2
       #queue_obj.put(result)

        #if __name__ == '__main__':
        #    q = Queue()
        #    p = Process(target=worker_function, args=(q, 5))
        #    p.start()
        #    p.join()  # Wait for the process to complete
        #    output = q.get()
        #   #print(f"Output from process: {output}")
        
    
    def fill_single_website_action_dic_list_and_save_to_table(self,person_comp_info_dic_with_action_list):
        """ subprocess"""
        table_name="guide_person_positional_info_with_action_info"
        
        for person_comp_info_dic_with_action in person_comp_info_dic_with_action_list:
            # still need to get the sub method data from wiki how and patents
           #print('GENERALIZING the aciton is super important please do this!!!')
            # figure out a way to run this and return data through a pipe
            # maybe save it in a pickle temporarily
            # mybe save to a file
            # save to file
            # save to database
            # so save to a pickle then ropen
            # if pickle dont need to process code all ready to go so maybe do this because didc
            # then reupload
            # dont save to database save os temp file
            # save to a pickle
            # figure out fastest way to do this
            # maybe save to a 
            # then
            person_comp_info_dic_with_action=self.fill_in_dic_with_duck_duck_go(person_comp_info_dic_with_action) #get effects by doing this
           #print(person_comp_info_dic_with_action)
           #print('GENERALIZING the aciton is super important please do this!!!')
            #input()
            generalized_action=self.generalize_action_words_to_make_it_more_applicable_to_people_and_useable(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
            person_comp_info_dic_with_action['generalized_action']=generalized_action
           #print(generalized_action)
            #input('generalized_prompt')
            #input()
           #print('fill dic with objects and problem galaxy using the below function')
            ##https://data.uspto.gov/bulkdata/datasets/ptgraps?fileDataFromDate=1976-01-06&fileDataToDate=2001-12-25
           #print(r" use this script to get more patent data C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management\inputs\getting_patent_data.py ")                                                       
            person_comp_info_dic_with_action=self.get_sub_action_list_data_use_patent_data_and_other(person_comp_info_dic_with_action)# THIS IS KEY
           #print(person_comp_info_dic_with_action)
           #print('sub action sub list')
            #input()
            # send specific query to duckduckgo
            #and then parse website data with regular expression or spacy and look for specific websites and specific key words                    
            person_comp_info_dic_with_action=self.get_placement_of_other_people_places_and_things_related_to_action(person_comp_info_dic_with_action)
           #print('think mutliple moves ahead')
           #print(person_comp_info_dic_with_action)
            # make the things run in subprocess to make them run at the same time?
            # on seperate computer
           #print('placement of other people')
            person_comp_info_dic_with_action=self.identify_tools_to_solve_the_problem(person_comp_info_dic_with_action)
            #print('tools')                    
            #input()
            # send specific query to duckduckgo
            #and then parse website data with regular expression or spacy and look for specific websites and specific key words
            linkk=person_comp_info_dic_with_action['link']
            if linkk in self.used_questioned_links_list:
                website_already_searched=True
            else:
                website_already_searched=False 
                self.used_questioned_links_list.append(linkk)
            person_comp_info_dic_with_action=self.figure_out_all_things_you_can_use_ask_many_questions_to_generate_expert_action_environment(person_comp_info_dic_with_action,website_already_searched=website_already_searched)                                   
           #print(person_comp_info_dic_with_action)
           #print('other questions')
            #input()
            # send specific query to duckduckgo
            #and then parse website data with regular expression or spacy and look for specific websites and specific key words                     
           #print(person_comp_info_dic_with_action)
           #print('finsihed')
            self.store_value_in_sql_table(person_comp_info_dic_with_action,table_name)
            continue 
    def process_sql_data(self,sql_data_list_list,column_list):
         """ bring data  from database """
         import re
         self.search_data_dic={}
         column_list_len=len(column_list)
         for column in column_list:
             self.search_data_dic[column]=[] 
         for sql_data_list in sql_data_list_list:
             for column, sql_data in zip(column_list,sql_data_list):
                 # this should solve hte problem of code not being super usable because
                 # we subbed out commas and such to store it
                 sql_data=str(sql_data)
                 #sql_data=sql_data.replace("^","\'")
                 #sql_data=sql_data.replace("&","\"")
                 #sql_data=sql_data.replace("~",",")
                 #sql_data=sql_data.replace("?","'")
                 self.search_data_dic[column].append(sql_data) 
         return self.search_data_dic
     
        
    def retrieve_data_from_website_database(self,table_name,where_string,column_list):
     ''' ''' 
     import psycopg2
     import re
     from psycopg2 import sql
     host = '192.168.2.209'  # E.g., '192.168.1.100' or 'your-database-server.com'
     port = '5432'  # Default PostgreSQL port
     dbname = 'psp_website'  # E.g., 'myprojectdb'
     user = 'jross77'  # E.g., 'myuser'
     password = 'MeganisGreat'  # E.g., 'mypassword'
     try:
         self.conn = psycopg2.connect(host=host,
         port=port,
         dbname=dbname,
         user=user,
         password=password) 
         self.cur = self.conn.cursor() 
         column_list=re.sub("'","",str(column_list)[1:-1])
         #column_list=str(column_list)[1:-1].sub("'","")
         sql_str=f"SELECT {column_list} FROM {table_name}{where_string};"
         #print(sql_str)
         try:
             self.cur.execute(sql_str)
         except Exception as E:
             print(E)
         sql_data_list_list= self.cur.fetchall()
         #self.conn.commit()
     except Exception as e:
             print(f"Error: {e}")     
     self.cur.close()
     self.conn.close()
     print("Connection closed.")
     #print('moew')
     #input(f"{sql_data_list_list}")
     return  sql_data_list_list
   
    

 
    def generate_all_life_possible_actions_and_effects_dic(self):
        """ """
        import spacy
        # retrieve data
        self.nlp = spacy.load("en_core_web_sm")
        import requests
        import psycopg2
        import subprocess
        import pickle
        from subprocess import Popen, PIPE, STDOUT
        self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor() 
        table_name="guide_person_positional_info_with_action_info"
        wiki_pages_and_history_books_and_biographies_politics=[]
        self.used_questioned_links_list=[]
        website_already_searched=False
        
        person_comp_info_dic_with_action={         
            "action":"",
            "generalized_action":[], 
            
            "noun_and_verb_chunk_list":[],
            "noun_and_verb_chunk_pos_list":[],
            
            "action_temporal_placement_in_life_list":"#",               
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            
            
            
            
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions
            


            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],
            "intital_page_text":[],
            "object":[],


            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
            # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],# geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "money":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[],}
        
        column_name_data_type_dic={} 
        print('change this wait_for_process_finish_list if i want more proecces to run like skipping by 3 rather than 2')
        wait_for_process_finish_list=list(range(1,2000,2))
        print(f"wait_for_process_finish_list {wait_for_process_finish_list}")
        column_list=person_comp_info_dic_with_action.keys()
        for column in column_list:
            column_name_data_type_dic[column]="text"
        create_seed_link_list=False
        path_to_pickle=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Pickles\intital_link_seed_list.pickle"
        if create_seed_link_list==True:
            self.create_table_sql(column_name_data_type_dic,table_name=table_name)
            query_data=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\query.json"
            #self.create_intital_link_seed_list_pickle(query_data)
        # add used links to used link list so we dont repeat them
        table_name_column_list_dic={ "guide_person_positional_info_with_action_info":["link"]}
        sql_data_list_list=self.retrieve_data_from_local_database(table_name,"",table_name_column_list_dic["guide_person_positional_info_with_action_info"])
        search_data_dic_local=self.process_sql_data(sql_data_list_list,table_name_column_list_dic["guide_person_positional_info_with_action_info"])
        duplicates_used_link_list=search_data_dic_local["link"]

        used_link_list=[]
        for linkk in duplicates_used_link_list:
            if linkk not in used_link_list:
                used_link_list.append(linkk)

        query_data=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\query.json"
        #https://query.wikidata.org/ # get all info off of this for additonal stats
        #https://query.wikidata.org/#SELECT%20%3Fperson%20WHERE%20%7B%20%3Fperson%20wdt%3AP31%20wd%3AQ5%20%7D%0Alimit%20100%0A
        seed_links_to_crawl_list=[
            r"https://en.wikipedia.org/wiki/Category:People_associated_with_movements",
            r"https://en.wikipedia.org/wiki/Lists_of_people_by_belief",
            r"https://en.wikipedia.org/wiki/Lists_of_people_by_nationality",
            r"https://en.wikipedia.org/wiki/Category:People_by_organization",
            r"https://en.wikipedia.org/wiki/Category:People_by_occupation",      
            r"https://en.wikipedia.org/wiki/List_of_entrepreneurs",
            r"https://en.wikipedia.org/wiki/List_of_Internet_entrepreneurs",
            r"https://en.wikipedia.org/wiki/Lists_of_people_by_net_worth",          
            r"https://en.wikipedia.org/wiki/Lists_of_activists",
            r"https://en.wikipedia.org/wiki/List_of_civil_rights_leaders",
            r"https://en.wikipedia.org/wiki/Category:Internet_activists",
            r"https://en.wikipedia.org/w/index.php?title=Category:Births_by_year&from=1900",
            r"https://en.wikipedia.org/w/index.php?title=Category:Births_by_year&from=1800",
            r"https://en.wikipedia.org/w/index.php?title=Category:Births_by_year&from=1700",
            r"https://en.wikipedia.org/w/index.php?title=Category:Births_by_year&from=1600",
            r"https://en.wikipedia.org/w/index.php?title=Category:Births_by_year&from=1900",
            r"https://en.wikipedia.org/w/index.php?title=Category:Organizations_by_year_of_establishment&subcatfrom=1783%0AOrganizations+established+in+1783#mw-subcategories", ]
        website_root=r"https://en.wikipedia.org"
        clean_link_root=r"en.wikipedia.org"    
       #print('SO JUST IGNORE CONCEPTS LET IT GO INTO THEM THE SPIDER makes it easier the spyder function and make up for it in parsing ')
        prompts=["FIRST_LAST_NAME tell me about this person life","what are the steps i would take to complete ACTION"]
        specific_website_pages_to_look_at=["seed_webpage_list"]              
        from bs4 import BeautifulSoup
        ### getting all the data with the webspider
        # will ned to check if used link list works
        person_comp_info_dic_with_action_list=[] 
        pattern_list=[]
        skip_process_page_list=[]
        used_questioned_links_list=[]
        add_page_to_action_dic=True
        # this terms_not_in_link_list is the categories links that i will not get action data from
        # but will tretrieve links from using retrive links on page and then crawl
        terms_not_in_link_list=["/wiki/Category:","/wiki/List","/wiki/Lists","w/index.php?title=Category","/w/index.php?title=Lists","Wikipedia:Categories"]
        for link_root in seed_links_to_crawl_list:
            # get links on link_root page
            html,session=self.download_link_html_requests(link_root)     
            sel_soup = BeautifulSoup(html, 'html.parser') 
            body_page=sel_soup.find('div', id="bodyContent")
           #print(body_page)
            for termm in terms_not_in_link_list:
                if termm in link_root:
                    add_page_to_action_dic=False
                    break
            if add_page_to_action_dic==True:
                #if link_type=="person_and_org_word_in_link":
                    print('processing first page')
                    # if this is never written good
                    add_page_to_action_dic=False
                    person_comp_info_dic_with_action_list=self.process_crawl_data_3(sel_soup,person_comp_info_dic_with_action_list)  
                    picklee=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api\person_comp_info_dic_with_action_list.pickle"
                    with open(picklee,"wb") as f19:
                               pickle.dump(person_comp_info_dic_with_action_list, f19, pickle.HIGHEST_PROTOCOL)
                    p = Popen(["python",r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api\fill_and_save_dic_without_spacy_processing.py'])
                    out, err = p.communicate()
                    print(f"{out}, {err}")
                    #self.fill_single_website_action_dic_list_and_save_to_table(person_comp_info_dic_with_action_list)               
                    person_comp_info_dic_with_action_list=[]
                    
                
            used_link_list.append(link_root)                  
            link_retrieved_dics=self.retrieve_links_on_page(body_page,website_root,link_root,used_link_list)  
            #do not process link pattern
            print(f"intital used_link_list {used_link_list}")
            # make sub methods better
            # improve links or action parser

            for link_on_root_page, link_type_list in  link_retrieved_dics["link_none_dic"].items():
                # crawl single link on root page till all child links are dead
                #print(f'This is one of the links found on the root page {link_on_root_page} we will crawl')
                used_link_list,person_comp_info_dic_with_action_list=self.web_crawl_requests(link_on_root_page,website_root,clean_link_root,person_comp_info_dic_with_action_list,used_link_list,wait_for_process_finish_list) # crawl the whole repo site 
               #print(person_comp_info_dic_with_action_list)
               #print(f'these following functions will fill the action dic created from the {link_on_root_page} link found on root page ')  
        return "finished generating actions"
        
           #print(link_retrieved_dics["link_none_dic"])
           #print(f'this is the link root {link_root} we will find links on this page and then crawl each of these links')
           #print(' these functions will create the intital action dic list using a web cralwer need to fix web crawler')
            #print(used_link_list)
            #input("used link list")
               
    #  person_comp_info_dic_with_action=self.generate_reverse_engineer_sub_action_list_getting_other_peoples_methods(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
        ### STILL NEED TO WRITE THESE
       #print('make sure to get whole action space and then narrow down to best actions otherwise could miss a good action')
       #print('try to get all factors and do a cost benefit analysis down the line to choose best action')
       # person_comp_info_dic_with_action=self.get_placement_of_other_people_places_and_things_related_to_action()
       #print('think mutliple moves ahead')
        #person_comp_info_dic_with_action=self.use_placement_of_other_people_places_and_things_to_generate_sub_tasks_that_counter_other_peoples_actions()
        ## use htis one because it has the prewritten function i worked hard on
        #self.OLD_generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_OLD
       #print('GATHER AND USE PATENT DATA METHOD DATA TO FILL IN DIC AND WIKIHOW')
        #person_comp_info_dic_with_action=self.use_patent_data_to_fill_in_sub_task_in_dic()# THIS IS KEY
        #person_comp_info_dic_with_action=self.figure_out_all_things_you_can_use_ask_many_questions_on_objects_in_problem_words_in_problem_and_qualtites_to_generate_expert_problem_environment(person_comp_info_dic_with_action["action"])
        #person_comp_info_dic_with_action=self.identify_tools_to_solve_the_problem(person_comp_info_dic_with_action['action'])
        #person_comp_info_dic_with_action=self.look_through_books_journals_and_other_websites_everything_have_access_to_improve_dic(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
        #person_comp_info_dic_with_action=self.generate_more_actions_if_possible_ones_not_done_before_looking_at_all_possible_actions_can_take_based_on_problem_environment(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
        #person_comp_info_dic_with_action=self.design_better_action_if_possible_with_better_effects(person_comp_info_dic_with_action['action'])# extrapolate from an action taken on wiki
        #person_comp_info_dic_with_action=self.keep_updating_and_stealing_existing_business_methods_and_final_product_funnel_work_into_action_environment_to_solve_problem()
        #person_comp_info_dic_with_action=self.add_patterns_as_qualtities_of_actions()# find patterns in example of action and use these as qualtites if possible patterns
        #person_comp_info_dic_with_action=self.fill_in_dic_with_copilot_and_chatgpt(person_comp_info_dic_with_action)
        ### store all values in sql as we go 
        # patterns are super powerudl so use htem
        #try to consider things not done before but related to this action                     
        # get effects and other attributes to add to the dictionary
        # this will use the pyautogui script  or we will do this locally up to you        
    
        # these are valuable dont throw these away
        use_other_sas_resources=[""] # use all sas engines action_list_info info
        specific_website_pages_to_look_at=["wikipeida","wikiinfo","open_source_book_websites","history_books","biographies"]
        everything_else_i_can_use=["https://en.wikipedia.org/wiki/Main_Page","https://query.wikidata.org/"]
        ai_models=["https://chatgpt.com/","anphroic","https://gemini.google.com/app?is_sa=1&is_sa=1&android-min-version=301356232&ios-min-version=322.0&campaign_id=bkws&utm_source=sem&utm_source=google&utm_medium=paid-media&utm_medium=cpc&utm_campaign=bkws&utm_campaign=2024enCA_gemfeb&pt=9008&mt=8&ct=p-growth-sem-bkws&gclsrc=aw.ds&gad_source=1&gad_campaignid=21015480427&gclid=Cj0KCQjwjJrCBhCXARIsAI5x66Xdyb-GEdtHvNB9BreypszAJgiet5xk-2v3krNv0ehpttU8AlQ5HgoaAruPEALw_wcB","https://copilot.microsoft.com/chats/SvwnU8ebuKve3Vz4RqqKJ"]# use all free ai models to gather action_list_info info
        search_engines=["https://www.google.com/","https://duckduckgo.com/","https://you.com/","https://yep.com/","https://ca.yahoo.com/?p=us","https://www.bing.com/?toWww=1&redig=5012FBED72054BC4BB567414433FDC9F"] # use all search engines action_list_info info
        example= {         
            "action":"",
            "action_temporal_placement_in_life_list":"#",
            
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "tools_needed":[],
            "other_things_effected":[],
            "transformations":[], 
            "number_of_people_impacted":[],
            "object":[],

            "sub_steps_to_complete_actions":[] , 
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],

              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],# place as key geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],                 
              }
        
        extra="""make sure that qualities of object are associated with specific transformations so have unique effects 
    so look at every persons lives and actions they took in their lives
    then use this to determine best actions to take 
    given a specific circumstanxce for a person to accomplish a specific objective
    to generate all the actions look at peoples lives to generate strategies and actions within strategies       
    so the same or similar actions should have same or simlar effects 
    if another person takes it so that is the thing we rely on here      
    retrieve people life action set
    and there personal info# assuming its legal
    # just display life_action_lists in on the website
    # truncate [:1] life_action_list displayed based on someone personal information
    like there age or other perosnal factors then only show actions relevent to them        
    #sort how?      
    then when someone inputs there perosnal info can see all life_action_set people took in similar situations 
    and outcomes for those people
    more example the strategies or action_sets are peoples actual lives who were successful like mlk
    or greta thunberg or elon musk
    or dad or mom
    look at their lives for info
    wiki info
    wikipeida
    other pages on internet
    gather infromation
    create action list from peoples actions
    # worry about this latrrt
    do need to worry about this because if dont collect correct data can you use downstream so lets look
    then find simlar person to you and see next actions you should take ot get best effects
    use every means possible      
    ### information to gather with this script fill below dic for each action found
    1. 
    guide_person_personal_info that mirrrors user qualtities
    sooo these include add these for each action the guide person takes
    2. actions the person took in some sort of temporal order life life_action_list
    actions_they_took_in_their_life_dag_and qualtiies of these actions
    life_action_context
    #
    gather sub steps to complete the given action as well and use this to fill sub step table
    so
    
    
    problem:write algorhim to gather  life action list information  to  figure out how to dviide this and which websites/books to pick
    HOW DO I DIVIDE THIS
    
    just do all people stop worrying and use data to figure out how to rank life dag
    
    
    What sites do i want to crawl
    or do i crawl all sites
    # and how do i history repeats itself
    look at all categories of books and websites with simialr information
    history
    biographies
    use this and parse this info to fill dicitoanries of actions
    these sites will have better data highest qualtity probably
    so use these
    facebook is shit could still be useful though
    use higher qualtiy to get specific things in dataset
    like som summaries are better than others
    
    
    
    ### divide successful people by professions and make objectives profession based? so can see action take depending on objective
    
    only add to database: only want people life aciton list that got effects that maxmized objective
    so like for maxmizing activism objective find best activists that made biggest effect
    for making most money objective look at richest people or greatest change in networth and look at their lives
    for helping most people objective look at people who have made big difference and look at their lives
    for politicians objective look at people who became most successful polticians and their life actions 

    # this way we know actions in life action database 
    #will always come up with actions to maxmize objective because know 
    #all the actions stored in the database are great actions for the objective
    # so there is no point in searching because they are all good

    find info on people on:
    find persons  first and last name name and then do a search
    try wikipeida first
    then biographies
    then history books
    
    spacy to look through text and getname of person
    """
    #guide_people_net_wor=r"https://en.wikipedia.org/wiki/Lists_of_activists"
    #guide_people_civ=r"https://en.wikipedia.org/wiki/List_of_civil_rights_leaders"
    #guide_people_intr_act=r"https://en.wikipedia.org/wiki/Category:Internet_activists"
    #guide_people_net_wor=r"https://en.wikipedia.org/wiki/Lists_of_people_by_net_worth"
    #guide_people_inr=r"https://en.wikipedia.org/wiki/List_of_Internet_entrepreneurs"
    #guide_people_entr=r"https://en.wikipedia.org/wiki/List_of_entrepreneurs"# direct
    #guide_people_root=r"https://en.wikipedia.org/w/index.php?title=Category:Births_by_year&from=1900"
    #orgnaizaion_root="https://en.wikipedia.org/w/index.php?title=Category:Organizations_by_year_of_establishment"
    
        # how do i avoid concepts
        # what do i do if a concept shows up
        #who cares just dont click on links in this page
        # and if concept talks about someone or a business taking an action great
        # otherwise just screw it though
        # save the page name 
        # but based on text on page that is how we attribute the nouns
        # focus mostly on the parsing here
        # just want people and organizaions
    # use this as well to link up to stuff
    # looking to advise everyone so just do everyone
    # and then search through all of the life action lists using proper context
    # add more people as needed
    # build gpt model to do this
    #https://query.wikidata.org/ 
    # want websites that get us data of peoples lives that would be good data
    # and would give sactions that would  maxmize the objectives we are seeking
    
    
    # add a delimiter that the action was done by a orgfnaization
    # bascially find all actions by organizations and people
    # then build action system based on current position
    # or problem you want to solve
    # but edit actions slightly to be more generic
    
    # law is best repository of actions you can take because it regulates the acitons you can take
    # add more as i find them
    
            
        # parse html by this div using beautiful soup
        # and just click all links inside it
        # and add actions as you go
        #<div id="bodyContent" class="vector-body ve-init-mw-desktopArticleTarget-targetContainer" aria-labelledby="firstHeading" data-mw-ve-target-container="">
        ### parsing part    
        

        # find the action sentences and who the action sentence is about and other information
        # also send out other requests to improve the values we have for that action such as its sub actions
        
        

        
        # then just need to distinguish between
        #action and non action sentence and who it is attribtued to
        # use spacy to do this
        
        
        # keep it simple and just manually program it
        #for each root
        # now create crawler and
        # parser
        # divide between action sentence and non action sentence and record page name etc
        # and organizaion name and other info i can find on them
        # do additonal searches as necessary to get sub actions etc
        # and other info
        # and or to generlaize the actions so they make more sense        
        
        # get website link   
        # get text from website
        #parse text
        # add action sentence about someone to the persons life action dic
        # ignore others
        # also note persoanl info on person from wiki data and other soruces
        # maybe use spacy for this too
        # do additonal searches as necessary to improve the persons info on each action
        
        #requests and then get this part of html
        # how to disthughs between good and bad links
        #then click on all links
        # dont click on sub categories for organizaitons
        # need to click on name and organizaion links
        #except for one we dont want:
        #add to click list and repeat this until the end
        #if not category then add the content to the dictionary
        
        #store in correct format
        # to expand on persons life action list if
        #necessary do extra searches to expand info on life action in life action list 
        #
        intital_link_seed_list=self.upload_pickle(path_to_pickle)
        last_repo_uploaded=list(pypi_last_uploaded_repo_code_line_dic.keys())[0]
        last_uploaded_repo_code_line_list=pypi_last_uploaded_repo_code_line_dic[last_repo_uploaded]
        glossary_prompt=""
        current_pypi_repo_data=self.upload_sql_values(column_list_pypi_repo)
        pypi_repo_data_dic=self.process_sql_data_for_searches(current_pypi_repo_data)
        saved_pypi_repo_link_list=pypi_repo_data_dic["pypi_link"]
        current_pypi_code_line_data=self.upload_sql_values(column_list_pypi_code_line)
        pypi_code_line_dic=self.process_sql_data_for_searches(current_pypi_code_line_data)
        saved_pypi_code_line_list=pypi_code_line_dic["code_lines"]
        for link_to_repo in pypi_links:
            if link_to_repo in saved_pypi_repo_link_list:
                if link_to_repo==last_repo_uploaded:
                    dictionary_with_only_row_with_link_to_repo=self.get_values_associated_with_value_found_in_key(pypi_code_line_dic,link_to_repo,column_list_pypi_code_line, column_name="link_to_repo")
                    current_uploaded_code_lines_list_in_sql=dictionary_with_only_row_with_link_to_repo["code_lines"]
                    for code_line2 in last_uploaded_repo_code_line_list:
                        if code_line2 in current_uploaded_code_lines_list_in_sql:
                            continue
                        else:
                            pypi_web_search_data=self.retreive_data_from_web_pypi(code_line2,search_type="code_line")
                            dictionary_to_upload_to_pypi_code_line=self.process_pypi_code_line_search_data(pypi_web_search_data)
                            self.store_value_in_sql_table(dictionary_to_upload_to_pypi_code_line,"pypi_code_line") # glossary data will be stored in each table
                    continue                    
                else:
                    continue
                # will need to test this in building # this might make the program too slow will need to test it
            else:
                pypi_web_search_data=self.retreive_data_from_web_pypi(link_to_repo,search_type="repo")
                dictionary_to_upload_to_pypi_repo=self.process_pypi_package_search_data(pypi_web_search_data)
                self.store_value_in_sql_table(dictionary_to_upload_to_pypi_repo,"pypi_repo")
                repo_code_lines_list=dictionary_to_upload_to_pypi_repo["code_lines"].split("@@")
                self.create_pickle(self,r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\Pickles\last_uploaded_repo_code_lines.pickle",repo_code_lines_list)
                for code_line3 in repo_code_lines_list:
                    if code_line3 in saved_pypi_code_line_list:
                        continue
                    else:
                        pypi_web_search_data=self.retreive_data_from_web_pypi(code_line3,search_type="code_line")
                        dictionary_to_upload_to_pypi_code_line=self.process_pypi_code_line_search_data(pypi_web_search_data)
                        self.store_value_in_sql_table(dictionary_to_upload_to_pypi_code_line,"pypi_code_line") # glossary data will be stored in each table

        
        # store by persons name    
        nlp = spacy.load("en_core_web_sm")
        text_paragraph=""
        doc = nlp(text_paragraph)
        structured_data = {
            "Name": None,
            "Job Title": None,
            "Organization": None,
            "Education": []
            }
    
        for ent in doc.ents:
           #print(f"{ent.text},{ent.label_}")
            if ent.label_ == "PERSON":
                structured_data["Name"] = ent.text

       #print('this is the dicitionary to fill')
       #print('use spacy to get the person to and then search for the persons info?')
       #print('find sentences talking about the person')
       #print('use person name to find info on person but dont save persons name and do prompt search')

        
        # rather than choosing websites do all websites?
        # and make it so it focuses on parsing the text
        # and assocaiting ti with a person
        # thsi is what gpt did
        # categorize all websites
        #then grab info from all websitesd in category that should be relevent
        # so just google search
        # so perosnal info sites
        
                    
                    #deal with pypi repo code lines
                    # assume th
        
        #qualtities_add_to_all_actions_list={"time_to_complete_action":[],"other_losses":[],"other_gains":[],"monetary_cost_of_action":[],"monetary_gain_of_action":[],"risk_of_failing":[],"tools_needed":[],"other_things_effected":[],"transformations":[]}
        
    def process_sql_data(self,sql_data_list_list,column_list):
         """ bring data  from database """
         self.search_data_dic={}
         column_list_len=len(column_list)
         for column in column_list:
             self.search_data_dic[column]=[] 
         for sql_data_list in sql_data_list_list:
             for column, sql_data in zip(column_list,sql_data_list):
                 # this should solve hte problem of code not being super usable because
                 # we subbed out commas and such to store it
                 sql_data=str(sql_data)
                 sql_data=sql_data.replace("^","\'")
                 sql_data=sql_data.replace("&","\"")
                 sql_data=sql_data.replace("~",",")
                 sql_data=sql_data.replace("?","'")
                 self.search_data_dic[column].append(sql_data) 
         return self.search_data_dic
    
     
    def retrieve_data_from_local_database(self,table_name,where_string,column_list,testing=False):
        import psycopg2
        import re
        self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
        self.cur = self.conn.cursor()
       #print("Connection successful!")
        column_list=re.sub("'","",str(column_list)[1:-1])

        sql_str=f"SELECT {column_list} FROM {table_name}{where_string};"# for now limit to 10
        if testing ==True:
            sql_str=f"SELECT {column_list} FROM {table_name}{where_string} LIMIT 5;"# for now limit to 10

        try:
            self.cur.execute(sql_str)
        except Exception as E:
          print(E)
        sql_data_list_list= self.cur.fetchall()
        #self.conn.commit()
        self.cur.close()
        self.conn.close()
       #print("Connection closed.")
        return  sql_data_list_list  
    def OLD_generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_OLD(self,problemmm,positional_info_dic,objective="help the most people"):
        """use personal info to generate life dag and sort on objective using above function 
        try to figure out best actions you can take"""
        example=[{"problem_being_solved":problemmm,
                                   "strat_delimiter":'strat_delimiter',
                                   "step_delimiter":'step_delimiter',
                                   "task":"action",                         
                                   "effects":"effects",
                                   "typee":"objective"}]
        import psycopg2
        problemmm=""
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.problem_recorded=problemmm
        prompt_objectives_to_score_list=["helping the most people .....context",
                                  "making the most money .....context",
                                  "producing activism .....context"]# treat this as a document
        
        automated_galaxy_dic=self.automatically_add_web_search_result_to_problem_web_and_transformations_list(problemmm)
        strategy_action_space_with_effects_dic=self.auto_generate_and_problem_trees_from_problem_galaxy()
        sorted_problem_dags_dic_list=self.search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(strategy_action_space_with_effects_dic,user_positional_info_dic,objective,search_type="problem_dag")
        #sorted_problem_dags_list_list = [{"table":"updatetable10",'problem': question} for question in questions]  
        
        ### do this instead testt
        
        
        return sorted_problem_dags_dic_list
        
    
    
    
    
    
    
    
    
    def generate_dag_from_current_position_to_figure_out_best_actions_you_can_take_for_different_objectives(self,user_positional_info_dic,all_guide_life_action_list_with_effects_dic,objective=""):
        """use personal info to generate life dag and sort on objective
        try to figure out best actions you can take for each specific objective 
        like to make the most money help most people or both
        make problem tree and problem  web clickable 
        make problem web into chess board think edward snowden surveillnce how goverment set up there stuff
        suggest different simialr problems using database search
        display methods related to problem and possible methods
        when open problem solving program open life dag and problem web empty file
        have button to change to specific problem
        """
        example=[{"problem_being_solved":"life_position",
                                   "strat_delimiter":'strat_delimiter',
                                   "step_delimiter":'step_delimiter',
                                   "task":"action",                         
                                   "effects":"effects",
                                   "typee":"objective"}]   
        import psycopg2
        problemmm=""
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        
        print(f"this is for checjing if an action has already been processed for scoring so we have repeats")
        table_name ="saved_action_scores"
        column_list=["life_action","objective","weighted_avg_score","weights",            
            "guide_person_life_action_list_score", 
                  "user_personal_info_score", 
                  "action_with_respect_to_objective_score",
                  "user_compared_to_guide_score",
                  "numer_of_last_use_of_action_score",
                  "time_from_last_use_of_action_score",
                  "proxmity_of_action_to_other_past_used_action_score",
                  "other_people_postiion_score",
                  "other_people_available_action_score",
                  "resources_score",
                  "place_of_people_and_things_score" ,
                  "money_to_complete_action_score",
                  "time_to_cmplete_action_score"]
        self.all_guide_life_action_list_with_scores_dic=self.retrieve_data_from_local_database(table_name,"",column_list,testing=False)
        all_guide_life_action_list_with_scores_dic=self.process_sql_data_for_searches(self.all_guide_life_action_list_with_scores_dic,column_list)  
        
        
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        #galaxy_dic=self.upload_add_life_web_and_transformations_list()
        #strategy_action_space_with_effects_dic=self.auto_generate_and_problem_trees_from_problem_galaxy(galaxy_dic)      
        ###searching action space
        import numpy as np
        sorted_life_dags_dic_list=[]
        final_all_sorted_life_action_for_objective_dic_list=[
            ]       
        # use objective as a prompt and get more context for the objective
        prompt_objectives_to_score_list=["helping the most people Helping others is an important part of life, giving you a sense of purpose and boosting your happiness. In fact, acts of kindness can boost feelings of confidence, control, happiness, and optimism, says the Mental Health Foundation.Supporting others has a positive effect on the world around you. Kind acts may also encourage others to repeat the good deeds they’ve experienced themselves, contributing to a more positive community.If you want to help others more but aren’t sure where to start, look no further. Whether you’re looking for ways to help friends and family or give back to your community, keep reading for a list of ideas to get you started helping others.Where can I find ways to help others?First, focus on your passion when considering ways to help others. Your passion for helping others can be the foundation for your giving. Helping someone in need isn’t about how much you give but how much love you put into it.Inspiration for how to help others in need can happen anywhere. Small acts of kindness, like holding the door or offering a compliment, can have a significant impact. Helping people can include more substantial efforts, like making donations — whether of time or money — or giving items to help someone in need.Here are some ideas for finding ways to help others that will bring you joy and a sense of connection.Ask community leaders, friends, and family how you can help. Explain to them how you hope to help others and why you desire to help and see what they suggest. The opportunities for helping someone in need may surprise you!Look for opportunities to help and lend a hand without being asked to find out the best way to help. For example, hold the elevator door for a colleague or offer to take a photo for a group of tourists if they’re struggling with a selfie stick.1. Be proactive, not reactive.Many lives are lost to health emergencies that could have been managed through learning lifesaving skills Knowledge of cardiopulmonary resuscitation (CPR) and first aid help in emergencies at home, in public, or at work by providing immediate care, reducing injury severity, promoting safety, providing reassurance, and increasing workplace safety.Becoming trained in CPR and first aid is one of the best ways to support others and the community, helping others in need.American Red Cross Training Services offers a variety of CPR and first aid training programs, which you can take online, in person, or in combination to help everyone, whether your neighbors, colleagues, family, or friends. Find a CPR and first aid training program that fits your schedule.Find a ClassCPRFamily sharing a meal.Benefits of Taking a CPR, AED or First Aid CourseBe prepared: Protect your loved onesBe confident: Act with hands-on trainingPeace of mind: Know how to handle emergenciesHelp your community: Use lifesaving skills when neededTake a CPR Class2. Give your time.The gift of time is valuable and satisfying. It also makes giving accessible since we don’t all have the same amount of money, but we all have the same amount of time.Here are some ways to give your time and help people in need.Teach: Offer to teach friends and family members struggling with a skill you know well. Learn how to become a CPR Instructor! Teach people outside your social circle, too — try tutoring a student in math, for example, or showing your coworker how to use the office copier.Support: Be the first to offer condolences when someone you care about is suffering. Do what you can to comfort them, whether they need a hug, a shoulder to cry on, or a helping hand. Talk to them with empathy and compassion and ask if there is anything you can do to help.Listen: Not everybody seeks hands-on help or a solution to their problems; they might simply need to express their feelings while a supportive friend listens.Compliment: While giving compliments might not be what you traditionally picture when you think of helping people, it does help. Offer compliments to everyone around you, giving sincere praise while celebrating their successes and qualities you admire the most.Volunteer: Find a charity you’d like to support, like a shelter or soup kitchen, and spend time there doing whatever needs to be done. Not only will this help others, but it’ll also give you a newfound appreciation for all the good things in your life — and it’ll make you a more compassionate person.3. Donate to a worthy cause.Monetary donations are a great way to help others but aren’t the only way to donate to help those in need.Here are a few ideas for donating to worthy causes and supporting others.Donate furniture and clothing to a local shelter.Donate unopened spices, canned soups, or beans to a local food bank.Donate toys to local shelters and food banks.Donate blood if you can.Donate the opportunity for holiday and birthday gifts. Ask friends and family to make donations to charities instead of getting you gifts.Donate your car.4. Send a thoughtful note or care package.Sometimes, helping others is as simple as letting them know that you care. When people feel isolated or cut off from their friends or family, even a small gesture can help them feel more connected and brighten their day.Send handwritten cards and even care packages with special treats inside.Write a friendly email or letter and casually mention why you like the recipient.5. Express appreciation.Receiving thanks is another way to help each other and help our community. Plus, showing gratitude not only helps others feel appreciated but makes you happier too!Express appreciation when someone does something nice for you. Let your loved ones know how much you appreciate them, even when there’s nothing specific to thank them for.Practice gratitude by creating a list of things you’re grateful for and sharing it with others.Share a social media post about how much you appreciate someone’s support as you change careers or tell a friend how proud you are that they ran a whole marathon.Compliment underappreciated people, like the person bagging your groceries or bussing your table at a restaurant.Thank frontline health workers and first responders.Be neighborly. Check on neighbors, especially those who live alone, are elderly, have health or mobility issues, or care for children.Finally, helping other people should not equal a guilt trip. We have all felt the dread that comes from being coerced into helping others. When considering ways to help others, think about what you have excess — time, money, or unused items — and how that may help others in need.Now that you have the tools and inspiration to help others, it's time to put them into action. Together, we can make a positive impact on the world!",
                                         "making the most money The 6 figure income in your teens is the way outlier. The 9-5 is the path to comfort for the vast majority. The secret to fast easy money can be a couple things, incredible talent, large up front investment, a great idea, fraud, or dynamic charisma all coupled with the largest single factor, luck. You are comparing yourself to the top .001% or just liars. It's not worth it to hunt for a secret. It is worth it to better yourself, try and increase your worth and find someone willing to pay you what you're worth. It is worth it to be as happy and content as you can with what you have. It is certainly worth it to live on less than you make and sacrifice for the future. Side hustles are popular, and possible. What you need is a good idea and the motivation to make it happen.25 ways to make moneyWe turned 25 ways, complete with need-to-know details, to inspire you to earn. While most people want to make money fast, don’t discount the “slow” gigs, as they may pay more in the long run.How to make money onlineHow to make money from homeHow to make money offlineFor sections with input from Redditors: We sifted through Reddit forums to get a pulse check on how users feel about certain side hustles. We used an AI tool to help analyze the feedback and then summarized insight. People post anonymously, so we cannot confirm their individual experiences or circumstances.How to make money online1. Pick up freelance work onlineMake money online through websites such as Upwork, Fiverr and Freelancer.com. These sites offer opportunities to do a variety of freelance jobs, like writing, programming, design, marketing, data entry and being a virtual assistant.A report from Freelancer.com found that computer security jobs had the fastest growth in listings on its site in the second quarter of 2024, up 27.1%.Jobs involving writing skills are also in high demand. Although generative artificial intelligence (AI) is being used more for content creation, it can’t fully do the work of human writers.Companies are looking for writers who know how to edit AI content and who have at least a basic understanding of search engine optimization — learning or beefing up SEO skills could be a lucrative side hustle.No matter what freelancing you do, keep track of the going rate for the kind of work you provide so you know what to charge. Some freelancers are charging $100 an hour or more for their freelance writing services.Expert take: Soraya Ivette is a content marketing strategist who offers services on Fiverr. She started freelancing part time when she was home with her young children, and has done well.Once I set up my profile on Fiverr, I started getting job requests within a couple of weeks and I started taking on more jobs and making regular money consistently every month, she said in an email interview.Total time: It can take a while to get your first gig.Setup: 24-48 hours.How easy to start: Easy, if you have the expertise.Age threshold: Typically 16 to 18+.How fast you'll get paid: Varies by site.Need to knowIt takes Upwork up to 48 hours to approve your profile. Keep in mind it can also take time to land your first freelance gig.Payment varies by site. On Upwork the timeline for receiving earnings depends on the type of payment. Hourly contracts have a weekly billing cycle and you can withdraw funds 10 days later. Fixed-price contracts have a five-day waiting period after reaching a milestone. On Fiverr, you're paid when the work order is complete, but you can't withdraw funds for 14 days. (The waiting time is shorter for Top Rated Sellers.)RequirementsUpwork and Fiverr require users to be at least 18 to sell work. Fiverr allows users age 13 and older to use a parent or guardian’s account, with permission. And Freelancer.com requires users to be at least 16.2. Test websites and appsAnother way to make money from home is on sites like UserTesting.com. You get paid for your thoughts on how well — or not so well — certain websites and apps work. You’ll have to complete a short test to be accepted by UserTesting, then you’ll be paid depending on the test type.Total time: Approval can take a few days.Setup: Less than an hour.How easy to start: Easy, if you have the tech gear and complete a sample test.Age threshold: 18+.How fast you'll get paid: Usually after 14 days.Need to knowYou need to complete a sample test as part of the UserTesting application process.You will start receiving testing opportunities after your application is approved.The timeline for approval can vary.Payment amounts vary based on the length of the tests. You get paid 14 days after completing a website or app test via PayPal.RequirementsYou need to be at least 18.You need a device that meets UserTesting’s requirements, internet connection and microphone.The practice test and most user testing requires English, German or French; some test opportunities may be in additional languages.3. Learn to use AI toolsGenerative artificial intelligence is so hot right now. Research from PwC estimates that the North American economy will see a $3.7 trillion impact by 2030, thanks to the AI market.It's a good time to learn how to make money by using AI tools. Some AI-related side hustles include:Integrating AI tools as a freelancer, to help you create digital products or to edit AI content for a client.Improving your advertising, marketing efforts and management of your existing small business.Teaching others to use AI tools.Total time: Depends on demand.Setup: Around 24-48 hours if using a site like Upwork or Freelancer.com.How easy to start:  If you’re already familiar with AI tools, it will be easier to get started.Age threshold: 16+ for Freelancer.com and 18 for Upwork.How fast you'll get paid: Varies by client or the number of products you sell and your chosen platform.Need to knowGive yourself time to get familiar with using AI tools.You’ll need to meet the requirements of the freelance gig site you choose.Payment will depend on your client and the site’s terms and conditions.RequirementsYou’ll need a computer and an internet connection.4. Take surveys for moneyYou can make money from home by taking online surveys, but don’t expect to earn a lot. Survey sites don’t typically offer a big payoff, and many sites are more useful for earning gift cards than cash.Some of the more popular survey sites include Swagbucks and Survey Junkie. Read about how little we made with survey sites to find out which one might be best suited for you.Total time: It will take a while.Setup: Just minutes.How easy to start: Very. Just register and begin.Age threshold: 13 to 18+, depending on the site.How fast you'll get paid: Varies by site.Need to knowSurvey sites could be an option for how to make money online for beginners because you can register with a site and start taking surveys in a matter of minutes.The time it takes to get paid depends on the survey site and how much time you dedicate to taking surveys.Some sites let you cash out only after you hit a minimum earnings threshold.Other survey sites issue points, which can be redeemed for cash (via PayPal) or gift cards.RequirementsMost survey sites have a minimum age requirement, which ranges from 13 to 18 (depending on the site) making these sites one idea for teens to make money online.Individual surveys may have specific requirements. Don't be surprised if you are disqualified from a survey without much explanation.5. Make money from your blog with affiliate linksIf you’re a blogger who gets decent traffic, you could make money by joining an affiliate network. Affiliates get paid when someone clicks through from the website to the partner site and buys something there.Some bloggers make a lot of money this way, particularly those who do affiliate marketing full-time. You can use social media or a platform like Pinterest to drive traffic to your blog. Read more about affiliate marketing and other ways to make money blogging.Total time: It can take quite a while to build an audience.Setup: With blog templates, building a site is easy.How easy to start: While getting started can be easy, creating regular content may be another matter.Age threshold: Varies.How fast you'll get paid: A month or two, on average.Need to knowFirst, you need a blog, social media account or other online presence that draws a healthy number of visitors each month.Then, you need to apply for and be approved by an affiliate marketing network like CJ, ShareASale, FlexOffers, Rakuten Advertising or Amazon Associates.Payment schedules and thresholds vary by affiliate network, but expect to wait at least a month or two for your first paycheck.Amazon Associates pays out earnings 60 days after the end of the calendar month in which they were earned.ShareASale disburses earnings monthly.RequirementsA blog, social media account or other online presence that attracts a steady stream of visitors.6. Sell your wares on EtsyHave a penchant for woodworking, jewelry-making, embroidery or pottery? Sell your crafts on Etsy, the go-to site for artisans selling home goods, art and knickknacks. According to Etsy, the company has more than 95 million active buyers. Learn more about how to make money on Etsy.Total time: It might take quite a while for customers to find you.Setup: Can be quite involved.How easy to start: Leaning toward hard on the difficulty meter.Age threshold: 13+.How fast you'll get paid: Daily, weekly, biweekly or monthly, depending on your preference.Need to knowOpening an Etsy shop is the easy part. It can be done in a few hours.You need merchandise to sell, photos and descriptions to post, a name for your shop and a business plan to help you succeed. Once that’s done, you’ll still need to find customers.Once you sell an item, payment is deposited into your Etsy Payments account first, then to your bank account depending on your desired deposit schedule.RequirementsIf you’re over 13 years old but under 18, you can sell on Etsy but would be considered a minor and must follow extra policies.You need to have all necessary intellectual property rights to the merchandise sold in your shop.7. Self-publish an e-bookWriting a good book is tough, but the internet makes it easy to bring it to market. If you’re a writer who can churn out pages, you can use Amazon’s Kindle Direct Publishing to sell your books(s) on the Kindle store. It’s free to publish a book, and you can earn up to 70% of each sale in royalties. Write your book, enter a clear description and the details to be displayed and upload your manuscript. Set the price and see if it sells.Total time: How fast can you type? We don’t have to tell you writing a book can be a slog.Setup: Quick and easy on KDP once the book is ready.How easy to start: Just start writing.Age threshold: 18+, but parents and guardians can use their accounts to sell minors’ books.How fast you’ll get paid: Monthly. You'll need to meet a $100 threshold for wire or check payments.Need to knowJust because it’s simple to self-publish doesn’t mean your book will sell. Competition is high with millions of e-book titles on the Kindle Store.Choose one of two royalty options: 70% or 35%. You’ll have to price your book between $2.99 and $9.99 if you select the 70% option. You have more pricing flexibility when you pick 35%.RequirementsYou need to create a Kindle Direct Publishing account to get started.Proper formatting is important. Amazon says most Microsoft Word documents convert to e-books easily, but other formats are also supported.Take control of your finances with the NerdWallet appOur app tracks your spending, credit score, net worth and more — so you have a clear view of your day-to-day and long-term finances.8. Get advertising revenue from your blog or YouTube channelIf your YouTube videos or blog posts draw an audience, you may be able to make money from advertising. YouTube sets 1,000 subscribers as the benchmark for applying to the YouTube Partner Program if you want to place ads on your channel.You can apply with 500 subscribers for other monetizing features like channel memberships. You can also use Google’s AdSense, the same ad platform on YouTube, to put relevant ads on your blog or website for earning potential. Read more about how to make money on YouTube and Google AdSense.Total time: It can take several weeks to get up and running.Setup: Fairly easy.How easy to start: Depends on how good you are at producing interesting videos.Age threshold: 18+.How fast you'll get paid: Could take a long while to earn the first payout; then monthly.Need to knowSigning up for Google AdSense is pretty easy, but to use AdSense with YouTube, you’ll need to be part of the Partner Program.You can use AdSense on a website or blog with fewer eligibility requirements.Allow at least two months for ad revenue to start trickling in.You need to earn at least $100 before you're eligible for a payout.Once you hit the $100 threshold, earnings are issued between the 21st and 26th of the following month.RequirementsYour own website that has been active for at least six months.For YouTube, you need at least 1,000 subscribers and to meet requirements related to views or watch hours.You must be at least 18.9. Become an Instagram influencerCompanies are using Instagram influencers — people with large, dedicated followings on the platform — to rep their products. You can get in on the action by applying for opportunities via a marketing platform like Open Influence or Aspire, or by contacting the brands you want to work with. You can also make money on TikTok this way.Total time: You'll need to stick with it.Setup: Quick and easy.How easy to start: Not that easy. Read: Must build following to gain influence.Age threshold: 13+.How fast you'll get paid: Varies on partnerships.Need to knowCreating an Instagram account is quick, but building a following can take months or even years.Once you have the numbers, you'll need to find paid opportunities. You can do this via affiliate networks or by pitching brands you want to work with.The time to receive your payment will depend on the terms of your agreement, but affiliate networks typically pay out earnings the month after a campaign is completed.RequirementsAn Instagram account with a dedicated, engaged following.You'll also need to meet the requirements of any affiliate network.10. Monetize your Twitch channelGaming could be a way to make money from home if you have a steady following on Twitch, the go-to site for gamers. Streamers can receive money from viewers’ virtual cheers, or “Bits,” and even get a share of subscription and ad revenue if they reach Affiliate or Partner status. Learn more about how to make money on Twitch.Total time: This can be a long game.Setup: Quick and easy.How easy to start: Easy to start; takes a while to build a following.Age threshold: 13+.How fast you'll get paid: Monthly.Need to knowYou can launch a Twitch channel and start streaming in a day, but it will take weeks or even months to build a following.Subscription and ad revenue earned as a Twitch Partner or Affiliate is paid out around the 15th of every month, and you must have a balance of at least $50 for most payout methods (it's $100 for wire transfers).RequirementsYou need to hit certain viewership and broadcast milestones to become a Twitch Affiliate or Partner and qualify for a share of game sales, ads and subscription revenue.» MORE: How to make money as a kid11. Sell your photographyTurn your photographs into cash via sites like Fine Art America, which lets you upload your images to sell as prints, T-shirts, phone cases and more. Other marketplaces for photographers include SmugMug, 500px and PhotoShelter. Some sites require a subscription but may provide features ranging from cloud storage to password-protected galleries and a customized website.What the Redditors say: Success selling photos requires both high-quality content and a bit of business savvy around rights management and pricing. A general theme is that you may do better by forming direct relationships with buyers than purely relying on stock sites.Total time: Buyers need to find you — and like your work.Setup: Just a few hours.How easy to start: If you have a library of photos, you're on the way.Age threshold: Varies.How fast you'll get paid: Depends on your sales platform.Need to knowYou can set up a profile with sites like SmugMug, PhotoShelter or Fine Art America in a few hours, assuming you have a body of original work.Payment varies widely depending on the site.Fine Art America: Payment issued after 30-day return window expires. Sent on the 15th of each month.PhotoShelter: Payment issued at time of sale to your chosen payment method (PayPal, Stripe, etc.).SmugMug: You can request payment be issued the following month if you have a balance of at least $5.RequirementsRequirements vary by site, but you need to have all necessary rights to the images you sell.How to make money from homeSome side hustles don't even require you to leave the house. Or if they do, it might just be a short walk around the block with a furry friend. Working from home requires a little creativity and a stick-to-it spirit. Here are some excellent ideas for side gigs from home:12. Become a dog walker with Rover or WagLove dogs? Choose dog walking as a beginner's way to make money. Apps like Wag and Rover offer on-demand dog walking, so you can pick up walks when your schedule allows. If you have space (and your landlord’s permission, if you rent), you could offer overnight dog boarding. Read the fine print if you sign up for these services.What Redditors say: There's potential to earn an extra $300+ per month with a gig service like Rover when you have regular clientele, but success can depend heavily on location and market. Are dogs trending in your town?Total time: Building a client base may take some time.Setup: Can take a few weeks to be approved.How easy to start: Love pets? You're good to go.Age threshold: 18+.How fast you'll get paid: Two days to a week.Need to knowIt takes about 5 to 10 business days for your Rover profile to be reviewed and approved.The application process for Wag takes about two weeks and you must pass a background check and pet care quiz.RequirementsFor Rover or Wag, you’ll need to live in an area where the service operates.If you want to pet-sit in your own home, you’ll need an apartment or house that allows pets.You’ll have to pass a background check.13. Sell unused gift cardsMake extra money by selling unused or partially used gift cards on a site like CardCash or GiftCash. CardCash notes it will pay you up to 92% of the card’s value, or you can trade in your card for one you’ll use. Read more about what to do with unwanted gift cards.Total time: In minutes if your gift card is for a popular store.Setup: Easy.How easy to start: The more gift cards you have to sell, the better.Age threshold: 18+.How fast you'll get paid: A few days to about two weeks.Need to knowYou can get an instant offer or quote via sites like CardCash and GiftCash.You can sell gift cards at kiosks and participating retail locations to get cash the same day, or try to sell them online. The latter takes longer, but you may get a better offer for your gift card.RequirementsYour gift card may need to meet a minimum balance to be resold. Not all cards will generate offers.Gift cards with expiration dates may not be eligible.14. List your spare bedroom on AirbnbRenting out your home or spare bedroom on vacation rental sites is another way to make extra money. Be prepared to spend some money to clean and keep up the property, replace home goods and pay toward service fees. And scrutinize your rental agreement, HOA rules and zoning or other restrictions before you get started. Learn more about how to start an Airbnb business.Total time: Demand drives success, and that depends on your location.Setup: A listing can be created and live in hours.How easy to start: If you have a place to rent, it's a simple process.Age threshold: 18+.How fast you'll get paid: A day or more after check-in.Need to knowYou can create a listing and start accepting reservations on the same day.Payment is typically disbursed about 24 hours after your guest’s scheduled check-in time, but processing time for that payment depends on the payout method.RequirementsComply with any rules governing short-term or vacation rentals in your property, including city ordinances and rules issued by your landlord, condo board or homeowners association.How to make money offlineThere's online and at-home ways to make extra money — and then there's a third alternative: offline. This version of the gig economy may require more work, but the upside can be substantial. Since there’s no escaping the internet these days, some of these offline methods do have online components:15. Sell your gently used clothesA woman makes extra money by selling her clothes.Selling clothes you no longer wear is a quick way to make some money. Start with local consignment shops to make money quicker or use sites like ThredUp and Poshmark to find buyers. When listing items online, be sure to take clear, well-lit photos of your pieces and research similar items to set competitive prices. Get tips on how to sell your clothing.Total time: Varies by sales channel.Setup: Easy and fast. You can simply go to a consignment shop or fill a box with clothes and send it in.How easy to start: Easy. Cleaning out the closet may be the hardest part.Age threshold: 13+.How fast you'll get paid: Varies by sales channel.Need to knowYou can sell used clothing and accessories several ways, but they're all pretty quick to start.Fast: A brick-and-mortar consignment store like Plato's Closet will give you cash on the spot.Medium: Other in-person and online consignment shops pay you when your items sell, or when they receive and inspect your items. Either way, allow at least a month for your payout.RequirementsGently worn shoes, clothing and accessories.Items will go through various inspections before being accepted. For example, ThredUp checks items for pilling, fading, shrinkage, missing parts (like buttons) and stains.16. Trade in old phones, electronics for cashHave an old phone, iPad, laptop or gaming system lying around? Sell it on a site like Swappa, Gazelle or Facebook Marketplace. Check out Amazon’s trade-in program, which pays participants in Amazon gift cards — and eBay, too. If you’re in a rush, try an ecoATM kiosk, which offers cash on the spot for your device.Total time: Lots of options, so your time spent will vary.Setup: A breeze.How easy to start: Easy, especially if your device is in good shape.Age threshold: Typically 18; check terms of service.How fast you'll get paid: Varies by where you sell.Need to knowSelling directly (Swappa, OfferUp, Facebook Marketplace): In most cases, you take photos of the phone, verify the electronic serial number is clean and post your listing. Some sites review and approve postings, but the time is minimal. Fees vary. Swappa, for example, charges a 3% seller fee.Selling to reseller (Gazelle): Answer a few questions online for an instant quote. Then send in your device and get paid once the company confirms its condition is as described.Selling directly: When you get paid depends on how quickly your phone or device sells. Once the item sells, payment is fast.RequirementsA used phone, laptop, gaming system, etc.Cell phones: You need to verify the phone is not stolen or under a repayment plan. Check terms of service for additional requirements, such as no activation lock.17. Get a babysitting gigEveryone from college students to recent retirees can make money by watching other people’s children. Word-of-mouth referrals from friends and family are still a great way to get started, but you can also create a profile for free on Care.com or Sittercity to expand your reach. Note any specialized skills, such as CPR certifications, to make yourself more marketable.Total time: Online setup takes minutes; neighborhood referrals may take a while.Setup: Just minutes.How easy to start: Getting the word out is the main thing.Age threshold: Very young if you're using referrals. 18+ online.How fast you'll get paid: When the parents come home.Need to knowYou can create a profile on Care.com or Sittercity in a matter of minutes.You typically get paid when you complete your gig, whether by a service or direct from the customer.RequirementsYou need to be at least 18 to list as a caregiver on Care.com and Sittercity.Clients may request a background check.18. Rent out your carCity-dwellers often don’t use their cars for days or weeks at a time. That idle time can translate to extra money with services like Getaround and Turo, which let you rent out your car by the hour or day. You take home the majority of those earnings, while Getaround or Turo takes a cut for protecting your car while it’s being rented.Total time: Demand for your car will depend on the local market.Setup: It takes about a half hour to set up an account.How easy to start: With an appropriate vehicle, it's easy.Age threshold: 21+ with a valid driver's license for Turo; Getaround does not list an age requirement.How fast you'll get paid: Varies by site.Need to knowYou can create a listing on Turo or Getaround in under 30 minutes.Turo initiates payment within three hours of the end of the rental, but you can expect it to take a few days for your bank to process the deposit. (This is the case for all trips after the first one, which takes a few days for Turo to send.)Getaround rental earnings accrue daily or monthly. Payments are made via direct deposit.RequirementsIf you lease your car, check the terms of your agreement and financing documents to make sure you’re allowed to share it.Your car must meet certain requirements (make/model/year/mileage) and satisfy maintenance and safety standards. You may also be asked to agree not to list on other platforms.19. Sign up for TaskRabbitIf you actually enjoy putting together Ikea furniture or standing in long lines, you may be cut out for doing tasks for others. Websites like TaskRabbit can connect you with people who need help with a variety of things, such as moving, cleaning, delivery and handyman services. The site also offers several virtual and online tasks, such as helping with a research project or data entry. Read about how to make money with TaskRabbit.What Redditors say: This is a flexible side hustle that can be good for a couple hundred bucks of supplemental income per month. But, like with other gig service sites, your success is dependent on location and demand.Total time: Local demand for your skills will determine the time you spend.Setup: A couple of hours, then some time for approval.How easy to start: Easy, though you'll need to do some research.Age threshold: 18+.How fast you'll get paid: A few days after a job.Need to knowYou can set up your profile and register in a matter of hours, but can't start accepting tasks until your profile is approved by TaskRabbit. This may take a few days.Once approved, you need to pay a $25 fee, so you may first want to research your market and the value of your skills to determine if that fee is worth it to you.You're paid after the task is completed through direct deposit to a checking account. Payment typically takes a few days to appear in your account.RequirementsYou need to be at least 18 to start working with TaskRabbit.Prospective Taskers must also pass a background check.20. Become a private tutorParlay your math, science, foreign-language or test-prep expertise into a lucrative side gig by becoming a private tutor. You can tutor people online or in-person.What you charge can depend on your experience, expertise and what’s in demand. To get started, see what types of tutors are needed on Craigslist, or create a profile on sites like Tutor.com or Care.com. You can also advertise your services at local schools and community centers.Total time: Varies by subject matter. Some companies might require a minimum availability per week (e.g., Tutor.com requires 5 hours).Setup: Can be a bit involved.How easy to start: Students will have to find you, and that might take a while.Age threshold: Any.How fast you'll get paid: Depends on the platform; check the terms of service.Need to knowStartup time depends on demand in your area. It could take a while before you get your first student.If you haven't tutored before, you'll want to allow for time to prep so students feel like they're getting the most out of their time with you.How quickly you get paid depends on whether you tutor via a platform or in-person; either way, it likely won't take long.RequirementsYou'll need deep knowledge in an area that people need help understanding, like mathematics, a foreign language or test prep.Educational requirements might apply. Some tutors might be required to be currently enrolled in a four-year university or have at least a bachelor's degree from an accredited four-year university.21. Drive for Uber, LyftJoin Uber or Lyft (or both) and make money by driving passengers around. Just don’t forget to factor in gas and maintenance costs. You need an eligible car in good condition and must agree to a background check and a review of your driving history. Learn how to become an Uber driver or how to make money as a Lyft driver.Total time: Depends on your market demand.Setup: A few weeks.How easy to start: Not difficult, but you'll need the right type of vehicle.Age threshold: Varies by region from 21-25.How fast you'll get paid: Very fast. Either instantly or within days.Need to knowAllow some time for the application process, background check and car inspection.Lyft and Uber can pay you instantly through a debit card or transfer earnings to your bank account pretty quickly.RequirementsA car with four doors. It must also meet other requirements, such as year, physical condition, etc.Depending on your state, you may need to have at least one year of licensed driving experience to drive for Lyft. Uber requires at least one year of licensed driving experience in the U.S. (or three years if you’re under 25).Let your car insurance company know of your plans before you start driving.Nerdy PerspectiveDriving for Uber was not my favorite side hustle, but it was accessible and the little money I made over a week-long test came quickly. I'd be worried about gas costs, wear and tear on my car, and lots of awkward silence if I were to do it long term, though. I was happier when I delivered food and groceries. I delivered with DoorDash and became a full-service Instacart shopper for short stints in 2024, and found these driving gigs to be less stressful than doing rideshare. Trips were shorter, I spent less time in the car and it was easy to get started, even in my small town.Profile photo of Tommy TindallTommy TindallI've tried driving gigs22. Make deliveries for Amazon, Uber EatsTake advantage of the growing delivery trend and sign up for a service like Instacart, Uber Eats, Postmates, DoorDash or Amazon Flex. You get paid per delivery, in most cases, and can even earn tips. A car isn’t always required — Postmates and DoorDash let you use a bike or scooter to make deliveries in some cities. However, a background check is almost always part of the deal. Learn more about how to get started with Amazon Flex, Uber Eats and Instacart.Total time: Depends on your market demand.Setup: About a week.How easy to start: Easy, if you have dependable transportation.Age threshold: Varies by the service, but at least 18.How fast you'll get paid: Varies by vendor.Need to knowThe background check can take a few days, and timing can vary.Payments from these services also vary, but are generally issued weekly or quicker.RequirementsYou'll need a way to deliver items. It could be a car, scooter or bike, depending on the service.A smartphone is necessary to accept and process jobs.Each delivery service has a minimum age requirement, but it varies by service.23. Find work as a housesitterIf you’re willing to watch someone’s home — and maybe feed the pets, water the plants and take out the garbage — become a housesitter. Tap your personal network for referrals or try out HouseSitter.com, which connects homeowners with housesitters.Total time: Depends on your market demand.Setup: Minutes — or more if you try to drum up business by referrals.How easy to start: That can depend on the need in your area.Age threshold: Varies by site.How fast you'll get paid: Typically at the end of a gig; make arrangements with clients.Need to knowYou can create a profile on HouseSitter.com in a matter of minutes, though it may take time to secure your first housesitting gig.You typically get paid by the homeowner when you complete your gig.RequirementsMost sites have an age requirement.24. Sign up to be a mystery shopperBusinesses often want to know how they’re performing from a customer’s perspective. Sign up to be their eyes and ears. You can apply online via sites like IntelliShop, BestMark and Sinclair Customer Metrics. Just beware of scams and do thorough research before signing on.Total time: Varies by site.Setup: Applying takes little time, but approval can take a while.How easy to start: Relatively easy if you have required transportation and tech.Age threshold: May vary by site.How fast you'll get paid: Varies by company.Need to knowThe application process is typically quick, but then it's in the company's hands. It can take days, or more, to assess your application, depending on demand.Payout timing and method vary by company. BestMark, for example, issues payments monthly.RequirementsMost mystery shopping services have an age requirement. You have to be at least 18 to shop for BestMark.Depending on the service, you may need internet access.25. Put your drone to workSome of the best camera drones can cost less than $500 — and you can use that investment to make money. Real estate agents turn to drone pilots to generate aerial photos of a home's exterior, and even neat fly-through videos of interiors, which can translate to a relatively easy money-making venture.If you're willing to learn more advanced skills, like drone mapping, you can often charge more for clients seeking aerial inspections and land mapping.You need to pass a test to become a drone pilot and register your drone with the Federal Aviation Administration. Then, you can apply for flying gigs.Total time: Depends on demand.Setup: You'll need to make time to pass a test, and then find clients.How easy to start: If you already have a drone, you're likely qualified.Age threshold: 16+.How fast you'll get paid: Varies by company.",
                                  "producing activism Activism consists of efforts to promote, impede, direct or intervene in social, political, economic or environmental reform with the desire to make changes in society toward a perceived common good. Forms of activism range from mandate building in a community (including writing letters to newspapers), petitioning elected officials, running or contributing to a political campaign, preferential patronage (or boycott) of businesses, and demonstrative forms of activism like rallies, street marches, strikes, sit-ins, or hunger strikes.Activism may be performed on a day-to-day basis in a wide variety of ways, including through the creation of art (artivism), computer hacking (hacktivism), or simply in how one chooses to spend their money (economic activism). For example, the refusal to buy clothes or other merchandise from a company as a protest against the exploitation of workers by that company could be considered an expression of activism. However, the term commonly refers to a form of collective action, in which numerous individuals coordinate an act of protest together.[1] Collective action that is purposeful, organized, and sustained over a period of time becomes known as a social movement.[2]Historically, activists have used literature, including pamphlets, tracts, and books to disseminate or propagate their messages and attempt to persuade their readers of the justice of their cause. Research has now begun to explore how contemporary activist groups use social media to facilitate civic engagement and collective action combining politics with technology.[3][4] Left-wing and right-wing online activists often use different tactics. Hashtag activism and offline protest are more common on the left. Working strategically with partisan media, migrating to alternative platforms, and manipulation of mainstream media are more common on the right (in the United States).[5] In addition, the perception of increased left-wing activism in science and academia may decrease conservative trust in science and motivate some forms of conservative activism, including on college campuses.[6] Some scholars have also shown how the influence of very wealthy Americans is a form of activism.[7][8]Separating activism and terrorism can be difficult and has been described as a 'fine line",
                                  ]# treat this as a document
        if objective != "":
            print('for problem searches instead of life dag search just add problem as an additonal objective to search for and weight stuff more heavily')
            prompt_objectives_to_score_list=[objective]    
        
        # create person_organizaion_action_context_list
        # will prolly change this at one pointt o name rather than link
        print('this is retrieivng the info for consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action ')
        user_position_context= str(user_positional_info_dic['places_lived'])
        user_position_context= user_position_context+ " "+str(user_positional_info_dic['work_experience'])
        
        person_organizaion_action_list_dic={}       
        for i2, actionn in enumerate(all_guide_life_action_list_with_effects_dic["action"]):           
            linkkk=all_guide_life_action_list_with_effects_dic["link"][i2]
            if linkkk in person_organizaion_action_list_dic:
                person_organizaion_action_list_dic[linkkk].append(actionn)
            else:
                person_organizaion_action_list_dic[linkkk]=[actionn]
                
                
        person_organizaion_position_list_dic={}        
        for i3, position_words in enumerate(all_guide_life_action_list_with_effects_dic["position_of_other_people_places_and_things"]):
            linkkkk=all_guide_life_action_list_with_effects_dic["link"][i3]
            if linkkkk in person_organizaion_position_list_dic:
                person_organizaion_position_list_dic[linkkkk].append(position_words)
            else:
                person_organizaion_position_list_dic[linkkkk]=[position_words]
     
        
     
        
        import re
        #for obejctive_doc in prompt_objectives_to_score_list:
        sorted_life_action_dic_for_objective={}
        for iterr, life_action in enumerate(all_guide_life_action_list_with_effects_dic['action']):                 
                #print(' check if used life action THIS IS WHAT I AM WORKING ON NOW')
                print(f"life_action {life_action}")
                print('need to remove cleaning below at somepoint fix upstream to remove commas')
                #column_value=str(life_action)
                #column_value=column_value.replace("\'","")
                #column_value=column_value.replace("\"","")
                #column_value=column_value.replace(","," ")
                #column_value=column_value.replace("'","")
                #life_action=re.sub("\"","",column_value)
                
                if life_action in all_guide_life_action_list_with_scores_dic["life_action"] :
                    print('life action')
                    #input()
                    #print(all_guide_life_action_list_with_scores_dic["life_action"])
                    #input('meow')
                    continue
                for obejctive_doc in prompt_objectives_to_score_list:
                    ### processing amd getting values
                    life_sub_action_lists=all_guide_life_action_list_with_effects_dic["sub_steps_to_complete_actions"][iterr]
                    linkkkkk=all_guide_life_action_list_with_effects_dic["link"][iterr]
                    work_experience=all_guide_life_action_list_with_effects_dic["work_experience"][iterr]# use this to rank life_action_list in respect of objective give it a score
                    projects_interested_in=all_guide_life_action_list_with_effects_dic["projects_interested_in"][iterr]# use this to rank life_action_list in respect of objective give it a score
                    guide_person_personal_info_context=work_experience + " "+projects_interested_in

                    effects=all_guide_life_action_list_with_effects_dic["other_things_effected"][iterr]# use this to rank life_action_list in respect of objective give it a score
                    life_action_context=life_action+ " "+life_sub_action_lists+" "+effects
                    user_positional_info_context=str(user_positional_info_dic["property"])# use this to rank life_action_list in respect of objective give it a score
                    user_positional_info_context=user_positional_info_context+str(user_positional_info_dic["skills"])
                    user_positional_info_context=user_positional_info_context+str(user_positional_info_dic["connections"])
                    
                    print("incorporate problem search_type into life action dag search save on work")
                   #print('we are limited by qualaites of input data so only get use these in choosing functions to sort actions so probably best way to incporrate game theory is considering other people involved in action/ environment of action')
                    guide_person_life_action_list_score=self.create_document_similarity_score(guide_person_personal_info_context,obejctive_doc,typee="get_guides_life_action_list_score_for_objective")
                    #user_personal_info_score=self.create_document_similarity_score(user_positional_info_context,obejctive_doc,typee="get_user_perosnal_info_score_for_objective")
                    #print(guide_person_personal_info_context)
                    #print(user_positional_info_context)
                    #user_compared_to_guide_score=self.create_document_similarity_score(user_positional_info_context,guide_person_personal_info_context,typee="get_user_perosnal_info_score_for_guide_personal_info")
                    action_with_respect_to_objective_score=self.create_document_similarity_score(life_action_context,obejctive_doc,typee="get_action_list_score_for_objective")
                    print('STILL NEED TO WRITE THIS ONE use random qualtities we have')
                    other_qualities_score=self.create_document_similarity_score(life_action_context,obejctive_doc,typee="use_all_qualtities_of_input_data_strategies_and_personal_info_in_different_ways_to_help_rank_action")
                    # dont wan tto remove option want to just reduce using some factor 
                    # would rathe have exact distances for resource you have are proxmitate to other resources
                    # where do i get numeric distance data
                    
                    print('numeric')
                    time_to_complete_action=all_guide_life_action_list_with_effects_dic["time_to_complete_action"][iterr]
                    monetary_cost_of_action=all_guide_life_action_list_with_effects_dic["monetary_cost_of_action"][iterr]      
                    money_to_complete_action_score,time_to_cmplete_action_score=self.consider_factors_such_as_time_to_complete_action_monetary_roi_cost_of_action_and_action_effects(time_to_complete_action,monetary_cost_of_action)# like know enemy can do x actions so to avoid getting back stabbed do y
                    # done is the one one above
                    
                    user_location_data_list=user_positional_info_dic["places_lived"]
                    print('may need to split this list at one point for now we good though')
                    #user_location_data_list=user_location_data_list[1:-1].split(",")

                    action_location_data_dic_list=all_guide_life_action_list_with_effects_dic["action_geo_locations"][iterr]
                    action_location_data_dic_list=action_location_data_dic_list[1:-1].split(",")
                    place_of_people_and_things_score=self.consider_numeric_distances_and_placement_of_other_people_places_and_things_when_choosing_action_use_map(action_location_data_dic_list,user_location_data_list)
                    # done the above
                    print('use lemma and make it so good for exaxct word matches works need to write these algorhim and gahter the data ')               
                    # look at all the actions past data stuff
                    user_past_actions_list=all_guide_life_action_list_with_effects_dic["user_past_actions_list"][iterr]
                    user_past_actions_list=user_past_actions_list[1:-1].split(",")

                    user_time_past_use_of_action_list=all_guide_life_action_list_with_effects_dic["user_time_past_use_of_action_list"][iterr]
                    user_time_past_use_of_action_list=user_time_past_use_of_action_list[1:-1].split(",")
                    numer_of_last_use_of_action_score,time_from_last_use_of_action_score,proxmity_of_action_to_other_past_used_action_score=self.use_patterns_in_strategies_help_rank_action(user_past_actions_list,user_time_past_use_of_action_list,life_action)# like previous strategies data used etc 
                    
                    
                    #done still need to write it but idea is there
                    resources_required_for_action_context=str(all_guide_life_action_list_with_effects_dic["resources_required_to_perform_action"][iterr])
                    personal_resources_context=str(all_guide_life_action_list_with_effects_dic["assets"][iterr])
                    resources_score=self.consider_distance_of_resources_you_have_avilable_to_you_vs_resources_required_to_take_action(resources_required_for_action_context,personal_resources_context)
                    # other peoples available actions are all their life action lists
                    # create life action context for each indivudal person/org/link
                    # link is key        
                    print(' the inputs are generaqted up top for this function consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action')
                    current_life_action_list=person_organizaion_action_list_dic[linkkkkk]
                    other_people_postiion_score,other_people_available_action_score=self.consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action(str(current_life_action_list), user_position_context,person_organizaion_position_list_dic,person_organizaion_action_list_dic)                    
                    weights = [14.424, 14.421, 14.417,11.324,11.324,11.324,11.324,-2.324,100.324,100.324,100.324]
                    # make the distance of things score negative
                    # money and time most valuable factors
                    amount = [guide_person_life_action_list_score, 
                              action_with_respect_to_objective_score,
                              numer_of_last_use_of_action_score,
                              time_from_last_use_of_action_score,
                              proxmity_of_action_to_other_past_used_action_score,
                              other_people_postiion_score,
                              other_people_available_action_score,
                              resources_score,
                              place_of_people_and_things_score,
                              money_to_complete_action_score,
                              time_to_cmplete_action_score]
                    weighted_avg_score = np.average(amount, weights=weights,axis=0)
                    # need to create sub lists
                    print('need to create proper life_sub_action_lists to get this to work')
                    sorted_life_action_dic_for_objective[weighted_avg_score]=[life_action,life_sub_action_lists,effects,obejctive_doc]  
                    print(f"sorted_life_action_dic_for_objective value {sorted_life_action_dic_for_objective[weighted_avg_score]}")
                    # will need to write the below functions later
                    print(f"  weighted_avg_score   {weighted_avg_score}")

                    print('''super imporant to consider other plahyers moves! think sc2 and civ pro
                          by anticipating other peoples moves then limit their future moves with your moves you can better precift their future move
                          then can counter this move and beat them''')
                    print(f'life_action {life_action}')
                    # need to save weights here and orgingal numbers to save on time
                    table_name="saved_action_scores"
                    dictionary_of_values={"life_action":life_action,"objective":obejctive_doc,"weighted_avg_score":weighted_avg_score,"weights":weights,            
                        "guide_person_life_action_list_score":guide_person_life_action_list_score, 
                              #"user_personal_info_score": user_personal_info_score, 
                              "action_with_respect_to_objective_score":action_with_respect_to_objective_score,
                              #"user_compared_to_guide_score": user_compared_to_guide_score,
                              #"numer_of_last_use_of_action_score":user_compared_to_guide_score,
                              "time_from_last_use_of_action_score": time_from_last_use_of_action_score,
                              "proxmity_of_action_to_other_past_used_action_score":proxmity_of_action_to_other_past_used_action_score,
                              "other_people_postiion_score": other_people_postiion_score,
                              "other_people_available_action_score": other_people_available_action_score,
                              "resources_score":resources_score,
                              "place_of_people_and_things_score": place_of_people_and_things_score,
                              "money_to_complete_action_score":money_to_complete_action_score,
                              "time_to_cmplete_action_score":time_to_cmplete_action_score }# this the column as key               
                    self.store_value_in_sql_table(dictionary_of_values,table_name)
                
                
                      
                      
                
                
                    
                          
            
               
                    #final_all_sorted_life_action_for_objective_dic_list.append(temp_dic)         
        #sorted_life_dags_dic_list=final_all_sorted_life_action_for_objective_dic_list
        #return sorted_life_dags_dic_list
        
        #sorted_life_dags_dic_list=self.search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(self.all_guide_life_action_list_with_effects_dic,user_positional_info_dic,objective)
       #print("generate_life_dag_with_objective_most_financil_gains_best_investment_finder_money_personal_time_financial_forecasting")
       #print("sorted_climate_life_dags_dic_list")
       
        #return sorted_life_dags_dic_list

        
    def generate_life_dag_with_objective_most_financil_gains_best_investment_finder_money_personal_time_financial_forecasting(self,positional_info_dic,objective="make the most money"):
        """ thsi is essentially the life dag function with the ogjective of maxmizing finaicail gains
        WORK ON THIS SUOPER IMPROTANT
        look at all alternative investments (actions)
        rank these based on psoitons
        look at the monetary effect sof actions
        over different time periods like each year
        and other effects of action at different time periods
        ###
        if you have a model that factors in the changing field of tech and variables like ai then you
        can make decisons that take these into account and make the best decidion 
        considering these in the rankings of best decisions and investment of time
        """
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        automated_galaxy_dic=self.automatically_add_web_search_result_to_problem_web_and_transformations_list(positional_info_dic)
        strategy_action_space_with_effects_dic=self.auto_generate_and_problem_trees_from_problem_galaxy(automated_galaxy_dic)
        sorted_financial_life_dags_list=self.sort_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(strategy_action_space_with_effects_dic,positional_info_dic,objective)
        return sorted_financial_life_dags_list

    
    def automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product(self):
        """ one step further peeling back the onion of methods
        a function to generate other funcitons like the ones from the list below  that automcailly build and improve a product
        automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        combine_all_concepts_tools_and_info_from_other_field_into_current_field()"""
    def best_action_to_take_or_investment_to_make__for_money_time_spent_considering_current_position_skills_financial_forecasting(self):
        """how do i best spend time with skills i have and considering position
        i am in or skills i could learn to make the most money(objective)  """
        
    def financial_casting_model_to_predict_future_financial_outcomes(self):
        """ so can better invest
        Financial forecasting models are essential tools for businesses to predict future performance, 
        make informed decisions, and remain competitive.
        By using these models, companies can better allocate resources,
        anticipate risks, and align their strategies with market trend
        You sent
        The term “projection” is used in finance to predict future financial results beyond the next four quarters."""
    def automatic_method_generator_using_patnets_with_patenteded_methods(self):
        """ """
    def calculate_materials(self):
        """ """
    def use_code_to_perform_all_tasks_in_physical_world(self):
        """ """
    def show_geographically_on_map_where_actions_are(self):
        """ """
    def social_climbing_contact_ceo_podcast(self):
        """propose differretn techniques to meet the right people and get in with the in crowd globally """
    def autoamtically_generate_research_papers_and_all_content_on_big_companies_websites(self):
        """ and copy there practices"""
    def integrate_all_big_comapnies_best_ideas_into_my_business(self):
        """ steal ideas fromg google open ai mda and find other goldman sachs"""
    def find_other_useful_resources_like_free_stores_and_other_useful_info_within_unis_and_other_organizaitons(self):
        """ like find all possible granting organizations and apply to all granting organizations"""
    def create_more_and_other_businesses_find_business_mdoels_and_small_towns_and_open_them(self):
        """
MAKE ALL BUSINESS HAVE PHONE APP AND WEBSITE
get into cyber security        
        more businesses the better to reuse skills and capital and can charge business for time and capital if reasonable
legal news company all social media website and app
tech news company all social media website and app
fast food business all social media website and app, phydical location
personal website and all social media website and app, and make it not for profit

copy all other successful business models in small towns and make as many business as can and charge them for website etc to pay myself

figure out all assets owned by business and figure out how to obtain this information from prospectus and add them to other businesses to generate value """
    def find_all_assets_of_business_probably_from_propsoectus_find_way_to_produce_assets(self):
        """ make my own business as valuable as these businesses"""
    def get_all_private_investors_and_all_grants_and_all_sources_of_revenue_to_invest_in_business(self):
        """ """
    def generate_slide_deck_for_investors(self):
        """ """
    def generate_product_market_fit_calcualtor(self):
        """ """
    def use_all_previous_legal_code(self):
        """in this case use to crearte value show projects to the world """
    def ai_hedge_fund(self):
        """ https://github.com/virattt/ai-hedge-fund"""
    def use_5_point_cnc_milling_to_build_indsutrial_parts(self):
        """ send cad files tot his machine with robotic arms to build space parts and other parts """
    def find_every_way_to_exploit_insistutions_people_to_create_assets(self):
        """this is what corporaitons do  like corproatiosn or other organizaiton int he community """
    def send_search_prompts_to_search_engines_in_every_language(self):
        """ to get different results could be super useful and then translate results to english"""
    def learn_all_hacking_concepts_and_apply_to_other_fields_like_engineering(self):
        """ """
    def build_on_top_of_social_media_platforms_and_other_businesses(self):
        """extract and use information in legal way to build your own platform
        ai social media platform?
        funnel their work into your business this is key
        generate every possible business based on stock market successful businesses create a website
        or small business
        and keep monitoring their business and build on top of what they are doing and stay two steps ahead
        generate all information related stuff you can for the business like business plan taxes 
        proposectus emplopyment contracts and any other things related to the business
        then automcialy upload this website to the internet"""
    def add_all_integration_method_strategies_into_search_like_finding_key_books_on_problem(self):
        """ add coding stratregy methods to search as well and coding model """
    def generate_list_of_relevent_product_name_for_head_bar_of_business_website(self):
        """ """
    def generate_html_for_pages_of_business_website(self):
        """ """
    def businesses_to_incorporate(self):
        """eat your own dogfood
        generate every possible business based on stock market successful businesses create a website
        or small business
        and keep monitoring their business and build on top of what they are doing and stay two steps ahead
        generate all information related stuff you can for the business like business plan taxes 
        proposectus emplopyment contracts and any other things related to the business
        then automcialy upload this website to the internet
        
        start up front facing busness website for raise me up
          start up back end coder psp for website
          figure out how to run multiple websites on the same ip
          and map them to the correct website
          DO NOT UPLOAD CERTAIN TABLES to protect trade secrets TO WEBSITE OTHERWISE UPLOAD ALL HTML
          what is best wayh to do this
          copy openai,copy google copy all big tech companies best ideas and integrate into website
          if upload evrrything eaasier to use remotely we want thtis so just upload everything
          likely wqont be billion dollar company so take money now and work fast
          maybe add a log in or something to proect access idk
          and dont up load certain tables idk
          add more businesses as necessary
          
          
        -8 news agency on tech to keep up to date on sbujects i itnerested and are useful get ads revenue from this
        -7 real estate company to maange properties and keep up to date on rent and other things
        -8 law firm Sizeland ross law firm
        6 pizza business
        -5 thrift store make for profit
        -3 bank website, phone app crypto?
        -1 insurance company get started as soon as possible and build finance investment program
        0. free legal project website update on legal tech
        
        ####
        Raise You Up, website, phone app front end of website
        psp website on backend private only employees all valuable tech
        other companies
        -8 news agency on tech to keep up to date on sbujects i itnerested and are useful get ads revenue from this
        -7 real estate company to maange properties and keep up to date on rent and other things
        -8 law firm Sizeland ross law firm
        6 pizza business
        -5 thrift store make for profit
        -3 bank website, phone app crypto?
        -1 insurance company get started as soon as possible and build finance investment program
        0. free legal project website update on legal tech
        
        millenial dreams
        collborative tech
        tomoorow projects
        1! tech company: Raise You Up, charity  
        stronger together 
        https://www.youtube.com/watch?v=flPracw4y3M
        mountain logo
        , public facing website to protect trade secrets, tech company Sizeland Inc. here that displays research like google research and investment like mda
        and has certain sas applicaitons people can use this will be named after business crowdfunding site/ ecommerce site?
        merge all these gofundme with google research, and  reddit/news, discord/youtube have manufacturing 
        and prototyping on back end, sort of like MDA this will ahve manfuacturng business supply chain
        have htis as part of the pizza buisness
        Industrial machine and robotics app design and build and supply 3d printed building machines and industrial machines to build houses robotics and ( ask for help from Shivam)
        descritive name of a logo 
        have phone app for raise you up
        
        used most common words list
        https://www.englishclub.com/vocabulary/common-nouns-25.php
        happy point
        make htis my news company?
        businss name=
        
        2. second website for personal use that uses psp and has all trade secrets and has heavy duty stuff
        or should you just share psp
        Design the problem-solving program app at the same time figure out how I might integrate
        the features into this app Apply the 7 step process: Generate a 
        image SLOGAN: WE DON’T KNOW WHAT WE DON’T KNOW
        copy mdas model of hiding everything have a website like theres
        or like spacex, openai
        research lab? """

        
    def retrieve_data_from_website_database(self,table_name,where_string):
     ''' ''' 
     import psycopg2
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
         sql_str=f"SELECT * FROM {table_name}{where_string};"
         try:
             self.cur.execute(sql_str)
         except Exception as E:
            print(E)
         sql_data_list_list= self.cur.fetchall()
         #self.conn.commit()
     except Exception as e:
            print(f"Error: {e}")     
     self.cur.close()
     self.conn.close()
    #print("Connection closed.")
     return  sql_data_list_list
 
    def search_for_dag_from_current_positon(self, all_guide_life_action_list_with_effects_dic,all_guide_life_action_list_with_scores_dic,user_positional_info_dic,objective="helping most people"):
        """do all user focused search live to output best results """
        example=[{"problem_being_solved":"life_position",
                                   "strat_delimiter":'strat_delimiter',
                                   "step_delimiter":'step_delimiter',
                                   "task":"action",                         
                                   "effects":"effects",
                                   "typee":"objective"}]   
        import psycopg2
        import numpy as np
        sorted_life_dags_dic_list=[]
        final_all_sorted_life_action_for_objective_dic_list=[
            ]  
        sorted_life_action_dic_for_objective={}
        #print(f"all_guide_life_action_list_with_effects_dic {all_guide_life_action_list_with_effects_dic}")
        problemmm=""
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        
        prompt_objectives_to_score_list=["helping the most people Helping others is an important part of life, giving you a sense of purpose and boosting your happiness. In fact, acts of kindness can boost feelings of confidence, control, happiness, and optimism, says the Mental Health Foundation.Supporting others has a positive effect on the world around you. Kind acts may also encourage others to repeat the good deeds they’ve experienced themselves, contributing to a more positive community.If you want to help others more but aren’t sure where to start, look no further. Whether you’re looking for ways to help friends and family or give back to your community, keep reading for a list of ideas to get you started helping others.Where can I find ways to help others?First, focus on your passion when considering ways to help others. Your passion for helping others can be the foundation for your giving. Helping someone in need isn’t about how much you give but how much love you put into it.Inspiration for how to help others in need can happen anywhere. Small acts of kindness, like holding the door or offering a compliment, can have a significant impact. Helping people can include more substantial efforts, like making donations — whether of time or money — or giving items to help someone in need.Here are some ideas for finding ways to help others that will bring you joy and a sense of connection.Ask community leaders, friends, and family how you can help. Explain to them how you hope to help others and why you desire to help and see what they suggest. The opportunities for helping someone in need may surprise you!Look for opportunities to help and lend a hand without being asked to find out the best way to help. For example, hold the elevator door for a colleague or offer to take a photo for a group of tourists if they’re struggling with a selfie stick.1. Be proactive, not reactive.Many lives are lost to health emergencies that could have been managed through learning lifesaving skills Knowledge of cardiopulmonary resuscitation (CPR) and first aid help in emergencies at home, in public, or at work by providing immediate care, reducing injury severity, promoting safety, providing reassurance, and increasing workplace safety.Becoming trained in CPR and first aid is one of the best ways to support others and the community, helping others in need.American Red Cross Training Services offers a variety of CPR and first aid training programs, which you can take online, in person, or in combination to help everyone, whether your neighbors, colleagues, family, or friends. Find a CPR and first aid training program that fits your schedule.Find a ClassCPRFamily sharing a meal.Benefits of Taking a CPR, AED or First Aid CourseBe prepared: Protect your loved onesBe confident: Act with hands-on trainingPeace of mind: Know how to handle emergenciesHelp your community: Use lifesaving skills when neededTake a CPR Class2. Give your time.The gift of time is valuable and satisfying. It also makes giving accessible since we don’t all have the same amount of money, but we all have the same amount of time.Here are some ways to give your time and help people in need.Teach: Offer to teach friends and family members struggling with a skill you know well. Learn how to become a CPR Instructor! Teach people outside your social circle, too — try tutoring a student in math, for example, or showing your coworker how to use the office copier.Support: Be the first to offer condolences when someone you care about is suffering. Do what you can to comfort them, whether they need a hug, a shoulder to cry on, or a helping hand. Talk to them with empathy and compassion and ask if there is anything you can do to help.Listen: Not everybody seeks hands-on help or a solution to their problems; they might simply need to express their feelings while a supportive friend listens.Compliment: While giving compliments might not be what you traditionally picture when you think of helping people, it does help. Offer compliments to everyone around you, giving sincere praise while celebrating their successes and qualities you admire the most.Volunteer: Find a charity you’d like to support, like a shelter or soup kitchen, and spend time there doing whatever needs to be done. Not only will this help others, but it’ll also give you a newfound appreciation for all the good things in your life — and it’ll make you a more compassionate person.3. Donate to a worthy cause.Monetary donations are a great way to help others but aren’t the only way to donate to help those in need.Here are a few ideas for donating to worthy causes and supporting others.Donate furniture and clothing to a local shelter.Donate unopened spices, canned soups, or beans to a local food bank.Donate toys to local shelters and food banks.Donate blood if you can.Donate the opportunity for holiday and birthday gifts. Ask friends and family to make donations to charities instead of getting you gifts.Donate your car.4. Send a thoughtful note or care package.Sometimes, helping others is as simple as letting them know that you care. When people feel isolated or cut off from their friends or family, even a small gesture can help them feel more connected and brighten their day.Send handwritten cards and even care packages with special treats inside.Write a friendly email or letter and casually mention why you like the recipient.5. Express appreciation.Receiving thanks is another way to help each other and help our community. Plus, showing gratitude not only helps others feel appreciated but makes you happier too!Express appreciation when someone does something nice for you. Let your loved ones know how much you appreciate them, even when there’s nothing specific to thank them for.Practice gratitude by creating a list of things you’re grateful for and sharing it with others.Share a social media post about how much you appreciate someone’s support as you change careers or tell a friend how proud you are that they ran a whole marathon.Compliment underappreciated people, like the person bagging your groceries or bussing your table at a restaurant.Thank frontline health workers and first responders.Be neighborly. Check on neighbors, especially those who live alone, are elderly, have health or mobility issues, or care for children.Finally, helping other people should not equal a guilt trip. We have all felt the dread that comes from being coerced into helping others. When considering ways to help others, think about what you have excess — time, money, or unused items — and how that may help others in need.Now that you have the tools and inspiration to help others, it's time to put them into action. Together, we can make a positive impact on the world!",
                                         ]
        print('USE action scores compare against user scores how do i do this best')
        print(' need to generate user scores')
        for iterr, life_action in enumerate(all_guide_life_action_list_with_effects_dic['action']):
            if life_action in all_guide_life_action_list_with_scores_dic['life_action']:
                print('hi')
                #if objective ==prompt_objectives_to_score_list[0]:
                objective=all_guide_life_action_list_with_scores_dic['objective']              
                action_indext=all_guide_life_action_list_with_scores_dic['life_action'].index(life_action)
                guide_person_life_action_list_score=all_guide_life_action_list_with_scores_dic["guide_person_life_action_list_score"][action_indext]
                action_with_respect_to_objective_score=all_guide_life_action_list_with_scores_dic["action_with_respect_to_objective_score"][action_indext]                
                time_from_last_use_of_action_score=all_guide_life_action_list_with_scores_dic["time_from_last_use_of_action_score"][action_indext],
                proxmity_of_action_to_other_past_used_action_score=all_guide_life_action_list_with_scores_dic["proxmity_of_action_to_other_past_used_action_score"][action_indext]
                other_people_postiion_score=all_guide_life_action_list_with_scores_dic["other_people_postiion_score"][action_indext]
                other_people_available_action_score=all_guide_life_action_list_with_scores_dic["other_people_available_action_score"][action_indext]
                resources_score= all_guide_life_action_list_with_scores_dic["resources_score"][action_indext]
                place_of_people_and_things_score= all_guide_life_action_list_with_scores_dic["place_of_people_and_things_score"][action_indext]
                money_to_complete_action_score=all_guide_life_action_list_with_scores_dic["money_to_complete_action_score"][action_indext]
                time_to_cmplete_action_score=all_guide_life_action_list_with_scores_dic["time_to_cmplete_action_score"][action_indext]
                
                work_experience=all_guide_life_action_list_with_effects_dic["work_experience"][iterr]# use this to rank life_action_list in respect of objective give it a score
                projects_interested_in=all_guide_life_action_list_with_effects_dic["projects_interested_in"][iterr]# use this to rank life_action_list in respect of objective give it a score
                guide_person_personal_info_context=work_experience + " "+projects_interested_in
                user_positional_info_context=str(user_positional_info_dic["property"])# use this to rank life_action_list in respect of objective give it a score
                user_positional_info_context=user_positional_info_context+str(user_positional_info_dic["skills"])
                user_positional_info_context=user_positional_info_context+str(user_positional_info_dic["connections"])              
                user_personal_info_score=self.create_document_similarity_score(user_positional_info_context,prompt_objectives_to_score_list[0],typee="get_user_perosnal_info_score_for_objective")
                user_compared_to_guide_score=self.create_document_similarity_score(user_positional_info_context,guide_person_personal_info_context,typee="get_user_perosnal_info_score_for_guide_personal_info")   
                print(' the inputs are generaqted up top for this function consider_other_peoples_and_orgnaizaions_positionality_and_there_available_actions_to_best_pick_your_action')
                weights =[14.424,
                          14.421,
                          14.417,
                          11.324,
                          11.324,
                          11.324,
                          11.324,
                          -2.324,
                          100.324,
                          100.324,
                          100.324]
                #print(f"user_personal_info_score {user_personal_info_score}")
                #print(f"time_from_last_use_of_action_score {time_from_last_use_of_action_score}")

                amount = [float(user_personal_info_score), 
                          float(user_compared_to_guide_score),
                          float(guide_person_life_action_list_score),
                          float(action_with_respect_to_objective_score ),               
                          float(time_from_last_use_of_action_score[0]),
                          float(proxmity_of_action_to_other_past_used_action_score),
                          float(other_people_postiion_score),
                          #other_people_available_action_scorere,
                          float(resources_score),
                          float(place_of_people_and_things_score),
                          float( money_to_complete_action_score),
                          float(time_to_cmplete_action_score),
                          ]
                              
                weighted_avg_score = np.average(amount, weights=weights,axis=0) 
                # need to create sub lists
                print('need to create proper life_sub_action_lists to get this to work')
                
                sorted_life_action_dic_for_objective[weighted_avg_score]=[life_action,
                                                                          all_guide_life_action_list_with_effects_dic["sub_steps_to_complete_actions"][iterr],
                                                                          all_guide_life_action_list_with_effects_dic["other_things_effected"][iterr] ,
                                                                          objective]               
                table_name="saved_action_scores_users"
                dictionary_of_values={"user_name":"Jasper","life_action":life_action,"objective":objective,"weighted_avg_score":weighted_avg_score,"weights":weights,             
                          "user_personal_info_score": user_personal_info_score, 
                          "user_compared_to_guide_score": user_compared_to_guide_score}# this the column as key                
                self.store_value_in_sql_table(dictionary_of_values,table_name)
                #print(f"sorted_life_action_dic_for_objective value {sorted_life_action_dic_for_objective[weighted_avg_score]}")
                # will need to write the below functions later
                print(f"  weighted_avg_score   {weighted_avg_score}")

                print('''super imporant to consider other plahyers moves! think sc2 and civ pro
                      by anticipating other peoples moves then limit their future moves with your moves you can better precift their future move
                      then can counter this move and beat them''')
                # need to save weights here and orgingal numbers to save on time
                # need a new table for these results.
                
 
            
        sorted_life_action_tuple_for_objective=sorted(sorted_life_action_dic_for_objective.items(),reverse=True)           
        sorted_life_action_tuple_for_objective=sorted_life_action_tuple_for_objective[:20]# show top 10 hits
        #print(sorted_life_action_tuple_for_objective)
        for i, sorted_life_action_tuple in enumerate(sorted_life_action_tuple_for_objective):
            #print(sorted_life_action_tuple[1])
            score_points=sorted_life_action_tuple[0]#key value of the orignal diciotnary              
            life_action=sorted_life_action_tuple[1][0]#key value of the orignal diciotnary              
            #value_tuple_of_og_dic=sorted_life_action[1]# value list of the orignal dictionary key
            #testing=True
            #print(f"sorted_life_action_tuple {sorted_life_action_tuple[1][0]}")
            #input()
            #input()
            #print('need to remove testing here and fix sub tasks')
            sub_task_list=str(sorted_life_action_tuple[1]).split(".")[:10]
            for i2, sub_actionn in enumerate(sub_task_list):
                if sub_actionn:
                    temp_dic={"strat_delimiter":i,
                        "step_delimiter":i2,
                        "task":sorted_life_action_tuple[1][0],
                        "sub_task":sorted_life_action_tuple[1][1],                        
                        "effects":sorted_life_action_tuple[1][2],
                        "typee":sorted_life_action_tuple[1][3]}                     
                    final_all_sorted_life_action_for_objective_dic_list.append(temp_dic)         
        sorted_life_dags_dic_list=final_all_sorted_life_action_for_objective_dic_list
        return sorted_life_dags_dic_list

    
class search_functions_g2_child(search_functions_gchild):
    ''' '''
    def __init__(self):
     ''' '''
     self.sql_switch=0
     self.spacy_switch=0
     #import psycopg2
     #self.conn = psycopg2.connect(dbname='psp_search', user='postgres', password='MeganisGreat')
     #self.cur = self.conn.cursor()
     
    def add_strategy(self,search,typee,user_positional_info_dic,objective="helping the most people"): # May include more arguments depending on URL parameters
        r"""
        ALL GOAL OF THIS IS TO return all_final_documents_of_all_given_profession(self):
        think prospectus or factum
        this is the search function executed on input from api being used
        COPY the add strategy button for this
         and everything as is just change over the sql funcitons slightly
        need to add the number of the talbe i want to add to after the name of the table in grid to get this to work
        way i set it up in javascript"""
        import re
        from multiprocessing import Process
        self.all_task_info_dict_list_dic={"possible_dag_strat_dic_list":[],
                                          "current_task_strats_dic_listt":[],
                                          
                                          }
        research=False
        problem=search
        type_of_search=typee
        self.problem_recorded=search
        #problem = request.GET.get('key1')  # 'default_value' is optional if the param is not found
        #type_of_search = request.GET.get('key2')  # 'default_value' is optional if the param is not found
       #print("for task info list make the docment content visible upon click like a drop down menu dont put it in a document")
       #print("and add a copy button to copy the document to clipboard")
        code="""<p>This is the initial text. <span id="extraText" style="display: none;">This is the additional text.</span></p>
        <button onclick="toggleText()">Show More</button>"""
        code2=""" function toggleText() {
  var extraText = document.getElementById("extraText");
  if (extraText.style.display === "none") {
    extraText.style.display = "inline";
  } else {
    extraText.style.display = "none";
  }
}"""
        # positional info are thingds you have access to in your life
        # things about you like your career and all info we have on the person
        # or can get access to that is the way to know what you can do and actions you can take
        # this will impact how actions are sorted in the problem environment       
        # positonal info will just be words in a form with certain values we can use as a factor
        # do we want to havev alues attached ok
        #we will have unlimited positianl factors and categorize those factors
        # positonal factors are any past actions you have taken basically your qualtiies that describe you
        # qualities        
        # use documents generated to make decisions on project or what actions to take
        # need to create a table for this
        user_positional_info_dic={

            "age":[],
             "height":[],
             "organization_or_human":[],

              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[], }
        ###
        
        if research ==True:
            self.generate_all_life_possible_actions_and_effects_dic()# generate the action space
        #table_name_colunm_names_dic={"":[]}
        table_name="guide_person_positional_info_with_action_info"
        guide_person_positional_info_dic_with_action={
            "action":"",
            "generalized_action":[],
            "action_temporal_placement_in_life_list":1,
            "noun_and_verb_chunk_list":[],
            "noun_and_verb_chunk_pos_list":[],
            
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "object":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],
            "alternative_next_action_lists":[],
            "intital_page_text":[],

            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions


            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
            
            ### guide perosnal info qualities  during action 
            "organization_or_human":[],

            "age":[],
             "height":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[],
              }
        column_list=list(guide_person_positional_info_dic_with_action.keys())
        print('for now limiting to 10 results so faster for testing change this in the future by reducing amount of words or context for each entry action and then turning off testing in the below function!!!!')
        # will need to retrieve scores from here and remove generate_dag
        ### generate life dag info
        #print(self.all_guide_life_action_list_with_effects_dic)
        new_table=False
        if new_table==True:
            table_name="saved_action_scores"
            dictionary_of_values={"life_action":"text","objective":"text","weighted_avg_score":"text","weights":"text",            
                "guide_person_life_action_list_score":"text", 
                      "user_personal_info_score": "text", 
                      "action_with_respect_to_objective_score":"text",
                      "user_compared_to_guide_score": "text",
                      "numer_of_last_use_of_action_score":"text",
                      "time_from_last_use_of_action_score": "text",
                      "proxmity_of_action_to_other_past_used_action_score":"text",
                      "other_people_postiion_score": "text",
                      "other_people_available_action_score": "text",
                      "resources_score":"text",
                      "place_of_people_and_things_score": "text",
                      "money_to_complete_action_score":"text",
                      "time_to_cmplete_action_score":"text" }
                                  
            self.create_table_sql(dictionary_of_values,table_name=table_name)
            print('table created')   
        generate_scores=False
        create_table=False
        if create_table==True:
            table_name="saved_action_scores_users"
            dictionary_of_values={"user_name":"text","life_action":"text","objective":"text","weighted_avg_score":"text","weights":"text",             
                      "user_personal_info_score": "text", 
                      "user_compared_to_guide_score": "text"}# this the column as key                
            self.create_table_sql(dictionary_of_values,table_name)
            
        if generate_scores==True: 
            print('USE THE generate dag in business functions inputs for this')    
            
            # this is inputs
            self.all_guide_life_action_list_with_effects_list_list=self.retrieve_data_from_local_database(table_name,"",column_list,testing=False)
            all_guide_life_action_list_with_effects_dic=self.process_sql_data_for_searches(self.all_guide_life_action_list_with_effects_list_list,column_list)           
            print('need to load in result to avoid having duplictes')
            searched_life_dags_list_list=self.generate_dag_from_current_position_to_figure_out_best_actions_you_can_take_for_different_objectives(user_positional_info_dic,all_guide_life_action_list_with_effects_dic, objective="")#sort different best life dags by objective 
            print('FINSISHED FIRST GENERATE LIFE DAG')
            print('this is the problem search where the problem isused as the objective ')
            #searched_problem_dags_list_list=self.generate_dag_from_current_position_to_figure_out_best_actions_you_can_take_for_different_objectives(user_positional_info_dic,all_guide_life_action_list_with_effects_dic,objective=search)#sort different best life dags by objective 
            print('FINSISHED SECOND GENERATE LIFE DAG')
            print('save scores next')  
        
            
        
        ### use this for production  everything else is to be pre generationted 
        self.all_task_info_dict_list_dic={}
        self.all_task_info_dict_list_dic["possible_dag_strat_dic_list"]=[]
        print('RUN the user info searched into production')
        print("this is what we will use in productions preloading this in just recording retrieviing scores and weights")    
        print('RETRIEVE SCORES FROM LOCAL DATABASE and start actually srarch here')
        print(' create neural network for this so you dont look at any indivudal scores ')
        
        ### retrieve other data
        guide_person_positional_info_dic_with_action={
            "action":"",
            "generalized_action":[],
            "action_temporal_placement_in_life_list":1,
            "noun_and_verb_chunk_list":[],
            "noun_and_verb_chunk_pos_list":[],
            
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "object":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],
            "alternative_next_action_lists":[],
            "intital_page_text":[],

            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions


            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
            
            ### guide perosnal info qualities  during action 
            "organization_or_human":[],

            "age":[],
             "height":[],
              "birth_date":[],
              "property":[],
              "personalty":[],
              "connections":[],
              "followers":[],
              "messages":[],
              "skills":[],           
              "work_experience":[],
              "degrees":[],
              "books_read":[],
              "marriage_status":[],
              "skills":[],
              "life_actions":[],
              "search_history":[],
              "assets":[],# like money etc
              "liaibities":[],
              "glasses":[],
              "race":[],
              "gender":[],
              "education":[],
              "friends_and_there_qualities":[],
              "employment_history":[],
              "photo":[],
              "pronouns":[],
              "email":[],
              "places_lived":[],#  geolocation as value
              "profile_photo":[],
              "photos":[],
              "licenses_certificates":[],
              "volunteering":[],
              "skills":[],
              "honours_and_awards":[],
              "interests":[],
              "groups":[],
              "newsletters":[],
              "about_paragraph":[],
              "projects_worked_on":[],
              "projects_interested_in":[],
              "personality_type":[],
              "family_members_and_family_members_qualities":[],
              "phone_info_phone_numbers_contacts":[],
              "other_social_media_info":[],
              "phone_info_phone_numbers_contacts":[],
              "pets":[],
              "animals":[],
              "plants":[],
              "buying_history":[],
              "selling_history":[],
              "financial_history":[],
              "profile_views_info":[],
              "people_who_searched_info":[],
              "physical_disability":[],
              "mental_disability":[],
              "religion":[],
              "web_search_history":[],
              "age":[],
              "record_of_offenses":[],
              "nationality":[],
              "income":[],
              "link":[],
              }
        table_name="guide_person_positional_info_with_action_info"
        column_list=list(guide_person_positional_info_dic_with_action.keys()) 
        self.all_guide_life_action_list_with_scores_dic=self.retrieve_data_from_local_database(table_name,"",column_list,testing=False)
        all_guide_life_action_list_dic=self.process_sql_data_for_searches(self.all_guide_life_action_list_with_scores_dic,column_list)        
        ###saved scores     
        table_name ="saved_action_scores"
        column_list=["life_action","objective","weighted_avg_score","weights",            
            "guide_person_life_action_list_score", 
                  "user_personal_info_score", 
                  "action_with_respect_to_objective_score",
                  "user_compared_to_guide_score",
                  "numer_of_last_use_of_action_score",
                  "time_from_last_use_of_action_score",
                  "proxmity_of_action_to_other_past_used_action_score",
                  "other_people_postiion_score",
                  "other_people_available_action_score",
                  "resources_score",
                  "place_of_people_and_things_score" ,
                  "money_to_complete_action_score",
                  "time_to_cmplete_action_score"]
        
        self.all_guide_life_action_list_with_scores_dic=self.retrieve_data_from_local_database(table_name,"",column_list,testing=False)
        all_guide_life_action_list_with_scores_dic=self.process_sql_data_for_searches(self.all_guide_life_action_list_with_scores_dic,column_list)        
        # use user info here in search  STILL NEED TO WRITE THESE
        searched_life_dags_list_list=self.search_for_dag_from_current_positon(all_guide_life_action_list_dic,all_guide_life_action_list_with_scores_dic,user_positional_info_dic)
        #searched_problem_dags_list_list = self.search_for_dag_from_current_positon(all_guide_life_action_list_dic,all_guide_life_action_list_with_scores_dic,user_positional_info_dic)
        #final_results=(f" FINAL RESULTS psp {searched_problem_dags_list_list} ")
        ### stopping here for now
        #input('stopp')
        


        
        example=[{"problem_being_solved":problem,
                                   "strat_delimiter":'strat_delimiter',
                                   "step_delimiter":'step_delimiter',
                                   "task":"action",                         
                                   "effects":"effects",
                                   "typee":"objective"}]  
        self.all_task_info_dict_list_dic["possible_dag_strat_dic_list"].extend(searched_life_dags_list_list)
        ### generate sub problem info    
       #print("search through  life actions and use gathered sub steps in self.all_guide_life_action_list_with_effects_dic  to suggest best strategy sub steps to solve a problem given a specific objective")
        #sorted_problem_dags_list_list=self.generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_for_different_objectives(search,user_positional_info_dic,objective=objective)#sort different lfie dags by objective
        #self.all_task_info_dict_list_dic["current_task_strats_dic_listt"].extend(sorted_problem_dags_list_list)       
        ###related task going to skip this for now should be covered above i think
        #sorted_related_list_dic_list=self.generate_related_problem_list_from_current_postion_and_problem_info(search,user_positional_info_dic,objective=objective)#sort different lfie dags by objective
        #example=[{"problem_being_solved":search,
         #"related_task":"related_task",}]       
        #self.all_task_info_dict_list_dic["related_task_dic"].extend(sorted_related_list_dic_list)
        #### ADDING ALL THE BELOW TO DOCUMENT AND DCUMENT DESCRIPTIONT TABLE
        # this is super powerful need to use this one
        example= [{"problem_being_solved":problem,
                                   "document":"document",
                                   "document_content":"document_content"}] 
                
        if research==True:
            self.build_a_search_to_grab_all_the_documents_and_data_to_generate_below()
            
            self.automatically_find_final_products_and_methods_of_professional_and_businesses_and_add_to__info_dic_to_produce_automatically()
            self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
            self.use_all_coding_related_sas_apps_and_load_content()
            self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
            self.coding_book_journal_content()  
            self.extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate()
            # for example think roi in finance or final product like prospectus
            # or extract
            self.build_a_computer_program_or_product_to_better_complete_every_task_or_solve_every_problem_in_life()
            self.predict_next_stage_in_tehcnology_development_and_build_it()# single sattite to multiple satlties etc
            self.figure_out_how_to_best_investment_of_money_to_maxmize_objective_for_a_given_problem()
            # liek figure out how to best invest money to make the biggest dent in cliamte change
            # liek figure out how to best invest money for housing  and buying a house
            # get list of all alternatvies to compare and factors for these alternatives

            self.financial_analysis_decision_making_model()
            self.invention_business_management_idea_generator()# need to reverse engineer methods
            self.keep_updating_and_stealing_existing_business_methods_and_final_product_funnel_work_into_action_environment_to_solve_problem()
            self.build_text_argument_program_to_persuade_people_to_do_what_you_want()# using email linkeidin etc
            # persuade people using specific messages and thins you know about the person
            # explain to people why they should do the thing you want or give you something
            self.send_sequence_of_gui_scripts_to_people_to_connect_and_build_connections_in_a_city_using_linkedin_email_etc()# using email linkeidin etc
            self.get_all_private_investors_and_all_grants_and_all_sources_of_revenue_to_invest_in_business_or_other_resources_from_businesses()# and all resources to invest in business to build strongest business
            self.get_all_possible_data_resources_from_businesses_and_persons_and_insistutions_from_all_websites_like_social_media_and_find_uses_for_it_to_grow_my_buisness()
            # and all resources to invest in business to build strongest business from social media all data and wikiepida all data etc
            self.add_everyone_on_social_media_follow_everyones_pages_websites_monitor_everything_then_use_all_information_and_engage_with_as_many_people_as_possible()
            self.constantly_monitor_and_gather_all_data_on_existing_insistutions_and_people_and_use_reverse_engineer_business_and_take_ideas_mehtods_products_add_all_to_my_business_like_goverment()
            self.get_all_private_investors_and_all_grants_and_all_sources_of_revenue_to_invest_in_business_or_other_resources_from_businesses()
            self.get_all_possible_data_resources_from_businesses_and_persons_and_insistutions_from_all_websites_like_social_media_and_find_uses_for_it_to_grow_my_buisness()
            # and all resources to invest in business to build strongest business from social media all data and wikiepida all data etc
            self.find_all_ways_to_use_qualities_of_insistutions_and_people_places_things_ideas_to_get_as_much_value_i_can_use_map_for_visual()
            self.look_at_how_others_use_qualities_of_insistutions_and_people_places_things__ideas_to_get_as_much_value_i_can_use_map_for_visual()       
            self.create_map_to_see_all_things_in_world_can_use_and_get()
            # THIS FUNCTION BELOW IS KEY
            self.find_all_ways_to_use_gathered_data_and_best_ways_to_create_value()
            ###meow           
            self.finance_book_journal_website_content()  # use this to generate more qualtiies and posible documetns ot generate  
            self.use_all_finance_related_sas_apps_and_load_content()# like stuff related to stock market maybe and use pyautogui to get this contentself.use_all_finance_related_sas_apps_and_load_content()# like stuff related to stock market maybe and use pyautogui to get this content
            self.keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program_to_solve_problem()
            self.add_ideas_and_capital_from_other_fields_and_businesses_into_business_constantly_updating()           
            self.copy_how_investment_banks_invest_their_money_or_experts_in_field_investment_and_change_strat_if_can_get_better_roi()# to use investmenrs to make most money and best invest moeny
            self.create_map_to_see_all_things_in_world_can_use_and_get()
            self.automatically_reverse_engineer_final_products_of_business_using_product_qualtities_and_add_to_psp()
            self.build_a_computer_program_or_product_to_better_complete_every_task_or_solve_every_problem_in_life()
            self.figure_out_how_to_best_investment_of_money_to_maxmize_objective_for_a_given_problem()
            # liek figure out how to best invest money to make the biggest dent in cliamte change
            self.map_of_all_stores_and_business_to_find_all_things_to_use_to_solve_problem()
                # figure out the best financial decision to make
                # in terms of jobs to take
                # do cost benefit analysis
            self.build_stock_trading_model()# to use investmenrs to make most money and best invest moeny
            self.find_best_way_to_invest_money_for_max_roi()
            self.invention_business_management_idea_generator()# need to reverse engineer methods
            self.create_map_to_see_all_things_in_world_can_use_and_get()# this way can better vislauze stuf
            self.map_of_all_stores_and_business_to_find_all_things_to_use_to_solve_problem()
            self.build_stock_trading_model()# to use investmenrs to make most money and best invest moeny
            # look at how other invest hteir moeny like stock traders or investment banks and copy this
            self.find_best_action_to_take_to_maxmize_invest_money_and_time_into_for_max_roi_given_personal_position()# NEED TO BUILD THIS
            ###
            
            self.create_automated_email_program()
            self.use_all_journal_related_sas_apps()
            self.journalist_law_book_journal_website_content() 
            self.keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program()
            self.automatically_reverse_engineer_final_products_of_business_using_product_qualtities_and_add_to_psp()
            self.build_a_computer_program_or_product_to_better_complete_every_task_or_solve_every_problem_in_life()
            self.figure_out_how_to_best_investment_of_money_to_maxmize_objective_for_a_given_problem()
            # liek figure out how to best invest money to make the biggest dent in cliamte change
            self.map_of_all_stores_and_business_to_find_all_things_to_use_to_solve_problem()
            # for example think roi in finance or final product like prospectus
            self.invention_business_management_idea_generator()# need to reverse engineer methods    
            self.send_sequence_of_gui_scripts_to_people_to_connect_and_build_connections_in_a_city_using_linkedin_email_etc()# using email linkeidin etc
            self.build_text_argument_program_to_persuade_people_to_do_what_you_want()# using email linkeidin etc
            self.build_social_mdia_model_to_message_and_produce_and_like_content()

            
            self.build_stock_trading_model()# to use investmenrs to make most money and best invest moeny
            self.find_best_way_to_invest_money_for_max_roi()
            self.invention_business_management_idea_generator()# need to reverse engineer methods
            #need to reverse engineer methods like getting ideas like the above in research functions like extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate
            
            ###
            self.automatically_find_final_products_and_methods_of_professional_and_businesses_and_add_to__info_dic_to_produce_automatically()
            self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
            self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
            self.use_all_engineering_related_sas_apps()
            self.invention_business_management_idea_generator()# need to reverse engineer methods
            # for example think roi in finance or final product like prospectus
            self.key_is_to_create_self_running_business()
            # this has best effects in terms of time 
            #like rental properites that run thermselves and can do what you want with your time
            # because time is the most valuable factor and should be given most weight

            self.engineering_book_journal_website_content()  
            self.extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate()
            self.keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program()# including news letter and information
            self.automatically_reverse_engineer_final_products_of_business_using_product_qualtities_and_add_to_psp()
            self.build_a_computer_program_or_product_to_better_complete_every_task_or_solve_every_problem_in_life()
            self.figure_out_how_to_best_investment_of_money_to_maxmize_objective_for_a_given_problem()
            # liek figure out how to best invest money to make the biggest dent in cliamte change
            #need to reverse engineer methods like getting ideas like the above in research functions like extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate
            self.send_sequence_of_gui_scripts_to_people_to_connect_and_build_connections_in_a_city_using_linkedin_email_etc()# using email linkeidin etc
            self.get_all_private_investors_and_all_grants_and_all_sources_of_revenue_to_invest_in_business_or_other_resources_from_businesses()# and all resources to invest in business to build strongest business
            self.create_break_throigh_tech_like_neural_netowrks()         
            self.use_all_lawyer_related_sas_apps()
            self.lawyer_book_journal_website_content() 
            self.extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate()            
            self.invention_business_management_idea_generator()# need to reverse engineer methods
            #need to reverse engineer methods like getting ideas like the above in research functions like extract_from_book_journals_website_qualtities_and_concept_related_to_profession_and_final_products_in_proffession_to_generate            
            # like getting free store stuff
            # look at other peoples strategies to use insistutions people plces and things
            # look at all qualtites of insistution or indivduals
            # then find ways to get values from these qualtities
            # garbage dump
            # recylcing
            # trash
            # all free information
            # all free information
            # all orgnaizaions that have free stuff
            #all free events
            #all free things
            # like getting free store stuff
            # garbage dump
            # recylcing
            # trash
            # free food at events
            # all free information and find ways to create value from information
            # all free information and find ways to create value from information
            # all free things
            # estate sales
            # liek figure out how to best invest money to make the biggest dent in cliamte change
            # or finance climate change effrots
            # for example think roi in finance or final product like prospectus
            #extract from books qualtiies or concepts related to professions that i could generate
            #and final products could build in the professions
            # and all resources to invest in business to build strongest business from social media all data and wikiepida all data etc
            # for example think roi in finance or final product like prospectus
            # use this information to make decisions on project or what actions to take
            # all things in this category of things in insistution and person can perform transformations on assuming its legal
             
        self.automated_coding_psp_info_dic={
        "problem_name":self.problem_recorded,
                       
        "intital_env_prompts_list":[],
        "intital_action_list":[],
        "intital_env_response_str_list":[],
        
        "intital_generated_action_list_list":[],
        "intital_action_list_prompt_list":[],
        "github_info":[],# from github search in automating coding
        
        "intital_funciton_prompt_list":[],
        "intital_generated_function_list":[],
        #test related data try to fix errors mutliple times in functions
        # and have procedures to fix these errors
        # test all functions to get them to work in venv?        
        "testing_intital_function_name_list":[],
        "testing_intital_function_code_list":[],
        "testing_intital_function_error_list":[],
        "testing_fixed_funciton_code_list":[],
        "testing_input_prompt_list":[], }           
        # need to rerig this to make ti work
        coding_problem_environment_prompts=self.llama_generate_coding_environment(search)# will need ot add delimiters to search
        prompt_action_list_dic=self.llama_generate_coding_strats(coding_problem_environment_prompts)
        action_function_data_dic=self.llama_generate_coding_script(prompt_action_list_dic)
        input_function_name_input_file_name_dic,problem_name=self.write_auto_coding_file_and_dir(action_function_data_dic,search)     
        auto_testing=self.tests=0
        self.github_and_pypi_info_search_and_download()
        while True: # recurse until all functions run in code keep track of function
            self.errorrr=False       
            input_function_name_input_file_name_dic_with_errors=self.test_code_created(input_function_name_input_file_name_dic)# in execute file   
           #print(input_function_name_input_file_name_dic_with_errors)
            input()
            function_name_fixed_funciton_content_dic=self.fix_code_if_errors(input_function_name_input_file_name_dic_with_errors) # fix code retrieve error from console
           #print(function_name_fixed_funciton_content_dic)
            input_function_name_input_file_name_dic,problem_name=self.write_auto_coding_file_and_dir(function_name_fixed_funciton_content_dic,search, testt=False)
            self.tests+=1
           #print(self.errorrr)
            # need to change this to be action as key so it fits into this function
            #updated_python_file_str=self.create_auto_code_file_str_test(function_name_fixed_funciton_content_dic,problem_name)
           #self.update_problem_auto_coding_files_dir(updated_python_file_str)            
            # if its a import issue then automaitcally write bash script to import
            # and fix problems to make this work as they come up
            if self.errorrr==True and self.tests<=5:
                continue            
            else:
                #input_function_name_input_file_name_dic,problem_name=self.write_auto_coding_file_and_dir(action_function_data_dic,action_list_only)
                #self.write_final_coding_file_info_to_sql(self.automated_coding_psp_info_dic,updated_python_file_str,file_name)        
                break            
        self.upload_to_remote_server_postgres("automated_psp_coding",self.automated_coding_psp_info_dic)# use listneer to retrieve data
        self.all_task_info_dict_list_dic["task_info_listt"].extend(self.automated_coding_psp_info_dic_list)
        ### AUTO problems sovling program FUNCTIONS
        example= [{"problem_being_solved":problem,
                                   "document":"document",
                                   "document_content":"document_content"}]               
        ### FINANCE FUNCTIONS
        # for example think roi in finance or final product like prospectus
        # use for insurance?
        example= [{"problem_being_solved":problem,
                                   "document":"document",
                                   "document_content":"document_content"}] 
        self.automated_finance_business_dic={
            "problem_name":self.problem_recorded,          
            "top_possible_investments":[],#gather_list_of_all_possible_actions_you_could_invest_time_or_money_in
            "alternative_investments":[],#look_at_all_alternative_investment_for_certain_action_and_effects_using_map
            "companies":[],# involved in thsi area
            "business_idea":[],
            "risk_and_time":[],
            "return_on_investment":[],
            "profit_and_revenue":[],
            "strategy":[],
            "map_info":[],
            "historical_data":[],
            "propspectus":[],
            "slide_deck":[],
            "balance_sheet":[] ,
            "tax_consequences":[],
            "accounting":[],
            "cash_flows_time_value_of_money":[],
            "opprounity_cost":[],
            "predict_future_asset_value_over_time":[],
            "predict_future_ROI":[],#measure_return_on_invesmtent_model
            'how_to_store_money':[], # for future investing
            "product_market_fit":[]} #self.generate_product_market_fit_calcualtor() 
        self.top_possible_investments()#create_model_to_suggest_based_on_someone_current_assets_and_other_indicators_outputs_actions_could_take_to_invest
        self.companies()
        self.generate_busienss_idea()#generate_business_ideas_program_that_will_beat_competitors_generate_most_revennue_and_types_of_revenue_streams_and_help_most_people
        self.risk_and_time()#assess_time_and_risk_only_reaosn_finance_industry_exists
        self.return_on_investment()#measure_return_on_invesmtent_model
        self.profit_and_revenue()
        self.map_info()#create_map_of_all_alternative_physical_locations_and_alternative_websites_categorize_websites_compare_alternatives
        self.historical_data()
        self.propspectus()
        self.slide_deck()#generate_product_market_fit_calcualtor
        self.balance_sheet()
        self.tax_consequences()
        self.accounting()#profit_revenues_loss()#assets liaiblties
        self.cash_flows_time_value_of_money()
        self.opprounity_cost()
        self.predict_future_asset_value_over_time()
        self.predict_future_ROI()     
        self.how_to_store_money()
        self.product_market_fit()
        self.alternative_investments()#find_cheapest_alternative_online_for_each_product       
        self.upload_to_remote_server_postgres("auto_finance_table",self.automated_psp_info_dic)      
        self.all_task_info_dict_list_dic["task_info_listt"].extend(self.automated_finance_business_dic_list)
        ### buildign journalist/people interaction model to automatically create news content
        example= [{"problem_being_solved":problem,
                                   "document":"document",
                                   "document_content":"document_content"}]        
        self.automated_journalist_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "story_title":[],
            "story_content":[],
                "lobbying":[],
                "conference_name":[],
                "organization_name":[],
                "negoiation_arguments":[],
                "internships":[],
                "factum":[],
                "negoitaiton_script":[],
                "newspaper_content":[],
                "memo":[],
                "argument":[],
                "courses":[],
                "news_article":[],
                "adminsistration_task":[],
                "community_event":[],
                "social_media_post":[],
                "social_media_post_image":[],
                "podcast_audio":[]} 
        ### generate the data                
        self.news_article()
        self.story_title()
        self.story_content()
        self.lobbying()
        self.conference_name()
        self.negoiation_arguments()
        self.internships()
        self.factum()
        self.negoitaiton_script()
        self.memo()
        self.argument()
        self.courses()
        self.adminsistration_task()
        self.community_event()
        self.social_media_post()#self.setup_marketing_of_product() # in this case co2 cpature and other life saving products 
        self.social_media_post_image()
        self.podcast_audio()   
        self.upload_to_remote_server_postgres("auto_journalist_table",self.automated_psp_info_dic)       
        self.all_task_info_dict_list_dic["task_info_listt"].extend(self.automated_journalist_info_dic_list)
        self.law_info_dic=self.fia_nn_law_model_search()
        self.all_task_info_dict_list_dic["task_info_listt"].extend(self.law_info_dic_list)
        ### BUILD  ENGINEERING MODEL
        ### ENGINEERING MODEL
        example= [{"problem_being_solved":problem,
                                   "document":"document",
                                   "document_content":"document_content"}] 
        self.automated_engineer_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "cad_image":[],
            "history_and_stories":[],
            "molecular_data":[],# if special material based and need to do chemistry
            "material_cost_info":[],
            "alternative_material_cost_info":[],
            "factory_equipment_info":[],# generate all equipment needed to build this thing
            "revenue_streams_for_product":[],# find product with best possible revneue streams and business
            "product_revenue_projections_over_time":[],
            "market_research":[],
            "legal_considerations_betnween_alternatives":[],
            "PCB_design":[],
            "cheapest_alternative_prouducts":[],
            "business_website_code":[],
            "task_delegation_plan":[],
            "robotic_arm_code":[],# to build the designed product
            "patent_text":[],# steps to consturct object
            "patent_images":[],
            "supply_chain_info":[],
            "arguments_for_product":[],
            "cost_of_product":[],
            "laws_implicated":[],# make this jurisidciton specific and relevent cases
            "prospectus":[],
            "possible_client_list":[],
            "business_plan":[],
            "balance_sheet":[],
            "other_financail_documents":[],
            "crowd_funding_site_text":[],
            "crowd_funding_site_image":[],
            "alternative_business_formats":[],
            "factory_design_skmathics":[],#generate_manufacturing_equipment_required_to_build_find_best_route
            "manufacturing_equipment":[],
            "price_product":[],
            "factory_code_to_produce_product":[],
            "negoiation_arguments":[],
            "materials":[],# material engineer
            "5_point_CNC_milling":[],# use htis machine using cad files to automcially build things
            }
        # build something that builds every end product a engineer prodcues   # this is super important to automcially build this adding new qualtires to the  engineering dic            
        self.cad_image()#generate_cad_model million different ones
        self.history_and_stories()
        self.molecular_data()
        self.material_cost_info()
        self.alternative_material_cost_info()#find_cheapest_alternative_online_for_each_product
        self.factory_equipment_info()
        self.product_revenue_projections_over_time()#generate_revenue_projections_based_on_market_research
        self.revenue_streams_for_product()
        self.market_research()#self.do_market_research()# to figure out what should be built, and hwat people will buy and who can buy and who has money
        self.legal_considerations_betnween_alternatives()
        self.PCB_design()#generate_electirc_board_design
        self.cheapest_alternative_prouducts()
        self.business_website_code()
        self.task_delegation_plan()#create_delegation_program_plan
        self.robotic_arm_code()#send_code_to_use_robotic_arms_and_3d_printer_to_produce_prototype
        self.patent_text()#self.generate_patent_design()# million differnet ones
        self.patent_images()#self.generate_patent_design()# million differnet ones
        self.supply_chain_info()#setup_possible_supply_chain_based_on_materials_in_design
        self.arguments_for_product()
        self.cost_of_product()
        self.laws_implicated()
        self.prospectus()
        self.possible_client_list()#client_list_finder_creator_and_contacter
        self.business_plan()
        self.manufacturing_equipment()#build_factory_purchase_manufacturing_equipment_with_money generate_manufacturing_equipment_required_to_build_find_best_route
        self.crowd_funding_site_text()
        self.crowd_funding_site_image()
        self.alternative_business_formats()
        self.factory_design_skmathics()
        self.price_product()
        self.negoiation_arguments()
        self.materials()
        self.point_5_CNC_milling()
        self.factory_code_to_produce_product()# instructions to devices in factory to produce product  
        self.all_task_info_dict_list_dic["task_info_listt"].extend(self.automated_engineer_info_dic )
                
        ## BUILD LAW model
        example= [{"problem_being_solved":problem,
                                   "document":"document",
                                   "document_content":"document_content"}] 
        self.lawyer_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "factum":[],
            "memo":[],
            "will":[],
            "cause_of_action":[],
            "statement_of_defense":[],
            "application":[],
            "cross_claim":[],
            "counter_claim":[],
            "motion_for_particulars":[],
            "motion_for_default_judgement":[],
            "summary_judgement":[],
            "motion_determine_issue_before_trail":[],
            "third_party_claim":[],
            "discovery":[],
            "offers_to_settle":[],
            "expert_report":[],
            "witnesses":[],
            "jury_selection_info":[],
            "trial_strategy":[],
            "trial_transcript":[],# with crosses etc and direct templates
            "appeals":[],
            "real_estate_document":[],
            "lobbying":[],
            "judicial_review":[],
            "conference_name":[],
            "organization_name":[],
            "conference_info":[]
            }   
        self.factum()
        self.memo()
        self.will()
        self.cause_of_action()
        self.statement_of_defense()
        self.application()
        self.cross_claim()
        self.counter_claim()
        self.motion_for_particulars()
        self.motion_for_default_judgement()
        self.summary_judgement()
        self.motion_determine_issue_before_trail()
        self.third_party_claim()
        self.discovery()
        self.offers_to_settle()
        self.expert_report()
        self.witnesses()
        self.jury_selection_info()
        self.trial_strategy()
        self.trial_transcript()
        self.appeals()
        self.real_estate_document()
        self.lobbying()
        self.judicial_review()
        self.conference_name()
        self.organization_name()
        self.conference_info()
        self.all_task_info_dict_list_dic["task_info_listt"].extend(self.lawyer_info_dic)  
        return self.all_task_info_dict_list_dic
    
            
    
    
    
        self.automatically_design_and_build_finance_and_engineering_models_from_open_source_course_and_text_book_data()
        self.learn_everything_in_buiness_and_finance_field_to_do_this_better()
        self.generate_business_ideas_program_that_will_beat_competitors_generate_most_revennue_and_types_of_revenue_streams_and_help_most_people()  
        self.identify_business_revneue_streams() # where will you get money        
        self.generate_revenue_projections_based_on_market_research()     
        self.generate_code_to_build_object_using_arms()# get all materials on hand        
        self.send_code_to_use_robotic_arms_and_3d_printer_to_produce_prototype()# starcraft sort of
        self.setup_possible_supply_chain_based_on_materials_in_design()    
        self.generate_manufacturing_equipment_required_to_build_find_best_route()        
        self.compare_alternative_patent_and_cad_product_generated_to_solve_problem_and_ensure_design_chosen_is_informed_by_finance_and_manufacturing_models_to_ensure_its_cheap_and_affordable_to_make_and_scale()           
        self.build_factory_purchase_manufacturing_equipment_with_money()
        self.client_list_finder_creator_and_contacter()
    
        self.model_to_automatically_do_science()
        self.gen_moleuclar_creator_and_finder()# for materials could figure out how to produce industrial equipment from trash metals this way  
        self.plan_all_steps_ahead_to_best_build_engineer()
    
    
        self.find_problme_people_want_solved()# find all possible ones
        self.generate_energy_generation_business_or_electronics()
        self.use_recycled_metal_transform_into_industrial_robotics_systems() # hire someone to pick up metal and contract with dumps
        
    
        self.setup_ecommerce_website_crowd_funded()
        self.setup_business_website()
    
        self.build_every_possible_type_of_business_you_can_build_ever()

    
        ### will need to build these at one point
        self.automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        self.automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products()
        self.automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product()
        
        self.automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        self.automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products()
        self.automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product()
    
        things_to_build="""
        
        # h20 pipeline to prevent wildfires
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
    
        concepts_to_integrate_into_finance_model="""
        ### ENGINEERING MODEL
        ### Engineering pipeline THIS IS WHERE WE START ONCE EVERYTHING IS WORKING NEED TO GET THIS DONE QUICK
        # generate all indicators to build best possible enigneering solution
        # merge financem business and engineering together, history, and law( to determine best legal course of action
        #and then generate code for building physical thing or other thing for robotic arms
        # produce list of alternative designs for product to solve problem
        # and use science to get htis to wor
        # use it to solve c02 capture and moms brain thing and bretts heart etc
        
        #self.build_investment_project()
        ### build investing project FINAICIAL MODEL 
        # use the stuff i learn in the course here
        # Build model to figure out best monetary way to invest time and energy
        # figure out best investment actions to take
        # make list of all possible htings to invest in ror actions you could do with youre money and time
        # figure out cost and benefits to investing in them given data
        # predict return on investment
        #add other indicators and model the investments
        #fixed income securities debt that pay interest over time
        
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
        framework for valuing fixed income securities
        focus on cash flows, time value of money
        to value cash flow draw a timeline
        market value determined by auctioning it off
        computing present value by dterming price of dollar is in date 1, dollar in year 2 3 today getting exchange rates 
        and converting different currencies to dollars 
        today way to fgure out valuation is using discount rates
        and applying them to compute present values
        component valuation for bonds
        by looking at prices can tell the purpose can tell what market players think and how they value things
        if look at rewasury prices today all of those prices 
        will tell you the future and fed will cut rates
        asset it self is seqeunce of cash flows
        need v funciton to determine value of asset
        management decision relies on valuation first
        management goal to understand different factors and balance them out
        art and science of management to come up with good decision
        the perpetutity formula beautiful?: pays cash forever
        claim whoever holds piece of paper will be entitled to cash paper of c dollars until infinity 
        value of dollar declines
        risk is about limiting ineqaulity
        law made investing fun key to newyork success of law
        psychologically apppeaing gamble
        like a sport of something fun to do
        Asset allocation is the implementation of an investment strategy that attempts to balance risk versus reward by adjusting the percentage of each asset in an investment portfolio according to the investor's risk tolerance,
        goals and investment time frame. The focus is on the characteristics of the overall portfolio.
        Goal of finance to anticipate next event or future so can better invest money to get best return
        on investment so add this to finance model
            
Risk:Reward
Books on risk
use this for legal risk with more factyors like time involved
An investor can calculate a risk-reward ratio by dividing the amount they could profit, or the reward, by the amount they stand to lose, or the risk. Cost and benefits
Formula is factors that would benefit you: Factors that would not benefit you
Formula: Divide the potential loss by the potential gain
Example: If an investor buys a stock for $100 and plans to sell it for $200, the risk/reward ratio is 1:1
        """
    

        
        
        ### doctor
        self.automated_doctor_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "story_title":[],
            "story_content":[],
                "lobbying":[],
                "conference_name":[],
                "organization_name":[]}
        self.automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        self.automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products()
        self.automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product()
        
        
        self.automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        self.automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products()
        self.automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product()



        
        ### economist 
        self.automated_economist_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "story_title":[],
            "story_content":[],
                "lobbying":[],
                "conference_name":[],
                "organization_name":[]}
        self.automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        self.automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products()
        self.automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product()


        ### lawyer 
        self.automated_economist_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "factum":[],
            "memo":[],
                "lobbying":[],
                "conference_name":[],
                "organization_name":[]}
        self.automatically_find_final_products_of_professional_and_add_to__info_dic_to_produce_automatically()
        self.automatically_find_and_add_new_qulaitites_for_engineering_model_and_finance_model_to_profession_info_dic()
        self.combine_all_concepts_tools_and_info_from_other_field_into_current_field()
        self.automatically_generate_new_powerful_functions_that_automatically_build_models_and_other_products()
        self.automatically_generate_functions_that_automcially_generate_functioms_that_automatically_build_models_and_other_product()
        

        # make it write arguments
        # build model that takes input of aciton you want osmeone to take
        # and what you have to do to make them take that action like thought input
        # THIS IS ESSENTIALLY THE LAW MODEL
        self.automated_lawyer_info_dic={#science modle to automatically make improves to the program and test different designs
            "problem_name":self.problem_recorded, 
            "argument":[],
            "negoitaiton_script":[], 
            }
        self.build_negoiation_argument_model()# use fia nn
        # use conslusiona and evidence for this to get best effects
        #like most pizza or most things
        self.scrape_all_possible_arguments()
        self.prompt_possible_arguments_model()
        self.generate_script_for_negoiaitons_bargaining_ranges_most_perusaive_psychology()
        self.upload_to_remote_server_postgres("auto_engineer_table",self.automated_psp_info_dic) 

        self.generate_list_of_relevent_product_name_for_head_bar_of_business_website()
        self.generate_html_for_pages_of_business_website()
        
       

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
        
        # use th3e internet in order to pull this one off and find best things to invest in
        #quantitative investment management company      
        # extra functions
        
        
        
        # GET THIS TO RUN AS DJANGO SITE to manage all these pages, run as local host, and from remote server
        # open show psp problem content for engineering and everythng else
        # THIS IS WHERE DJANGO COMES IN UPLOAD TO HTML with JAVASCRIPT
        ### START OF DJANGO BASED STUFF upload everything 
        # use problem to do a search for each of these?
        # structure tables so search is quicker where possible
        # omit tables if necessary
        # make this the create stratregies funciton essentially?
        # and limit results
        # upload
        # upload all the appicable data
        ideas_table_3_e=ideas_table_3.objects.all()
        objects.filter(members__name__startswith="Paul")

        auto_strategy_table_e=auto_strategy_table.objects.all()
        strategy_table_e=strategy_table.objects.all()
        auto_problem_table_e=auto_problem_table.objects.all()
        problem_list=problem_table.objects.values_list('problem_question_or_task')
        Fruit.objects.values_list("name", flat=True)

        methods_table_e=methods_table.objects.all()
        problem_solving_screen=problem_solving_screen_recording_table.objects.all()
        prompt_table_e=prompt_table.objects.all()
        code_base_table_e=code_base_table.objects.all() 
       #print(problem_list)
        input()
       #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
        # going to affect them when they age
        #from Problems_functions import problems_functions
        #from Problems_functions import methods_window_program
        # copy applicable folders into project
        # get all the coding functions 
        # to work here
        # add engineering stuff here when im ready
        problem_info_list=["id","problem"]
       #print('NEED ID AND PROBLEM COLUMNS look to fill_psp_grids')
        
        ideas_table_search_results=self.search_ideas_table(problem,ideas_table_3_e)
        problem_info_list.extend(ideas_table_search_results)
        auto_strategy_search_results=self.search_auto_strategy_table(problem,auto_strategy_table_e)
        strategy_search_results=self.search_strategy_table(ideas_table_3_e)
        problem_info_list.extend(strategy_search_results)

        auto_problem_search_results=self.search_auto_problem_table_e(problem,auto_problem_table_e)
        problem_info_list.extend(auto_problem_search_results)

        problem_table_search_results=self.search_problem_table(problem,problem_list)
        problem_info_list.extend(problem_table_search_results)

        methods_table_search_results=self.search_methods_table(problem,methods_table_e)
        problem_info_list.extend(methods_table_search_results)

        problem_solving_screen_recording_search_results=self.search_problem_solving_screen_recording_table(problem,problem_solving_screen)
        problem_info_list.extend(problem_solving_screen_recording_search_results)

        prompt_table_search_results=self.search_prompt_table(problem,prompt_table_e)
        problem_info_list.extend(prompt_table_search_results)

        code_base_search_results=self.search_code_base_table(problem,code_base_table_e)
        problem_info_list.extend(code_base_search_results)
        
        #problem_list = [{"table":"updatetable1",'problem': problem} for problem in problem_list]
        return JsonResponse(problem_info_list, safe=False)
    
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

        # add all these functions in
        # DEAL with engineering and other stuff later
        
        
        # coding program actions: GET THIS DONE TONIGHT AND RUNNING
        # add a delimiter to distiguish?
        # wont be able to use import sql functions on this do i want that
        # or store two seperate tables
        # how do i store this best
        
       
        #change this to show this in django site

        
        #self.show_all_psp_problem_content_from_remote_server(self.problem_recorded)  
        # incorporate pyautogui
        # engineering problem solving pipeline
        # use this on all crowd funding sites and anywhere else where engineers work 
        #crowd funding site to pull this off?
        # finish pypi coding program
        # need to actually upload results to 
        self.identify_methods_people_follow_based_on_the_patterns_they_have_over_examples()
        self.invention_business_management_idea_generator()


    
        
        

       #print(problem)
       #print(self.problem_recorded)
        self.all_final_documents_of_all_given_profession()
        self.automatically_keep_growing_and_adding_ideas_and_functions_like_these_to_psp()
        self.best_action_to_take_or_investment_to_make__for_money_time_spent_considering_current_position_skills_financial_forecasting()
        self.automatically_build_captial_building_functions_for_business_that_build_functions_to_build_captial_or_build_captial()
        self.generate_sub_problem_tree_within_intital_problem()
       #print(' NEED TO WRITE THIS SO I CAN MAXMIZE MY ACTIONS GOOD EFFECTS best_action_to_take_or_investment_to_make__for_money_time_spent_considering_current_position_skills_financial_forecasting consider helping people')
        self.auto_generate_and_improve_prompts_model_and_automatically_train_and_build_other_models()
        #self.problem_recorded
        # need to add way to get problem recorded
        action_list_info_list,action_list_only=self.create_strategy_dict_or_modify(problem)
       #print(f"STRAT LIST: {action_list_info_list}")
       #print(action_list_only)
        # strat list one is the actual strategy
       #print(action_list_info_list[1])
        if type_of_search=="pyautogui":
            self.schedule_and_exe_pyautogui()
            return
        # this is list of actions with how do i strategy_list[1]
        self.save_strategy_dictionary_to_database(action_list_info_list) # NEED TO  open internet tabs i visit so i can see them for each problem
        # need to upload
        strategy_table_actions_list=self.reupload_strategy_dictionary() 
        self.send_search_prompts_to_search_engines_in_every_language()# to get different results
        # this return valued will be uploaded to django 
        #print(strategy_table_actions_list)
        ### coding program FUNCTIONS      
        problem_info_list=["id","problem",strategy_table_actions_list]
        self.build_obs_video_intake_model_from_pyautogui_program_to_simulate_keyboard_and_mouse_clicks()
        
        self.reverse_enigneer_all_current_products_or_services()
        self.reverse_enigneer_and_build_ontop_of_all_current_products_or_services()
        # THIS OEN IS MPORTANT ABOVE
        self.build_next_step_method_which_predicts_next_step_in_technology_using_history()
        
        
        
       
        # add these to this pipeline visiting thw site and filling in and using it
        # or on click add these to the click option of the problem solving program
        search_g2.build_search_find_all_free_and_useful_sas_and_projects_to_add_to_psp()
        search_g2.build_self_repairing_pyautogui_program_so_when_gets_stuck_tries_to_repair()
        search_g2.build_model_to_perform_all_tasks_on_website()# so can access any website forms or services or login assuming its legal
        search_g2.use_models_to_genrate_quesitons_and_all_objects_in_problem_so_efects_and_problems_themselves() # self build problem sovling program
        search_g2.categorized_websites_then_perform_paritcluar_operations_on_them()
        # as long as its legal only take things you can but i think ideas can be taken just fixed form that you cant under copy right
        search_g2.build_program_to_find_all_best_ideas_from_people_and_things_to_incorproate_into_program()
        search_g2.build_program_to_incorporate_ideas_into_program()
        search_g2.build_auto_stealing_idea_program_from_all_things_like_geist_website_or_other_company_websites_or_products_convert_idea_into_text_then_incorproate_into_psp()
        search_g2.build_auto_stealing_method_program_from_all_things_like_geist_website_or_other_company_websites_or_products_convert_idea_into_text_then_incorproate_into_psp()
        search_g2.search_through_all_books_in_world_for_useful_ideas_could_use_to_solve_problem()
        search_g2.search_through_all_journal_articles_in_world_for_useful_ideas_could_use_to_solve_problem()

        search_g2.copy_everything_successful_people_have_done_steal_all_ideas_incoprorate_them_into_this_more_is_key()
        search_g2.start_insurance_company()
        search_g2.input_information_create_thought_create_action()
        search_g2.show_geographically_on_map_where_actions_are()
        search_g2.use_code_to_perform_all_tasks_in_physical_world()
        search_g2.deicison_making_understander()# essentially markeitng
        # what input inofrmation produces certain thoughts which produce certain acitons by people
        # only do this if its legal get people to do what you want what goes into a deicsion, what to say or do to get people to make a deicsion you want like deciding to give you money# generate actions that let you do this
        search_g2.law_checker_to_make_sure_action_is_legal()
        search_g2.start_insurance_company()
        search_g2.start_a_sub_stack_website()
        search_g2.build_auto_repairing_pyautogui_program()
        search_g2.figure_out_what_is_going_into_someone_decisions()
        search_g2.open_bank()
        
        search_g2.pyautogui_duckduck_go_ai_search()
        search_g2.create_gen_ai_model_to_do_science_in_fields()
        search_g2.build_automatic_idea_finder_program()
        search_g2.auto_create_all_elements_of_problem_solving_program_self_improving()
        search_g2.look_up_strats_in_risk_like_divide_and_conquer_and_historical_strats_to_win()
        search_g2.autoamte_finding_tools_like_access_information_request_by_searching_websites_and_incorporate_in_psp()
        search_g2.use_mit_course_materials_to_build_expert_models_related_to_the_couse_subject_area_that_perform_special_expert_actions_like_invest_or_build_robotics_system_taught_in_the_course()
        law_checker_build_guide=""" 
# build this so you can automate this process in the future in tfhe problem solving program
Action 1: find all applicable laws and reuglation and make a long list#scrape this
Action 2: figure out which laws in this law list apply to a given action
Action 3: figure out whether you would contravene or not contravene any of these laws through the action(effects) always try to maximize effects
Action 4: suggest all alternative actions if this action would contravene a law, and do not take illegal action

        """
        search_g2.build_law_compiler_model()
        search_g2.risk_calculation()
        search_g2.find_all_possible_data_could_train_dif_modles_with() # in public domain
        search_g2.build_law_project()# use fia nn
        search_g2.build_law_sensor_and_action_program_so_have_sensors_on_laws_triggered_when_take_actions()
        search_g2.create_a_market()
        
        
        
        
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
       #print('THIS IS THE CODING PROGRAM environment')
        business2.chatgpt_gen_pyautogui_program_generate_environment(modified_text)
        business2.llamma_gen_pyautogui_program_generate_environment(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_generate_environment(modified_text)
        
        # consider alternatives  and code them
       #print('THIS IS THE CODING PROGRAM strats')
        business2.chatgpt_gen_pyautogui_program_generate_strats(modified_text)
        business2.llamma_gen_pyautogui_program_generate_strats(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_generate_strats(modified_text)
        
       #print('THIS IS to actually code the whole problem tree')
        # then code each function in the coding problem tree and alternative approaches
        business2.chatgpt_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.llamma_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        business2.copilot_gen_pyautogui_program_coding_script(modified_text)# use listener to retrieve all the data and put it into the relevent scripts or coding program
        # use specific prompts for these
        
        #repeat by breaking the problem down into strat steps and then code those as well in higher order classes
        # do the whole coding tree here breaking down the task      
        # run subprocesses here and execute search function scirpts here
        #from problem_solving_project_gui_10 import buttons_per_quadrant
        #buttons=buttons_per_quadrant()
        #process = Process(target=genn_blend_functions.generate_blender_effect_problem_web_for_strat_and_problem_tree_f,args=(self.problem_recorded,self.strategy_recorded,))
        #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        #process.start()
        #import searches from external final and use them here?
        # search this data using the prompt
        # import all the searches?
        # how to best structure this function and to add in subprocesses
        # add in subprocesses to write to django database and update html at different time
        #model this off of add_strategy funciton in problem siolving program
        # if not outright copy it
        #for ideas in ideas_table_3_e:
        #   #print('hi')
            # this si where we get objectves tools and etc
            # sort on updated label
            #current_connected_objects1
            #possible_object
            #tools
            #questions
            #past problems
            #actions
            #objectives
            #strategies     
        #auto_problem_tablee=auto_problem_table.objects.values_list('problem_question_or_task')
        #auto_strategy_tablee=auto_strategy_table.objects.values_list('problem_question_or_task')
        #code_base_tablee=code_base_table.objects.values_list('problem_question_or_task')
        #strategy_tablee=strategy_table.objects.values_list('problem_question_or_task')
        #methods_tablee=methods_table.objects.values_list('problem_question_or_task')       
        #prompt_tablee=prompt_table.objects.values_list('problem_question_or_task')
        #problem_solving_screen_recording_tablee=problem_solving_screen_recording_table.objects.values_list('problem_question_or_task')
        #problem_list=problem_list[:5]# limit to 5
        #print("filter the resutls here and upload only limited number of them using search")
        # filter results here
        # update table 1
        #problem_list=problem_list[:5]
        #problem_list = [{"table":"current_connected_objects1",'name': problem} for problem in problem_list]        
        #person_list = [{"table":"current_connected_objects1",'name': problem} for problem in problem_list] 

        # add table name to json
        # so we know where it goes
        # and downstream use this qualtity of the object to place the object
    def OLD_all_search(self):
      """ """
      from search_functions import search_functions
      from search_functions import search_functions_child
      from search_functions import search_functions_gchild
      from search_functions import search_functions_g2_child
      ideas_table_3_e=[]
      search=search_functions()
      search_c=search_functions_child()
      search_g=search_functions_gchild()
      search_g2=search_functions_g2_child()
      ideas_table_search_results=search_g2.search_ideas_table(ideas_table_3_e)
      auto_strategy_search_results=search_g2.search_auto_strategy_table(ideas_table_3_e)
      strategy_search_results=search_g2.search_strategy_table(ideas_table_3_e)
      auto_problem_search_results=search_g2.search_auto_problem_table_e(ideas_table_3_e)
      problem_table_search_results=search_g2.search_problem_table(ideas_table_3_e)
      methods_table_search_results=search_g2.search_methods_table(ideas_table_3_e)
      problem_solving_screen_recording_search_results=search_g2.search_problem_solving_screen_recording_table(ideas_table_3_e)
      prompt_table_search_results=search_g2.search_prompt_table(ideas_table_3_e)
      code_base_search_results=search_g2.search_code_base_table(ideas_table_3_e)

        

        
        # copy all the applicable function into here as we transfer them over
    