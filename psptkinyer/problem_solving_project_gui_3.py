# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:40:12 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
import tkinter as tk
from tkinter import *
import time
program_start_time=time.time()
window = tk.Tk()
window.state('zoomed')
window.title('Problem Solving Program')

   


def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


class buttons_per_quadrant():
    def __init__(self):
        """ """
        import pyperclip
        from ctypes import windll
        import pyautogui

    def handle_click(self, event):
        """ """
        print("The button was clicked!")
    def switch_to_step_building_method(self):
        """ button on top of screen clicked will change the names functions and textboxes used in program"""
        
    def import_tools_problems_or_existing_ideas(self, label,table_name= "labels_for_idea_program_2"): 
        """  import data to different quadrants on the page """
        
        self.cur.execute(f"""SELECT sentence FROM {table_name} WHERE label={label};""")
        label_list=[]
        all_idea_in_database_list_format= self.cur.fetchall()
        for idea in all_idea_in_database_list_format: 
            label_list.append(str(idea))
            continue
        # how to get value of the 
        return label_list
    
    def divide_problem_into_pos_from_main_box(self, sentence):
        
        import en_core_web_trf
        nlp = en_core_web_trf.load()
        for i,idea in enumerate(all_idea_in_database_list_format):
            pos_unmodified_sentence = nlp(idea[5])
            temp_sentence_pos_list=[]
            
            for part_of_speech_parts in pos_unmodified_sentence:
                word_with_pos=[part_of_speech_parts,part_of_speech_parts.pos_]
                temp_sentence_pos_list.append(word_with_pos)

                #print(part_of_speech_parts.pos_)
                #print(part_of_speech_parts)

            all_idea_in_database_list_format[i].append(temp_sentence_pos_list)
       
        return all_idea_in_database_list_format
    
    def highlight_text(self):
        """ perform an operation on the text within the white box like highlighting or performing some function"""
        self.text_box.tag_add('red_fg', '1.0', 'end')
        self.text_box.tag_configure("red_fg", foreground="blue")
        
     # ghost list
     #print(self.object_list)
     #for i,s in enumerate(self.object_list):
     #    print(i)
     #    print(s)
     #content=window.selection_get()  
    
      
  
    def bring_idea_tool_or_problem_to_a_center_box_to_work_with(self,event: str) -> str:
        """ bring one of the items in a list to a center box to better see and perform trnasofmrations on or connect to"""
        from ctypes import windll
        import pyautogui
        import time
        import pyperclip
        import copy
        import re 
        
        
        self.starting_time_idea=time.time()
        try: 
            content=window.selection_get()
            content= re.sub('\d+:','',content) 
            content=content[:-1]
            self.text_box2.insert(tk.END, content)
            windll.user32.EmptyClipboard()
            global stored_copy_object
            self.stored_copy_object=copy.deepcopy(content)
            self.carry_information_about_copied_text()
        except Exception as e:
            print(e)
        # space before word and a space after considers it part of word
        # different center boxes will have different purposes and differnet functions available to each of them and different things you can do to the text
    def carry_information_about_copied_text(self,table_name= "labels_for_idea_program_2"):
        #print(self.stored_copy_object)
        self.cur.execute(f"""SELECT * FROM {table_name} WHERE sentence = '{self.stored_copy_object}';""")
        specific_entry= self.cur.fetchall()
        self.object_list=""
        for first_entry in specific_entry: 
            self.object_list=list(first_entry)
            break
        return self.object_list   
    def export_idea_to_new_table(self,event):
        """ export data to different tables  """
        import re
        import time
        finish_time_idea=time.time()
        modified_text=self.text_box2.get('1.0', 'end')
        try:
            updated_label_grouped= re.search("(\d+);",modified_text)
            updated_label=updated_label_grouped.group(1)
            updated_text_grouped = re.search("(.*)(\d+);",modified_text)
            updated_sentence=updated_text_grouped.group(1) 
            print(updated_label)
            print(updated_sentence)
        except Exception as e:
            print(e) 
        
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
        self.start_problem_time=time.time()
        self.method_list_dictionary={}
        self.recorded_question_or_tool_for_method_list=[]
        self.objective_list_for_method=[]
        self.ideas_list_for_method=[]


        # for tecording whole time it took to make conenctions for game like envrionment
        #program_start_time# if 2 minutes has passed and text in the problem window then save as problem_object
        #DO THIS if problem_dictionary_already_exists then 
        #save it before starting a new one
        
        self.problem_recorded=self.text_box.get('1.0', 'end')
        self.problem_recorded=re.sub('\n',"",self.problem_recorded)
        print( self.problem_recorded)
        self.problem_recorded="?? "+ self.problem_recorded
        
        time_created =time.time()
        self.problem_list_dictionary={self.problem_recorded:[time_created]}
        print(self.problem_list_dictionary)
        # this is the thing that makes sure that we can add qualtities to the project
        self.current_object_or_problem=self.problem_recorded
        
        
 
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
        
    def show_steps_in_sub_method(self,event):
        """ when clicking 1 in submethod window will show the sub steps of a particualr sub-method"""
        #leaving thename of submethod at the top and rest of to copy if needed into the method or 
        # need to save sub-methods in special way in idea database to be able to do this

        
        # will need to save sub method in a particular way
    def revert_back_to_show_all_sub_methods(self,event):
        """ when clicked relist all the relevent sub-methods whether for conn window or method window"""
        

        
        
 
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
    
  
    def add_qualitites_expand_current_qualtity_or_problem_dictionary(self,event): 
        """ press certain key to add to the list of lists in the key of a dictionary with first 
        item being tool or question used and second being qualtity being assigned to the
        given problem or key object"""
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
        for objecttt in problem_entries:
            problem_question_or_task= objecttt[1]
            specific_problem_or_object= objecttt[2]
            objectt_string=f"{specific_problem_or_object};"
            qualitity_list = objecttt[4]
            if qualitity_list:
                qualitity_list=re.sub("\n","",qualitity_list)
                qualitity_list=re.sub("\\n","",qualitity_list)
                qualitity_list=re.split(",",qualitity_list[1:-1])
                for i6, qualities_of_entry in enumerate(qualitity_list):
                    if i6==0:
                        objectt_string+=f"{qualities_of_entry}"
                    else:
                        objectt_string+=f"={qualities_of_entry}"
                        
                self.listbox1.insert(tk.END, objectt_string) 
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
        for objecttt in problem_entries:
            problem_question_or_task= objecttt[1]
            specific_problem_or_object= objecttt[2]
            objectt_string=f"{specific_problem_or_object};"
            qualitity_list = objecttt[4]
            if qualitity_list:
                qualitity_list=re.sub("\n","",qualitity_list)
                qualitity_list=re.sub("\\n","",qualitity_list)
                qualitity_list=re.split(",",qualitity_list[1:-1])
                for i6, qualities_of_entry in enumerate(qualitity_list):
                    if i6==0:
                        objectt_string+=f"{qualities_of_entry}"
                    else:
                        objectt_string+=f"={qualities_of_entry}"
                        
                self.listbox1.insert(tk.END, objectt_string) 
    def  ghost_list(self, sql_list):
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

    def upload_past_problem_to_keep_expanding_network(self,event):
        """ query sql database for past problem and upload its conns to the program """
        import re
        self.method_list_dictionary={}
        self.recorded_question_or_tool_for_method_list=[]
        self.objective_list_for_method=[]
        self.ideas_list_for_method=[]
        problem_to_reupload=self.text_box.get('1.0', 'end')
        print(problem_to_reupload)
        problem_to_reupload_split=re.split("\n",problem_to_reupload)
        print(problem_to_reupload_split[0])
        self.problem_recorded=problem_to_reupload_split[0]
        self.cur.execute(f"""SELECT * FROM problem_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
        self.problem_list_dictionary={}
        problem_entries= self.cur.fetchall()
        print(problem_entries)
        self.current_object_or_problem=self.problem_recorded
        # start on root problem
        for numm, objectt1 in enumerate(problem_entries):
                if numm==0:
                    intital_time_for_object=objectt1[7]
                    self.problem_list_dictionary={self.problem_recorded:[intital_time_for_object]}
                    specfic_object=objectt1[2]
                    tool_or_question_used=objectt1[3]
                    qual_list=objectt1[4]
                    timme=objectt1[6]
                    timme=re.split(",",timme[1:-1])
                    qual_list=re.split(",",qual_list[1:-1])
                    tool_or_question_used=re.split(",",tool_or_question_used[1:-1])
                    for tooll,quall,timm in zip(tool_or_question_used,qual_list,timme):
                        self.problem_list_dictionary[specfic_object].append([tooll,quall,timm])
                    continue
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
        print(self.problem_list_dictionary)
        self.reupload_problem_to_view_in_listbox(self.problem_recorded)

    def switch_to_method_window(self,event):
        """ left click button to switch from connections window to building method window on selected problem"""
        def generate_problem_webb():
            """ create the nodes and edges for the problem web """
            import copy
            self.node_name_list=[]
            self.color_map=[]
            self.edge_map=[]
            self.node_number_list=[]
            color_levels_list=["#A0CBE2","yellow","orange","pink","red","#A0CBE2"]
            for key5,list_of_qualities in self.problem_list_dictionary.items():
                if len(key5)> 15:
                    key5=key5[:12]
                objecttt=key5
                if "?? " in objecttt:
                    problemmm=copy.deepcopy(objecttt)
                    self.node_name_list.append(problemmm)
                    self.color_map.append(color_levels_list[0])
                    for i9, quality1 in enumerate(list_of_qualities):     
                        if i9==0:
                            continue
                        qualitityy=quality1[1]
                        if len(qualitityy)> 15:
                            qualitityy=qualitityy[:12]
                        self.edge_map.append((problemmm,qualitityy))
                        self.node_name_list.append(qualitityy)
                        self.color_map.append(color_levels_list[1])
                    continue
                print('START')
                print(self.edge_map)
                print(self.node_name_list)
                print(self.color_map)
                if objecttt not in self.node_name_list:
                    self.node_name_list.append(objecttt)
                    self.color_map.append(color_levels_list[1])
                    self.edge_map.append((problemmm,objecttt))
                for i10, qualityy2 in enumerate(list_of_qualities):
                    if i10==0:
                        continue
                    qualitityy=qualityy2[1]
                    if len(qualitityy)> 15:
                        qualitityy=qualitityy[:12]   
                    self.edge_map.append((objecttt,qualitityy))
                    if qualitityy not in self.node_name_list:
                        self.node_name_list.append(qualitityy) 
                        root_index=self.node_name_list.index(objecttt)
                        root_color=self.color_map[root_index] 
                        current_color_index=color_levels_list.index(root_color)
                        self.color_map.append(color_levels_list[current_color_index+1]) 
                        continue
 
            self.node_number_list=list(range(len(self.node_name_list)))
        def change_names_of_textboxes():
            """ change names of all the boxes"""
            # store previous methods under submethods
            frames={self.frame2:12,self.frame4:10,self.frame5:5,self.frame7:9,self.frame3:15}# self.frame1:13  is connecte dobjectds
            for  frame, category in frames.items():
                for widget in frame.winfo_children():
                    widget.destroy()  
                if category ==15:
                    self.generate_side_lists_method_design(frame,category, title_of_text="Current Method Steps")
                    continue
                if category ==5:
                    self.generate_side_lists_method_design(frame,category, title_of_text="Objectives")
                    continue
                if category == 9:
                    self.generate_side_lists_method_design(frame,category, title_of_text="Sub-Methods")
                    continue
                else:
                    self.generate_side_lists_method_design(frame,category)
                    continue
        
        def generate_head_note_for_main_box():
            """erase center box widget but keep buttons in the correct position in the frame """
            button_list=[decrease,increase,decrease,decrease,decrease,decrease,decrease,decrease,decrease,decrease]
            text_list=["1:Conns-Design","2:Steps-Design","Web-Grab","Update-Databases","New-Problem","List-Past-Problems","List-Problems","Record_Problem"]
            for ii, button_type,textt in zip(range(9),button_list,text_list):
                self.button = tk.Button(master=self.frame6, text=textt, fg='white')
                #command=self.highlight_text,
                self.button.grid(row=0, column=ii, sticky="nsew")
                self.button.config(font=('Times New Roman',10),bg='green')
                if textt=="List-Past-Problems":
                    self.button.bind("<Button-1>",self.list_past_problems)
        
                if textt=="List-Problems":
                    self.button.bind("<Button-1>",self.list_possble_problems)
                    
                if textt=="Record_Problem":
                    self.button.bind("<Button-1>",self.record_problem_and_create_problem_dictionary)
                    
                if textt=="2:Steps-Design":
                    self.button.bind("<Button-1>",self.switch_to_method_window)

                
            
        change_names_of_textboxes()
        generate_problem_webb()
        generate_head_note_for_main_box()
        
        # need to find a way to use the problem web at one point
        #display_method_dicitonary_on_start_up_if_there_is_one() # and make a new one
        # want to add the rest here
    
    def record_question_or_tool_idea_used_for_method(self,event: str)-> str:
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
        # we always need to specfiy a method step
        #need to incorproate question or tool used here
        #self.recorded_question_or_tool_for_method_list
        def create_dict_or_modify():
            # this is currently not behaving correctly need to edit it and make changes this is the next problem
            """ update dictionary adding new step or  modifying existing step """
            import re
            import time
            import copy
            time_method_found =time.time()
            # number not behaving correctly got to fix this
            unwanted_terms_str = "/#=\]"
            self.delimiter_dicitonary_for_method= {"#":"placement", "=":"idea_web",  "]": "objective", "/":"tool_or_question" }
            self.placement_dictionary= {"placement":3,"idea_web":1,"objective":2,"tool_or_question":0}
            content=self.text_box1.get('1.0', 'end') # textbox1 is the method window
            self.previous_method_list_dictionary=copy.deepcopy(self.method_list_dictionary)
            if ";" in content: # new step
                objectt_and_qualities=re.split(';',content)
                step_name=objectt_and_qualities[0]
                self.method_list_dictionary[step_name]=[time_method_found]
                self.method_list_dictionary[step_name].append([[],[],[],0,[]]) # problem # 1 is there because it is the second entry in this steps list of lists
                self.current_step=step_name
                content=re.split(r"([/#=\]])",objectt_and_qualities[1])
            else:
                content=re.split(r"([/#=\]])",content)   
            stored_delimiter=""
            for qual3 in content:            
                if  "/#=]" in qual3:
                    stored_delimiter=qual3
                    continue
                else:
                    if stored_delimiter=="":
                        stored_delimiter="=" 
                    method_quality_type=self.delimiter_dicitonary_for_method[stored_delimiter]
                    location_in_dictionary_list_for_qual=self.placement_dictionary[method_quality_type]
                    if stored_delimiter=="#":
                        self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual]=qual3 
                    if stored_delimiter!="#":
                        if qual3 not in unwanted_terms_str:
                            self.method_list_dictionary[step_name][1][location_in_dictionary_list_for_qual].append(qual3) 

                            
            # add time
            self.method_list_dictionary[step_name][1][4].append(time_method_found)
            self.method_list_dictionary[step_name][1][0].extend(self.recorded_question_or_tool_for_method_list)
            self.method_list_dictionary[step_name][1][2].extend(self.objective_list_for_method)
            # need to deal with ideas web now to easily put ideas into a method step
            self.method_list_dictionary[step_name][1][1].extend(self.ideas_list_for_method)

            # this ensure we don't keep copying the same ideas and tools for each step we update
            self.recorded_question_or_tool_for_method_list=[]
            self.objective_list_for_method=[]
            self.ideas_list_for_method=[]
            print(self.method_list_dictionary)
            return self.method_list_dictionary
        
       
        def save_method_dictionary_to_database() :
            import re
            """ take the method list dictitonary and bring it to database for methods disassembling it and uploading it""" 
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
                        self.cur.execute( f""" UPDATE methods_table 
                                         Set question_or_tool_for_method= '{str(tool_or_question_list)}', ideas_from_web = '{str(idea_web_list)}',
                                         objectives_maxmized = '{str(objective_list)}', time_method_found = '{str(time_found_list)}'
                                         WHERE problem_being_solved = '{str(self.problem_recorded)}' and method_step = '{str(step_name)}';""")
                    else:
                        #print("5")
                        #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
                        # problem being solved
                        self.cur.execute( f""" INSERT INTO methods_table (problem_being_solved,method_step ,question_or_tool_for_method,ideas_from_web,objectives_maxmized,temporal_placement,time_method_found)
                                 VALUES ('{str(self.problem_recorded)}','{str(step_name)}','{str(tool_or_question_list)}','{str(idea_web_list)}','{str(objective_list)}','{str(placement_int)}','{str(time_found_list)}');""")
                    

                self.conn.commit()  

                
           
                
                    #self.placement_dictionary= {"placement":3,"idea_web":1,"objective":2,"tool_or_question":0}
    
        
        def reupload_method_dictionary():
            """ take the method list dictitonary and bring it back into the program  from sql database"""
            self.cur.execute(f"""SELECT * FROM methods_table WHERE problem_being_solved = '{self.problem_recorded}';""")
            self.listbox4.delete(0, tk.END)
            method_entries= self.cur.fetchall()
            # still need to remove  question marks
            
            # need to delete all previous entries
            #dicc={"id":"bigserial","problem_being_solved":"text", "method_step":"text", "question_or_tool_for_method":"text","ideas_from_web":"text","objectives_maxmized":"text","temporal_placement":"text" ,"time_method_found":"text"}
            for objecttt in method_entries:
                #id 0
                #problem 1
                # step name 2
                #tool 3
                #ideas 4
                # optimize 5
                # order 6
                #time 7
                print('hi')
                print(objecttt)
                problem_being_solved= objecttt[1]
                method_step= str(objecttt[2])
                temporal_placement = str(objecttt[6])
                self.method_step_str = temporal_placement + " "+method_step + "\n"
                self.listbox4.insert(tk.END, f"{self.method_step_str}") 
                

        
        create_dict_or_modify()
        save_method_dictionary_to_database()
        reupload_method_dictionary()

    # imagination step we need figure out how we are going to use methods
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
        import time
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
      
    
    def change_back_to_conn_window(self,event): # still need to tie this to
         """ save everything that has been written in the methods box and in the current methods dicitonary then go back to conn window"""
         # clear everything frome xisting window
         for w in window.winfo_children():
             w.destroy()
         #recreate existing window
         # work out kinks later
         for i in range(3):
             window.columnconfigure(i, weight=1, minsize=75)
             window.rowconfigure(i, weight=1, minsize=50)
             for j in range(0, 3):
                 # create a indivudal label for each 
                 if i==0 and j==0:# existing galaxies to draw on  # on left side all the way down
                     quad.frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     current_galaxies_connected_list=quad.import_tools_problems_or_existing_ideas(2)
                     quad.side_lists("Current Connected Objects",current_galaxies_connected_list,quad.frame1)
                     continue
                 if i==0 and j==1:
                     
                     quad.frame8 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     quad.main_problem_window()
                     continue
                 if i==0 and j ==2: # questions I need to ask to form connections
                     quad.frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     questions_list=quad.import_tools_problems_or_existing_ideas(4)
                     quad.side_lists("Questions",questions_list,quad.frame2)
                     continue
                 if i==1 and j==0:# existing galaxies to draw on  # on left side all the way down
                     quad.frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     existing_objects_in_database_list=quad.import_tools_problems_or_existing_ideas(7)
                     quad.side_lists("Possible Objects",existing_objects_in_database_list,quad.frame3)
                     
                     # will have to set function values somehow
                     continue
                 if i ==1 and j==1:
                     quad.frame6 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     quad.qualitites_boxes("Object and Qualities of Selected Object","Web Objects And Ideas",level=0)
                     continue
                 if i==1 and j ==2:
                     frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     quad.sub_method_box_1()   
                 if i ==2 and j==0:
                     quad.frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     tools_list=quad.import_tools_problems_or_existing_ideas(10)
                     quad.side_lists("Tools",tools_list,quad.frame4)
                     continue
                     
                 if i ==2 and j==1:
                     frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     quad.qualitites_boxes("Edit-or-Create-Sentences","Develop-Sub-Method",level=1 )
                     continue
                 if i==2 and j==2:
                     quad.frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                     objectives_list=quad.import_tools_problems_or_existing_ideas(14) # need to make this work
                     quad.side_lists("Web-Results",objectives_list,quad.frame5)
                     continue
class quadrants_of_program(buttons_per_quadrant):
    def __init__(self):
        import psycopg2

        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.background_label_color='grey'
        
    def side_lists(self, title_of_text,label_list,frame_name: str):
        """display a list of exisitng galaxies from database, this is the one on the sides of the screen """
        frame_name.grid(row=i, column=j, padx=0, pady=0)
        frame_name.configure(bg='light yellow')
        
        label = tk.Label(master=frame_name,text=title_of_text, fg="black", bg=self.background_label_color)
        label.grid(row=0, columnspan=3)
        label.config(font=('Times New Roman',8),bg='light yellow')
        if title_of_text != "Current Connected Objects":
            listbox = tk.Listbox(frame_name,width=60) 
        if title_of_text== "Current Connected Objects":
            self.listbox1 = tk.Listbox(frame_name,width=60) 
            listbox=self.listbox1
            self.listbox1.bind("4",self.switch_to_previous_galaxy)
        listbox.grid(row=1,column=0, columnspan=3)
        listbox.bind('1', self.bring_idea_tool_or_problem_to_a_center_box_to_work_with)
        listbox.bind("2",self.record_question_or_tool_used)
        listbox.bind('3',self.transport_object_from_object_window)
        #<Double-Button-1>
        for i2, idea in enumerate(label_list): 
            #ideaa = idea.strip('\'')
            #.join(map(str, ini_list))))
            ideaa=idea[2:-2]
            listbox.insert(tk.END, f"{i2}:{ideaa}")   
        entry=tk.Entry(master=frame_name)
        entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
        button_list=[decrease,increase,decrease]
        text_list=["1:Update-text","Form-Conn","Swap-Conn"]
        for ii, button_type,textt in zip(range(4),button_list,text_list):
            update_galaxies = tk.Button(master=frame_name, text=textt)
            update_galaxies.config(bg='orange')
            update_galaxies.grid(row=3, column=ii, sticky="nsew")
            update_galaxies.bind("<Button-1>", self.handle_click)
            
    def generate_side_lists_method_design(self, frame_name,category,title_of_text=""):
        #list_of_text_titles=["Current Connected Objects","Questions","Possible Objects","Tools","Web-Results"]
        label_list=self.import_tools_problems_or_existing_ideas(category)
        # need to fix category names
        label = tk.Label(master=frame_name,text=title_of_text, fg="black", bg=self.background_label_color)
        label.grid(row=0, columnspan=3)
        label.config(font=('Times New Roman',8),bg='light yellow')
        if title_of_text == "Current Method Steps":
            print("title_of_text")
            self.listbox4 = tk.Listbox(frame_name,width=60)
            self.listbox4.grid(row=1,column=0, columnspan=3)
            self.listbox4.bind('3',self.transport_to_method_window)
            self.listbox4.bind("4",self.switch_to_previous_galaxy)
            entry=tk.Entry(master=frame_name)
            entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 
            button_list=[decrease,increase,decrease]
            text_list=["1:Update-text","Form-Conn","Swap-Conn"]
            for ii, button_type,textt in zip(range(4),button_list,text_list):
                update_galaxies = tk.Button(master=frame_name, text=textt)
                update_galaxies.config(bg='orange')
                update_galaxies.grid(row=3, column=ii, sticky="nsew")
                update_galaxies.bind("<Button-1>", self.handle_click)  
            return "finished"
        if title_of_text== "Objectives":
            print('objective reached')
            self.listbox5 = tk.Listbox(frame_name,width=60)
            self.listbox5.grid(row=1,column=0, columnspan=3)
            # 2 will need to be different key to add to objectives list
            self.listbox5.bind("2", self.record_objective_used_for_method)
            self.listbox5.bind('3',self.transport_to_method_window)
            self.listbox5.bind("4",self.switch_to_previous_galaxy)
            for i in range(10):
                dog='woo'
                self.listbox5.insert(tk.END,f'{dog}')
        else:
            if category ==12:
                title_of_text="Questions"    
            if category == 10:
                title_of_text="Tools"
            listbox = tk.Listbox(frame_name,width=60) 
            listbox.grid(row=1,column=0, columnspan=3)
            listbox.bind('1', self.transport_to_idea_editing_window_method)
            listbox.bind("2",self.record_question_or_tool_idea_used_for_method)
            listbox.bind('3',self.transport_to_method_window)
            for i2, idea in enumerate(label_list): 
                ideaa=idea[2:-2]
                listbox.insert(tk.END, f"{i2}:{ideaa}") 
        entry=tk.Entry(master=frame_name)
        entry.grid(row=2, column=0,columnspan=3, sticky="nsew") 

        button_list=[decrease,increase,decrease]
        text_list=["1:Update-text","Form-Conn","Swap-Conn"]
        for ii, button_type,textt in zip(range(4),button_list,text_list):
            update_galaxies = tk.Button(master=frame_name, text=textt)
            update_galaxies.config(bg='orange')
            update_galaxies.grid(row=3, column=ii, sticky="nsew")
            update_galaxies.bind("<Button-1>", self.handle_click)  
    def main_problem_window(self):
        """ """
        self.frame8.grid(row=i, column=j, padx=5, pady=5)
        self.frame8.config(bg="white")
        button_list=[decrease,increase,decrease,decrease,decrease,decrease,decrease,decrease,decrease,decrease]
        text_list=["1:Conns-Design","2:Steps-Design","Web-Grab","Update-Databases","New-Problem","List-Past-Problems","List-Problems","Record_Problem"]
        for ii, button_type,textt in zip(range(9),button_list,text_list):
            button = tk.Button(master= self.frame8, text=textt, fg='white')
            #command=self.highlight_text,
            button.grid(row=0, column=ii, sticky="nsew")
            button.config(font=('Times New Roman',10),bg='green')
            if textt=="List-Past-Problems":
                button.bind("<Button-1>",self.list_past_problems)
            if textt=="List-Problems":
                button.bind("<Button-1>",self.list_possble_problems)
            if textt=="Record_Problem":
                button.bind("<Button-1>",self.record_problem_and_create_problem_dictionary)
            if textt=="2:Steps-Design":
                button.bind("<Button-1>",self.switch_to_method_window)
        self.text_box = tk.Text(master=self.frame8,width=100)
        self.text_box.grid(row=1, columnspan = 9)  
        self.text_box.bind(';',self.import_problem)
        self.text_box.bind('-',self.upload_past_problem_to_keep_expanding_network)
        #self.text_box.bind('2',self.text_box.tag_add( background= "black", foreground= "white") )
    def qualitites_boxes(self, text_box_1_title,text_box_2_title,level=0):
        if level==0:
            self.frame6.grid(row=i, column=j, padx=5, pady=5)
            self.frame6.config(bg='light blue')
            self.label1 = tk.Label(master=self.frame6,text=text_box_1_title,fg="white",bg=self.background_label_color)
            self.label1.grid(row=0,column=0)
            self.label1.config(font=('Times New Roman',8),bg='light blue')
            self.label2 = tk.Label(master=self.frame6,text=text_box_2_title,fg="white",bg=self.background_label_color)
            self.label2.grid(row=0,column=1)
            self.label2.config(font=('Times New Roman',8),bg='light blue')
            self.text_box0 = tk.Text(self.frame6,width=50)
            self.text_box0.grid(row=1,column=0)
            #self.text_box0.bind("-",self.export_object_to_new_table)   
            self.text_box0.bind("-",self.add_qualitites_expand_current_qualtity_or_problem_dictionary)
            self.text_box01 = tk.Text(self.frame6,width=50)
            self.text_box01.grid(row=1,column=1)    
        else:
            frame.grid(row=i, column=j, padx=5, pady=5)
            frame.config(bg='light blue')
            label1 = tk.Label(master=frame,text=text_box_1_title,fg="white",bg=self.background_label_color)
            label1.grid(row=0,column=0)
            label1.config(font=('Times New Roman',8),bg='light blue')
            label2 = tk.Label(master=frame,text=text_box_2_title,fg="white",bg=self.background_label_color)
            label2.grid(row=0,column=1)
            label2.config(font=('Times New Roman',8),bg='light blue')
            self.text_box1 = tk.Text(frame,width=50)
            self.text_box1.grid(row=1,column=0)
            self.text_box1.bind("-",self.add_step_or_modify)
            #self.text_box1.bind('-',self.export_idea_to_new_table)
            self.text_box2 = tk.Text(frame,width=50)
            self.text_box2.grid(row=1,column=1)
            self.text_box2.bind('-',self.export_idea_to_new_table)

            

        #btn_increase = tk.Button(master=frame, text="+", command=increase)

        #btn_increase.grid(row=1, column=2, sticky="nsew")

    def sub_method_box_1(self,frame): 
        """ will outline sub-method of questioning to perform, this is the one on the middle right of the screen"""
        frame.grid(row=i, column=j, padx=5, pady=5)
        frame.config(bg='red')

        label1 = tk.Label(master=frame,text="Sub-Methods",fg="white",bg="red")
        label1.grid(row=0)
        label1.config(font=('Times New Roman',8))

        #frame.grid(row=i, column=j, padx=5, pady=5)
        entry=tk.Entry(master=frame)
        entry.grid(row=1, sticky="nsew") 
        #column=0,columnspan=3
        
        button_list=[decrease,increase,decrease,decrease]
        text_list=["conn","update","import",""]
        #for ii, button_type,textt in zip(range(4),button_list,text_list):
        #    btn_decrease = tk.Button(master=frame, text=textt, command=button_type)
        #    btn_decrease.grid(row=1, column=ii, sticky="nsew")
        #    btn_decrease.config(font=('Times New Roman',10), bg="red")
 
        self.listboxsub_method = tk.Listbox(frame,width=60,background='white',height=10) 
        self.listboxsub_method.grid(row=2)#column=0, columnspan=4
        self.listboxsub_method.bind('1',self.show_steps_in_sub_method)

        label_listt=self.import_tools_problems_or_existing_ideas(8)
        for values in label_listt: 
            self.listboxsub_method.insert(tk.END, values) 
if __name__ == "__main__":
    quad = quadrants_of_program()
    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
        for j in range(0, 3):
            # create a indivudal label for each 
            if i==0 and j==0:# existing galaxies to draw on  # on left side all the way down
                quad.frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                current_galaxies_connected_list=quad.import_tools_problems_or_existing_ideas(2)
                quad.side_lists("Current Connected Objects",current_galaxies_connected_list,quad.frame1)
                continue
            if i==0 and j==1:
                quad.frame8 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                quad.main_problem_window()
                continue
            if i==0 and j ==2: # questions I need to ask to form connections
                quad.frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                questions_list=quad.import_tools_problems_or_existing_ideas(4)
                quad.side_lists("Questions",questions_list,quad.frame2)
                continue
            if i==1 and j==0:# existing galaxies to draw on  # on left side all the way down
                quad.frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                existing_objects_in_database_list=quad.import_tools_problems_or_existing_ideas(7)
                quad.side_lists("Possible Objects",existing_objects_in_database_list,quad.frame3)
                # will have to set function values somehow
                continue
            if i ==1 and j==1:
                quad.frame6 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                quad.qualitites_boxes("Object and Qualities of Selected Object","Web Objects And Ideas",level=0)
                continue
            if i==1 and j ==2:
                quad.frame7 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                quad.sub_method_box_1(quad.frame7)   
            if i ==2 and j==0:
                quad.frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                tools_list=quad.import_tools_problems_or_existing_ideas(10)
                quad.side_lists("Tools",tools_list,quad.frame4)
                continue
            if i ==2 and j==1:
                frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                quad.qualitites_boxes("Edit-or-Create-Sentences","Develop-Sub-Method",level=1 )
                continue
            if i==2 and j==2:
                quad.frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                objectives_list=quad.import_tools_problems_or_existing_ideas(14) # need to make this work
                quad.side_lists("Web-Results",objectives_list,quad.frame5)
                continue
            #if i == 2 and j ==2:
                # replacing this method now
            #frame.grid(row=i, column=j, padx=5, pady=5)
            #label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            #label.pack(padx=5, pady=5)
    window.mainloop()
    
