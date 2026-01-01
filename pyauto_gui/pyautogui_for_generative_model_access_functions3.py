# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:22:00 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
import tkinter as tk
class pyautogui_for_generative_model_access_functions():
    
    def __init___(self):
        """ """
        import time
        from selenium import webdriver
        import pyautogui
        from selenium.webdriver.common.keys import Keys
    
    def init_gui_window(self):
        """create main tkinyer window """
        self.window = tk.Tk()
        self.window.title('pyautogui glossary')
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
    
    def init_frames(self,bg_color="pink"):
        """ add frames to application"""
        self.main_frame0 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1,bg=bg_color)
        self.main_frame0.grid(row=0,column=0)#column=0, columnspan=4 #row=2,columnspan=2
     
        
        #self.main_frame5 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        #self.main_frame5.grid(row=0,column=5)#column=0, columnspan=4 #row=2,columnspan=2
    def init_text_box(self,font_size=10,font_type='Microsoft YaHei'):
         """ """
         font_type_and_size= (font_type,font_size)
         self.text_box1 = tk.Text(self.main_frame0,bd=0,height=20,width=30)#width=100
         self.text_box1.config(font=font_type_and_size)
         self.text_box1.grid(row=1,column=0)  #columnspan = 9#row=iterator
         documentation="""Program ignores first mouse click so you will need to click twice
To create a loop press . “`”
To end loop also press : “`”
To wait till image gone:"="
To wait till image present: ";"
To take a screen shot press: “,”
Do a long drag of mouse to do a full s.creen drag but must be within a certain time
Do a short drag to do the exact veritcle drag you want
To End the while loop:"]"
always when firsting enter a new page or clicking a button 
use wait till image present
this way we always start a sequence at the right time
once element is present
write the name of the textbox being filled when typing keys
so know downstream what this textbox writing is for
To end program close tkinyer window or press numlock
To save script presses press esc
remember to build as much context as possible so press the whole way through
So you can create whole operation in one go if possible 
And copy paste parts you need elsewhere  and fine tune
use past scripts as templates for new computers
"""
         self.text_box1.insert(tk.END, f"{documentation}")
         
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
        path_to_frame=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\screen_shots\screenshot{screen_shot_time}.png"
        cv2.imwrite(path_to_frame,frame)
        return path_to_frame,active_window_name,spacing_to_add
    def mini_screen_scroll(self,pressed_x_position,pressed_y_position,released_y_position):
        """scroll the length and direction between the  mouse press and mouse release """
        amount_to_scroll=int(pressed_y_position)-int(released_y_position)
        drag_to_command=f"\npyautogui.moveTo({pressed_x_position}, {pressed_y_position})\ntime.sleep(1)\npyautogui.scroll({amount_to_scroll})"
        return drag_to_command
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

    
    def store_value_in_sql_table(self,dictionary_of_values,table_name):
        """key are row names, value is the values that go in the rows """
        import re
        table_columns=""
        values_string=""
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        
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
    def upload_sql_values(self, table_name="pypi_table",column_list=None):
          """do a sql query to see if any of the values are already in codebase and if so remove them from glossary list """
          import psycopg2
          table_columns=""
          values_string=""
          where_string=""
          column_str=""
          self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
          self.cur = self.conn.cursor()
          
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
      
        
    def full_screen_scroll(self,pressed_x_position,pressed_y_position,screen_height,released_y_position):
        """ will make program full scroll  is x and y is different from a mouse click x is about the same and y is very different with a short time difference  and time is very short differnet than previous click """
        import time
        import pyautogui
        click_1=pressed_y_position
        click_2=released_y_position
        if click_2>click_1: # we have increased y so gone down the screen
            amount_to_scroll=int(released_y_position)+int(screen_height)
        if click_2<=click_1:# we have decreased the y so gone up the screen
            amount_to_scroll=int(released_y_position)-int(screen_height)
        drag_to_command=f"\npyautogui.moveTo({pressed_x_position}, {pressed_y_position})\ntime.sleep(1)\npyautogui.scroll({amount_to_scroll})"
        return drag_to_command
    def open_website_page_for_autogui(self,link):
         """ """
         import webbrowser
         webbrowser.open(link)  # Go to example.com
    def get_clipboard_data(self):
         """ this is for chatgpt"""
         import pyperclip
         data=pyperclip.paste()
         print(data)
         return data
    def upload_coding_file_and_split_lines(self,coding_file):# not using this currently
        """upload code and split lines  """
        with open(rf"{coding_file}", "r") as f:
            coding_file=str(f.read())
            python_script_split_lines=coding_file.splitlines()
            function=False
        return python_script_split_lines
    
    def import_packages_autogui_file(self,strr_for_py_auto_script):
        """ """
        strr_for_py_auto_script+="\nimport pyautogui"
        strr_for_py_auto_script+="\nimport time"
        strr_for_py_auto_script+="\nfrom PIL import ImageGrab"
        strr_for_py_auto_script+="\nimport numpy as np"
        strr_for_py_auto_script+="\nimport pytesseract"
        strr_for_py_auto_script+=f"\npytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'"
        strr_for_py_auto_script+="\nsaved_screen_shots_text_list=[]"
        #strr_for_py_auto_script+="\ntime.sleep(3)"
        return strr_for_py_auto_script
    def upload_from_sql_single_result(self,search_prompt,column_list,table_name="code_base_table"):
        """do a sql query to see if any of the values are already in codebase and if so remove them from glossary list """
        import psycopg2
        self.conn =  psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        column_str=""
        for i, column_name in enumerate(column_list):
            if i ==0:
                column_str+=f"{column_name}"
            else:
                column_str+=f",{column_name}"         
        sql_str= f"SELECT {column_str} FROM {table_name} WHERE code_base_function ILIKE '%{search_prompt}%';"
        self.cur.execute(sql_str)
        search_result_from_new_database= self.cur.fetchall()
        return search_result_from_new_database
    def process_sql_data_for_searches(self,sql_data_list_list,column_list):
         """ bring data  from database """
         self.search_data_dic={}
         column_list_len=len(column_list)
         for column in column_list:
             self.search_data_dic[column]=[] 
         for sql_data_list in sql_data_list_list:
             for column, sql_data in zip(column_list,sql_data_list):
                 sql_data=str(sql_data)
                 sql_data=sql_data.replace("^","\'")
                 sql_data=sql_data.replace("&","\"")
                 sql_data=sql_data.replace("~",",")
                 sql_data=sql_data.replace("?","'")
                 self.search_data_dic[column].append(sql_data) 
         return self.search_data_dic
    def search_data_dic_for_newest_time_stamp(self,search_data_dicc,search_prompt):
        """ get the single newest search result for a sql function"""
        time_stamp_list=search_data_dicc["time_stamp"]
        code_base_function_list=search_data_dicc["code_base_function"]
        single_function_str=""
        highest_time_stamp=0
        for i6, code_base_function,time_stamp in zip(range(len(time_stamp_list)),code_base_function_list,time_stamp_list):
            if float(time_stamp)>float(highest_time_stamp):
                highest_time_stamp=time_stamp
                single_function_str=code_base_function
        return single_function_str
    def create_template_mouse_click(self,keyy,timee,path_to_frame,folder_name,box_size=80):
        """take a partial screenshot to get the template image """
        from PIL import ImageGrab
        from PIL import Image
        import pytesseract
        import re
        screenshot=Image.open(path_to_frame)
        print(path_to_frame)
        top_left_mouse_click=re.search(r"\(\d+, \d+\)",keyy).group(0) 
        mouse_cordinate_split=re.search("(\d+), (\d+)",top_left_mouse_click)
        x=int(mouse_cordinate_split.group(1))
        y=int(mouse_cordinate_split.group(2))
        top_left_x=x-box_size
        top_y=y-box_size
        right_x=x+box_size
        bottom_y=y+box_size
        img_template = screenshot.crop((int(top_left_x), int(top_y), int(right_x), int(bottom_y)))
        template_location_str=folder_name+f"template{timee}.png"
        img_template.save(template_location_str) 
        return template_location_str
    def add_mouse_click(self,strr_for_py_auto_script,keyy,keyboard_or_mouse,timee,path_to_frame,active_window_name,folder_name):
        """ create template from screenshot and then add as a mouse click to gui"""
        if keyboard_or_mouse=="mouse_press_l" or keyboard_or_mouse=="mouse_press_r" :
            print('hi')
            self.template_location_str=self.create_template_mouse_click(keyy,timee,path_to_frame,folder_name)
            strr_for_py_auto_script+="\n"+fr"print('{active_window_name}')"
            strr_for_py_auto_script+=f"\nself.wait_till_template_present(r'{self.template_location_str}')"
        return strr_for_py_auto_script
        #if keyboard_or_mouse=="mouse_release_l":
        #    print('hi')
        #if keyboard_or_mouse=="mouse_release_r":
        #    print('hi')


    def add_mouse_code_lines_to_pyautogui_file(self,strr_for_py_auto_script,keyy,keyboard_or_mouse,screen_height,time_from_previous_action,timee,path_to_frame,active_window_name,mouse_scroll_change_for_full_page_scroll=360):
        """this produces the mouse presses actions """
        # problem integratge new features so always use template for all mouse clicks
        import re
        mouse_press_or_release=keyboard_or_mouse
        mouse_cordinate_to_click=re.search(r"\(\d+, \d+\)",keyy).group(0) 
        mouse_cordinate_split=re.search("(\d+), (\d+)",mouse_cordinate_to_click)
        x=mouse_cordinate_split.group(1)
        y=mouse_cordinate_split.group(2)
        if mouse_press_or_release=="mouse_press":
            print('hi')
            self.mouse_pressx=x
            self.mouse_pressy=y
            self.mouse_press_str=f"{self.mouse_pressx},{self.mouse_pressy}"
            return strr_for_py_auto_script 
        if mouse_press_or_release=="mouse_release":
            self.mouse_releasex=x
            self.mouse_releasey=y
            self.mouse_release_str=f"{self.mouse_releasex},{self.mouse_releasey}"
            if self.mouse_press_str==self.mouse_release_str:
                strr_for_py_auto_script+=f"\npyautogui.moveTo{mouse_cordinate_to_click}\ntime.sleep(1)\npyautogui.click()"
                return strr_for_py_auto_script
            else:
                mouse_y_change=abs(int(self.mouse_pressy)-int(y))
                print(mouse_y_change)
                print(mouse_scroll_change_for_full_page_scroll)
                # we need to get the 
                if mouse_y_change>=mouse_scroll_change_for_full_page_scroll:
                    drag_to_command=self.full_screen_scroll(self.mouse_pressx,self.mouse_pressy,screen_height,self.mouse_releasey)
                    strr_for_py_auto_script+=drag_to_command
                    print("full_page_scroll")
                if mouse_y_change<mouse_scroll_change_for_full_page_scroll:
                    mini_screen_scroll=self.mini_screen_scroll(self.mouse_pressx,self.mouse_pressy,self.mouse_releasey)
                    strr_for_py_auto_script+=mini_screen_scroll
                    print("mini_screen_scroll")
                return strr_for_py_auto_script
            
    def take_screenshot_and_grab_text(self):
        """take a screenshot """
        import time
        timee=time.time()
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
        self.screenshot_name=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screen_shot\screenshot{timee}.png"
        screenshot.save(self.screenshot_name)
        return self.screenshot_name
    def create_template_screenshot(self,screen_shot_name,top_left_mouse_click,bottom_right_mouse_click,folder_name=""):
        """take a partial screenshot to get the template image """
        ### TESTIGN TO SEE IF THIS WORKS NEXT
        from PIL import ImageGrab
        from PIL import Image
        import pytesseract
        import re
        screenshot=Image.open(screen_shot_name)
        print(screen_shot_name)
        time_stamp_of_screenshot=re.search(r"\d+\.\d+",screen_shot_name).group(0)
        top_left_mouse_click=re.search(r"\(\d+, \d+\)",top_left_mouse_click).group(0) 
        mouse_cordinate_split=re.search("(\d+), (\d+)",top_left_mouse_click)
        top_left_x=mouse_cordinate_split.group(1)
        top_y=mouse_cordinate_split.group(2)
        bottom_right_mouse_click=re.search(r"\(\d+, \d+\)",bottom_right_mouse_click).group(0) 
        mouse_cordinate_split=re.search("(\d+), (\d+)",bottom_right_mouse_click)
        right_x=mouse_cordinate_split.group(1)
        bottom_y=mouse_cordinate_split.group(2)
        print(f"LOCATION OF SCREENSHOT({int(top_left_x)}, {int(top_y)}, {int(right_x)}, {int(bottom_y)}")
        img_template = screenshot.crop((int(top_left_x), int(top_y), int(right_x), int(bottom_y)))
        template_location_str=folder_name+f"template{time_stamp_of_screenshot}.png"
        #template_location_str=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template{time_stamp_of_screenshot}.png"
        img_template.save(template_location_str) 
        return template_location_str
    
  
    
    def create_new_autogui_file(self,strr_for_py_auto_script):
        """ """
        strr_for_py_auto_script=r"# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy"
        strr_for_py_auto_script+="\nclass pyautogui_functions():"
        strr_for_py_auto_script+="\ndef __init__(self):"
        strr_for_py_auto_script+="\nprint('start_pyautogui_class')"
        strr_for_py_auto_script+="\ndef pyauto_gui_function0(self,prompt_list):"
        strr_for_py_auto_script+="\nself.open_website_page_for_autogui(link)"# will need to check this
        return strr_for_py_auto_script
    # need to change how this is strcutred so if seperatge into there own seperate folders for each script

    def create_pyauto_gui_function_str(self,keyboard_and_mouse_press_and_time_list,add_additional_functions=["check_for_template(self"]):
        """ Use info generated from  mouse clicks to create a function for pyautogui """
        import re
        import os
        import pyautogui
        self.screen_size=pyautogui.size()
        self.screen_height=self.screen_size[1]
        self.screen_width=self.screen_size[0]
        dictionary_of_keyys={"start_for_loop":f"\nfor prompt in prompt_list:",
                             "end_for_loop":f"\ncontinue",
                             "ctrl_c":f"\npyautogui.hotkey('ctrl', 'c')",
                             "take_screenshot_and_grab_text":f"\nscreenshot = ImageGrab.grab()\nimg1 = np.array(screenshot)\ntext = pytesseract.image_to_string(img1)\nsaved_screen_shots_text_list.append(text)",
                             "ctrl_a":f"\npyautogui.hotkey('ctrl', 'a')",
                             "enter":f"\npyautogui.press('enter')",
                             #"alt":f"\npyautogui.hotkey('alt', 'tab')",# dont think i need alt tab
                             "backspace":f"\npyautogui.press('backspace')",
                             "loop_ender":f"\nprint('loop_ender')\nend_the_loop"
                             
                             }
        strr_for_py_auto_script=""
        previous_time=None
        self.previous_keyboard_or_mouse=None
        mouse_press_x_position=None
        mouse_press_y_position=None
        time_from_previous_action=None
        self.block_four_clicks_switch=False
        column_list=["code_base_function","code_file_name","time_stamp"]
        self.click_count=0
        keys_to_look_for=dictionary_of_keyys.keys()
        pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files")
        pyauto_file_dir_list_len=len(pyauto_file_dir_list)
        self.script_folder_name= r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files" + r"\pyautogui_script_"+ rf"{str(pyauto_file_dir_list_len+1)}" + "\\"
        os.mkdir(self.script_folder_name)
        strr_for_py_auto_script=self.create_new_autogui_file(strr_for_py_auto_script)  
        strr_for_py_auto_script=self.import_packages_autogui_file(strr_for_py_auto_script)
        for i,keyboard_and_mouse_press_and_time in enumerate(keyboard_and_mouse_press_and_time_list):
            if self.block_four_clicks_switch==True:
                self.click_count+=1
                if self.click_count>3:
                    self.click_count=0
                    self.block_four_clicks_switch=False
                    continue
                else:
                    continue    
            keyboard_or_mouse=keyboard_and_mouse_press_and_time[0]
            keyy=keyboard_and_mouse_press_and_time[1]
            timee=keyboard_and_mouse_press_and_time[2]
            if i ==0:
                self.previous_time=timee
            else:
                time_change=timee-self.previous_time
                self.previous_time=timee
                strr_for_py_auto_script+=f"\ntime.sleep({time_change})"

            
            # add this as time to sleep
            if keyboard_or_mouse=="template_creator":
                strr_for_py_auto_script+=f"\nprint('{keyboard_or_mouse} {i}')"
                screen_shot_name=keyy[0]
                screen_shot_command=keyy[1]
                # grab the four mouse clicks after
                top_left_mouse_click=keyboard_and_mouse_press_and_time_list[i+1][1]
                bottom_right_mouse_click=keyboard_and_mouse_press_and_time_list[i+3][1]
                # need to figure out how to do this one
                self.template_location_str=self.create_template_screenshot(screen_shot_name,top_left_mouse_click,bottom_right_mouse_click,folder_name=self.script_folder_name)# creating template in past time
                if screen_shot_command=="wait_till_image_gone":
                    strr_for_py_auto_script+=f"\nself.wait_till_template_gone(r'{self.template_location_str}')"
                if screen_shot_command=="wait_till_image_present":
                    strr_for_py_auto_script+=f"\nself.wait_till_template_present(r'{self.template_location_str}')"
                self.block_four_clicks_switch=True
                continue
            if keyy in keys_to_look_for:
                strr_for_py_auto_script+=f"\nprint('{keyy}: {i}')"
                strr_for_py_auto_script+=dictionary_of_keyys[keyy]
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                if i==len(keyboard_and_mouse_press_and_time_list)-1:
                    strr_for_py_auto_script+=f"\nreturn saved_screen_shots_text_list"     
                continue
            #if keyboard_or_mouse=="loop_ender":
            #    strr_for_py_auto_script+=f"\nprint('{keyy}: {i}')"
            #    strr_for_py_auto_script+=f"\nend_the_loop"
            #    continue
            if keyboard_or_mouse=="keyboard":
                strr_for_py_auto_script+=f"\nprint('{keyy}: {i}')"
                strr_for_py_auto_script+=f"\npyautogui.write({keyy})" 
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                if i==len(keyboard_and_mouse_press_and_time_list)-1:# trying to find a place to put return statement
                    strr_for_py_auto_script+=f"\nreturn saved_screen_shots_text_list"  
                continue
            ### MOUSE STUFF
            # need to modify what is added for left mouse click using info i gathered
            if keyboard_or_mouse=="mouse_press_l" or keyboard_or_mouse=="mouse_press_r":
                path_to_frame=keyboard_and_mouse_press_and_time[3]
                active_window_name=keyboard_and_mouse_press_and_time[4]
                spacing_to_add=keyboard_and_mouse_press_and_time[5]
                strr_for_py_auto_script+=spacing_to_add
                
                if keyboard_or_mouse=="mouse_press_l":
                    strr_for_py_auto_script+=f"\nprint('{keyy}: {i}')"
                    strr_for_py_auto_script= self.add_mouse_click(strr_for_py_auto_script,keyy,keyboard_or_mouse,timee,path_to_frame,active_window_name,self.script_folder_name)
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                if i==len(keyboard_and_mouse_press_and_time_list)-1:# trying to find a place to put return statement
                    strr_for_py_auto_script+=f"\nreturn saved_screen_shots_text_list"
                continue
            ## THESE ARE LEFT
            if keyboard_or_mouse=="mouse_move":
                mouse_start_position=keyy
                print(mouse_start_position)
                mouse_cordinates=re.search(r"\((-?\d+), (-?\d+)\)",mouse_start_position) 
                #mouse_cordinate_split=re.search("(-?\d+), (-?\d+)",mouse_cordinates)
                x=int(mouse_cordinates.group(1))
                y=int(mouse_cordinates.group(2))
                strr_for_py_auto_script+=f"\npyautogui.moveTo({x}, {y})"
                
                mouse_end_position=keyboard_and_mouse_press_and_time[3]
                print(mouse_end_position)
                mouse_cordinates=re.search(r"\((-?\d+), (-?\d+)\)",mouse_end_position) 
                #mouse_cordinate_split=re.search("(\d+), (\d+)",mouse_cordinates)
                x=int(mouse_cordinates.group(1))
                y=int(mouse_cordinates.group(2))
                strr_for_py_auto_script+=f"\npyautogui.moveTo({x}, {y})"
                continue
                
            if keyboard_or_mouse=="mouse_scroll":
                amount_to_scroll=keyboard_and_mouse_press_and_time[3]
                mouse_cordinates=re.search(r"\(\d+, \d+\)",keyy).group(0) 
                mouse_cordinate_split=re.search("(\d+), (\d+)",mouse_cordinates)
                x=int(mouse_cordinate_split.group(1))
                y=int(mouse_cordinate_split.group(2))
                strr_for_py_auto_script+=f"\npyautogui.moveTo({x}, {y})\npyautogui.scroll({amount_to_scroll})"
                continue
          
        for function_name in add_additional_functions:
            function_name=re.sub("\(","\\(",function_name)
            function_name=re.sub("\)","\\)",function_name) # will need to test to see if this works
            function_result=re.search(function_name,strr_for_py_auto_script)
            if function_result:
                print("FOUND")
                continue
            else:
                print("NOT FOUND")                
                strr_for_py_auto_script=self.add_function_str_from_sql_to_file(function_name,column_list,strr_for_py_auto_script)
                continue
        strr_for_py_auto_function_split_lines=strr_for_py_auto_script.splitlines()
        return strr_for_py_auto_function_split_lines
    
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
    def add_to_or_create_new_python_file(self,python_file_str,code_file_name):
        """create a python script with the values we just created """
        with open(f"{code_file_name}","w") as f2:
            f2.write(python_file_str)   
    def get_text_from_image(self,screenshot):
        """get text from images """
        import pytesseract
        import numpy as np
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img1 = np.array(screenshot)
        text = pytesseract.image_to_string(img1)
        #print(text)
        return text
    def send_text_to_server(self):
        """we will make a website and send the data to it once we have the time """
    def add_new_line_character(self, inputt_str):
        """ """
        output_str=inputt_str+"\n"
        return output_str
    def add_function_str_from_sql_to_file(self,search_prompt,column_list,strr_for_py_auto_script):
        """upload the function to the strring for pyautogui"""
        #print(search_data_dic)
        # TEMPOARILY JUST GOING TO SCTAP THIS fix it if we need to make it more diverse by fixing search funciton in glossary program
        strr_for_py_auto_script+=f"\ndef check_for_template(self,template_location):"
        strr_for_py_auto_script+=f"\nimport cv2"
        strr_for_py_auto_script+=f"\nimport numpy as np"
        strr_for_py_auto_script+=f"\nimport pyautogui"
        strr_for_py_auto_script+=f"\nfrom PIL import ImageGrab"
        strr_for_py_auto_script+=f"\nscreenshot = ImageGrab.grab()"
        strr_for_py_auto_script+="\n"+rf"screenshot.save(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png')"
        strr_for_py_auto_script+="\n"+rf'img_rgb = cv2.imread(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png")'
        strr_for_py_auto_script+=f"\ntemplate = cv2.imread(template_location)"
        strr_for_py_auto_script+=f"\nh, w = template.shape[:-1]"
        strr_for_py_auto_script+="\n"+fr"res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)"
        strr_for_py_auto_script+=f"\nthreshold = .9"
        strr_for_py_auto_script+=f"\nlocation_of_template = np.where(res >= threshold)"
        strr_for_py_auto_script+=f"\nreturn location_of_template,h, w"
        # add wait till image gone
        ### scroll up
        strr_for_py_auto_script+=f"\ndef scroll_up_whole_page(self):"
        strr_for_py_auto_script+=f"\nimport pyautogui"
        strr_for_py_auto_script+=f"\nfor i in range(30):"
        strr_for_py_auto_script+=f"\npyautogui.moveTo(1919, 212)"
        strr_for_py_auto_script+=f"\npyautogui.scroll(1000)"
        ### screenshot save text and scroll down
        strr_for_py_auto_script+=f"\ndef screenshot_saved_text_and_scroll_down_whole_page(self):"
        strr_for_py_auto_script+=f"\nimport time"
        strr_for_py_auto_script+=f"\nimport pyautogui"
        strr_for_py_auto_script+=f"\nfrom PIL import ImageGrab"
        strr_for_py_auto_script+=f"\nimport numpy as np"
        strr_for_py_auto_script+=f"\nimport pytesseract"
        strr_for_py_auto_script+=f"\nsaved_screen_shots_text_list=[]"
        strr_for_py_auto_script+=f"\npytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'"
        strr_for_py_auto_script+=f"\nwhile True:"
        strr_for_py_auto_script+=f"\nscreenshot = ImageGrab.grab()"
        strr_for_py_auto_script+=f"\nimg1 = np.array(screenshot)"
        strr_for_py_auto_script+=f"\ntext = pytesseract.image_to_string(img1)"
        strr_for_py_auto_script+=f"\nsaved_screen_shots_text_list.append(text)"
        strr_for_py_auto_script+=f"\npyautogui.moveTo(1919, 212)"
        strr_for_py_auto_script+=f"\ntime.sleep(1)"
        strr_for_py_auto_script+=f"\npyautogui.scroll(-300)"
        strr_for_py_auto_script+="\n"+rf"template_present_value,h, w=self.check_for_template(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png')"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\nprint('match')"
        strr_for_py_auto_script+=f"\nbreak"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\nimg_template = screenshot.crop((177, 306, 1188, 448))"
        strr_for_py_auto_script+="\n"+rf"img_template.save(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png')"
        strr_for_py_auto_script+=f"\ncontinue"
        ### click_button_once_found
        strr_for_py_auto_script+=f"\ndef click_button_once_found(self,template_path):"
        strr_for_py_auto_script+=f"\nimport time"
        strr_for_py_auto_script+=f"\nimport pyautogui"
        strr_for_py_auto_script+=f"\nfrom PIL import ImageGrab"
        strr_for_py_auto_script+=f"\nimport numpy as np"
        strr_for_py_auto_script+=f"\nimport pytesseract"
        strr_for_py_auto_script+=f"\nwhile True:"
        strr_for_py_auto_script+=f"\npyautogui.click(1700, 971)"
        strr_for_py_auto_script+=f"\npyautogui.scroll(-1000)"
        strr_for_py_auto_script+=f"\ntemplate_present_value,h, w=self.check_for_template(template_path)#template"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\npyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))"
        strr_for_py_auto_script+=f"\nemplate_present_value,h, w=self.check_for_template(template_path)#template"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\npyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))"
        strr_for_py_auto_script+=f"\nbreak"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\nbreak"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\ncontinue"
        ### wait till template gone
        strr_for_py_auto_script+=f"\ndef wait_till_template_gone(self,template_path):"
        strr_for_py_auto_script+=f"\nimport time"
        strr_for_py_auto_script+=f"\nimport pyautogui"
        strr_for_py_auto_script+=f"\nfrom PIL import ImageGrab"
        strr_for_py_auto_script+=f"\nimport numpy as np"
        strr_for_py_auto_script+=f"\nimport pytesseract"
        strr_for_py_auto_script+=f"\nwhile True:"
        strr_for_py_auto_script+=f"\ntime.sleep(3)"
        strr_for_py_auto_script+=f"\ntemplate_present_value,h, w=self.check_for_template(template_path)# loading screen"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\ntime.sleep(1)"
        strr_for_py_auto_script+=f"\npyautogui.click(1700, 971)"
        strr_for_py_auto_script+=f"\ncontinue"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\ntemplate_present_value,h, w=self.check_for_template(template_path)"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\ntime.sleep(1)"
        strr_for_py_auto_script+=f"\npyautogui.click(1700, 971)"
        strr_for_py_auto_script+=f"\ncontinue"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\ntime.sleep(3)"
        strr_for_py_auto_script+=f"\ntemplate_present_value,h, w=self.check_for_template(template_path)"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\ntime.sleep(1)"
        strr_for_py_auto_script+=f"\npyautogui.click(1700, 971)"
        strr_for_py_auto_script+=f"\ncontinue"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\nbreak"
        strr_for_py_auto_script+=f"\ntime.sleep(5)"
        ### def wait till template present
        strr_for_py_auto_script+=f"\ndef wait_till_template_present(self,template_path):"
        strr_for_py_auto_script+=f"\nimport time"
        strr_for_py_auto_script+=f"\nimport pyautogui"
        strr_for_py_auto_script+=f"\nfrom PIL import ImageGrab"
        strr_for_py_auto_script+=f"\nimport numpy as np"
        strr_for_py_auto_script+=f"\nimport pytesseract"
        strr_for_py_auto_script+=f"\ncounterr=0"

        strr_for_py_auto_script+=f"\nwhile True:"
        strr_for_py_auto_script+=f"\ncounterr+=1"
        strr_for_py_auto_script+=f"\nif counterr>30:"
        strr_for_py_auto_script+=f"\nrestart_master_script(input_values)"
        strr_for_py_auto_script+=f"\nreturn"
        strr_for_py_auto_script+=f"\ntemplate_present_value,h, w=self.check_for_template(template_path)"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\npyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))"
        strr_for_py_auto_script+=f"\nbreak"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\ncontinue"
        strr_for_py_auto_script+=f"\ntime.sleep(2)"
        # when it gets stuck restart the whole program
          # build this in
          # this way if it is not working at one point it does not screw us
          # call itself recurviely if it recurses too many times just add this in
          
        return strr_for_py_auto_script
        single_newest_function_str=self.search_data_dic_for_newest_time_stamp(search_data_dic,search_prompt)
        print(single_newest_function_str)
        function_line_list=single_newest_function_str.splitlines()
        print(function_line_list)
        for line in function_line_list:
            line=line.strip()
            strr_for_py_auto_script+=f"\n{line}"
        return strr_for_py_auto_script
