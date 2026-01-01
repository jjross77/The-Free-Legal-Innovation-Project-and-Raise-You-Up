# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:10:11 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
class pyautogui_script_functions():
 def __init___(self):
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
 
    
    
 def add_or_create_pyautogui_function_exe_files(self,exe_and_main_file_path,exe_and_main_file_path_linux,code_file_name_no_path,multiprocessing=False, remote=False):
     """ """
     import re
     import os
     import time
     import time
     import os
     import re
     from datetime import date
     from datetime import datetime
     todayy=date.today()
     timee=time.time()
     datee=datetime.today().strftime('%Y-%m-%d')
     if multiprocessing==True:
         file_name="multiprocessing_pyautogui_function_exe"
     if multiprocessing==False:
         file_name="pyautogui_function_exe"
         
     exe_file_name=exe_and_main_file_path+"\\"+ file_name+str(todayy)+ "  "+str(timee)+".py"
     exe_file_name=re.sub(r"[ -]","_",exe_file_name)
     #linux
     exe_file_name_linux=exe_and_main_file_path_linux+"/"+ file_name+str(todayy)+ "  "+str(timee)+".py"
     exe_file_name_linux=re.sub(r"[ -]","_",exe_file_name_linux)
     
     #write file content
     inputt_file_str=rf"# -*- coding: utf-8 -*-\n"+f"Created on {datee} {timee}  @author: yyyyyyyyyyyyyyyyyyyy"
     inputt_file_str+="\nif __name__ == '__main__':"
     inputt_file_str+="\n import sys"
     if remote==True:
         inputt_file_str+=f"\n sys.path.append(r'{exe_and_main_file_path_linux}')"    
     if remote==False:
         inputt_file_str+=f"\n sys.path.append(r'{exe_and_main_file_path}')"       
     inputt_file_str+=f"\n from {code_file_name_no_path} import pyautogui_functions"        
     inputt_file_str+=f"\n pyauto=pyautogui_functions()"         
     if multiprocessing==True:
         inputt_file_str+=f"\n pyauto.multiprocess_pyautogui_scripts_with_tab_logic()"          
     if multiprocessing==False:
         inputt_file_str+=f"\n pyauto.pyauto_gui_function0()"   
     # write file to computer  
     with open(exe_file_name_linux,"w") as f:
         f.write(inputt_file_str)
     return exe_file_name,exe_file_name_linux
 
 def create_template_mouse_click(self,screenshot_and_xy,box_size=20):
     """take a partial screenshot to get the template image """
     from PIL import ImageGrab
     from PIL import Image
     import pytesseract
     import re
     import time
     screenshot=screenshot_and_xy[0]    
     screenshot=Image.open(screenshot)
     #print(path_to_frame)
     #top_left_mouse_click=re.search(r"\(\d+, \d+\)",keyy).group(0) 
     #mouse_cordinate_split=re.search("(\d+), (\d+)",top_left_mouse_click)
     #x=int(mouse_cordinate_split.group(1))
     #y=int(mouse_cordinate_split.group(2))
     # do pixel scaling on x y
     xy=screenshot_and_xy[1]
     x=xy[0]
     y=xy[1]
     top_left_x=x-box_size
     top_y=y-box_size
     right_x=x+box_size
     bottom_y=y+box_size
     timee=time.time()
     img_template = screenshot.crop((int(top_left_x), int(top_y), int(right_x), int(bottom_y)))
     # make this saved in the folder
     linux_folder=r"/home/username/Documents/pyautogui/pyautogui_remote_creation_files"
     #template_location_str_windows=folder_name+f"\\template{timee}.png"
     
     #self.dir_to_store_script_linux
     #screenshot name
     ####
     #folder name
     template_location_str_linux=self.dir_to_store_script_linux+f"/template{timee}.png"
     img_template.save(template_location_str_linux) 
     return template_location_str_linux,template_location_str_linux
 def create_pyauto_gui_function_str_remote(self,current_script_str):
     """need to locate the corresponding screenshot with the corresponding click
     and subsistute the click for screens shot"""  
     import copy
     current_script_line_list=current_script_str.splitlines()
     current_script_line_list_f=copy.deepcopy(current_script_line_list)
     for i, screenshot_and_xy in enumerate(self.keyboard_and_mouse_press_and_time_list):       
         self.template_location_str,self.template_location_str_linux=self.create_template_mouse_click(screenshot_and_xy)
         strr_for_py_auto_script=f"""\n  if platformm=='nt':
     self.wait_till_template_present(r'{self.template_location_str}')
    else:# linux
     self.wait_till_template_present(r'{self.template_location_str_linux}') """
         current_script_line_list_f[i]=strr_for_py_auto_script           
     final_file_str=""
     for linee in current_script_line_list_f:
         final_file_str+=f"\n{linee}"
     return final_file_str
 def add_to_or_create_new_python_file(self,python_file_str,code_file_name):
     """create a python script with the values we just created """
     with open(f"{code_file_name}","w" ,encoding="utf-8") as f2:
         f2.write(python_file_str) 
 def create_pyautogui_file_of_inputs_and_video(self,previous_active_window,code_file_name_path_linux_creator):
      """ this will output the pyautogui file of the session we wanted to record """
      import time
      import os
      import re
      from datetime import date
      # create directory
      # need to feed in the previous active window here
      root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_creation_files"
      pyauto_file_dir_list=os.listdir(r"/home/jross77/Documents/pyautogui_remote_creation_files/")
      previous_active_window=re.sub(r"[^a-zA-Z0-9 ]", "", previous_active_window)# check this
      previous_active_window=re.sub(r"[ -]","_",previous_active_window)     
      self.dir_to_store_script=root_folder+"\\"+previous_active_window  
      self.dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui_remote_creation_files/"+previous_active_window
      #self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
      #self.dir_to_store_script_linux=re.sub(r"[ -]","_",self.dir_to_store_script_linux)
      timeee=time.time()    
      if previous_active_window not in pyauto_file_dir_list:
          os.mkdir(self.dir_to_store_script_linux)  
      #create coding files
      todayy=date.today()  
      code_file_name_only=previous_active_window+str(todayy)+ "  "+str(timeee)
      code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
      code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only+".py"
      code_file_name_path_linux=self.dir_to_store_script_linux+"/"+code_file_name_only+".py"
      code_file_name_no_path_for_function_import=code_file_name_only      
      code_file_name_only_screenshot=previous_active_window+str(todayy)+ "  "+str(timeee)
      code_file_name_only_screenshot=re.sub(r"[ -\.]","_",code_file_name_only_screenshot)
      final_code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only_screenshot+".py"
      code_file_name_no_path_for_function_import=code_file_name_only_screenshot  
      with open(code_file_name_path_linux_creator,"r") as ff:
          current_script_str=ff.read()
      python_file_str=self.create_pyauto_gui_function_str_remote(current_script_str)             
      self.add_to_or_create_new_python_file(python_file_str,code_file_name_path_linux)  
      single_process_exe_file_name,single_exe_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=False,remote=True)
      multi_process_file_name,multi_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=True,remote=True)
      #bash_file_name,bash_file_name_linux=self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,single_process_exe_file_name, remote=True)
      final_linux_script_dir=r"/home/jross77/Documents/pyautogui_remote_files/"+previous_active_window
      remote_computer_script_dic={"multi_process_file_name_linux":multi_process_file_name_linux,"final_code_file_name_path":final_code_file_name_path,"final_linux_script_dir":final_linux_script_dir,"dir_to_store_script_linux":self.dir_to_store_script_linux,"single_exe_process_file_name_linux":single_exe_process_file_name_linux,"single_exe_process_file_name":single_process_exe_file_name,"dir_to_store_script":self.dir_to_store_script}
      return remote_computer_script_dic
        
 def create_new_script_with_screen_shots_and_send_to_server(self,previous_active_window,code_file_name_path_linux):
     """need to write this one """
     import copy
     import socket
     host_name = socket.gethostname()
     IPAddr=socket.gethostbyname(host_name)
     #print(IPAddr)
     #IPAddr = socket.gethostbyname(hostname)
     print("Your Computer Name is:" + host_name)
     print("Your Computer IP Address is:" + IPAddr)
     #input()
     #host=sys.argv[1]
     import time
     timee=time.time()
     remote_computer_script_dic=self.create_pyautogui_file_of_inputs_and_video(previous_active_window,code_file_name_path_linux)  
     table_name=f"pyautogui_exe_files_table"
     column_name_data_type_dic={
          "exe_file_name":remote_computer_script_dic["single_exe_process_file_name_linux"],
          "multi_exe_file_name":remote_computer_script_dic["multi_process_file_name_linux"],
          "code_file_name":remote_computer_script_dic["multi_process_file_name_linux"],
          "bash_function_name":remote_computer_script_dic["multi_process_file_name_linux"],
          "window_name":remote_computer_script_dic["multi_process_file_name_linux"],
          "timee":timee,
          "computer_name":host_name,
          "host":IPAddr }
        # dicitonary of objects and qualtities  in problem to use to ask questions  
        # current ip is the website server i think 
     
     self.upload_to_remote_server_postgres(table_name,column_name_data_type_dic)
    
           
       
 
 
 def screen_record(self,screen_shot_time):
     import pyautogui
     import cv2
     import numpy as np
     import re
     spacing_to_add=""
     img = pyautogui.screenshot()     
     frame = np.array(img)
     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     path_to_frame=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\screen_shots\screenshot{screen_shot_time}.png"
     cv2.imwrite(path_to_frame,frame)
     #active_window_url=self.find_url_in_image(path_to_frame,active_window_name)
     return path_to_frame

      

 def pyautogui_click_function(self,x_og,y_og,current_screen_height,current_screen_width,og_screen_height,og_screen_width):
     """ perform click at spot and take screenshot and get template to create script later
     need to sort out scaling here
     note previous screensize and note current screensize and change accordingly
     sort out how to access scripts created on remote server on main computer
     maybe run a site so you can see the database results
     and automatically generate a executable that you can quickly add to psp
     to run on that computer either for multiprocessing or single prcoessing
    1. generate screenshot template on click on remote computer follow method already used
    2. feed into another funciton to generate a script with screenshots locally use method already used
    3. send info on this screenshott to remote website server that above
    4. make functions saved on the remote server available to easily add to psp and exe, 
    add website page to display table?
    #  Original rectangle: Width = 4, Height = 6, Desired point: (2, 3)
    #New rectangle: Width = 8, Height = 12
    #Calculations:
    #x-proportion: 2 / 4 = 0.5
    #y-proportion: 3 / 6 = 0.5
    #New point:
    #x-coordinate: 8 * 0.5 = 4
    #y-coordinate: 12 * 0.5 = 6
     """
     #from pynput import mouse
     import time 
     import pyautogui
     # get laptop screensize
     #get current screen size
     og_screen_height,og_screen_width
     current_screen_height,current_screen_width
     x_prop=x_og/og_screen_width
     y_prop=y_og/og_screen_height
     scaled_x=current_screen_width*x_prop
     scaled_y=current_screen_height*y_prop
     pyautogui.click(scaled_x,scaled_y) # need to scale x and  y correctly
     query_time= time.time()
     path_to_frame=self.screen_record(query_time)
     #print(f"ACTIVE WINDOW:{self.active_window_url} ")
     #self.active_window_url=self.get_active_url_name_from_browsers_history()
     #self.keyboard_and_mouse_press_and_time_list.append([path_to_frame,"mouse_press_l",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,self.active_window_name,spacing_to_add])  
     self.keyboard_and_mouse_press_and_time_list.append([path_to_frame,[scaled_x,scaled_y]])  
     
                 
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
 
