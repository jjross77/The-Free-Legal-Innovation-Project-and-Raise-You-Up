# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 08:04:30 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

class record_screen_for_additonal_problem_data_and_send_to_sql_l():
    def __init__(self):
        """ """
        import time
        
    def suggest_based_on_key_strokes_methods_and_strats_to_use_and_problems_to_solve(self):
        """and suggest other things like coding problem trees etc """
    def record_time_taken_to_solve_problems_based_on_page_on_timing_and_use_to_choose_better_strats(self):
         """  basically record the time we are stuck on any given window"""
         import time
         
    

         
         
    def record_screen_for_additonal_problem_data_and_send_to_sql_function(self,none):
        """ """
        # automcially when working on problems show certain methods from recorded data
        from pynput import mouse
        import time
        print('meow')
        from pynput.mouse import Listener
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.counterr=0
        self.problem_recorded=""
        self.last_screen_shot_taken_time=0
        self.keyboard_and_mouse_press_and_time_list=[]
        self.ctrl_activated=False
        self.for_loop=False
        self.while_loop=False
        self.tab_skip=False
        self.last_input=None
        self.move_to_list_counterr=0
        self.stored_mouse_move_list=[]
        self.previous_active_window_name=""
        self.mouse_listener = mouse.Listener(on_click=self.mouse_pynput_on_click)
        self.mouse_listener.start()
        print('mouse')
        
        #self.window.mainloop()# program will end here
        #self.mouse_listener.stop()
    def screen_record(self,screen_shot_time):
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
            screen_recording_info_dic={"path_to_screenshot":path_to_frame,"active_window_name":active_window_name,"timee":query_time}
            self.last_screen_shot_taken_time=query_time
        else:
            # dont save the screenshot to save on space on computer
            screen_recording_info_dic={"path_to_screenshot":"","active_window_name":active_window_name,"timee":query_time}
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
     
 
    def mouse_pynput_on_click(self,x, y, button, pressed):
        """record on click elements """
        # get mouse scroll
        from pynput import mouse
        import time 
        self.counterr+=1
        print(self.counterr)
        if self.counterr>=4:
            if button == mouse.Button.left:
                query_time= time.time()
                screen_recording_info_dic=self.screen_record(query_time)
                self.upload_problem_screen_information_to_sql(screen_recording_info_dic)
                self.update_problem_solving_program_to_problem_being_solved_based_on_screenshot_info_nn(screen_recording_info_dic)
                self.counterr=0
                
            
        
        
    
    def update_problem_solving_program_to_problem_being_solved_based_on_screenshot_info_nn(self,screen_recording_info_dic):
        """ """
        
        
        
    def upload_problem_screen_information_to_sql(self,screen_recording_info_dic):
        """ """
        import time
        import psycopg2
        path_to_screenshot=screen_recording_info_dic["path_to_screenshot"]
        active_window_name=screen_recording_info_dic["active_window_name"]
        timee=screen_recording_info_dic["timee"]

        path_to_screenshot=self.clean_strs_before_input_into_sql(path_to_screenshot)
        active_window_name=self.clean_strs_before_input_into_sql(active_window_name)
        timee=self.clean_strs_before_input_into_sql(timee)

        # need to make sure not to over write  values here

        self.cur.execute( f""" INSERT INTO problem_solving_screen_recording_table (problem_question_or_task,path_to_screenshot,active_window_name,timee)
                     VALUES ('{str(self.problem_recorded)}','{str(path_to_screenshot)}','{str(active_window_name)}','{str(timee)}');""")
            
        self.conn.commit()
        