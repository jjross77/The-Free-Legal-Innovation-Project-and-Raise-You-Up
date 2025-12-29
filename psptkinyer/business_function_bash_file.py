# -*- coding: utf-8 -*-\n"+f"Created on 2025-05-01 1746141410.8774834  @author: yyyyyyyyyyyyyyyyyyyy
def Problem_Solving_Program2025_05_01__1746141410_8745205():
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
    exe_file=rf"/home/jross77/Documents/pyautogui/Problem_Solving_Program2025_05_01__1746141410_8745205/C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\Problem_Solving_Program\pyautogui_function_exe2025_05_01__1746141410.876516.py
    screen_dir_name="Problem_Solving_Program2025_05_01__1746141410_8745205"
    bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\pyauto.sh"
    run_pyauto_str=f'''#!/bin/bash
    source /home/jross77/Documents/pyautogui/venv/bin/activate
    export DISPLAY=:0
    #xdotool mousemove 100 200 # this works and gives me hope
    python3 /home/jross77/Documents/pyautogui/Problem_Solving_Program2025_05_01__1746141410_8745205/C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\Problem_Solving_Program\pyautogui_function_exe2025_05_01__1746141410.876516.py
    deactivate 
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
    input()