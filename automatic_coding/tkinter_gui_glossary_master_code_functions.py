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
        self.window.title('Code-Base Glossary Search')
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
        
        #self.main_frame5 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        #self.main_frame5.grid(row=0,column=5)#column=0, columnspan=4 #row=2,columnspan=2
 
    def init_list_boxs(self,font_size=10,font_type='Microsoft YaHei'):
        """ add listboxs to application"""
        font_type_and_size= (font_type,font_size)
        self.listbox_width=int(round(int(self.screen_width_characters)/5.5))
        self.listbox_height=int(round(self.screen_height_characters/3))
        self.listboxxy0 = tk.Listbox(self.main_frame0,width=10,height=self.listbox_height) 
        self.listboxxy0.config(yscrollcommand=self.yscroll0,font=font_type_and_size)  
        self.listboxxy0.grid(row=1,column=0)#row=1,column=0, columnspan=3
        
        self.listboxxy1 = tk.Listbox(self.main_frame1,width=int(round(self.screen_width_characters/3.5)),height=self.listbox_height) 
        self.listboxxy1.config(yscrollcommand=self.yscroll1,font=font_type_and_size)  
        self.listboxxy1.grid(row=1,column=0)#row=1,column=0, columnspan=3
        
        self.listboxxy2 = tk.Listbox(self.main_frame2,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy2.config(yscrollcommand=self.yscroll2,font=font_type_and_size) # make this slightly larger
        self.listboxxy2.grid(row=1,column=0)#row=1,column=0, columnspan=3
        
        self.listboxxy3 = tk.Listbox(self.main_frame3,width=self.listbox_width,height=self.listbox_height) 
        self.listboxxy3.grid(row=1,column=0)#row=1,column=0, columnspan=3
        self.listboxxy3.config(yscrollcommand=self.yscroll3,font=font_type_and_size) 
        
        self.listboxxy4 = tk.Listbox(self.main_frame4,width=round(self.screen_width_characters/5),height=self.listbox_height) 
        self.listboxxy4.grid(row=1,column=0)#row=1,column=0, columnspan=3
        self.listboxxy4.config(yscrollcommand=self.yscroll4,font=font_type_and_size) 

    def init_search_bars(self):
        """add search bar to application """
        self.entry_1=tk.Entry(master=self.main_frame1)
        self.entry_1.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_2=tk.Entry(master=self.main_frame2)
        self.entry_2.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_3=tk.Entry(master=self.main_frame3)
        self.entry_3.grid(row=2,columnspan=1, sticky="nsew") 
        
        self.entry_4=tk.Entry(master=self.main_frame4)
        self.entry_4.grid(row=2,columnspan=1, sticky="nsew") 
        
        #self.entry_2=tk.Entry(master=self.main_frame2)
        #self.entry_2.grid(row=2,columnspan=1, sticky="nsew") 
    def init_labels(self):
        """ add labels to application"""
        label = tk.Label(master=self.main_frame0,text="Tabs", fg="black", bg="blue")
        
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

    def init_buttons(self):
        """add buttons to application """
        self.button_1 = customtkinter.CTkButton(master=self.main_frame1, text="line_of_code_search_sort_and_upload",text_color='white')
        self.button_1.grid(row=3, column=0, sticky="nsew")
        
        self.button_2 = customtkinter.CTkButton(master=self.main_frame2, text="glossary_search",text_color='white')
        self.button_2.grid(row=3, column=0, sticky="nsew")
        
        self.button_3 = customtkinter.CTkButton(master=self.main_frame3, text="update_code_base",text_color='white')
        self.button_3.grid(row=3, column=0, sticky="nsew")
        
        self.button_4 = customtkinter.CTkButton(master=self.main_frame4, text="pyautogui_button",text_color='white')
        self.button_4.grid(row=3, column=0, sticky="nsew")
    def bind_functions_list_boxs(self):
        """add buttons functions to listboxs """
        self.listboxxy3.bind('1', self.view_glossary_websites)
        self.listboxxy4.bind('1', self.open_python_file_in_idle)
        
        
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
        time_stamp = time.time()
        saved_class_line=""
        saved_function_line=""
        python_code_line_list=[]
        stored_glossary_code_dic={}
        whole_functions_dic={}
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
            #save the functions
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
                    line_of_code=line.strip()
                    coding_file_dic["docstring"].append(docstring)
                    coding_file_dic["line_of_code"].append(line_of_code)
                    coding_file_dic["code_base_function"].append(whole_functions_dic[saved_function_name_line])
                    coding_file_dic["code_file_name"].append(coding_file_name)
                    coding_file_dic["class_name"].append(saved_class_line)
                    coding_file_dic["line_number_in_file"].append(line_number)
                    coding_file_dic["time_stamp"].append(time_stamp)
        return coding_file_dic

    
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
         create_table_str=r"CREATE TABLE code_base (id bigserial"
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
        "time_stamp":[]}
        python_file_list=self.create_list_of_current_python_scripts_in_codebase()
        for python_file in python_file_list:
            coding_file_dic=self.process_coding_file(python_file,coding_file_dic)
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
          sql_data_list_list=self.upload_sql_values(table_name="code_base",column_list=column_list)# swap this when the other table is ready code_base #bad one is b
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


            
        
