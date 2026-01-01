# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 04:21:20 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
# merge these into one app can access glossary elements and lines of code when you search using 
# single search bar
# so it will have both gollsary info and  all function info from code base asscoaited with glossary
#CREATE TKINYER button SUCH THAT YOU RECORD problem tree action that have used a past function
# when searching so that you can easily when you have a simialr action you need
# to take will pull up this function first
import tkinter as tk
import customtkinter
import sys
import re
import time
import psycopg2
from multiprocessing import Process
sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\labeling_code_and_creating_glossary  a1.1.1')
sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\save_all_code_in_sql_table a 1.1.1.1')
from save_all_code_in_sql_table_functions import save_all_code_in_sql_table_functions
from save_all_code_in_sql_table_functions import save_all_code_in_sql_table_functions_child
from labeling_code_and_creating_glossary_functions import labeling_code_and_creating_glossary_function
from labeling_code_and_creating_glossary_functions import labeling_code_and_creating_glossary_function_child
class tkinter_gui_glossary_master_code_functions(labeling_code_and_creating_glossary_function_child,save_all_code_in_sql_table_functions_child):
    """THIS WILL ALLOW US TO ACCESS GLOSSARY FOR ALL FUNCTIONS AND LINES OF CODE
    AND IT WILL ALLOW US TO ACCESS FUNCTIONS FROM OUR CODE BASE AND MAYBE OTHER RELATIONSHIPS
    STORED IN TWO SEPERATE TABLES"""# use context from glossary to find functions you need BRILLIANT
    # then maybe cutback if you need to 
    def __init__(self):
        """ """
        self.sql_switch=0
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor() 
    def init_gui_window(self):
        """create main tkinyer window """
        self.window = tk.Tk()
        self.window.state('zoomed')
        self.window.title('Coding Program')
        self.window.columnconfigure(0, weight=1, minsize=75)
        self.window.rowconfigure(0, weight=1, minsize=50)
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width_characters=self.screen_width*0.125
        self.screen_height_characters=self.screen_height*0.125
        print(f"self.screen_width_characters: {self.screen_width_characters}")
        print(f"self.screen_height_characters: {self.screen_height_characters}")
        print(f"self.screen_width: {self.screen_width}")
        print(f"self.screen_height: {self.screen_height}")

        ## in characters
        #1 pixel = 0.125 character
    def init_scroll_bar(self):
         """ add in scroll bar"""
         self.scrollbar = tk.Scrollbar(self.main_frame4,orient='vertical')
         self.scrollbar.grid(column=1,row=0,rowspan=2)#row=1,column=0, columnspan=3 #column=5,row=0,rowspan=4
         self.scrollbar.config(command=self.yview)
         # still need to make this full size of box
         #listbox.config(yscrollcommand = self.scrollbar.set)  
    def init_frames(self,bg_color="pink"):
        """ add frames to application"""
        self.main_frame0 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame0.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
     
        self.main_frame1 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame1.grid(row=0,column=1)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame2 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, bg=bg_color)
        self.main_frame2.grid(row=0,column=2)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame3 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame3.grid(row=0,column=3)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame4 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame4.grid(row=0,column=4)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame5 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame5.grid(row=0,column=5)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame6 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame6.grid(row=1,column=0)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame7 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame7.grid(row=1,column=1)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame8 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame8.grid(row=1,column=2)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame9= tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame9.grid(row=1,column=3)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame10 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame10.grid(row=1,column=4)#column=0, columnspan=4 #row=2,columnspan=2
        
        self.main_frame11 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame11.grid(row=1,column=5)#column=0, columnspan=4 #row=2,columnspan=2
        
       
    def init_list_boxs(self,font_size=10,font_type='Microsoft YaHei'):
        """ add listboxs to application"""
        font_type_and_size= (font_type,font_size)
        self.listbox_width=int(round(int(self.screen_width_characters)/6))# the six is for 6 listboxs
        self.listbox_width=int(round(self.listbox_width))
        self.listbox_height=int(round(self.screen_height_characters/3))# may need to change htis /2
        self.listbox_height=int(round(self.listbox_height/2))
        
        self.listboxxy0 = tk.Listbox(self.main_frame0,width=self.listbox_width,height=int(round(self.listbox_height/2))) 
        self.listboxxy0.config(yscrollcommand=self.yscroll1,font=font_type_and_size)  
        self.listboxxy0.grid(row=7,column=0)#row=1,column=0, columnspan=3

       
        self.listboxxy1 = tk.Listbox(self.main_frame1,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy1.config(yscrollcommand=self.yscroll1,font=font_type_and_size)  
        self.listboxxy1.grid(row=3,column=0)#row=1,column=0, columnspan=3
        
        self.listboxxy2 = tk.Listbox(self.main_frame2,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy2.config(yscrollcommand=self.yscroll2,font=font_type_and_size) # make this slightly larger
        self.listboxxy2.grid(row=3,column=0)#row=1,column=0, columnspan=3
        
        self.listboxxy3 = tk.Listbox(self.main_frame3,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy3.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy3.config(yscrollcommand=self.yscroll3,font=font_type_and_size) 
        
        self.listboxxy4 = tk.Listbox(self.main_frame4,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy4.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy4.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        self.listboxxy5 = tk.Listbox(self.main_frame5,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy5.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy5.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        self.listboxxy6 = tk.Listbox(self.main_frame6,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy6.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy6.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        self.listboxxy7 = tk.Listbox(self.main_frame7,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy7.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy7.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        self.listboxxy8 = tk.Listbox(self.main_frame8,width=self.listbox_width,height=int(round(self.listbox_height/2))) 
        self.listboxxy8.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy8.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        self.listboxxy81 = tk.Listbox(self.main_frame8,width=self.listbox_width,height=int(round(self.listbox_height/2))) 
        self.listboxxy81.grid(row=4,column=0)#row=1,column=0, columnspan=3
        self.listboxxy81.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        
        
        self.listboxxy9 = tk.Listbox(self.main_frame9,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy9.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy9.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
       
        self.listboxxy10 = tk.Listbox(self.main_frame10,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy10.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy10.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 
        
        self.listboxxy11 = tk.Listbox(self.main_frame11,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy11.grid(row=3,column=0)#row=1,column=0, columnspan=3
        self.listboxxy11.config(yscrollcommand=self.yscroll4,font=font_type_and_size)
        
      

    def init_search_bars(self):
        """add search bar to application """
        self.entry_0=tk.Entry(master=self.main_frame0)
        self.entry_0.grid(row=3,columnspan=1, sticky="nsew") 
        
        self.entry_01=tk.Entry(master=self.main_frame0)
        self.entry_01.grid(row=4,columnspan=1, sticky="nsew")
        
        self.entry_02=tk.Entry(master=self.main_frame0)
        self.entry_02.grid(row=5,columnspan=1, sticky="nsew")
        
        self.entry_03=tk.Entry(master=self.main_frame0)
        self.entry_03.grid(row=6,columnspan=1, sticky="nsew")
        
       
        
        self.entry_1=tk.Entry(master=self.main_frame1)
        self.entry_1.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_2=tk.Entry(master=self.main_frame2)
        self.entry_2.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_3=tk.Entry(master=self.main_frame3)
        self.entry_3.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_4=tk.Entry(master=self.main_frame4)
        self.entry_4.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_5=tk.Entry(master=self.main_frame5)
        self.entry_5.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_6=tk.Entry(master=self.main_frame6)
        self.entry_6.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_7=tk.Entry(master=self.main_frame7)
        self.entry_7.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_8=tk.Entry(master=self.main_frame8)
        self.entry_8.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_9=tk.Entry(master=self.main_frame9)
        self.entry_9.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_10=tk.Entry(master=self.main_frame10)
        self.entry_10.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_11=tk.Entry(master=self.main_frame11)
        self.entry_11.grid(row=2,columnspan=1, sticky="nsew") 
        
       
        
        #self.entry_2=tk.Entry(master=self.main_frame2)
        #self.entry_2.grid(row=2,columnspan=1, sticky="nsew") 
    def init_labels(self):
        """ add labels to application"""
        label = tk.Label(master=self.main_frame0,text="Automate Commands", fg="black", bg="blue")
        
        label.grid(row=0,column=0)
        label.config(font=('Times New Roman',10),bg='white')
        
        label = tk.Label(master=self.main_frame1,text="Functions", fg="black", bg="blue")
        label.grid(row=0,column=0)
        label.config(font=('Times New Roman',10),bg='white')
        
        label = tk.Label(master=self.main_frame2,text="Code Lines", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white') 
        
        label = tk.Label(master=self.main_frame3,text="Glossary", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame4,text="File Name", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame5,text="Similar previous Coding Problem projects", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame6,text="Pypi Packages", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame7,text="PyPi Code Lines", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame8,text="Gen AI", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame9,text="Coding assistant", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame10,text="Github Search", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
        label = tk.Label(master=self.main_frame11,text="Problem Solving Program", fg="black", bg="blue")
        label.grid(row=0)
        label.config(font=('Times New Roman',10),bg='white')  
        
       

    def init_buttons(self):
        """add buttons to application """
        self.button_0 = customtkinter.CTkButton(master=self.main_frame0, text="swap out listbox",text_color='white')
        self.button_0.grid(row=1, column=0, sticky="nsew")
        
        
        self.button_1 = customtkinter.CTkButton(master=self.main_frame1, text="line_of_code_search_sort_and_upload",text_color='white')
        self.button_1.grid(row=1, column=0, sticky="nsew")
        
        self.button_2 = customtkinter.CTkButton(master=self.main_frame2, text="glossary_search",text_color='white')
        self.button_2.grid(row=1, column=0, sticky="nsew")
        
        self.button_3 = customtkinter.CTkButton(master=self.main_frame3, text="update_code_base",text_color='white')
        self.button_3.grid(row=1, column=0, sticky="nsew")
        
        self.button_4 = customtkinter.CTkButton(master=self.main_frame4, text="pyautogui_button",text_color='white')
        self.button_4.grid(row=1, column=0, sticky="nsew")
        
        self.button_5 = customtkinter.CTkButton(master=self.main_frame5, text="pyautogui_button",text_color='white')
        self.button_5.grid(row=1, column=0, sticky="nsew")
        
        self.button_6 = customtkinter.CTkButton(master=self.main_frame6, text="pyautogui_button",text_color='white')
        self.button_6.grid(row=1, column=0, sticky="nsew")
        
        self.button_7 = customtkinter.CTkButton(master=self.main_frame7, text="pyautogui_button",text_color='white')
        self.button_7.grid(row=1, column=0, sticky="nsew")
        
        self.button_8 = customtkinter.CTkButton(master=self.main_frame8, text="pyautogui_button",text_color='white')
        self.button_8.grid(row=1, column=0, sticky="nsew")
        
        self.button_9 = customtkinter.CTkButton(master=self.main_frame9, text="pyautogui_button",text_color='white')
        self.button_9.grid(row=1, column=0, sticky="nsew")
        
        self.button_10 = customtkinter.CTkButton(master=self.main_frame10, text="pyautogui_button",text_color='white')
        self.button_10.grid(row=1, column=0, sticky="nsew")
        
        self.button_11 = customtkinter.CTkButton(master=self.main_frame11, text="pyautogui_button",text_color='white')
        self.button_11.grid(row=1, column=0, sticky="nsew")
        
       
        
        
        
        
    
      
        
        
    def bind_functions_list_boxs(self):
        """add buttons functions to listboxs """
        self.listboxxy3.bind('1', self.view_glossary_websites)
        self.listboxxy4.bind('1', self.open_python_file_in_idle)
        
        self.listboxxy1.bind('2', self.import_function_to_use_in_building_file)

        
        
        # open up a window with values for database
        # expand on glossary defintions open new window
    def bind_functions_buttons(self):
         """add button functions to buttons """
         self.button_1.bind("<Button-1>", self.line_of_code_search_sort_and_upload)
         self.button_2.bind("<Button-1>", self.glossary_search_sort_and_upload)
         self.button_3.bind("<Button-1>", self.update_code_base)
    def bind_functions_search_bars(self):
         """add button functions to search bars """
         self.entry_1.bind('<Return>', self.code_base_function_search_sort_and_upload)
         self.entry_0.bind('<Return>', self.execute_building_project_command)

         #self.entry_2.bind('1', self.show_problemss) 
         # glossary data
    ### UPLOAD SQL DATA and create search function
    
    def yscroll0(self, *args):
        if self.listboxxy1.yview() != self.listboxxy0.yview():
            self.listboxxy1.yview_moveto(args[0])
        self.scrollbar.set(*args)
    def yscroll1(self, *args):
        if self.listboxxy1.yview() != self.listboxxy0.yview():
            self.listboxxy1.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll2(self, *args):
        if self.listboxxy2.yview() != self.listboxxy1.yview():
            self.listboxxy2.yview_moveto(args[0])
        self.scrollbar.set(*args)
    def yscroll3(self, *args):
        if self.listboxxy3.yview() != self.listboxxy2.yview():
            self.listboxxy3.yview_moveto(args[0])
        self.scrollbar.set(*args)
        
    def yscroll4(self, *args):
        if self.listboxxy4.yview() != self.listboxxy3.yview():
            self.listboxxy4.yview_moveto(args[0])
        self.scrollbar.set(*args)
    def yview(self, *args):
        self.listboxxy0.yview(*args)
        self.listboxxy1.yview(*args)
        self.listboxxy2.yview(*args)
        self.listboxxy3.yview(*args)
        self.listboxxy4.yview(*args)
    def upload_sql_values(self, table_name="code_base",column_list=None):
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
         print(column_str)
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
    def remove_duplicates_for_search_data_dic(self):
         """ deal with the fact that there are five of each line of code because of glossary """
         search_data_dic_temp={"glossary_definiton":[],"code_base_function":[],"line_of_code":[],"glossary_website":[],"code_file_name":[] }
         #column_list=["glossary_definiton","code_base_function","line_of_code","glossary_website"]
         used_code_list=[]
         counterr=0
         for i, line_of_code in enumerate(self.search_data_dic["line_of_code"]):
             if line_of_code in used_code_list:
                 continue
             else:
                 search_data_dic_temp["glossary_definiton"].append(f"{counterr}::: {self.search_data_dic['glossary_definiton'][i]}")
                 search_data_dic_temp["code_base_function"].append(self.search_data_dic["code_base_function"][i])
                 search_data_dic_temp["line_of_code"].append(self.search_data_dic['line_of_code'][i])
                 search_data_dic_temp["glossary_website"].append(self.search_data_dic["glossary_website"][i])
                 search_data_dic_temp["code_file_name"].append(self.search_data_dic["code_file_name"][i])   
                 counterr+=1

                 used_code_list.append(line_of_code)
         self.search_data_dic=search_data_dic_temp        
         # this will make search much faster
         return search_data_dic_temp
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
    def add_data_to_listbox(self,list_box_object,sorted_line_code_match_list,unsorted_data_list):
          """ """
          list_box_object.delete(0, tk.END)
          for average_match_for_line_of_code_line_of_code_placement_in_list in sorted_line_code_match_list:
              #print(average_match_for_line_of_code_line_of_code_placement_in_list)
              average_match_for_line_of_code=average_match_for_line_of_code_line_of_code_placement_in_list[0]
              line_of_code_placement_in_list=average_match_for_line_of_code_line_of_code_placement_in_list[1]
              data_value=unsorted_data_list[line_of_code_placement_in_list]
              #print(data_value)
              list_box_object.insert(tk.END, data_value)
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
    def line_of_code_search_sort_and_upload(self,event):
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
         for line_of_code_placement_in_list, line_of_code in enumerate(line_of_code_list):
             #print(f"line_of_code:{line_of_code}")
             self.used_prompt_letters=[]
             final_line_of_code_match_list=[]
             line_of_code_characters=self.create_characters(line_of_code)
             for prompt_letter_list_value, prompt_letter in enumerate(self.prompt_characters):
                 prompt_single_letter_match_list=[]
                 prompt_single_letter_match_list=self.prompt_letter_comparison_to_line_of_code_character(prompt_letter,prompt_letter_list_value,line_of_code_characters)
                 if prompt_single_letter_match_list=="used_letter":
                     print("used_letter")
                     continue
                 if prompt_single_letter_match_list:
                     final_line_of_code_match_list=self.weigh_character_match_list(prompt_single_letter_match_list,final_line_of_code_match_list)
             if final_line_of_code_match_list:
                 average_match_for_line_of_code=self.create_average_match_line(final_line_of_code_match_list)
                 line_of_code_value_dic[line_of_code]=[average_match_for_line_of_code,line_of_code_placement_in_list] 
              #PART 2: sort 
         print(f"line_of_code_value_dic: {line_of_code_value_dic}")

         sorted_line_code_match_list=self.line_of_code_sort(line_of_code_value_dic)
         #PART 3: upload
         print(f"sorted_line_code_match_list: {sorted_line_code_match_list}")
         
         self.add_data_to_listbox(self.listboxxy1,sorted_line_code_match_list,code_base_function_list)
         self.add_data_to_listbox(self.listboxxy2, sorted_line_code_match_list,line_of_code_list)
         self.add_data_to_listbox(self.listboxxy3,sorted_line_code_match_list,glossary_definiton_list)
         self.add_data_to_listbox(self.listboxxy4,sorted_line_code_match_list,code_base_file_name_list)
   #### view_glossary_website_button MAKE THIS AFTER GLOSSARY SEARCH
   
   
   
    def init_glossary_window(self):
       """create main tkinyer window """
       self.window_websites = tk.Tk()
       self.window_websites.config(bg="white")
       self.window_websites.title('Glossary-Info')
       #self.window_websites.state('zoomed') 
       self.window_websites.columnconfigure(0, weight=1, minsize=75)
       self.window.rowconfigure(0, weight=1, minsize=50) 
       self.screen_width2 = self.window.winfo_screenwidth()
       self.screen_height2 = self.window.winfo_screenheight()
       self.screen_width_characters2=self.screen_width2*0.125
       self.screen_height_characters2=self.screen_height2*0.125
    def init_tab_scroll_bar(self):
        """ add in scroll bar"""
        self.scrollbar = tk.Scrollbar(self.main_frame2_websites,orient='vertical')
        self.scrollbar.grid()#row=1,column=0, columnspan=3 #column=5,row=0,rowspan=4
        #self.scrollbar.config(command=self.)
        # still need to make this full size of box
        #listbox.config(yscrollcommand = self.scrollbar.set)  
    def yview_2(self):
        """ """
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0))
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
            
            
   
        
        
    def init_glossary_frames(self,bg_color="pink"):
       """ add frames to application"""
       #self.main_frame0_websites = tk.Frame(master=self.window_websites, relief=tk.RAISED,bg=bg_color)
       #self.main_frame0_websites.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
       #self.main_frame1_websites = tk.Frame(master=self.window_websites, relief=tk.RAISED, borderwidth=1,bg=bg_color)
       #self.main_frame1_websites.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
       frame_size=int(round(self.screen_width_characters2/4))
       
    
       self.main_frame1_websites = tk.Frame(master=self.window_websites, relief=tk.RAISED, borderwidth=1,bg=bg_color)
       self.main_frame1_websites.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
       
       self.main_frame2_websites = tk.Frame(master=self.window_websites, relief=tk.RAISED, borderwidth=1,bg=bg_color)
       self.main_frame2_websites.grid(row=0,column=1)#column=0, columnspan=4 #row=2,columnspan=2
      
       self.main_frame3_websites = tk.Frame(master=self.window_websites, relief=tk.RAISED, borderwidth=1,bg=bg_color)
       self.main_frame3_websites.grid(row=0,column=2)#column=0, columnspan=4 #row=2,columnspan=2
       
       #self.main_frame4_websites = tk.Frame(master=self.window_websites, relief=tk.RAISED, borderwidth=1,bg=bg_color)
       #self.main_frame4_websites.grid(row=0,column=3)#column=0, columnspan=4 #row=2,columnspan=2
    def init_text_box(self,font_size=10,font_type='Microsoft YaHei'):
         """ """
         font_type_and_size= (font_type,font_size)
         self.text_box1 = tk.Text(self.main_frame1_websites,bd=0,height=self.listbox_height,width=30)#width=100
         self.text_box1.config(font=font_type_and_size)
         self.text_box1.grid(row=1,column=0)  #columnspan = 9#row=iterator
         #self.text_box.config(state="disabled",font=font_type_and_size)
         self.text_box2 = tk.Text(self.main_frame2_websites,bd=0,height=self.listbox_height)#width=100
         self.text_box2.config(font=font_type_and_size)
         self.text_box2.grid(row=1,column=0)  #columnspan = 9#row=iterator
         
         
   

        
    def generate_button_list_widget(self,text):
         """ """
         #  create this like a tab in google chrome which points to
         #append them to the frame
         #  keep them a specific size
         # use scroll bar to view them all
         self.scrollbar = tk.Scrollbar(self.window_websites,orient='vertical')
         self.scrollbar.grid()#row=1,column=0, columnspan=3 #column=5,row=0,rowspan=4
         self.scrollbar.config(command=self.yview)
         #return list_of_button_widgets
         
         


    def init_glossary_list_boxs(self,font_size=10,font_type='Microsoft YaHei'):
       """ add listboxs to application"""
       # how do we deal with very long strings so we can view them
       # for list of actions and really long strategies
       # and for glossary definitions
       # apply this solution for strats and action lists in selected method
       #alternative widget to listbox
       # what would this look like
       # create a 
       #text.config(state=DISABLED)
       # create a for loop of text widgets?
       # we will create a list of text boxes with disabled
       # which have a scroll bar attached to them
       # we can apply this same solution to tabs
       # creating a button and adding it to the list when a new tab is open
       
       
       font_type_and_size= (font_type,font_size)
       self.listbox_width=int(round(int(self.screen_width_characters)/3))
       self.listbox_height=int(round(self.screen_height_characters/3))
       #self.listboxxy0_websites = tk.Listbox(self.main_frame0_websites) 
       #self.listboxxy0_websites.config(font=font_type_and_size) #yscrollcommand=self.yscroll0, 
       #self.listboxxy0_websites.grid(row=1,column=0)#row=1,column=0, columnspan=3
      # 
       #self.listboxxy1_websites = tk.Listbox(self.main_frame1_websites,height=self.listbox_height) 
       #self.listboxxy1_websites.config(font=font_type_and_size)  
       #self.listboxxy1_websites.grid(row=1,column=0)#row=1,column=0, columnspan=3
       
       #self.listboxxy2_websites = tk.Listbox(self.main_frame2_websites,width=int(round(self.screen_width_characters/3.5))) 
       #self.listboxxy2_websites.config(yscrollcommand=self.yscroll2,font=font_type_and_size) # make this slightly larger
       #self.listboxxy2_websites.grid(row=1,column=0)#row=1,column=0, columnspan=3
       
       self.listboxxy3_websites = tk.Listbox(self.main_frame3_websites,width=self.listbox_width,height=self.listbox_height) 
       self.listboxxy3_websites.grid(row=1,column=0)#row=1,column=0, columnspan=3
       self.listboxxy3_websites.config(yscrollcommand=self.yscroll3,font=font_type_and_size) 
       
       #self.listboxxy4_websites = tk.Listbox(self.main_frame4_websites,height=self.listbox_height) 
       #self.listboxxy4_websites.grid(row=1,column=0)#row=1,column=0, columnspan=3
       #elf.listboxxy4_websites.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 

    def init_glosary_search_bars(self):
       """add search bar to application """
       
       
       self.entry_2_websites=tk.Entry(master=self.main_frame2)
       self.entry_2_websites.grid(row=2,columnspan=1, sticky="nsew") 
       #self.entry_2=tk.Entry(master=self.main_frame2)
       #self.entry_2.grid(row=2,columnspan=1, sticky="nsew") 
    def init_glossary_labels(self):
       """ add labels to application"""
       label = tk.Label(master=self.main_frame1_websites,text="Line of Code", fg="black", bg="blue")
       label.grid(row=0)
       label.config(font=('Times New Roman',10),bg='white')
       label = tk.Label(master=self.main_frame2_websites,text="Glossary Definition", fg="black", bg="blue")
       label.grid(row=0)
       label.config(font=('Times New Roman',10),bg='white') 
       label = tk.Label(master=self.main_frame3_websites,text="Website", fg="black", bg="blue")
       label.grid(row=0)
       label.config(font=('Times New Roman',10),bg='white') 
    def init_glossary_buttons(self):
       """add buttons to application """
       self.button_1_websites = customtkinter.CTkButton(master=self.main_frame1_websites, text="line_of_code_search_sort_and_upload",text_color='white')
       self.button_1_websites.grid(row=2, column=0, sticky="nsew")
       
       self.button_2_websites = customtkinter.CTkButton(master=self.main_frame2_websites, text="glossary_search",text_color='white')
       self.button_2_websites.grid(row=2, column=0, sticky="nsew")
       
       self.button_3_websites = customtkinter.CTkButton(master=self.main_frame3_websites, text="update_code_base",text_color='white')
       self.button_3_websites.grid(row=2, column=0, sticky="nsew")
       
       #self.button_4_websites = customtkinter.CTkButton(master=self.main_frame4_websites, text="pyautogui_button",text_color='white')
       #self.button_4_websites.grid(row=2, column=0, sticky="nsew")
    def bind_glossary_functions_list_boxs(self):
       """add buttons functions to listboxs """
       #self.listboxxy3.bind('1', self.view_glossary_websites)
       #self.listboxxy4.bind('1', self.open_python_file_in_idle)
       
       # open up a window with values for database
       # expand on glossary defintions open new window
    def bind__glossary_functions_buttons(self):
        """add button functions to buttons """
        #self.button_1.bind("<Button-1>", self.line_of_code_search_sort_and_upload)
        #self.button_2.bind("<Button-1>", self.glossary_search_sort_and_upload)
        #self.button_3.bind("<Button-1>", self.update_code_base)
    def bind__glossary_functions_search_bars(self):
        """add button functions to search bars """
        #self.entry_1.bind('<Return>', self.code_base_function_search_sort_and_upload)
        #self.entry_2.bind('1', self.show_problemss)
    
    def init_glossary_website_window(self):
        """ """
        # this is hte one we are working on now
        self.init_glossary_window()
        self.init_glossary_frames()
        #self.init_glossary_scroll_bar()
        self.init_text_box()
        self.init_glossary_list_boxs()
        self.init_glosary_search_bars()
        self.init_glossary_labels()
        self.init_glossary_buttons()
        self.bind_glossary_functions_list_boxs()
        self.bind__glossary_functions_buttons()
        self.bind__glossary_functions_search_bars()
        
    def view_glossary_websites(self,event,font_size=10,font_type='Microsoft YaHei'):
        """ """
        import re
        glossary_definiton_list=self.search_data_dic["glossary_definiton"]
        website_list_list=self.search_data_dic["glossary_website"]
        line_of_code_list=self.search_data_dic["line_of_code"]
        #sql query looking for major portion of website?
        select_glossary_definition=self.window.selection_get()
        glossary_def_num_in_list=re.search(r"(\d+):::",select_glossary_definition)
        glossary_def_index=int(glossary_def_num_in_list.group(1))
        print(glossary_def_index)
        glossary_definiton_list_list=glossary_definiton_list[glossary_def_index]
        website_list_list=website_list_list[glossary_def_index]
        glossary_definiton_list=glossary_definiton_list_list.split("@@@")
        website_list=website_list_list.split("@@@")
        self.init_glossary_website_window()
        self.text_box1.insert(tk.END, f"{line_of_code_list[glossary_def_index]}") 
        #self.listboxxy1_websites.insert(tk.END, f"{line_of_code_list[glossary_def_index]}")  
        for i2, glossary in enumerate(glossary_definiton_list):
            if i2==0:
                self.text_box2.insert(tk.END, f"{glossary}")
            else:
                self.text_box2.insert(tk.END, f"\n\n\n{glossary}")     
        #state="disabled",
        for website in website_list:
            self.listboxxy3_websites.insert(tk.END, website)  


        
   #### GLOSSARY SEARCH STUFF
   
    
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

            # reduce the word count to 350 for each paragraph # maybe shorter if we have to
    def create_words(self,words_string):
           """ creates a list of words splitng on spaces"""
           import re
           words_string= re.sub(r"\s\s+",r" ", words_string )
           words_string=words_string.lower()
           words_list=words_string.split(" ")
           return words_list

    def glossary_search(self,glossary_definiton_list_list,prompt_word_list):
        """search throught he combined paragraphs to find amount of matching words to words to prompt """
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
   
   
    def upload_data_to_sql_table(self):
        """upload information that you wish to upload to sql using this page """
        # need to break this up
     
        
     
        
    ### START OF WORK ON UPDATE CODE BASE
    
    def process_sql_data(self,sql_data_list_list,column_list):
           """ bring data  from database """
           search_data_dic={}
           column_list_len=len(column_list)
           for column in column_list:
               search_data_dic[column]=[] 
           for sql_data_list in sql_data_list_list:
               for column, sql_data in zip(column_list,sql_data_list):
                   search_data_dic[column].append(sql_data) 
           return search_data_dic
       
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

    
    def remove_values_from_dic_1_within_dic_2(self,coding_file_dic,sql_data_dic):
         """ remove values from coding file dic that have the same line_of_code code file name and line number in file as in the sql dic"""
         #coding
         coding_file_dic_without_used_values_list=[]
         line_of_code_list_coding=coding_file_dic["line_of_code"]
         code_file_name_list_coding=coding_file_dic["code_file_name"]
         code_base_function_list=coding_file_dic["code_base_function"]
         class_name_list=coding_file_dic["class_name"]
         line_number_in_file_list_coding=coding_file_dic["line_number_in_file"]
         code_base_function_list=coding_file_dic["code_base_function"]
         docstring_list=coding_file_dic["docstring"]
         time_stamp_list=coding_file_dic["time_stamp"]
         print("remove_values_from_dic_1_within_dic_2")
         print(f"input:{len(time_stamp_list)}")
         #sql
         line_of_code_list_sql=sql_data_dic["line_of_code"]
         print(f"sql {len(line_of_code_list_sql)}")
         code_file_name_list_sql=sql_data_dic["code_file_name"]
         line_number_in_file_list_sql=sql_data_dic["line_number_in_file"]
         #loop to check for matching values
         for i, line_of_code_coding, code_file_name_coding,number_in_file_coding in zip(range(len(line_of_code_list_coding)), line_of_code_list_coding,code_file_name_list_coding,line_number_in_file_list_coding):
             match=False
             number_in_file_coding=str(number_in_file_coding)
             for line_of_code_sql, code_file_name_sql,number_in_file_sql in zip(line_of_code_list_sql,code_file_name_list_sql,line_number_in_file_list_sql):
                     if code_file_name_sql==code_file_name_coding and number_in_file_sql==number_in_file_coding:
                         match =True
                         break     
             if match==True:
                continue
             if match==False:
                 time_stamp=time_stamp_list[i]
                 docstring=docstring_list[i]
                 class_name=class_name_list[i]
                 code_base_function=code_base_function_list[i]
                 coding_file_dic_without_used_values={
                 "line_of_code": line_of_code_coding, 
                 "code_base_function": code_base_function,
                 "code_file_name":code_file_name_coding, 
                 "class_name":class_name,
                 "line_number_in_file":number_in_file_coding,
                 "docstring":docstring,
                 "time_stamp":time_stamp}
                 coding_file_dic_without_used_values_list.append(coding_file_dic_without_used_values)    
         print(f"output {len(coding_file_dic_without_used_values_list)}")
         return coding_file_dic_without_used_values_list  
    def create_glossary_prompt_tkinyer_sub(self,coding_file_dic_without_used_values_list,glossary_prompt):
        """ adds prompt to the front of each line of code we want to add to the glossary """
        coding_file_dic_without_used_values_list_with_glossary_prompt=[]
        for coding_file_dic_without_used_valuess in coding_file_dic_without_used_values_list:
            line_of_code=coding_file_dic_without_used_valuess["line_of_code"]
            coding_file_dic_without_used_valuess["glossary_prompt"]=f"{glossary_prompt} " + line_of_code + " do"  
            coding_file_dic_without_used_values_list_with_glossary_prompt.append(coding_file_dic_without_used_valuess)
            
        return coding_file_dic_without_used_values_list_with_glossary_prompt
    
    def create_glossary_prompt_tkinyer(self,coding_file_dic,glossary_prompt):
        # we need to modfiy this so that it can take the dictionary as a input
         """this is the create prompt function that is to be used with the tkinyter applciation for lookign up code and glossary """
         column_list=["line_of_code","code_file_name","line_number_in_file"]
         sql_data_list_list=self.upload_sql_values(column_list=column_list)
         sql_data_dic=self.process_sql_data(sql_data_list_list,column_list)
         coding_file_dic_without_used_values_list=self.remove_values_from_dic_1_within_dic_2(coding_file_dic,sql_data_dic)
         coding_file_dic_without_used_values_list_with_glossary=self.create_glossary_prompt_tkinyer_sub(coding_file_dic_without_used_values_list,glossary_prompt)
         return coding_file_dic_without_used_values_list_with_glossary
    
  
    def save_all_code_in_sql_table(self):
         """ go through all coding files in coding and save function line calls in a function to sql for post processing"""
         python_file_list=self.create_list_of_current_python_scripts_in_codebase()
         for python_file in python_file_list:
             python_code_line_list=self.process_coding_file(python_file)
             for python_code_line_dic in python_code_line_list:
                 self.store_value_in_sql_table(python_code_line_dic,"code_base_table")

        
        
    def save_all_code_in_sql_table_implement(self):
        if __name__ == '__main__':
            import sys
            import re
            import time
            import psycopg2
            from multiprocessing import Process
            sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\save_all_code_in_sql_table a 1.1.1.1')
            from save_all_code_in_sql_table_functions import save_all_code_in_sql_table_functions
            from save_all_code_in_sql_table_functions import save_all_code_in_sql_table_functions_child
            save_code=save_all_code_in_sql_table_functions()
            save_codec=save_all_code_in_sql_table_functions_child()
            coding_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Problems a1\Problems_functions.py"
            save_codec.save_all_code_in_sql_table()

    def get_all_code_from_github_and_translate_through_generative_model_to_get_in_usable_format_and_use_this_code_in_code_searchs_as_well(self):
        """ """
        # get all code on the internet and repeat this process for all useful funcitons you can find
        # and reassemble them
        # so we can then use this code not ever have ot write code again
    def view_all_glossary_websites_for_code_line(self):
        """ """
        
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

    def show_method_steps(self,event):
        """show the actions and strategies for a given problem """

        
    def store_value_in_sql_table(self,dictionary_of_values,table_name):
        """key are row names, value is the values that go in the rows """
        table_columns=""
        values_string=""
        if self.sql_switch==0:
            import psycopg2
            self.sql_switch=self.init_sql()
            self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
            self.cur = self.conn.cursor()
        for i, (table_column, column_value) in enumerate(dictionary_of_values.items()):
            # this will fix the error
            #^&~?
            column_value=str(column_value)
            column_value=column_value.replace("\'","^")
            column_value=column_value.replace("\"","&")
            column_value=column_value.replace(",","~")
            column_value=column_value.replace("'","?")
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
    # how can i impove the program
    # what is the program
    def open_python_file_in_idle(self,event):
        """modularize this with single purpose functions to """
        import subprocess
        python_script=self.window.selection_get()
        args=["python", "-m", "idlelib",python_script]
        subprocess.Popen(args)
        
    #Problem 3  these four are together in modifying the searc funciton
    #def use_first_listbox_as_tab_tracker_to_open_and_close_open_methods_or_glossary_tabs(self):
        # bascialyl reverse engineering chrome
    #    """use first listbox track open and closed tabs """
        # probably will only do this if we have extra time and ti becomes hard to manage all the open
        # tabs but current way seems fine
        # otherwise just add to listbox the name of strat open and 
        # add button for delete to close method and press 1 to open the given method
        # add a item to a tab, write to it when the glossary is open   
    #def create_intital_listbox_indicates_position_value_each_listbox(self):
    #    """ """  
    # where does this fit into the overall project
    # do we wanna delete every time
    # maybe only once a day
    def change_create_glossary_promp_using_pypi_data(self,coding_file_dic_without_used_values_list):
        """ """
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
         print(create_table_str)
         self.cur.execute(create_table_str)
         self.conn.commit()
         
    def delete_table_sql(self,table_name="code_base"):# still need to test this
         """delete a sql table """
         import psycopg2
         self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
         self.cur = self.conn.cursor() 
         self.cur.execute( f""" DROP TABLE {table_name};""")
         self.conn.commit()
    def convert_dictionary_list_to_list_of_dictionary(self,dictionary_with_list_values,column_list):
        """ """
        # put it inot proper format
        list_of_dictionary=[]
        for i,column in enumerate(dictionary_with_list_values[column_list[0]]):# for lenght of dicitonary with list values
            temp_dic={}
            for column in column_list:# for each key in this dicitonary
                temp_dic[column]=dictionary_with_list_values[column][i]
                
            list_of_dictionary.append(temp_dic)
        return list_of_dictionary
        
    def match_code_base_code_definitions_to_code_base_search_result(self,code_stored_in_sql_all_versions,code_base_search_result):
        """ this will help us match glossary definitions """
        import time
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

        return list_of_code_base_line_to_upload_to_sql,coding_file_dic_without_used_values_list

    def locate_newest_code_base_time_stamp(self,code_stored_in_sql_all_versions):
         """ deal with the fact that there are five of each line of code because of glossary """
         newest_entry_time_stamp=None
         temp_time_stamp_list=[]
         for i, time_stamp in enumerate(code_stored_in_sql_all_versions["time_stamp"]): 
             temp_time_stamp_list.append(float(time_stamp))
         if temp_time_stamp_list:
             newest_entry_time_stamp=max(temp_time_stamp_list)
         return newest_entry_time_stamp
    def get_code_on_computer(self):
        """ retrieve all the code on the computer and return it in a list of dictionaries"""
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
        "class_created_line_number":[]
        }
        python_file_list=self.create_list_of_current_python_scripts_in_codebase()
        for python_file in python_file_list:
            coding_file_dic,class_function_line_dic=self.process_coding_file(python_file,coding_file_dic)
        return coding_file_dic
     
    def update_code_base(self,event):# new one
        """ will run the code base creation function and glossary creation function"""
        import sys
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\labeling_code_and_creating_glossary  a1.1.1')
        from labeling_code_and_creating_glossary_functions import labeling_code_and_creating_glossary_function
        from labeling_code_and_creating_glossary_functions import labeling_code_and_creating_glossary_function_child
        label=labeling_code_and_creating_glossary_function()
        labelc=labeling_code_and_creating_glossary_function_child()
        glossary_promptt="what does"
        label.spacy_switch=0 # will need to add this to final code
        label.sql_switch=0
        code_stored_in_sql_all_versions={}
        column_list=["glossary_definiton","code_base_function","line_of_code","glossary_website","code_file_name","time_stamp"]	
        code_base_column_list=["class_name","code_base_function","code_file_name","docstring","line_number_in_file","line_of_code","time_stamp"]
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
        try:
            sql_data_list_list=self.upload_sql_values(table_name="code_base_all_version_info",column_list=column_list)
            #sql_data_list_list=gui.upload_sql_values(table_name="code_base_table",column_list=column_list)
            code_stored_in_sql_all_versions=self.process_sql_data_for_searches(sql_data_list_list,column_list)
        except Exception as e:
            print(e)
            code_stored_in_sql_all_versions=None
        code_base_search_result=self.get_code_on_computer() 
        if code_stored_in_sql_all_versions["glossary_definiton"]!=[]:
            #print("og")
            list_of_code_base_line_to_upload_to_sql_with_glossary,coding_file_dic_without_used_values_list=self.match_code_base_code_definitions_to_code_base_search_result(code_stored_in_sql_all_versions,code_base_search_result) # see what glossary defintions we have already
            newest_entry_time_stamp=self.locate_newest_code_base_time_stamp(code_stored_in_sql_all_versions)# copy code from this function to 
            current_time_stamp=time.time()
            time_change=current_time_stamp-newest_entry_time_stamp
            if  time_change> 86400:# seconds in a day
                self.delete_table_sql(table_name="code_base")
                self.create_table_sql(column_name_data_type_dic,table_name="code_base")
                for code_base_sql_line in list_of_code_base_line_to_upload_to_sql_with_glossary:
                    self.store_value_in_sql_table(code_base_sql_line,"code_base")        
        if code_stored_in_sql_all_versions["glossary_definiton"]==[]:
            self.delete_table_sql(table_name="code_base")
            self.create_table_sql(column_name_data_type_dic,table_name="code_base")
            coding_file_dic_without_used_values_list=self.convert_dictionary_list_to_list_of_dictionary(code_base_search_result,code_base_column_list)
        prompt_data=self.change_create_glossary_promp_using_pypi_data(coding_file_dic_without_used_values_list)# still need to write this once probably modfying the below function
        coding_file_dic_without_used_values_list_with_glossary=self.create_glossary_prompt_tkinyer_sub(coding_file_dic_without_used_values_list,glossary_promptt)
        glossary_code_dic_len=len(coding_file_dic_without_used_values_list_with_glossary)
        list_of_values_to_stop_at=list(range(6,glossary_code_dic_len,6))
        for i3,coding_line_information_with_prompt in enumerate(coding_file_dic_without_used_values_list_with_glossary):
            #print(coding_line_information_with_prompt)
            p = Process(target=labelc.retrieve_glossary_data_from_web_and_post_process_tkinyer, args=(coding_line_information_with_prompt,"code_base"))
            p.start()
            if i3 in list_of_values_to_stop_at:
                p.join() 
    def get_current_problem_project_path(self):
        """ get the last edited file in all of the coding dir and then finds the problem directory this file belongs to """
        coding_root=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding"

        import os
        import re
        from os.path import join, getsize
        root_list=[]
        sorted_time_file_list=[]
        file_path_last_modified_time_dic={"file_dir_path":[],
                                          "time_last_modified":[]}
        exempt_dirs_list=["raise_you_up","jasper_legal_news", "psp_website","websites","pyautogui_files","automate_terminal_commands","Problem_solving_phone_app",'flip_phone_app','instagram_clone', 'messager_clone', 'phone_app','testing_2', 'testing_3', 'testing_4', 'testing_5', 'testing_6', 'testing_ap','screen_shots',"screen_shots"]# test this
        last_time_latest_file_modified=0
        
        # only walk from sub the tree
        dirr_list=os.listdir(coding_root)
        print(dirr_list)
        for dirr in dirr_list:
            if dirr in exempt_dirs_list:
                print('DIRR BAND')
                continue
            #print(dirr)
            #input()
            good_sub_dir=coding_root+"\\"+dirr
            for root, dirs, files in os.walk(good_sub_dir):
                unwanted_dir=False
                ####
                #print('DIRRS')
                #print(dirs)
                #input()
                
                print("root")
                print(root)
                print(dirs)
                #input()
                #for dirrr in dirs:
                #if root in exempt_dirs_list:
                #    print(root)
                #    print('ALL IS DOG')
                #    continue
                dirs_in_dir_path=re.split(r"\\",root)
                #problem_name=dirs_in_dir_path[-1]
                #root_path=re.split(root,"\\")  
                for dirrrr in dirs_in_dir_path:
                    if dirrrr in exempt_dirs_list:
                        unwanted_dir=True
                        print('UNWANTED DIRRR')
                        break
                if unwanted_dir==True:
                    continue
                    
                #    continue
                files_and_dir_list=os.scandir(root)
                #print(files_and_dir_list)
                for file in files_and_dir_list:
                    if  file.is_file():#file.is_dir() or
                       file_stats=file.stat()
                       last_time_current_file_modified=file_stats.st_mtime
                       newest_building_file_dir_path=file.path
                       print(newest_building_file_dir_path)
                       # only pyton files
                       print(newest_building_file_dir_path[-3:])

                       if newest_building_file_dir_path[-3:]==".py":
                           print("py FOUND")
                           file_path_last_modified_time_dic["file_dir_path"].append(newest_building_file_dir_path)
                           file_path_last_modified_time_dic["time_last_modified"].append(last_time_current_file_modified)

                           
                      
                   
        file_path_last_modified_time_list_len=len(file_path_last_modified_time_dic["time_last_modified"])-1
        for i11,time_last_modified  in enumerate(file_path_last_modified_time_dic["time_last_modified"]):
            file_path=file_path_last_modified_time_dic["file_dir_path"][i11]
            if i11==0:
                print(time_last_modified)
                sorted_time_file_list.append([time_last_modified,file_path])
                continue
            for i,sorted_time_values in enumerate(sorted_time_file_list):
                sorted_time_value=sorted_time_values[0]
                if time_last_modified>=sorted_time_value:
                    sorted_time_file_list.insert(i,[time_last_modified,file_path])
                    break
                if i==file_path_last_modified_time_list_len :
                    sorted_time_file_list.append([time_last_modified,file_path])
                    break
        last_edited_file_path=sorted_time_file_list[0][1]
        # find problem directory
        problem_name_search=re.search(r"Coding\\(.*?)\\",last_edited_file_path)
        problem_project_name=problem_name_search.group(1)
        problem_project_path=coding_root+f"\{problem_project_name}"
        return problem_project_path,problem_project_name

        def get_finished_building_file_path_name(self,problem_project_path):
            """ """
            import os
            building_folder_path=problem_project_path+f"\\building"
            last_time_latest_file_modified=0
            building_files=os.scandir(building_folder_path)
            os.walk
            for file in building_files:
                if file.is_dir() or file.is_file():
                   file_stats=file.stat()
                   last_time_current_file_modified=file_stats.st_mtime
                   if last_time_current_file_modified>last_time_latest_file_modified:
                       last_time_latest_file_modified=last_time_current_file_modified
                       newest_building_file_name=file.name
                       newest_building_file_path=file.path
                       
            import os
            building_folder_path=problem_project_path+f"\\building"
            last_time_latest_file_modified=0
            building_files=os.scandir(building_folder_path)
            for file in building_files:
                if file.is_dir() or file.is_file():
                   file_stats=file.stat()
                   last_time_current_file_modified=file_stats.st_mtime
                   if last_time_current_file_modified>last_time_latest_file_modified:
                       last_time_latest_file_modified=last_time_current_file_modified
                       newest_building_file_name=file.name
                       newest_building_file_path=file.path
            print(f"newest_building_file_name: {newest_building_file_name}")                   
            return newest_building_file_path
        
    def upload_building_project_commands(self):
        """ """
        self.listboxxy0.delete(0, tk.END)
        #dog=[i for i in range(20)]
        command_list=["press 2 on function in list box to import function from building script to main script",
                      "first entry command",
                      "second entry text",
                      "0: plan out and create  project intital problem tree  and end state function and or database dic and diagram this problem tree dag for later reference",
                      "ALWAYS START WITH 0 when starting a new project so we plan to end state and effects fo different strategies or problem trees, this will display previous project problem trees for reference",
                     " for example for 0 plan out and create refer script example_for_create_problem_tree in building scripts  folder  automating coding project creation tree ",
                     """FOR NONE DATABASE PROJECT JUST SUBMIT a INTITAL  function PROBLEM TREE LIKE something like the  following:
                         '''processes_status=self.start_processes()\nended_process_status=self.end_processes()\nnew_process_name=self.create_new_processes()'''
                           
                           """,
                           """column_name_data_type_dic_coding={
                           "screen_shot_paths":"text",
                            "template_paths":"text",
                            "code_file_name_paths":"text",# only if it is a coding file otherwise just paste the active frame
                            "code_found_on_screen_per_click":"text",
                            "text_found_on_screen_per_click":"text",
                            "key_board_presses_per_click":"text",
                            "problem_name":"text",# use contexual informationfor this from screenshot and the above rows
                            "time_stamps":"FLOAT",
                            "active_windows_per_click":"text",
                            "date":"text",
                            "visual_of_problem_environment_paths":"text",#same one we have been generating
                            "visual_of_problem_tree_paths":"text",# dag
                            "strategies":"text",#ask how to a generative model?
                            "actions":"text",#ask how to a generative model?
                            "tools":"text",
                            "questions":"text",
                            "effects":"text",
                            "end_state":"text",
                            "problem_web":"text"
                            }""",
                           
                      "1: create_new_project_problem",
                      "second entry for problem name COMMAS ''",
                      "third entry either for column_name_dic or intital problem tree",
                      "fourth entry for table if a database project",
                      "to add non-database problem tree use triple quotes around tree",
                      "2:add_ last accessed building_script_function_to_main_file",
                      "make sure to save the building file you want to upload before clicking this button so it upload this one to the main script and not the wrong file", 
                      "same for pressing 3",
                      "3: generate_unwritten_function_in_parent_class_and_create_building_scripts ",
                      "4: plan out and  edit existing problem project tree to add feature or improve it and write end state function and or database dic and diagram this problem tree dag for later reference",
                      "5: edit existing problem project or add new feature with these tools"
                      ]# need to use this on the next project to get emails
        
        for i, command in enumerate(command_list):
            list_box_row=f"{command}"
            self.listboxxy0.insert(tk.END, list_box_row)
    def process_entry_inputs(self,command_list):
        """ """
        import json
        processed_command_list=[]
        for command in command_list:
            command=f"{command}"
            print(command)
            if command:
                command = eval(command) 
            print(type(command))
            print(command)
            processed_command_list.append(command)
        return processed_command_list[0],processed_command_list[1],processed_command_list[2],processed_command_list[3]
        
    def execute_building_project_command(self,event):
        """ """
        command_name=self.entry_0.get() # entry 1
        context_1=self.entry_01.get() # entry 2
        context_2=self.entry_02.get() # entry 3
        context_3=self.entry_03.get() # entry 4
        command_name,context_1,context_2,context_3=self.process_entry_inputs([command_name,context_1,context_2,context_3])
        
        # use problem solving program to start a project
        # build each strat in problem dag and sub trees in building files
        # and use this same program to edit this project down stream to add in new features
        # build this now
        #outline problem there
        # record problem and end state first step
        # add a button to swap to this coding version of problem solving program
        # for coding results maybe
        # and get strats generated from there
        # need to design the new coding problem solving program?
        # what is the problem you want to solve
        
        
        # have all problem solving programs running at once when using it
        if command_name==0:
            # basically put the building scripts on steriods with this and coding proram
            # so how do we do this integration with the coding program to help us
            # generate a project and build building script faster
            
            # and intitally 
            
            # by using the problem solving program when you are building them in addition to the 
            #coding progroam to help you write them
            # and when editing and creating a new project problem tree intitally
            
            #integrate a edited version of problem solving program with this coding program
            
            # writing a funciton is a problem or prblem tree we must apply the problem solving process to
            
            # use problem solving program to build problem trees or fucnctions
            
            # building a function whether intital problem tree or building file to implement an action intital tree
            #is a problem that we need ot use the problem solving program for
            # use htis program to help us write building functions and fill in entire function trees in larger probblem
        
            intital_problem_tree_building_script_text="what is the problem?"
            # think of this as a building script
            # to start the intital project
            # need to integrate the problem solving program here
            # edit our current building file creator file to include the thing
            # we come up here to improve it
            # basically the same process but we are building on it
            # essentially use the problem solving program to get your intital
            # script?
            # how do i do this
            print('hi')
            # action 1
            # action 2
            # action 3
            # consider the effects
            # consider the strategies
            # record intital problem trees with images?
            # create a script to help you build intital problem tree 
            # and then this script will draw a diagram of the project
            # of the intital prbolem tree or database 
    
        if command_name==1:
            problem_project_name=context_1
            table_name=context_3
            if table_name:
                print('TABLE NAME FOUND')
                column_name_data_type_dic_coding=context_2
                database_project=True   
                self.create_new_problem_project(problem_project_name,column_name_data_type_dic_coding=column_name_data_type_dic_coding,table_name=table_name,database_project=database_project)  
            else:
                intital_problem_tree=context_2
                self.create_new_problem_project(problem_project_name,intital_problem_tree=intital_problem_tree)
        if command_name==2:
            print('hi')
            problem_project_path,problem_project_name=self.get_current_problem_project_path()
            self.add_building_code_to_main_file(problem_project_path,problem_project_name)
            self.generate_unwritten_function_in_parent_class_and_create_building_scripts(problem_project_path)
        if command_name==3:
            print('hi')
            problem_project_path,problem_project_name=self.get_current_problem_project_path()
            self.generate_unwritten_function_in_parent_class_and_create_building_scripts(problem_project_path)
 
        if command_name==4:
            print('hi')
            # use problem solving program to edit problem trees or fucnctions
            # and keep using it when new problems come up when editing andf repeat the process
            # building a function whether intital problem tree or building file to implement an action intital tree
            #is a problem that we need ot use the problem solving program for

            
        if command_name==5:
            print('hi')
            self.group_functions_in_youngest_class_based_on_packages_and_context()# like group sql functions together
            self.generalize_function_inputs()  
            
            
            
            
    def convert_sql_table_to_problem_tree(self,column_name_data_type_dic_coding,table_name):
        """ """
        intital_problem_tree=""
        for column_name,column_type in column_name_data_type_dic_coding.items():
            intital_problem_tree+=f"\n{column_name}=self.generate_{column_name}()"
        intital_problem_tree+=f"\ntable_name='{table_name}'"
        intital_problem_tree+="\ndicitonary_of_values={"
        for i, (column_name,column_type) in enumerate(column_name_data_type_dic_coding.items()):
            if i==0:
                intital_problem_tree+=f"\n'{column_name}':{column_name}"
                continue
            intital_problem_tree+=f",\n'{column_name}':{column_name}"
            continue
            
        intital_problem_tree+="\n}"
        intital_problem_tree+="\nself.store_value_in_sql_table(dicitonary_of_values,table_name)"
        return intital_problem_tree
   
    def create_project_folders(self,problem_project_name):
        """ """
        import os
        import re
        problem_project_name=re.sub(" ","_",problem_project_name)
        problem_project_path = r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding' +f"\{problem_project_name}"
        problem_script_folder_path=problem_project_path+f"\{problem_project_name}_functions"
        building_folder_path=problem_project_path+f"\\building"
        inputs_folder_path=problem_project_path+f"\\inputs"
        strategy_folder_path=problem_project_path+f"\\strategies"
        if not os.path.exists(problem_project_path):
            os.makedirs(problem_project_path)
            os.makedirs(problem_script_folder_path)
            os.makedirs(building_folder_path)
            os.makedirs(inputs_folder_path)  
            os.makedirs(strategy_folder_path) 
            return problem_project_path, problem_script_folder_path,building_folder_path,inputs_folder_path,strategy_folder_path

        else:
            print("this directory already exists for this project")

            
        
    def construct_python_file_dic(self,python_script_split_lines,strip_code=True):
        """ takes a  python file and turns it into a dicitonary divided into class and functions"""
        class_dic_function_list_function_dic_code_list_code={}
        saved_function_line=""
        current_class_name=None
        function=False
        class_dic_function_list_function_dic_code_list_code[current_class_name]={}
        for line_number,code_line in enumerate(python_script_split_lines):  
            if strip_code==True:
                code_line=code_line.strip() # we may want to swap this and not strip   
            line_type="normal"
            if "class " in code_line:
                current_class_name=code_line
                class_dic_function_list_function_dic_code_list_code[current_class_name]={}
                continue
            if "def " in code_line:
                current_function_name=code_line
                class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name]=[]  
                function=True
                continue
            if function==True:
                if "end_the_loop" in code_line:
                    line_type="end_the_loop"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue  
                if "import " in code_line:
                    line_type="package"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue    
                if "for " in code_line:
                    line_type="for_loop"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue    
                if "continue" in code_line:
                    line_type="continue"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue    
                if "break" in code_line:
                    line_type="break"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue 
                if "while" in code_line or "for " in code_line:
                    line_type="loop"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue    
                if "if " in code_line or "else:" in code_line:
                    line_type="if_else"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue    
                if ":" and "\\" in code_line:
                    line_type="link"
                    class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})
                    continue 
                class_dic_function_list_function_dic_code_list_code[current_class_name][current_function_name].append({"code_line":code_line,"line_type":line_type,"line_number":line_number})    
        return class_dic_function_list_function_dic_code_list_code
    
    
    
    def remove_single_tab(self,tab_count):
        """ remove a single tab from the tab count list """
        tab_count_len=len(tab_count)-1
        tab_count_list=[" "]*tab_count_len
        tab_count="".join(tab_count_list)
        return tab_count
    
    def write_a_python_file_str(self,class_dic_function_list_function_dic_code_list_code,new_file=True):
        """ write a python file from inputs adding in the tabs and the newline characters to format may not be purpose though"""
        # find the closest screenshot in the screenshots folder to the time of the button press
        python_file_str=""
        previous_if_else_in_function=False
        if new_file==True:
            write_header=r"# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy"
            python_file_str=write_header
        for classs_key,function_dictionary in class_dic_function_list_function_dic_code_list_code.items():                
            if classs_key!=None:
                python_file_str+=f"\n{classs_key}"
            for function_key, line_of_code_dictionary_list in function_dictionary.items():
                colon_switch=False
                colon_switch2=False
                if_else_switch=False
                loop_switch=False
                tab_count=""
                if classs_key==None:
                    python_file_str+=f"\n{function_key}"
                if classs_key!=None:
                    tab_count+=" "
                    python_file_str+=f"\n{tab_count}{function_key}" 
                    tab_count+=" "# this is for the subsquent lines of code to be tabbed in the funciton 
                for line_of_code_dictionary in line_of_code_dictionary_list:
                    code_line=line_of_code_dictionary["code_line"]
                    line_type=line_of_code_dictionary["line_type"]
                    line_number=line_of_code_dictionary["line_number"]
                    if line_type=="continue" or line_type=="break":
                        python_file_str+=f"\n{tab_count}{code_line}"
                        tab_count=self.remove_single_tab(tab_count)
                        continue
                    if line_type =="for_loop":
                        python_file_str+=f"\n{tab_count}{code_line}"
                        tab_count+=" "
                        continue
                        
                    if line_type=="link":
                        python_file_str+=f"\n{tab_count}{code_line}"
                        continue
                    if line_type=="end_the_loop":
                        print('end the loop')
                        tab_count=self.remove_single_tab(tab_count)
                        continue
                    if line_type=="loop":
                             python_file_str+=f"\n{tab_count}{code_line}"
                             tab_count+=" "
                             loop_switch=True
                             continue    
                    if line_type=="if_else":
                        if if_else_switch==False:
                             python_file_str+=f"\n{tab_count}{code_line}"
                             tab_count+=" "
                             continue
                    python_file_str+=f"\n{tab_count}{code_line}"     
        return python_file_str
    def master_write_a_python_file_str(self,python_script_split_lines):
        """ """
        class_dic_function_list_function_dic_code_list_code=self.construct_python_file_dic(python_script_split_lines,strip_code=True)
        python_file_str=self.write_a_python_file_str(class_dic_function_list_function_dic_code_list_code)
        return python_file_str
    
    
    def create_problem_script(self,problem_project_name,intital_problem_tree,problem_script_folder_path):
        """ start at g2 class"""
        import time
        from datetime import datetime
        import re
        problem_project_name=re.sub(" ","_",problem_project_name)
        timee=time.time()
        datee=datetime.today().strftime('%Y-%m-%d')
        problem_script_path=problem_script_folder_path+f"\{problem_project_name}"+"_functions0.py"
        problem_script_str=rf"# -*- coding: utf-8 -*-\n"+"Created on {datee} {timee}  @author: yyyyyyyyyyyyyyyyyyyy"
        # create all the class functions
        class_name_list=["","_child","_gchild","_g2child"]
        init_function_content_list=["self.sql_switch=0","self.spacy_switch=0","import psycopg2","self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')","self.cur = self.conn.cursor()"]
        for i7, class_name in enumerate(class_name_list):
            if i7==0:
                problem_script_str+=f"\nclass {problem_project_name}_functions{class_name}():"
            else:
                problem_script_str+=f"\nclass {problem_project_name}_functions{class_name}({problem_project_name}_functions{class_name_list[i7-1]}):"# to inherit between classes
            problem_script_str+="\ndef __init__(self):"
            problem_script_str+="\n''' '''"
            for code_line in init_function_content_list:
                problem_script_str+=f"\n{code_line}"
            if class_name=="_g2child":
                problem_script_str+=f"\ndef {problem_project_name}(self):"
                problem_script_str+=f"\n''' '''"
                problem_script_str+=f"\n{intital_problem_tree}"
        problem_script_str_split_lines=problem_script_str.splitlines()
        problem_script_str=self.master_write_a_python_file_str(problem_script_str_split_lines)
        with open(problem_script_path,"w") as f: 
            f.write(problem_script_str)   
        return
    def create_function_in_parent_class(self,problem_project_path):
       """assume newest script in the folder is the one we are working out of """
        #create_function_in_parent_class
       class_function_created_applied_dic={}
       class_placement_in_file_dic={}
       class_placement_list=[]
       class_counter=0
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
       "class_created_line_number":[]}
       import re
       import os
       python_file_pattern=re.compile(r"(.*?)(\d+)?\.py")
       dirs_in_dir_path=re.split(r"\\",problem_project_path)
       problem_name=dirs_in_dir_path[-1]
       function_dir_name=problem_name+"_functions"
       function_path=problem_project_path+f"\{function_dir_name}"
       print(function_path)
       function_dir_list=list(os.listdir(function_path))
       function_dir_list_len=len(function_dir_list)
       # find the newest file in dir
       highest_file_number=0
       current_python_file=""
       for file in function_dir_list:
           print(file)
           if ".py" in file:
               file_components=re.search(python_file_pattern,file)
               file_name=file_components.group(1)
               file_number=file_components.group(2)
               print(file_name)
               print(file_number)
               if file_number:
                   file_number=int(file_number)
               if file_number>=highest_file_number:
                   highest_file_number=file_number
                   current_python_file=function_path+f"\{file}"
                   new_file_name=f"{file_name}"+f"{file_number+1}"+".py"
           
           
       print(current_python_file)
       print(new_file_name)
       coding_file_dic, class_function_line_dic=self.process_coding_file(current_python_file,coding_file_dic)
       # how do we pick a class in the best way possible
       with open(current_python_file,"r") as f1:
           python_file_str=f1.read() 
       # use info on file to determine which class to write to
       # and write to the next eldest class   


       #print(coding_file_dic)
       line_of_code_list_coding=coding_file_dic["line_of_code"]
       code_file_name_list_coding=coding_file_dic["code_file_name"]
       code_base_function_list=coding_file_dic["code_base_function"]
       class_name_list=coding_file_dic["class_name"]
       line_number_in_file_list_coding=coding_file_dic["line_number_in_file"]
       code_base_function_list=coding_file_dic["code_base_function"]
       docstring_list=coding_file_dic["docstring"]
       time_stamp_list=coding_file_dic["time_stamp"]
       function_name_list=coding_file_dic["function_name"]
       class_created_line_number_list=coding_file_dic["class_created_line_number"]
       #selected_class
       function_in_file_pattern=re.compile(r"self\.([a-zA-Z0-9_]+)\(.*\)")# these are the functions we want
       #function_in_file_pattern=re.compile(r"def .*\.([a-zA-Z0-9_]+)\(.*\)")# these are the functions we want



       class_function_line_dic# we need to modify this so that it gets all the functions that 
       #dont have code lines yet and knows they are there so it does not over write
       # create list of functions applied(codelines) used in each class that is search able
       class_placement_list_with_class_pre_fix=[]
       # get class applied list
       for i3, classs in enumerate(class_name_list):
           class_name=re.search(r"class (.*)\(",classs).group(1)
           line_of_code=coding_file_dic["line_of_code"][i3]
           function_search_result=re.search(function_in_file_pattern,line_of_code)# this we need to fix
           if class_name not in class_function_created_applied_dic:
               class_counter+=1
               class_placement_in_file_dic[class_counter]=class_name
               class_placement_list.append(class_name)
               class_placement_list_with_class_pre_fix.append(classs)
               
               class_function_created_applied_dic[class_name]={"function_created":[],"functions_applied":[]}
           if function_search_result:
               class_function_created_applied_dic[class_name]["functions_applied"].append(function_search_result.group(1))
       
        # get class created list
       saved_class_choice=""
       for i5,function_defined_line_number in enumerate(class_function_line_dic["function_defined_line_number"]):
           function_namee=class_function_line_dic["function_name"][i5]
           for i6,class_line_number in enumerate(class_function_line_dic["class_defined_line_number"]):
               if function_defined_line_number>class_line_number:
                   print(f"function_defined_line_number : {function_defined_line_number}")
                   class_name=class_function_line_dic["class_name"][i6]
                   saved_class_choice=class_name# because this function might fall within this class line number range
           print(saved_class_choice)
           
           #if function_namee in class_function_created_applied_dic[saved_class_choice]["function_created"]:
           #    continue
           class_function_created_applied_dic[saved_class_choice]["function_created"].append(function_namee)
           
           
       # this is what we need to modify to not rewritoe the same function twice in child class
       class_function_to_create_list_dic={}      
       for child_class,function_created_applied_dic in  class_function_created_applied_dic.items():
           class_placement_in_file=class_placement_list.index(child_class)
           if class_placement_in_file==0:# we cant do the first class because it would have no parent to write to
               continue
           parent_class=class_placement_list[class_placement_in_file-1]
           class_function_to_create_list_dic[parent_class]=[]
           class_function_created_applied_dic[child_class]["functions_applied"]
           child_class_function_applied_list=class_function_created_applied_dic[child_class]["functions_applied"]
           parent_class_function_created_list=class_function_created_applied_dic[parent_class]["function_created"]

           for function_applied in child_class_function_applied_list:
               #print(parent_class_function_created_list)
               if function_applied in parent_class_function_created_list:
                   continue
               else:
                   if function_applied in class_function_to_create_list_dic[parent_class]:
                       continue
                   class_function_to_create_list_dic[parent_class].append(function_applied)  
         
                   
         
       ######
       print(f"class_function_to_create_list_dic: {class_function_to_create_list_dic}")
       python_script_line_list=list(python_file_str.splitlines())
       class_created_line_number_list=coding_file_dic["class_created_line_number"]
       for class_to_change, function_to_create_list in class_function_to_create_list_dic.items():
           if function_to_create_list==[]:
               continue
           functions_to_add_list=[]
           for function in function_to_create_list:
               functions_to_add_list.append(f" def {function}(self):")
               functions_to_add_list.append("  ''' '''")
               functions_to_add_list.append("  #inputs:")
               functions_to_add_list.append("  #outputs:")
               functions_to_add_list.append("  #packages:")
               functions_to_add_list.append("  #chatgpt_prompt:")
               functions_to_add_list.append("  #search_prompt:")
               functions_to_add_list.append("  #end state: ")
               functions_to_add_list.append("  return ")
           for i4, classs in enumerate(class_name_list):
               class_name=re.search(r"class (.*)\(",classs).group(1)
               if class_to_change==class_name:
                   class_to_change_index=class_placement_list.index(class_to_change)
                   child_classs=class_placement_list_with_class_pre_fix[class_to_change_index+1]
                   child_class_index=coding_file_dic["class_name"].index(child_classs)
                   line_number_before_next_class_defined=coding_file_dic["class_created_line_number"][child_class_index]-1# minusing 1 here ot get the line before
                   #python_script_line_list[line_number_before_next_class_defined]# will need to edit this
                   python_script_line_list2=python_script_line_list[:line_number_before_next_class_defined]+functions_to_add_list+python_script_line_list[line_number_before_next_class_defined:]
       new_python_file_str=""
       #try: 
       print("this breaking here is to stop the program before writing a new file either in main or building if there is no results to write dont fix this")
       # this breaking here is to stop the program if there is no results to write dont fix this
       for line5 in python_script_line_list2:
           new_python_file_str+=f"\n{line5}"       
       new_file_name_path= function_path+f"\{new_file_name}"
       with open(new_file_name_path,"w") as f:
           f.write(new_python_file_str)
       return class_function_to_create_list_dic,coding_file_dic
        # label these correctly # label all of the funciton
        # like encode the formula we wanted to use using a_1
        # so we know which function corresponds to which other parent functions
    def transfer_building_function_to_main_file(self,building_file_path,problem_folder_path):
        """ this will find all attributes in a building script and then wrtie them into the main function"""
        import time
        import re
        building_file_dic={"inputs":[],# these will be added after self
                           "notes":[],
                           "doc_string":[],
                           "code_lines":[],
                           "outputs":[]# these we will give after the return statement     
            }
        dirs_in_dir_path=re.split(r"\\",building_file_path)
        function_nameee=dirs_in_dir_path[-1][:-3]
        time_stamp = time.time()
        saved_class_line=""
        saved_function_line=""
        python_code_line_list=[]
        stored_glossary_code_dic={}
        whole_functions_dic={}
        function_number_list_for_in_line_code={}
        #what we are doing now is a building folder this will tell us how to write it to the file
        # and fill in the function
        # so lets figure out how to write this to the function
        package_to_describe=re.compile(r"\(.*?\)")
        within_bracket_pattern=re.compile(r"\((.*)\)")
        print(building_file_path)
        with open(building_file_path,"r",encoding="utf8") as f8:
            building_file_str=f8.read()
        building_file_str_split_lines=building_file_str.splitlines()
        temp_input_list=[]
        temp_output_list=[]
        for line_number,line in enumerate(building_file_str_split_lines):
            if line_number<3:
                continue
            line_striped=line.strip()
            line=re.sub(r"\+","",line)
            building_file_dic["code_lines"].append(line)# this we will get add as is
            bracket_within_code_line=re.search(within_bracket_pattern,line)
            if bracket_within_code_line:# this is for inputs        
                bracket_content=bracket_within_code_line.group(1)
                bracket_content_split=re.split("[,]",bracket_content)
                for bracket_content in bracket_content_split:
                    character_present=re.search(r"[a-zA-Z]",bracket_content)
                    if character_present:
                        unwanted_character_present=re.search(r"[\"\'\(\[\}]",bracket_content)
                        if unwanted_character_present:
                            continue
                        kwarg_input=re.search("=(.*)",bracket_content)# for kwargs
                        if kwarg_input:
                            kwarg_input=kwarg_input.group(1)
                            if kwarg_input in building_file_dic["inputs"]:
                                continue
                            building_file_dic["inputs"].append(kwarg_input)
                            continue  
                        if bracket_content=="":
                            continue  
                        if bracket_content in building_file_dic["inputs"]:
                            continue
                        building_file_dic["inputs"].append(bracket_content)
                        continue 
            # outputs time    
            if line_striped[:2]=="if":
                continue
            if line_striped[:1]=="#":
                continue
            if bracket_within_code_line:
                start_of_bracket_found=bracket_within_code_line.start(1)
                line=line[:start_of_bracket_found]
            outputs=re.search(r"(.*)=",line)
            #outputs=re.search(r"(.*)=.*\(",line)
            if outputs:
                output_split=re.split("[,]",outputs.group(1))
                for output in output_split:
                    # we could improve this at one point
                    output=output.strip()
                    if  output in building_file_dic["outputs"]:
                        continue
                    building_file_dic["outputs"].append(output)
        # to the other file
        import os
        python_file_pattern=re.compile(r"(.*?)(\d+)?\.py")
        dirs_in_dir_path=re.split(r"\\",problem_folder_path)
        problem_name=dirs_in_dir_path[-1]
        function_dir_name=problem_name+"_functions"
        #print(function_dir_name)
        function_path=problem_folder_path+f"\{function_dir_name}"
        #print(function_path)
        function_dir_list=list(os.listdir(function_path))
        function_dir_list_len=len(function_dir_list)
        highest_file_number=0
        current_python_file=""
        new_main_script_name=""
        new_main_file_path=""
        for file in function_dir_list:
            #print(file)
            if ".py" in file:
                file_components=re.search(python_file_pattern,file)
                file_name=file_components.group(1)
                file_number=file_components.group(2)
                if file_number:
                    file_number=int(file_number)
                if file_number>=highest_file_number:
                    highest_file_number=file_number
                    current_python_file=function_path+f"\{file}"
                    new_main_script_name=f"{file_name}"+f"{file_number+1}"+".py"
                    new_main_file_path=function_path+f"\{new_main_script_name}"
                
            
        print(f"current_python_file: {current_python_file}" )
        print(f"new_file_path : {new_main_file_path}")
        
        with open(current_python_file,"r") as f1:
            python_file_str=f1.read() 
        # find next function
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
        "class_created_line_number":[]}
        coding_file_dic, class_function_line_dic=self.process_coding_file(current_python_file,coding_file_dic)
        print(coding_file_dic)
        print(class_function_line_dic)
        for line_num, function_name1 in enumerate(class_function_line_dic["function_name"]):
            print(function_name1)
            print(function_nameee)
            if function_name1==function_nameee:
                # we need to add 1 to other line numbers because upstream in prcoess coding we add 1 to line numbers
                function_def_line_number=class_function_line_dic["function_defined_line_number"][line_num]
                next_function_line_number=class_function_line_dic["function_defined_line_number"][line_num+1]
                break
        inputt_str=""
        python_file_str_split_lines=list(python_file_str.splitlines())
        for inputt in building_file_dic["inputs"]:
             inputt_str+=f",{inputt}"
        print("since we added 1 to line number upstream in process coding we need to remove 1 from line number here to get right line in split lines")
        python_file_str_split_lines[function_def_line_number-1]=f" def {function_nameee}(self{inputt_str}):"

        python_file_str_split_lines.insert(function_def_line_number+1,"BLANK")
        output_str="return "
        code_line_str=""
        ### SUPER IMPORTANT DO NOT DELETE
        # we add 2 to this list because we need to go one past file value to get  blank included into script
        # we minus 1 to get the the line number in split lines corresponding to  next function line number since we added one upstream in processing coding
        python_file_str_split_lines=python_file_str_split_lines[:function_def_line_number+2] +  python_file_str_split_lines[next_function_line_number-1:]
        # this is where we start building the function str that will replace the previous function str that was being used
        # action 1remove if name ==main if there is one
        # action 2 make sure the spacing and tabs align assume  3 spaces needed 
        for i8, outputtt in enumerate(building_file_dic["outputs"]):
            if i8==0:
                output_str+=f"{outputtt}"
                continue
            else:
                output_str+=f",{outputtt}"
        if_name_main_space_remove=False
        for code_line in building_file_dic["code_lines"]:
            if "if __name__ == '__main__':"in code_line:
                if_name_main_space_remove=True
                continue
            if if_name_main_space_remove==True:
                code_line_str+=f"\n {code_line}"# add a double space because of space from main   
            if if_name_main_space_remove==False:
                code_line_str+=f"\n  {code_line}"# add two spaces
        code_line_str=code_line_str+f"\n  {output_str}"
            
        python_file_str_split_lines[function_def_line_number+1]=code_line_str# add it on blank  if neeed be
        final_file_str=""

        #python_file_str_split_lines[line_number_to_write_content_to]=code_line_str
        for lineee in python_file_str_split_lines:
            final_file_str+=f"\n{lineee}"
        # delete things currently in function
        print(f'THIS IS THE SCRIPT NAME {new_main_script_name}')
        with open(new_main_file_path,"w") as f3:
            f3.write(final_file_str) 
  
            
        return building_file_dic,class_function_line_dic,new_main_file_path,coding_file_dic
    def add_input_files_to_project(self,problem_name,newest_building_file_path,building_file_dic,class_function_line_dic,new_main_file_path,coding_file_dic):
        """ """
        import re
        import os
        import time
        from datetime import datetime
        python_file_pattern=re.compile(r"(.*?)(\d+)?\.py")
        inputt_file_str=""
        timee=time.time()
        datee=datetime.today().strftime('%Y-%m-%d')
        print(new_main_file_path)
        new_main_script_name=re.split(r"\\",new_main_file_path)[-1]
        new_main_script_name=new_main_script_name[:-3]
        dirs_in_dir_path=re.split(r"\\",newest_building_file_path)
        building_script_name=dirs_in_dir_path[-1]
        building_function_name=building_script_name[:-3]
        problem_folder_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding"+f"\{problem_name}"
        problem_dir_list_dic={}
        dir_list_len_dic={}
        dirs_in_dir_path=re.split(r"\\",problem_folder_path)
        problem_name=dirs_in_dir_path[-1]
        folder_types=["inputs","_functions","strategies","building"]
        input_folder_path=rf"{problem_folder_path}"+"\inputs"
        problem_function_folder_path=problem_folder_path+f"\{problem_name}_functions"
        
        for folder_type in folder_types:
            if folder_type=="_functions":
                folder_name=problem_name+folder_type
            else:
                folder_name=folder_type 
            path=problem_folder_path+f"\{folder_name}"
            dir_list=list(os.listdir(path))
            dir_list_len=len(dir_list)
            problem_dir_list_dic[folder_name]=dir_list
            dir_list_len_dic[folder_name]=dir_list_len   
        update_file=False
        highest_file_number=0
          
        for script in problem_dir_list_dic["inputs"]:   
            file_components=re.search(python_file_pattern,script)
            file_name=file_components.group(1)
            file_number=file_components.group(2)
            print(f"file_name: {file_name}")
            print(f"file_number: {file_name}")
            updated_file_result=re.search(building_function_name,file_name)
            if updated_file_result:
                file_number=int(file_number)
                if file_number>=highest_file_number:
                    highest_file_number=file_number
                    update_file=True
                
        if update_file==True:
            file_name=problem_folder_path+f"\inputs"+f"\{building_function_name}"+f"{highest_file_number+1}"+".py"      
        if update_file==False:
            file_name=problem_folder_path+f"\inputs" +f"\{building_function_name}0.py"
        
        words_in_function_file_name=new_main_script_name.split("_")
        first_word_in_function_file_name=words_in_function_file_name[0]
        class_init_str="" 
        inputt_file_str=rf"# -*- coding: utf-8 -*-\n"+f"Created on {datee} {timee}  @author: yyyyyyyyyyyyyyyyyyyy"
        inputt_file_str+="\nif __name__ == '__main__':"
        inputt_file_str+="\n import sys"
        inputt_file_str+=f"\n sys.path.append(r'{problem_function_folder_path}')"
        class_init_name_dic={}
        for i, class_namee in enumerate(class_function_line_dic["class_name"]):
            inputt_file_str+=f"\n from {new_main_script_name} import {class_namee}"
            class_init_name =f"{first_word_in_function_file_name}{i}"
            inputt_file_str+=f"\n {class_init_name}={class_namee}()" 
            class_init_name_dic[class_namee]=class_init_name
        print(building_file_dic)
        if len(building_file_dic["inputs"])>1:
            inputt_listt=[]
            for inputt in building_file_dic["inputs"]:
                if inputt=="self":
                    continue
                inputt_file_str+= f"\n {inputt}="
                inputt_listt+=f"{inputt},"
        else:
            inputt_listt=""
            #if building_file_dic:
            #    if building_file_dic['inputs'][0]=="self":
            #        inputt_listt=""
            #    else:
            #         inputt_listt=f"{building_file_dic['inputs'][0]},"
            #         inputt_file_str+= f"\n {building_file_dic['inputs'][0]}="  
        # class associaoted with function
        # still need to get this correct the class jname when we import a function
        class_name_of_function="COUld NOT FIND"
        function_class_init_name=""
        for i5, function_name1 in enumerate(coding_file_dic["function_name"]):
            print('MEOW')
            if function_name1==building_function_name:# need to test this
                print(function_name1)
                print(building_function_name)

                class_name_of_function=coding_file_dic["class_name"][i5]
                class_name=re.search(r"class (.*)\(",class_name_of_function).group(1)
                function_class_init_name=class_init_name_dic[class_name]
                print(function_class_init_name)
                print(class_name)
                break
     
        inputt_file_str+=f"\n {function_class_init_name}." +f"{building_function_name}"+f"()"
        with open(file_name,"w") as f:
            f.write(inputt_file_str)
            
    def fill_in_function_gen_strats_for_function_using_problem_solving_program_code_program(self,problem_project_path,class_function_to_create_list_dic,coding_file_dic):
        """ use all the strategies we have come up with for writing functions to write
        this function from coding method in problem solving 
        program"""
        # we will use all the info from clicks etc and on the screent o write this at one point
        print(' we will use the pypi data and searches we create to fill this in when we are ready')
        print("we will use problem solving program saearcxh as well to generate strategiews and DAG when ready")
        print('we will also use whatever info we can get from mouse clicks as context to generate a good response for this')
        print('and we will use info in the coding file')
        print('YOU NEED TO WRITE THIS FUNCTION OCNE YOU HAVE ALL THE SEARCHES DONE IS KEY')
        # this is when we would generate results for each function given our context
        # that is not written in the program

        
        
        
        
        
        
        
        # add a strats folder with sub folders associated with each function the coding program generate strats for
        # with a single script with he different strats or problem trees to complete that function
        # load these in a folder named after the function
        # scans the code file
        # use all the notes we made in the problem solving program to build this program
        # so apply all the structures and ideas we designed to design this
        
            
            
    
    def add_building_files_to_project(self,problem_project_path,class_function_to_create_list_dic,coding_file_dic):
        """ this will cover creat project building and inputs """
        import time
        from datetime import datetime
        import re
        import os
        function_in_file_pattern=re.compile(r"self\.([a-zA-Z0-9_]+)\(.*\)")# these are the functions we want
        code_base_function_list=coding_file_dic["code_base_function"]
        line_of_code_list_coding=coding_file_dic["line_of_code"]
        building_project_dir=problem_project_path+f"\\building"
        for class_to_change, function_to_create_list in class_function_to_create_list_dic.items():
            if function_to_create_list==[]:
                continue
            for function_name in function_to_create_list:
                for i6, line_of_code in enumerate(line_of_code_list_coding):
                    function_search_result=re.search(function_in_file_pattern,line_of_code)# this we need to fix
                    if  function_search_result:
                        function_in_line=function_search_result.group(1)
                        if function_in_line==function_name:
                            code_base_function=code_base_function_list[i6]
                            break
                timee=time.time()
                datee=datetime.today().strftime('%Y-%m-%d')
                problem_script_path=building_project_dir+f"\{function_name}"+".py"
                counterrr=0
                while True:
                    if os.path.exists(problem_script_path):# this way we never overwrite anything in building hopefully
                        counterrr+=1
                        problem_script_path=building_project_dir+f"\{function_name}_{counterrr}"+".py"
                    else:
                        break
                script_str=rf"# -*- coding: utf-8 -*-\n"+f"Created on {datee} {timee}  @author: yyyyyyyyyyyyyyyyyyyy"
                script_str+="\n  #what this function does:"+"\n\n  #context_info about how this function fits in overall pipeline:"+"\n\n  #inputs:"+"\n\n  #outputs:"+"\n\n #packages:"+"\n\n  #chatgpt_prompt:"+"\n  #search_prompt:"+"\n  #end state: "
                actions_str=""
                for i in range(6):
                    actions_str+=f"\n\naction{i}"
                script_str+=actions_str
                script_str+=f"\n#{function_name}(self):"
                script_str+=f"\n''' '''"
                script_str+=f"\n{code_base_function}"# need to get upstream functions
                    # we will make this more sophicasted later if we can modify the  master write python file  function
                script_str_split_lines=script_str.splitlines()
                with open(problem_script_path,"w") as f: 
                    f.write(script_str)
                    
        
        
    def create_new_problem_project(self,problem_project_name,intital_problem_tree="",column_name_data_type_dic_coding="",table_name="",database_project=False):
        """ """
        import os
        problem_project_name=re.sub(" ","_",problem_project_name)
        problem_project_path = r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding' +f"\{problem_project_name}"
        if database_project==True:
            self.create_table_sql(column_name_data_type_dic_coding,table_name=table_name)
            intital_problem_tree=self.convert_sql_table_to_problem_tree(column_name_data_type_dic_coding,table_name) 
        if not os.path.exists(problem_project_path):
            problem_project_path, problem_script_folder_path,building_folder_path,inputs_folder_path,strategy_folder_path=self.create_project_folders(problem_project_name)
            self.create_problem_script(problem_project_name,intital_problem_tree,problem_script_folder_path)
            class_function_to_create_list_dic,coding_file_dic=self.create_function_in_parent_class(problem_project_path)
            self.add_building_files_to_project(problem_project_path,class_function_to_create_list_dic,coding_file_dic)
        else:
            print('THIS PROJECT EXISTS')
      
    def generate_unwritten_function_in_parent_class_and_create_building_scripts(self,problem_project_path):
        """ this funciton will also generate results in listboxs on how we might write the given function"""# we are going to test each of these now so we dont create building files every time unless we have to
        # NEED TO FIX THESE TWO TOMORROW
        class_function_to_create_list_dic,coding_file_dic=self.create_function_in_parent_class(problem_project_path)# adding extras when we dont need them
        self.add_building_files_to_project(problem_project_path,class_function_to_create_list_dic,coding_file_dic)# adding extras when we dont need to them fix this
        self.fill_in_function_gen_strats_for_function_using_problem_solving_program_code_program(problem_project_path,class_function_to_create_list_dic,coding_file_dic) 
        
    def add_building_code_to_main_file(self,problem_project_path,problem_project_name):
        """ """
        newest_building_file_path=self.get_finished_building_file_path_name(problem_project_path)# find newest save in the directory and use this one
        building_file_dic,class_function_line_dic,new_main_file_path,coding_file_dic=self.transfer_building_function_to_main_file(newest_building_file_path,problem_project_path)
        print('when you are done writing the function press enter in this script to build strategies')
        self.add_input_files_to_project(problem_project_name,newest_building_file_path,building_file_dic,class_function_line_dic,new_main_file_path,coding_file_dic)
        
    def improve_finished_problem_project(self):
        """ """
        self.group_functions_in_youngest_class_based_on_packages_and_context()# like group sql functions together
        self.generalize_function_inputs()  
                
                
                
    
    def find_function_info_in_dic(self):
        """ """
    def get_finished_building_file_path_name(self,problem_project_path):
        """ """
        import os
        building_folder_path=problem_project_path+f"\\building"
        last_time_latest_file_modified=0
        building_files=os.scandir(building_folder_path)
        for file in building_files:
            if file.is_dir() or file.is_file():
               file_stats=file.stat()
               last_time_current_file_modified=file_stats.st_mtime
               if last_time_current_file_modified>last_time_latest_file_modified:
                   last_time_latest_file_modified=last_time_current_file_modified
                   newest_building_file_name=file.name
                   newest_building_file_path=file.path
        print(f"newest_building_file_name: {newest_building_file_name}")                   
        return newest_building_file_path
    
    
    def get_import_function_name_and_path_from_tkinyer(self,function_to_import):
        """ this will break since we use codingfile dic if the funciton does not have any uses of ( or ) in it"""
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
        "class_created_line_number":[]}
        import re
        function_split_liness=function_to_import.splitlines()
        for lineee in function_split_liness:
            function_str_testtt=lineee.strip()
            if function_str_testtt[:3]=="def":
                import_function_name=re.search(r"def (.*)\(",lineee).group(1)
                function_inputs=re.search(r"\(.*\)",lineee).group(0)
                break
        code_base_function_index=self.search_data_dic["code_base_function"].index(function_to_import)
        import_function_code_file_name=self.search_data_dic["code_file_name"][code_base_function_index]
        print("if it breaks here check whether functions is in a class if it is not just copy paste the funciton in as is")
        coding_file_dic, class_function_line_dic=self.process_coding_file(import_function_code_file_name,coding_file_dic)
        #print(coding_file_dic["line_of_code"])
        #print(coding_file_dic)
        
        # how do we get the class and the function names we want
        #print(f"the coding_fiel_dic: {coding_file_dic}")
        #print(import_function_name)
        #print(f"coding_file_dic: {coding_file_dic['class_name']}")
        #print(f"coding_file_dic[function_name]: {coding_file_dic['function_name']}")
        function_name_index=coding_file_dic["function_name"].index(import_function_name)
        #print(function_name_index)

        function_class_name=coding_file_dic["class_name"][function_name_index]
        #print(f"function_class_name: {function_class_name}")
        print()
        import_function_class_name=re.search(r"class (.*)\(",function_class_name).group(1)
        return import_function_class_name,import_function_name,import_function_code_file_name,function_inputs
    def import_function_to_use_in_building_file_sub(self,import_function_class_name,import_function_name,import_function_code_file_name,newest_building_file_path,function_inputs):
        """ """
        import time
        import re
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
        "class_created_line_number":[]}
        with open(newest_building_file_path,"r",encoding="utf8") as f8:# this is file we are writing to easy
            building_file_str=f8.read()
        dirs_in_dir_path=re.split(r"\\",import_function_code_file_name)
        import_function_class_folder_path="\\".join(dirs_in_dir_path[:-1])
        print(import_function_class_folder_path)
        functions_file_name=dirs_in_dir_path[-1][:-3]        
        words_in_function_file_name=functions_file_name.split("_")
        first_word_in_function_file_name=words_in_function_file_name[0]
        class_init_str="" 
        building_file_str_split_lines=building_file_str.splitlines()
        sys_init=False
        for i3, code_line in enumerate(building_file_str_split_lines):
            if "if __name__ == '__main__':" in code_line:
                main_def_code_line=i3
            if "import sys" in code_line:
                sys_init=True
                sys_code_line=i3
        if sys_init==False:
            class_init_str+="\nif __name__ == '__main__':"
            class_init_str+="\n import sys"
            
        class_init_str+=f"\n sys.path.append(r'{import_function_class_folder_path}')"
        class_init_str+=f"\n from {functions_file_name} import {import_function_class_name}"
        class_init_name =f"{first_word_in_function_file_name}"
        class_init_str+=f"\n {class_init_name}={import_function_class_name}()" 
        class_init_str+=f"\n {class_init_name}.{import_function_name}{function_inputs}"
        if sys_init==True:
            building_file_str_split_lines.insert(sys_code_line+1,class_init_str)
        if sys_init==False:
            building_file_str_split_lines.insert(1,class_init_str)
        final_file_str=""
        for lineee in building_file_str_split_lines:
            final_file_str+=f"\n{lineee}"
        with open(newest_building_file_path,"w") as f:
            f.write(final_file_str) 
      
        
    def import_function_to_use_in_building_file(self,event):
        """press 2 on function listbox and then import this funciton """
        print("note this will not work when there is no class defined in the function folder rather simply copy paste these function into your building script because wihtout class should not import")
        problem_project_path,problem_project_name=self.get_current_problem_project_path()
        function_to_import=self.window.selection_get()
        import_function_class_name,import_function_name,import_function_code_file_name,function_inputs=self.get_import_function_name_and_path_from_tkinyer(function_to_import)
        newest_building_file_path=self.get_finished_building_file_path_name(problem_project_path)# find newest save in the directory and use this one
        self.import_function_to_use_in_building_file_sub(import_function_class_name,import_function_name,import_function_code_file_name,newest_building_file_path,function_inputs)# still need to fix this
        
  
    
    def improve_glossary_search_result_by_changing_search_prompt_using_pypi_info_and_add_pypi_info_to_glossary_window(self):
        """WE ADD PYPI INFO TO THIS"""
        # work on glossary stuff once we have done pypi stuff?
       # and then make search better with pypi info like package names
       # and look at database of pypi data scraped to help get glossary defintions
       # and exmaples for code
       # and other examples
       # then add these features to our glossary search results displayed
       # then redo glossary search with improved pypi info used
       #like
   
        
         
        
   
    def retrieve_data_from_chat_gpt(self,path_to_pickle,intital_prompt,recurse_prompt,i,pickle_file_name_root,pattern_to_search_soup):# NOUNS WHEN WE COME BACK
    # need to modify this
    # make it for websearch instead
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
        how_question_lists=[]
        counterr=0
        cwd = os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Pickles") 
        link = r"https://chatgpt.com/"
        #firefox_options = FirefoxOptions()
        #firefox_options.headless = True
        #driver= webdriver.Firefox(options=firefox_options)
        driver= webdriver.Firefox()
        session = requests.Session()
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept':'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/webp,*/*;q=0.8'}
        driver.get(link) #the pages link must be inserted here
        content = driver.find_element(By.ID, 'prompt-textarea')
        content.send_keys(f"{intital_prompt}")
        content.send_keys(Keys.ENTER)
        time.sleep(20)
        try:
            while True:
                content = driver.find_element(By.ID, 'prompt-textarea')
                content.send_keys(f"{recurse_prompt}")
                content.send_keys(Keys.ENTER)
                time.sleep(20)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                html= driver.execute_script("return document.documentElement.outerHTML")
                sel_soup = BeautifulSoup(html, 'html.parser')
                text_from_website=sel_soup.get_text()
                print(text_from_website)
                items_found_list=re.findall(pattern_to_search_soup,text_from_website)
                print(items_found_list)
                for question in items_found_list:
                    if question in how_question_lists:
                        continue
                    else:
                        how_question_lists.append(question)     
        except:
            with open(path_to_pickle,"wb") as  f7: #1
                pickle.dump(how_question_lists, f7, pickle.HIGHEST_PROTOCOL)
            i= f"{i}_{i}"
            pickle_file_name=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\pickles\{pickle_file_name_root}{i}.pickle"
            self.retrieve_data_from_chat_gpt(pickle_file_name,intital_prompt,recurse_prompt,i,pickle_file_name_root,pattern_to_search_soup)  
            
            
      
    def search_google_chatgpt_code_base_upload_search_results_into_single_page_before_write_function(self):
        """ """
        # change the way the search is written to make it faster
        
    #def need_to_make_glossary_more_useful_and_understandable_managable(self):
    #    """ """
        # make more useful by attaching code examples in next project using 
        # generative models
        # can do this after the pip download project
        


    
    
    

class tkinter_gui_glossary_master_code_functions_child(tkinter_gui_glossary_master_code_functions):
    def __init__(self):
       """ """
       self.sql_switch=0 
    
    
    
   
    def load_in_gui(self):
          """ """
          column_list=["glossary_definiton","code_base_function","line_of_code","glossary_website","code_file_name"]
          self.init_gui_window()
          self.init_frames()
          self.init_scroll_bar()
          self.init_list_boxs()
          self.init_list_boxs()
          self.init_search_bars()
          self.init_labels()
          self.init_buttons()
          self.bind_functions_list_boxs()
          self.bind_functions_buttons()
          self.bind_functions_search_bars()
          self.upload_building_project_commands()
          sql_data_list_list=self.upload_sql_values(table_name="code_base_table",column_list=column_list)# swap this when the other table is ready code_base #bad one is b
          data=self.process_sql_data_for_searches(sql_data_list_list,column_list)
          data2=self.remove_duplicates_for_search_data_dic()
          self.window.mainloop()
          return data2


          

class tkinter_gui_glossary_master_code_functions_gchild(tkinter_gui_glossary_master_code_functions_child):
    def __init__(self):
       """ """
    

def tkinyer_gui_to_access_glosarry(self):
    """ """
def store_all_code_i_have_written_in_table_and_make_searchable_through_tkyiner_gui(self):
     """ """
     def RECORD_problem_tree_action_that_used_past_function_with_when_so_can_use_info_for_simialr_actions_in_future(self):
         """ """
     #CREATE TKINYER button SUCH THAT YOU RECORD problem tree action that have used a past function
     # when searching so that you can easily when you have a simialr action you need
     # to take will pull up this function first
         

     # just build one big gui for searching tables
     # and create a button to do data labeling
     #to create a table
     #kill two birds with one stone
     # and to search the database so a search bar
      
          
          # and l


            
        
