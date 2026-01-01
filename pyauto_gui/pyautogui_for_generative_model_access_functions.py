# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 05:29:05 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
# i think we should generate a new script file instead of adding to an existing one
# each time so we dont overwrite and ruin existing scripts
class pyautogui_for_generative_model_access_functions():
    def __init___(self):
        """ """
        import time
        from selenium import webdriver
        import pyautogui
        from selenium.webdriver.common.keys import Keys

    def mini_screen_scroll(self,pressed_x_position,pressed_y_position,released_y_position):
        """scroll the length and direction between the  mouse press and mouse release """
        amount_to_scroll=int(pressed_y_position)-int(released_y_position)
        drag_to_command=f"\npyautogui.moveTo({pressed_x_position}, {pressed_y_position})\ntime.sleep(1)\npyautogui.scroll({amount_to_scroll})"
        return drag_to_command
    #f"\npyautogui.dragTo({recorded_mouse_y_position}, {pressed_y_position}, button='left')"
    #drag_to_command=f"\npyautogui.dragTo({recorded_mouse_y_position}, {pressed_y_position}, button='left')"
        # from intital y position to next mouse why position
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
        #drag_to_command=f"\npyautogui.dragTo({recorded_mouse_y_position}, {int(screen_height)+int(recorded_mouse_y_position)}, button='left')"
        return drag_to_command
    # i think just full page scroll if we press a specific button
    # otherwise copy mouse scroll
    # if x and y is very different from last mouse click
    # if mouse start if different than mouse end
    # this will be downstream so we will only need to use list not doing this on the spot

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
     #import win32clipboard
     #win32clipboard.OpenClipboard()
     #data = win32clipboard.GetClipboardData()
     #win32clipboard.CloseClipboard()
     # set clipboard data
     #win32clipboard.OpenClipboard()
     #win32clipboard.EmptyClipboard()
     #win32clipboard.SetClipboardText('testing 123')
     #win32clipboard.CloseClipboard()
     # get clipboard data

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
        strr_for_py_auto_script+="\ntime.sleep(15)"
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
                 # this should solve hte problem of code not being super usable because
                 # we subbed out commas and such to store it
                 sql_data=str(sql_data)
                 sql_data=sql_data.replace("^","\'")
                 sql_data=sql_data.replace("&","\"")
                 sql_data=sql_data.replace("~",",")
                 sql_data=sql_data.replace("?","'")
                 self.search_data_dic[column].append(sql_data) 
         return self.search_data_dic
    def search_data_dic_for_newest_time_stamp(self,search_data_dicc,search_prompt):
        """ get the single newest search result for a sql function"""
        #column_list=["code_base_function","code_file_name","time_stamp"]
        #final_line_of_code_match_list=[]
        time_stamp_list=search_data_dicc["time_stamp"]
        code_base_function_list=search_data_dicc["code_base_function"]
        single_function_str=""
        highest_time_stamp=0
        for i6, code_base_function,time_stamp in zip(range(len(time_stamp_list)),code_base_function_list,time_stamp_list):
            if float(time_stamp)>float(highest_time_stamp):
                highest_time_stamp=time_stamp
                single_function_str=code_base_function
        return single_function_str
    def create_new_autogui_file(self,strr_for_py_auto_script):
        """ """
        strr_for_py_auto_script=r"# -*- coding: utf-8 -*-\n"+"Created on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy"
        strr_for_py_auto_script+="\nclass pyautogui_functions():"
        strr_for_py_auto_script+="\ndef __init__(self):"
        strr_for_py_auto_script+="\nprint('start_pyautogui_class')"
        strr_for_py_auto_script+="\ndef pyauto_gui_function0(self,prompt_list):"
        return strr_for_py_auto_script
    def add_to_an_existing_auto_gui_file(self,strr_for_py_auto_script):
        import re
        import os
        count_number_of_functions_in_file=re.compile(r"def ")
        code_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\pyautogui_functions.py"
        code_file_name_copy=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\pyautogui_functions_copy.py"
        pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files")
        with open(code_file_name,"r") as original_file:
            file_str=original_file.read()
        with open(code_file_name_copy,"w")as copy_file:  # save a copy since we are overwriting this later
            copy_file.write(file_str) 
        function_found_list=re.findall(count_number_of_functions_in_file,file_str)
        function_found_list_len=len(function_found_list)
        print(f"function_found_list:{function_found_list}")
        strr_for_py_auto_script=file_str
        strr_for_py_auto_script+=f"\ndef pyauto_gui_function{function_found_list_len}(self,prompt_list):" 
        return strr_for_py_auto_script
    def add_mouse_code_lines_to_pyautogui_file(self,strr_for_py_auto_script,keyy,keyboard_or_mouse,screen_height,time_from_previous_action,mouse_scroll_change_for_full_page_scroll=360):
        """this produces the mouse presses actions """
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
        self.screenshot_name=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot{timee}.png"
        screenshot.save(self.screenshot_name)
        return self.screenshot_name
        #screenshot.close()
        #def img_text(file):
        #center_of_image=pyautogui.locateCenterOnScreen(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\test2.png')
        #print(center_of_image)
        #print("the world is here")
    
    # create a template
    # do not continue until you see this template
    # continue when you see this template
    # need to add these buttons following the period
    # or add two seperate buttons
    # or change period button 

    # then deal with scroll

    def create_template_screenshot(self,screen_shot_name,top_left_mouse_click,bottom_right_mouse_click):
        """take a partial screenshot to get the template image """
        ### TESTIGN TO SEE IF THIS WORKS NEXT
        from PIL import ImageGrab
        from PIL import Image
        import pytesseract
        import re
        # just have to get this right now
        #img_right_area = (400, 0, 800, 600)
        #1720549529.3786867
        screenshot=Image.open(screen_shot_name)
        print(screen_shot_name)
        # extract so we have a matching time know they are connected
        time_stamp_of_screenshot=re.search(r"\d+\.\d+",screen_shot_name).group(0)
        top_left_mouse_click=re.search(r"\(\d+, \d+\)",top_left_mouse_click).group(0) 
        mouse_cordinate_split=re.search("(\d+), (\d+)",top_left_mouse_click)
        top_left_x=mouse_cordinate_split.group(1)
        top_y=mouse_cordinate_split.group(2)
        bottom_right_mouse_click=re.search(r"\(\d+, \d+\)",bottom_right_mouse_click).group(0) 
        mouse_cordinate_split=re.search("(\d+), (\d+)",bottom_right_mouse_click)
        right_x=mouse_cordinate_split.group(1)
        bottom_y=mouse_cordinate_split.group(2)
        #box = (top_left_x, top_y, right_x, bottom_y) #(left_x, top_y, right_x, bottom_y)
        print(f"LOCATION OF SCREENSHOT({int(top_left_x)}, {int(top_y)}, {int(right_x)}, {int(bottom_y)}")
        img_template = screenshot.crop((int(top_left_x), int(top_y), int(right_x), int(bottom_y)))
        template_location_str=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template{time_stamp_of_screenshot}.png"
        img_template.save(template_location_str) 
        # screen shot we want to add to the 
        return template_location_str
    #top_left_x, top_y =top_left_mouse_click
    #right_x, bottom_y=bottom_right_mouse_click # need to still make these work find out how to parse thios
    #top_left_x, top_y =top_left_mouse_click
    #right_x, bottom_y=bottom_right_mouse_click # need to still make these work find out how to parse thios
    #box = (top_left_x, top_y, right_x, bottom_y) #(left_x, top_y, right_x, bottom_y)
        #im = ImageGrab.grab(box_corindates) # grabs the box cordinates
        #text = pytesseract.image_to_string(im)
        # add this to mouse funcitons to take a partial screenshot and save the template
        # of the partial screenshot taken to use later in the code
        # and then create button for whole screenshot
