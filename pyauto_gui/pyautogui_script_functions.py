# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:10:11 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
class pyautogui_script_functions():
    def __init___(self):
        """ """
 
    def check_for_template(self,template_location):
     import cv2
     import numpy as np
     import pyautogui
     import os
     platformm=os.name
     from PIL import ImageGrab
     screenshot = ImageGrab.grab()
     if platformm=='nt':
       screenshot.save(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png')
       img_rgb = cv2.imread(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png") 
     else:# linux
      screenshot.save(r'/home/jross77/Documents/pyautogui/screenshot.png')
      img_rgb = cv2.imread(r"/home/jross77/Documents/pyautogui/screenshot.png")
      
     template = cv2.imread(template_location)
     h, w = template.shape[:-1]
     res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
     threshold = .9
     location_of_template = np.where(res >= threshold)
     return location_of_template,h, w 
           
    def scroll_up_whole_page(self):
     import pyautogui
     for i in range(30):
      pyautogui.moveTo(1919, 212)
      pyautogui.scroll(1000) 
    def screenshot_saved_text_and_scroll_down_whole_page(self):
     import time
     import pyautogui
     from PIL import ImageGrab
     import numpy as np
     import pytesseract
     saved_screen_shots_text_list=[]
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR	esseract.exe'
     while True:
      screenshot = ImageGrab.grab()
      img1 = np.array(screenshot)
      text = pytesseract.image_to_string(img1)
      saved_screen_shots_text_list.append(text)
      pyautogui.moveTo(1919, 212)
      time.sleep(1)
      pyautogui.scroll(-300)
      template_present_value,h, w=self.check_for_template(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png')
      if template_present_value[0].any():
       print('match')
       break
      else:
       img_template = screenshot.crop((177, 306, 1188, 448))
       img_template.save(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png')
       continue 
    def click_button_once_found(self,template_path):
     import time
     import pyautogui
     from PIL import ImageGrab
     import numpy as np
     import pytesseract
     while True:
      pyautogui.click(1700, 971)
      pyautogui.scroll(-1000)
      template_present_value,h, w=self.check_for_template(template_path)#template
      if template_present_value[0].any():
       pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
       emplate_present_value,h, w=self.check_for_template(template_path)#template
       if template_present_value[0].any():
        pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
        break
       else:
        break
      else:
        continue            
    def grab_text_from_clipboard_re_search_and_add_text_to_clipboard(self, re_pattern,groupp=0):
     import pyperclip
     import re
     text_to_process=pyperclip.paste()
     search_result=re.search(re_pattern,text_to_process)
     if search_result:
      search_result=search_result.group(groupp)
      pyperclip.copy(search_result)
             
    def wait_till_template_gone(self,template_path):
     import time
     import pyautogui
     from PIL import ImageGrab
     import numpy as np
     import pytesseract
     while True:
      time.sleep(3)
      template_present_value,h, w=self.check_for_template(template_path)# loading screen
      if template_present_value[0].any():
       time.sleep(1)
       pyautogui.click(1700, 971)
       continue
      else:
       template_present_value,h, w=self.check_for_template(template_path)
       if template_present_value[0].any():
        time.sleep(1)
        pyautogui.click(1700, 971)
        continue
       else:
        time.sleep(3)
        template_present_value,h, w=self.check_for_template(template_path)
        if template_present_value[0].any():
         time.sleep(1)
         pyautogui.click(1700, 971)
         continue
        else:
         break
        time.sleep(5)          
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
    def process_clipboard_and_send_data_to_other_computer(self,prompt,link):
     import pyautogui
     import pyperclip
     import subprocess
     import json
     import re
     import psycopg2
     import time
     from psycopg2 import sql
     host = '192.168.2.209'  
     port = '5432'  
     dbname = 'canlawaccessible'  
     user = 'jross77'  
     password = 'MeganisGreat' 
     sql_str=f"SELECT my_id FROM pyautogui_master ;" 
     highest_id=0
     #code_line=re.pattern()# find lines i think could be code 
     # add them together
     # if multiple words just next to each other
     # then count as text
     # and no "" or '' around the words
     from bs4 import BeautifulSoup
     #parse data
     data=pyperclip.paste()
     print(data)
     soup = BeautifulSoup(data)
     p_tag_text=soup.get_text() 
     timee=time.time()
     # get id from master database that just uploaded and use this for my_id
     try:
         self.conn = psycopg2.connect(host=host,
         port=port,
         dbname=dbname,
         user=user,
         password=password)      
         self.cur = self.conn.cursor()       
         print("Connection successful!")
         self.cur.execute(sql_str)
         id_list_list= self.cur.fetchall()
         for  idd in id_list_list:
             iddd=int(idd[0])
             if iddd>=highest_id:
                 highest_id=iddd
     except Exception as e:
             print(f"Error: {e}")   
     dictionary_of_values={
     "my_id":highest_id+1,
     "code":None,# break this up into list
      "explantory_text":None,
      "prompt_problem_searched":prompt,# only if it is a coding file otherwise just paste the active frame
      "time_stamp":timee,
      "whole_text_chunk":p_tag_text,
      "website_link":link,
      "action":"write_to_pyautogui"} 
     self.upload_data_to_website_database(dictionary_of_values)




       
     #send data to website database
     # use a model down stream to parse it
     # no patterns same evident maybe blank lines
     #p_tag_text_list=p_tag_text.splitlines()
     #for text_line in p_tag_text_list:
     #    =re.search(code_line,text_line)
     #    if result:
     #        result.group(0)
     #    find code if find a pattern eventually
     #dictionary_of_values={prompt_problem_searched:prompt,whole_text_chunk:p_tag_text }
     # dicitonary of objects and qualtities  in problem to use to ask questions
     #then run script listner to get data back into computer to retrive the data from database
     #dictionary_of_values={
     #"code":["def int"],# break this up into list
     # "explantory_text":["int means this"],
     # "prompt_problem_searched":["{prompt}"],# only if it is a coding file otherwise just paste the active frame
     # "time_stamp":[timee],
     # "whole_text_chunk":["everything together"]}
         
    def move_mousey(self,move_to_list):
        import pyautogui
        for x_y_positions_list in move_to_list:
          pyautogui.moveTo(x_y_positions_list[0],x_y_positions_list[1])
    def move_mousey(self,move_to_list):
       import pyautogui
       for x_y_positions_list in move_to_list:
         pyautogui.moveTo(x_y_positions_list[0],x_y_positions_list[1])
         
    def find_newest_pyautogui_light_table(self):
        ''' '''
        import re
        import psycopg2
        host = '192.168.2.209'# ip address here
        port = '5432'
        dbname = 'canlawaccessible'
        user = 'jross77'
        password = 'MeganisGreat'
        current_highest_num=0
        newest_pyautogui_light_table=""
        get_all_table_names_str = '''
          SELECT table_name
          FROM information_schema.tables
          WHERE table_schema = 'public'
          ORDER BY table_name;'''
        try:
            self.conn = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password)  
            self.cur = self.conn.cursor()
            self.cur.execute(get_all_table_names_str)
            tables = self.cur.fetchall()
            print(tables)
            for table in tables:
                print(table[0])
                table_name=table[0]
                light_table_found=re.search(r"pyautogui_light_table_(\d)*",table_name)
                if light_table_found:
                    print(light_table_found)
                    print(light_table_found.group(1))
                    pyautogui_num_value=int(light_table_found.group(1))# get table number
                    if pyautogui_num_value>current_highest_num:
                        newest_pyautogui_light_table=table_name
                        current_highest_num=pyautogui_num_value
                        continue
                else:
                    continue
            self.cur.close()
            self.conn.close()
            #print("Connection closed.") 
            print(newest_pyautogui_light_table)
        except Exception as e:
            print(f"Error: {e}")
            input()
        return newest_pyautogui_light_table 
       
       
    def upload_data_to_website_database(self,dictionary_of_values):
       import psycopg2
       newest_pyautogui_light_table=self.find_newest_pyautogui_light_table()
       # want to write to the two tables i just created
       # write to and note actions when wrting to master current light table
       # create a master table and a light table
       # in a partiuclar way so they can retrieved by the listener 
       # find the highest value table
       import re
       from psycopg2 import sql
       host = '192.168.2.209'  
       port = '5432'  
       dbname = 'canlawaccessible'  
       user = 'jross77'  
       password = 'MeganisGreat'  
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
           sql_pyauto_gui_master_str_insert=f"INSERT INTO pyautogui_master ({table_columns}) VALUES ({values_string});"
           try:
               self.cur.execute(sql_pyauto_gui_master_str_insert)
           except Exception as E:
               print(E)           
           self.conn.commit()
           sql_pyauto_gui_light_str_insert=f"INSERT INTO {newest_pyautogui_light_table} ({table_columns}) VALUES ({values_string});"
           try:
               self.cur.execute(sql_pyauto_gui_light_str_insert)
           except Exception as E:
               print(E)            
           self.conn.commit()
       except Exception as e:
               print(f"Error: {e}")          
       self.cur.close()
       self.conn.close()
       print("Connection closed.")
    