class pyautogui_for_generative_model_access_functions_child(pyautogui_for_generative_model_access_functions):
    def __init___(self):
        """ """
    def store_problem_data(self):
        """ """
        table_name=""
        dicitonary_of_values={"email_name":email_name,
                                    "email_password":password,
                                    "github_user_name":user_name,
                                    "github_password":password,
                                    "email_last_accessed":time_stamp}
        self.store_value_in_sql_table(dicitonary_of_values,table_name)
    def run_program_on_startup(self):
        """ """
        #https://medium.com/@BetterEverything/run-python-scripts-on-windows-startup-cec5e177db59#:~:text=You%20can%20go%20to%20the,file%20into%20the%20Startup%20folder.
        #You can go to the folder by pressing the Windows key (⊞) + R. Then a program called Run appears in which you type shell:startup and hit enter. This will open the Startup folder. You can then drag and drop or copy the Python file into the Startup folder
    def upload_problem_data(self):
        """ """
        column_list=[]
        sql_data_list_list=self.upload_sql_values(table_name="problem_tree_table?",column_list=column_list)
        self.process_sql_data_for_searches(sql_data_list_list,column_list)
  
    
    
    
    #save each click to database?
    # maybe leverage windows to determine which coding file has been updated 
    # latest
    # other options is to screenshot and use info on the screen
    # maybe use screenshot info to peice together code we were working on
    # figure out the functions in the screenshot and then determine the script folder this function is in
    # from thsi get the script name and save this to the result
    
    # use screenshots look at screenshot to determine the coding file we are working 
        


    def on_mouse_scroll(self,x, y, dx, dy):
        import time
        timee=time.time()
        amount_to_scroll=100
        if self.last_input=="mouse_scroll":
            #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
            self.keyboard_and_mouse_press_and_time_list[-1][3]+=amount_to_scroll
        else:
            self.keyboard_and_mouse_press_and_time_list.append(["mouse_scroll",'Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)),timee,amount_to_scroll])
            self.last_input="mouse_scroll"

    def on_mouse_move(self, x, y):
        import time
        timee=time.time()
        
        if self.last_input=="mouse_move":
            print('Pointer moved to {0}'.format((x, y)))
            mouse_end_position='{0}{1}'.format('Pressed',(x, y))
            self.keyboard_and_mouse_press_and_time_list[-1][3]=mouse_end_position
            print(self.keyboard_and_mouse_press_and_time_list[-1])
        else:
            mouse_start_position='{0}{1}'.format('Pressed',(x, y))
            self.keyboard_and_mouse_press_and_time_list.append(["mouse_move",mouse_start_position,timee,mouse_start_position])
            self.last_input="mouse_move"

    def mouse_pynput_on_click(self,x, y, button, pressed):
        """record on click elements """
        # get mouse scroll
        from pynput import mouse
        import time 
        query_time= time.time()
        path_to_frame,active_window_name,spacing_to_add=self.screen_record(query_time)
        if button == mouse.Button.right:# need to add in right mosue clicks
            print('RIGHT')
            print('{0}{1}'.format('Pressed',(x, y)))
            if self.last_input=="mouse_press_r":
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_release_r",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,active_window_name,spacing_to_add])
                print(self.keyboard_and_mouse_press_and_time_list)
                self.last_input="mouse_release_r"
                return
            else:
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_press_r",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,active_window_name,spacing_to_add]) 
                self.last_input="mouse_press_r"
                return
        if button == mouse.Button.left:
            if self.last_input=="mouse_press_l":
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_release_l",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,active_window_name,spacing_to_add])
                print(self.keyboard_and_mouse_press_and_time_list)
                self.last_input="mouse_release_l"
                return
            else:
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_press_l",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,active_window_name,spacing_to_add])  
                self.last_input="mouse_press_l"
                return
 
    def keyboard_on_press_pynput(self,event):
        """ """
        from pynput import keyboard
        import time
        import re
        if event == keyboard.Key.esc:# do all the work in here with downstream functions
            #code_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\
            self.create_pyautogui_file_of_inputs_and_video()
            print("stop this program by closing the pyautogui window!")  
        self.last_input="keyboard"
        try:
            pressed_button='{0}'.format(event.char)
            print(pressed_button)
            
            if self.keyboard_and_mouse_press_and_time_list:
                if pressed_button=="]":
                     print("loop-ender")
                     self.keyboard_and_mouse_press_and_time_list.append(["loop_ender","loop_ender",time.time()])
                     return
                if pressed_button=="=": #can't loop on the first click 
                     print("wait_till_image_gone") # save screenshot when this button is clicked
                     screenshot_name=self.take_screenshot_and_grab_text()
                     self.keyboard_and_mouse_press_and_time_list.append(["template_creator",[screenshot_name,"wait_till_image_gone"],time.time()])
                     return
                if pressed_button==";":# wait till see image and click
                    print("wait_till_image_present") # save screenshot when this button is clicked
                    screenshot_name=self.take_screenshot_and_grab_text()
                    self.keyboard_and_mouse_press_and_time_list.append(["template_creator",[screenshot_name,"wait_till_image_present"],time.time()])
                    print(self.keyboard_and_mouse_press_and_time_list)
                    return
                if pressed_button=="`": #can't loop on the first click 
                     print("loop")
                     if self.for_loop==True:
                         self.keyboard_and_mouse_press_and_time_list.append(["end_for_loop","end_for_loop",time.time()])
                         self.for_loop=False
                         print(self.keyboard_and_mouse_press_and_time_list)
                         return
                     if self.for_loop !=True:
                         self.keyboard_and_mouse_press_and_time_list.append(["start_for_loop","start_for_loop",time.time()])
                         self.for_loop=True
                         print(self.keyboard_and_mouse_press_and_time_list)
                         return 
                if pressed_button ==",": #can't loop on the first click 
                     print("take a regular screenshot")
                     self.keyboard_and_mouse_press_and_time_list.append(["keyboard","take_screenshot_and_grab_text",time.time()])
                     return     
                last_keyboard_or_mouse_press=self.keyboard_and_mouse_press_and_time_list[-1][0]
                #print(f"last key board or mouse press:{last_keyboard_or_mouse_press}")
                last_value=self.keyboard_and_mouse_press_and_time_list[-1][1] 
                if self.ctrl_activated==True and pressed_button=="a": # for control a
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_a",time.time()])   
                    return
                if self.ctrl_activated==True and pressed_button=="c":# for control c
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_c",time.time()])
                    return
                if last_keyboard_or_mouse_press=="keyboard" and self.ctrl_activated==False:# last press was keyboard and not control
                    if last_value in self.ctrl_command_list:# to stop a write command
                        self.keyboard_and_mouse_press_and_time_list.append(["keyboard",'{0}'.format(event.char),time.time()])   
                    if last_value not in self.ctrl_command_list: # to continue a  write command
                        self.keyboard_and_mouse_press_and_time_list[-1][1]+='{0}'.format(event.char)        
                if last_keyboard_or_mouse_press=="keyboard": # last press was mouse
                    return
                
                
                else:
                    # fixing keyboard
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard",'{0}'.format(event.char),time.time()]) 

                # might need to redo this
                    #print('{0}'.format(event.char))
                    #print('MEOW')
                self.ctrl_activated=False     
            else:# first value in list_list
                if pressed_button=="`": #can't loop on the first click 
                     print("loop")
                     if self.for_loop==True:
                         self.keyboard_and_mouse_press_and_time_list.append(["keyboard","end_for_loop",time.time()])
                         self.for_loop=False  
                         return
                     if self.for_loop !=True:
                         self.keyboard_and_mouse_press_and_time_list.append(["keyboard","start_for_loop",time.time()])
                         self.for_loop=True
                         return
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard",'{0}'.format(event.char),time.time()])
            print('keyboard key pressed is:{0}'.format(event.char))
        except AttributeError:
            print(str('{0}'.format(event)))
                  
            if str('{0}'.format(event))=="Key.enter":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","enter",time.time()]) 
                print('enter!')
                return
            if str('{0}'.format(event))=="Key.ctrl_l":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl",time.time()]) 
                self.ctrl_activated=True
                print('ctrl_activated')
                return
            #if str('{0}'.format(event))=="Key.alt_l":
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","alt",time.time()]) 
            #    print('alt!')
            #    return
            #if str('{0}'.format(event))=="Key.tab":
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","tab",time.time()]) 
            #    print('alt!')
            #    return
            #if str('{0}'.format(event))=="Key.backspace":
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","backspace",time.time()]) 
            #    print('alt!')
            #    return
            #f_search=re.search(r"Key.(f.*)",str('{0}'.format(event)))
            #if f_search:
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard",f_search.group(1),time.time()]) 
            #    print('f pressed')


                
    def keyboard_pynput_release(self,event):
        from pynput import keyboard
        listt=[]
        if event == keyboard.Key.num_lock:
            self.mouse_listener.stop()
            self.window.destroy()
            
            return False  #press shift to Stop listener
        
        
    def generate_problem_text(self):
        """use information from key strokes to generate this and other context saved in dictionary related to pyautogui """
        
    def generate_end_states(self):
        """ """
    def generate_question(self):
         """ """
    def generate_tools(self):
        """ """
    def generate_problem_environment(self):
        """ """
        
    def generate_effects(self):
        """ """
        self.problem_tree_dictionary.append()
        
    def suggest_based_on_context_similar_problems(self):
        """ this will run automatically tied in both the coding program and problem solving program"""
        #uses the info in he problem dic to look throigh 
        #database of past problems and suggest the cloest problem you have done 
        #before like what you are doing
        #now and allows you to access this information
        
    def upload_results_to_coding_program_and_problem_solving_program_3d_program_law_program(self):
        """ """
        problem_solving_program_dic=self.generate_problem_solving_program_data()
        self.upload_data_to_problem_solving_program_window(problem_solving_program_dic)
        
    def generate_and_upload_data_from_copilot(self,prompt_list):
        """ """
        import sys
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files')
        from pyautogui_functions import pyautogui_functions
        my_pyauto_gui=pyautogui_functions()
        self.open_website_page_for_autogui(r"https://copilot.microsoft.com/")
        prompt_data=my_pyauto_gui.pyauto_gui_function0(prompt_list)  
        return prompt_data
        data=self.get_clipboard_data()
        self.send_text_to_server(data) # or send text to database
    def generate_and_upload_data_from_chatgpt(self,pyautogui_script_to_run):
         """ """
         import sys
         prompt_list=["hello world","meow"]
         sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files')
         from pyautogui_functions import pyautogui_functions
         my_pyauto_gui=pyautogui_functions()
         self.open_website_page_for_autogui()
         my_pyauto_gui.pyauto_gui_function0(prompt_list) #max 4 
         data=self.get_clipboard_data()
         self.send_text_to_server(data) # or send text to database
    def create_pyautogui_file_of_inputs_and_video(self):
        """ this will output the pyautogui file of the session we wanted to record  """
        strr_for_py_auto_function_split_lines=self.create_pyauto_gui_function_str(self.keyboard_and_mouse_press_and_time_list)
        python_file_dic=self.construct_python_file_dic(strr_for_py_auto_function_split_lines)
        python_file_str=self.write_a_python_file_str(python_file_dic)
        code_file_name=self.script_folder_name+r"pyautogui_functions.py"
        self.add_to_or_create_new_python_file(python_file_str,code_file_name)
    

class pyautogui_for_generative_model_access_functions_gchild(pyautogui_for_generative_model_access_functions_child):
    def __init___(self):
        """ """
        import pyautogui
        self.screen_size=pyautogui.size()
        self.screen_height=self.screen_size[1]
        self.screen_width=self.screen_size[0]
    # build more programs as needed add them like this
    def find_code_from_screen_shot(self):
        """ """
        # locate coding file was working on using os
        # locate code in screen shot
        # use to make suggestions on next steps using the coding program
        # and to construct a problem tree and 
        # suggest code edits
        # using some generative model if possible
        # use screenshot to pin point code?
    
    
    def generate_and_store_problem_solving_program_data(self):
        """ """
        self.generate_column
        
        table_name="problem_solving_tree"
        dicitonary_of_values={"template_paths":template_paths,
        "code_file_name_paths":code_file_name_paths,# only if it is a coding file otherwise just paste the active frame
        "code_found_on_screen_per_click":code_found_on_screen_per_click,
        "text_found_on_screen_per_click":text_found_on_screen_per_click,
        "key_board_presses_per_click":key_board_presses_per_click,
        "problem_name":problem_name,# use contexual informationfor this from screenshot and the above rows
        "time_stamps":time_stamps,
        "active_windows_per_click":active_windows_per_click,
        "date":date,
        "visual_of_problem_environment_paths":visual_of_problem_environment_paths,#same one we have been generating
        "visual_of_problem_tree_paths":visual_of_problem_tree_paths,# dag
        "strategies":strategies,#ask how to a generative model?
        "actions":actions,#ask how to a generative model?
        "tools":tools,
        "questions":questions,
        "effects":effects,
        "end_state":end_state,
        "problem_web":problem_web# dicitonary 
        }
        self.store_value_in_sql_table(problem_solving_program_dic,table_name)
        # use problem solving data and integrate into different gui programs or website
        # to display and access the results
        
    def generate_and_store_coding_problem_solving_program_data(self):
        """ """
        screen_shot_paths=self.generate_screen_shot_paths()
        template_paths=self.generate_template_paths()
        code_file_name_paths=self.generate_code_file_name_paths()
        code_found_on_screen_per_click=self.generate_code_found_on_screen_per_click()
        found_on_screen_per_click=self.generate_text_found_on_screen_per_click()
        key_board_presses_per_click=self.generate_key_board_presses_per_click()
        problem_name=self.generate_problem_name()
        time_stamps=self.generate_time_stamps()
        active_windows_per_click=self.generate_active_windows_per_click()
        date=self.generate_date()
        visual_of_problem_environment_paths=self.generate_visual_of_problem_environment_paths()
        visual_of_problem_tree_paths=self.generate_visual_of_problem_tree_paths()
        strategies=self.generate_strategies()
        actions=self.generate_actions()
        tools=self.generate_tools()
        questions=self.generate_questions()
        effects=self.generate_effects()
        end_state=self.generate_end_state()
        problem_web=self.generate_problem_web()




        table_name="coding_problem_solving_tree"
        dicitonary_of_values={"screen_shot_paths":screen_shot_paths,
         "template_paths":template_paths,
         "code_file_name_paths":code_file_name_paths,# only if it is a coding file otherwise just paste the active frame
         "code_found_on_screen_per_click":code_found_on_screen_per_click,
         "text_found_on_screen_per_click":text_found_on_screen_per_click,
         "key_board_presses_per_click":key_board_presses_per_click,
         "problem_name":problem_name,# use contexual informationfor this from screenshot and the above rows
         "time_stamps":time_stamps,
         "active_windows_per_click":active_windows_per_click,
         "date":date,
         "visual_of_problem_environment_paths":visual_of_problem_environment_paths,#same one we have been generating
         "visual_of_problem_tree_paths":visual_of_problem_tree_paths,# dag
         "strategies":strategies,#ask how to a generative model?
         "actions":actions,#ask how to a generative model?
         "tools":tools,
         "questions":questions,
         "effects":effects,
         "end_state":end_state,
         "problem_web":problem_web# dicitonary 
         }
        self.store_value_in_sql_table(dicitonary_of_values,table_name)
        # use problem solving data and integrate into different gui programs or website

        
    def generate_and_store_3d_problem_solving_program_data(self):
        """ """
        table_name="three_d_problem_solving_tree"
        dicitonary_of_values={"template_paths":template_paths,
        "code_file_name_paths":code_file_name_paths,# only if it is a coding file otherwise just paste the active frame
        "code_found_on_screen_per_click":code_found_on_screen_per_click,
        "text_found_on_screen_per_click":text_found_on_screen_per_click,
        "key_board_presses_per_click":key_board_presses_per_click,
        "problem_name":problem_name,# use contexual informationfor this from screenshot and the above rows
        "time_stamps":time_stamps,
        "active_windows_per_click":active_windows_per_click,
        "date":date,
        "visual_of_problem_environment_paths":visual_of_problem_environment_paths,#same one we have been generating
        "visual_of_problem_tree_paths":visual_of_problem_tree_paths,# dag
        "strategies":strategies,#ask how to a generative model?
        "actions":actions,#ask how to a generative model?
        "tools":tools,
        "questions":questions,
        "effects":effects,
        "end_state":end_state,
        "problem_web":problem_web# dicitonary 
        }
            
           
        self.store_value_in_sql_table(dicitonary_of_values,table_name)
        # use problem solving data and integrate into different gui programs or website

        
    def generate_and_store_law_problem_solving_program_data(self):
        """ """
        table_name="legal_problem_solving_tree"
        dicitonary_of_values={"template_paths":template_paths,
        "code_file_name_paths":code_file_name_paths,# only if it is a coding file otherwise just paste the active frame
        "code_found_on_screen_per_click":code_found_on_screen_per_click,
        "text_found_on_screen_per_click":text_found_on_screen_per_click,
        "key_board_presses_per_click":key_board_presses_per_click,
        "problem_name":problem_name,# use contexual informationfor this from screenshot and the above rows
        "time_stamps":time_stamps,
        "active_windows_per_click":active_windows_per_click,
        "date":date,
        "visual_of_problem_environment_paths":visual_of_problem_environment_paths,#same one we have been generating
        "visual_of_problem_tree_paths":visual_of_problem_tree_paths,# dag
        "strategies":strategies,#ask how to a generative model?
        "actions":actions,#ask how to a generative model?
        "tools":tools,
        "questions":questions,
        "effects":effects,
        "end_state":end_state,
        "problem_web":problem_web# dicitonary 
        }
        self.store_value_in_sql_table(dicitonary_of_values,table_name)
        # use problem solving data and integrate into different gui programs or website

        
        
        
        
    def init_glossary_window(self):
        """ """
        self.init_gui_window()
        self.init_frames()
        self.init_text_box()
   
    def init_pyauto_gui_creation_script_program(self):
        """ """
        from pynput import keyboard
        from pynput import mouse
        import time
        import os
        import logging
        from pynput.mouse import Listener
        from multiprocessing import Queue, Process
        
        self.keyboard_and_mouse_press_and_time_list=[]
        self.ctrl_command_list=["ctrl_c","ctrl_a"]
        self.ctrl_activated=False
        self.for_loop=False
        self.while_loop=False
        self.last_input=None
        self.previous_active_window_name=""
        self.init_glossary_window()
        with  keyboard.Listener(on_press=self.keyboard_on_press_pynput, on_release=self.keyboard_pynput_release) as self.keyboard_listener:
            self.mouse_listener = mouse.Listener(on_click=self.mouse_pynput_on_click,on_scroll=self.on_mouse_scroll,on_move=self.on_mouse_move)
            self.mouse_listener.start()
            self.window.mainloop()# program will end here
            self.mouse_listener.stop()
            
        

            
       
            
        # constantly be checking for the active window
        
        # then use this information to help build downstream application
        
        
        

            #if event == keyboard.Key.num_lock:
            #    self.window.destroy()
            #try: 
            #    self.keyboard_listener.join()
                

            #except Exception as e:
            #         print(e)
            #         print('Done'.format(e.args[0]))
