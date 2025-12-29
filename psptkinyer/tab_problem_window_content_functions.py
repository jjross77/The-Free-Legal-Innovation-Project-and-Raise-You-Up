# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 08:01:28 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

class tab_problem_window_content_functions():
    def __init__(self):
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.background_label_color='grey'
        self.problem_recorded=None
    
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
    def open_psp_problem_related_windows_in_tab_format(self):
         """ will need to subprocess this i think
         need to design the gui"""
         import tkinter as tk                     
         from tkinter import ttk 
         # add a tab that creates new tabs when selected
         #frame = tk.Frame()
         #notebook.add(frame, text="+")

         # make tab a master of an already existing thing like coding program?
         # then dont need to do anything special
   
         root = tk.Tk() 
         root.title("Tab Widget") 
         tabControl = ttk.Notebook(root) 
         tab1 = ttk.Frame(tabControl) 
         tab2 = ttk.Frame(tabControl) 
         tabControl.add(tab1, text ='Tab 1') 
         tabControl.add(tab2, text ='Tab 2') 
         window_methods2=""
         tabControl.pack(expand = 1, fill ="both") 
         listbox1 = tk.Listbox(master=tab1,width=60).grid(column = 0, 
                                   row = 0,  
                                   padx = 30, 
                                   pady = 30) 
         #listbox1 = tk.Listbox(tab1,width=60).grid(column = 0, 
         #                          row = 0,  
         #                          padx = 30, 
         #                          pady = 30) 

         #ttk.Label(tab1,  
         #          text ="Welcome to GeeksForGeeks").grid(column = 0,  
         #                               row = 0, 
         #                               padx = 30, 
         #                               pady = 30)   
         ttk.Label(tab2, 
                   text ="Lets dive into the world of computers").grid(column = 0, 
                                             row = 0,  
                                             padx = 30, 
                                             pady = 30) 
           
         root.mainloop()   

  
     
     
    def show_all_psp_problem_content_from_remote_server(self, problem_name):
        """ show al the webpages we opened, show the information in a nice format that we can use to solve a problem"""
        import subprocess
        psp_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        auto_coding_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        engineer_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        investment_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        business_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        law_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        negoiation_problem_data=self.upload_sql_data_from_remote_server(column_value,column_name,table_name)
        #change this to show this in django site

        
        # LOAD IN ALL THE TKYINER TABS
        
        
        
        
        
        # add tab logic to the window
        # popen all this shit everything
        #subprocess.Popen(["python", "show_all_psp_problem_content_from_remote_server.py"])

        #self.open_psp_problem_related_windows_in_tab_format()
        # need to integrate tab logic into problem solving program
        # create windows for enginnering, glossary, investment, and integrate into tab logic        
        # create master problem solving window rather than specific locations?
        #self.open_psp_window_in_specific_location()
        # create new window for glossary
        # open everything else as normal
        # just open update info in coding
        # just open and update dinwo in engineering
        # and reapt this for the rest
        # maybe switch over to usng html?
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
     
        
    