# update text to your GUI
    
    def check_for_template(self,template_location):
        """we will save the screenshot to disk and then upload it using cv2 imread """
        # get the image in retime and simply use the template that we store
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
    def find_template2(self,template_location): # we are no longer using this but is good reference
        """we will save the screenshot to disk and then upload it using cv2 imread """
        # get the image in retime and simply use the template that we store
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
        loc = np.where(res >= threshold) # this gets us any point that has a .9 or above
        #loc = np.where(res >= threshold) # this gets us any point that has a .9 or above
        if loc[0].any(): # this is an array that looks liek this [1,2,3,4,5],[1,2,3,4]
            # i thinkt he two arrays returned are the x and y values that match this button
                print(loc)
                print(loc[0][0])
                print(loc[0][1])
                print(int(loc[0][0]))#x
                print(int(loc[1][0]))#y
                pyautogui.click(int(loc[1][0]+w/2),int(loc[0][0]+h/2))
                
                # array one is the y corindate
                # array two is the x corindate
                # from resulting array from np.where [[1,2,3,4],[1,2,3,4]]
                # the four values in the arrays are the  found x and y corindate respectively 
                # for the image
                
            # add a self.template button
            # store template files in a directory
            # and access
            
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
        # will have to check this again at one point might not be working
        if "pyautogui_functions.py" in pyauto_file_dir_list:
            print("file does exist")
            strr_for_py_auto_script=self.add_to_an_existing_auto_gui_file(strr_for_py_auto_script)
            print(strr_for_py_auto_script)
        else:
            print("file does not exist")
            strr_for_py_auto_script=self.create_new_autogui_file(strr_for_py_auto_script)  
            print(strr_for_py_auto_script)  
        #if len(pyauto_file_dir_list)>0:# the file already exists so we add an additional function to it
        #else:# otherwise create the file
        #    strr_for_py_auto_script=self.create_new_autogui_file(strr_for_py_auto_script)
        strr_for_py_auto_script=self.import_packages_autogui_file(strr_for_py_auto_script)
        #print(strr_for_py_auto_script)
        #print('start of loop')
        print(keyboard_and_mouse_press_and_time_list)
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
            ### this is the time stuff to add we will remove this and instead use template creator to guide us on timing
            # it is cleaner this way
            #if previous_time:
            #    time_from_previous_action=round(timee-previous_time,2)#round
                #print(strr_for_py_auto_script)
                #print(f"\ntime.sleep({10})")
            #    strr_for_py_auto_script+=f"\ntime.sleep({7.5})"
                #strr_for_py_auto_script+=f"\ntime.sleep({time_from_previous_action})"
            # need to fix looping
            previous_time=timee
            if keyboard_or_mouse=="template_creator":
                screen_shot_name=keyy[0]
                screen_shot_command=keyy[1]
                # grab the four mouse clicks after
                top_left_mouse_click=keyboard_and_mouse_press_and_time_list[i+1][1]
                bottom_right_mouse_click=keyboard_and_mouse_press_and_time_list[i+3][1]
                self.template_location_str=self.create_template_screenshot(screen_shot_name,top_left_mouse_click,bottom_right_mouse_click)# creating template in past time
                if screen_shot_command=="wait_till_image_gone":
                    strr_for_py_auto_script+="f\nself.wait_till_template_gone(self,r'self.template_location_str')"
                if screen_shot_command=="wait_till_image_present":
                    strr_for_py_auto_script+="f\self.wait_till_template_present(self,r'self.template_location_str')"
                self.block_four_clicks_switch=True
                continue 
            if keyy in keys_to_look_for:
                strr_for_py_auto_script+=dictionary_of_keyys[keyy]
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                if i==len(keyboard_and_mouse_press_and_time_list)-1:
                    strr_for_py_auto_script+=f"\nreturn saved_screen_shots_text_list"     
                continue
            if keyboard_or_mouse=="loop_ender":
                strr_for_py_auto_script+=f"\nend_the_loop"
                continue
            if keyboard_or_mouse=="keyboard":
                # if its the first time
                #print('KEY BOARD')
                strr_for_py_auto_script+=f"\npyautogui.write(prompt)" 
                #print('hi')
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                if i==len(keyboard_and_mouse_press_and_time_list)-1:# trying to find a place to put return statement
                    strr_for_py_auto_script+=f"\nreturn saved_screen_shots_text_list"  
                continue
            if keyboard_or_mouse=="mouse_press" or keyboard_or_mouse=="mouse_release":
                #strr_for_py_auto_script,keyy,mouse_scroll_change_for_full_page_scroll,keyboard_or_mouse,screen_height,time_from_previous_action
                strr_for_py_auto_script=self.add_mouse_code_lines_to_pyautogui_file(strr_for_py_auto_script,keyy,keyboard_or_mouse,self.screen_height,time_from_previous_action)
                self.previous_keyboard_or_mouse=keyboard_or_mouse 
                if i==len(keyboard_and_mouse_press_and_time_list)-1:# trying to find a place to put return statement
                    strr_for_py_auto_script+=f"\nreturn saved_screen_shots_text_list"
        # TEST THIS LATER
        #print(strr_for_py_auto_script)
        #print('first loop finished')
        for function_name in add_additional_functions:
            #print(f"function_name: {function_name}")
            function_name=re.sub("\(","\\(",function_name)
            #print(f"function_name: {function_name}")
            function_name=re.sub("\)","\\)",function_name) # will need to test to see if this works
            # check for string in current strr for py autoscript
            #print(f"function_name: {function_name}")
            function_result=re.search(function_name,strr_for_py_auto_script)
            if function_result:
                print("FOUND")
                continue
            else:
                print("NOT FOUND")                
                strr_for_py_auto_script=self.add_function_str_from_sql_to_file(function_name,column_list,strr_for_py_auto_script)
                #print(strr_for_py_auto_script)
                continue
            #error is here need to go through function and 
            # fix this
            # to improve output results
        strr_for_py_auto_function_split_lines=strr_for_py_auto_script.splitlines()
        #print(strr_for_py_auto_function_split_lines)
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
    # previous funcitons indent is being screwed up
    # being added tabs
    
		#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR	esseract.exe'
        # fixing pytesseract because it has colons
    def remove_single_tab(self,tab_count):
        """ remove a single tab from the tab count list """
        #print(f"length tab count: {len(tab_count)}")
        tab_count_len=len(tab_count)-1
        #print(f"length tab count: {tab_count_len}")
        tab_count_list=[" "]*tab_count_len
        #print(f"length tab count: {len(tab_count_list)}")
        tab_count="".join(tab_count_list)
        return tab_count
    # we need to take screenshots
    # to get button position
    def write_a_python_file_str(self,class_dic_function_list_function_dic_code_list_code,new_file=True):
        """ write a python file from inputs adding in the tabs and the newline characters to format may not be purpose though"""
		#h, w = template.shape[:-1]
        #dealing with slice
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
                        #if loop_switch==True:
                        #    print(code_line)
                        #    tab_count=self.remove_single_tab(tab_count)
                        #    python_file_str+=f"\n{tab_count}{code_line}"
                        #    tab_count+="\t"
                        #    loop_switch=False
                        #    continue
                        #if loop_switch==False:
                             python_file_str+=f"\n{tab_count}{code_line}"
                             tab_count+=" "
                             loop_switch=True
                             continue
                         
                    if line_type=="if_else":
                        
                        if if_else_switch==False:
                             #print(code_line)
                             #print("if_else_switch")
                             python_file_str+=f"\n{tab_count}{code_line}"
                             tab_count+=" "
                             #if_else_switch=True
                             continue
                        #if if_else_switch==True:
                        #     print(code_line)
                        #     print("if_else_switch")
                        #     print("TRUE")
                        #     print(len(tab_count))
                        #     tab_count=self.remove_single_tab(tab_count)
                        #     print(len(tab_count))
                        #     python_file_str+=f"\n{tab_count}{code_line}"

                         #    print(tab_count)
                         #    tab_count+="\t"
                         #    print(tab_count)

                          #   if_else_switch=False
                          #   continue
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
        print(text)
        return text          
    ### building chatgpt and other generative ai pyautogui pipelines
    def send_text_to_server(self):
        """we will make a website and send the data to it once we have the time """
    def add_new_line_character(self, inputt_str):
        """ """
        output_str=inputt_str+"\n"
        return output_str
        
        
    def add_function_str_from_sql_to_file(self,search_prompt,column_list,strr_for_py_auto_script):
        """upload the function to the strring for pyautogui"""
        #error is here need to go through function and 
        # fix this
        # to improve output results
        # uploading wrong function
        # want to get it to upload the right one
        #next problem to solve
        print("START OF ADD FUNCTION")
        search_result_from_new_database=self.upload_from_sql_single_result(search_prompt,column_list)
        print(search_result_from_new_database)
        search_data_dic=self.process_sql_data_for_searches(search_result_from_new_database,column_list)
        print(search_data_dic)
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
        strr_for_py_auto_script+="\n"+rf"\ntemplate_present_value,h, w=self.check_for_template(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png')"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
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
        strr_for_py_auto_script+=f"\nwhile True:"
        strr_for_py_auto_script+=f"\ntime.sleep(1)"
        strr_for_py_auto_script+=f"\npyautogui.click(1700, 971)"
        strr_for_py_auto_script+=f"\ntemplate_present_value,h, w=self.check_for_template(template_path)"
        strr_for_py_auto_script+=f"\nif template_present_value[0].any():"
        strr_for_py_auto_script+=f"\npyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))"
        strr_for_py_auto_script+=f"\nelse:"
        strr_for_py_auto_script+=f"\ncontinue"
        strr_for_py_auto_script+=f"\ntime.sleep(2)"
        return strr_for_py_auto_script
        # need to fix search to use this to allow for it in glossary dic
        single_newest_function_str=self.search_data_dic_for_newest_time_stamp(search_data_dic,search_prompt)
        print(single_newest_function_str)
        function_line_list=single_newest_function_str.splitlines()
        print(function_line_list)
        for line in function_line_list:
            line=line.strip()
            strr_for_py_auto_script+=f"\n{line}"
        return strr_for_py_auto_script
    ### click button once found
    def wait_till_template_present(self,template_path):
        import pyautogui
        import time
        from PIL import ImageGrab
        import numpy as np
        import pytesseract
        while True:
         time.sleep(1)
         pyautogui.click(1700, 971)
         template_present_value,h, w=self.check_for_template(template_path)
         print(template_present_value)
         if template_present_value[0].any():
          pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
          break
         else:
          continue
        time.sleep(2)
        
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
    
    def screenshot_saved_text_and_scroll_down_whole_page(self):
        import pyautogui
        import time
        from PIL import ImageGrab
        import numpy as np
        import pytesseract
        saved_screen_shots_text_list=[]
        while True:# testing this and done
             print('found')
             screenshot = ImageGrab.grab()
             img1 = np.array(screenshot)
             text = pytesseract.image_to_string(img1)
             print(text)
             saved_screen_shots_text_list.append(text)
             pyautogui.moveTo(1919, 212)
             time.sleep(1)
             pyautogui.scroll(-300)
             # previous the previous screenshot is the same
             # make a temporary template
             template_present_value,h, w=self.check_for_template(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png")# scrolling down
             if template_present_value[0].any():
                 print('match')
                 break
             else:
                 img_template = screenshot.crop((177, 306, 1188, 448))
                 print('new save')
                 img_template.save(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\template_temporary.png")
                 continue
    def wait_till_template_gone(self,template_path): 
        import pyautogui
        import time
        from PIL import ImageGrab
        import numpy as np
        import pytesseract
        while True:
         time.sleep(3)
         template_present_value,h, w=self.check_for_template(template_path)# loading screen
         print(template_present_value)
         if template_present_value[0].any():
              print('found')
              time.sleep(1)
              pyautogui.click(1700, 971)
              continue
         else:
           template_present_value,h, w=self.check_for_template(template_path)# attemtping to reconnect
           if template_present_value[0].any(): 
               print('found')
               time.sleep(1)
               pyautogui.click(1700, 971)
               continue
           else:
               time.sleep(3)
               template_present_value,h, w=self.check_for_template(template_path)# loading screen
               print(template_present_value)
               if template_present_value[0].any():
                    print('found')
                    time.sleep(1)
                    pyautogui.click(1700, 971)
                    continue
               else:
                   break      
        time.sleep(5)
        
             
    def scroll_up_whole_page(self):
        import pyautogui
        import time
        from PIL import ImageGrab
        import numpy as np
        import pytesseract
        """ """
        for i in range(30):# test this and done
                pyautogui.moveTo(1919, 212)
                pyautogui.scroll(1000)# scroll to the top
                print("scroll")
        ### screenshot and scroll down
   
class pyautogui_for_generative_model_access_functions_child(pyautogui_for_generative_model_access_functions):
    def __init___(self):
        """ """
    
    def mouse_pynput_on_click(self,x, y, button, pressed):
        """record on click elements """
        from pynput import mouse
        import time 
        if self.keyboard_and_mouse_press_and_time_list:
            last_input=self.keyboard_and_mouse_press_and_time_list[-1][0]
            if last_input=="mouse_press":
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_release",'{0}{1}'.format('Pressed',(x, y)),time.time()])
                return
            else:
                self.keyboard_and_mouse_press_and_time_list.append(["mouse_press",'{0}{1}'.format('Pressed',(x, y)),time.time()])  
                return
        else:
            self.keyboard_and_mouse_press_and_time_list.append(["mouse_press",'{0}{1}'.format('Pressed',(x, y)),time.time()])      
        print('{0} at {1}'.format('Pressed' ,(x, y)))
        
    def keyboard_on_press_pynput(self,event):
        """ """
        from pynput import keyboard
        import time
        if event == keyboard.Key.esc:# do all the work in here with downstream functions
            code_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\pyautogui_functions.py"
            strr_for_py_auto_function_split_lines=self.create_pyauto_gui_function_str(self.keyboard_and_mouse_press_and_time_list)
            python_file_dic=self.construct_python_file_dic(strr_for_py_auto_function_split_lines)
            python_file_str=self.write_a_python_file_str(python_file_dic)
            self.add_to_or_create_new_python_file(python_file_str,code_file_name)
            print("STOP this program using num lock")  
        try:
            pressed_button='{0}'.format(event.char)
            print(pressed_button)
            if self.keyboard_and_mouse_press_and_time_list:
                # exit loop symbol?
                if pressed_button=="]":
                     print("loop-ender")
                     self.keyboard_and_mouse_press_and_time_list.append(["loop_ender","loop_ender",time.time()])
                     return

                    
                if pressed_button==".": #can't loop on the first click 
                     print("wait_till_image_gone") # save screenshot when this button is clicked
                     #if self.while_loop==True:
                     #    #end while loop
                     #    return
                     screenshot_name=self.take_screenshot_and_grab_text()
                     self.keyboard_and_mouse_press_and_time_list.append(["template_creator",[screenshot_name,"wait_till_image_gone"],time.time()])
                     return
                     

                if pressed_button==";":# wait till see image and click
                    print("wait_till_image_present") # save screenshot when this button is clicked
                    screenshot_name=self.take_screenshot_and_grab_text()
                    self.keyboard_and_mouse_press_and_time_list.append(["template_creator",[screenshot_name,"wait_till_image_present"],time.time()])
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
            if str('{0}'.format(event))=="Key.enter":
                self.keyboard_and_mouse_press_and_time_list.append(["keyboard","enter",time.time()]) 
            if str('{0}'.format(event))=="Key.ctrl_l":
                self.ctrl_activated=True
                print('ctrl_activated')
            #if '{0}'.format(event)=="key.ctrl_l":
            #    print('hi')
            
            #if str('{0}'.format(event))=="ctrl_l":
            #    print("it worked")
                #record it and then record next key stroke
                # and if this is a or c then record
                # it as a control a or c command
    def keyboard_pynput_release(self,event):
        from pynput import keyboard
        listt=[]
        if event == keyboard.Key.num_lock:
            self.mouse_listener.stop()
            return False  #press shift to Stop listener
        #self.keyboard_listener.stop()
        #self.global_hot_keys_listener.stop()
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

class pyautogui_for_generative_model_access_functions_gchild(pyautogui_for_generative_model_access_functions_child):
    def __init___(self):
        """ """
        import pyautogui
        self.screen_size=pyautogui.size()
        self.screen_height=self.screen_size[1]
        self.screen_width=self.screen_size[0]
    def init_pyauto_gui_creation_script_program(self):
        """ """
        from pynput import keyboard
        from pynput import mouse
        import time
        import os
        import logging
        from pynput.mouse import Listener
        self.keyboard_and_mouse_press_and_time_list=[]
        self.ctrl_command_list=["ctrl_c","ctrl_a"]
        self.ctrl_activated=False
        self.for_loop=False
        self.while_loop=False

        with  keyboard.Listener(on_press=self.keyboard_on_press_pynput, on_release=self.keyboard_pynput_release) as self.keyboard_listener:
            #self.global_hot_keys_listener= keyboard.GlobalHotKeys({ '<ctrl>+c': self.on_activate_ctrl_c,'<ctrl>+a': self.on_activate_ctrl_a})
            #self.global_hot_keys_listener.start()
            self.mouse_listener = mouse.Listener(on_click=self.mouse_pynput_on_click)
            self.mouse_listener.start()
            try: 
                self.keyboard_listener.join()
            except Exception as e:
                     print(e)
                     print('Done'.format(e.args[0]))

        # what is the problem i wan tto solve
        

#pyautogui_for_generative_model_access a1.1.1.1.1.1