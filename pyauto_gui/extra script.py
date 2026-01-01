def create_pyautogui_remote_computer_creation_scripts(self,previous_active_window,previous_active_window_url):
    """
    this will save mouse cllick locations and scale them based on screen size
    add remote kwarg to each of the functions and modify them as necessary 
    change the main file that is to be executed in the script so it will retrieve screenshots
    and it will evenutally take information gathered and generate another pyautogui file
    that would operate like the one created with the video function
    add the vdieo function inside the script created on other computer
    so you can create the script in the other script from screenshots"""
    # copy functions used in the above code to create other pyautogui file
    # copy as much as possilbe to save on work
    # change the main file that is to be ex
    import time
    import os
    import re
    from datetime import date
    root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_server_files"
    pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_server_files")
    previous_active_window=re.sub(r"[^a-zA-Z0-9 ]", "", previous_active_window)# check this
    previous_active_window=re.sub(r"[ -]","_",previous_active_window)     
    self.dir_to_store_script=root_folder+"\\"+previous_active_window  
    self.dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui_remote_server_files/"+previous_active_window
    self.dir_to_store_script=re.sub(r"[ -]","_",self.dir_to_store_script)
    self.dir_to_store_script_linux=re.sub(r"[ -]","_",self.dir_to_store_script_linux)
    if previous_active_window not in pyauto_file_dir_list:
        os.mkdir(self.dir_to_store_script)      
    python_file_str=self.create_pyauto_gui_function_str(self.keyboard_and_mouse_press_and_time_list,previous_active_window_url, remote=True)
    #print(python_file_str)
    todayy=date.today()
    timeee=time.time()    
    code_file_name_only=previous_active_window+str(todayy)+ "  "+str(timeee)
    code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
    code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only+".py"
    code_file_name_no_path_for_function_import=code_file_name_only
    self.add_to_or_create_new_python_file(python_file_str,code_file_name_path)
    single_process_file_name=self.add_or_create_pyautogui_function_exe_files(self.dir_to_store_script,code_file_name_no_path_for_function_import,multiprocessing=False, remote=True)
    bash_file_name,bash_file_name_linux=self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,self.dir_to_store_script_linux,code_file_name_no_path_for_function_import,single_process_file_name, remote=True)
    #self.add_or_create_business_processes_pre_made_bash_function_file(self.dir_to_store_script,code_file_name_no_path_for_function_import,multi_process_file_name)
    # to multiprocess we will just
    remote_computer_script_dic={"bash_file_name":bash_file_name,"single_process_file_name":single_process_file_name,"dir_to_store_script":self.dir_to_store_script}
    return remote_computer_script_dic
    
    
   
    # execute the pyautogui script within the bash command
    #also ssh over the pyautogui script to execute to
    #create the other pyautogui script
    # write script info back to server on remote computer
    # to the pyautogui exe table
    # retrieve this information on this local computer
    self.create_pyautogui_script_and_exe_script_to_create_other_script()
    self.write_created_script_info_to_remote_pyautogui_exe_table()
    self.translate_click_info_into_exe_script()
    self.add_pyautogui_creation_to_pyautogui_script_to_create_another_file()# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 06:53:21 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

