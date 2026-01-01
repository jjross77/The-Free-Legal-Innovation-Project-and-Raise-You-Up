# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:52:29 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
import tkinter as tk
class pyautogui_for_generative_model_access_functions():
    
    def __init___(self):
        """# start xdotools and get pyautogui to work
        export DISPLAY=:0 # use this to set display FIXES ERROR IT SEEMS  
        touch ~/.Xauthority
        ls -l ~/.Xauthority# check permissions
        chmod 600 ~/.Xauthority
        xdotool mousemove 100 200  """
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
To move the cursor to a position without clicking  press  “[”
To create a loop press . “`”
To end loop also press : “`”
To wait till image gone:"="
To wait till image present press in the top left 
and bottom right corrner of screenshot: ";"
To take a screen shot press: “,”
To open a new webbrowser screen press: “/”
pressing shift will produce shift tab:"shift"
process text in clipboard with re : "."
ctrl c in script to skip to next command or click

To save script press Esc
use keybaord asmuch as possilbe for as little errors as possible from screenshots or misclicks
click in positions on buttons where content wont change on part of the screen
 because a different types input for example when inputting email information make sure dont include this in screenshot so click to other side of button so this changing content wont be displayed and wont make program fail
need to hover over buttons so get correct screenshot if they change color or change time.sleep
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
        #active_window_url=self.find_url_in_image(path_to_frame,active_window_name)
        return path_to_frame,active_window_name,spacing_to_add
    
    ###### this is a problem we need to solve

    
    # action 1 create button to open a fresh screen to email being used as recovery
    # just add webrowser function to code to open webrowser
    # add this as a button and the function etc
    # screenshots cant be relied on here
    
    #action 2 create button to open correct email and extact the code and get it to clipboard
    # screenshot?
    # find location of proper email
    # use position and text of email to locate it
    # note cursor position and make sure that it is within a certain
    # radius of where the cursor was clicked on the screen
    # add this to make sure if multiple of same button clicks the
    # correct one
    # button not in area specified then dont click it
    #maybe just add this to normal button
    
    
    # action 3 create button to extract code
    # take a screenshot of the email process text in the email and then
    
    
    

    # action 4 create button to bring back to screen where need to paste code
    # fix ctrl c and ctrl v 
    
    
    
    def mini_screen_scroll(self,pressed_x_position,pressed_y_position,released_y_position):
        """scroll the length and direction between the  mouse press and mouse release """
        amount_to_scroll=int(pressed_y_position)-int(released_y_position)
        drag_to_command=f"\npyautogui.moveTo({pressed_x_position}, {pressed_y_position})\ntime.sleep(1)\n  pyautogui.scroll({amount_to_scroll})"
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
    def get_chrome_history(self):
        # Path to Chrome's history database on Windows
        import os
        import sqlite3
        import shutil
        import platform
        import pandas as pd
        history_db = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")

        # Check if the database file exists
        if not os.path.exists(history_db):
            print("Chrome's history database not found.")
            return None

        # Establish a connection to the database
        conn = sqlite3.connect(history_db)

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query to retrieve browsing history
        cursor.execute("""
            SELECT 
                urls.title, 
                urls.url, 
                visits.visit_time
            FROM 
                urls 
            LEFT JOIN 
                visits ON urls.id = visits.url
            ORDER BY 
                visits.visit_time DESC
        """)

        # Fetch all rows from the query
        rows = cursor.fetchall()

        # Close the connection
        conn.close()

        # Convert the result to a Pandas DataFrame (optional)
        df = pd.DataFrame(rows, columns=["Title", "URL", "Visit Time"])

        return df
        
    
    def get_firefox_history(self):
        # Determine the platform and set the path for the Firefox history database
        import os
        import sqlite3
        import shutil
        import platform
        if platform.system() == "Windows":
            firefox_profile_path = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
        elif platform.system() == "Darwin":  # macOS
            firefox_profile_path = os.path.join(os.getenv('HOME'), 'Library', 'Application Support', 'Firefox', 'Profiles')
        elif platform.system() == "Linux":
            firefox_profile_path = os.path.join(os.getenv('HOME'), '.mozilla', 'firefox')

        # Get the first profile folder in the Firefox profiles directory
        profiles = [f for f in os.listdir(firefox_profile_path) if f.endswith('.default-release') or f.endswith('.default')]
        if not profiles:
            print("Firefox profile not found!")
            return None
        
        profile_path = os.path.join(firefox_profile_path, profiles[0], 'places.sqlite')

        # Ensure the Firefox places.sqlite file exists
        if not os.path.exists(profile_path):
            #print("Firefox history file not found!")
            return None
        
        # Connect to the database and query history
        connection = sqlite3.connect(profile_path)
        cursor = connection.cursor()
        
        query = "SELECT url, title, visit_count, last_visit_date FROM moz_places ORDER BY last_visit_date DESC LIMIT 10"
        cursor.execute(query)
        history = cursor.fetchall()
        
        connection.close()

        return history
    def get_active_url_name_from_browsers_history(self):
        #chrome_histroy=self.get_chrome_history()
        import re
        firefox_history = self.get_firefox_history()
        history_file_counter_list=[]
        unwanted_item_list=["","mozilla","firefox","—"]
        #print(chrome_histroy)
        #print(firefox_history)
        #print("\nFirefox History:")
        lowered_active_window_name=self.active_window_name.lower()
        lowered_active_window_name=re.sub(r"-","",lowered_active_window_name)
        # remove moizzla google from name and empty spaces, mozilla,firefox,empty space
        #print(f"ACTIVE WINDOW NAME: {lowered_active_window_name}")
        
        lowered_active_window_name_word_list=lowered_active_window_name.split(" ")
        #print(lowered_active_window_name_word_list)
        for unwanted_item in unwanted_item_list:
            if unwanted_item in lowered_active_window_name_word_list:
                lowered_active_window_name_word_list.remove(unwanted_item)
        #print('AFER')
        #print(lowered_active_window_name_word_list)
        if firefox_history:
            #print('firefox history')
            for history_link in firefox_history:
                history_link=history_link[0]
                history_link=history_link.lower()
                #print(history_link)
                #print(lowered_active_window_name_word_list)
                counterr=0
                for wordd in lowered_active_window_name_word_list:
                    if wordd in history_link:
                        counterr+=1
                #print(f"counterr {counterr}")
                history_file_counter_list.append(counterr) 
            max_value_in_counter_list=max(history_file_counter_list)
            highest_counter_index=history_file_counter_list.index(max_value_in_counter_list)
            highest_counted_website=firefox_history[highest_counter_index]
            #print(f"HIGHEST WEBPAGE: {highest_counted_website}")
            return highest_counted_website
        return "could not find file histry"    
        

           
          
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
        drag_to_command=f"\npyautogui.moveTo({pressed_x_position}, {pressed_y_position})\ntime.sleep(1)\n  pyautogui.scroll({amount_to_scroll})"
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
        strr_for_py_auto_script+="""
  import pyautogui
  import time
  from PIL import ImageGrab
  import numpy as np
  import pytesseract
  platformm=os.name
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  saved_screen_shots_text_list=[]"""
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
    def create_template_mouse_click(self,keyy,timee,path_to_frame,folder_name,box_size=20):
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
        # make this saved in the folder
        template_location_str_windows=folder_name+f"\\template{timee}.png"
        #linux_folder=r"/home/username/Documents/pyautogui/"
        #self.dir_to_store_script_linux
        #screenshot name
        ####
        #folder name
        template_location_str_linux=self.dir_to_store_script_linux+f"/template{timee}.png"

        
        img_template.save(template_location_str_windows) 
        return template_location_str_windows,template_location_str_linux
    

        
    def add_mouse_click(self,strr_for_py_auto_script,keyy,keyboard_or_mouse,timee,path_to_frame,active_window_name,folder_name,remote=False):
        """ create template from screenshot and then add as a mouse click to gui"""
        import re
        if keyboard_or_mouse=="mouse_press_l" or keyboard_or_mouse=="mouse_press_r" :
            if remote==True:
                #print('add something different')
                #print('hi')
                top_left_mouse_click=re.search(r"\(\d+, \d+\)",keyy).group(0) 
                mouse_cordinate_split=re.search("(\d+), (\d+)",top_left_mouse_click)
                x=int(mouse_cordinate_split.group(1))
                y=int(mouse_cordinate_split.group(2))
                strr_for_py_auto_script+="\n  "+fr"print('replace mouse click next two lines with screenshot code using down stream function')"
                strr_for_py_auto_script+="\n  "+fr"print('{active_window_name}')"
                strr_for_py_auto_script+=f"\n  self.pyautogui_click_function({x},{y},current_screen_height,current_screen_width,og_screen_height,og_screen_width) "# need to scale x and  y correctly
                strr_for_py_auto_script+="\n  "+fr"print('add in screenshot')"
                # wuill need to scale mouse clicks to screen size """
             
                #take the screenshot instead
            if remote==False:
                print('hi')
                self.template_location_str,self.template_location_str_linux=self.create_template_mouse_click(keyy,timee,path_to_frame,folder_name)
                strr_for_py_auto_script+="\n  "+fr"print('{active_window_name}')"
                strr_for_py_auto_script+=f"""\n  if platformm=='nt':
       self.wait_till_template_present(r'{self.template_location_str}')
      else:# linux
       self.wait_till_template_present(r'{self.template_location_str_linux}') """
                #strr_for_py_auto_script+=f"\n  self.wait_till_template_present(r'{self.template_location_str}')\n"# modify template location str
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
        template_location_str_linux=self.dir_to_store_script_linux+ +f"template{time_stamp_of_screenshot}.png"
        ####
        #template_location_str=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template{time_stamp_of_screenshot}.png"
        img_template.save(template_location_str) 
        return template_location_str,template_location_str_linux
    
  
    
    def create_new_autogui_file(self,strr_for_py_auto_script,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux):
        """ """
        import pyautogui
        # get laptop screensize
        #get current screen size
        self.screen_size=pyautogui.size()
        
        og_screen_size=[self.screen_height,self.screen_width]       
        strr_for_py_auto_script=r"# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy"
        strr_for_py_auto_script+="\nclass pyautogui_functions():"
        strr_for_py_auto_script+="\n def __init__(self):"
        strr_for_py_auto_script+="\n  print('start_pyautogui_class')"
        strr_for_py_auto_script+="\n def pyauto_gui_function0(self):"
        # will need to check this
        strr_for_py_auto_script+=f"""\n  import os
  code_file_name_path_linux='{code_file_name_path_linux}'
  code_file_name_only='{code_file_name_only}'
  self.keyboard_and_mouse_press_and_time_list=[]
  previous_active_window='{previous_active_window}'
  os.environ['DISPLAY'] = ':0'
  import pyautogui
  current_screen_size=pyautogui.size()
  og_screen_height={self.screen_size[1]}
  og_screen_width={self.screen_size[0]}#laptop
  og_screen_height=current_screen_size[0]
  og_screen_width=current_screen_size[1]
  self.screen_size=pyautogui.size()
  current_screen_height=self.screen_size[1]
  current_screen_width=self.screen_size[0]
  # calcuate scale factor
  # just scale pixels?
  
  #current_screen_size=[self.screen_height,self.screen_width]
  
  
  """
        strr_for_py_auto_script+=f"\n  import webbrowser"
        strr_for_py_auto_script+=f"\n  link=r'{previous_active_window_url[0]}'"
        strr_for_py_auto_script+=f"\n  webbrowser.get('firefox').open(link)"
        #strr_for_py_auto_script+=f"\n  self.open_website_page_for_autogui(link)"
        #strr_for_py_auto_script+=f"\n  edge_path= r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'"
        
       # strr_for_py_auto_script+=f"\n  #webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))"
       # strr_for_py_auto_script+=f"\n  #webbrowser.get('edge').open('http://www.google.com')"

        return strr_for_py_auto_script
    # need to change how this is strcutred so if seperatge into there own seperate folders for each script
    def add_remote_mouse_click(self):
        """ """
        

    def create_pyauto_gui_function_str(self,keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux,add_additional_functions=["check_for_template(self"],remote=False):
        """ Use info generated from  mouse clicks to create a function for pyautogui """
        import re
        import os
        import pyautogui
        self.screen_size=pyautogui.size()
        self.screen_height=self.screen_size[1]
        self.screen_width=self.screen_size[0]
        dictionary_of_keyys={"start_for_loop":f"\n  for prompt in prompt_list:",
                             "end_for_loop":f"\n  continue",
                             #"ctrl_c":f"\npyautogui.hotkey('ctrl', 'c')",
                             #"ctrl":f"\npyautogui.hotkey('ctrl', 'c')",# assume control c can manually change tyo control a
                             "take_screenshot_and_grab_text":f"\n  screenshot = ImageGrab.grab()\nimg1 = np.array(screenshot)\ntext = pytesseract.image_to_string(img1)\nsaved_screen_shots_text_list.append(text)",
                             #"ctrl_a":f"\npyautogui.hotkey('ctrl', 'a')",
                             "enter":f"\n  pyautogui.press('enter')",
                             "alt":f"\n  pyautogui.hotkey('alt', 'tab')",# dont think i need alt tab
                             "backspace":f"\n  pyautogui.press('backspace')",
                             "loop_ender":f"\n  print('loop_ender')\nend_the_loop",                            
                             "DOWN":f"\n  pyautogui.press('down')",
                             "UP":f"\n  pyautogui.press('up')",
                             "LEFT":f"\n  pyautogui.press('left')",
                             "RIGHT":f"\n  pyautogui.press('right')",
                             "tab":f"\n  pyautogui.hotkey('tab')",                             
                             "ctrl_c":f"\n  pyautogui.hotkey('ctrl', 'c')",
                             "ctrl_a":f"\n  pyautogui.hotkey('ctrl', 'a')",
                             "ctrl_p":f"\n  pyautogui.hotkey('ctrl', 'p')",
                             "ctrl_s":f"\n  pyautogui.hotkey('ctrl', 's')",
                             "F12":f"\n  pyautogui.hotkey('f12')",
                             "open_new_internet_window":f"\n  webbrowser.open(link)",
                             "grab_text_add_to_clipboard":f"\n  self.grab_text_from_clipboard_re_search_and_add_text_to_clipboard(re_pattern=r'\d\d\d\d\d\d')",
                             "shift":"\n  pyautogui.hotkey('shift', 'tab')"}
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
        strr_for_py_auto_script=self.create_new_autogui_file(strr_for_py_auto_script,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux)  
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
                strr_for_py_auto_script+=f"\n  time.sleep({time_change})"

            # add this as time to sleep
            if keyboard_or_mouse=="template_creator":
                strr_for_py_auto_script+=f"\n  print('{keyboard_or_mouse} {i}')"
                screen_shot_name=keyy[0]
                screen_shot_command=keyy[1]
                # grab the four mouse clicks after
                top_left_mouse_click=keyboard_and_mouse_press_and_time_list[i+1][1]
                bottom_right_mouse_click=keyboard_and_mouse_press_and_time_list[i+3][1]
                # need to figure out how to do this one
                self.template_location_str,self.template_location_str_linux=self.create_template_screenshot(screen_shot_name,top_left_mouse_click,bottom_right_mouse_click,folder_name=self.dir_to_store_script)# creating template in past time
                if screen_shot_command=="wait_till_image_gone":
                    strr_for_py_auto_script+=f"\n  self.wait_till_template_gone(r'{self.template_location_str}')"
                if screen_shot_command=="wait_till_image_present":
                    # having setting for if windows one option is linux other option
                   strr_for_py_auto_script+="""  if platformm=='nt':
   self.wait_till_template_present(r'{self.template_location_str}')
  else:# linux
      self.wait_till_template_present(r'{self.template_location_str_linux}') """
      
                    #strr_for_py_auto_script+=f"\n  self.wait_till_template_present(r'{self.template_location_str}')\n"# modify template location str    
                    #strr_for_py_auto_script+=f"\n  self.wait_till_template_present(r'{self.template_location_str}')\n"# modify template location str
                    #strr_for_py_auto_script+=f"\n  self.wait_till_template_present(r'{self.template_location_str}')\n"# modify template location str
                self.block_four_clicks_switch=True
                continue
            if keyy in keys_to_look_for:
                strr_for_py_auto_script+=f"\n  print('{keyy}: {i}')"
                strr_for_py_auto_script+=dictionary_of_keyys[keyy]
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                #if i==len(keyboard_and_mouse_press_and_time_list)-1:
                #    strr_for_py_auto_script+=f"\n  return saved_screen_shots_text_list"     
                continue
            #if keyboard_or_mouse=="loop_ender":
            #    strr_for_py_auto_script+=f"\nprint('{keyy}: {i}')"
            #    strr_for_py_auto_script+=f"\nend_the_loop"
            #    continue
        
            if keyboard_or_mouse=='move_cursor':# test if this works
               x_position,y_position=keyboard_and_mouse_press_and_time[3]
               strr_for_py_auto_script+=f"\npyautogui.moveTo{x_position,y_position}"
               continue
                
            if keyboard_or_mouse=="keyboard":
                strr_for_py_auto_script+=f"\n  print('{keyy}: {i}')"
                strr_for_py_auto_script+=f"\n  pyautogui.write({keyy})" 
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                #if i==len(keyboard_and_mouse_press_and_time_list)-1:# trying to find a place to put return statement
                #    strr_for_py_auto_script+=f"\n  return saved_screen_shots_text_list"  
                continue
            ### MOUSE STUFF
            # need to modify what is added for left mouse click using info i gathered
            if keyboard_or_mouse=="mouse_press_l" or keyboard_or_mouse=="mouse_press_r":
                path_to_frame=keyboard_and_mouse_press_and_time[3]
                active_window_name=keyboard_and_mouse_press_and_time[4]
                spacing_to_add=keyboard_and_mouse_press_and_time[5]
                strr_for_py_auto_script+=spacing_to_add
                
                if keyboard_or_mouse=="mouse_press_l":
                    strr_for_py_auto_script+=f"\n  print('{keyy}: {i}')"
                    if remote==True:
                        # regenerate keyboard_mouse_press time list with script
                        # to run through again?
                        #what is the best way to do this
                        # want to generate another list of mouse releases
                        # to generate a normal script
                        # from running the script remotely
                        # to process through this function again
                        # use remote add_mouse_click_to_take_screenshot etc
                        # how do i do this
                        # want to add that it should run the script
                        # get all the necessary screenshots
                        # and replace the clicks with the screenshots in a new script
                        # generate new script as we go?
                        # can you run 
                        #pynput to record pyautogui? Does not work keep it simple stupid
                        # use screenshots
                        # so add to pyautogui after click some logic
                        # to write the screenshots to another script
                        # replacing the clicks
                        # with the screenshots
                        # so run the pynput script while this is running 
                        # to generate another script once it is done
                        # simply add the sa
                        # figure out way to do this
                        # so record screenshot info somewhere
                        # then modify existing script replacing 
                        # the mouse presses we have done here
                        # by marking them with the correct screenshot presses
                        # how do we replace the click with screenshots in a new script
                        # add a function at end of the script generated here
                        # that will create the other script by reading over this script
                        # and retreiving screenshot info taken when this script executed
                        # and subsistuting the add mouse clicks here with proepr screenshots
                        # then forward this script to server database so can execute proper one later
                        
                        
                        strr_for_py_auto_script= self.add_mouse_click(strr_for_py_auto_script,keyy,keyboard_or_mouse,timee,path_to_frame,active_window_name,self.dir_to_store_script,remote=True)

                    if remote==False:
                        strr_for_py_auto_script= self.add_mouse_click(strr_for_py_auto_script,keyy,keyboard_or_mouse,timee,path_to_frame,active_window_name,self.dir_to_store_script)

                        
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                #if i==len(keyboard_and_mouse_press_and_time_list)-1:# trying to find a place to put return statement
                #    strr_for_py_auto_script+=f"\n  return saved_screen_shots_text_list"
                continue
            ## THESE ARE LEFT
            if keyboard_or_mouse=="mouse_move":
                self.move_to_list_counterr+=1
                stored_mouse_move_list_items=keyboard_and_mouse_press_and_time[3]
                strr_for_py_auto_script+=f"""
  move_to_list{self.move_to_list_counterr}={stored_mouse_move_list_items}
  self.move_mousey(move_to_list{self.move_to_list_counterr})"""
                #strr_for_py_auto_script+=f"\nmove_to_list{self.move_to_list_counterr}={stored_mouse_move_list_items}\nfor x_y_positions_list in move_to_list{self.move_to_list_counterr}:\npyautogui.moveTo(x_y_positions_list[0],x_y_positions_list[1])"
                continue 
            
            if keyboard_or_mouse=="mouse_scroll":
                amount_to_scroll=keyboard_and_mouse_press_and_time[3]
                mouse_cordinates=re.search(r"\(\d+, \d+\)",keyy).group(0) 
                mouse_cordinate_split=re.search("(\d+), (\d+)",mouse_cordinates)
                x=int(mouse_cordinate_split.group(1))
                y=int(mouse_cordinate_split.group(2))
                strr_for_py_auto_script+=f"\n  pyautogui.moveTo({x}, {y})\n  pyautogui.scroll({amount_to_scroll})"
                continue
            
        
        if remote==False:
              strr_for_py_auto_script+="""
#if want to use this page data do the following commands otherwise skip this
   pyautogui.hotkey('f12')
   time.sleep(0.5)
   pyautogui.write('const  txt  = document.documentElement.outerHTML;',interval=0.05)
   pyautogui.hotkey('enter')
   pyautogui.write('copy(  txt);',interval=0.05)
   pyautogui.hotkey('enter')  
   prompt=''  
   self.process_clipboard_and_send_data_to_other_computer(prompt,link)     
              """
              strr_for_py_auto_script=self.add_function_str_from_sql_to_file(column_list,strr_for_py_auto_script)

        if remote==True:
              strr_for_py_auto_script+="""
   #if want to use this page data do the following commands otherwise skip this
  #host=sys.argv[1]
  self.create_new_script_with_screen_shots_and_send_to_server(previous_active_window,code_file_name_path_linux)     
              """
              # need to modify this to add that other function file nstead here 
              # so we dont do this stupid formating anymore
              # lets do it
              strr_for_py_auto_script=self.add_function_str_from_sql_to_file(column_list,strr_for_py_auto_script,remote=True)                   

        #for function_name in add_additional_functions:
        #    function_name=re.sub("\(","\\(",function_name)
        #    function_name=re.sub("\)","\\)",function_name) # will need to test to see if this works
        #    function_result=re.search(function_name,strr_for_py_auto_script)
        #    if function_result:
        #        print("FOUND")
        #        continue
        #    else:
        #        print("NOT FOUND")
                
                    
                
                #pyautogui.hotkey('f12')
                #pyautogui.sendkeys('const txt = document.documentElement.outerHTML;')
                #pyautogui.hotkey('f12')
                #pyautogui.sendkeys(' copy(txt); ')
                #pyautogui.hotkey('enter')
                #pyautogui.sendkeys('txt')
                #pyautogui.hotkey('enter')            
                #const txt = document.documentElement.outerHTML;

                
              #  continue
        #strr_for_py_auto_function_split_lines=strr_for_py_auto_script.splitlines()
        return strr_for_py_auto_script
    
    
    
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
    
    def send_post_request_to_django(self,post_data_dic):
        """ use postgres maybe"""
        import requests
        post_data = {'name': 'Gladys'}
        response = requests.post('http://example.com', data=post_data_dic)
        content = response.content

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
        with open(f"{code_file_name}","w" ,encoding="utf-8") as f2:
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
    def add_function_str_from_sql_to_file(self,column_list,strr_for_py_auto_script,remote=False):
        """upload the function to the strring for pyautogui make tab logic not apply to this
        change this to just import functions as a class from another file?"""
        #print(search_data_dic)
        # TEMPOARILY JUST GOING TO SCTAP THIS fix it if we need to make it more diverse by fixing search funciton in glossary program
        if remote ==True:
            file_name=r"C:/Users/yyyyyyyyyyyyyyyyyyyy/Documents/Coding/automating_coding/pyautogui_for_generative_model_access a1.1.1.1.1.1/pyautogui_script_functions_remote.py"
            with open(file_name,"r") as f:
                coding_file=f.read()
                #parse file_str
                python_script_split_lines=coding_file.splitlines()
                python_script_split_lines=python_script_split_lines[9:]# removed unwanted part
                for line_number,line in enumerate(python_script_split_lines):
                    strr_for_py_auto_script+=f"\n{line}"    
                return strr_for_py_auto_script 
        strr_for_py_auto_script+=r"""
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
  return location_of_template,h, w """
        
        strr_for_py_auto_script+="""
 def scroll_up_whole_page(self):
  import pyautogui
  for i in range(30):
   pyautogui.moveTo(1919, 212)
   pyautogui.scroll(1000) """
        strr_for_py_auto_script+=r"""
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
    continue """
        strr_for_py_auto_script+=r"""
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
           """
        strr_for_py_auto_script+=r"""
 def grab_text_from_clipboard_re_search_and_add_text_to_clipboard(self, re_pattern,groupp=0):
  import pyperclip
  import re
  text_to_process=pyperclip.paste()
  search_result=re.search(re_pattern,text_to_process)
  if search_result:
   search_result=search_result.group(groupp)
   pyperclip.copy(search_result)
 """         
          
        strr_for_py_auto_script+=r"""
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
     time.sleep(5)"""          
        strr_for_py_auto_script+=r"""
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
     input("input here and move to next click needed so skip buttons that screw parts of script up so no restart")"""           
        strr_for_py_auto_script+=r"""
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
  """
      
        strr_for_py_auto_script+=fr"""
 def move_mousey(self,move_to_list):
     import pyautogui
     for x_y_positions_list in move_to_list:
       pyautogui.moveTo(x_y_positions_list[0],x_y_positions_list[1])"""
        strr_for_py_auto_script+=fr"""
 def move_mousey(self,move_to_list):
    import pyautogui
    for x_y_positions_list in move_to_list:
      pyautogui.moveTo(x_y_positions_list[0],x_y_positions_list[1])"""
      
        strr_for_py_auto_script+=r"""
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
     return newest_pyautogui_light_table """
    
    
        strr_for_py_auto_script+=r"""
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
    print("Connection closed.")"""
        return strr_for_py_auto_script
    
  #retrieve data from website#how to do this automcially
  
  #run command to add data to coding file
    def screen_record_clicky(self,screen_shot_time,xy_str):
        import pyautogui
        import cv2
        import numpy as np
        import win32gui
        import re
        import time
        query_time=time.time()
        spacing_to_add=""
        img = pyautogui.screenshot()
        window = win32gui.GetForegroundWindow()
        active_window_name = win32gui.GetWindowText(window)
        active_window_name=re.sub(r"\'","",active_window_name)
        active_window_name=re.sub(r"\"","",active_window_name)
        print(active_window_name)
        print(self.previous_active_window_name)
        # 2 minutes?
        if self.previous_active_window_name!= active_window_name or query_time - self.last_screen_shot_taken_time>60:
            print(query_time - self.last_screen_shot_taken_time)
            print('Screenshot taken!')
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            path_to_frame=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\screenshots\screenshot{screen_shot_time}.png"
            cv2.imwrite(path_to_frame,frame)
            screen_recording_info_dic={"path_to_screenshot":path_to_frame,"active_window_name":active_window_name,"timee":query_time,"problem_question_or_task":xy_str}
            self.last_screen_shot_taken_time=query_time
        else:
            # dont save the screenshot to save on space on computer
            screen_recording_info_dic={"path_to_screenshot":"","active_window_name":active_window_name,"timee":query_time,"problem_question_or_task":xy_str}
        self.previous_active_window_name=active_window_name
        
            # add a bunch of new line characters to seperate out strs

        return screen_recording_info_dic
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
        path_to_screenshot=screen_recording_info_dic["path_to_screenshot"]
        active_window_name=screen_recording_info_dic["active_window_name"]
        timee=screen_recording_info_dic["timee"]
        problem_question_or_task=screen_recording_info_dic["problem_question_or_task"]

        path_to_screenshot=self.clean_strs_before_input_into_sql(path_to_screenshot)
        active_window_name=self.clean_strs_before_input_into_sql(active_window_name)
        timee=self.clean_strs_before_input_into_sql(timee)

        # need to make sure not to over write  values here
        #self.cur = self.conn.cursor()

        self.cur.execute( f""" INSERT INTO problem_solving_screen_recording_table (problem_question_or_task,path_to_screenshot,active_window_name,timee)
                     VALUES ('{str(problem_question_or_task)}','{str(path_to_screenshot)}','{str(active_window_name)}','{str(timee)}');""")
            
        self.conn.commit()
        
  
  

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
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
              except:
                  continue
          for link_finals in saved_link_list:
              try:
                  req = session.get(link_finals, headers=headers)
                  soup = BeautifulSoup(req.text)
                  p_tag_text=soup.get_text()
                  saved_text_from_websites_and_link_dic[link_finals]=str(p_tag_text)
              
              except:
                  continue
          driver.quit()
          return saved_text_from_websites_and_link_dic
      
        # when it gets stuck restart the whole program
          # build this in
          # this way if it is not working at one point it does not screw us
          # call itself recurviely if it recurses too many times just add this in
          
        
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
            return
        else:
            self.keyboard_and_mouse_press_and_time_list.append(["mouse_scroll",'Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)),timee,amount_to_scroll])
            self.last_input="mouse_scroll"
            print('MOUSE SCROLL')
            return
    def on_mouse_move(self, x, y):
        import time
        import re
        timee=time.time()
        # add this as a list in slot 4 
        # check last positon in keybaord list
        if self.last_input!="mouse_move":
            print('Pointer moved to {0}'.format((x, y)))
            mouse_end_position='{0}{1}'.format('Pressed',(x, y))
            #self.keyboard_and_mouse_press_and_time_list[-1][3]=mouse_end_position
            self.keyboard_and_mouse_press_and_time_list.append(["mouse_move","mouse_movee",timee,self.stored_mouse_move_list])
            self.stored_mouse_move_list=[]
            # will have to test this to see if missing anything here
            self.last_input="mouse_move"
      
        else:
            mouse_cordinates=re.search(r"\((-?\d+), (-?\d+)\)",'{0}{1}'.format('Pressed',(x, y))) # test this
            x=int(mouse_cordinates.group(1))
            y=int(mouse_cordinates.group(2))

            #mouse_start_position='{0}{1}'.format('Pressed',(x, y))
            self.stored_mouse_move_list.append([x,y])
            self.last_input="mouse_move"
    def mouse_pynput_on_click2(self,x, y, button, pressed):
        #print('WOOHAHAHAH')
        from pynput import mouse
        import time 
        self.counterrrr+=1
        print(self.counterrrr)
        xy_str=f"{x} {y}"
        if self.counterrrr>=4:
            if button == mouse.Button.left:
                query_time= time.time()
                screen_recording_info_dic=self.screen_record_clicky(query_time,xy_str)
                self.upload_problem_screen_information_to_sql(screen_recording_info_dic)
                self.counterrrr=0
                print('SCREEN SHOT TAKEN!')
    def mouse_pynput_on_click(self,x, y, button, pressed):
        """record on click elements """
        # get mouse scroll
        from pynput import mouse
        import time 
        #self.counterrrr+=1
        #print(self.counterrrr)
        xy_str=f"{x} {y}"
        #if self.counterrrr>=4:
        #    if button == mouse.Button.left:
        #        query_time= time.time()
        #        screen_recording_info_dic=self.screen_record_clicky(query_time,xy_str)
        #        self.upload_problem_screen_information_to_sql(screen_recording_info_dic)
        #        self.counterrrr=0
        #        print('SCREEN SHOT TAKEN!')
        ## og stuff
        query_time= time.time()
        previous_active_window_2=self.previous_active_window
        self.previous_active_window=self.active_window_name
        previous_active_window_url=self.active_window_url
        # find last accessed browser tab using chrome and firefox history apis
        path_to_frame,self.active_window_name,spacing_to_add=self.screen_record(query_time)
        print(f"ACTIVE WINDOW:{self.active_window_url} ")
        # this only works for firefox
        self.active_window_url=self.get_active_url_name_from_browsers_history()
        if self.previous_active_window!="" and self.active_window_name!=self.previous_active_window:  
            if self.start_recording==False:
                self.previous_active_window=self.previous_active_window[:40]
                previous_active_window_2=previous_active_window_2[:40]
                #self.create_pyautogui_file_of_inputs_and_video(previous_active_window,previous_active_window_url)
                self.create_pyautogui_file_of_inputs_and_video_2(previous_active_window_2,previous_active_window_url)
                print('new upload!')
                print(self.keyboard_and_mouse_press_and_time_list)

                self.keyboard_and_mouse_press_and_time_list=[]        
        if button == mouse.Button.right:# need to add in right mosue clicks
            print('RIGHT')
            print('{0}{1}'.format('Pressed',(x, y)))
            if self.last_input=="mouse_press_r":
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_release_r",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,self.active_window_name,spacing_to_add])
                print(self.keyboard_and_mouse_press_and_time_list)
                self.last_input="mouse_release_r"
                return
            else:
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_press_r",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,self.active_window_name,spacing_to_add]) 
                self.last_input="mouse_press_r"
                return
        if button == mouse.Button.left:
            if self.last_input=="mouse_press_l":
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_release_l",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,self.active_window_name,spacing_to_add])
                print(self.keyboard_and_mouse_press_and_time_list)
                self.last_input="mouse_release_l"
                return
            else:
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_press_l",'{0}{1}'.format('Pressed',(x, y)),query_time,path_to_frame,self.active_window_name,spacing_to_add])  
                self.last_input="mouse_press_l"
                return
    def keyboard_on_press_pynput(self,event):
        """ """
        from pynput import keyboard
        import time
        import re
        import pyautogui
        #pressed_button='{0}'.format(event.char)
        self.last_input="keyboard"
        try:
            pressed_button='{0}'.format(event.char)
            print(pressed_button)
            if pressed_button=="`":
                if self.start_recording==True:
                    self.start_recording=False
                    print('finished recording')
                    query_time= time.time()
                    self.previous_active_window=self.active_window_name
                    previous_active_window_url=self.active_window_url  
                    previous_active_window=previous_active_window[:40]
                    self.create_pyautogui_file_of_inputs_and_video(self.previous_active_window,previous_active_window_url)
                    self.keyboard_and_mouse_press_and_time_list=[] 
                    return
                self.start_recording=True
                self.keyboard_and_mouse_press_and_time_list=[]
                print('clearing keyboard chunk list')
                print('starting to record for a special chunk sequence')
                print('` Pressed')          
                return
            if self.keyboard_and_mouse_press_and_time_list:
                if pressed_button=="":
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_c",time.time()]) 
                    print('ctrl c!')
                    return
                if pressed_button=="":
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_a",time.time()]) 
                    print('ctrl a!')
                    return
                if pressed_button=="":
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_p",time.time()]) 
                    print('ctrl p!')
                    # add a process file thing here? and re maybe? add in optional
                    # add to clipboard and re text? to grab the code
                    # or whatever we want to do with the page html
                    return
                if pressed_button=="":
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_s",time.time()]) 
                    print('ctrl s!')
                    return
                if pressed_button=="[":
                     print(" move cursor to position")
                     x_y_position_tuble=pyautogui.position() 
                     self.keyboard_and_mouse_press_and_time_list.append(["move_cursor","move_cursor",time.time(),x_y_position_tuble])
                     return         
                if pressed_button=="/":# will need to test this to see if its gett he forward slash
                      print("open new firefox tab with webrowser to speicfic page")
                      x_y_position_tuble=pyautogui.position() 
                      self.keyboard_and_mouse_press_and_time_list.append(["keyboard","open_new_internet_window",time.time(),x_y_position_tuble])
                      return
                if pressed_button==".":# need to think out still how to get best effects from this
                     print("process text in clipboard with regex  and add output to clipboard ")
                     x_y_position_tuble=pyautogui.position() 
                     self.keyboard_and_mouse_press_and_time_list.append(["keyboard","grab_text_add_to_clipboard",time.time(),x_y_position_tuble])
                     return
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
                    print('ctrl A!')
                    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl_a",time.time()])   
                    return
                if self.ctrl_activated==True and pressed_button=="c":# for control c
                    print('ctrl c!')
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
            #if str('{0}'.format(event))=="Key.ctrl_l":
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","ctrl",time.time()]) 
            #   self.ctrl_activated=True
            #    print('ctrl_activated')
            #    return
            if str('{0}'.format(event))=="Key.f12":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","F12",time.time()]) 
                print('f12!')
                return
            
            
            if str('{0}'.format(event))=="Key.down":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","DOWN",time.time()]) 
                print('down!')
                return
            
            if str('{0}'.format(event))=="Key.up":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","UP",time.time()]) 
                print('up!')
                return
            
            if str('{0}'.format(event))=="Key.left":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","LEFT",time.time()]) 
                print('left!')
                return
            
            if str('{0}'.format(event))=="Key.right":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","RIGHT",time.time()]) 
                print('right!')
                return
            # dont want inital tabs after shift or alt is clicked
            if str('{0}'.format(event))=="Key.tab": 
                 if self.tab_skip== True:
                     self.tab_skip=False
                     print('last key alt or shift need to click or type something else to use tab')
                     return
                 else:
                        self.keyboard_and_mouse_press_and_time_list.append(["keyboard","tab",time.time()]) 
                        print('Tab!')
                        return  
            if str('{0}'.format(event))=="Key.alt_l":
                self.tab_skip=True
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","alt",time.time()]) 
                print('alt!')
                return               
            if str('{0}'.format(event))=="Key.shift":
                self.tab_skip=True
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","shift",time.time()]) 
                print('shift tab!')
                return
 
            #if str('{0}'.format(event))=="Key.backspace":
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard","backspace",time.time()]) 
            #    print('alt!')
            #    return
            #f_search=re.search(r"Key.(f.*)",str('{0}'.format(event)))
            #if f_search:
            #    self.keyboard_and_mouse_press_and_time_list.append(["keyboard",f_search.group(1),time.time()]) 
            #    print('f pressed')
        #for screen_namee in self.screens_where_screen_shots_wanted_list:
        #    if screen_namee in self.active_window_name:
                #if event == keyboard.Key.esc:# do all the work in here with downstream functions
                    #code_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\
                    #self.create_pyautogui_file_of_inputs_and_video()
                    #print("stop this program by closing the pyautogui window!")             
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
         
    

    
    def create_mouse_click_only_keyboard_mouse_press_list(self,keyboard_and_mouse_press_and_time_list):
        """ """
        import re
        click_cordinate_list=[]
        for i,keyboard_and_mouse_press_and_time in enumerate(keyboard_and_mouse_press_and_time_list):
            keyboard_or_mouse=keyboard_and_mouse_press_and_time[0]
            if keyboard_or_mouse=="mouse_press_l" or keyboard_or_mouse=="mouse_press_r":
                mouse_x_y=keyboard_and_mouse_press_and_time[1]
                top_left_mouse_click=re.search(r"\(\d+, \d+\)",mouse_x_y).group(0) 
                mouse_cordinate_split=re.search("(\d+), (\d+)",top_left_mouse_click)
                x_click=int(mouse_cordinate_split.group(1))
                y_click=int(mouse_cordinate_split.group(2))
                click_cordinate_list.append([x_click,y_click])
            if keyboard_or_mouse=="keyboard":
                click_cordinate_list.append(["keybaord"])
        return click_cordinate_list
    def process_coding_file_simple(self,coding_file,coding_file_dic):
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
        function_number_list_for_in_line_code={}
        package_to_describe=re.compile(r"\(.*?\)")
        re.compile("")
        
        python_script_split_lines=coding_file.splitlines()
        function=False
        # first run to get whole functions
        for line_number,line in enumerate(python_script_split_lines):
            docstring=""
            function_str_test=line.strip()
            function_search=False
            if function_str_test[:3]=="def":
                function_name=re.search(r"def (.*)\(",line).group(1)
                class_function_line_dic["function_name"].append(function_name)
                class_function_line_dic["function_defined_line_number"].append(line_number)
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
                class_function_line_dic["class_defined_line_number"].append(line_number)
                class_name=re.search(r"class (.*)\(",line).group(1)
                class_function_line_dic["class_name"].append(class_name)
                saved_class_line=line
                class_line_number=line_number
                continue 
            if class_function_str_test[:3]=="def":
                function_search=True 
                function_name=re.search(r"def (.*)\(",line).group(1)# may need to rewrite this
                #function_name=f"{line}"
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
                    coding_file_dic["function_defined_line_number"].append(function_defined_line_number)
                    coding_file_dic["class_created_line_number"].append(class_line_number)
                    coding_file_dic["docstring"].append(docstring)
                    coding_file_dic["line_of_code"].append(line_of_code)
                    coding_file_dic["code_base_function"].append(whole_functions_dic[saved_function_name_line])
                    coding_file_dic["class_name"].append(saved_class_line)
                    coding_file_dic["line_number_in_file"].append(line_number)
                    coding_file_dic["time_stamp"].append(time_stamp)
                    
        return coding_file_dic, class_function_line_dic
    
    
    def generate_code_chunk_list(self,python_file_str):
        """ """
        import re
        start_code_chunk=False
        code_chunk_list=[]   
        function_code_line_list=[]
        python_file_str_list=python_file_str.split('\n')
        code_chunk=""
        start_creating_chunk=False
        #print('PYTHON FILE STR')
        #print(python_file_str_list)
        # break it on start of function to first return
        recordding=False
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
        code_chunk=""
        coding_file_dic, class_function_line_dic=self.process_coding_file_simple(python_file_str,coding_file_dic)
        #print('CODING FILE DIC')
        #print(coding_file_dic["code_base_function"])
        #print(coding_file_dic["function_name"])
        #print(coding_file_dic)
        #gotta fix this
        pyauto_function=""
        for i7, function_name in enumerate(coding_file_dic["function_name"]):
            if function_name=="pyauto_gui_function0":
                pyauto_function=coding_file_dic["code_base_function"][i7]             
                break
        pyauto_function_line_list=pyauto_function.split("\n")
        
        #print(f"function_code_line_list{function_code_line_list}")  
        code_chunk=""        
        for i7, code_line2 in enumerate(pyauto_function_line_list):
            if "saved_screen_shots_text_list" in code_line2:
                start_creating_chunk=True
            if start_creating_chunk==False:
                continue
            if start_creating_chunk==True:        
                if "self.wait_till_template_present(r'/hom" in code_line2:
                    #break on click
                    # might lose last click in that case can subsitute it in
                    code_chunk+="\n"+code_line2 
                    code_chunk_list.append(code_chunk)
                    code_chunk="" 
                    continue
                code_chunk+="\n"+code_line2                                                            
                if i7==len(pyauto_function_line_list)-1:
                    #print('HEEEE')
                    if code_chunk:
                        code_chunk_list.append(code_chunk)
                        #print("FINAL COUNTDOWN")   
               
        return code_chunk_list
                
                
            # everything intitally ignore
            #break on chunk
            # problem here now i think
            
            

    def tab_logic_to_generate_tabs_and_multiprocess_pyautogui_scripts(self,python_file_str,previous_active_window_url,multi_process_number=9):
        """ this will make it so you can multiprocess the pyautogui faster"""
        code_chunk_list=self.generate_code_chunk_list(python_file_str) 
        # need to strip these
        #code_line=code_line.strip()
        #print(f"code_chunk_list")
        #print(code_chunk_list)
        multiprocess_pyautogui_scripts_with_tab_logic=f"""
 def multiprocess_pyautogui_scripts_with_tab_logic(self):
  """ """
  import webbrowser
  import time
  import pyautogui
  import time
  from PIL import ImageGrab
  import numpy as np
  import pytesseract  
  import os
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  saved_screen_shots_text_list=[]
  
  # make sure this is firefox
        """ 
        multiprocess_pyautogui_scripts_with_tab_logic+=f"\n  link=r'{previous_active_window_url[0]}'"
        multiprocess_pyautogui_scripts_with_tab_logic+=f"\n  webbrowser.open(link, new=2, autoraise=True)"
        # open all urls      
        multiprocess_pyautogui_scripts_with_tab_logic+=f"""
  for n in range({multi_process_number-1}):
      time.sleep(0.1)
      pyautogui.keyDown('alt')
      pyautogui.keyDown('d')
      pyautogui.keyUp('alt')
      pyautogui.keyUp('d')
      pyautogui.keyDown('shift')
      pyautogui.keyDown('enter')
      pyautogui.keyUp('shift')
      pyautogui.keyUp('enter')
      
      
            """              
        # add tab logic do a single click/action on each page before going to the
        for i_chunk, code_chunkyy in enumerate(code_chunk_list):
            #print(code_chunkyy)
            #print('CODE CHUNKY')
            
            for process_num in range(multi_process_number):
                tab_list_start="['tab']"
                for tabb in range(process_num):
                    tab_list_start2=tab_list_start[:-1]+ ",'tab'"+"]"
                    tab_list_start=tab_list_start2
                tab_list_start="tab_list="+tab_list_start
                tab_str_to_add=f"""
  {tab_list_start}
  pyautogui.keyDown('alt')
  for tab in tab_list:
    pyautogui.press(tab)
  pyautogui.keyUp('alt')"""              
                #code_chunkyy+=                
                multiprocess_pyautogui_scripts_with_tab_logic+=code_chunkyy+tab_str_to_add

                
        return multiprocess_pyautogui_scripts_with_tab_logic        
    
    def create_equvalent_dev_tools_code_using_screenshot_info(self,previous_active_window_url,keyboard_and_mouse_press_and_time_list):
        """need to run this on other computer to generate the content then send it back to generate the file
        scp the file created on the other computer into this computer?
        how do i send the info back somehow?
        send them to click
        finish creating files  on other computer"""
        #run code on other machine
        #but first add xpath listner
        #then
        #record xpaths 
        #then
        #add a queue to run the pyautogui scripts on the other pc
        #to get xpath
        #then
        #add xpaths
        import time
        import pyautogui
        import time
        import multiprocessing
        import subprocess
        copy_clip="""function copyObjectToClipboard(obj) {
      // Convert the object to a JSON string
      const json = JSON.stringify(obj, null, 2);

      // Create a textarea element
      const textarea = document.createElement('textarea');
      textarea.value = json;

      // Add the textarea to the page
      document.body.appendChild(textarea);

      // Select the textarea
      textarea.select();

      // Copy the textarea value to the clipboard
      document.execCommand('copy');

      // Remove the textarea from the page
      document.body.removeChild(textarea);
    }"""
        
        get_xpath_function= """function getElementXPath(element) {
    var paths = [];

    // Loop through the element's ancestors to construct the full XPath
    while (element !== null && element.nodeType === Node.ELEMENT_NODE) {
        var path = element.nodeName.toLowerCase();  // Get the element's tag name
        if (element.id) {
            path += '[@id="' + element.id + '"]'; // If the element has an ID, use it
        } else {
            var sibling = element;
            var siblingCount = 1;

            // Count how many sibling elements share the same tag name
            while (sibling.previousElementSibling) {
                sibling = sibling.previousElementSibling;
                if (sibling.nodeName.toLowerCase() === element.nodeName.toLowerCase()) {
                    siblingCount++;
                }
            }
            if (siblingCount > 1) {
                path += '[' + siblingCount + ']'; // Add position if there are other siblings with the same tag name
            }
        }

        paths.unshift(path);  // Add the current path to the front of the array
        element = element.parentNode;  // Move up to the parent element
    }

    return paths.length ? '/' + paths.join('/') : null; // Join all the paths with '/'
}"""
        use_xpath_function=   """document.addEventListener('click', function(event) {
           var element = event.target;  // The element that was clicked
           var xpath = getElementXPath(element);  // Get the XPath of the clicked element
           console.log('XPath of clicked element: ', xpath);
           
       }); """ 
        
        store_logs_add_to_x_path="let capturedLogs = [];"
        # capture the message logs
        """console.log = function(message) {
  capturedLogs.push(message); // Store the message in capturedLogs
  // Call the original console.log method to also display the message in DevTools
  originalConsoleLog(message);
}; """
            
        copy_text_files= " let textToCopy = 'Hello, this is a text message!';"

        copy_log_files_to_clipbaord="""// Use the Clipboard API to copy the text to the clipboard
navigator.clipboard.writeText(textToCopy)
  .then(() => {
    console.log('Text copied to clipboard!');
  })
  .catch((err) => {
    console.error('Failed to copy text: ', err);
  });"""
        
             
        click_cordinate_list=self.create_mouse_click_only_keyboard_mouse_press_list(keyboard_and_mouse_press_and_time_list)  
        import webbrowser
        webbrowser.open(previous_active_window_url)
        time.sleep(2)
        pyautogui.hotkey('f12') # open dev tools
        pyautogui.write(f"{xpath_function}")
        pyautogui.press('enter')
        pyautogui.write(f"{use_xpath_function}")
        pyautogui.press('enter')
        for click_location in click_cordinate_list:
            if len(click_location)==2:
                xx=click_location[0]
                yy=click_location[1]
                pyautogui.moveTo(xx,yy)
                pyautogui.click(xx,yy)                
            else:
                continue 
        pyautogui.moveTo(xx,yy)
        pyautogui.click(xx,yy)        
        #retrieve xpath data from dev tools logs
        # or find other way to log the things being clicked
        # use pyautogui to reselect dev tools
        # then copy the variable to clipboard
        # then need command
        #screenshot?
        import pyperclip
        click_to_simulate_logs=pyperclip.paste()
        #convert logs into a list to write code from
        equavlent_dev_tools_selenium_code_str="""
            def execute_javascript_dev_tool_code_generate_script():
             """ """
             import webbrowser
             webbrowser.open(previous_active_window_url)  # Go to example.com
             time.sleep(2)
             pyautogui.hotkey('f12') # open dev tools                                
            """
        click_to_simulate_logs_list=re.split(r"\n",click_to_simulate_logs)        
        for log_line in click_to_simulate_logs_list:
            if log_line== "log_line_with_relevent_info":                    
                print('hi')
                equavlent_dev_tools_selenium_code_str+="pyautogui.write()"
                # anoymous debugger eval code is a error if dont change the variable name
                # like from xpath1 to xpath2
                # let xpath1 = "/div/div[2]/div[2]/article/div/div/section/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/span/div/div/div/div/div/p/a"; 
                equavlent_dev_tools_selenium_code_str+="""              
                let xpath = "{log_line}";
                let element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

                // Simulate a click on the element
                if (element) {
                  element.click();
                } else {
                  console.log("Element not found!");
                """
        return equavlent_dev_tools_selenium_code_str
        # convert the code into javascirpt to click on elements in browser
        #if can use element id use the below
        #"""
        #// Get the element by its ID
        #let button = document.getElementById('myButton');
        #// Simulate a click on the button
        #button.click();
        #"""
 
        
        #and convert it to javascript to execute in console on that page
        # create javascript to click these elements
        
        
        # how to get the elements and make them click
        
        # execute the pyautogui script presses pressing in the locations noted
        #retrive results to clipboard from the console the 
 
        
        # gather information from the page to figure out which element it is
        # do this by hovering over area where you clicked
        # then practice click on this area using javascript code
        # execute pyautogui clicks
        
        # wait till tab opens
        # find the relevent elements
        #execute necessary javasceipt commands to find reelevent elements on page
        # then save commands to click them javascript to click them
        #grab the info somehow and use it to write to the pyautogui string
        
                
        
    def create_selenium_equvalent_of_code_using_screenshot_info(self,previous_active_window_url,keyboard_and_mouse_press_and_time_list):
        """maybe run this as a script on the other computer using ssh  """
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        import re
        element_info_list=[]
        element_to_click_with_selenium_list=[]
        element_to_click_and_type_with_selenium_list=[]
        firefox_options = FirefoxOptions()
        firefox_options.headless = True
        driver= webdriver.Firefox(options=firefox_options)
        click_cordinate_list=self.create_mouse_click_only_keyboard_mouse_press_list(keyboard_and_mouse_press_and_time_list)  
        #driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
        print(f"previous link: {previous_active_window_url}")
        previous_active_window_url=previous_active_window_url[0]
        driver.get(previous_active_window_url)
        # NEED TO TEST THIS
        while driver.execute_script("return document.readyState;") != "complete":
            time.sleep(1)  # Sleep for 1 second before checking again
        # Once the page is fully loaded, continue with other actions
        print("Page is fully loaded")
        elements = driver.find_elements(By.XPATH, "//*")  # This selects all elements on the page
        print(elements)
        driver.quit()
        # Iterate through all elements and print their tag name and some additional information
        # deal with the text inputs too?
        # add in keyboard info if there is any typing
        print(f"click coridnate list: {click_cordinate_list}")
        for xy_click_or_keyboard in click_cordinate_list:
            if len(xy_click_or_keyboard)==1:
                #keyboard
                element_to_click_with_selenium_list.append("keybaord selenium command")
                continue
            x_click=xy_click_or_keyboard[0]
            y_click=xy_click_or_keyboard[1] 
            difference_from_click_to_element_x_list=[]
            difference_from_click_to_element_y_list=[]
            difference_from_click_to_element_total_list=[]
            for iterr,element in enumerate(elements):
                #print(f"Tag: {element.tag_name}, Text: {element.text.strip()}")
                tag_name=element.tag_name
                element_location = element.rect
                width=element_location['width']
                height=element_location['height']
                x_element=element_location['x']
                y_element=element_location['y']
                distance_from_x_element_to_click=int(x_element)-int(x_click)
                distance_from_y_element_to_click=int(y_element)-int(y_click)
                total_distance= abs(distance_from_x_element_to_click)+abs(distance_from_y_element_to_click)
                difference_from_click_to_element_x_list.append(distance_from_x_element_to_click)
                difference_from_click_to_element_y_list.append(distance_from_y_element_to_click)
                difference_from_click_to_element_total_list.append(total_distance)
                # find value that minizes x and y
            min_total_distance= min(difference_from_click_to_element_total_list)
            min_difference_x=min(difference_from_click_to_element_x_list)
            min_difference_y=min(difference_from_click_to_element_y_list)
            min_total_index=difference_from_click_to_element_total_list.index(min_total_distance)
            min_distance_x_index=difference_from_click_to_element_x_list.index(min_difference_x)
            min_distance_y_index=difference_from_click_to_element_y_list.index(min_difference_y)
            element_wanted=elements[min_total_index]# closest element hopefully found here
            element_to_click_and_type_with_selenium_list.append(element_wanted)
            print(f"element_to_click_and_type_with_selenium_list: {element_to_click_and_type_with_selenium_list}") 
             # check if they match
             #if not choose one that minimizes x and y
        # generate selenium code string
        
        selenium_code_str=f""" 
        def selenium_code(self):
            """ """
            from selenium import webdriver
            import time
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            import re
            element_info_list=[]
            element_to_click_with_selenium_list=[]
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            driver= webdriver.Firefox(options=firefox_options)
            driver.get({previous_active_window_url})
            while driver.execute_script("return document.readyState;") != "complete":
                time.sleep(1)
            content = driver.find_element(By.CLASS_NAME, 'search__input').click()
        """     
        for elementtt in element_to_click_and_type_with_selenium_list:
            if "mouse":
                selenium_code_str+="\n    content = driver.find_element(By.CLASS_NAME, 'search__input').click()"
            if "keyboard":
                # this may be the same delent where we just clicked so ignore first one for now 
                #selenium_code_str+="\n    content = driver.find_element(By.CLASS_NAME, 'search__input')"
                selenium_code_str+="\n    content.send_keys(f'{problem_to_search_for}')"
                selenium_code_str+="\n    content.send_keys(Keys.ENTER)"   
        # may want to add send keys here for keyboard clicks
        
        return selenium_code_str,element_to_click_and_type_with_selenium_list
        #content = driver.find_element(By.CLASS_NAME, 'search__input').click()
        #content.send_keys(f"{question_to_search_for}")
        #content.send_keys(Keys.ENTER)
        #time.sleep(2)
        #print(content)
        #html= driver.execute_script("return document.documentElement.outerHTML")
        #sel_soup = BeautifulSoup(html, 'html.parser')
        #links_of_dif_docs= sel_soup.findAll("a") 
        #driver.find_element_by_css_selector('.button.c_button.s_button').click()
   
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
        with open(exe_file_name,"w") as f:
            f.write(inputt_file_str)
        return exe_file_name,exe_file_name_linux
    def add_or_create_business_processes_pre_made_bash_function_file(self,exe_and_main_file_path,exe_and_main_file_path_linux,code_file_name_no_path,exe_file_name,remote=False):
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
        business_processes_pre_made_bash_function_file_name="business_function_bash_file.py"
        business_processes_pre_made_bash_function_file_name=exe_and_main_file_path+"\\"+ business_processes_pre_made_bash_function_file_name+str(todayy)+ "  "+str(timee)+".py"
        business_processes_pre_made_bash_function_file_name=re.sub(r"[ -]","_",business_processes_pre_made_bash_function_file_name)
        
        business_processes_pre_made_bash_function_file_name="business_function_bash_file.py"
        business_processes_pre_made_bash_function_file_name_linux=exe_and_main_file_path_linux+"/"+ business_processes_pre_made_bash_function_file_name+str(todayy)+ "  "+str(timee)+".py"
        business_processes_pre_made_bash_function_file_name_linux=re.sub(r"[ -]","_",business_processes_pre_made_bash_function_file_name)
        #write file content
        file_strr=fr"""# -*- coding: utf-8 -*-\n"+f"Created on {datee} {timee}  @author: yyyyyyyyyyyyyyyyyyyy
def {code_file_name_no_path}():
    import subprocess
    import os
    import re
    #all_computer_names=["big_white","big_black","hp_laptop","website_server","corsair","acer","hp"]
    computer_name= "hp_laptop"
    self.computer_info_dic=self.ip_address_look_up_table_creator()
    computer_name_index=self.computer_info_dic["computer_name"].index(computer_name)
    host=self.computer_info_dic["ip_number"][computer_name_index]
    username=self.computer_info_dic["user_name"][computer_name_index]
    computer_password=self.computer_info_dic["computer_password"][computer_name_index]
    dbnames=self.computer_info_dic["dbnames"][computer_name_index]
    data_base_password=self.computer_info_dic["data_base_password"][computer_name_index]
    exe_file=rf"/home/jross77/Documents/pyautogui/{code_file_name_no_path}/{exe_file_name}
    screen_dir_name="{code_file_name_no_path}"
    bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\pyauto.sh"
    run_pyauto_str=f'''#!/bin/bash
    source /home/jross77/Documents/pyautogui/venv/bin/activate
    export DISPLAY=:0
    #xdotool mousemove 100 200 # this works and gives me hope
    python3 /home/jross77/Documents/pyautogui/{code_file_name_no_path}/{exe_file_name}
    deactivate"""

        file_strr+=r""" 
    #python3 /path/to/your_script.py arg1 arg2
    #xvfb-run python your_script.py
    # Deactivate virtual environment (if needed)
    deactivate'''
    # change this to only copy the newest files maybe
    scp_command = [f"scp","-r",rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\{screen_dir_name}",fr"{username}@{host}:/home/jross77/Documents/pyautogui"]# put the script you want to run here 
    self.subprocess_run_script_remotely(scp_command)
    with open(bash_file_name,"w") as f:
        f.write(run_pyauto_str)
        print('write')
    script_dir=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\{screen_dir_name}" 
    scp_command_list = [f"scp",f"{bash_file_name}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here 
    self.subprocess_run_script_remotely(scp_command_list)
    #ssh into the 
    doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix","/home/jross77/Documents/pyauto.sh"]
    self.subprocess_run_script_remotely(doc2ui)
    ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/pyauto.sh"]# put the script you want to run here
    try:
        subprocess.run(ssh_command, check=True,shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to SSH into {host}: {e}")
        input()
    input()"""  
        with open(business_processes_pre_made_bash_function_file_name,"w") as f:
            f.write(file_strr)
        return business_processes_pre_made_bash_function_file_name,business_processes_pre_made_bash_function_file_name_linux

   
    def subprocess_popen_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         p=subprocess.Popen(command_list)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
         print('ERROR')
     return p
     #inputs:
     #outputs:
     #packages:
     #chatgpt_prompt:
     #search_prompt:
     #end state: 
     return 
    def subprocess_run_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         subprocess.run(command_list, check=True,shell=True)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
     #inputs:
     #outputs:
     #packages:
     #chatgpt_prompt:
     #search_prompt:
     #end state: 
     return 
    def exe_pyautogui_creation_script_on_other_computers_sub_2(self,username,host,remote_computer_script_dic,dir_to_store_script_linux,bash_file_name,bash_file_name_linux):
         """ remote computer dir need this to copy over
         then execute these functions on remote dir"""  
         #doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix",f"{bash_file_name_linux}"]
         doc2ui = [f"ssh", f"{username}@{host}","dos2unix",f"{bash_file_name_linux}"]
         self.subprocess_run_script_remotely(doc2ui)
         #p5=self.subprocess_run_script_remotely(doc2ui)
         #self.subprocess_popen_script_remotely(doc2ui)

         
    def exe_pyautogui_creation_script_on_other_computers_sub_3(self,username,host,remote_computer_script_dic,dir_to_store_script_linux,bash_file_name,bash_file_name_linux):
         """ remote computer dir need this to copy over
         then execute these functions on remote dir""" 
         #bash_file_name_linux=remote_computer_script_dic["bash_file_name_linux"]
         #single_exe_process_file_name_linux=remote_computer_script_dic["single_exe_process_file_name_linux"]
         ssh_command = [f"ssh",  f"{username}@{host}",f"bash {bash_file_name_linux}"]# put the script you want to run here
         print('haha')
         self.subprocess_popen_script_remotely(ssh_command)
         #pyautogui_creation = [f"ssh",  f"{username}@{host}","python3",f"{single_exe_process_file_name_linux}"]      
         #self.subprocess_run_script_remotely(pyautogui_creation)
         #print('doc2')
         #self.subprocess_run_script_remotely(ssh_command)

         
         
    def exe_pyautogui_creation_script_on_other_computers_sub(self,username,host,remote_computer_script_dic,dir_to_store_script_linux,relevent_prep_file_name_and_dir_dic):
         """ remote computer dir need this to copy over
         then execute these functions on remote dir
         run mkdir locally as a bash will be way faster i think
         turning this into a bash scrip tto exectue everything for mkdir"""        
         #copy bash scrip t overexe_pyautogui_creation_script_on_other_computers_sub_3
         remote_mkdir_bash_file_name2=relevent_prep_file_name_and_dir_dic["remote_mkdir_bash_file_name2"]
         dir_scripts_stored=relevent_prep_file_name_and_dir_dic["dir_scripts_stored"]
         bash_file_name_linux=relevent_prep_file_name_and_dir_dic["bash_file_name_linux"]
         local_mkdir_bash_file_name2=relevent_prep_file_name_and_dir_dic["local_mkdir_bash_file_name2"]
         #=relevent_prep_file_name_and_dir_dic[]
         #=relevent_prep_file_name_and_dir_dic[]

         scp_command = [f"scp",local_mkdir_bash_file_name2,f"jross77@{host}:/home/jross77/Documents"]# put the script you want to run here 
         p1=self.subprocess_popen_script_remotely(scp_command)
         #run doc2unix on itpw
         print('doc1')
         doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix",f"{remote_mkdir_bash_file_name2}"]
         p2=self.subprocess_popen_script_remotely(doc2ui)
          #self.subprocess_run_script_remotely(doc2ui)
         #then execute it
         ssh_command = [f"ssh",  f"{username}@{host}",f"bash {remote_mkdir_bash_file_name2}"]# put the script you want to run here
         self.subprocess_run_script_remotely(ssh_command)
         #p3=self.subprocess_popen_script_remotely(ssh_command)
         print('RAN BASH')
         #script_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_server_files" 
         #mkdir_command = [f"ssh","-X",  f"{username}@{host}","mkdir","-p",f"{dir_to_store_script_linux}"]
         scp_command = [f"scp","-r",rf"{dir_scripts_stored}",f"jross77@{host}:/home/jross77/Documents/pyautogui_remote_creation_files"]# put the script you want to run here 
         #scp_command_list = [f"scp","-r", f"{script_dir}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here 
         #self.subprocess_run_script_remotely(scp_command)
         p4=self.subprocess_popen_script_remotely(scp_command)       
         doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix",f"{bash_file_name_linux}"]
         p5=self.subprocess_popen_script_remotely(doc2ui)
         #print('doc2')
         #p5=self.subprocess_popen_script_remotely(doc2ui)
         print('DOC')
         process_listner_list=[p1,p2,p4,p5]
         #process_listner_list=[p1,p2,p4,p5]
         return process_listner_list
         file_and_dir_creation_bash_str=fr"""#!/bin/bash
         DIR="{dir_to_store_script_linux}"
         DIR2="{final_linux_script_dir}"
         if [ ! -d "$DIR" ]; then
          echo "dir not exists!"
          mkdir -p "$DIR"
          chmod 777 "$DIR"
         fi
         if [ ! -d "$DIR2" ]; then
          echo "dir not exists!"
          mkdir -p "$DIR2"
          chmod 777 "$DIR2"
         fi"""
     

                          

                 
         
         
         
         #create bash script file locally
#         file_and_dir_creation_bash_str=fr"""#!/bin/bash
#DIR="{dir_to_store_script_linux}"
#DIR2="{final_linux_script_dir}"
#mkdir -p "$DIR"
#mkdir -p "$DIR2"
#"""
         #script_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_server_files" 
         #mkdir_command = [f"ssh","-X",  f"{username}@{host}","mkdir","-p",f"{dir_to_store_script_linux}"]
         #mkdir_command = [f"ssh",  f"{username}@{host}","mkdir",f"{dir_to_store_script_linux}"]

         #self.subprocess_run_script_remotely(mkdir_command)
         #p1=self.subprocess_popen_script_remotely(mkdir_command)
         #mkdir_command = [f"ssh","-X",  f"{username}@{host}","mkdir","-p",f"{final_linux_script_dir}"]
         #self.subprocess_run_script_remotely(mkdir_command)
         #p2=self.subprocess_popen_script_remotely(mkdir_command)
         #scp_command = [f"scp","-r",rf"{dir_scripts_stored}",f"jross77@{host}:/home/jross77/Documents/pyautogui_remote_creation_files"]# put the script you want to run here 
         #scp_command_list = [f"scp","-r", f"{script_dir}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here 
         #self.subprocess_run_script_remotely(scp_command)
         #p3=self.subprocess_popen_script_remotely(scp_command)       
         #doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix",f"{bash_file_name_linux}"]
         #self.subprocess_run_script_remotely(doc2ui)
         #p4=self.subprocess_popen_script_remotely(doc2ui)
         #print('DOC')
         #print(p3)
         #input('HELLO GOOD SIR')
         #process_listner_list=[p1,p2,p3,p4]
         #return process_listner_list
         #input()
         #ssh_command = [f"ssh",  f"{username}@{host}",f"bash {bash_file_name_linux}"]# put the script you want to run here
         #self.subprocess_run_script_remotely(ssh_command)
         #self.subprocess_popen_script_remotely(ssh_command)
         #print("/home/jross77/Documents/pyautogui_creation_scripts")
         #print('meow')
         # create and install virtual environment so everything runs
         # need to create pyautgui env if not already there
         #just install pyautogui mannually to avoid errors refer to setup_computer_to_run_pyautogui ?
         # Define the directory path please refer to setup_computer_to_run_pyautogui for guidance

         # transfer over bash file and pyautogui exe and code creation file
         pyautogui_venv_bash="""#!/bin/bash
DIR="/home/jross77/Documents/pyautogui"
DIRR="/home/jross77/Documents/happy_man"
VENV_DIR="/home/jross77/Documents/pyautogui/venv"
# Create the directory
if [ -d "$DIR" ]; then
 echo "dir exists!"
else
 echo "dir not exists!"
 mkdir -p "$DIR"
 chmod 777 "$DIR"
 sudo chown jross77 "$DIR"
 mkdir -p "$DIRR"
 chmod 777 "$DIRR"
 sudo chown jross77 "$DIRR"
fi
# Check if the virtual environment already exists
if [ -d "$VENV_DIR" ]; then
 echo "Virtual environment already exists. Activating..."
 # Activate the existing virtual environment
 source "$VENV_DIR/bin/activate"
else
 echo "Virtual environment does not exist. Creating a new one..."
 # Create a new virtual environment
 
 python3 -m venv "$VENV_DIR"
 # Activate the newly created virtual environment
 source "$VENV_DIR/bin/activate"
fi
sudo apt install -y python3-pip
sudo apt-get install xvfb
sudo apt install dos2unix# this is super important to make sure we can do this
pip install --upgrade pip
pip install pyautogui
sudo apt install idle
sudo apt-get install scrot
sudo apt-get install python3-tk
sudo apt-get install python3-dev
sudo chmod -R u+w /home/jross77/Documents/pyautogui/venv/lib/python3.12/site-packages/
sudo chown -R $USER /home/jross77/Documents/pyautogui/venv/lib/python3.12/site-packages/
pip install pillow
sudo chmod -R u+w /home/jross77/Documents/pyautogui/venv/bin/
sudo chown -R $USER /home/jross77/Documents/pyautogui/venv/
pip install numpy
pip install pytesseract
pip install beautifulsoup4
pip install pyperclip
sudo apt-get install tesseract-ocr
pip install opencv-python
sudo apt-get update
sudo apt install curl  
sudo apt-get install xclip
sudo apt update
sudo systemctl enable ssh
sudo ufw allow ssh
sudo systemctl restart ssh
sudo apt install postgresql
sudo apt-get install libpq-dev python-dev
sudo apt-get install --reinstall libpq-dev
pip install psycopg2
sudo apt install xdotool
export PATH=$PATH:/usr/bin:/usr/local/bin
echo 'export PATH=$PATH:/usr/bin:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc
sudo chmod 755 $(which python3)
sudo chown jross77:jross77 $(which python3)
export DISPLAY=:0 # use this to set display FIXES ERROR IT SEEMS  
touch ~/.Xauthority
ls -l ~/.Xauthority# check permissions
chmod 600 ~/.Xauthority
xdotool mousemove 100 200 
         """
         
         # transfer    
    def run_pyautogui_creation_script_on_all_other_computers_create_script_locally_to_ensure_correct_pixels(self,previous_active_window,previous_active_window_url,timee,dir_to_store_script,remote_computer_script_dic,dir_to_store_script_linux,relevent_prep_file_name_and_dir_dic,remote=False):
        #previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,remote=remote
        """ testing this on host 200  # run this command on all the computers at once
        need to subprocess this so it does not break everything else and then get different statements to run
        and use 
        try:
        except Exception as E:
            print(E)
            print('FAILED')""" 
        import time
        host_list=["192.168.2.43","192.168.2.207","192.168.2.46","192.168.2.47","192.168.2.45"]
        #host_list=["192.168.2.200"]# this is temporary
        host_list=["192.168.2.43"]# this is temporary
        bash_file_name=relevent_prep_file_name_and_dir_dic["bash_file_name"]
        bash_file_name_linux=relevent_prep_file_name_and_dir_dic["bash_file_name_linux"]

        user_name_list=["jross77","jross77","jross77","jross77","jross77"]
        all_sub_process_listener_list=[]
        for host, user_name, in zip(host_list,user_name_list):
            process_listner_list=self.exe_pyautogui_creation_script_on_other_computers_sub(user_name,host,remote_computer_script_dic,dir_to_store_script_linux,relevent_prep_file_name_and_dir_dic)
            all_sub_process_listener_list.extend(process_listner_list)
        # only execute this when others subporocess have finished
        for processs in  all_sub_process_listener_list:
            while True:
                poll = processs.poll()
                if poll != None:
                    # process is dead
                    break
                if poll == None:
                    time.sleep(1.5)
                    print(processs)
                    print(' ALIVE not done yet')
                    continue
        print('fixxing them up')
        for host, user_name, in zip(host_list,user_name_list):
            self.exe_pyautogui_creation_script_on_other_computers_sub_2(user_name,host,remote_computer_script_dic,dir_to_store_script_linux,bash_file_name,bash_file_name_linux)       
        print('READY CAPTAIN')
        for host, user_name, in zip(host_list,user_name_list):
            self.exe_pyautogui_creation_script_on_other_computers_sub_3(user_name,host,remote_computer_script_dic,dir_to_store_script_linux,bash_file_name,bash_file_name_linux)
        return
        #only execute when p.poll is done
        # create list of subprocess p value listeners
        # when all of these are finished execute this subsqent command
        #p=subprocess.Popen(command_list)
        #poll = p.poll()
        #if poll != None:
        #    print('meow')
        
        
        #production version so fast and not slow dont use subprocess
        #dir_scripts_stored=remote_computer_script_dic["dir_to_store_script"]
        #final_linux_script_dir=remote_computer_script_dic["final_linux_script_dir"]
        # so learn how to run this commpletely seperately
        #for host, user_name, in zip(host_list,user_name_list): 
            #how do i run this and let everything else continue
        #    self.exe_pyautogui_creation_script_on_other_computers_sub(user_name,host,,bash_file_name,bash_file_name_linux,dir_to_store_script,final_linux_script_dir)
            # run this as a bash

                
        #copy over dir pyautogui
        
        # execute the pyautogui script within the bash command
        #also ssh over the pyautogui script to execute to
        #create the other pyautogui script
        # write script info back to server on remote computer
        # to the pyautogui exe table
        # retrieve this information on this local computer
      
        # get screen size 
        #get other screen size on other computer
        # change clicks and timings ocnsidering changes as necessary and fine tune
        # then run script to create pyautogui script
    def create_pyautogui_file_of_inputs_and_video_remote(self,previous_active_window,previous_active_window_url):
         """ this will output the pyautogui file of the session we wanted to record 
         FOR REMOTE
         this will save mouse cllick locations and scale them based on screen size
         add remote kwarg to each of the functions and modify them as necessary 
         change the main file that is to be executed in the script so it will retrieve screenshots
         and it will evenutally take information gathered and generate another pyautogui file
         that would operate like the one created with the video function
         add the vdieo function inside the script created on other computer
         so you can create the script in the other script from screenshots"""
         import time
         import os
         import re
         from datetime import date
         root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_creation_files"
         pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_creation_files")
         previous_active_window=re.sub(r"[^a-zA-Z0-9 ]", "", previous_active_window)# check this
         previous_active_window=re.sub(r"[ -]","_",previous_active_window)     
         self.dir_to_store_script=root_folder+"\\"+previous_active_window  
         self.dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui_remote_creation_files/"+previous_active_window
         self.final_dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui_remote_files/"+previous_active_window
         #self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
         timeee=time.time()  
         todayy=date.today()
         code_file_name_only=previous_active_window+str(todayy)+ "  "+str(timeee)
         code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
         code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only+".py"
         code_file_name_path_linux=self.dir_to_store_script_linux+"/"+code_file_name_only+".py"
         code_file_name_no_path_for_function_import=code_file_name_only            
         if previous_active_window not in pyauto_file_dir_list:
             os.mkdir(self.dir_to_store_script) 
         remote=True
         python_file_str=self.create_pyauto_gui_function_str(self.keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux, remote=remote)
         self.add_to_or_create_new_python_file(python_file_str,code_file_name_path)           
         single_process_exe_file_name,single_exe_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=False,remote=True)
         bash_file_name,bash_file_name_linux=self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,single_process_exe_file_name, remote=True)
         remote_computer_script_dic={"code_file_name_path_linux":code_file_name_path_linux,"code_file_name_only":f"{code_file_name_only}.py","final_linux_script_dir":self.final_dir_to_store_script_linux,"dir_to_store_script_linux":self.dir_to_store_script_linux,"bash_file_name":bash_file_name,"single_exe_process_file_name_linux":single_exe_process_file_name_linux,"single_exe_process_file_name":single_process_exe_file_name,"dir_to_store_script":self.dir_to_store_script}
         return remote_computer_script_dic  
    def insert_into_postgres_local(self,column_name_data_type_dic,table_name=""):
     ''' '''
     import psycopg2
     import re
     self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
     self.cur = self.conn.cursor()
     print("Connection successful!")
     for i, (table_column, column_value) in enumerate(column_name_data_type_dic.items()):
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
     #self.cur.close()
     #self.conn.close()
     print("Connection closed.")
     #inputs:
     #outputs:
     #packages:
     #chatgpt_prompt:
     #search_prompt:
     #end state: 
     return 
    def upload_data_from_website_database(self,dictionary_of_values,table_name="",host="192.168.2.209"):
     ''' '''
     import psycopg2
     import re
     from psycopg2 import sql
     host = host  # E.g., '192.168.1.100' or 'your-database-server.com'
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
             
     #self.cur.close()
     #self.conn.close()
     print("Connection closed.")
    def subprocess_run_script_remotely(self,command_list):
     ''' '''
     import subprocess
     try:
         subprocess.run(command_list, check=True,shell=True)
     except subprocess.CalledProcessError as e:
         print(f"Failed to SSH into :{e}")
     #inputs:
     #outputs:
     #packages:
     #chatgpt_prompt:
     #search_prompt:
     #end state: 
     return 
    def run_page_action_script_creation_from_website_server_on_other_servers(self,previous_active_window,previous_active_window_url,timeee,dir_to_store_script_linux,remote=""):
        """do this as a bash script maybe? """
        #[previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,self.dir_to_store_script_linux,remote=remote]
        #pyautogui_creation = [f"ssh",  f"{username}@{host}","python3","run_pyautogui_creation_script_on_all_other_computers_create_script_locally_to_ensure_correct_pixels", "previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,self.dir_to_store_script_linux,remote=remote"]
        #self.subprocess_run_script_remotely(pyautogui_creation)
        # run the below line as a script on the remote server
        #self.run_pyautogui_creation_script_on_all_other_computers_create_script_locally_to_ensure_correct_pixels
        #(previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,self.dir_to_store_script_linux,remote_computer_script_dic,remote=remote)
   
        
    def prep_exe_files_for_website_server_pyautogui_creation(self,remote_computer_script_dic,timee):
        """ """
        #input()
        #pyautogui_remote_creation_files # need to change this on widows
        #pyautogui_creation_scripts# currently used on linux
        #with open(bash_file_name,"w") as f:
        #    f.write(bash_code_to_get_run_xdo_tools_and_create_pyautogui)
        #    print('write')
        # test version!!! to see errors and inputs for tracking with subprocess
        import time
        #host_list=["192.168.2.200","192.168.2.233","192.168.2.213","192.168.2.28","192.168.2.207"]
       
        dir_to_store_script=remote_computer_script_dic["dir_to_store_script"]
        dir_to_store_script_linux=remote_computer_script_dic["dir_to_store_script_linux"]
        single_exe_process_file_name_linux=remote_computer_script_dic["single_exe_process_file_name_linux"]
        code_file_name_only=remote_computer_script_dic["code_file_name_only"]
        main_model_bash=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\main_model.sh"
        with open(main_model_bash,"r") as f3:
            f3_file_str=f3.read()
        f3_file_str_list=f3_file_str.splitlines()
        f3_file_str_list[8]=fr'python3 {single_exe_process_file_name_linux}'
        final_file_str=""
        for i, linee in enumerate(f3_file_str_list):
            if i==0:
                final_file_str=f"{linee}"
            else:
                final_file_str+=f"\n{linee}"              
        bash_file_name=dir_to_store_script+r"\bash" +str(timee)+".sh"
        print(bash_file_name)
        bash_file_name_linux=dir_to_store_script_linux+r"/bash" +str(timee)+".sh"
        print(bash_file_name_linux)
        #main_model_bash2=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\main_model2.sh"
        #main_model_bash_remote=# NEED TO DO THIS STILL create the new bash file
        final_file_str=rf"{final_file_str}"
        with open(bash_file_name,"w") as f4:
            f4.write(final_file_str)
        print(single_exe_process_file_name_linux)
        # may need to create the venv and install all packages so be ready for this       
        print(dir_to_store_script)
        print('BASH')
        print(dir_to_store_script_linux)
        
        
        import time
        dir_scripts_stored=remote_computer_script_dic["dir_to_store_script"]
        final_linux_script_dir=remote_computer_script_dic["final_linux_script_dir"]
        print('valuable dirs')
        print(dir_to_store_script_linux)
        print(final_linux_script_dir)
        local_mkdir_bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\mkdir_bash.sh"

        with open(local_mkdir_bash_file_name, "r") as f:
            file_str=f.read()
        file_str_list=file_str.splitlines()
        print(file_str_list)
        file_str_list[1]=fr'for dir in "{dir_to_store_script_linux}" "{final_linux_script_dir}"; do'
        final_file_str=""
        for i, linee in enumerate(file_str_list):
            if i==0:
                final_file_str=f"{linee}"
            else:
                final_file_str+=f"\n{linee}"
        local_mkdir_bash_file_name2=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\mkdir_bash2.sh"
        remote_mkdir_bash_file_name2=r"/home/jross77/Documents/mkdir_bash2.sh"

        with open(local_mkdir_bash_file_name2, "w") as f2:
            f2.write(final_file_str)
            
        relevent_file_name_and_dir_dic={"bash_file_name":bash_file_name,"bash_file_name_linux":bash_file_name_linux,"remote_mkdir_bash_file_name2":remote_mkdir_bash_file_name2,"local_mkdir_bash_file_name2":local_mkdir_bash_file_name2,"dir_scripts_stored":dir_scripts_stored}

        return relevent_file_name_and_dir_dic
    def create_and_upload_all_exe_files_to_website_server(self):
        """ """
        #input()
        #pyautogui_remote_creation_files # need to change this on widows
        #pyautogui_creation_scripts# currently used on linux
        #with open(bash_file_name,"w") as f:
        #    f.write(bash_code_to_get_run_xdo_tools_and_create_pyautogui)
        #    print('write')
        # test version!!! to see errors and inputs for tracking with subprocess
        import time
        #host_list=["192.168.2.200","192.168.2.233","192.168.2.213","192.168.2.28","192.168.2.207"]     
        dir_to_store_script=remote_computer_script_dic["dir_to_store_script"]
        dir_to_store_script_linux=remote_computer_script_dic["dir_to_store_script_linux"]
        single_exe_process_file_name_linux=remote_computer_script_dic["single_exe_process_file_name_linux"]
        code_file_name_only=remote_computer_script_dic["code_file_name_only"]
        main_model_bash=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\main_model.sh"
        with open(main_model_bash,"r") as f3:
            f3_file_str=f3.read()
        f3_file_str_list=f3_file_str.splitlines()
        f3_file_str_list[8]=fr'python3 {single_exe_process_file_name_linux}'
        final_file_str=""
        for i, linee in enumerate(f3_file_str_list):
            if i==0:
                final_file_str=f"{linee}"
            else:
                final_file_str+=f"\n{linee}"              
        bash_file_name=dir_to_store_script+r"\bash" +str(timee)+".sh"
        print(bash_file_name)
        bash_file_name_linux=dir_to_store_script_linux+r"/bash" +str(timee)+".sh"
        print(bash_file_name_linux)
        #main_model_bash2=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\main_model2.sh"
        #main_model_bash_remote=# NEED TO DO THIS STILL create the new bash file
        final_file_str=rf"{final_file_str}"
        with open(bash_file_name,"w") as f4:
            f4.write(final_file_str)
        print(single_exe_process_file_name_linux)
        # may need to create the venv and install all packages so be ready for this       
        print(dir_to_store_script)
        print('BASH')
        print(dir_to_store_script_linux)
        return bash_file_name,bash_file_name_linux
    def generate_local_pyautogui_scripts(self,keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window):
        """ """
        import time
        import os
        import re
        from datetime import date
        ### previous
        root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files"
        pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files")
        previous_active_window=re.sub(r"[^a-zA-Z0-9 ]", "", previous_active_window)# check this
        previous_active_window=re.sub(r"[ -]","_",previous_active_window)     
        self.dir_to_store_script=root_folder+"\\"+previous_active_window  
        self.dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui/"+previous_active_window
        #self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
        #self.dir_to_store_script_linux=re.sub(r"[ -]","_",self.dir_to_store_script_linux)
        timeee=time.time()    
        todayy=date.today()
        code_file_name_only=previous_active_window+str(todayy)+ "  "+str(timeee)
        code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
        code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only+".py"
        code_file_name_no_path_for_function_import=code_file_name_only
        code_file_name_path_linux=self.dir_to_store_script_linux+"/"+code_file_name_only+".py"
        if previous_active_window not in pyauto_file_dir_list:
            if previous_active_window!="":
                os.mkdir(self.dir_to_store_script)   
        remote=False
        python_file_str=self.create_pyauto_gui_function_str(self.keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux,remote=remote)
        multiprocess_pyautogui_scripts_with_tab_logic=self.tab_logic_to_generate_tabs_and_multiprocess_pyautogui_scripts(python_file_str,previous_active_window_url,multi_process_number=9)# generate somethign that could run the script 6 times at once to bottom of file
        python_file_str+=multiprocess_pyautogui_scripts_with_tab_logic  
        #try:
        self.add_to_or_create_new_python_file(python_file_str,code_file_name_path)
        single_process_file_name,single_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=False)
        multi_process_file_name,multi_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=True)
        bash_file_name,bash_file_name_linux=self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,single_process_file_name, remote=True)
        relevent_local_file_names=[code_file_name_path,single_process_file_name,single_process_file_name_linux,multi_process_file_name,multi_process_file_name_linux,bash_file_name,bash_file_name_linux]
        return relevent_local_file_names,single_process_file_name,multi_process_file_name

    def make_remote_pyautogui_creation_bash(self):
        """pyauto_remote_creation_bash """
        #self.execute_bash_creation_script()
        # make this a listender that executes these every 3 minutes to avoid errors
        # then mark those that have been created like within a seperate table  
        ### make the bash
        import time
        timee=time.time()
        dir_to_store_script=remote_computer_script_dic["dir_to_store_script"]
        dir_to_store_script_linux=remote_computer_script_dic["dir_to_store_script_linux"]
        single_exe_process_file_name_linux=remote_computer_script_dic["single_exe_process_file_name_linux"]
        code_file_name_only=remote_computer_script_dic["code_file_name_only"]
        main_model_bash=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\pyauto_remote_exe_for_remote_creation_bash.sh"
        
        
        ### OPEN FILE
        with open(main_model_bash,"r") as f3:
            f3_file_str=f3.read()
        ### edit file
        f3_file_str_list=f3_file_str.splitlines()
        f3_file_str_list[2]=fr'python3 {single_exe_process_file_name_linux}'
        
        ### regenerate file str
        final_file_str=""
        for i, linee in enumerate(f3_file_str_list):
            if i==0:
                final_file_str=f"{linee}"
            else:
                final_file_str+=f"\n{linee}"              
        bash_file_name=dir_to_store_script+r"\bash" +str(timee)+".sh"
        bash_file_name_linux=dir_to_store_script_linux+rf"/{previous_active_window_bash}" +str(timee)+".sh"

        ### write file
        final_file_str=rf"{final_file_str}"
        with open(bash_file_name,"w") as f4:
            f4.write(final_file_str)
        return bash_file_name,bash_file_name_linux,pyautogui_linux_dir

    def copy_bash_pyautogui_creation_script_over(self,bash_file_name,bash_file_name_linux,bash_linux_dir):
        """ """
        username="jross77"
        host = '192.168.2.209'# ip address here
        scp_command = [f"scp",rf"{bash_file_name}",f"jross77@{host}:{bash_linux_dir}"]# put the script you want to run here 
        self.subprocess_run_script_remotely(scp_command)
        doc2ui = [f"ssh", f"{username}@{host}","dos2unix",f"{bash_file_name_linux}"]
        self.subprocess_run_script_remotely(doc2ui)
    def upload_all_relevent_pyautogui_creation_files(self):
        """ upload the python files we will use within the listender 
        to create pyautogui from remote website server on other servers"""
        #host = '192.168.2.209'# ip address here
        ##scp_command = [f"scp","-r",rf"{dir_scripts_stored}",f"jross77@{host}:/home/jross77/Documents/pyautogui_remote_creation_files"]# put the script you want to run here 
        #p4=self.subprocess_popen_script_remotely(scp_command) 
        #self.remote_creation_python_script()
        

    def generate_and_copy_over_remotely_remote_server_pyautogui_creation_files(self,intital_upload=True):
        """ need to set up a queue for these on he remote server adding this into the script
        and then im done so ifnished run pyauto on other computers and then starts next ones
        solution maybe is run a script every 5 minutes that will run all of the newly uploaded to database pyautogui creation script
        and have this script as listener running when start psp program is running
        and this way it creates a queue
        create seperate table to track scripts that have been created
        import subprocess
for i in xrange(n):
  p = subprocess.Popen(('someprog.exe', str(i))
  p.wait()"""     
        bash_file_name,bash_file_name_linux,bash_linux_dir=self.make_remote_pyautogui_creation_bash()
        self.copy_bash_pyautogui_creation_script_over(bash_file_name,bash_file_name_linux,bash_linux_dir)
        print(' THE LISTENDER IN BUSINESS FUNCITONS WILL DO THE CREATION ON RMEOTE COMPUTER')
        if intital_upload==True:
            self.upload_all_relevent_pyautogui_creation_files()
            
    
    def create_pyautogui_file_of_inputs_and_video_2(self,previous_active_window,previous_active_window_url):
        """ this will output the pyautogui file of the session we wanted to record 
        FOR REMOTE
        this will save mouse cllick locations and scale them based on screen size
        add remote kwarg to each of the functions and modify them as necessary 
        change the main file that is to be executed in the script so it will retrieve screenshots
        and it will evenutally take information gathered and generate another pyautogui file
        that would operate like the one created with the video function
        add the vdieo function inside the script created on other computer
        so you can create the script in the other script from screenshots
        ###
        KEEP IT SIMPLE AND USE THE WEBSITE COMPUTER
        IF PROBLEMS ARISE DOWN STREAM REOCPY PROCESSS THEN
        API pyautogui into WEBSITE
        api into website or just use websit
        going to use big black and api the info to website
        for privacy concerns going to have to use the server
        saving both the 
        will use
        to make this feel better just use a singel table but on server have multiple tables so looks pretty on website and faster
        """ 
        ###
        import time
        timee=time.time()
        relevent_local_file_names,exe_file_path,multiprocess_file_path=self.generate_local_pyautogui_scripts(self.keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window)
        #upload the below info to sql locally and remotely
        #self.keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux
        # attach screenshots and times as well if you can
        ### local database
        table_name="pyautogui_page_action_table"
        column_name_data_type_dic={
            "script_name":f"{previous_active_window}_{timee}",
            "keyboard_and_mouse_press_and_time_list":f"{self.keyboard_and_mouse_press_and_time_list}",# break this up into list
          "active_window_url":previous_active_window_url,
          "active_window":previous_active_window,# only if it is a coding file otherwise just paste the active frame
          "time_stamps":timee,
          "screenshots_path":None,
          "computer_name":"msi_laptop",

          "other_associated_files":f"{relevent_local_file_names}"}
        self.insert_into_postgres_local(column_name_data_type_dic,table_name=table_name)
        ### upload to website database use this with obs
        #table_name="pyautogui_page_action_table"
        #column_name_data_type_dic={
        #    "script_name":f"{previous_active_window}_{timee}",
        # "keyboard_and_mouse_press_and_time_list":f"{self.keyboard_and_mouse_press_and_time_list}",# break this up into list
        #  "active_window_url":previous_active_window_url,
        #  "active_window":previous_active_window,# only if it is a coding file otherwise just paste the active frame
        #  "time_stamps":timee,
        #  "screenshots_path":None,
        #  "computer_name":"msi_laptop",
        #  "other_associated_files":f"{relevent_local_file_names}"}
        
        #self.upload_data_from_website_database(column_name_data_type_dic,table_name=table_name,host="192.168.2.209")
        print('to make this feel better just use a singel table but on server have multiple tables so looks pretty on website and faster')
        ### this we will upload to later with all scripts generated by pyautogui, local generated pyautogui scripts here for laptop
        #table_name="website_pyautogui_usable_script_table"
        #column_name_data_type_dic={
        # "script_name":f"{previous_active_window}_{timee}",
        #  "exe_file":exe_file_path,# only if it is a coding file otherwise just paste the active frame
        #  "multiprocess_exe_file":multiprocess_file_path,
        #  "timee":timee,
        #  "computer_name":"msi_laptop",
        #  "other_associated_files":f"{relevent_local_file_names}"}
        #self.upload_data_from_website_database(column_name_data_type_dic,table_name=table_name,host="192.168.2.209")    
        #print('DO THESE REMAINING DATABASES writes ON WEBSITE SERVER SO DONT OVERLOAD LAPTOP and makes program smooth')
        #print('DO AS LITTLE ON LAOTPN AS POSSIBLE and offload everything to other server')
        print('build obs video intake model that take video from obs and simulates the actions with pyautogui using training data recorded here')
        ### upload to big black computer database
        #table_name="pyautogui_page_action_table"
        #column_name_data_type_dic={
        #    "script_name":f"{previous_active_window}_{timee}",
        ## "keyboard_and_mouse_press_and_time_list":f"{self.keyboard_and_mouse_press_and_time_list}",# break this up into list
         # "active_window_url":previous_active_window_url,
         # "active_window":previous_active_window,# only if it is a coding file otherwise just paste the active frame
         # "time_stamps":timee,
         # "screenshots_path":None,
         # "computer_name":"msi_laptop",

         # "other_associated_files":f"{relevent_local_file_names}"}
        #self.upload_data_from_website_database(column_name_data_type_dic,table_name=table_name,host="192.168.2.43")
        
        ### big black usable script table
        #table_name="website_pyautogui_usable_script_table"
        #column_name_data_type_dic={
        # "script_name":f"{previous_active_window}_{timee}",
        #  "exe_file":exe_file_path,# only if it is a coding file otherwise just paste the active frame
        #  "multiprocess_exe_file":multiprocess_file_path,
        #  "timee":timee,
        #  "computer_name":"msi_laptop",
        #  "other_associated_files":f"{relevent_local_file_names}"}
        ### do this for obs videos
        #self.upload_data_from_website_database(column_name_data_type_dic,table_name=table_name,host="192.168.2.43")
        ###
        print("offer this as api for people do processing on big black")
        print('SET UP THE GENERATION AND CREATION FROM BIG BLACK and upload the created files to website database and big black database')
        print("this way we have options down the road to not run off website or run off big black if slow then jsut upload to big black and api in the data")
        print('use api because more secure and down stream can save on server resources if running a bunch of sites')
        print("# upload all the remote server files using the above script")
        print('TESTING THE BELOW')

        #self.generate_and_copy_over_remotely_remote_server_pyautogui_creation_files()# do this on big black


        
    def create_pyautogui_file_of_inputs_and_video(self,previous_active_window,previous_active_window_url):
        """ this will output the pyautogui file of the session we wanted to record 
        FOR REMOTE
        this will save mouse cllick locations and scale them based on screen size
        add remote kwarg to each of the functions and modify them as necessary 
        change the main file that is to be executed in the script so it will retrieve screenshots
        and it will evenutally take information gathered and generate another pyautogui file
        that would operate like the one created with the video function
        add the vdieo function inside the script created on other computer
        so you can create the script in the other script from screenshots
        ###
        will use"""
        import time
        import os
        import re
        from datetime import date
        ### previous
        root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files"
        pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files")
        previous_active_window=re.sub(r"[^a-zA-Z0-9 ]", "", previous_active_window)# check this
        previous_active_window=re.sub(r"[ -]","_",previous_active_window)     
        self.dir_to_store_script=root_folder+"\\"+previous_active_window  
        self.dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui/"+previous_active_window
        #self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
        #self.dir_to_store_script_linux=re.sub(r"[ -]","_",self.dir_to_store_script_linux)
        timeee=time.time()    
        todayy=date.today()
        code_file_name_only=previous_active_window+str(todayy)+ "  "+str(timeee)
        code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
        code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only+".py"
        code_file_name_no_path_for_function_import=code_file_name_only
        code_file_name_path_linux=self.dir_to_store_script_linux+"/"+code_file_name_only+".py"
        if previous_active_window not in pyauto_file_dir_list:
            os.mkdir(self.dir_to_store_script)   
        remote=False
        python_file_str=self.create_pyauto_gui_function_str(self.keyboard_and_mouse_press_and_time_list,previous_active_window_url,previous_active_window,code_file_name_only,code_file_name_path_linux,remote=remote)
        multiprocess_pyautogui_scripts_with_tab_logic=self.tab_logic_to_generate_tabs_and_multiprocess_pyautogui_scripts(python_file_str,previous_active_window_url,multi_process_number=9)# generate somethign that could run the script 6 times at once to bottom of file
        python_file_str+=multiprocess_pyautogui_scripts_with_tab_logic  
        #try:
        self.add_to_or_create_new_python_file(python_file_str,code_file_name_path)
        single_process_file_name,single_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=False)
        multi_process_file_name,multi_process_file_name_linux=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,multiprocessing=True)
        bash_file_name,bash_file_name_linux=self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,single_process_file_name, remote=True)
        #self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,code_file_name_no_path_for_function_import,single_process_file_name)
        #self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,code_file_name_no_path_for_function_import,multi_process_file_name)
        # save recorded key strokes and mouse presses and screenshots all indicators we can find during period on that page and time stamps etc
        # input into a gen model later for that page
        # THIS IS TODAYS PROBLEM need to create tables and then get inputs and then        
        # if its still laggy after this we will have to jsut deal with it
        # this will do all the work connecting to all the other computers etc
        # insert all this file info into the local pyautogui table
        remote_computer_script_dic=self.create_pyautogui_file_of_inputs_and_video_remote(previous_active_window,previous_active_window_url)# add this to a specific directory
        relevent_prep_file_name_and_dir_dic=self.prep_exe_files_for_website_server_pyautogui_creation(remote_computer_script_dic,timeee)
        self.run_pyautogui_creation_script_on_all_other_computers_create_script_locally_to_ensure_correct_pixels(previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,self.dir_to_store_script_linux,remote_computer_script_dic,relevent_prep_file_name_and_dir_dic,remote=remote)
        return        
        extra="""table_name="pyautogui_page_action_table"
        column_name_data_type_dic={
         "keyboard_and_mouse_press_and_time_list":"text",# break this up into list
          "active_window_url":"text",
          "active_window":"text",# only if it is a coding file otherwise just paste the active frame
          "time_stamps":"text",
          "screenshots_path":"text",
          "local_stored_pyauto_scripts":f""}  
        self.insert_into_postgres_local(column_name_data_type_dic,table_name=table_name)
        table_name="pyautogui_page_action_table"
        column_name_data_type_dic={
         "keyboard_and_mouse_press_and_time_list":"text",# break this up into list
          "active_window_url":"text",
          "active_window":"text",# only if it is a coding file otherwise just paste the active frame
          "time_stamps":"text",
          "screenshots_path":"text",
          "local_stored_pyauto_scripts":"text"}  
        self.upload_data_from_website_database(column_name_data_type_dic,table_name=table_name)
        table_name="website_pyautogui_usable_script_table"
        column_name_data_type_dic={
         "script_name":"text",# break this up into list
          "exe_file":"text",# only if it is a coding file otherwise just paste the active frame
          "multiprocess_exe_file":"text",
          "timee":"text",
          "computer_name":"text",
          "other_script_files":"text"}
        self.upload_data_from_website_database(column_name_data_type_dic,table_name=table_name)"""
        #self.create_and_upload_all_exe_files_to_website_server(previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,self.dir_to_store_script_linux,remote_computer_script_dic,bash_file_name,bash_file_name_linux,remote_computer_script_dic,timeee,remote=remote)
        #self.exe_on_website_server_pyautogui_creation_files()
        # have website send and monitor scripts running on other computer so laptop doesnt get overwhelemed?
        
        # REPLACE THIS SOME HOW FIGURE OUT BEST WAY with the thing below run it on other computer
        # run as bash script maybe?
        # or use info that we upload to database locally
        #relevent_prep_file_name_and_dir_dic=self.prep_exe_files_for_website_server_pyautogui_creation(remote_computer_script_dic,timeee)
        
        # try to do all of this remotely on another server 
        # maybe generate one big bash file and execute this on the other computer
        # this way only send one request one of current computer
        # send relevent information via database
        # then execute script on remote computer using database info having some sort of prompt
        #self.run_pyautogui_creation_script_on_all_other_computers_create_script_locally_to_ensure_correct_pixels(previous_active_window,previous_active_window_url,timeee,self.dir_to_store_script,self.dir_to_store_script_linux,remote_computer_script_dic,relevent_prep_file_name_and_dir_dic,remote=remote)
        
                # have this all viewable on webiste server
                # run the below line as a script on the remote server
            
        #except Exception as E:
        #    print(E)                
        #    print('Failed')              
        #return

        # want to create python_file_str only from this function
        #avoid tab logic entirely      
        #python_file_dic=self.construct_python_file_dic(strr_for_py_auto_function_split_lines)
        #remove all for loops add them to seperate function downstream to avoid tab logic problems
        #avoid all the tab logic with if statements and other statements and add them to functions
        #python_file_str=self.write_a_python_file_str(python_file_dic)
        #do selenium and dev tools when i have energy 
        #do what is necessary right now
        #selenium_code_str,element_to_click_and_type_with_selenium_list=self.create_selenium_equvalent_of_code_using_screenshot_info(previous_active_window_url,self.keyboard_and_mouse_press_and_time_list)
        #python_file_str+=selenium_code_str      
        #equavlent_dev_tools_selenium_code_str=self.create_equvalent_dev_tools_code_using_screenshot_info(previous_active_window_url,self.keyboard_and_mouse_press_and_time_list)
        #python_file_str+=equavlent_dev_tools_selenium_code_str
        #dont know if it will work
        # need to fix code file_name    
        #fix from import socorrect file
        #fixcodingfilename
        #remove periods
        #and remove py from fromone
       
        # add or create file in folder to automatically run the other file to test it
        # web crawl website to get site map using sleenium and requests
        # and gather data 
        # or use common crawl data
        # for either of the 3 methods selenium web tools or whatever
        # and have option to subsistute in other scripts in between
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
    def use_problem_solving_coding_program_to_identify_similar_problems_based_upon_context(self):
        """NEED TO ADD THIS in for FOR automating CODING """
    # use problem solving coding progrtamt o identify similar problems based upon context on the page
    # and the previous creenshot information and sugges tthis and allow you to copy paste these into the function
    # or previous functions
    
    
    def generate_and_store_problem_solving_program_data(self):
        """ """
        screen_shot_paths=self.generate_screen_shot_paths()
        template_paths=self.generate_template_paths()
        code_file_name_paths=self.generate_code_file_name_paths()
        code_found_on_screen_per_click=self.generate_code_found_on_screen_per_click()
        text_found_on_screen_per_click=self.generate_text_found_on_screen_per_click()
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
        screen_shot_paths=self.generate_screen_shot_paths()
        
        table_name="problem_solving_tree"
        problem_solving_program_dic={
            "screen_shot_paths":screen_shot_paths,
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
        self.store_value_in_sql_table(problem_solving_program_dic,table_name)
        # use problem solving data and integrate into different gui programs or website
        # to display and access the results
        
    def generate_and_store_coding_problem_solving_program_data(self):
        """ """
        screen_shot_paths=self.generate_screen_shot_paths()
        template_paths=self.generate_template_paths()
        code_file_name_paths=self.generate_code_file_name_paths()
        code_found_on_screen_per_click=self.generate_code_found_on_screen_per_click()
        text_found_on_screen_per_click=self.generate_text_found_on_screen_per_click()
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
        problem_solving_program_dic_coding={
            "screen_shot_paths":screen_shot_paths,
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
        self.store_value_in_sql_table(problem_solving_program_dic_coding,table_name)
        # use problem solving data and integrate into different gui programs or website

        
    def generate_and_store_3d_problem_solving_program_data(self):
        """ """
        screen_shot_paths=self.generate_screen_shot_paths()
        template_paths=self.generate_template_paths()
        code_file_name_paths=self.generate_code_file_name_paths()
        code_found_on_screen_per_click=self.generate_code_found_on_screen_per_click()
        text_found_on_screen_per_click=self.generate_text_found_on_screen_per_click()
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
        material_list=self.generate_model_generation_of_mateiral_or_tool_for_problem()
        table_name="three_d_problem_solving_tree"
        # use model to generate 3d model of image
        # geenrate when any image appears on screen and save the 3d model
        dicitonary_of_values={
        "3-d model_generation_of_mateiral_or_tool_for_problem":material_list,     
            "screen_shot_paths":screen_shot_paths,
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

        
    def generate_and_store_law_problem_solving_program_data(self):
        """ """
        screen_shot_paths=self.generate_screen_shot_paths()
        template_paths=self.generate_template_paths()
        code_file_name_paths=self.generate_code_file_name_paths()
        code_found_on_screen_per_click=self.generate_code_found_on_screen_per_click()
        text_found_on_screen_per_click=self.generate_text_found_on_screen_per_click()
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
        
        
        table_name="legal_problem_solving_tree"
        dicitonary_of_values={
            "screen_shot_paths":screen_shot_paths,
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
        self.screens_where_screen_shots_wanted_list=["Mozilla Firefox","Google Chrome"]
        self.keyboard_and_mouse_press_and_time_list=[]
        self.ctrl_command_list=["ctrl_c","ctrl_a"]
        self.ctrl_activated=False
        self.for_loop=False
        self.while_loop=False
        self.tab_skip=False
        self.start_recording=False
        self.last_input=None
        self.move_to_list_counterr=0
        self.stored_mouse_move_list=[]
        self.previous_active_window_name=""
        self.active_window_name=""
        self.previous_active_window=""

        self.active_window_url=""
        self.counterrrr=0
        self.last_screen_shot_taken_time=0
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        # firefox history and chrome history api to get website name?
        self.init_glossary_window()
        with  keyboard.Listener(on_press=self.keyboard_on_press_pynput, on_release=self.keyboard_pynput_release) as self.keyboard_listener:
            self.mouse_listener = mouse.Listener(on_click=self.mouse_pynput_on_click,on_scroll=self.on_mouse_scroll,on_move=self.on_mouse_move)
            self.mouse_listener.start()
            self.mouse_listener2 = mouse.Listener(on_click=self.mouse_pynput_on_click2)
            self.mouse_listener2.start()
            self.window.mainloop()# program will end here
            self.mouse_listener.stop()
            self.mouse_listener2.stop()
            # keep it simple
            # finish tomorrow
            
            #have it so only start recroding key presses when press  specific button click and end with button click
            # try to get these key strokes to run automcially on other computers and send to server
            # and try to be able to start script on other computer from website on server using database
            # but otherwise just get this creation program so can run manually on other computers
            #start recording screen with OBS use video data later
            # have a script running accessing varius llm done by the day after tomorrow
            
            
            
            
            # what might be better is to record a certain amount of actions then
            # like in version 5 copy it to other computers using this strcture
            # not just record arebitrary clicking
            # because wont be efficent
            # but recrod screesnhots
            # so revert version 5 adding a button to start the program and recoridng clicks
            # then a button to shut it off and send it to all other computers
            
        

            
       
            
        # constantly be checking for the active window
        
        # then use this information to help build downstream application
        
        
        

            #if event == keyboard.Key.num_lock:
            #    self.window.destroy()
            #try: 
            #    self.keyboard_listener.join()
                

            #except Exception as e:
            #         print(e)
            #         print('Done'.format(e.args[0]))
