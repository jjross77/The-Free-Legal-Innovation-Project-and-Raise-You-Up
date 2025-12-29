


# -*- coding: utf-8 -*-\nCreated on Mon Jun 24 05:29:05 2024  @author: yyyyyyyyyyyyyyyyyyyy
class business_process_management_functions():
 def __init__(self):
  ''' '''
  self.sql_switch=0
  self.spacy_switch=0
  import psycopg2
  self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
  self.cur = self.conn.cursor()
 def subprocess_run_script_remotely(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
class business_process_management_functions_child(business_process_management_functions):
 def __init__(self):
  ''' '''
  self.sql_switch=0
  self.spacy_switch=0
  import psycopg2
  self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
  self.cur = self.conn.cursor()
 def retrieve_data_from_chat_gpt(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def write_bash_file(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def write_other_file(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def retrieve_data_from_website_database(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def upload_data_from_website_database(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 

 def create_table_on_remote_server(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_content_to_problem_solving_program(self):
  ''' '''
  self.conn_local = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")

  print('CONTENT')
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_code_to_appriproate_coding_file(self):
  ''' '''
  import psycopg2
  self.conn_local = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")

  print('CODE')
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def subprocess_run_script_remotely(self,command_list):
  ''' REMOVING SHELL HERE MADE A HUGE DIFFERENCES'''
  import subprocess
  try:
      subprocess.run(command_list, check=True)
      #subprocess.run(command_list, shell=True, check=True)

  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into :{e}")
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 

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
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 

 def add_content_of_bash_script(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def init_sql(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def ip_address_look_up_table_creator(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def insert_into_problem_solving_data(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_coding_project(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def edit_coding_project(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
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
  get_all_table_names_str = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name;"""
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
          light_table_found=re.search("pyautogui_light_table_(\d)*",table_name)
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
  # close connection and cur
  return  newest_pyautogui_light_table
 
 def problem_solving_program_action_logic(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def mark_as_used_id(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def setup_llm_model_from_lm_studio(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def retrieve_column_data(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def retrieve_table_data(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def process_table_column_names(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def clean_column_value_for_sql(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def break_up_column_value_if_too_long(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_table_column_value_str(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def insert_values_stringgs_into_sql(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_pyautogui_file_of_inputs_and_video(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def exe_pyautogui_creation_script_on_other_computers_sub(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_up_website_on_internet(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_up_website_on_local_network(self):
  ''' go to elecotrnics doc for info on how to start server
   THIS IS THE PSP starter on webserver? '''

  dir_scripts_stored=""
  run_pyauto_str=f"""#!/bin/bash
  source /home/jross77/Documents/pyautogui/venv/bin/activate
  # Run the Python script with arguments
  # need to run it as a subprocess or find way to execute it as if its not being sshed
  export DISPLAY=:0
  #follow instructions in electornics book to keep screen on
  #xdotool mousemove 100 200 # this works and gives me hope
  python3 {exe_file}
  #python3 /path/to/your_script.py arg1 arg2
  #xvfb-run python your_script.py
  # Deactivate virtual environment (if needed)
  deactivate"""
  # change this to only copy the newest files maybe
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
  
  #inputs:
  return 
 def create_and_run_bash_file(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def mkdir_dir_bash(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def update_all_website_code_and_restart_websites(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def record_mods_to_files_local_to_remote_server_for_django_websites(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def generate_all_business_list(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def set_up_multi_sites_nginx_gunicorn_systemd(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def psp_pipeline(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_all_other_business_content(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def sudo_remove_bash(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def update_website_code_and_restart_website(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def modify_file_locally(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def keep_updating_and_stealing_existing_business_work_funnel_work_into_program(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_tailwind_template_to_setup_django_website(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_tailwind_template_to_set_up_django_website(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def generate_all_category_business_list(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def build_phone_app_for_business(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def use_penetration_tesing_tools_on_server_to_test_security(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def keep_updated_on_business_in_category_and_take_all_ideas_add_to_business(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def reverse_engineer_business_work_and_add_ideas_and_work_to_program(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def build_on_top_of_existing_business_in_category_and_constantly_update_and_reverse_engineer_business_products_and_add_to_business(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_customized_template_files_website_dir(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def copy_files_only_into_remote_dir(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_list_of_all_stock_market_businesses(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def model_all_stock_market_websites(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
class business_process_management_functions_gchild(business_process_management_functions_child):
 def __init__(self):
  ''' '''
  self.sql_switch=0
  self.spacy_switch=0
  import psycopg2
  self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
  self.cur = self.conn.cursor()
 def start_processes(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def end_processes(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_new_processes(self,pyautogui_script_to_run,hi):
  ''' '''
  import sys
  sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_for_generative_model_access a1.1.1.1.1.1')
  from pyautogui_for_generative_model_access_functions import pyautogui_for_generative_model_access_functions_child
  pyautogui=pyautogui_for_generative_model_access_functions_child()
  pyautogui.generate_and_upload_data_from_chatgpt(self,pyautogui_script_to_run)
  hi='meow'    
  import os
  os.listdir(hi)
  print('hi')
  print('hello')
  print('meow')
  print('meow')
  print('NEW  FILE') 
  print("")
  return 
   #what this function does:   
 def start_instagram_automatic_creator(self):
  '''javacript below '''
  #const txt = document.documentElement.outerHTML;
  #alert(txt);
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_facebook_automatic_creator(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_linkedin_automatic_creator(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_ddns_listner(self):
  ''' '''
  import sys
  import time
  sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\FLIP_website')
  from ddns_functions import ddns_functions
  ddnss=ddns_functions()
  ip="142.184.88.130"
  ddnss.login_to_pork_bun_change_dns(ip)
  saved_ip =""
  while True:
      #check if internet connection
      if connectioned_to_internet:
          if ip != saved_ip:
              ddnss.login_to_pork_bun_change_dns(ip)
      time.sleep(5)
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_web_crawler(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_selenium_scrapers(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def goverment_rss_feed_listner(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def ssh_into_all_other_computers(self,host,username):
  ''' going to use a authentication key to do this refer to electornics document NEED TO DO THIS FOR ALL COMPUTERS WANT TO SSH AND SUE THIS COMMAND TO AUTOMATE PASSWORD INPUT'''
  import subprocess
  ### updated
  # hp laptop 207
  BIG_BLACK="192.168.2.43"
  website_ip=r"192.168.2.209"#server computer
  big_white=r"192.168.2.214"#server computer
  #corsair 45
  #46 is other acer
  #47 other ip
  

  # 
  # THESE ARE THE TWO KEY COMMANDS to get automated ssh to work and to run scripts automcailyl
  # sudo apt install open ssh server
  # use    ssh-keygen -t rsa -b 4096 -C "your_email@example.com" to generate a key
  # for authentication
  #Copy Your Public Key to the Remote Server using git bash
  #```bash
  #ssh-copy-id username@remote_host
  #```
  #EXTRA INFO
  #CHANGE BOTH OF THESE PCS TO LINUX
  #ssh desktop-2ifptl3/rossg@192.168.2.154 laptop  password Munchlax3
  # ssh desktop-s7na8dm\doggo777@192.168.2.191 big white
 
  # just give up and move all computers to linux so can automate these commands?
  # or simply manually enter on certain pcs
  # if is window pc
  # and if gets
  # for now leave it and
  # then if need more compute
  # then transfer it over 
  # sceurity issues worry can solve this linux more secure and private
  # i think i transfer my big white to linux first, download everything etc
  # then i transfer other laptop
  # this solves the openssh issue
  # and can use all these computers as if they were the same which is the goal
  # and if this one breaks
  # buy new one with windows on it
  # basically run all code in ubuntu
  # writing code base to ubuntu on windows machine
  # if i do this then will run all computers well
  # and will be gucci
  
  #import pexpect?
  #print subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
  #do the ssh certificate on all the computers and set this up using elecontrics guide
  #generated from chatgpt
  #host="192.168.2.163"
  #username="jross77"
  #ssh_command = [f"ssh","-t",  f"{username}@{host}","sudo", "run"]# put the script you want to run here
  ssh_command = [f"ssh","-t",  f"{username}@{host}","python3"]# put the script you want to run here
  #ssh_command = [f"cat","hello.py","|","ssh",f"{username}@{host}","python","-"]# put the script you want to run here
  #ssh_command = [f"scp","-r",r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management",  f"{username}@{host}:/home/jross77/Downloads"]# put the script you want to run here
  #scp file.txt remote_username@10.10.0.2:/remote/directory
  try:
      # Run the ssh command
      subprocess.run(ssh_command, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}: {e}")
  input()    
  #return host,username,password,ssh_command
 def upload_code_base_to_other_computers(self,host,username):
  '''USE THIS FUNCTION TO be able to run scripts i write on laptop on computers im sshing into '''
  #step 1 folder
  #step 2 
  #step 3
  #step 4
  import subprocess
  host="192.168.2.163"
  username="jross77"

  ssh_command = [f"scp","-r",r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management",  f"{username}@{host}:/home/jross77/Downloads"]# put the script you want to run here
  
  #scp file.txt remote_username@10.10.0.2:/remote/directory  
  try:
      # Run the ssh command
      subprocess.run(ssh_command, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}: {e}")
  input()
  
  
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
  
       
  return
 def create_bash_script_for_other_computer(self):
  ''' '''

  # -*- coding: utf-8 -*-\nCreated on 2024-11-29 1732938622.9827178  @author: yyyyyyyyyyyyyyyyyyyy
  
  import sys
  input_str=""
  sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Problems a1')
  from Problems_functions import problems_functions
  Problems=problems_functions()
  Problems.slot_in_verbs_using_pos_information()
 
  return input_str,Problems
  return 
 def run_bash_script_on_other_computers(self,username,host,file_name):
  ''' '''
  import subprocess
  # THESE ARE THE TWO KEY COMMANDS to get automated ssh to work and to run scripts automcailyl
  # sudo apt install open ssh server
  # use    ssh-keygen -t rsa -b 4096 -C "your_email@example.com" to generate a key
  # for authentication
  #Copy Your Public Key to the Remote Server using git bash
  #```bash
  #ssh-copy-id username@remote_host
  #```
  #EXTRA INFO
  #CHANGE BOTH OF THESE PCS TO LINUX
  #ssh desktop-2ifptl3/rossg@192.168.2.154 laptop  password Munchlax3
  # ssh desktop-s7na8dm\doggo777@192.168.2.191 big white
 
  # just give up and move all computers to linux so can automate these commands?
  # or simply manually enter on certain pcs
  # if is window pc
  # and if gets
  # for now leave it and
  # then if need more compute
  # then transfer it over 
  # sceurity issues worry can solve this linux more secure and private
  # i think i transfer my big white to linux first, download everything etc
  # then i transfer other laptop
  # this solves the openssh issue
  # and can use all these computers as if they were the same which is the goal
  # and if this one breaks
  # buy new one with windows on it
  # basically run all code in ubuntu
  # writing code base to ubuntu on windows machine
  # if i do this then will run all computers well
  # and will be gucci
  
  #import pexpect?
  #print subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
  #do the ssh certificate on all the computers and set this up using elecontrics guide
  #generated from chatgpt
  host="192.168.2.163"
  username="jross77"
  #ssh -t user@server "sudo script"
  ssh_command = [f"ssh","-t",  f"{username}@{host}","sudo", "{bash_file_name}"]# put the script you want to run here
  #ssh_command = [f"ssh","-t",  f"{username}@{host}","python3"]# put the script you want to run here

  #ssh_command = [f"scp","-r",r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\business_process_management",  f"{username}@{host}:/home/jross77/Downloads"]# put the script you want to run here

  #scp file.txt remote_username@10.10.0.2:/remote/directory
  
  try:
      # Run the ssh command
      subprocess.run(ssh_command, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}: {e}")
  input()
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def upload_applicable_sql_database_table_to_other_computers(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def grab_journal_articles_books_and_patents_to_keep_up_with_cutting_edge_tech_feed_into_psp(self):
  '''need to stay up to date and make easy to keep up build pipeline to do this '''
  # build all possible patents for factory
  # build all possible models keep up to date with newest models and find uses for them
  #Find out and create a feed to keep up to date with newest thing in field of machine learning and training etc and new models, build pipeline for this store article translate into readable format. So you at end o f pipeline
  #1.	Figure out new ideas and tools that have been developed usually related to
  #math in machine learning, robotics, computer hardware, critical thinking and reading, 
  #problem solving and strategy( this involves science) ,
  #learning and teaching, brain, programming and  fields I want to be an expert in
  #2.	Learn what these tools are through questioning and maybe running through a generative model
  #3.	Create method Translate new ideas/tools into code I can use or into problem solving methods
  #4.	Implement new code and ideas into current projects to improve and apply elsewhere and use as tools in current system
  #Effects: keep up to date on and learned Learn newest  things in the field on machine learning and comp sci and therefore never become irrelevant
  #Develop method to learn things  rapid and apply to problem solving rpcoess and programming so I have software that implement ideas and can use as tool to improve my life

  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def retrieve_data_from_chat_gpt(self,path_to_pickle,intital_prompt,recurse_prompt,i,pickle_file_name_root,pattern_to_search_soup):# NOUNS WHEN WE COME BACK
     """ access chatgpt using an intital prompt a path to store the information and a indicatory of a unique value to give the pickle file"""
     # all these scripts will hinge on pyautogui/selenoum program
     #create a pyautogui script  for this
     # need to modify this
     # make it for websearch instead
     # using pyautogui
     # and add a tab shifting system to grab data from windows
     # or find a way to grab window data without scirpt
     # load data into coding program
     import re
     import requests
     import pickle
     import os
     from selenium import webdriver
     from bs4 import BeautifulSoup
     from selenium.webdriver.common.by import By
     from selenium.webdriver.common.keys import Keys
     import time
     from selenium.webdriver.common.action_chains import ActionChains
     from selenium.webdriver.firefox.options import Options as FirefoxOptions
     how_question_lists=[]
     counterr=0
     cwd = os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Pickles") 
     link = r"https://chatgpt.com/"
     #firefox_options = FirefoxOptions()
     #firefox_options.headless = True
     #driver= webdriver.Firefox(options=firefox_options)
     driver= webdriver.Firefox()
     session = requests.Session()
     headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
     'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
     'Accept':'text/html,application/xhtml+xml,application/xml;'
     'q=0.9,image/webp,*/*;q=0.8'}
     driver.get(link) #the pages link must be inserted here
     content = driver.find_element(By.ID, 'prompt-textarea')
     content.send_keys(f"{intital_prompt}")
     content.send_keys(Keys.ENTER)
     time.sleep(20)
     try:
         while True:
             content = driver.find_element(By.ID, 'prompt-textarea')
             content.send_keys(f"{recurse_prompt}")
             content.send_keys(Keys.ENTER)
             time.sleep(20)
             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
             html= driver.execute_script("return document.documentElement.outerHTML")
             sel_soup = BeautifulSoup(html, 'html.parser')
             text_from_website=sel_soup.get_text()
             print(text_from_website)
             items_found_list=re.findall(pattern_to_search_soup,text_from_website)
             print(items_found_list)
             for question in items_found_list:
                 if question in how_question_lists:
                     continue
                 else:
                     how_question_lists.append(question)     
     except:
         with open(path_to_pickle,"wb") as  f7: #1
             pickle.dump(how_question_lists, f7, pickle.HIGHEST_PROTOCOL)
         i= f"{i}_{i}"
         pickle_file_name=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\pickles\{pickle_file_name_root}{i}.pickle"
         self.retrieve_data_from_chat_gpt(pickle_file_name,intital_prompt,recurse_prompt,i,pickle_file_name_root,pattern_to_search_soup)  
         
 def set_up_tor_for_requests(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  
  # Make a request through the Tor connection
  # IP visible through Tor
  import requests
  session = requests.session()
  # Tor uses the 9050 port as the default socks port
  session.proxies = {'http':  'socks5://127.0.0.1:9050',
                     'https': 'socks5://127.0.0.1:9050'}
  print(session.get("http://httpbin.org/ip").text)
  # Above should print an IP different than your public IP

  # Following prints your normal public IP
  print(requests.get("http://httpbin.org/ip").text)
  return session

 def search_common_crawl(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def send_messages_over_instagram(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def send_messages_over_facebook(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def send_messages_over_other_platforms(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def retrieve_emails(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def send_emails(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def find_grants_to_apply_to(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def write_grant_applications_and_automcially_apply(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_website(self):
  ''' '''
  import subprocess
  import os
  file_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Music\canlawaccessible"
  os.chdir(file_dir)
  #create bash file for linux
  #source is for linux
  command_str="""
source env/bin/activate
python manage.py runserver
"""
  command_str="env\Scripts\activate"

  self.write_bash_file(command_str)#.sh fule
  self.write_other_file() 
  #create other file for windows
  # then run this file in commands
  console_command=r"python manage.py runserver"
  #; activate virtual envrionment then run manage.py runserver
  start_website_commands = [f"python","manage.py",  f"runserver"]
  try:
      # Run the ssh command
      subprocess.run(start_website_commands, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(e)
  input()
  return
  
 def start_website_on_main_website_server(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  
  return 
 def setup_nginx_to_run_multiple_websites(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_table_on_remote_server(self,table_name,column_name_data_type_dic):
  '''create table for this '''
  import psycopg2
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
      create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
      for column_name,data_type in column_name_data_type_dic.items():
          create_table_str+=f",{column_name} {data_type}"
      end_create_table_str = ");"
      create_table_str+=end_create_table_str
      print(create_table_str)
      self.cur.execute(create_table_str)
      self.conn.commit()
  except Exception as E:
          print(E)
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  return 

 def retrieve_data_from_website_database(self,table_name,where_string,column_list):
  ''' ''' 
  import psycopg2
  import re
  from psycopg2 import sql
  host = '192.168.2.209'  # E.g., '192.168.1.100' or 'your-database-server.com'
  port = '5432'  # Default PostgreSQL port
  dbname = 'psp_website'  # E.g., 'myprojectdb'
  user = 'jross77'  # E.g., 'myuser'
  password = 'MeganisGreat'  # E.g., 'mypassword'
  try:
      self.conn = psycopg2.connect(host=host,
      port=port,
      dbname=dbname,
      user=user,
      password=password) 
      self.cur = self.conn.cursor() 
      column_list=re.sub("'","",str(column_list)[1:-1])
      #column_list=str(column_list)[1:-1].sub("'","")
      sql_str=f"SELECT {column_list} FROM {table_name}{where_string};"
      #print(sql_str)
      try:
          self.cur.execute(sql_str)
      except Exception as E:
          print(E)
      sql_data_list_list= self.cur.fetchall()
      #self.conn.commit()
  except Exception as e:
          print(f"Error: {e}")     
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  #print('moew')
  #input(f"{sql_data_list_list}")
  return  sql_data_list_list
 def upload_data_to_psp_website_database_3(self,table_name,dictionary_of_values):
     import psycopg2
     import re
     from psycopg2 import sql
     host = '192.168.2.209'  # E.g., '192.168.1.100' or 'your-database-server.com'
     port = '5432'  # Default PostgreSQL port
     dbname = 'psp_website'  # E.g., 'myprojectdb'
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
         
 def upload_data_from_website_database_2(self,table_name,dictionary_of_values):
     ''' '''
     import re
     for i, (table_column, column_value) in enumerate(dictionary_of_values.items()):
         column_value=str(column_value)
         column_value=column_value.replace("\'","")
         column_value=column_value.replace("\"","")
         #column_value=column_value.replace(","," ")
         column_value=column_value.replace("'","")
         column_value=re.sub("\"","",column_value)
         if len(column_value)>400000:# probabyl going to be the movement list so how do i deal weith this
             print(column_value)
             column_value=column_value[:400000]
             print(column_value)
             input("stop value si too long review and make database changes in spl for pyauto table on website")
             return
             
         if i ==0:
             table_columns =  f"{table_column}"
             values_string = f"'{column_value}'"
             continue
         else:
             table_columns=  table_columns+f",{table_column}"
             values_string= values_string+f",'{column_value}'"
             continue
     sql_str=f"INSERT INTO {table_name} ({table_columns}) VALUES ({values_string});"
     self.cur.execute(sql_str)
    
  
     
 def upload_data_from_website_database(self,table_name,dictionary_of_values):
  ''' '''
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
 def setup_website_and_ssh(self):
  ''' use notes in electronics'''
  setup_commands="""
  https://learndjango.com/tutorials/django-login-and-logout-tutorial
  python manage.py createsuperuser
  sudo apt install openssh-client
  sudo apt install openssh-server
  sudo apt install python3.12-venv
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo apt-get update -y
  python3 -V
  python3 -m venv env
  source env/bin/activate
  sudo apt-get install dos2unix
  python -m pip install django
  python -m pip install psycopg2
  sudo apt install lm-sensors
  pip install django-environ
  sudo apt-get install --reinstall libpq-dev
  pip install psycopg2-binary
  mkdir freelegalproject
  django-admin startproject project freelegalproject
  cd freelegalproject
  django-admin startapp fiann
  python manage.py runserver
  python manage.py migrate
  mkdir -pv fiann/templates/fiann/
  #change database configs
  #create db canlawaccessible
  createdb canlawaccessible
  sudo -u postgres psql
  CREATE ROLE jross77 WITH LOGIN PASSWORD 'MeganisGreat';
  GRANT CONNECT ON DATABASE canlawaccessible TO jross77;
  ALTER ROLE jross77 WITH SUPERUSER;
  \q
  NEED TO EXIT POSTGRES USER BEFORE CREATE DATABASE
  
  #checking connection settings for remote access in pg_hba.conf
  modify settings file with the databases variable below
  then type manage.py migrate
  python manage.py migrate
  
  write to postgres database from remote server
  #
  Step 5: Ensure PostgreSQL Server Is Accessible Remotely
  Edit PostgreSQL’s pg_hba.conf File:
  
  The file is typically located in the PostgreSQL data directory (commonly /etc/postgresql/{version}/main/pg_hba.conf on Linux).
  Add a line that allows your local IP address to connect to the PostgreSQL database
  sudo nano pg_hba.conf
  host    all             all             192.168.2.28/32            md5
  
  192.168.0.14 for the laptop currently
  Open the postgresql.conf
  sudo nano postgresql.conf
  Allow Remote Connections:
  file on the remote server and ensure the listen_addresses parameter is set to * to allow connections from any IP address,
  listen_addresses = '*'
  #ctrl w in nano to find where listen addresses is located
  Restart PostgreSQL:
  sudo service postgresql restart
  #test remote connection
  # get remote connectin to work on widnows
  
  C:\Program Files\PostgreSQL\14\
  Set the PostgreSQL Environment Variables
  C:\Program Files\PostgreSQL\15\bin
  # add environment variable to bin directory
  C:\Program Files\PostgreSQL\15\bin
  # psql should now work that you have created envrionment variable
  psql -h 192.168.2.209 -U jross77 -d canlawaccessible #ip is of the server currently at Goulburn
  #psql -h 192.168.2.209 -U jross77 -d canlawaccessible
  #DROP TABLE pyautogui_master;
  #DROP TABLE pyautogui_light_table_1;
  # it works
  Try these commands
  \dt
  SELECT * FROM my_table;
  \q
  Firewall Issues: Ensure that the PostgreSQL server’s port (default 5432) is not blocked by a firewall on the remote server.
  The .env file should be in the same directory as settings.py
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
        'NAME': 'canlawaccessible',  # Name of the database you created
        'USER': 'jross77',  # PostgreSQL username
        'PASSWORD': 'MeganisGreat',  # PostgreSQL password
        'HOST': 'localhost',  # Leave as 'localhost' if the database is on the same machine
        'PORT': '5432',  # Default port for PostgreSQL
    }
}
  """
  import psycopg2
  from psycopg2 import sql

  # Define the database connection parameters
  host = 'your-remote-server-ip-or-domain'  # E.g., '192.168.1.100' or 'your-database-server.com'
  port = '5432'  # Default PostgreSQL port
  dbname = 'your-database-name'  # E.g., 'myprojectdb'
  user = 'your-username'  # E.g., 'myuser'
  password = 'your-password'  # E.g., 'mypassword'

  # Connect to the PostgreSQL database
  try:
      connection = psycopg2.connect(
          host=host,
          port=port,
          dbname=dbname,
          user=user,
          password=password
      )
      print("Connection successful!")

      # Create a cursor to interact with the database
      cursor = connection.cursor()

      # Example: Inserting data into a table
      insert_query = """
      INSERT INTO your_table_name (column1, column2) 
      VALUES (%s, %s)
      """
      data_to_insert = ('value1', 'value2')

      cursor.execute(insert_query, data_to_insert)

      # Commit the transaction
      connection.commit()

      print("Data inserted successfully!")

  except Exception as e:
      print(f"Error: {e}")

  finally:
      if connection:
          # Close the cursor and connection
          cursor.close()
          connection.close()
          print("Connection closed.") 

# host is ip address   192.168.0.16
  #USE alt delete command to delete none useful lines from nano
  #https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8

  #execute db command

  return 
 
 def create_pyautogui_webscraped_content_table(self):
  ''' '''
  table_name="pyautogui_content"
  column_name_data_type_dic={
  "code":"text",# break this up into list
   "explantory_text":"text",
   "prompt_problem_searched":"text",# only if it is a coding file otherwise just paste the active frame
   "time_stamp":"text",
   "whole_text_chunk":"text",
   "website_link":"text"}
   
   # dicitonary of objects and qualtities  in problem to use to ask questions
  
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
 def retrieve_data_from_pyautogui_website_database(self):
  ''' '''
  table_name="pyautogui_content"
  where_string=""
  sql_data_list_list=self.retrieve_data_from_website_database(table_name,where_string)
  #print(sql_data_list_list)
  input()
  return column_name_data_type_dic

 def upload_data_from_pyautogui_website_database(self):
  ''' '''
  #dictionary_of_values={table_column:column_value}
  import time
  timee=time.time()
  table_name="pyautogui_content"
  dictionary_of_values={
  "code":["def int"],# break this up into list
   "explantory_text":["int means this"],
   "prompt_problem_searched":["what is a int"],# only if it is a coding file otherwise just paste the active frame
   "time_stamp":[timee],
   "whole_text_chunk":["everything together"]}
   # dicitonary of objects and qualtities  in problem to use to ask questions
  self.upload_data_from_website_database(table_name,dictionary_of_values)
  print("hi")
  input()
  return 
 def pyautogui_table_listner_to_convert_into_coding_problem_solving_info(self):
  '''write me a listen er in python to listen for a database update '''
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
  try:
      self.conn = psycopg2.connect(
          host=host,
          port=port,
          dbname=dbname,
          user=user,
          password=password)  
      self.cur = self.conn.cursor()      
      print("connection started")      
      sql_str_pyauto_gui_light=f"SELECT my_id,whole_text_chunk,action FROM {newest_pyautogui_light_table}"
      sql_str_pyauto_gui_used_id=f"SELECT used_my_id_value FROM used_id_pyautogui_table"# dont need to interact with master
      while True:# start listener
          time.sleep(40)
          used_id_list=[]
          self.cur = self.conn.cursor()# create new cursor          
          self.cur.execute(sql_str_pyauto_gui_used_id)       
          id_list_list= self.cur.fetchall()  
          for id_in_list in id_list_list:
              idd=id_in_list[0]
              used_id_list.append(int(idd))
          self.cur = self.conn.cursor()# create new cursor          
          self.cur.execute(sql_str_pyauto_gui_light)
          pyauto_gui_light_data_list_list= self.cur.fetchall() 
          print(pyauto_gui_light_data_list_list)

          for pyauto_gui_light_data_list in pyauto_gui_light_data_list_list :
              my_id=int(pyauto_gui_light_data_list[0])# assume it will be 0 here
              if my_id in used_id_list:
                  print('didnt find nothing')
                  continue
              else: 
                  print('taking action')
                  self.problem_solving_program_action_logic(pyauto_gui_light_data_list)
                  self.mark_as_used_id(my_id)# mark as used id 
          print("listener pass!:")         
  except Exception as e:
      print(f"Error: {e}")
      input()    
      # within last give minutes 
      #used_id_pyautogui_table
      #pyautogui_master
      #pyautogui_light_table_1 # wil increase at points
 def ssh_pyautogui_script_other_computer(self):
  ''' '''
  
  
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 

 def setup_computer_to_run_pyautogui(self):
  '''sudo apt-get install xvfb try xvfb at one point if we can 
  xvfb-run python your_script.py'''
  
  import subprocess
  import re
  username="jross77"
  host='192.168.2.207'# it is now 192.168.2.207 # for laptop
  file_name_with_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\update_comp__for_pyautogui.sh"
  file_name_with_dir_list=re.split(r"\\",file_name_with_dir)
  print(file_name_with_dir_list)
  file_name=file_name_with_dir_list[-1]
  print(file_name)
  pyauto_dir=r"/home/jross77/Documents/".strip()
  dir_to_copy_script_to=r"/home/jross77/Documents/".strip()
  fixt_key_ssh="""https://stackoverflow.com/questions/20840012/ssh-remote-host-identification-has-changed
  # fix keygen errors
  ssh-keygen -R 192.168.3.10 """
  # need to remove all tabs and extra spaces to get this to run
  #super delicate
  # no extra spacing on a single line
  # must have the triple quotes at the end of a codeline in  file no new line
  # use the below command for debugging
  # NEED TO HAVE THIS USED TO MAKE BASH SCRIPTS WORK
  #sudo apt install dos2unix # fix new line errors with this
  #bash -x /home/jross77/Documents/update_comp__for_pyautogui.sh
  #create bash file to do this
  # NEED TO SET PERMISSIONS AND OWNER TO all and jross77 for files created in this way
  setup_round_two="""# this one should work better 
  TURN THE BELOW INTO A PROPER BASHSCRIPT
  ERROR WITH aspire
  WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
  may need to use pip3 install for various thing
  
  
  """
  bash_script_str="""
  """
  set_up_computer_commands=r"""#!/bin/bash
# Define the directory path
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
sudo apt install gnome-screenshot
sudo apt install idle
sudo apt-get install xauth#to get screen to work pyauto
#probably dont need these but keep in case
# create this file touch ~/.Xauthority
#add to shell init export XAUTHORITY=$HOME/.Xauthority
#set correct permissions chmod 600 /home/jross77/.Xauthority
#set up x11 forwarding in /etc/ssh/sshd_config ,X11Forwarding yes
#export PATH=$PATH:/bin:/usr/bin:/usr/local/bin
#source ~/.bashrc

sudo apt-get install scrot

sudo apt-get install python3-tk

sudo apt-get install python3-dev
# install pillow with these commands
# change dirtectory permissions to install pillow
sudo chmod -R u+w /home/jross77/Documents/pyautogui/venv/lib/python3.12/site-packages/
# change permissions
sudo chown -R $USER /home/jross77/Documents/pyautogui/venv/lib/python3.12/site-packages/
pip install pillow
# install numpy
sudo chmod -R u+w /home/jross77/Documents/pyautogui/venv/bin/
sudo chown -R $USER /home/jross77/Documents/pyautogui/venv/
pip install numpy
pip install pytesseract
pip install beautifulsoup4
pip install pyperclip
pip install opencv-python
sudo apt-get install tesseract-ocr
pip install opencv-python
sudo apt install gnome-screenshot
sudo apt-get update
sudo apt install curl  
sudo apt-get install xclip
sudo apt update
sudo systemctl enable ssh # sset it to run automaitcally on boot
sudo ufw allow ssh
#/etc/ssh/sshd_config # change stuf in this fle to get ssh to work
# change in this file these two settings
#PermitTTY (should be yes to allow terminal sessions)
#AllowUsers or DenyUsers (to ensure the user is not restricted)
sudo systemctl restart ssh
sudo apt install postgresql
sudo apt-get install libpq-dev python-dev
sudo apt-get install --reinstall libpq-dev
pip install psycopg2
# THIS MAKES PYAUTOGUI MOUSE WORK need to swithc to xorg
sudo apt install xdotool
# need to change resoultion and sizing settings to make this work with ubuntu
# add python location to path
export PATH=$PATH:/usr/bin:/usr/local/bin
echo 'export PATH=$PATH:/usr/bin:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc
sudo chmod 755 $(which python3)
sudo chown jross77:jross77 $(which python3)# change permissions
# if ssh is screwing up re install ubuntu

# get python to work

# start xdotools and get pyautogui to work
export DISPLAY=:0 # use this to set display FIXES ERROR IT SEEMS  
touch ~/.Xauthority
ls -l ~/.Xauthority# check permissions
chmod 600 ~/.Xauthority
xdotool mousemove 100 200 

# dont run the below lines ensure .xauthority is at home/jross77
#touch /home/jross77/Documents/pyautogui/.Xauthority # this creates the xauthroity file

#export XAUTHORITY=/path/to/.Xauthority# export the environment variable
#export XAUTHORITY=/home/jross77/Documents/pyautogui 
#export XAUTHORITY=/home/jross77/Documents/pyautogui/.Xauthority
# add this line to shell to have it persist across sessions
#keep screen on using
sudo apt install screen
screen
# upload pyautogui creation script to other computer directory of pyautogui and directory of other computer pyautogui
# choose the ip address
# run pyautogui creaton script on other computer like i run law society script
scp -r  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\pyautogui_for_generative_model_access a1.1.1.1.1.1 jross77@192.168.2.200:/home/jross77/Documents/pyautogui
scp -r  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\Inputs jross77@192.168.2.200:/home/jross77/Documents/pyautogui

#Step3  install environment and necessary dependencies
#execute script within other script that sshed into system to avoid xauthorizaiton problem?
# fix this error doing the following
#Error: connection to server at "192.168.2.209", port 5432 failed: FATAL:  no pg_hba.conf entry for host "192.168.2.207", user "jross77", database "canlawaccessible", SSL encryption
#connection to server at "192.168.2.209", port 5432 failed: FATAL:  no pg_hba.conf entry for host "192.168.2.207", user "jross77", database "canlawaccessible", no encryption
#host    all             all             192.168.2.207/32           md5
host    all             all             192.168.2.239/32           md5
host    all             all             192.168.2.209/32           md5


#sudo systemctl reload postgresql
#/etc/postgresql/[version]/main/pg_hba.conf
#sudo nano pg_hba.conf """
  # fix the spacing issues related to creating this file in windows
  #sed -i 's/\r$//' /path/to/your/script.sh
  print(set_up_computer_commands)
  #set_up_computer_commands = set_up_computer_commands.replace('\r', '')
  with open(file_name_with_dir,"w") as f:
      f.write(set_up_computer_commands)
      print('write')
  #copy script to the computer   
  scp_command_list = [f"scp",f"{file_name_with_dir}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here
  self.subprocess_run_script_remotely(scp_command_list)
  #ssh into the 
  doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/update_comp__for_pyautogui.sh"]
  self.subprocess_run_script_remotely(doc2ui)
  #ssh user@remote_host "sudo bash /path/to/remote/script.sh"
  #ssh user@remote_host "bash -s' < /path/to/local/script.sh"
  #print(scp_command_list)
  file_to_exe=dir_to_copy_script_to+file_name
  file_to_exe=file_to_exe.strip()
  #chmod +x /home/jross77/Documents/update_comp__for_pyautogui.sh
  #ssh_command = [f"ssh",  f"{username}@{host}",f"chmod" ,"+x","home/jross77/Documents/update_comp__for_pyautogui.sh"]# put the script you want to run here
  ssh_command = [f"ssh",  f"{username}@{host}",f"chmod +x {file_to_exe}"]# put the script you want to run here
  self.subprocess_run_script_remotely(ssh_command)
  print(file_to_exe)
  ssh_command = [f"ssh",  f"{username}@{host}",f"sudo -S bash {file_to_exe}"]# put the script you want to run here
  self.subprocess_run_script_remotely(ssh_command)

  input()
 
  
 def chatgpt_ssh_script(self):
  '''this lets us run local script ssh root@MachineB 'bash -s' < local_script.sh '''# try running a local script 
  # scp whole folder of pyautogui script we want to run 
  # get in the directory 
  #scp: stat remote: No such file or directory
  #scp_command = [f"scp","-r",f"{script_dir}",fr"{username}@{host}:/home/jross77/Documents/pyautogui"]# put the script you want to run here
  # run the script
  # need to execute the venv before python here
  #ssh username@remote_host "bash -s" < /path/to/local/script.sh 
  # scp only new files maybe?
  # or scp only the directory being used
  # and move the screenshots into that directory if possible 
  import subprocess
  import os
  import re
  username="jross77"
  host='192.168.2.207'
  # only upload necessary files from now on if possible
  # to make testing much faster
  script_to_test=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\ChatGPT__Mozilla_Firefox\ChatGPT__Mozilla_Firefox2025_01_02__1735871006_360773.py"
  file_name_with_dir_list=re.split(r"\\",script_to_test)
  print(file_name_with_dir_list)
  file_name=file_name_with_dir_list[-1]
  screen_folder=file_name_with_dir_list[-2]
  # get dir
  #pyautogui_function_exe2025_01_03__1735926882.28694.py
  #ChatGPT__Mozilla_Firefox2025_01_03__1735926882_2829506.p
  #pyautogui_function_exe2025_01_03__1735926882.28694.py
  #C:/Users/yyyyyyyyyyyyyyyyyyyy/Documents/Coding/automating_coding/pyautogui_files/ChatGPT__Mozilla_Firefox/ChatGPT__Mozilla_Firefox2025_01_03__1735926868_404963.py
  pyauto_gui_script_with_path=r"/home/jross77/Documents/pyautogui"+"/"+screen_folder+"/"+file_name
  pyauto_gui_script_with_path=r"/home/jross77/Documents/ChatGPT__Mozilla_Firefox2025_01_02__1735876680_2023377.py"
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox2025_01_02__1735876680_2023377.py"
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/ChatGPT__Mozilla_Firefox2025_01_03__1735926868_404963.py"
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_03__1735926882.28694.py" 
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_03__1735926882.28694.py" 
  # need to get correct link and make sure clicking is correct
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_07__1736302392.7445173.py"
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_07__1736302392.7445173.py"
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_07__1736308463.3360422.py"
  pyauto_gui_script_with_path=r" /home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_07__1736308571.4890265.py"
  # maybe only copy over content before a certain time period or after a certain time period
  # to make scp faster

  # make the scp faster here


  
#C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\ChatGPT__Mozilla_Firefox\ChatGPT__Mozilla_Firefox2025_01_07__1736302392_7445173.py
  # need to try a new pyautogui file here
  # activate virtual envrionment
  bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\pyauto.sh"
  run_pyauto_str=f"""#!/bin/bash
source /home/jross77/Documents/pyautogui/venv/bin/activate
# Run the Python script with arguments
# need to run it as a subprocess or find way to execute it as if its not being sshed
export DISPLAY=:0
#follow instructions in electornics book to keep screen on
#xdotool mousemove 100 200 # this works and gives me hope
python3 {pyauto_gui_script_with_path}
#python3 /path/to/your_script.py arg1 arg2
#xvfb-run python your_script.py
# Deactivate virtual environment (if needed)
deactivate"""
  # change this to only copy the newest files maybe

  scp_command = [f"scp","-r",r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\ChatGPT__Mozilla_Firefox",fr"{username}@{host}:/home/jross77/Documents/pyautogui"]# put the script you want to run here 
  self.subprocess_run_script_remotely(scp_command)
  with open(bash_file_name,"w") as f:
      f.write(run_pyauto_str)
      print('write')
  script_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\ChatGPT__Mozilla_Firefox" 
  scp_command_list = [f"scp",f"{bash_file_name}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here 
  self.subprocess_run_script_remotely(scp_command_list)

  doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix","/home/jross77/Documents/pyauto.sh"]
  self.subprocess_run_script_remotely(doc2ui)
  
  ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/pyauto.sh"]# put the script you want to run here
  self.subprocess_run_script_remotely(ssh_command)
  input()
 
 def law_society_practice_script(self):
  '''# start xdotools and get pyautogui to work
  export DISPLAY=:0 # use this to set display FIXES ERROR IT SEEMS  
  touch ~/.Xauthority
  ls -l ~/.Xauthority# check permissions
  chmod 600 ~/.Xauthority
  xdotool mousemove 100 200  '''
  import subprocess
  import os
  import re
  import sys
  # always need to specify host computer to run pyautogui on
  host=sys.argv[1]
  print(host)
  print('nEHEHEH')
  #input()
  username="jross77"
  #host='192.168.2.207'
  testttt=True
  # only upload necessary files from now on if possible
  # to make testing much faster
  script_to_test=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\ChatGPT__Mozilla_Firefox\ChatGPT__Mozilla_Firefox2025_01_02__1735871006_360773.py"
  file_name_with_dir_list=re.split(r"\\",script_to_test)
  print(file_name_with_dir_list)
  file_name=file_name_with_dir_list[-1]
  screen_folder=file_name_with_dir_list[-2]
  dir_to_law=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox"
  #exe_file=r"/home/jross77/Documents/pyautogui/Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox/pyautogui_function_exe2025_01_07__1736308571.4890265.py"
  #exe_file=r"/home/jross77/Documents/pyautogui/Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox/pyautogui_function_exe2025_01_08__1736317384.5429323.py"
  exe_file=r"/home/jross77/Documents/pyautogui/Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox/pyautogui_function_exe2025_01_08__1736321463.4291465.py"
  screen_dir_name="Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox"
  bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\pyauto.sh"
    
  run_pyauto_str=f"""#!/bin/bash
  source /home/jross77/Documents/pyautogui/venv/bin/activate
  # Run the Python script with arguments
  # need to run it as a subprocess or find way to execute it as if its not being sshed
  export DISPLAY=:0
  #follow instructions in electornics book to keep screen on
  #xdotool mousemove 100 200 # this works and gives me hope
  python3 {exe_file}
  #python3 /path/to/your_script.py arg1 arg2
  #xvfb-run python your_script.py
  # Deactivate virtual environment (if needed)
  deactivate"""
  # change this to only copy the newest files maybe
  if testttt!=True:
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
      #input()
  #input()
  
 
 

 def update_computer_to_run_ssh_certificate_with_other_computer(self):
  ''' still need to write this one'''
  import subprocess
  import os
  import re
  username="jross77"
  host='192.168.2.209'
  # only upload necessary files from now on if possible
  # to make testing much faster
  # use bash
  fixt_key_ssh="""https://stackoverflow.com/questions/20840012/ssh-remote-host-identification-has-changed
  # fix keygen errors
  ssh-keygen -R 192.168.2.233 """
  bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\run_certificate.sh"  
  run_pyauto_str=f"""#!/bin/bash
  #get maybe run these command manually 
  sudo apt install openssh-server
  Add correct host key in C:\\Users\\yyyyyyyyyyyyyyyyyyyy/.ssh/known_hosts
  # remove from known hosts a computer when resetting ssh
  # then readd host key
  ssh-keygen -t rsa -b 4096 -C "rossgrove77@gmail.com"# if no key on laptop
  ssh-copy-id {username}@{host}
  ssh-copy-id jross77@192.168.2.233
  
  #ssh-copy-id jross77@192.168.2.209#bash
  sudo ufw allow ssh
  #ssh -v 192.168.2.209 to try to debug use this
  # the -v fixed the problem
  # then installed certifcate on other laptop to server
  #Copy Your Public Key to the Remote Server using git bash
  """
  with open(bash_file_name,"w") as f:
      f.write(run_pyauto_str)
      print('write')
  scp_command_list = [f"scp",f"{bash_file_name}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here 
  try:
      subprocess.run(scp_command_list, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}:{e}")
  #ssh into the 
  doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix","/home/jross77/Documents/run_certificate.sh"]
  try:
      subprocess.run(doc2ui, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}:{e}")   
  ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/run_certificate.sh"]# put the script you want to run here
  try:
      subprocess.run(ssh_command, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}: {e}")
      input()
  input()
  return 

 def update_computer_to_run_postgresql(self):
  ''' still need to write this one'''
  setup_commands="""
  https://learndjango.com/tutorials/django-login-and-logout-tutorial
  sudo apt install openssh-client
  sudo apt install openssh-server
  sudo apt install python3.12-venv
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo apt-get update -y
  python3 -V
  python3 -m venv env
  source env/bin/activate
  python -m pip install django
  python -m pip install psycopg2
  pip install django-environ
  sudo apt-get install --reinstall libpq-dev
  pip install psycopg2-binary
  mkdir freelegalproject
  django-admin startproject project freelegalproject
  cd freelegalproject
  django-admin startapp fiann
  python manage.py runserver
  python manage.py migrate
  mkdir -pv fiann/templates/fiann/
  #change database configs
  #create db canlawaccessible
  createdb canlawaccessible
  sudo -u postgres psql
  CREATE ROLE jross77 WITH LOGIN PASSWORD 'MeganisGreat';
  GRANT CONNECT ON DATABASE canlawaccessible TO jross77;
  ALTER ROLE jross77 WITH SUPERUSER;
  \q
  NEED TO EXIT POSTGRES USER BEFORE CREATE DATABASE
  
  #checking connection settings for remote access in pg_hba.conf
  modify settings file with the databases variable below
  then type manage.py migrate
  python manage.py migrate
  
  write to postgres database from remote server
  #
  Step 5: Ensure PostgreSQL Server Is Accessible Remotely
  Edit PostgreSQL’s pg_hba.conf File:
  
  The file is typically located in the PostgreSQL data directory (commonly /etc/postgresql/{version}/main/pg_hba.conf on Linux).
  Add a line that allows your local IP address to connect to the PostgreSQL database
  sudo nano pg_hba.conf
  host    all             all             192.168.2.28/32            md5
  
  192.168.0.14 for the laptop currently
  Open the postgresql.conf
  sudo nano postgresql.conf
  Allow Remote Connections:
  file on the remote server and ensure the listen_addresses parameter is set to * to allow connections from any IP address,
  listen_addresses = '*'
  #ctrl w in nano to find where listen addresses is located
  Restart PostgreSQL:
  sudo service postgresql restart
  #test remote connection
  # get remote connectin to work on widnows
  
  C:\Program Files\PostgreSQL\14\
  Set the PostgreSQL Environment Variables
  C:\Program Files\PostgreSQL\15\bin
  # add environment variable to bin directory
  C:\Program Files\PostgreSQL\15\bin
  # psql should now work that you have created envrionment variable
  psql -h 192.168.2.209 -U jross77 -d canlawaccessible #ip is of the server currently at Goulburn
  # it works
  Try these commands
  \dt
  SELECT * FROM my_table;
  \q
  Firewall Issues: Ensure that the PostgreSQL server’s port (default 5432) is not blocked by a firewall on the remote server.
  The .env file should be in the same directory as settings.py
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
        'NAME': 'canlawaccessible',  # Name of the database you created
        'USER': 'jross77',  # PostgreSQL username
        'PASSWORD': 'MeganisGreat',  # PostgreSQL password
        'HOST': 'localhost',  # Leave as 'localhost' if the database is on the same machine
        'PORT': '5432',  # Default port for PostgreSQL
    }
}
  """
  import psycopg2
  from psycopg2 import sql

  # Define the database connection parameters
  host = 'your-remote-server-ip-or-domain'  # E.g., '192.168.1.100' or 'your-database-server.com'
  port = '5432'  # Default PostgreSQL port
  dbname = 'your-database-name'  # E.g., 'myprojectdb'
  user = 'your-username'  # E.g., 'myuser'
  password = 'your-password'  # E.g., 'mypassword'

  # Connect to the PostgreSQL database
  try:
      connection = psycopg2.connect(
          host=host,
          port=port,
          dbname=dbname,
          user=user,
          password=password
      )
      print("Connection successful!")
      # Create a cursor to interact with the database
      cursor = connection.cursor()
      # Example: Inserting data into a table
      insert_query = """
      INSERT INTO your_table_name (column1, column2) 
      VALUES (%s, %s)
      """
      data_to_insert = ('value1', 'value2')

      cursor.execute(insert_query, data_to_insert)

      # Commit the transaction
      connection.commit()

      print("Data inserted successfully!")

  except Exception as e:
      print(f"Error: {e}")

  finally:
      if connection:
          # Close the cursor and connection
          cursor.close()
          connection.close()
          print("Connection closed.") 

# host is ip address   192.168.0.16
  #USE alt delete command to delete none useful lines from nano
  #https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8 
  return 
 def ip_address_table_creator(self):
  '''create ip address table in specified database'''
  import psycopg2
  from psycopg2 import sql
  table_name="ip_address_table_info_on_servers"
  host = 'your-remote-server-ip-or-domain'  # E.g., '192.168.1.100' or 'your-database-server.com'
  port = '5432'  # Default PostgreSQL port
  dbname = 'your-database-name'  # E.g., 'myprojectdb'
  user = 'your-username'  # E.g., 'myuser'
  password = 'your-password'  # E.g., 'mypassword'
  column_name_data_type_dic={
  "computer_name":'text',
  "ip_number":"text",# break this up into list
   "user_name":"text",
   "computer_password":"text",# only if it is a coding file otherwise just paste the active frame
   "dbnames":"text",
   "tables_in_database":"text",
   "data_base_password":"text"}
  try:
      self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
      self.cur = self.conn.cursor()
      create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
      for column_name,data_type in column_name_data_type_dic.items():
          create_table_str+=f",{column_name} {data_type}"
      end_create_table_str = ");"
      create_table_str+=end_create_table_str
      print(create_table_str)
      self.cur.execute(create_table_str)
      self.conn.commit()
  except Exception as E:
          print(E)
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  input()
  return 

  
 def ip_address_look_up_table_creator(self):
  table_name="ip_address_table_info_on_servers"
  column_list=["computer_name","ip_number","user_name","computer_password","dbnames","data_base_password"]
  import psycopg2
  table_columns=""
  values_string=""
  where_string=""
  column_str=""
  self.computer_info_dic={}
  if self.sql_switch==0:
      self.sql_switch=self.init_sql()
  for i2, column in enumerate(column_list):
      if i2==0:
          column_str=column
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
  """ bring data  from database """
  self.computer_info_dic={}
  column_list_len=len(column_list)
  for column in column_list:
      self.computer_info_dic[column]=[] 
  for sql_data_list in sql_data_list_list:
      for column, sql_data in zip(column_list,sql_data_list):
          # this should solve hte problem of code not being super usable because
          # we subbed out commas and such to store it
          sql_data=str(sql_data)
          sql_data=sql_data.replace("^","\'")
          sql_data=sql_data.replace("&","\"")
          sql_data=sql_data.replace("~",",")
          sql_data=sql_data.replace("?","'")
          self.computer_info_dic[column].append(sql_data) 
  #computer_name":'text',
  #"ip_number":"text",# break this up into list
  # "user_name":"text",
  # "computer_password":"text",# only if it is a coding file otherwise just paste the active frame
  # "dbnames":"text",
  # "tables_in_database":"text",
  # "data_base_password":"text"
  print(self.computer_info_dic)
  practice_grabbing_data="""computer_name_index=self.computer_info_dic["computer_name"].index('big_white')
  ip_number=self.computer_info_dic["ip_number"][computer_name_index]
  computer_name=self.computer_info_dic["computer_name"][computer_name_index]
  computer_password=self.computer_info_dic["computer_password"][computer_name_index]
  dbnames=self.computer_info_dic["dbnames"][computer_name_index]
  data_base_password=self.computer_info_dic["data_base_password"][computer_name_index]
  print(computer_name)
  print(computer_name_index)"""
  #input()
  return self.computer_info_dic

 def insert_into_ip_address_table(self,column_name_data_type_dic):
     '''all work is in the input file '''
     self.insert_into_postgres_local(column_name_data_type_dic,table_name="ip_address_table_info_on_servers")
     

  
 def bash_script_template_creator(self):
  ''' '''
  all_computer_names=["big_white","big_black","hp_laptop","website_server","corsair","acer","hp"]
  computer_name= "big_white"
  computer_info=self.ip_address_look_up_table_creator(computer_name)
  host=computer_info["host"]
  username=computer_info["username"]
  self.add_content_of_bash_script()
  self.subprocess_run_script_remotely(command_list)
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 
 def modify_values_in_sql(self):
  ''' '''
  import psycopg2
  from psycopg2 import sql
  
  # Establish the connection to the PostgreSQL database
  connection = psycopg2.connect(
      dbname="your_dbname", 
      user="your_username", 
      password="your_password", 
      host="your_host", 
      port="your_port"
  )
  
  # Create a cursor object to interact with the database
  cursor = connection.cursor()
  
  # Define the SQL UPDATE query with placeholders
  update_query = """
      UPDATE your_table_name
      SET column_name = %s
      WHERE condition_column = %s
  """
  
  # Values to be updated
  new_value = 'new_value'
  condition_value = 'condition_value'
  
  try:
      # Execute the UPDATE query
      cursor.execute(update_query, (new_value, condition_value))
  
      # Commit the transaction to the database
      connection.commit()
  
      # Check how many rows were affected
      print(f"{cursor.rowcount} row(s) updated.")
      
  except Exception as error:
      # Rollback the transaction in case of an error
      connection.rollback()
      print(f"Error: {error}")
  
  finally:
      # Close the cursor and connection
      cursor.close()
      connection.close()
      
 
 def create_master_pyautogui_table(self):
  ''' '''
  table_name="pyautogui_master"
  column_name_data_type_dic={
  "my_id":"text",
  "code":"text",# break this up into list
   "explantory_text":"text",
   "prompt_problem_searched":"text",# only if it is a coding file otherwise just paste the active frame
   "time_stamp":"text",
   "whole_text_chunk":"text",
   "website_link":"text",
   "action":"text"}   
   # dicitonary of objects and qualtities  in problem to use to ask questions  
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  
  return 
 def create_light_pyautogui_table(self,current_pyautogui_light_table_value):
  ''' '''
  current_pyautogui_light_table_value+=1

  table_name=f"pyautogui_light_table_{current_pyautogui_light_table_value}"
  column_name_data_type_dic={
  "my_id":"text",
  "code":"text",# break this up into list
   "explantory_text":"text",
   "prompt_problem_searched":"text",# only if it is a coding file otherwise just paste the active frame
   "time_stamp":"text",
   "whole_text_chunk":"text",
   "website_link":"text",
   "action":"text"}   
   # dicitonary of objects and qualtities  in problem to use to ask questions  
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
  

 def create_used_id_pyautogui_table(self):
  ''' '''
  table_name="used_id_pyautogui_table"
  column_name_data_type_dic={
  "used_my_id_value":"text"# break this up into lis
  }
   
   # dicitonary of objects and qualtities  in problem to use to ask questions
  
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
       

 def delete_info_from_table(self):
  ''' '''

  import psycopg2
  starting_idd
  ending_id=0
  table_name=""
  starting_idd=1
  conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
  cur = conn.cursor()
  #if ending_id!=0:
  cur.execute(f"""DELETE  FROM   {table_name} WHERE id >{starting_idd} ;""")
  #else:
  #    cur.execute(f"""DELETE  FROM   ideas_table_3 WHERE id >{starting_idd} and id < {ending_id} ;""")
  conn.commit()
  #self.conn.close()
  cur.close()

 def problem_solving_program_action_logic(self,pyauto_gui_light_data_list):
  ''' '''
  import re
  text_content=pyauto_gui_light_data_list[1]
  action_value=pyauto_gui_light_data_list[2]
  if  action_value == "problem_solving_data":
      self.insert_into_problem_solving_data()
      self.add_content_to_problem_solving_program()
  if  action_value == "coding_folder_creator":
      self.create_coding_project() 
      self.edit_coding_project()
      self.add_code_to_appriproate_coding_file()    
  return action_value

 def create_table_on_local_database(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def prompt_chat_gpt_2(self):
  """ """
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
  print(computer_name)
  print(computer_name_index) 
  
  exe_file=r"/home/jross77/Documents/pyautogui/ChatGPT__Mozilla_Firefox/pyautogui_function_exe2025_01_11__1736657025.939748.py"
  screen_dir_name="ChatGPT__Mozilla_Firefox"
  bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\pyauto.sh"
  run_pyauto_str=fr'''#!/bin/bash
  source /home/jross77/Documents/pyautogui/venv/bin/activate
  export DISPLAY=:0
  #follow instructions in electornics book to keep screen on
  python3 {exe_file}
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
    
 def mark_as_used_id(self,my_id):
  ''' '''
  import psycopg2
  host = '192.168.2.209'# ip address here
  port = '5432'
  dbname = 'canlawaccessible'
  user = 'jross77'
  password = 'MeganisGreat'
  current_highest_num=0
  newest_pyautogui_light_table=""
  table_name="used_id_pyautogui_table"
  column_name_data_type_dic={
  "used_my_id_value":"text"# break this up into lis
  }  
  print('VALUE INSERTED INTO used_id_pyautogui_table')
  sql_str=f"INSERT INTO used_id_pyautogui_table (used_my_id_value) VALUES ('{my_id}');"
  try:   
      self.cur = self.conn.cursor()
      self.cur.execute(sql_str)
      self.conn.commit()      
  except Exception as E:
    print(E)     
  return 
 def setup_llm_model_from_lm_studio(self):
  """ """

  '''follow guide in electornics book
  https://lmstudio.ai/docs/api/rest-api
  install from website then runt he below command
  chmod u+x LM_Studio-*.AppImage
./LM_Studio-*.AppImage --appimage-extract
cd squashfs-root
sudo chown root:root chrome-sandbox
sudo chmod 4755 chrome-sandbox
./lm-studio
sudo apt  install curl
to get lms to work you need to run a couple commands in studio
  lms server start # to stop, run `lms server stop`
  lms server stop'''
  # lets just run it from huggingface
  import subprocess 
  username="jross77"
  host='192.168.2.200'
  # -t is key here
  ssh_commandd = [f"ssh", f"{username}@{host}","-t","lms"]# put the script you want to run here
  self.subprocess_run_script_remotely(ssh_commandd)
  input()
 
 def query_llm_from_lm_studio(self):
  """add this to problem solving program to query llm when writing strategies or using record problem """
  '''https://lmstudio.ai/docs/api/rest-api
  POST /api/v0/completions
  POST /api/v0/chat/completions
  curl http://localhost:1234/api/v0/chat/completions \
  # list all downloaded models
  curl http://localhost:1234/api/v0/models
  curl http://localhost:1234/api/v0/completions 
  # this shows you how to use the api
  # need to learn how to use the api and add it to the problem solving program
  # check available modles on the system with this command
  curl http://localhost:1234/api/v0/models
  # USE ONE OF THE MODELS LISTED
  # JUST SEND DATA LIKE THIS COMMAND TO THE API
  curl http://localhost:1234/api/v0/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b-instruct",
    "prompt": "the meaning of life is",
    "temperature": 0.7,
    "max_tokens": 100,
    "stream": false,
    "stop": "\n"
  }'  
  '''
  #self.llm_studio_set_up =False
  
  #if self.llm_studio_set_up ==False:
  #    self.setup_llm_model_from_lm_studio() 
  #    self.llm_studio_set_up=True
  import requests
  headers = {
      'Content-Type': 'application/json',}
  json_data = {
      'model': 'llama-7b',
      'prompt': 'What is the meaning of life?',
      'temperature': 0.7,
      'max_tokens': 50,
      'stream': False, }
  response = requests.post('192.168.2.200:1234/api/v1/completions', headers=headers, json=json_data)
  print(response)
  # parse response and upload to coding program or prolem solving program  
  with open('response.json', 'wb') as f:
      f.write(response.content) 
  curl_command="""curl http://localhost:5000/api/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-7b",
    "prompt": "What is the meaning of life?",
    "temperature": 0.7,
    "max_tokens": 50,
    "stream": false
  }' -o response.json"""
 # Note: json_data will not be serialized by requests
 # exactly as it was in the original request.
 #data = '{\n    "model": "llama-7b",\n    "prompt": "What is the meaning of life?",\n    "temperature": 0.7,\n    "max_tokens": 50,\n    "stream": false\n  }'
 #response = requests.post('http://localhost:5000/api/v1/completions', headers=headers, data=data)
  return
 def setup_website_and_api_to_run_llamma(self):
  ''' THE GUIDE FOR GETTING TOKEN HUGGINFACE TO WORK IS guide for huggingface in downloads on latop '''
  more_notes="""use this for running amd gpu
  python manage.py createsuperuser
  sudo apt update
sudo apt install libjpeg-dev python3-dev python3-pip
pip3 install wheel setuptools
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.2/
import torch
print(torch.cuda.is_available())
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  http://<your-local-ip>:8000.
  http://192.168.2.200:8000 # big black
  http://192.168.2.214:8000/# big white"""
  install_and_start_fast_api_windows=""" 
  python -m venv venv
  .\venv\Scripts\activate
  pip freeze > requirements.txt
  pip install -r requirements.txt
  # in virtual envrionmnt
  python -m pip install fastapi
  python -m pip install  uvicorn
  python -m pip install transformers
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  python -m pip install accelerate
  # unblock port 8000 
  Open the Control Panel
  Select Windows Firewall
  Select Advanced settings
  Select Inbound rules
  Select New rule
  Select Port
  Select TCP
  Select Specific local ports
  Enter the port you want to allow
  Select Allow the connection
  Select Next
  Check Domain, Private, and Public
  Enter a name : Fastapi
  .\venv\Scripts\activate
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  # test transformers running

  """
  set_up_llama_to_be_fasster= """ 
  https://huggingface.co/docs/transformers/main/en/model_doc/llama3
  
  """
  
  
  
  commands_bash="""
  
  sudo apt update
  sudo apt install python3 python3-pip
  sudo apt install virtualenv
  mkdir llama
  cd fastapi-project
  virtualenv venv
  source venv/bin/activate
  pip install fastapi uvicorn
  sudo ufw allow 8000
  sudo ufw status
  touch main.py
  # create main.py file to run the api
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  # example post request
  data = {
      "name": "Smartphone",
      "price": 799.99
  }
  # Send POST request to FastAPI server
  response = requests.post(url, json=data)

  # Check if the request was successful
  if response.status_code == 200:
      # Parse and print the response JSON
      response_data = response.json()
      print("Response from FastAPI:")
      print(response_data)
  else:
      print(f"Failed to get response, status code: {response.status_code}")
      
  #### params   
  #@app.post("/items/")
  #async def create_item(item: Item):
  #    return {"name": item.name, "price": item.price}
  """
  
  example_script="""
from fastapi import FastAPI
app = FastAPI()
from pydantic import BaseModel
app = FastAPI() # htis is commented out to avoid errors in file
###class Item(###BaseModel)###:
  #    name: str
  #    price: float
@app.get("/items/")
async def get_item(name: str, price: float):
    # add in huggingface model here to process input
    # proudce output
    return {"name": name, "price": price}
  """
  #pip install transformers torch
  transformer="""
  from transformers import AutoTokenizer, AutoModelForCausalLM
  import torch

  # Load the Llama model and tokenizer from Hugging Face
  model_name = "meta-llama/Llama-2-7b-chat-hf"  # Specify the model name here
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForCausalLM.from_pretrained(model_name)

  # Ensure the model is in evaluation mode and move it to the GPU (if available)
  model.eval()
  if torch.cuda.is_available():
      model = model.to("cuda")
  def generate_response(prompt: str):
      # Tokenize the input prompt
      inputs = tokenizer(prompt, return_tensors="pt")
      
      # Move the inputs to the GPU (if available)
      if torch.cuda.is_available():
          inputs = {key: value.to("cuda") for key, value in inputs.items()}
      
      # Generate a response using the model
      with torch.no_grad():
          outputs = model.generate(
              inputs["input_ids"],
              max_length=100,   # Adjust max_length as needed
              num_return_sequences=1,
              do_sample=True,   # Use sampling, set to False for deterministic output
              top_p=0.9,        # Adjust for controlling randomness
              temperature=0.7,   # Control the creativity of responses
              pad_token_id=tokenizer.eos_token_id
          )
      
      # Decode the generated response
      response = tokenizer.decode(outputs[0], skip_special_tokens=True)
  # Example of running the model with a prompt
  prompt = "What is the capital of France?"
  response = generate_response(prompt)

  print("Generated response:")
  print(response)
  return response """
  happy="""
  `pip install accelerate
  # may need to do a docker image to get this to work
  #https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html
  https://huggingface.co/docs/optimum/en/amd/amdgpu/overview 
  https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/hugging-face-models.html
  pip install transformers

  pip install --upgrade --upgrade-strategy eager optimum[amd]
  
  https://docs.docker.com/engine/install/ubuntu/
  https://huggingface.co/docs/optimum/onnxruntime/usage_guides/amdgpu
  https://huggingface.co/docs/optimum/onnxruntime/usage_guides/amdgpu
  # NEED TO FOLLOW THIS GUIDE FOR AMDGPU on huggingface
  First install rocm
  https://rocm.docs.amd.com/projects/install-on-linux/en/latest/
  create bash file with these command sin side it
  #!/bin/bash
  sudo apt update
  sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
  sudo apt install python3-setuptools python3-wheel libpython3.12
  sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
  wget https://repo.radeon.com/amdgpu-install/6.3.1/ubuntu/noble/amdgpu-install_6.3.60301-1_all.deb
  sudo apt install ./amdgpu-install_6.3.60301-1_all.deb
  sudo apt update
  sudo apt install amdgpu-dkms rocm

  # install docker refer to bahs file i created for this docker_install.sh in llamma folder
  https://docs.docker.com/engine/install/ubuntu/
  # this uninstalls all bad packages
  for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
  Install using the apt repository
  # Add Docker's official GPG key:
  #!/bin/bash
  sudo apt-get update
  sudo apt-get install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc
  # Add the repository to Apt sources:
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update
  
  #2
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  #3 
  sudo docker run hello-world
  
  # go back to huggingface guide
  docker build -f Dockerfile -t ort/rocm . # this doesnt work
  sudo poweroff # to poweroff
  sudo reboot # to reboot
  # trying pytorch route
  https://rocm.docs.amd.com/en/docs-5.1.3/how_to/pytorch_install/pytorch_install.html
  docker pull rocm/pytorch:latest 
  docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G rocm/pytorch:latest

  
  # bare metal install for HUGGINGFACE
  https://huggingface.co/docs/optimum/onnxruntime/usage_guides/amdgpu#accelerated-inference-on-amd-gpus-supported-by-rocm
  Install any dependencies needed for installing the wheels package.
  sudo apt update
  sudo apt install libjpeg-dev python3-dev
  pip3 install wheel setuptools
  pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/rocm5.2/
  Local Installation Steps:
  pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0
  # pre-requisites
  pip install -U pip
  pip install cmake onnx
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  # Install ONNXRuntime from source
  git clone --single-branch --branch main --recursive https://github.com/Microsoft/onnxruntime onnxruntime
  cd onnxruntime
  ./build.sh --config Release --build_wheel --allow_running_as_root --update --build --parallel --cmake_extra_defines CMAKE_HIP_ARCHITECTURES=gfx90a,gfx942 ONNXRUNTIME_VERSION=$(cat ./VERSION_NUMBER) --use_rocm --rocm_home=/opt/rocm
  pip install build/Linux/Release/dist/*
  ### python file to create examples
  https://huggingface.co/docs/optimum/onnxruntime/usage_guides/amdgpu#accelerated-inference-on-amd-gpus-supported-by-rocm
  
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer
ort_model = ORTModelForSequenceClassification.from_pretrained(
  "philschmid/tiny-bert-sst2-distilled",
  export=True,
  provider="ROCMExecutionProvider",
)

tokenizer = AutoTokenizer.from_pretrained("philschmid/tiny-bert-sst2-distilled")
inputs = tokenizer("expectations were low, actual enjoyment was high", return_tensors="pt", padding=True)

outputs = ort_model(**inputs)
assert ort_model.providers == ["ROCMExecutionProvider", "CPUExecutionProvider"]

# error ValueError: Asked to use ROCMExecutionProvider as an ONNX Runtime execution provider, but the available execution providers are ['CPUExecutionProvider'].

from optimum.onnxruntime import ORTModelForSequenceClassification

ort_model = ORTModelForSequenceClassification.from_pretrained(
  "distilbert-base-uncased-finetuned-sst-2-english",
  export=True,
  provider="ROCMExecutionProvider",
)

from optimum.pipelines import pipeline
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

pipe = pipeline(task="text-classification", model=ort_model, tokenizer=tokenizer, device="cuda:0")
result = pipe("Both the music and visual were astounding, not to mention the actors performance.")
print(result)
Additionally, you can pass the session option log_severity_level = 0 (verbose), to check whether all nodes are indeed placed on the ROCM execution provider or not:
import onnxruntime

session_options = onnxruntime.SessionOptions()
session_options.log_severity_level = 0

ort_model = ORTModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    export=True,
    provider="ROCMExecutionProvider",
    session_options=session_options
)
#example to test gpu
import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')

for gpu in gpus:
    print("Name:", gpu.name, " Type:", gpu.device_type)
    
    
    
I have an 7800XT and ROCm 6.0 works just fine, the HIP libraries have gfx1101 enabled, there are even tensile.dat files for rocBLAS.

MIOpen has some gfx11 kernels as well as references to the gfx1101 target, but i didn´t try MIOpen.

However keep in mind, that things like pytorch ship with rocm included and pytorch does not have tensile files for gfx1101 for example. However you can still get it to work by setting: HSA_OVERRIDE_GFX_VERSION='11.0.0', which essentially tells the ROCm libs to use the gfx1100 target instead of the gfx1101 target.



To use the HSA_OVERRIDE_GFX_VERSION variable to make the ROCm libraries target the gfx1100 (instead of gfx1101), you would essentially be telling the ROCm stack to treat your AMD Radeon RX 7800 XT (which is based on the RDNA 3 architecture) as a previous RDNA target (likely RDNA 2-based).
# getting 7800XT to run strats
export HSA_OVERRIDE_GFX_VERSION=11.0.0
echo $HSA_OVERRIDE_GFX_VERSION
Run your ROCm-enabled application: Once the environment variable is set, you can launch the ROCm-enabled software, such as TensorFlow or any other computationally intensive program that uses ROCm for GPU acceleration.
# to persist set up use thuis
echo "export HSA_OVERRIDE_GFX_VERSION=11.0.0" >> ~/.bashrc
source ~/.bashrc

# strat 2
Install amdgpu
Install docker
I have an 7800XT and ROCm 6.0 works just fine,
the HIP libraries have gfx1101 enabled, there are even tensile.dat files for rocBLAS.
Verify or change the docker device storage driver
Build an ROCm container using docker CLI
Verify the ROCm-docker container built successfully
If you're having trouble running ROCm on your 7800 XT, you can try exporting the environment variable HSA_OVERRIDE_GFX_VERSION to 11.0.0 in wsl2. 
https://www.reddit.com/r/ROCm/comments/16zmba9/is_the_rx7800xt_supported_by_rocm/?share_id=ZplQrQTzFGoZzQCosYNcP&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1
#fake the 7900 card
export HSA_OVERRIDE_GFX_VERSION=11.0.0
TORCH_COMMAND='pip install torch torchvision --extra-index-url pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.7' python launch.py --precision full --upcast-sampling
#lots of info here
https://boards.4chan.org/g/thread/103798432/anyone-got-this-shit-running-on-a-7800-xt
#strat 3 just use opencl directly to run cuda
https://www.reox.at/blog/posts/linux_amdgpu_and_opencl_with_RX7800XT/
OpenCL™ (Open Computing Language) is a low-level API for heterogeneous computing that runs on CUDA-powered GPUs. Using the OpenCL API, developers can launch compute kernels written using a limited subset of the C programming language on a GPU.


#strat 4:
I got SD running on a RX 7800XT.
The trick was to use the docker method from: https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs (also make sure your user account is part of the video, renderer and docker group).
First startup will fail, but that's expected. Then update python to v3.9-full like stated on the page.
Manually update pytorch:
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.7
Fake to be a 7900XTX card:
export HSA_OVERRIDE_GFX_VERSION=11.0.0
Then I mananged to start it with:
TORCH_COMMAND='pip install torch torchvision --extra-index-url pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.7' python launch.py --precision full --upcast-sampling
Hope that helps!

#strat 5:
https://github.com/ROCm/ROCm/issues/2590
You will need a 7800 XT, 7900 GRE, 7900 XT or 7900 XTX card, the latest llama.cpp code, and a matching recent Llama 2-13B-based GGUF model.
Export HSA_OVERRIDE_GFX_VERSION=11.0.1 in your environment, then compile llama.cpp for ROCm (using the LLAMA_HIPBLAS=1 option).
Launch the server:
./server -m /path/to/model.gguf -c 4096 -ngl 43 --mlock --host 0.0.0.0 --port 8080
Open http://localhost:8080 in your browser, set temperature to zero, and insert the following prompt in the bottom field:
What happened to Apollo 13?
(Don't change any other options.)
Click Send, then measure the time it takes before Llama starts generating text. (The speed of text generation is unaffected, it's the time it takes for Llama to even begin generating text that takes time. Also, only the first invocation with each prompt is slow - subsequent invocations without restarting the server will come from the prompt cache, and thus hide the regression.)
Now, repeat this procedure with HSA_OVERRIDE_GFX_VERSION=11.0.0 exported in your environment (instead of 11.0.1). Observe how the text starts to get generated almost instantaneously,instead of a multi-second delay as with 11.0.1.
If you replace the prompt with something longer (e.g. "What is this song called?" followed by the lyrics of your country's national anthem), the difference gets exponentially worse.
                                                
                                                 
strat 6:
To get a 7800 XT to run ROCm, you can install amdgpu, docker, 
and build the ROCm container using docker CLI. 
You can also try setting HSA_OVERRIDE_GFX_VERSION='11.0.0'.
However keep in mind, that things like pytorch ship with rocm included and pytorch does not have tensile files for gfx1101 for example.
However you can still get it to work by setting: HSA_OVERRIDE_GFX_VERSION='11.0.0',
which essentially tells the ROCm libs to use the gfx1100 target instead of the gfx1101 target.

STRAT7:
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html

getting torch to work with rocm
git clone https://github.com/pytorch/examples.git
cd examples/mnist
python3 main.py

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html
#pip install torch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2
Testing the PyTorch installation
#STRAT8 THIS IS THE ONE
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html
make sure system prequesites are in place
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html
#obtain linux distro
uname -m && cat /etc/*release
# check supported distro
Ubuntu 24.04.2
upgrade linux distro to a supported distro
24.04.1 LTS currently this
sudo apt update
sudo apt upgrade
sudo do-release-upgrade
# check kernel
uname -srmv
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo apt install python3-setuptools python3-wheel libpython3.12
groups
sudo usermod -a -G video,render $LOGNAME
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf
/etc/udev/rules.d/70-amdgpu.rules 
sudo nano 70-amdgpu.rules
KERNEL=="kfd", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="renderD*", MODE="0666"
sudo udevadm control --reload-rules && sudo udevadm trigger
Grant GPU access to a custom group
sudo groupadd devteam
sudo usermod -a -G devteam jross77
FOLLOW THE ROCM GUIDE:
https://rocm.docs.amd.com/projects/radeon/en/latest/index.html
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/prerequisites.html
sudo apt-get update
sudo apt-get dist-upgrade
FOLLOW the guides produced by the hardware producer first and be careful tof ollow each step
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/howto_native_linux.html
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-radeon.html
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-pytorch.html
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-onnx.html
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-tensorflow.html
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-triton.html

# BIG WHITE NOTES
ALWAYS upgrade packages when getting errors to knewest
needed to upgrade to newest transformers, torch and install accelrate to get big white to work
python -m pip install packaga_name --upgrade
needed to run with admin prvileges for install of pytorch gpu stuff below

# need to download newest version of torch to get gpu to work
https://pytorch.org/get-started/locally/

  
  import torch
  from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaForCausalLM

  tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b")

  with torch.device("cuda"):
    model = AutoModelForCausalLM.from_pretrained(
    "tiiuae/falcon-7b",
    torch_dtype=torch.float16,
    use_flash_attention_2=True,
    )


  """
  
  #https://curlconverter.com/
  #https://stackoverflow.com/questions/42604586/converting-a-curl-to-python-requests
  #pip install --upgrade --upgrade-strategy eager optimum[amd]
  
  
  
# Function to generate a response using the model

 def query_website_and_api_running_llamma(self):
  ''' '''    
  import requests
  #http://192.168.2.200:8000 # big black
  #ssh desktop-s7na8dm\doggo777@192.168.2.214
  #http://192.168.2.214:8000/# big white 
  #>ssh desktop-s7na8dm\doggo777@192.168.2.214
  #cd Documents\psp_api
  #.\venv\Scripts\activate
  #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  url = "http://192.168.2.214:8000/items/"
  params = {
    "prompt": "write me a function to access a database remotely",
    "price": 999.99}
# Send GET request to FastAPI server with query parameters
  response = requests.get(url, params=params)
  # Send POST request to FastAPI server
  print(response.json())
  # Check if the request was successful
  if response.status_code == 200:
      # Parse and print the response JSON
      response_data = response.json()
      print("Response from FastAPI:")
      print(response_data)
      print('hi')
      response_str=response_data['name']['content']
      # process data here
      print("Response from FastAPI:")
      print(response_str)         
  else:
      print(f"Failed to get response, status code: {response.status_code}")   
  return response_str 
 
 def create_table_sql(self):
  ''' '''
  
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 
 def create_prompt_table(self):
  ''' '''
  import psycopg2
  table_name="prompt_table"
  column_name_data_type_dic={
  "prompt":'text',
  "prompt_type":"text",# break this up into list
   "timee":"text"}
  try:
      self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
      self.cur = self.conn.cursor()
      create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
      for column_name,data_type in column_name_data_type_dic.items():
          create_table_str+=f",{column_name} {data_type}"
      end_create_table_str = ");"
      create_table_str+=end_create_table_str
      print(create_table_str)
      self.cur.execute(create_table_str)
      self.conn.commit()
  except Exception as E:
          print(E)
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  input()
  

 def upload_prompts(self,table_column,column_value,sql_str,E):
  ''' '''
  import psycopg2
  import re
  from psycopg2 import sql
  table_name="prompt_table"
  import time
  timee=time.time()
  #use data generated in questions of fpsp?
  #add extra column for prompt type
  dictionary_of_values={
  "prompt":['text'],
  "prompt_type":['text'], #prompt types
   "timee":[]}
  prompt_list_len=len(dictionary_of_values["prompt"])
  
  for i in range(prompt_list_len):
      dictionary_of_values["timee"].append(timee)
      
  try:
      self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
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
  
     
 def categorize_all_websites_to_perform_speicfic_actions_on_like_apply_for_grants(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def check_terms_and_conditions_program_on_website_before_crawl(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_website_world_map_and_real_world_map_to_figure_out_actions_to_take(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_automated_psp_coding_table(self):
  ''' '''

  table_name="automated_psp_coding"
  column_name_data_type_dic={
      
      "problem_name":"text",
      "prompt_env_list":"text",
      "env_response_str_list":"text",
      "prompt_glossary_list":"text",
      "glossary_response_str_list":"text",
      "prompt_strat_list":"text",
      "strat_response_str_list":"text" }
    
   # dicitonary of objects and qualtities  in problem to use to ask questions  
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
  
  
  
       
       
       
  
       
  return table_name,column_name_data_type_dic
  return 
 def automatically_sign_up_for_all_free_trials_in_world(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_auto_psp_table(self):
  ''' '''

  table_name=f"auto_psp_table"
  column_name_data_type_dic={
      "problem_name":"text",
      "prompt_env_list":"text",
      "env_response_str_list":"text",
      "prompt_glossary_list":"text",
      "glossary_response_str_list":"text",
      "prompt_strat_list":"text",
      "strat_response_str_list":"text" }
    # dicitonary of objects and qualtities  in problem to use to ask questions  
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
  
   
       
       
       
  
       
  return table_name,column_name_data_type_dic
 def setup_tailwind_django(self):
  r''' 
  https://learndjango.com/tutorials/django-login-and-logout-tutorial
  https://www.freecodecamp.org/news/how-to-integrate-tailwind-with-django/
  follow the django installaiton instructions
  if possible just copy over whole dir of working django project like folder psp_website just work standalone
  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\psp_website
  #otherwsie follow below steps

 
  python3 -V
  python3 -m venv env
  source env/bin/activate
  env\Scripts\activate
  python -m pip install django
  python -m pip install psycopg2
  pip install django-environ
  sudo apt-get install --reinstall libpq-dev
  pip install psycopg2-binary
  mkdir psp
  django-admin startproject project psp
  cd psp
  django-admin startapp auto_coding_psp
  python manage.py runserver
  python manage.py migrate
  mkdir auto_coding_psp\templates
  
  #create db Website_Can_Law_Accessible
  # manually make database this in windows in pgadmin, if in linux follow the below commands
  createdb Website_Can_Law_Accessible
  sudo -u postgres psql
  CREATE ROLE jross77 WITH LOGIN PASSWORD 'MeganisGreat';
  GRANT CONNECT ON DATABASE canlawaccessible TO jross77;
  ALTER ROLE jross77 WITH SUPERUSER;
  \q 
  # NEED TO DO THIS EVERY TIME TO UPDATE POSTGRES DATABASE MODELS
  # to add models to postgres database use the following:
  manage.py migrate
  python manage.py migrate
  
  ###setup django site using previously created files in FLIP_Website
  copy over models,views,and urls,utils,templates and templates to new folder
  

  ### setup postgres on django database
  https://www.strongdm.com/blog/postgres-create-user
  https://stackoverflow.com/questions/4482239/postgresql-database-service
  #login to laptop database using this
  psql -U postgres # password Meganiscute
  psql -U postgres -d can_law_accessible # password Meganiscute
 

  $ sudo -u postgres psql
  \password
  Enter password: ...  

  ## set up environment file and .env to secure the website
  #copy .env to postgres project
  from pathlib import Path
  import environ
  import os
  env = environ.Env()
  environ.Env.read_env()
  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent
  # Quick-start development settings - unsuitable for production
  # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = env("SECRET_KEY")
  set database to 
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': env("DB_NAME"),
          'USER': env("DB_USER"),
          'PASSWORD': env("DB_PASSWORD"),
          'HOST': env("DB_HOST"),
          'PORT': env("DB_PORT"),
      }
  }
  #login to manage.py windows
  #windows
  # for production change it to the above for now use the below database settings and key
  set SECRET_KEY='django-insecure-cej+-)*u$e!0!c)lfqk%5^leuauh5^$kqvc)bvg@77t@@e6*sp'
  # set all other variables above as well manually in a bash script then
  python manage.py runserver
  #linux
  pwd
  source .DJANGO_SECRET_KEY
  echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
  source .DJANGO_SECRET_KEY
  psql -h localhost -U postgres -p 5432


  C:\Program Files\PostgreSQL\14\
    Set the PostgreSQL Environment Variables
    C:\Program Files\PostgreSQL\15\bin
    # add environment variable to bin directory
    C:\Program Files\PostgreSQL\15\bin
    # psql should now work that you have created envrionment variable
    psql -h 192.168.2.209 -U jross77 -d canlawaccessible #ip is of the server currently at Goulburn
    # it works
    Try these commands
    \dt
    SELECT * FROM my_table;
    \q
    Firewall Issues: Ensure that the PostgreSQL server’s port (default 5432) is not blocked by a firewall on the remote server.
    The .env file should be in the same directory as settings.py
    # this is for laptop
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
            'NAME': 'Website_Can_Law_Accessible',  # Name of the database you created
            'USER': 'postgres',  # PostgreSQL username
            'PASSWORD': 'Meganiscute',  # PostgreSQL password
            'HOST': 'localhost',  # Leave as 'localhost' if the database is on the same machine
            'PORT': '5432',  # Default port for PostgreSQL
        }
    }
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
          'NAME': 'canlawaccessible',  # Name of the database you created
          'USER': 'jross77',  # PostgreSQL username
          'PASSWORD': 'MeganisGreat',  # PostgreSQL password
          'HOST': 'localhost',  # Leave as 'localhost' if the database is on the same machine
          'PORT': '5432',  # Default port for PostgreSQL
      }
  }
    
create all the models to run psp and transfering them over from other database
you must not manually delete tables from postgres let django take car eof it to prevent errors
# this will make a list of columns we can copy SUPER VALUEABLE
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'code_base'
  AND table_schema = 'public'  -- Adjust schema if needed
ORDER BY ordinal_position;
# once all models are uploaded need to transfer data over
# use busines script funciton to copy data over
# funciton is called select all data form one table insert into table in otehr database
# ONLY USE THIS OEN IF OTHER ONE DOES NOT WORK
COPY (SELECT column1, column2, column3 FROM source_table) 
TO '/path/to/source_table.csv' DELIMITER ',' CSV HEADER;
COPY destination_table (column1, column2, column3) 
FROM '/path/to/source_table.csv' DELIMITER ',' CSV HEADER;

# use this wind to install tailwind in a project directory
https://tailwindcss.com/docs/installation/tailwind-cli
# refer to psp_website for how its done or just copy this project
USE TAILWIND COMMAND LINE INTERFACE
refer to http://127.0.0.1:8000/f_window/
# add this to header
# find latest docs on tailwind and follow instrcutiosn on there these are currently latest
npm install tailwindcss @tailwindcss/cli
@import "tailwindcss"; # add to dir src and create input.css file and output.css file
# start css updaer
npx @tailwindcss/cli -i .\static\input.css -o .\static\output.css --watch
# need to run command from static to get this to work
# and keep it listening for css to work
# i cli imports the code and 
# add tailwind to html
<link href="./output.css" rel="stylesheet"># in head and path to tailwind file it to css
Configure static files in django following this guide
https://docs.djangoproject.com/en/5.1/howto/static-files/ 
https://stackoverflow.com/questions/61456431/how-do-i-load-css-file-into-html-in-django 
# add this to setting sfolder
STATICFILES_DIRS = [ BASE_DIR / "static",]
# have a static file in your base dir
# add this to html
{% load static %}
Some code here.....
<link href="{% static 'output.css' %}" rel="stylesheet"> # add this to header
# add this to urls folder
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# will need ot change during produciton for more security usng nginx server
# refer to tailwind css doc for examples of things to add
https://tailwindui.com/?ref=top
https://tailwindflex.com/@bunny/simple-login-form
https://tailwindui.com/components/marketing/sections/newsletter-sections
https://tailwindui.com/components/marketing/sections/heroes
https://docs.djangoproject.com/en/5.1/topics/db/queries/
https://www.brennantymrak.com/articles/fetching-data-with-ajax-and-django
https://stackoverflow.com/questions/11762629/pass-information-from-javascript-to-django-app-and-back
https://how.dev/answers/how-to-add-an-eventlistener-to-multiple-elements-in-javascript
python -m pip install bs4
pip install spacy
python -m spacy download en_core_web_sm
nltk.download('punkt_tab')
python -m pip install nltk
load in ncessary models and install them in virtual envrionment
when sending get requests very sensntive to every slash and spelling
# brackets in javascript need to be correct or a error will be fprodciued in console
# must work within other functions in javascript like post request cant export all data
# use this for django
{% for item in hehe%}
<span class="text-info">Case Name: {{ item.0}} </span>
{% endfor %}
{% for key, values in context.items %}
{% for item in values%}
{% endfor %}
<body class="bg-gray-100 p-6">
    <div class="grid grid-cols-3 gap-4">
        <div id="item1" class="bg-blue-500 text-white p-4">Item 1</div>
        <div id="item2" class="bg-green-500 text-white p-4">Item 2</div>
        <div id="item3" class="bg-red-500 text-white p-4">Item 3</div>
    </div>

    <script>
        // Fetch data from the backend API
        fetch('http://localhost:3000/api/items')
            .then(response => response.json())  // Parse the JSON response
            .then(data => {
                // Dynamically update the content of each grid item
                document.getElementById('item1').innerText = data[0].content;
                document.getElementById('item2').innerText = data[1].content;
                document.getElementById('item3').innerText = data[2].content;
            })
            .catch(error => console.error('Error fetching data:', error));
    </script>


   

             

'''
 
 def retrieve_column_data(self,download_table_name):
      """ """
      import psycopg2
      self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
      self.cur = self.conn.cursor()        
      sql_str_column_finder=f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{download_table_name}';"     
      try:
          self.cur.execute(sql_str_column_finder)
      except Exception as E:
          print(E)
      sql_column_list_list= self.cur.fetchall()  
      column_name_list=[]
      column_name_str=""
      # need to deal with organizing of columns to ensure they match up
      for i8, column_name in enumerate(sql_column_list_list):
          column_name=column_name[0]    
          if i8==0:
              column_name_list.append(column_name)
              column_name_str+=f"{column_name}"
          else:
              column_name_list.append(column_name)
              column_name_str+=f",{column_name}"        
              
      return  column_name_str,column_name_list
 def retrieve_table_data(self,column_name_str,download_table_name):
      """ """
      sql_str=f"SELECT {column_name_str} FROM {download_table_name};"
      try:
          self.cur.execute(sql_str)
      except Exception as E:
          print(E)
      sql_data_list_list= self.cur.fetchall()# real data for specific table
      self.cur.close()
      self.conn.close()
      return sql_data_list_list
  
 def process_table_column_names(self,table_column,table_columns,iterator):
      """ """
      if iterator==0:
          #print(f"table_column{table_column}")
          table_columns =  f"{table_column}"                      
      else:
          table_columns=  table_columns + f",{table_column}"
      return table_columns 
  
 def clean_column_value_for_sql(self,column_value):
      """ """
      import re
      column_value=str(column_value)
      column_value=column_value.replace("\'","")
      column_value=column_value.replace("\"","")
      column_value=column_value.replace(","," ")
      column_value=column_value.replace("'","")
      column_value=re.sub("\"","",column_value)      
      return column_value
 def break_up_column_value_if_too_long(self,column_value):
     """ need to find a way to remind database this is connected to orginal function, if funciton too long"""
     temp_column_value_list=[]
     column_value_len=len(column_value)
     if column_value_len>=19000:
         temp_column_value_list=[]
         for i in range(0,len(column_value),19000):
             column_value_chunk=column_value[i:i+19000]
             temp_column_value_list.append(column_value_chunk)
     if column_value_len<19000:
         temp_column_value_list.append(column_value)    
     return temp_column_value_list
 
    
 def create_table_column_value_str(self,temp_column_value_list,new_stored_str_list,iterator):
     """ need to get this to work """ 
     stored_str_list=new_stored_str_list
     new_stored_str_list=[]
     for column_value in temp_column_value_list: 
         if iterator==0:
             new_stored_str_list.append(f"'{column_value}'") 
         else:
             for stored_str in stored_str_list: 
                 new_stored_str=stored_str+ f",'{column_value}'"
                 new_stored_str_list.append(new_stored_str) 
              # if multiple temp column value 
             # dont want to add both to str need to instead build seperate ones        
     return new_stored_str_list
 
     
 def insert_values_stringgs_into_sql(self,new_stored_str_list,table_columns,upload_table_name):
     """ """
     
     
     for values_stringg in new_stored_str_list:# set up as a list   
       sql_str=f"INSERT INTO {upload_table_name} ({table_columns}) VALUES ({values_stringg});"
       #print(sql_str)
       try:
           self.cur.execute(sql_str)
       except Exception as E:
           print(f"table_columns{table_columns}")
           print(f"values_string{new_stored_str_list}")
           print('EROR')      
           print(E)
           input()             
 def select_all_data_from_one_table_insert_into_table_in_other_database(self):
  ''' '''
  import re
  import psycopg2
  #"auto_strategy_table","code_base_table", "auto_problem_table","code_base_all_version_info","ip_address_table_info_on_servers"
  #"galaxies_table","ideas","ideas2","ideas_table_3",
  #"labels_for_idea_program","labels_for_idea_program_2",
  tables_to_copy_list=[
                       "problem_tree_table","problem_table",
                       "prompt_table", "methods_table","strategy_table","problem_solving_screen_recording_table"]
  for download_table_name in tables_to_copy_list:
      try:
          column_name_str,column_name_list=self.retrieve_column_data(download_table_name)
          sql_data_list_list=self.retrieve_table_data(column_name_str,download_table_name)          
          self.conn = psycopg2.connect(dbname='Website_Can_Law_Accessible', user='postgres', password='Meganiscute')
          self.cur = self.conn.cursor()
          upload_table_name= "auto_coding_psp_"+download_table_name
          for sql_data_list in sql_data_list_list:
              value_str_list2=[]
              values_string=""
              column_name_value_str_list_dic={}
              table_columns=""
              stored_str_list=[]
              new_stored_str_list=[]
              for i5, column_value in enumerate(sql_data_list):
                  table_column=column_name_list[i5]
                  if table_column=="id":
                      table_column="idd"
                  table_columns= self.process_table_column_names(table_column,table_columns,i5)
                  column_value=self.clean_column_value_for_sql(column_value)
                  temp_column_value_list=self.break_up_column_value_if_too_long(column_value)# produces broken up column values 
                  new_stored_str_list=self.create_table_column_value_str(temp_column_value_list,new_stored_str_list,i5)             
              self.insert_values_stringgs_into_sql(new_stored_str_list,table_columns,upload_table_name)
              print(upload_table_name)
              #self.conn.commit()                                                     
          print(download_table_name)   
          self.conn.commit()     
          self.cur.close()
          self.conn.close()    
      except Exception as E:
          print(E)
          #auto_coding_psp_auto_strategy_table
      
  
  
  
  
  
 def setup_computer_to_run_fast_api(self):
  ''' '''
  # step 1
  #pip3 freeze > requirements.txt  # Python3 # get all required packages from environment on big white in requirement file
  #pip install pipreqs
  #pipreqs /path/to/project
  #step 2
  #Step 1 scp current working fastapi info from big white to laptop with requirements file
  # only copy over the main,py file and requirements rather than whole directory next time
  #scp -r username@remote_server_ip:/path/to/source_directory /local/destination/directory
  #scp -r desktop-s7na8dm\doggo777@192.168.2.214:C:\Users\doggo777\Documents\psp_api C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\fast_api_big_white 
  #Step2 scp this info to big black from laptop
  #scp -r /path/to/local/storage user@remote.host:/path/to/copy
  #scp -r  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\fast_api_big_white jross77@192.168.2.200:/home/jross77/Documents/psp_api
  #Step3  install environment and necessary dependencies
  #cd /home/jross77/Documents/psp_api2
  #python3 -m venv env
  #source env/bin/activate
  # test run script without uvicorn
  #python3 main.py
  # step 4 install all dependencies
  FOLLOW_THIS_FUNCTION_for_depeneceies=""
  dependent="""sudo apt install uvicorn
   pip install fastapi
  """
  
  
  # cp main.py /home/jross77/Documents/psp_api2
  #/home/jross77/Documents/psp_api/fast_api_big_white/psp_api
  
  
  
  
  
  #ssh jross77@192.168.2.200
  #cd /home/jross77/Documents/psp_api/fast_api_big_white/psp_api
  #source env/bin/activate
  #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  #http://192.168.2.200:8000 # big black
  
  #pip install -r requirements.txt
  #sudo apt install python3.12-venv
  #rm -r venv/
  # step 4 install all dependencies
  
  
  # step 5 test run api on big black
  #ssh desktop-s7na8dm\doggo777@192.168.2.214
  #http://192.168.2.214:8000/# big white 
  #>ssh desktop-s7na8dm\doggo777@192.168.2.214
  #cd Documents\psp_api
  #.\venv\Scripts\activate
  #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def transfer_pyautogui_creation_program_to_other_computers(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_pyautogui_exe_files_table_on_server(self):
  ''' '''
  table_name=f"pyautogui_exe_files_table"
  column_name_data_type_dic={
       "exe_file_name":"text",
       "multi_exe_file_name":"text",
       "code_file_name":"text",
       "bash_function_name":"text",
       "window_name":"text",
       "timee":"text",
       "computer_name":"text",
       "host":"text",
       "other_files":"text"}
     # dicitonary of objects and qualtities  in problem to use to ask questions  
     # current ip is the website server i think
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 

  #context_info about how this function fits in overall pipeline:

 def transfer_over_and_run_pyautogui_creation_program(self):
  '''going to run clicks on other comptuer instead based on screen size difference
  # just vary the clicks based on screen size and record timign ad write the script
  on the other computer using that
  # or keep it simple and just vary the script over
  and try to create scripts locally by running clicks to get pixels to line up
  # would save time moving over to other computer
  # have options to execute the commands locally if the script does not work
  # so bascially create fall back too so create this function
  # and create 
  this way to avoid going to manually on other computer'''
  # upload pyautogui creation script to other computer directory of pyautogui and directory of other computer pyautogui
  # choose the ip address
  # run pyautogui creaton script on other computer like i run law society script
  host="192.168.2.200"
  #copy_dir_1="scp -r C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\pyautogui_for_generative_model_access a1.1.1.1.1.1 jross77@192.168.2.200:/home/jross77/Documents/pyautogui"
  scp_command = [f"scp","-r",rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\pyautogui_for_generative_model_access a1.1.1.1.1.1 jross77@{host}:/home/jross77/Documents/pyautogui"]# put the script you want to run here 
  self.subprocess_run_script_remotely(scp_command)
  #copy_dir_2="scp -r C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\Inputs jross77@{host}:/home/jross77/Documents/pyautogui"
  scp_command = [f"scp","-r",rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\Inputs jross77@{host}:/home/jross77/Documents/pyautogui"]# put the script you want to run here 
  self.subprocess_run_script_remotely(scp_command)
  # start pyautogui using the init input script
  # need to modify this for ubuntu and linux
  # start pyautogui scirpt using bash
  
  #### modify to copy over pyautogui contnet
  import subprocess
  import os
  import re
  import sys
  # always need to specify host computer to run pyautogui on
  host=sys.argv[1]
  print(host)
  print('nEHEHEH')
  #input()
  username="jross77"
  #host='192.168.2.207'
  testttt=True
  # only upload necessary files from now on if possible
  # to make testing much faster
  script_to_test=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\ChatGPT__Mozilla_Firefox\ChatGPT__Mozilla_Firefox2025_01_02__1735871006_360773.py"
  file_name_with_dir_list=re.split(r"\\",script_to_test)
  print(file_name_with_dir_list)
  file_name=file_name_with_dir_list[-1]
  screen_folder=file_name_with_dir_list[-2]
  dir_to_law=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox"
  #exe_file=r"/home/jross77/Documents/pyautogui/Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox/pyautogui_function_exe2025_01_07__1736308571.4890265.py"
  #exe_file=r"/home/jross77/Documents/pyautogui/Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox/pyautogui_function_exe2025_01_08__1736317384.5429323.py"
  exe_file=r"/home/jross77/Documents/pyautogui/Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox/pyautogui_function_exe2025_01_08__1736321463.4291465.py"
  screen_dir_name="Home__The_Law_Foundation_of_Ontario__Mozilla_Firefox"
  bash_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\bash_files\pyauto.sh"
    
  run_pyauto_str=f"""#!/bin/bash
  source /home/jross77/Documents/pyautogui/venv/bin/activate
  # Run the Python script with arguments
  # need to run it as a subprocess or find way to execute it as if its not being sshed
  export DISPLAY=:0
  #follow instructions in electornics book to keep screen on
  #xdotool mousemove 100 200 # this works and gives me hope
  python3 {exe_file}
  #python3 /path/to/your_script.py arg1 arg2
  #xvfb-run python your_script.py
  # Deactivate virtual environment (if needed)
  deactivate"""
  # change this to only copy the newest files maybe
  if testttt!=True:
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
      #input()
  #input()


  #context_info about how this function fits in overall pipeline:
  
  
  print('hi')
  print('meow')
       
  return 
 def setup_open_hands(self):
  '''
  https://docs.docker.com/desktop/setup/install/linux/
  sudo apt install gnome-terminal
  sudo apt-get update
  # download from website
  https://docs.docker.com/desktop/setup/install/linux/ubuntu/
 sudo apt-get install ./docker-desktop-amd64.deb
 https://docs.docker.com/engine/install/ubuntu
 install docker engine using above 
 # Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# install open hands

$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
$ docker run hello-world
$ reboot

  docker pull docker.all-hands.dev/all-hands-ai/runtime:0.24-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.24-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands-state:/.openhands-state \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.24
  
  
  '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return
 def exe_pyautogui_creation_script_on_other_computers_sub(self,username,host,remote_computer_script_dic,dir_to_store_script_linux,bash_file_name,bash_file_name_linux):
  """ remote computer dir need this to copy over
         then execute these functions on remote dir"""
  # sort out bash file name
  # figure out this scrip
  #bash_file_name=remote_computer_script_dic["bash_file_name"]
  dir_scripts_stored=remote_computer_script_dic["dir_to_store_script"]
  final_linux_script_dir=remote_computer_script_dic["final_linux_script_dir"]
  script_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_server_files" 
  mkdir_command = [f"ssh","-X",  f"{username}@{host}","mkdir","-p",f"{dir_to_store_script_linux}"]
  self.subprocess_run_script_remotely(mkdir_command)
  mkdir_command = [f"ssh","-X",  f"{username}@{host}","mkdir","-p",f"{final_linux_script_dir}"]
  self.subprocess_run_script_remotely(mkdir_command)
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
  scp_command = [f"scp","-r",rf"{dir_scripts_stored}",f"jross77@{host}:/home/jross77/Documents/pyautogui_remote_creation_files"]# put the script you want to run here 
  #scp_command_list = [f"scp","-r", f"{script_dir}",  f"{username}@{host}:/home/jross77/Documents/"]# put the script you want to run here 
  self.subprocess_run_script_remotely(scp_command)
  doc2ui = [f"ssh","-X",  f"{username}@{host}","dos2unix",f"{bash_file_name_linux}"]
  self.subprocess_run_script_remotely(doc2ui)      
  print('DOC')
  #input()
  ssh_command = [f"ssh",  f"{username}@{host}",f"bash {bash_file_name_linux}"]# put the script you want to run here
  self.subprocess_run_script_remotely(ssh_command)
 def test_script_to_fix_mouse_scaling(self):
  ''' figure out a method to write test cases'''
  import subprocess
  import os
  import re
  import sys
  user_name="jross77"
  host="192.168.2.233"
  import time
  timee=time.time()
  #remote_computer_script_dic=self.create_pyautogui_file_of_inputs_and_video(previous_active_window,previous_active_window_url, remote=True)# add this to a specific directory
  # need to find location of all of these to test only single script
  root_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_creation_files"
  pyauto_file_dir_list=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_creation_files")
  self.dir_to_store_script_linux=r"/home/jross77/Documents/pyautogui_remote_creation_files/"+"\PolicenowneedawarranttogetapersonsIPaddressSupremeCourtrulesCBCNewsMozillaFirefox"
  dir_to_store_script=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_remote_creation_files\\PolicenowneedawarranttogetapersonsIPaddressSupremeCourtrulesCBCNewsMozillaFirefox"
  dir_to_store_script_linux=self.dir_to_store_script_linux
  single_exe_process_file_name_linux= self.dir_to_store_script_linux+"/"+r"pyautogui_function_exe2025_03_02__1740915035.1175854.py"
  code_file_name_only=r"PolicenowneedawarranttogetapersonsIPaddressSupremeCourtrulesCBCNewsMozillaFirefox2025_03_02__1740915035_1155868.py"  
  bash_code_to_get_run_xdo_tools_and_create_pyautogui=f"""#!/bin/bash
source /home/jross77/Documents/pyautogui/venv/bin/activate
export DISPLAY=:0   
touch ~/.Xauthority
ls -l ~/.Xauthority
chmod 600 ~/.Xauthority
xdotool mousemove 100 200 click 1
python3 {single_exe_process_file_name_linux}  """   
  print(single_exe_process_file_name_linux) 
  print(dir_to_store_script)
  print('BASH')
  print(dir_to_store_script_linux)
  bash_file_name=dir_to_store_script+r"\bash" +str(timee)+".sh"
  print(bash_file_name)
  bash_file_name_linux=dir_to_store_script_linux+r"/bash" +str(timee)+".sh"
  print(bash_file_name_linux)
  print(" correct          /home/jross77/Documents/pyautogui_creation_scripts/")
  remote_computer_script_dic={"dir_to_store_script":dir_to_store_script,"final_linux_script_dir":dir_to_store_script_linux}
  with open(bash_file_name,"w") as f:
      f.write(bash_code_to_get_run_xdo_tools_and_create_pyautogui)
      print('write')
  self.exe_pyautogui_creation_script_on_other_computers_sub(user_name,host,remote_computer_script_dic,dir_to_store_script_linux,bash_file_name,bash_file_name_linux)
  #copy over dir pyautogui
  # step 1 find script to repeadily execute on remote server
  # step 2 modify this script as necessary to get scaling to work
  # and to make sure it is doing the correct things  
  return 
 def start_up_website_on_local_network(self,website_name):
   ''' go to elecotrnics doc for info on how to start server
   THIS IS THE PSP starter on webserver? '''
   bash_file_str="""#!/bin/bash
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
sudo killall gunicorn
python manage.py collectstatic
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
python manage.py collectstatic
python manage.py migrate
"""
   # C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites # this dir has all the websites
   edit_file_path=""
   scp_command = [f"scp","{edit_file_path}",f"jross77@{host}:/home/jross77/Documents/pyautogui_remote_creation_files"]# put the script you want to run here 
   self.subprocess_run_script_remotely(scp_command)
   self.create_and_run_bash_file(bash_file_str)
   

  
 
 def start_up_website_on_internet(self,website_name,project_folder_name):
  '''
  '''
  # need to end current ngninx server and reload it
  # with another server
  # edit files by copying over them prior to sending in the bash script if you need to change any of the underlying 
  #configurations
  bash_file_str="""#!/bin/bash
pwd
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl reload nginx
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
sudo killall gunicorn
python manage.py collectstatic
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
python manage.py collectstatic
python manage.py migrate
"""
    # C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites # this dir has all the websites
  self.create_and_run_bash_file(bash_file_str)

  return 

 def update_website_code_and_restart_website(self,website_name,sub_dir_list,copy_sub_dirs=True,copy_whole_website=False):
  '''make edits to website on laptop and then send these edits to remote server and update server
  assume we will be running as website and not locally
  WE WILL BE WORKING ON PSP FOR NOW
  but from raise me up file
  will need to modify some local files ont he server to make this work
  NOTE Raise you up on laptop is a copy of website 5 the oen that works
  will need to specify specific dirs to copy to make this work faster in future
  echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
  # copy folders being modified in real time make this improvement when you have time
  going to need to edity some files to get multple fo these to run wit nginx
  need to do this for all websites
  pkill gunicorn is KEY
  print('please use pkill gunicron after updating site to fix catching and display issues of html')

  '''
  import os
  # going to use systemctl now so multiple instances
  test="""


sudo systemctl start flip.socket
sudo systemctl enable flip.socket

sudo systemctl start jasper_legal_news.socket

sudo systemctl enable jasper_legal_news.socket
sudo systemctl status flip.socket
sudo systemctl status jasper_legal_news.socket
file /run/jasper_legal_news.sock
file /run/flip.sock
sudo systemctl daemon-reload
sudo systemctl restart flip.socket flip.service
sudo systemctl restart jasper_legal_news.socket jasper_legal_news.service
sudo systemctl restart nginx
sudo systemctl restart gunicorn
  
  """
  start_up_website_on_internet="""#!/bin/bash
pwd
sudo systemctl restart gunicorn
sudo systemctl restart nginx
"""
#systemctl start nginx
#systemctl enable nginx
  old_start_single_websites_on_internet_bash=F"""#!/bin/bash
pwd
sudo killall gunicorn
ps ax|grep gunicorn
cd /home/jross77/all_websites/{website_name}
source env/bin/activate
cd freelegalproject
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
"""
  host="192.168.2.209"
  host_name="jross77"
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
  print(website_dirs)
  mkdirr=False
  if mkdirr==True:
      dir_to_make="/home/jross77/all_websites/"
      self.mkdir_dir_bash(dir_to_make,host,host_name)
  #scp_command = [f"scp","-r",rf"{local_folder_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here 
  if copy_sub_dirs==True:
      for i, intital_dirr_with_spaces in enumerate(sub_dir_list):
          sub_dir_win=r""
          sub_dir_lin=""
          dirr_list=intital_dirr_with_spaces.split(" ")
          for dirrr in dirr_list:
              sub_dir_lin+=f"/{dirrr}"
              sub_dir_win+=rf"\{dirrr}"
          local_folder_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\{website_name}\{sub_dir_win}"
          remote_dir_path=rf"/home/jross77/all_websites/{website_name}"
          # may need to add sudo here
          scp_command = [f"scp","-r",rf"{local_folder_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here 
          self.subprocess_run_script_remotely(scp_command)
  if copy_whole_website==True:
      website_dir_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\{website_name}"
      remote_dir_path=rf"/home/jross77/all_websites"
      scp_command = [f"scp","-r",rf"{website_dir_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here 
      self.subprocess_run_script_remotely(scp_command)

  self.create_and_run_bash_file(start_up_website_on_internet,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True) 
  return 

 def mkdir_dir_bash(self,dir_to_make,host,host_name):
   """ """
   import subprocess
   mkdir_bashs=rf"""#!/bin/bash
# Define the directory path
DIR="{dir_to_make}"
# Create the directory
if [ -d "$DIR" ]; then
 echo "dir exists!"
else
 echo "dir not exists!"
 mkdir -p "$DIR"
 chmod 777 "$DIR"
 sudo chown jross77 "$DIR"
fi   """   
   mkdir_local_file_name=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\New folder\bash.sh"
   with open(mkdir_local_file_name,"w") as f:
       f.write(mkdir_bashs)
   scp_command_list = [f"scp",f"{mkdir_local_file_name}",  f"{host_name}@{host}:/home/jross77/"]# put the script you want to run here 
   self.subprocess_run_script_remotely(scp_command_list)
   #ssh into the 
   doc2ui = [f"ssh","-X",  f"{host_name}@{host}","dos2unix","/home/jross77/bash.sh"]
   self.subprocess_run_script_remotely(doc2ui)  
   ssh_command = [f"ssh",  f"{host_name}@{host}",f"bash /home/jross77/bash.sh"]# put the script you want to run here
   try:
       subprocess.run(ssh_command, check=True,shell=True)
   except subprocess.CalledProcessError as e:
       print(f"Failed to SSH into {host}: {e}")
         
     
 def create_and_run_bash_file(self,bash_script_str,bash_write_dir_name="/home/jross77/bash/",bash_file_name=r"pyauto.sh",mkdirr=False,local_bash_dir_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash",host="192.168.2.209",host_name="jross77",sudoo=False):
  ''' save unique bash file name here'''
  import subprocess
  local_bash_filee=local_bash_dir_path+"\\"+bash_file_name
  if mkdirr==True:
      self.mkdir_dir_bash(bash_write_dir_name,host,host_name)
  with open(local_bash_filee,"w") as f:
      f.write(bash_script_str)
  scp_command_list = [f"scp",f"{local_bash_filee}",  f"{host_name}@{host}:{bash_write_dir_name}"]# put the script you want to run here 
  self.subprocess_run_script_remotely(scp_command_list)
  #ssh into the
  #copy_content_of_dir= r"cp -a website5/. /home/jross77/all_websites/psp_website"
  #copy_contents_of_directory=r"cp -a psp_website/. raise_you_up/"

  doc2ui = [f"ssh","-X",  f"{host_name}@{host}","dos2unix",f"{bash_write_dir_name}/{bash_file_name}"]
  self.subprocess_run_script_remotely(doc2ui)  
  if sudoo==True:
      ssh_command = [f"ssh",  f"{host_name}@{host}",f"sudo -S bash {bash_write_dir_name}/{bash_file_name}"]# put the script you want to run here
  else:
      ssh_command = [f"ssh",  f"{host_name}@{host}",f"bash {bash_write_dir_name}/{bash_file_name}"]# put the script you want to run here

      

  try:
      subprocess.run(ssh_command, check=True,shell=True)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into {host}: {e}")  
  return 

 def start_up_all_websites_on_server_on_internet(self):
  '''setup ngnix server to be able to work and run mutliple different websites
  set up gunicorn to also run mutliple websites
  set up django and other websites in pipeline to run different websites
  mdoficaitons to be made to server to get ngnix to run mutliple websites and gunicorn to run mutliple websites'''
  # create folder for all websites?
  import os
  start_all_websites_on_internet_bash="""#!/bin/bash
pwd
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
sudo killall gunicorn
python manage.py collectstatic
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
python manage.py collectstatic
python manage.py migrate
"""
  # end current websites being run and create a start website being run
  self.create_and_run_bash_file(start_all_websites_on_internet_bash)        
 
  
  return 
 def start_up_all_websites_on_server_on_local_network(self):
  '''  THIS IS THE ONE WE WILL DO NOW
  need to write these bash scripts or we are fucked
  FOLLOW INSTRUCTIONS IN funciton : setup_website_and_api_to_run_llamma
  and setup_computer_to_run_fast_api
  and electroncics book

  
  '''
  import os
  start_all_websites_on_internet_bash="""#!/bin/bash
pwd
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
sudo killall gunicorn
python manage.py collectstatic
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
python manage.py collectstatic
python manage.py migrate
"""
  # end current websites being run and create a start website being run
 
  self.create_and_run_bash_file(start_all_websites_on_internet_bash)        
 

  return 
 def update_all_website_code_and_restart_websites(self,sub_dir_list,copy_sub_dirs=True,copy_whole_website=False):
  '''
  FOLLOW INSTRUCTIONS IN funciton : setup_website_and_api_to_run_llamma
  source env/bin/activate
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  modify gunicorn devleopment config file
  and /etc/nginx/sites-available/ file adding gunicorn to this file
  http://192.168.2.200:8000 
  DONT COPY OVER ALL FOLDERS IN WEBSITe
  ONLY COPY OVER SPEICFIC ONES, otherwise have issues 
  like copy over html or apps but not whole infastrcture
  create venv and install uvicorn etc locally using a creation funciton locally
  so everything runs
  create bash script to do this
  # this is how you start guicorn
  gunicorn -c config/gunicorn/dev.py 
  pwd
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl reload nginx
sudo systemctl status nginx

  '''
  import os
  host="192.168.2.209"
  host_name="jross77"
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
  print(website_dirs)
  mkdirr=False
  if mkdirr==True:
      dir_to_make="/home/jross77/all_websites/"
      self.mkdir_dir_bash(dir_to_make,host,host_name)
  #scp_command = [f"scp","-r",rf"{local_folder_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here 
  # need to make this all one bash script to avoid typing the password a 100 times
  #sudo systemctl start gunicorn-dev 
  #gunicorn myproject.wsgi
  # to keep running when you close the terminal
  #gunicorn -c config/gunicorn/dev.py myapp:app --bind 0.0.0.0:8000 &
  #gunicorn -c config/gunicorn/dev.py myapp:app
  start_all_websites_on_internet_bash=f"""#!/bin/bash
pwd
sudo killall gunicorn
ps ax|grep gunicorn"""
  for i, website_name in enumerate(website_dirs):
      start_all_websites_on_internet_bash+=f"""cd /home/jross77/all_websites/{website_name}
source env/bin/activate
cd freelegalproject
sudo mkdir -pv /var/{log,run}/gunicorn/
sudo chown -cR jross77:jross77 /var/{log,run}/gunicorn/
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log

"""  
      if i>2:
          break
      print(start_all_websites_on_internet_bash)    
#tail -f /var/log/gunicorn/dev.log #cant add this in yet
      if copy_sub_dirs==True:
          # copy sub dirs from local sub dirs
          for i, intital_dirr_with_spaces in enumerate(sub_dir_list):
              sub_dir_win=r""
              sub_dir_lin=""
              dirr_list=intital_dirr_with_spaces.split(" ")
              for dirrr in dirr_list:
                  sub_dir_lin+=f"/{dirrr}"
                  sub_dir_win+=rf"\{dirrr}"
              local_folder_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\{website_name}\{sub_dir_win}"
              remote_dir_path=rf"/home/jross77/all_websites/{website_name}/{sub_dir_lin}"
              scp_command = [f"scp","-r",rf"{local_folder_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here 
              self.subprocess_run_script_remotely(scp_command)
  self.create_and_run_bash_file(start_all_websites_on_internet_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True) 
   
 
    
 def start_up_all_apis(self):
  ''' '''
  return 
 def update_and_start_up_all_apis(self):
  ''' '''
  import os
  start_all_websites_on_internet_bash="""#!/bin/bash
pwd
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
sudo killall gunicorn
python manage.py collectstatic
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
python manage.py collectstatic
python manage.py migrate
"""
  host="192.168.2.209"
  host_name="jross77"
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis")
  print(website_dirs)
  mkdirr=True
  if mkdirr==True:
      dir_to_make="/home/jross77/all_apis/"
      self.mkdir_dir_bash(dir_to_make,host,host_name)
      print('hi')
  for website_dir in website_dirs:
      website_dir_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\{website_dir}"
      scp_command = [f"scp","-r",rf"{website_dir_path}",f"jross77@{host}:/home/jross77/all_apis/"]# put the script you want to run here 
      self.subprocess_run_script_remotely(scp_command)
  if internet==True:
      self.create_and_run_bash_file(start_all_websites_on_internet_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77") 


  
  return 


  
  
 def update_and_start_single_api(self):
  ''' '''

  return 
 def startup_single_api(self):
  ''' '''

  
  return 
 def setup_website_on_remote_server(self):
  '''once you get og website 5 to work just copy this into all the other 
  folders and change the port being used
  then just do setup
  follow the guide to fix everything
  create process to update computers meaning
  FIRST THING TOMORROW:
  COPY website5 to psp website 
  
  going to set up all websites at once with this? 
  FOLLOW INSTRUCTIONS IN funciton : setup_website_and_api_to_run_llamma
  source env/bin/activate
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  modify gunicorn devleopment config file
  and /etc/nginx/sites-available/ file adding gunicorn to this file
  http://192.168.2.200:8000 
  DONT COPY OVER ALL FOLDERS IN WEBSITe
  ONLY COPY OVER SPEICFIC ONES, otherwise have issues 
  like copy over html or apps but not whole infastrcture
  refer to setting up fastapi word doc
  create venv and install uvicorn etc locally using a creation funciton locally
  so everything runs
  create bash script to do this
  copy the working website in website 5 folder
  into all the other folders and use that and just change
  the nginx configuraiton and uvicvorn info since it already works'''
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
  print(website_dirs)
  mkdirr=True
  if mkdirr==True:
      dir_to_make="/home/jross77/all_websites/"
      self.mkdir_dir_bash(dir_to_make,host,host_name)
      print('hi')
  
  website_dir_name="psp_website"
  start_all_websites_on_internet_bash=f"""#!/bin/bash
pwd
cd /home/jross77/all_websites/{website_dir_name}
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
sudo killall gunicorn
python manage.py collectstatic
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
gunicorn -c config/gunicorn/dev.py
tail -f /var/log/gunicorn/dev.log
sudo systemctl start nginx	
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
python manage.py collectstatic
python manage.py migrate
"""
  self.create_and_run_bash_file(start_all_websites_on_internet_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77") 
  return 
 def copy_website_or_api_remote_server_to_local_server(self):
  '''NEED TO FOGURE THIS OUT so can make edits easily on local
  maybe way we copy is by nano and then copy whole file 
  using ctrl a and copy into local file
  
  use memroy stick and then transfer to main computer using 
  that if cant ssh into laptop need ot figure this out
  just work out of raise me up folder which has a copy of the working website 5 folder'''
  start_all_websites_on_internet_bash=f"""#!/bin/bash
"""
  self.create_and_run_bash_file(start_all_websites_on_internet_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77") 
  return 
 def copy_remote_server_file_to_local_computer(self):
  ''' going to ctrl a nano and then creat eit locally and pwd the path 
  and this is how we will modify local files?
  makes it easier to duplicate these
  copy key files into some folder w ecreate
  \key_files_remote_serever
  and then work out of this to edit these files
  and save their og path on remote server here'''
  return  
 

 
 def record_mods_to_files_local_to_remote_server_for_django_websites(self,final_local_file_path,final_remote_file_dir,sudoo=False,mkdirr=False):
  '''  this is for files in strange places like the nginx file or other files in strange directories

  sned the files we edit in  key_files_remote_serever back to the remote server in their edited form
  this way we keep track of changes and can mutliply the changes quite easily into the different websites
  just cp to the other folder
  # send edits to all websites where possible to save on time'''
  import os
  host="192.168.2.209"
  host_name="jross77"
  # need to scp and then bash sudo it
  # so will need ot change this
  dirs_and_file_of_local_pile_path_list=final_local_file_path.split("\\")
  # get file_name and remote remote server path
  remote_server_copy_file_path="/home/jross77/key_files_remote_serever"+f"/{dirs_and_file_of_local_pile_path_list[-1]}"# get the file name
  #print(remote_server_copy_file_path)
  records_mods_bash=f"""#!/bin/bash
pwd
sudo cp {remote_server_copy_file_path} {final_remote_file_dir}
  """
  if sudoo==True:
      remote_server_copy_dir=r"/home/jross77/key_files_remote_serever"
      if mkdirr==True:
          self.mkdir_dir_bash(remote_server_copy_dir,host,host_name)
      # copy the file over
      scp_command = [f"scp",rf"{final_local_file_path}",f"jross77@{host}:{remote_server_copy_dir}"]# put the script you want to run here   
      # bash the file into the folder
      self.subprocess_run_script_remotely(scp_command)
      self.create_and_run_bash_file(records_mods_bash,mkdirr=True,sudoo=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77") 
      return
      # put the script you want to run here 
  else:
      scp_command = [f"scp",rf"{final_local_file_path}",f"jross77@{host}:{final_remote_file_dir}"]# put the script you want to run here   
  self.subprocess_run_script_remotely(scp_command)
  
      
  return 
 
 def change_gunicorn_port_binding_on_all_websites(self):
  '''find the gunicorn port file
  modify it in each different website uniquely
  locally changing the port in eahc file using a bahs script
  need to figure out the sub contents here
  need to find a generic way to do this
  modify each website indivdual over all websites?
  for now do this if need to do it again write another function
  #intital_dir="raise_you_up"
  #modify file locally
  # use copy script
  #uvicorn
  #make mod in raise you up
  # make this mod in all other websites but in a different way
  # how to best do this and make it repeatable?
  # so cannot copy over speicifc subfolders after this
  # because will delete the changes
  # so how do i best do this
  # make change on local website
  # then modify this change?
  # maybe sub dir script will only be to modify indivudal files instead of whole dirs
  # may need to be more precise, and modify the past files
  # so just use funciton?
  ###
  # robust method to edit scripts
  # devleop it here
  # python starts at 0 in file lines
  # normal files start at 1 '''
  # make modificaitons to gunicorn file in all website dirs
  website_dir_list=[]
  import os
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
  starting_port=8000
  for websitee in website_dirs:
      gunicorn_file_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites"+r"\\"+websitee+r"\freelegalproject\config\gunicorn\dev.py"
      with open(gunicorn_file_path, "r") as f:
          gunicorn_file_to_mod_str=f.read()
      gunicorn_file_to_mod_str_list=gunicorn_file_to_mod_str.splitlines()
      line_to_sub=f'bind = "0.0.0.0:{starting_port}"'
      starting_port+=1
      gunicorn_file_to_mod_str_list[10-1]=line_to_sub# need to minus 1 from line number we want to sub it out
      #rewrite the file witht eh mod
      moded_file_str=""
      for i, linee in enumerate(gunicorn_file_to_mod_str_list):
          if i ==0:
              moded_file_str=linee
          else:
              moded_file_str+="\n"+f"{linee}"  
      with open(gunicorn_file_path, "w") as f:
          gunicorn_file_to_mod_str=f.write(moded_file_str)

      
      #so always add one to line number when subbign out lines in a file
      
      
  #modify speicfic file in all website dirs
  
  # step 2 copy these changes to the other computer make modificaitons
  sub_dir1=r"freelegalproject project" # NEED TO HAVE SPACES HERE
  sub_dir2=r"freelegalproject fiann" # NEED TO HAVE SPACES HERE
  sub_dir3=r"freelegalproject static" # NEED TO HAVE SPACES HERE
  sub_dir_list=[sub_dir1,sub_dir2,sub_dir3]
  self.update_all_website_code_and_restart_websites(sub_dir_list)
     
  
  
 def update_all_websites_from_single_website(self,website_name,sub_dir_list,copy_sub_dirs=True,copy_whole_website=False):
  '''  DOO NOTT DO NOT USE THIS just make modificaiton locally and copy over
  KEEP IT SIMPLE STUPID
  can use script to make modifcaiton locally
  this will be for to make changes to specific files like uvicorn to save on time on all websites from a single website
  since we will copy the strcture of website5 which is in raise you up to all websites
  specific files might be the nginx file on the remote server
  which we will want to edit locally and then copy changes to the local server'''
  import os
  host="192.168.2.209"
  host_name="jross77"
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
  print(website_dirs)
  mkdirr=False
  if mkdirr==True:
      dir_to_make="/home/jross77/all_websites/"
      self.mkdir_dir_bash(dir_to_make,host,host_name)
  #make this take an intital website and then copy a specifc file or folder to all the other websites
  # use os to checker whether is a file or a folder and make a decision 
  for websitee in website_dirs:
      if copy_sub_dirs==True:
          for i, intital_dirr_with_spaces in enumerate(sub_dir_list):
              sub_dir_win=r""
              sub_dir_lin=""
              dirr_list=intital_dirr_with_spaces.split(" ")
              for dirrr in dirr_list:
                  sub_dir_lin+=f"/{dirrr}"
                  sub_dir_win+=rf"\{dirrr}"
              local_folder_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\{website_name}\{sub_dir_win}"
              remote_dir_path=rf"/home/jross77/all_websites/{websitee}/{sub_dir_lin}"
              file_test=os.path.isfile(local_folder_path)
              dir_test=os.path.isdir(local_folder_path)
              if file_test==True:
                  scp_command = [f"scp",rf"{local_folder_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here 
              if dir_test ==True:
                  scp_command = [f"scp","-r",rf"{local_folder_path}",f"jross77@{host}:{remote_dir_path}"]# put the script you want to run here      
              self.subprocess_run_script_remotely(scp_command)
  return 
  
 def duplicate_contents_of_one_folder_in_other_folders_bash(self,intital_dir_linux,dir_to_copy_to_list):
  ''' DO NOT USE THESE this is the wrong way to do this just edit on local and then copy over using 
  update code and start server always
  '''
  import os
  duplicate_dirs_bash=f"""#!/bin/bash"""
  for dirr in dir_to_copy_to_list:
      website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
      print(website_dirs)
      duplicate_dirs_bash+="\n"+fr"cp -a {intital_dir_linux}/. {dirr}"
  print(duplicate_dirs_bash)
  self.create_and_run_bash_file(duplicate_dirs_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True) 
  return 

 def duplicate_sub_contents_of_one_folder_in_other_folders_bash(self,intital_dir_linux,dir_to_copy_to_list,sub_dir):
  ''' DO NOT USE THESE this is the wrong way to do this just edit on local and then copy over using 
  update code and start server
  '''
  import os
  duplicate_dirs_bash=f"""#!/bin/bash"""
  for dirr in dir_to_copy_to_list:
      website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
      print(website_dirs)
      duplicate_dirs_bash="\n"fr"cp -a {intital_dir_linux}/. {dirr}"
  print(duplicate_dirs_bash)
  self.create_and_run_bash_file(duplicate_dirs_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True) 

 def change_setting_django_to_run_on_local_network(self):
  ''' '''

  print('hi')
  print('hi')
  print('hi')
  return 
  return 
 def change_setting_django_to_run_on_internet(self):
  ''' '''

  print('hi')
  print('hi')
  print('hi')
  return 
 def check_latest_port_number_and_assign_website_next_port_number(self):
     """ this will check which port number is used and choose next one on website server"""
 def set_up_multi_sites_nginx_gunicorn_systemd(self,website_name,port_domain,removee=False):
  ''' TO CORRECT A FAILED SERVICE error type:systemctl reset-failed servicename.service
  sudo chown -R jross77:jross77 migrations/
  need to change permisisons of migraiton folder at one point to jross77
  
  follow the insturcitons set out inv arious articles here is key
  https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu
  https://docs.gunicorn.org/en/latest/deploy.html
  https://caterinadmitrieva.medium.com/serving-multiple-django-apps-on-second-level-domains-with-gunicorn-and-nginx-a4a14804174c
   sudo nano /etc/systemd/system/gunicorn.service
   going to start from scratch using these commands
   then copy it over on usb to repeat the commands
   # set up all the website properly like this with there own venv
   # then can modify specific sub dirs in them
   # use test file lines script to edit files
   https://ubuntu.com/core/docs/networkmanager/configure-wifi-connections
   get website on server running
   copy over the all_websites folder when all websites are created\
  then start using update website code function
  update website code and restart website
  #once copied dirs to local computer
  sudo systemctl restart nginx
  sudo systemctl restart gunicorn
  #sub_dir1=r"raise_you_up" # NEED TO HAVE SPACES HERE
  #website="raise_you_up"
  #sub_dir_list=[sub_dir1,]
  #self.update_website_code_and_restart_website(website_name,sub_dir_list)
  Error: open() "/etc/nginx/sites-enabled/{website_name}"
  to fix this error remove {website_name} from sites enabled dir
  to fix error service start limit hit reboot computer
  or systemctl reset-failed servicename.service
  https://stackoverflow.com/questions/59752840/docker-socket-failed-with-result-service-start-limit-hit-after-protecting-doc
  if internal server error try running manage.py and figure out whaty is wrong with django
  sudo systemctl restart gunicorn
  # need to create unique user for website and assign user for that website
  FOR WEBSITE SECURITY
  ''' 
  # create file sudo nano /etc/systemd/system/gunicorn.service
  #https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu
  # to stop nginx use this sudo systemctl stop nginx
  # probably not using this
  # need to create unique user for website and assign user for those dirs on the website
  # or just make everything root except project files idk
  #need to make it so that
  #sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
  # need to manually create the database it looks like
  # need to send psql commandf sinto the other computer
  # need to be root to do this it seems
  #need to use pyautoghui to enter tthese commands?
  # will use pyautogui for this i think
  #psql -U postgres
  # need to fix settings file again now
  # need to fix the search_c value now maybe add it back in
  # the other file to the program but erase most of the data
  set_up_data_base=f"""#!/bin/bash
YOU MUST CREATE DATABASE TO GET THIS TO WORK named after website
sudo apt update
psql -h <hostname> -p <port> -U <username> -d <database>
$ python manage.py makemigrations --name changed_my_model your_app_label

sudo --login --user=postgres
psql
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
to exit stuff use \q
check avialbe databases postgres=# \l
exit with \q
 psql -U jross77 -d canlawaccessible
CREATE USER jross77 WITH PASSWORD 'MeganisGreat';
CREATE USER jross777 WITH PASSWORD 'MeganisGreat';
CREATE DATABASE canlawaccessible;
GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross777;
GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross77;
ALTER ROLE jross77 SET client_encoding TO 'utf8';
ALTER ROLE jross77 SET default_transaction_isolation TO 'read committed';
ALTER ROLE jross77 SET timezone TO 'UTC';

### THESE ARE THE KEY COMMANDS
sudo -u postgres psql
CREATE DATABASE business_advice;
GRANT ALL PRIVILEGES ON DATABASE business_advice TO jross777;
GRANT ALL PRIVILEGES ON DATABASE business_advice TO jross77;
\q
# run this once the program has run database is made
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
cat .DJANGO_SECRET_KEY
python manage.py makemigrations {website_name}
python manage.py migrate
CREATE USER jross777 WITH PASSWORD 'MeganisGreat';
ALTER ROLE jross777 SET client_encoding TO 'utf8';
ALTER ROLE jross777 SET default_transaction_isolation TO 'read committed';
ALTER ROLE jross777 SET timezone TO 'UTC';
\q"""
  #import subprocess
  #subporcess.run()
  self.create_remote_database_pyautogui(website_name)
  port_domain2=self.check_latest_port_number_and_assign_website_next_port_number()
  #self.create_and_run_bash_file(set_up_data_base,mkdirr=False, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True)  
  #input(r"created database!")

  # need to sudo rm- to remove them faster
  #ls -l /home/jross77/all_websites/raise_you_up/static/
  #sudo chown -R www-data:www-data /home/jross77/all_websites/raise_you_up/static/
  bash_install_web_1=f"""#!/bin/bash
cd /home/jross77/all_websites/
mkdir {website_name}
cd {website_name}
python3 -m venv env
source env/bin/activate
pip install django gunicorn psycopg2-binary
pip install requests
django-admin startproject {website_name} /home/jross77/all_websites/{website_name}
python manage.py makemigrations
python manage.py migrate"""
  if removee==True:
      self.sudo_remove_bash(website_name)
  self.create_and_run_bash_file(bash_install_web_1,mkdirr=False, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=False)  
  # copy over the settings file need to figure this out
  # may need to change permissions for these dirs
  # need to do this in a paritcualr way it seems
  # do the sudo copy i guess
  # need to log in as root to do this
  host="192.168.2.209"
  print("scp settings")
  # edit settings folder
  #removign riase you up in urls and as wsgi app
  # and every place it might screw things up
  ### add to settings change static to this one
  # will need to change the line numbers here
  template=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\settings.py" 
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\settings.py"  
  # need to ensure spacing is correct here
  # edit database name
  modify_line_dic={55:f"ROOT_URLCONF = '{website_name}.urls'",
                   73:f'WSGI_APPLICATION = "{website_name}.wsgi.application"',                 
                   43:f'    "{website_name}"]  ',
                   81:f"        'NAME': '{website_name}',",}
                  # will need to test tis last one}# add to installed app website name
  self.modify_file_locally(template,final_local_file_path,modify_line_dic)
  remote_file_path=rf"/home/jross77/all_websites/{website_name}/{website_name}/"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=False)
  #settings_file_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\raise_you_up\raise_you_up\settings.py"
  #remote_file_path=rf"/home/jross77/all_websites/{website_name}/{website_name}/settings.py"
  #self.record_mods_to_files_local_to_remote_server_for_django_websites(settings_file_path,remote_file_path,sudoo=True)
  
  # will use update website code and restart website
  # can also just copy over specific dirs using -r next time
  #once copied dirs to local computer
  # to update tyhem faster
  #using raise_you_up_file
  # so modify file locally
  # then copy over this change?
  #r=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\raise_you_up"
  #sub_dir1=r"raise_you_up" # NEED TO HAVE SPACES HERE
  #website="raise_you_up"
  #sub_dir_list=[sub_dir1,]
  #self.update_website_code_and_restart_website(website_name,sub_dir_list)
  # need to modify settings file here changing accepted hosts to 
  
  
  #### create all  socket  service, and nginx file
  # use the test_file_lines script in building
  # keep the console
  #open and the file you want to use asa  template to find lines to sub
  ###gunicorn.service
  print("gunicorn.service")
  # use test file lines script to edit files in building business functions
  template=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\flip.service"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\{website_name}.service" 
  # need to ensure spacing is correct here
  from django.core.management.utils import get_random_secret_key  
  django_secret_key=get_random_secret_key()
  
  modify_line_dic={2:f'Requires={website_name}.socket',
                   6:f'Environment="SECRET_KEY={django_secret_key}"',

                   8:f'WorkingDirectory=/home/jross77/all_websites/{website_name}',
                   9:f'ExecStart=/home/jross77/all_websites/{website_name}/env/bin/gunicorn \\',# change the line relating to
                   12:f'          --bind unix:/run/{website_name}.sock \\',
                   13:f'          {website_name}.wsgi:application',
                   }           
  self.modify_file_locally(template,final_local_file_path,modify_line_dic)
  remote_file_path="/etc/systemd/system/"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=True)

  ###gunicorn.socket
  # use the test_file_lines script in building
  # keep the console
  #open and the file you want to use asa  template to find lines to sub
  print("gunicorn.socket")
  template=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\flip.socket"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\{website_name}.socket"
  modify_line_dic={3:f'ListenStream=/run/{website_name}.sock'}
  self.modify_file_locally(template,final_local_file_path,modify_line_dic)
  remote_file_path="/etc/systemd/system/"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=True)
  
  
  ###website nginx file
  # use the test_file_lines script in building
  # keep the console
  #open and the file you want to use asa  template to find lines to sub
  ###/etc/nginx/sites-available/raise_you_up
  print("nginx")
  template=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\flip"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\{website_name}"
  modify_line_dic={6:f'        root /home/jross77/all_websites/{website_name}/;',
                   12:f'        proxy_pass http://unix:/run/{website_name}.sock;',
                   1:f'    listen {port_domain};',}
  self.modify_file_locally(template,final_local_file_path,modify_line_dic)
  remote_file_path="/etc/nginx/sites-available/"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=True)
  #need to figure out nginx research how to strcture this file to get it to work for different use cases
  bash_installs_2=fr"""#!/bin/bash
cd /home/jross77/all_websites/{website_name}
source env/bin/activate
sudo ufw allow 8000
deactivate
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo journalctl -u {website_name}.socket
sudo systemctl start {website_name}.socket
sudo systemctl enable {website_name}.socket
sudo systemctl status {website_name}.socket
sudo systemctl start {website_name}.service
sudo systemctl enable {website_name}.service
sudo systemctl status {website_name}.service
sudo systemctl status {website_name}
file /run/{website_name}.sock
systemctl reset-failed {website_name}.service
sudo systemctl restart gunicorn
sudo ln -sf /etc/nginx/sites-available/{website_name} /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
"""
#sudo ln -sf /etc/nginx/sites-available/agriculture /etc/nginx/sites-enabled
  self.create_and_run_bash_file(bash_installs_2,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True)
  self.add_tailwind_template_to_set_up_django_website(website_name,installl_tailwind=False)
  print('TO CORRECT A FAILED SERVICE error type:systemctl reset-failed servicename.service')
  input("stopping to start bash")
  www_name=r"example.com"
  self.make_final_production_changes_to_website_files(website_name,www_name)
#curl --unix-socket /run/{website_name}.sock localhost
#systemctl reset-failed {website_name}.service # use bank.service
# killall gunicorn # to fix some errors
#file /run/{website_name}.sock
#curl --unix-socket /run/{website_name}.sock localhost # this tests the socket
#sudo systemctl status {website_name}
#sudo journalctl -u gunicorn
#sudo systemctl daemon-reload
#sudo systemctl status {website_name}
#sudo journalctl -u {website_name}.socket
#python manage.py runserver 0.0.0.0:8000
#gunicorn --bind 0.0.0.0:8000 raise_you_up.wsgi
#sudo journalctl -u {website_name}.socket
#sudo systemctl status {website_name}
#curl --unix-socket /run/{website_name}.sock localhost # this tests the socket
#sudo systemctl status {website_name}
#sudo journalctl -u gunicorn
# configure nginx to pass traffic to gunicorn, link sites enabled, use sf here to overwrite a bad symlink instead of s
# create{website_name} in  /etc/nginx/sites-available/, and other sites, next line is important
# change listen number from 80 in this file to listen on different ports for the different websites
# make sure to include semi colon after server name or ip
#sudo ufw delete allow 8000
#sudo ufw allow 'Nginx Full'
  #sudo service nginx configtest /etc/nginx/sites-available/{website_name}
  # edit the settings file in
  # add 192.168.2.209 to allowed hosts in settings
  #C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\raise_you_up\freelegalproject\project\settings.py
  #locally
  # The simplest case: just add the domain name(s) and IP addresses of your Django server
  # ALLOWED_HOSTS = [ 'example.com', '203.0.113.5']
  # To respond to 'example.com' and any subdomains, start the domain with a dot
  # ALLOWED_HOSTS = ['.example.com', '203.0.113.5']
  #ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . ., 'localhost']
  # edit postgres
  
  # at root of project run:
  #~/myprojectdir/manage.py makemigrations
  #~/myprojectdir/manage.py migrate
  #~/myprojectdir/manage.py createsuperuser
  
  return 
 def business_idea_folder_website_creator_and_business_creator_using_psp_pipeline(self):
  '''generate every possible business based on stock market successful businesses create a website
  or small business
  and keep monitoring their business and build on top of what they are doing and stay two steps ahead
  generate all information related stuff you can for the business like business plan taxes 
  proposectus emplopyment contracts and any other things related to the business
  then automcialy upload this website to the internet
  build on top of existing businesses and keep updated on these businesses and keep taing thier stuff and reverse engineering'''
  all_possible_businesses=self.generate_all_category_business_list()# these are business we will actually run
  set_up_website_list=["raise_you_up","jasper_legal_news","flip","bank", "canva_replica","construction"] 
  self.keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program()# assuming its legal
  starting_port=84
  for website_name in all_possible_businesses:
      if website_name in set_up_website_list:
          print(f" FOUND THIS WEBSITE {website_name}")
          continue
      else:
          print(f" Change THIS WEBSITE {website_name}")
          starting_port+=1
          input()
          self.set_up_multi_sites_nginx_gunicorn_systemd(website_name,starting_port,removee=True)
          self.add_tailwind_template_to_set_up_django_website(website_name,installl=False)
          self.build_phone_app_for_business(website_name)
          self.use_penetration_tesing_tools_on_server_to_test_security(website_name)
          psp_info=self.psp_pipeline(website_name)# import info from psp pipeline api from running website?
          self.create_all_other_business_content(website_name)
          self.keep_updated_on_business_in_category_and_take_all_ideas_add_to_business(website_name)
          self.reverse_engineer_business_work_and_add_ideas_and_work_to_program(website_name)
          self.build_on_top_of_existing_business_in_category_and_constantly_update_and_reverse_engineer_business_products_and_add_to_business()
          self.add_ideas_and_capital_from_other_fields_and_businesses_into_business_constantly_updating()

          
      
      
      # reverse egineer things they come up with and keep active feeds
      #on all business like this and search and update for all business like this categorize like new tech starts up
      # take their ideas anditnegrate it into the program
      
      # example of contnet is setup all social media
      # set up all marketng
      # set up all contracts and legal
      # set up all business processes
      # set up business plan
      #s set up propsectyus
      #generate enegineering solution and otyher solutions for product
      # set up all other things might be used by business like software
      # or tools and have businesses ready to go

  return 
 def sudo_remove_bash(self,website_name):
  ''' '''
  sudo_remove_bash=f"""#!/bin/bash
sudo rm -r /home/jross77/all_websites/{website_name}
sudo systemctl restart gunicorn

"""
  self.create_and_run_bash_file(sudo_remove_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True) 
  print(r"REMOVE DIR")
  return

  
  import os
  host="209"
  host_name="jross77"
  website_dirs=os.listdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites")
  print(website_dirs)
  set_up_website_list=["raise_you_up","jasper_legal_news","flip"]
  mkdirr=True
  if mkdirr==True:
      dir_to_make="/home/jross77/all_apis/"
      self.mkdir_dir_bash(dir_to_make,host,host_name)
      print('hi')
  for website_name in website_dirs:
      if website_name in set_up_website_list:
          print(f" FOUND THIS WEBSITE {website_name}")
          input()
          continue
      else:
          #run the remove bash command
          j=r"sudo rm -r {website_name}"
          # then run the commands to create the website
          input()
          business2.set_up_multi_sites_nginx_gunicorn_systemd(website_name)        
      website_dir_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\{website_dir}"
      scp_command = [f"scp","-r",rf"{website_dir_path}",f"jross77@{host}:/home/jross77/all_apis/"]# put the script you want to run here 
      self.subprocess_run_script_remotely(scp_command)


  return 
 def modify_file_locally(self,template,final_file_path,modify_line_dic,insert_file_line_dic={}):
  ''' need to test the insert file line dic'''
  with open(template,"r") as f1:
      file_str=f1.read()
  line_dic={}
  local_file_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\{website_name}"
  file_str_list=file_str.splitlines()
  for linee_number,linee_mod_value in modify_line_dic.items():
      file_str_list[linee_number]=linee_mod_value
  if insert_file_line_dic:
   for line_to_insert_below,linee_insert_value in insert_file_line_dic.items():          
     file_str_list[line_to_insert_below+1].insert(intital_line_to_append_below,linee_append_value)
  moded_file_str=""
  for i, lineee in enumerate(file_str_list):
      if i ==0:
          moded_file_str=lineee
      else:
          moded_file_str+="\n"+f"{lineee}"      
  with open(final_file_path,"w") as f2:
      f2.write(moded_file_str)
  return 
 def add_tailwind_template_to_set_up_django_website(self,website_name,installl_tailwind=False):
  ''' 
  #npx @tailwindcss/cli -i .\static\input.css -o .\static\output.css --watch
  #linux this seems to work
  npx @tailwindcss/cli -i .\static\input.css -o .\static\output.css --watch
  https://docs.djangoproject.com/en/5.1/howto/static-files/ 
  https://stackoverflow.com/questions/61456431/how-do-i-load-css-file-into-html-in-django 
  https://tailwindui.com/?ref=top
  https://tailwindflex.com/@bunny/simple-login-form
  https://tailwindui.com/components/marketing/sections/newsletter-sections
  https://tailwindui.com/components/marketing/sections/heroes
  https://docs.djangoproject.com/en/5.1/topics/db/queries/
  https://www.brennantymrak.com/articles/fetching-data-with-ajax-and-django
  https://stackoverflow.com/questions/11762629/pass-information-from-javascript-to-django-app-and-back
  https://how.dev/answers/how-to-add-an-eventlistener-to-multiple-elements-in-javascript
  # used this to test if database worked
  # d=problem_table(problem_question_or_task="d")
      # d.save()
      #https://stackoverflow.com/questions/44657829/css-file-blocked-mime-type-mismatch-x-content-type-options-nosniff
      #debug = False
      #https://stackoverflow.com/questions/72496666/the-cross-origin-opener-policy-header-has-been-ignored-django
      #SECURE_CROSS_ORIGIN_OPENER_POLICY = None THIS IS KEY TO ADD TO SETTINGS
      # may need to change this at one point
      With debug turned off Django won't handle static files for you any more - your production web server (Apache or something) should take care of that.
      SECURE_CONTENT_TYPE_NOSNIFF = False
      SECURE_CROSS_ORIGIN_OPENER_POLICY = None
      port 7777 for current agrticulture
      sudo killall gunicorn solved it when issues with 500 error probably caused by gunicorn
      WHEN RUN INTO A IMPORTANT ERRROR TRY kill all gunicorn
'''
  copy_in_necessary_files_to_dir=""
  tailwind_install_setup__bash="""#!/bin/bash
sudo apt install npm nodejs
npm install tailwindcss @tailwindcss/cli"""
  if installl_tailwind==True:
      self.create_and_run_bash_file(tailwind_install_setup__bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True)     
  self.add_customized_template_files_website_dir(website_name)
  
  # this should translate the tables wanted over
  start_tailwind_bash=f"""#!/bin/bash
cd /home/jross77/all_websites/{website_name}
npx @tailwindcss/cli -i ./static/input.css -o ./static/output.css 
cd /home/jross77/all_websites/{website_name}
source env/bin/activate
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
cat .DJANGO_SECRET_KEY
python manage.py makemigrations {website_name}
python manage.py migrate
python manage.py collectstatic

sudo killall gunicorn
sudo systemctl restart gunicorn
sudo systemctl restart nginx

"""
  self.create_and_run_bash_file(start_tailwind_bash,mkdirr=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True) 

  return 
 def build_phone_app_for_business(self):
  '''take current phone app as a template and use it to build another phone app '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def transfer_psp_remote_pc(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def use_penetration_tesing_tools_on_server_to_test_security(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def generate_all_category_business_list(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program(self):
  ''' funnel this into websites and automcailly update and improve them'''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_customized_template_files_website_dir(self,website_name,mkdir_key_files=True,mkdir_temp_web=True):
  '''
  https://taylor.town/5w
  create a template folder
  add the template to it that uses tailwind css
  edit the urls, views files in a specific way
  add tailwind files
  need to add all templates i want for the website
  and edit the views to include all views for this website
  and edit the urls to include all views for this website
  add the tailwind configs
  give urls generic names
  and views generic names 
  give templates generic names
  gonna do this remotely
  # edit this file and add content related to the website using ai  at one point
  figure out how to get tailwind set up locally on current raise you up
  and copy the steps i take there on here 
  https://codingnomads.com/serve-django-static-files-with-nginx
  need to add all templates i want for the website
  and edit the views to include all views for this website
  and edit the urls to include all views for this website
  add the tailwind configs
  model off of psp website design and files
  add these to other websites
  if possible take from existing business websites for ideas
  @import "tailwindcss"; # add to dir src and create input.css file and output.css file
  # we will rebuild algo and improve it so more important fast and use it
  # then hide it
  do this locally or do this remotely
  locally might be easier
  do this on remote server so never touch code?
  # try to get tailwind css to run on raise you up on remote server
  # then copy these configs to the local server
  # figure out the instructions you need to follow to get node to run and changes to different files
    # windows
    # just copy in all templates from psp website dir and dir itself
    # and copy as much content from current psp website as you can to save on work
    #self.mkdir_dir_bash(remote_template_dir,host,host_name,sudoo=True)
    #host="192.168.2.209"
    #host_name="jross77"
    # add the tailwnd css files
    cp -r static/ /home/jross77/all_websites/raise_you_up
    running the tialwind listner at same time at tailwind to work on manage.py 
    need to get it to run on nginx now
    https://news.ycombinator.com/
    
    #python manage.py runserver 0.0.0.0:8000
    # this currently makes tailwind work for raise you up
    # need to get this to work for 

    how do i get tialwind to recognize guniocrn by using nginx
    3. Configure Nginx to Serve Static Files (Production)
    configure pertmissions
    make sure there are permissions all the way up to the templates file
    ls -l /home/jross77/all_websites/raise_you_up/static/
    #sudo chown -R www-data:www-data /home/jross77/all_websites/raise_you_up/static/
    sudo chown -R jross77:jross77 /home/jross77/all_websites/raise_you_up/static
    sudo chown -R jross77:jross77 /home/jross77/all_websites/raise_you_up/static/

    sudo chown -R www-data:www-data base.html
ps -eo user,comm | grep nginx
sudo chmod -R 755 /home/jross77/all_websites/raise_you_up/static/
python manage.py collectstatic
sudo chmod 755 /home/jross77/all_websites/raise_you_up
sudo chmod 755 /home/jross77/all_websites/raise_you_up/static  
sudo systemctl restart nginx
sudo systemctl restart gunicorn
3. Ensure No Conflicting Permissions in nginx.conf
move all static files to a different path that nginx can more easily access
and change the nginx file related to the specific site static location 
/var/www/freelegalproject.org/static
# change this to site name
turning debugging to false helped fix this
now 
gunicorn --bind 0.0.0.0:8000 raise_you_up.wsgi
works and produces the css
THIS IS SOLUTION
https://www.uptimia.com/questions/how-to-fix-nginx-403-forbidden-error-when-serving-static-files
need to change the user line in the nginx.conf file to jross77 from www-data
user jross77;
and then set permissions to jross77 of static file in django project
meed to set a different user with less permissions as the nginx user later in the nginx file to improve security
# need to keep the css tailwind file open to update the css
while working
to reduce chance of the site getting hacked
/etc/nginx/sites-available/raise_you_up
6. Try with a Simpler Static Path (Temporary Test)
npx @tailwindcss/cli -i ./static/input.css -o ./static/output.css --watch
this must be executed in root of project
https://medium.com/django-unleashed/securing-django-applications-best-practices-for-managing-secret-keys-and-environment-variables-f10f5a53490b
use django enviorn instead here its better follow the guide above
SECRET_KEY = 'django-insecure-3y)74e+@6aas4er6(2$ekc1)ni5-n%w&*43q_6r+4lt-*_*11j'
https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
need to do everything on checklist before deplying site as well
python3 manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
g7)37xqz2d4mh7r1a3vo7a!5b7s_bk@8)7xn+(gdo2uq)nsfil
    create .env file and add secret key and debug
    pip install python-dotenv
    https://django-environ.readthedocs.io/en/latest/quickstart.html
    python -m pip install django-environ
    https://serverfault.com/questions/413397/how-to-set-environment-variable-in-systemd-service
    How to set environment variable in systemd service?
    python manage.py check --deploy
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
cat .DJANGO_SECRET_KEY
need debug to be ture to fix certain errros

'''
  project_dir=rf"/home/jross77/all_websites/{website_name}/{website_name}/"
  temp_key_file_website_dir=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites"
  
  import os
  print("IMPORTANT: to edit these files use this funciton in building test_file_lines_1 to create modify_line_dic")
  # edit templates os they are relevent for website
  remote_server_copy_dir=r"/home/jross77/key_files_remote_serever"
  host="192.168.2.209"
  host_name="jross77"
  # need to change this
  temp_website_dir=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}" 
  isExist = os.path.exists(temp_website_dir)
  if isExist==False:      
      os.mkdir(temp_website_dir)
      #print('hi')
      #print(isExist)
  temp_website_template_dir=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\templates"
  isExist = os.path.exists(temp_website_template_dir)
  if isExist==False:
      os.mkdir(temp_website_template_dir)
      print(isExist)
  ### view and urls
  ### views write to new file
  view_template_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\views.py"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\views.py"
  if website_name =="x":
      insert_file_line_dic={}
      modify_line_dic={}
  else:
      insert_file_line_dic={}
      modify_line_dic={}
  self.modify_file_locally(view_template_path,final_local_file_path,modify_line_dic,insert_file_line_dic=insert_file_line_dic)
  ### urls write to new file
  urls_template_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\urls.py"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\urls.py"
  re_pattern_to_find=r"auto_coding_psp"
  re_pattern_to_have=fr"{website_name}"
  if website_name =="x":
      self.re_sub_and_create_new_file(re_pattern_to_find,re_pattern_to_have,urls_template_path,final_local_file_path)      
  else:
      self.re_sub_and_create_new_file(re_pattern_to_find,re_pattern_to_have,urls_template_path,final_local_file_path)
      #insert_file_line_dic={}
      #modify_line_dic={32:f"import {website_name}.views"}
  # need to remove all auto_coding and just replace with other stuff
  #self.modify_file_locally(urls_template_path,final_local_file_path,modify_line_dic,insert_file_line_dic=insert_file_line_dic)  
  # gotta figure out how i wanna edit the templates
  # and edit views and urls
  starting_template_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\templates"
  template_file_list=os.listdir(starting_template_folder)
  for template_file_name in template_file_list:
      final_template_file_path=temp_website_template_dir+ r"\\"+template_file_name
      template=starting_template_folder +r"\\"+template_file_name
      if template_file_name=="website_name.html":
          insert_file_line_dic={}
          modify_line_dic={}
      else:
          # find a business in the category and copy prducts they might sell
          # fill in website name  question answered, rpdouct 1 product 2  with reelvent info for each business
          # fill in template as well
          insert_file_line_dic={}
          modify_line_dic={}
      final_project_template_folder=temp_website_dir+r"\\"+r"templates"   
      self.modify_file_locally(template,final_template_file_path,modify_line_dic,insert_file_line_dic=insert_file_line_dic)
      # then copy the template to new local templates folder?  
      # modify the view and url to add the unique template to the website
      # need to figure out views and urls now
      # need to modify views and urls
      # to work with new task bar names
      #just going to modify these manaully
      # then make htem work on the first one and change as necessary   
      ###view
      view_template_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\views.py"
      final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\views.py"
      if website_name =="x":
          modify_line_dic={}
          insert_file_line_dic={}        
      else:
          insert_file_line_dic={}
          modify_line_dic={}
      self.modify_file_locally(view_template_path,final_local_file_path,modify_line_dic,insert_file_line_dic=insert_file_line_dic)
      ### urls
      urls_template_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\urls.py"
      final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\urls.py"
      if website_name =="x":
          modify_line_dic={}
          insert_file_line_dic={}
      else:
          modify_line_dic={}
          insert_file_line_dic={}
      self.modify_file_locally(urls_template_path,final_local_file_path,modify_line_dic,insert_file_line_dic=insert_file_line_dic) 
  # add template with edited templates files for website to inside app  folder
  copy_template_dir=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\templates"
  scp_command = [f"scp","-r",rf"{copy_template_dir}",f"jross77@{host}:{project_dir}"]# put the script you want to run here   
  self.subprocess_run_script_remotely(scp_command)
  #copy over edited views  and urls inside app linking to created template files
  # gotta create the sub website dir
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\views.py"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,project_dir,sudoo=False)
  ### copy over search functons
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\search_functions.py"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,project_dir,sudoo=False)
  ### copy to other computer urls
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\temp_websites\{website_name}\urls.py"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,project_dir,sudoo=False)
  ### copy over modles file
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\models.py"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,project_dir,sudoo=False)
  # copy static folder into root of proeject
  final_local_static_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\static"
  root_project_dir=f"/home/jross77/all_websites/{website_name}/"
  scp_command = [f"scp","-r",rf"{final_local_static_path}",f"jross77@{host}:{root_project_dir}"]# put the script you want to run here   
  self.subprocess_run_script_remotely(scp_command)
  # copy over relevent tailwind files directly into app dir liek package-lock json
  intital_local_file_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\other_tailwind_files"
  self.copy_files_only_into_remote_dir(intital_local_file_dir,project_dir)
  change_permissions_bash=rf"""#!/bin/bash
sudo chown -R jross77:jross77 /home/jross77/all_websites/{website_name}/static/
sudo killall gunicorn
sudo systemctl restart gunicorn
"""
  self.create_and_run_bash_file(change_permissions_bash,mkdirr=False, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77",sudoo=True)

  return 
 def copy_files_only_into_remote_dir(self,final_local_file_dir,final_remote_file_dir,sudoo=False,mkdirr=False):
     """ will need to test the star here"""
     host="192.168.2.209"
     host_name="jross77"
     remote_server_copy_dir=r"/home/jross77/key_files_remote_serever"

     dir_contents_wanted=final_local_file_dir.split("\\")[-1]
     remote_dir_contents_to_copy= remote_server_copy_dir+"/"+f"{dir_contents_wanted}/"
     print(remote_dir_contents_to_copy)
     records_mods_bash_sudo=f"""#!/bin/bash
pwd
sudo cp -r {remote_dir_contents_to_copy}* {final_remote_file_dir}
     """
     records_mods_bash=f"""#!/bin/bash
pwd
cp -r {remote_dir_contents_to_copy}* {final_remote_file_dir}
     """
     if mkdirr==True:
         self.mkdir_dir_bash(remote_server_copy_dir,host,host_name)
     if sudoo==True:        
         scp_command = [f"scp",'-r',rf"{final_local_file_dir}",f"jross77@{host}:{remote_server_copy_dir}"]# put the script you want to run here   
         self.subprocess_run_script_remotely(scp_command)
         self.create_and_run_bash_file(records_mods_bash,mkdirr=True,sudoo=True, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77") 
     else:
         scp_command = [f"scp", '-r', rf"{final_local_file_dir}",f"jross77@{host}:{remote_server_copy_dir}"]# put the script you want to run here   
         self.subprocess_run_script_remotely(scp_command)
         print('meow')
         self.create_and_run_bash_file(records_mods_bash,mkdirr=False,sudoo=False, bash_write_dir_name="/home/jross77/bash",bash_file_name="pyauto.sh",host="192.168.2.209",host_name="jross77") 
     
         
     

 def build_on_top_of_existing_business_in_category_and_constantly_update_and_reverse_engineer_business_products_and_add_to_business(self):
  '''keep this running as a listender taking all ideas from eixsting busiensses and integrating into business websites 
  update websites using this
  also use goverment data to improve business and takr ideas from oen business and add to other business in other categoriews'''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def start_hacking_with_virtual_box(self):
  ''' https://blog.stealthsecurity.sh/how-to-build-your-private-hacking-lab-with-virtualbox-6eb56e6a6a01
  use an alternative to virutal box and use phone apps'''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def reverse_engineer_and_keep_up_dated_all_business_on_stock_market(self):
  '''DO ALL BUISNESSES IN ECONONOMY INSTEAD
  have this running as a listener in backgrund to keep updating these websites
  these are business we may choose to run but will use to monitor and build our own business
  use all mentions of business and all work created by business creating feeds into websites associated with business
  and then possibly transfer to websites we use if we like the business built
  '''
  self.model_all_stock_market_websites_and_bussiness_processes()
  stock_market_busines_list=self.create_list_of_all_stock_market_businesses()
  self.keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program()# assuming its legal
  self.constantly_website_bussiness_model_using_internet()# find websites on business and take this ifnormaiton and integrate into model websites  
  self.take_business_final_product_add_to_my_business()
  starting_port=84
  set_up_website_list=["psp_website"]
  for website_name in stock_market_busines_list:
      if website_name in set_up_website_list:
          print(f" FOUND THIS WEBSITE {website_name}")
          continue
      else:
          print(f" Change THIS WEBSITE {website_name}")
          starting_port+=1
          input()
          self.set_up_multi_sites_nginx_gunicorn_systemd(website_name,starting_port,removee=True)
          self.add_tailwind_template_to_set_up_django_website(website_name,installl=False)
          self.build_phone_app_for_business(website_name)
          self.use_penetration_tesing_tools_on_server_to_test_security(website_name)
          psp_info=self.psp_pipeline(website_name)# import info from psp pipeline api from running website?
          self.create_all_other_business_content(website_name)
          self.keep_updated_on_business_in_category_and_take_all_ideas_add_to_business(website_name)
          self.reverse_engineer_business_work_and_add_ideas_and_work_to_program(website_name)
          self.build_on_top_of_existing_business_in_category_and_constantly_update_and_reverse_engineer_business_products_and_add_to_business()
          self.add_ideas_and_capital_from_other_fields_and_businesses_into_business()
          
      

  return 
 def make_final_production_changes_to_website_files(self,website_name,www_name):
  ''' make these changes once you have a website name and are ready to lautch business
  and psp has autogenerated and been updating busienss process from business in category
  https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
  # see if current set up can listen for multiple websites on port 80
  # it seems like it can according to this below link
  # so reset to port 80 nginx config file whenever you are ready to actually have website work online
  https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04
  # if this fials try the below
  Define Server Names: In your Nginx configuration file (usually /etc/nginx/sites-available/your_site), 
  use the server_name directive to specify the domain names or server names your server should handle.
  server {
        listen 80;
        server_name domain1.com; # Server name 1
        # ... other configurations for domain1.com ...
    }
  

    server {
        listen 80;
        server_name domain2.com; # Server name 2
        # ... other configurations for domain2.com ...
    }
    Multiple Server Blocks: You'll likely have multiple server blocks, each handling a different domain or server name.
  setup super user on site for admin backend or maybe remove admin depending
  need to figure this one out
  WARNINGS: need to check these off
  ?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
  ?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
  ?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
  ?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
  add the following settings to the website before lautching!!!! super important
  # and make necessary changes from this website link  
  Turning on HTTPS
  ssl_protocols TLSv1.2 TLSv1.3;
  sudo snap install --classic certbot
  sudo ln -s /snap/bin/certbot /usr/bin/certbot
  sudo certbot --nginx --rsa-key-size 4096 --no-redirect
  www.supersecure.codes,supersecure.codes
  # Add to project/settings.py
  https://securityheaders.com/
  https://www.ssllabs.com/ssltest/
  # next do penetration testing for the site to further secure it '''
  ### reset the website nginx file to port 80 and add the actually website name
  #https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04
  #https://realpython.com/django-nginx-gunicorn/#making-your-site-production-ready-with-https
  reset_to_port_80=f"""{www_name}
  {website_name}
  port 80
  listen 80 ;
  listen [::]:80 ;
  # one site have this for 
  server_name example.com www.example.com;
  other site have
  server_name test.com www.test.com;
  sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
  sudo ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/
  sudo ln -s /etc/nginx/sites-available/agriculture /etc/nginx/sites-enabled/

  """
  # will need to know the  files im working with and their structure
  # produced from the earlier function
  # so fix earlir function then write this one
  template=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\raise_you_up\raise_you_up\nginxfile.py"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\nginxfile.py" 
  modify_line_dic={}               
  self.modify_file_locally(template,final_local_file_path,modify_line_dic)
  remote_file_path=rf"/home/jross77/all_websites/{website_name}/{website_name}/"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=True)
  change_nginx_proxy="""
  refer to real python for this
  # Nginx configuration: /etc/nginx/sites-available/supersecure need to edit this to redirect to https refer to guide
    return                    307 https://$host$request_uri;
  #sudo nginx -t
  #sudo snap install --classic certbot
  #sudo ln -s /snap/bin/certbot /usr/bin/certbot
  #ssl_protocols TLSv1.2 TLSv1.3;
  proxy_set_header    X-Forwarded-Proto $scheme;
  
  """
  template=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\raise_you_up\raise_you_up\nginxfile"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\nginxfile" 
  modify_line_dic={}      
  insert_file_line_dic={}         
  self.modify_file_locally(template,final_local_file_path,modify_line_dic,insert_file_line_dic=insert_file_line_dic)
  remote_file_path=rf"/home/jross77/all_websites/{website_name}/{website_name}/"
  self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=True) 
  # create a producton setting file for hwen im ready to lautch
  change_settings_file=""" 
  SECURE_HSTS_SECONDS = 30  # Unit is seconds; *USE A SMALL VALUE FOR TESTING!*
  SECURE_HSTS_PRELOAD = True
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
  SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
  python -m pip install django-csp
  MIDDLEWARE += ["csp.middleware.CSPMiddleware"]
  CSP_STYLE_SRC = ["'self'", "cdn.jsdelivr.net"]# this may be optional need to test css stuff later
  SECURE_HSTS_SECONDS = 2_592_000  # 30 days
  # test sites security
  """
  template=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\websites\raise_you_up\raise_you_up\settings.py"
  final_local_file_path=rf"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\key_files_remote_serever\settings.py" 
  modify_line_dic={}               
  #self.modify_file_locally(template,final_local_file_path,modify_line_dic)
  #remote_file_path=rf"/home/jross77/all_websites/{website_name}/{website_name}/"
  #self.record_mods_to_files_local_to_remote_server_for_django_websites(final_local_file_path,remote_file_path,sudoo=True)
  
  return "website!"
 
  
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def add_api_for_psp_to_all_websites(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def re_sub_and_create_new_file(self,re_pattern_to_find,re_pattern_to_have,template,final_file_path):
  ''' '''
  import re
  with open(template,"r") as f1:
      file_str=f1.read()
  new_str=re.sub(re_pattern_to_find,re_pattern_to_have,file_str)
  #print(new_str)
  #input()
  with open(final_file_path,"w") as f2:
      f2.write(new_str)
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_remote_database_pyautogui(self,website_name):
  '''use pyautogui creation script to login and run temrinal commands to create database for website '''
  print('make me!')
  set_up_data_base=f"""#!/bin/bash
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo -u postgres psql
CREATE DATABASE agriculture;
CREATE USER jross777 WITH PASSWORD 'MeganisGreat';
ALTER ROLE jross777 SET client_encoding TO 'utf8';
ALTER ROLE jross777 SET default_transaction_isolation TO 'read committed';
ALTER ROLE jross777 SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE agriculture TO jross777;
\q  
  """
  #inputs:
      
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def check_latest_port_number_and_assign_website_next_port_number(self):
  '''check this on remote server '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def build_news_feed_automatic_updater(self):
  '''https://github.com/sdmg15/Best-websites-a-programmer-should-visit
  use sites from this to keep up tod ate
  add websites as needed to keep up t date on latest content
  and use searches as well
  C:/Users/yyyyyyyyyyyyyyyyyyyy/Documents/sdmg15_Best-websites-a-programmer-should-visit_ _link_ Some useful websites for programmers..pdf
  https://github.com/OpenBB-finance/OpenBB'''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def reverse_engineer_and_keep_up_dated_all_business_in_economy_historticlly_and_present(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def market_research_program(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def transfer_updated_search_function_data_and_code_to_big_white_start_api(self):
  ''' '''
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_local_pyautogui_page_action_table(self):
  ''' '''
  import psycopg2
  table_name="pyautogui_page_action_table"
  column_name_data_type_dic={
      "script_name":"text",
   "keyboard_and_mouse_press_and_time_list":"text",# break this up into list
    "active_window_url":"text",
    "active_window":"text",# only if it is a coding file otherwise just paste the active frame
    "time_stamps":"text",
    "screenshots_path":"text",
    "computer_name":"text",
    "other_associated_files":"text"}
  try:
      self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
      self.cur = self.conn.cursor()
      create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
      for column_name,data_type in column_name_data_type_dic.items():
          create_table_str+=f",{column_name} {data_type}"
      end_create_table_str = ");"
      create_table_str+=end_create_table_str
      print(create_table_str)
      self.cur.execute(create_table_str)
      self.conn.commit()
  except Exception as E:
          print(E)
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  input()
   
   # dicitonary of objects and qualtities  in problem to use to ask questions
  return 
 def create_remote_pyautogui_page_action_table(self):
  ''' '''
  table_name="pyautogui_page_action_table"
  column_name_data_type_dic={
    "script_name":"text",
   "keyboard_and_mouse_press_and_time_list":"text",# break this up into list
    "active_window_url":"text",
    "active_window":"text",# only if it is a coding file otherwise just paste the active frame
    "time_stamps":"text",
    "screenshots_path":"text",
    "computer_name":"text",

    "other_associated_files":"text"}
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_website_usable_pyautogui_table(self):
  ''' '''
  table_name="website_pyautogui_usable_script_table"
  column_name_data_type_dic={
   "script_name":"text",# break this up into list
    "exe_file":"text",# only if it is a coding file otherwise just paste the active frame
    "multiprocess_exe_file":"text",
    "timee":"text",
    "computer_name":"text",
    "other_associated_files":"text"}
  self.create_table_on_remote_server(table_name,column_name_data_type_dic)
  input()
  return 
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_big_black_usable_pyautogui_table(self):
  '''
  psql
  sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
  to exit stuff use \q
  check avialbe databases postgres=# \l
  exit with \q
   psql -U jross77 -d canlawaccessible
  CREATE USER jross77 WITH PASSWORD 'MeganisGreat';
  CREATE USER jross777 WITH PASSWORD 'MeganisGreat';
  CREATE DATABASE canlawaccessible;
  GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross777;
  GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross77;
  ALTER ROLE jross77 SET client_encoding TO 'utf8';
  ALTER ROLE jross77 SET default_transaction_isolation TO 'read committed';
  ALTER ROLE jross77 SET timezone TO 'UTC';
  Select column_name,data_type From information_schema.columns Where table_name='pyautogui_page_action_table';
  cd /etc/postgresql/16/main/
  sudo nano pg_hba.conf
  host    all             all             192.168.2.239/32           md5
  host    all             all             192.168.2.209/32           md5
  sudo systemctl reload postgresql
  sudo nano postgresql.conf
  #listen_addresses = '*'         # what IP address(es) to listen on;
  uncomment his line
    sudo ufw allow 5432
'''
  import psycopg2
  from psycopg2 import sql
  host = '192.168.2.43'  # E.g., '192.168.1.100' or 'your-database-server.com'
  port = '5432'  # Default PostgreSQL port
  dbname = 'canlawaccessible'  # E.g., 'myprojectdb'
  user = 'jross77'  # E.g., 'myuser'
  password = 'MeganisGreat'  # E.g., 'mypassword'
  table_name="website_pyautogui_usable_script_table"
  column_name_data_type_dic={
   "script_name":"text",# break this up into list
    "exe_file":"text",# only if it is a coding file otherwise just paste the active frame
    "multiprocess_exe_file":"text",
    "timee":"text",
    "computer_name":"text",
    "other_associated_files":"text"}
  try:
      self.conn = psycopg2.connect(host=host,
      port=port,
      dbname=dbname,
      user=user,
      password=password)  
      self.cur = self.conn.cursor() 
      create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
      for column_name,data_type in column_name_data_type_dic.items():
          create_table_str+=f",{column_name} {data_type}"
      end_create_table_str = ");"
      create_table_str+=end_create_table_str
      print(create_table_str)
      self.cur.execute(create_table_str)
      self.conn.commit()
  except Exception as E:
          print(E)
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  input()

  return 
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def create_big_black_pyautogui_action_table(self):
  '''need to set up postgres for this
  psql
  sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
  to exit stuff use \q
  check avialbe databases postgres=# \l
  exit with \q
   psql -U jross77 -d canlawaccessible
  CREATE USER jross77 WITH PASSWORD 'MeganisGreat';
  CREATE USER jross777 WITH PASSWORD 'MeganisGreat';
  CREATE DATABASE canlawaccessible;
  sudo -u postgres psql
  GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross777;
  GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross77;
  ALTER ROLE jross77 SET client_encoding TO 'utf8';
  ALTER ROLE jross77 SET default_transaction_isolation TO 'read committed';
  ALTER ROLE jross77 SET timezone TO 'UTC';
  ALTER DATABASE canlawaccessible OWNER TO jross77; THIS FIXED EVERYTHING
  Select column_name,data_type From information_schema.columns Where table_name='pyautogui_page_action_table';
  host    all             all             192.168.2.239/32           md5
host    all             all             192.168.2.237/32            md5
host    all             all             192.168.2.239/32            md5
host    all             all             192.168.2.207/32            md5
host    all             all             192.168.2.43/32           md5
host    all             all             192.168.2.214/32           md5
host    all             all             192.168.2.209/32           md5
host    all             all             192.168.2.45/32           md5
host    all             all             192.168.2.46/32           md5
host    all             all             192.168.2.47/32           md5
maybe doesnt like spaces that is why need to 
copy the working files on other servers for sudo nano pg_haba.conf
GRANT USAGE ON SCHEMA public TO jross77;
GRANT CREATE ON SCHEMA public TO jross77;
GRANT USAGE ON SCHEMA public TO jross777;
GRANT CREATE ON SCHEMA public TO jross777;
psql -h 192.168.2.43 -U jross77 -d canlawaccessible #ip is of the server currently at Goulburn
DROP TABLE pyautogui_page_action_table;

  '''
  import psycopg2
  from psycopg2 import sql
  table_name="pyautogui_page_action_table"
  column_name_data_type_dic={
      "script_name":"text",
   "keyboard_and_mouse_press_and_time_list":"text",# break this up into list
    "active_window_url":"text",
    "active_window":"text",# only if it is a coding file otherwise just paste the active frame
    "time_stamps":"text",
    "screenshots_path":"text",
    "computer_name":"text",
    "other_associated_files":"text"}
  host = '192.168.2.43'  # E.g., '192.168.1.100' or 'your-database-server.com'
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
      create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
      for column_name,data_type in column_name_data_type_dic.items():
          create_table_str+=f",{column_name} {data_type}"
      end_create_table_str = ");"
      create_table_str+=end_create_table_str
      print(create_table_str)
      self.cur.execute(create_table_str)
      self.conn.commit()
  except Exception as E:
          print(E)
  self.cur.close()
  self.conn.close()
  print("Connection closed.")
  input()
  return 
  #inputs:
  #outputs:
  #packages:
  #chatgpt_prompt:
  #search_prompt:
  #end state: 
  return 
 def check_rows_in_table_on_remote_server(self):
     """ """
     
 def check_rows_in_action_table_on_remote_server(self):
      """ """
      self.check_rows_in_table_on_remote_server(table_name="pyautogui_page_action_table")
    
 
      #self.check_rows_in_table_on_remote_server(table_name="pyautogui_page_action_table")
 def pyautogui_generated_on_other_computers_scripts_table(self):
     """ """
     table_name="pyautogui_other_computer_completed_generation_table"
     column_name_data_type_dic={
      "script_name":"text",# break this up into list
       "timee":"text",
       "computer_name":"text",}
     self.create_table_on_remote_server(table_name,column_name_data_type_dic)
     input()
     return 
 def retrieve_data_from_bigblack_database(self,table_name,where_string,column_list):
     """ """
     import psycopg2
     import re
     from psycopg2 import sql
     host = '192.168.2.43'  # E.g., '192.168.1.100' or 'your-database-server.com'
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
         column_list=re.sub("'","",str(column_list)[1:-1])
         sql_str=f"SELECT {column_list} FROM {table_name}{where_string};"
         #print(sql_str)
         #input()
         try:
             self.cur.execute(sql_str)
         except Exception as E:
             print(E)
         sql_data_list_list= self.cur.fetchall()
         #self.conn.commit()
     except Exception as e:
             print(f"Error: {e}")     
     self.cur.close()
     self.conn.close()
     print("Connection closed.")
     return  sql_data_list_list
 def process_sql_data(self,sql_data_list_list,column_list):
      """ bring data  from database """
      import re
      self.search_data_dic={}
      column_list_len=len(column_list)
      for column in column_list:
          self.search_data_dic[column]=[] 
      for sql_data_list in sql_data_list_list:
          for column, sql_data in zip(column_list,sql_data_list):
              # this should solve hte problem of code not being super usable because
              # we subbed out commas and such to store it
              sql_data=str(sql_data)
              #sql_data=sql_data.replace("^","\'")
              #sql_data=sql_data.replace("&","\"")
              #sql_data=sql_data.replace("~",",")
              #sql_data=sql_data.replace("?","'")
              self.search_data_dic[column].append(sql_data) 
      return self.search_data_dic
   
 def retrieve_data_from_local_database(self,table_name,where_string,column_list):
     import psycopg2
     import re
     self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
     self.cur = self.conn.cursor()
     print("Connection successful!")
     column_list=re.sub("'","",str(column_list)[1:-1])

     sql_str=f"SELECT {column_list} FROM {table_name}{where_string};"
     try:
         self.cur.execute(sql_str)
     except Exception as E:
         print(E)
     sql_data_list_list= self.cur.fetchall()
     #self.conn.commit()
     self.cur.close()
     self.conn.close()
     print("Connection closed.")
     return  sql_data_list_list
 def edit_bash_line_file(self,intital_bash_file_name,final_bash_file_name,mod_line,line_number=0):
     """ """
     with open(intital_bash_file_name,"r") as f3:
         f3_file_str=f3.read()
     f3_file_str_list=f3_file_str.splitlines()
     f3_file_str_list[line_number]=fr'{mod_line}'
     final_file_str=""
     for i, linee in enumerate(f3_file_str_list):
         if i==0:
             final_file_str=f"{linee}"
         else:
             final_file_str+=f"\n{linee}"              
     final_file_str=rf"{final_file_str}"
     with open(final_bash_file_name,"w") as f4:
         f4.write(final_file_str)
     print('change made')
 def upload_data_to_big_black_database(self,table_name,dictionary_of_values):
     """ """
     import re
     print("Connection successful!")
     for i, (table_column, column_value) in enumerate(dictionary_of_values.items()):
         column_value=str(column_value)
         column_value=column_value.replace("\'","")
         column_value=column_value.replace("\"","")
         #column_value=column_value.replace(","," ")
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
       
 def find_values_in_one_sql_dic_not_in_another_dic(self,search_data_dic_all_values,search_data_dic_missing_values,column_wanted,table_column_list):
     """ """
     import re
     missing_values_to_add_dic_list=[]        
     column_value_list_all_values=search_data_dic_all_values[column_wanted]
     column_value_list_missing_values=search_data_dic_missing_values[column_wanted]
     for i, column_all_values in enumerate(column_value_list_all_values):
         if column_all_values in column_value_list_missing_values:
             continue
         else:      
             missing_values_to_add_dic={}
             for column in table_column_list:
                 missing_value=search_data_dic_all_values[column][i]               
                 missing_values_to_add_dic[column]=missing_value
             missing_values_to_add_dic_list.append(missing_values_to_add_dic)
             #print(column_all_values)
     #print(f"missing_values_to_add_dic_list {missing_values_to_add_dic_list}")    
     #print(f"search_data_dic_all_values {search_data_dic_all_values['script_name']}")   
     # need to remove bracekts
     # and break up things added to the list

     #print(f"\n\nsearch_data_dic_missing_values {search_data_dic_missing_values['script_name']}")       
     return missing_values_to_add_dic_list
         
 def backup_both_pyauto_action_and_usable_table_to_big_black_from_website_among_oher_tables(self):
     """ this will look through all the database on website server tables and copy infomraiton we have not copied before and add it to big black
     when i add a new table to models on website database adds database name a underscore then table name to the table name-"""
     #upload website tables   
     import psycopg2
     import re
     from psycopg2 import sql
     #"website_pyautogui_usable_script_table":["script_name","exe_file","multiprocess_exe_file","timee","computer_name","other_associated_files"]
     table_name_column_list_dic={ "psp_website_pyautogui_page_action_table_2":["script_name","computer_name","other_associated_files","keyboard_or_mouse_list","press_scroll_move_list","timee_list","active_window_name_list","path_to_frame_list","spacing_to_add_list","key_value_list","active_window_url_list"],
                                 }
     for table_name, column_list in table_name_column_list_dic.items():
         sql_data_list_list=self.retrieve_data_from_website_database(table_name,"",column_list)
         search_data_dic_website=self.process_sql_data(sql_data_list_list,column_list)
         #upload bigblack tables
         sql_data_list_list=self.retrieve_data_from_bigblack_database("pyautogui_page_action_table_2","",column_list) 
         search_data_dic_big_black=self.process_sql_data(sql_data_list_list,column_list)
         #make list of file on wewbsite not on bigblack
         #print(f"search_data_dic_big_black:{search_data_dic_big_black}")
         #print(f"search_data_dic_website:{search_data_dic_website}")

         if table_name=="psp_website_pyautogui_page_action_table_2":# will need to edit this
             column_wanted="script_name"
         if table_name=="website_pyautogui_usable_script_table":
             column_wanted="script_name"
         dic_list_to_upload_to_big_black=self.find_values_in_one_sql_dic_not_in_another_dic(search_data_dic_website,search_data_dic_big_black,column_wanted,column_list)
         #print(f"dic_list_to_upload_to_big_black{dic_list_to_upload_to_big_black}")
         
         #print(dic_list_to_upload_to_big_black)
         # stop here for testing
         #input()
         #format should be single value in a list of dics with single value in each dic
         # this is big black upload
         host = '192.168.2.43'  # E.g., '192.168.1.100' or 'your-database-server.com'
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
             for dicc in dic_list_to_upload_to_big_black:  
                 print('website to big black  upload successful')
                 self.upload_data_to_big_black_database("pyautogui_page_action_table_2",dicc)
             self.conn.commit()
             self.cur.close()
             self.conn.close()
             print("Connection closed.")
         except Exception as e:
                print(f"Error: {e}")
        
         

 def create_pyautogui_file_of_inputs_and_video_venv(self):
     """create a virutal environment
     python3 -m venv env
     source env/bin/activate
     pip install psycopg2-binary
     do this for generate pyautogui files on big black too
     /home/jross77/Documents/generate_pyauto_gui_files
     """
 def add_secret_key_from_website_server_to_big_black(self):
     """  ssh-copy-id jross77@192.168.2.43"""
     print(' # need to fix public key from website server to bigblack jross77@192.168.2.43: Permission denied (publickey,password). scp: Connection closed')

 def test_generate_pyautogui_files_on_other_computers_from_big_black(self):
     # working up to here!
     
     completed_table="pyautogui_other_computer_completed_generation_table"
     uncompleted_table="pyautogui_page_action_table"
     website_listener_folder_path=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website"
     big_black_generate_folder_path=r"/home/jross77/Documents/generate_pyauto_gui_files_remote_linux"
     column_wanted_to_compare_list=["script_name","computer_name"]
     intital_pyauto_generate_bash_file=r"create_pyautogui_file_of_inputs_and_video_bash_intital.sh" # add this to bash
     final_pyauto_generate_bash_file=r"create_pyautogui_file_of_inputs_and_video_bash_final.sh" # add this to bash
     intital_pyauto_generate_bash_file_path=website_listener_folder_path + "/"+intital_pyauto_generate_bash_file
     final_pyauto_generate_bash_path=website_listener_folder_path + "/"+ final_pyauto_generate_bash_file
     username="jross77"
     host="192.168.2.43"
     # create generate_pyauto_gui_files_remote_linux on big black
     print(' WE USE SEPERATE FOLDER HERE TO ISOLATE THE GENERATIVE pyautogui code to protect ip')
     username="jross77"
     host="192.168.2.43"
     create_pyautogui_file_of_inputs_and_video_folder=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\generate_pyauto_gui_files_remote_linux"
     scp_command_list = [f"scp","-r",f"{create_pyautogui_file_of_inputs_and_video_folder}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
     self.subprocess_run_script_remotely(scp_command_list)
     script_name_to_use=r"re.error: bad escape \c at position 19 -_1745883260.4090803"
     #print(script_name_to_use)
     #print(f"to complete {to_complete_generation_table_dic}")
     print(' listner to_complete_generation_table_dic')

     line_to_sub_value=fr'database_script_name="{script_name_to_use}"'
     self.edit_bash_line_file(intital_pyauto_generate_bash_file_path,final_pyauto_generate_bash_path,line_to_sub_value,line_number=3)  
     print('see if bash file was created')              
     # copying from server to bigblack
     # still not creating the final file after edit need to fixt his
     # C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website
     host="192.168.2.43"
     scp_command_list = [f"scp",fr"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website\{final_pyauto_generate_bash_file}",  f"{username}@{host}:{big_black_generate_folder_path}/"]# put the script you want to run here '
     self.subprocess_run_script_remotely(scp_command_list)
     doc2ui = [f"ssh",  f"{username}@{host}","dos2unix",f"{big_black_generate_folder_path}/{final_pyauto_generate_bash_file}"]
     self.subprocess_run_script_remotely(doc2ui)   
     print("# need to fix the pyautogui bash so it can execute now")
     print(' need to upload the creation files tot he correct server')
     ssh_command = [f"ssh",  f"{username}@{host}",f"bash {big_black_generate_folder_path}/{final_pyauto_generate_bash_file}"]# put the script you want to run here
     self.subprocess_run_script_remotely(ssh_command)  
     input()
     
 def process_pyautogui_page_action_table(self,pyautogui_page_action_list_list,pyautogui_action_column_list):
     """ """
     import re
     pyautogui_page_action_dic={}
     single_value_columns_list=["script_name","computer_name","other_associated_files"]
     for  action_listt in pyautogui_page_action_list_list:
         for i, actionn_column_value in enumerate(action_listt):
             column_list_name=pyautogui_action_column_list[i]
             if column_list_name in single_value_column_list:
                 pyautogui_page_action_dic[column_list_name]=action_listt_or_value          
                 continue
         action_dic_list=re.split(",",action_listt_or_value[1:-1])
         pyautogui_page_action_dic[column_list_name]=action_dic_list
     return pyautogui_page_action_dic
      
 def upload_local_pyauto_scripts_not_on_website_database(self):
     """when we are not at home we will not upload everything so this iwll be to upload stuff not currently uploaded
     STILL NEED TO TEST THIS AT ONE POINT
     when i add a new table to models on website database adds database name a underscore then table name to the table name """
     table_name_column_list_dic={ "psp_website_pyautogui_page_action_table_2":["script_name","computer_name","other_associated_files","keyboard_or_mouse_list","press_scroll_move_list","timee_list","active_window_name_list","path_to_frame_list","spacing_to_add_list","key_value_list","active_window_url_list"],
                                 }
     #"website_pyautogui_usable_script_table":["script_name","exe_file","multiprocess_exe_file","timee","computer_name","other_associated_files"]
     for table_name, column_list in table_name_column_list_dic.items():
         #upload local
         sql_data_list_list=self.retrieve_data_from_local_database("pyautogui_page_action_table_2","",column_list)
         #pyautogui_page_action_dic_list_local=self.process_pyautogui_page_action_table(sql_data_list_list,table_name_column_list_dic["pyautogui_page_action_table_2"])
         search_data_dic_local=self.process_sql_data(sql_data_list_list,column_list)
         #upload rmote
         sql_data_list_list=self.retrieve_data_from_website_database(table_name,"",column_list)
         #pyautogui_page_action_dic_list_website=self.process_pyautogui_page_action_table(sql_data_list_list,table_name_column_list_dic["pyautogui_page_action_table_2"])
         search_data_dic_website=self.process_sql_data(sql_data_list_list,column_list)
         if table_name=="psp_website_pyautogui_page_action_table_2":
             column_wanted="script_name"
         dic_list_to_upload_to_website=self.find_values_in_one_sql_dic_not_in_another_dic(search_data_dic_local,search_data_dic_website,column_wanted,column_list)   
         print(f"dic_list_to_upload_to_website{dic_list_to_upload_to_website}")
         # stop here for testing
         import psycopg2
         import re
         from psycopg2 import sql
         host = '192.168.2.209'  # E.g., '192.168.1.100' or 'your-database-server.com'
         port = '5432'  # Default PostgreSQL port
         dbname = 'psp_website'  # E.g., 'myprojectdb'
         user = 'jross77'  # E.g., 'myuser'
         password = 'MeganisGreat'  # E.g., 'mypassword'
         try:
             self.conn = psycopg2.connect(host=host,
             port=port,
             dbname=dbname,
             user=user,
             password=password)            
                           
             print("Connection successful!")
             self.cur = self.conn.cursor()
             for dicc in dic_list_to_upload_to_website:    
                 try:
                     print('local to website upload successful')
                     self.upload_data_from_website_database_2(table_name,dicc)
                     
                 except Exception as e:
                     self.cur.close()
                     self.cur = self.conn.cursor()
                     print(f"Error: {e}")
                 
                 
             self.conn.commit()
             self.cur.close()
             self.conn.close()
             print("Connection closed.")
         except Exception as e:
             
             print(f"Error: {e}")
                
 def create_pyautogui_page_action_table_2(self):
     """this will have edits so we can upload from sql the keyboard_and_mouse_press_and_time_list on the other computer
     broke up the list list into its seperate qualities
     will have to change process sql data function now downstream
     need to rerig the upstream functions to make this list better
      # just dont upload these and then dont need to worry aobut redoing processing sql function
      
      # delimiter between values in the list within a column to distingusih them?
      # delimter of @@@?
      # save each key as a seperate column with lists as values
     """
     
     ### create table locally
     import psycopg2
     table_name="pyautogui_page_action_table_2"
     column_name_data_type_dic={ 
      # only upload these columns for doing processing sql and doing work on big black to generate new pyautogui scripts
      "keyboard_or_mouse_list":"text",   
      "press_scroll_move_list":"text",
      "timee_list":"text",
      "active_window_name_list":"text",
      "path_to_frame_list":"text",
      "spacing_to_add_list":"text",
      "key_value_list":"text",
      "active_window_url_list":"text",
      # just dont upload these and then dont need to worry aobut redoing processing sql function
       "script_name":"text",
       "computer_name":"text",      
       "other_associated_files":"text"}
     try:
         self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
         self.cur = self.conn.cursor()
         create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
         for column_name,data_type in column_name_data_type_dic.items():
             create_table_str+=f",{column_name} {data_type}"
         end_create_table_str = ");"
         create_table_str+=end_create_table_str
         print(create_table_str)
         self.cur.execute(create_table_str)
         self.conn.commit()
     except Exception as E:
             print(E)
     self.cur.close()
     self.conn.close()
     print("Connection closed.")
     
     ### create table on website 
     print('make the website table through models now GOING TO DO THIS THROUGH MODELS NOW')
     #table_name="pyautogui_page_action_table_2"
     column_name_data_type_dic={ 
      # only upload these columns for doing processing sql and doing work on big black to generate new pyautogui scripts
      "keyboard_or_mouse_list":"text",   
      "press_scroll_move_list":"text",
      "timee_list":"text",
      "active_window_name_list":"text",
      "path_to_frame_list":"text",
      "spacing_to_add_list":"text",
      "key_value_list":"text",
      "active_window_url_list":"text",
      # just dont upload these and then dont need to worry aobut redoing processing sql function
       "script_name":"text",
       "computer_name":"text",      
       "other_associated_files":"text"}
     #self.create_table_on_remote_server(table_name,column_name_data_type_dic)
     ### create table on big black
     import psycopg2
     from psycopg2 import sql
     table_name="pyautogui_page_action_table_2"
     column_name_data_type_dic={ 
      # only upload these columns for doing processing sql and doing work on big black to generate new pyautogui scripts
      "keyboard_or_mouse_list":"text",   
      "press_scroll_move_list":"text",
      "timee_list":"text",
      "active_window_name_list":"text",
      "path_to_frame_list":"text",
      "spacing_to_add_list":"text",
      "key_value_list":"text",
      "active_window_url_list":"text",
      # just dont upload these and then dont need to worry aobut redoing processing sql function
       "script_name":"text",
       "computer_name":"text",      
       "other_associated_files":"text"}
     host = '192.168.2.43'  # E.g., '192.168.1.100' or 'your-database-server.com'
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
         create_table_str=rf"CREATE TABLE {table_name} (id bigserial"
         for column_name,data_type in column_name_data_type_dic.items():
             create_table_str+=f",{column_name} {data_type}"
         end_create_table_str = ");"
         create_table_str+=end_create_table_str
         print(create_table_str)
         self.cur.execute(create_table_str)
         self.conn.commit()
     except Exception as E:
             print(E)
     self.cur.close()
     self.conn.close()
     print("Connection closed.")
     return 
 
 def subprocess_popen_script_remotely(self,command_list):
  ''' '''
  import subprocess
  try:
      p=subprocess.Popen(command_list)
  except subprocess.CalledProcessError as e:
      print(f"Failed to SSH into :{e}")
      print('ERROR')
  return p
 def transfer_psp_search_function_api_to_big_white(self):
     hello=r"""THIS IS TO SET UP FASTAPI    
     # step 1
     #pip3 freeze > requirements.txt  # Python3 # get all required packages from environment on big white in requirement file
     #pip install pipreqs
     #pipreqs /path/to/project
     #step 2
     #Step 1 scp current working fastapi info from big white to laptop with requirements file
     # only copy over the main,py file and requirements rather than whole directory next time
     #scp -r username@remote_server_ip:/path/to/source_directory /local/destination/directory
     #scp -r desktop-s7na8dm\doggo777@192.168.2.214:C:\Users\doggo777\Documents\psp_api C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\fast_api_big_white 
     #Step2 scp this info to big black from laptop
     #scp -r /path/to/local/storage user@remote.host:/path/to/copy
     #scp -r  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\fast_api_big_white jross77@192.168.2.200:/home/jross77/Documents/psp_api
     #Step3  install environment and necessary dependencies
     #cd /home/jross77/Documents/psp_api2
     #python3 -m venv env
     #source env/bin/activate
     or env/Scripts/Activate
     # test run script without uvicorn
     #python3 main.py
     # step 4 install all dependencies
     FOLLOW_THIS_FUNCTION_for_depeneceies=""
     dependent sudo apt install uvicorn
      pip install fastapi
      pip install uvicorn
      pip install psycopg2-binary
      pip install torch --index-url https://download.pytorch.org/whl/cu118
      pip install transformers
      pip install accelerate

     # cp main.py /home/jross77/Documents/psp_api2
     #/home/jross77/Documents/psp_api/fast_api_big_white/psp_api
     #ssh jross77@192.168.2.200
     #cd /home/jross77/Documents/psp_api/fast_api_big_white/psp_api
     #source env/bin/activate
     #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     #http://192.168.2.200:8000 # big black 
     #pip install -r requirements.txt
     #sudo apt install python3.12-venv
     #rm -r venv/
     # step 4 install all dependencies   
     # step 5 test run api on big black
     #ssh desktop-s7na8dm\doggo777@192.168.2.214
     #http://192.168.2.214:8000/# big white 
     #>ssh desktop-s7na8dm\doggo777@192.168.2.214
     #cd Documents\psp_api
     #.\venv\Scripts\activate
     #uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     #inputs:
     #outputs:
     #packages:
     #chatgpt_prompt:
     #search_prompt:
     #end state: 
     return """
 
     username="desktop-s7na8dm\doggo777"
     host="192.168.2.214"
     api_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api"
     #scp -r  C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\fast_api_big_white jross77@192.168.2.200:/home/jross77/Documents/psp_api
     scp_command_list = [f"scp", "-r",f"{api_dir}",  fr"{username}@{host}:C:\Users\doggo777\Documents\Coding\apis"]# put the script you want to run here 
     self.subprocess_run_script_remotely(scp_command_list)
     
 def activate_psp_search_function_api_on_big_white(self):
     """add this to all websites I create as the search function
     use psp website and license it to all my businesses like manus/ charities
     start this up on bgi white locally so dont need to worry
     nohup python3 script.py &
     use nohup to run htis remotely and turn off ssh conneciton and have it still running
     kill exisitng python prcoesses with pkill -9 python on restart if use nohup
     python -m venv env
     add this for loggings
     --log-level debug
     MUST KILL ALL EXISTING PYTHON PROCESSES before styarting api to ensure it restarts correctly
     so turn off reload on fastapi when debugging to enure the fastapi locses and port 8000 actually
     starts to run the new fastapi process
     """

     print("PLEASE ADD NOHUP TO BASH WHEN RUNNIGN THIS TO keep it running when ssh connection dies")
     print('kill exisitng python prcoesses with pkill -9 python on restart')
     ### example code below
     username=r"desktop-s7na8dm\doggo777"
     host="192.168.2.214"  
     ssh_command = [f"ssh",  f"{username}@{host}",r"cd C:\Users\doggo777\Documents\Coding\apis\psp_search_function_api\psp_search_function_api && .\env\Scripts\activate && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]# put the script you want to run here
     # activate white api 
     #ssh_command = [f"ssh",  f"{username}@{host}",r"cd C:\Users\doggo777\Documents\psp_api\ && .\venv\Scripts\activate && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]# put the script you want to run here
     #self.subprocess_popen_script_remotely(ssh_command)
     self.subprocess_run_script_remotely(ssh_command)
     print('done')
     input()
     #bash_file=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\activate_psp_api_on_big_white.sh"
     # may need to do this with a single line
     #.\venv\Scripts\activate && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     #scp_command_list = [f"scp",f"{bash_file}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
     #self.subprocess_run_script_remotely(scp_command_list)    
     # execute listener on website which talks to big black
     #doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/activate_psp_api_on_big_white.sh"]
     #self.subprocess_run_script_remotely(doc2ui)    


 def transfer_pyautogui_generation_listener_to_big_black(self):
     """ """
     #     C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website
     #C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\activate_psp_api_on_big_white.sh     
     username="jross77"
     host="192.168.2.43"  
     listner_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website"
     scp_command_list = [f"scp", "-r",f"{listner_dir}",  fr"{username}@{host}:/home/jross77/Documents/Coding"]# put the script you want to run here 
     self.subprocess_run_script_remotely(scp_command_list)
     
 def activate_pyautogui_generation_listener_on_big_black(self):
     """nohup python3 script.py &
     use nohup to run htis remotely and turn off ssh conneciton and have it still running
     ill exisitng python prcoesses with pkill -9 python on restart in bash
     nohup python your_script.py &
     ps aux | grep python verify script running
"""
     print("PLEASE ADD NOHUP TO BASH WHEN RUNNIGN THIS TO keep it running when ssh connection dies")
     print('kill exisitng python prcoesses with pkill -9 python on restart')   
     #     psp_search_function_api_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website"
     ### example code below
     username="jross77"
     host="192.168.2.43"  
     #scp_command_list = [f"scp",f"{bash_dir}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
     #self.subprocess_run_script_remotely(scp_command_list)   
     # execute listener on website which talks to big black
     #doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/copy_website_to_big_black_usb.sh"]
     #self.subprocess_run_script_remotely(doc2ui)  
     print('note this listener  will be running on big white')
     ssh_command = [f"ssh",  f"{username}@{host}",r"cd /home/jross77/Documents/Coding && source env/bin/activate && python ./pyauto_gui_listener_website/pyautogui_website_computer_creation_listener_exe.py"]# put the script you want to run here 
     #ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/copy_website_to_big_black_usb.sh"]# put the script you want to run here
     #self.subprocess_run_script_remotely(ssh_command)
     self.subprocess_popen_script_remotely(ssh_command)
     
 def transfer_pyauto_script_exe_schedule_listener_to_big_black(self):
     """ """
     #     C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website
     #C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\activate_psp_api_on_big_white.sh     
     username="jross77"
     host="192.168.2.43"  
     listner_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_script_exe_schedule_listener_big_black"
     scp_command_list = [f"scp", "-r",f"{listner_dir}",  fr"{username}@{host}:/home/jross77/Documents/Coding"]# put the script you want to run here 
     self.subprocess_run_script_remotely(scp_command_list)
     
 def activate_pyauto_script_exe_schedule_listener_on_big_black(self):
     """nohup python3 script.py &
     use nohup to run htis remotely and turn off ssh conneciton and have it still running
     ill exisitng python prcoesses with pkill -9 python on restart in bash
     nohup python your_script.py &
     ps aux | grep python verify script running
"""
     print("PLEASE ADD NOHUP TO BASH WHEN RUNNIGN THIS TO keep it running when ssh connection dies")
     print('kill exisitng python prcoesses with pkill -9 python on restart')   
     #     psp_search_function_api_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website"
     ### example code below
     username="jross77"
     host="192.168.2.43"  
     #scp_command_list = [f"scp",f"{bash_dir}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
     #self.subprocess_run_script_remotely(scp_command_list)   
     # execute listener on website which talks to big black
     #doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/copy_website_to_big_black_usb.sh"]
     #self.subprocess_run_script_remotely(doc2ui)  
     print('note this listener  will be running on big white')
     ssh_command = [f"ssh",  f"{username}@{host}",r"cd /home/jross77/Documents/Coding && source env/bin/activate && python ./pyauto_script_exe_schedule_listener_big_black/exe_pyauto_script_exe_schedule_listener_big_black.py"]# put the script you want to run here 
     #ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/copy_website_to_big_black_usb.sh"]# put the script you want to run here
     #self.subprocess_run_script_remotely(ssh_command)
     self.subprocess_popen_script_remotely(ssh_command)
 ###notifications listener
 def transfer_notification_generation_listener_to_big_black(self):
     """ """
     #     C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website
     #C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\activate_psp_api_on_big_white.sh     
     username="jross77"
     host="192.168.2.43"  
     listner_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\notifications_generation_listener_big_black"
     scp_command_list = [f"scp", "-r",f"{listner_dir}",  fr"{username}@{host}:/home/jross77/Documents/Coding"]# put the script you want to run here 
     self.subprocess_run_script_remotely(scp_command_list)
     
 def activate_notification_generation_listener_on_big_black(self):
     """nohup python3 script.py &
     use nohup to run htis remotely and turn off ssh conneciton and have it still running
     ill exisitng python prcoesses with pkill -9 python on restart in bash
     nohup python your_script.py &
     ps aux | grep python verify script running"""
     
     print("PLEASE ADD NOHUP TO BASH WHEN RUNNIGN THIS TO keep it running when ssh connection dies")
     print('kill exisitng python prcoesses with pkill -9 python on restart')   
     #     psp_search_function_api_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyauto_gui_listener_website"
     ### example code below
     username="jross77"
     host="192.168.2.43"  
     #scp_command_list = [f"scp",f"{bash_dir}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
     #self.subprocess_run_script_remotely(scp_command_list)   
     # execute listener on website which talks to big black
     #doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/copy_website_to_big_black_usb.sh"]
     #self.subprocess_run_script_remotely(doc2ui)  
     print('note this listener  will be running on big white')
     ssh_command = [f"ssh",  f"{username}@{host}",r"cd /home/jross77/Documents/Coding && source env/bin/activate && python ./notifications_generation_listener_big_black/exe_notifications_generation_listener_big_black.py"]# put the script you want to run here 
     #ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/copy_website_to_big_black_usb.sh"]# put the script you want to run here
     #self.subprocess_run_script_remotely(ssh_command)
     self.subprocess_popen_script_remotely(ssh_command)
     
     
     

 
 def activate_all_apis_and_listeners(self):
     """ startup all apis running on big white that website server uses"""
     self.transfer_notification_generation_listener_to_big_black()
     self.transfer_psp_search_function_api_to_big_white()
     self.transfer_pyautogui_generation_listener_to_big_black()
     self.transfer_pyauto_script_exe_schedule_listener_to_big_black()
     self.activate_psp_search_function_api_on_big_white()
     self.activate_pyauto_script_exe_schedule_listener_on_big_black()
     self.activate_notification_generation_listener_on_big_black
     input("time to start listener")
     self.activate_pyautogui_generation_listener_on_big_black()
     print('still need to find a way to get all of these to run togethe to make it easier to run this thingr')


 def transfer_website_data_from_website_server_to_usb_on_big_black_to_usb(self):
     """ use this to get created websites off the server and onto usb on bigblack"""
     website_dir_to_copy=r"/home/jross77/all_websites/psp_website"
     usb_dir_on_big_black="/home/jross77/Documents"
     bash_dir=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\bash\copy_website_to_big_black_usb.sh"
     username="jross77"
     host="192.168.2.43" 
     with open(bash_dir,"r") as f3:
         file_str=f3.read()
     file_str_list=file_str.splitlines()
     file_str_list[1]=fr'scp -r {website_dir_to_copy} {username}@{host}:{usb_dir_on_big_black} '
     final_file_str=""
     for i, linee in enumerate(file_str_list):
         if i==0:
             final_file_str=f"{linee}"
         else:
             final_file_str+=f"\n{linee}"              
     with open(bash_dir,"w") as f4:
         f4.write(final_file_str)
    
     username="jross77"
     host="192.168.2.209"  
     scp_command_list = [f"scp",f"{bash_dir}",  f"{username}@{host}:/home/jross77/Documents"]# put the script you want to run here 
     self.subprocess_run_script_remotely(scp_command_list)
     
     # execute listener on website which talks to big black
     doc2ui = [f"ssh",  f"{username}@{host}","dos2unix","/home/jross77/Documents/copy_website_to_big_black_usb.sh"]
     self.subprocess_run_script_remotely(doc2ui)         
     ssh_command = [f"ssh",  f"{username}@{host}",f"bash /home/jross77/Documents/copy_website_to_big_black_usb.sh"]# put the script you want to run here
     self.subprocess_run_script_remotely(ssh_command)

     
 def setup_javacript_on_websites(self):
     """ how to add a src file to a djanog site
     n your project's settings.py file, ensure that django.contrib.staticfiles is included
     in INSTALLED_APPS. Define STATIC_URL to specify the URL path for serving static files 
     (e.g., STATIC_URL = '/static/'). Optionally, you can define STATICFILES_DIRS 
     to specify additional directories where Django should look for static files.
     Inside the "static" directory, create subdirectories to organize your files (e.g., "css", "js", "images").
     Place your src file in the appropriate subdirectory.
     In your Django templates, use the {% load static %} tag at the beginning of the file to load
     the static template tags. Then, use the {% static 'path/to/your/src/file' %} tag to reference
     your src file in your HTML code. For example:
    
    1. Configure Static Files Settings
    2. Create a Static Files Directory
    3. Reference Static Files in Templates {% load static %}
    4. Collect Static Files for Production
    python manage.py collectstatic
    to upload static files use the above command
    when internal server error or changed code and need to debug 
    when debugging need turn on deubg = true in settings
    then run the server with the following command and access it with    
    python manage.py runserver 0.0.0.0:8000
    http://192.168.2.209:8000/
    after done need to turn off debugging = True in settings

    """
 def debugging_django_website_code_tips(self):
     """ when internal server error or changed code and need to debug 
     when debugging need turn on deubg = true in settings
     then run the server with the following command and access it with    
     python manage.py runserver 0.0.0.0:8000
     http://192.168.2.209:8000/
     after done need to turn off debugging = True in settings"""
 def clean_tables_on_website_and_big_black(self):
     """ psql into big black and website proper database and DELETE FROM table_name
     sudo -u postgres psql
     \l to list databases available on the server
     canlawaccessible
     use \q to quit
     \c canlawaccessible  to access canlawaccessible
     \dt for tables
     website db =psp_website
     bigblack db = canlawaccessible
     table = pyautogui_page_action_table_2
     can also use tru
     TRUNCATE TABLE psp_website_pyautogui_page_action_table_2;
     DELETE FROM psp_website_pyautogui_page_action_table_2;
     DELETE FROM pyautogui_page_action_table_2;
     SELECT COUNT(*) FROM psp_website_pyautogui_page_action_table_2
     then when use delete from table; need to make sure statement is single line and table name is correct"""
     
     
 def setup_new_fastapi_on_big_white_or_website(self):
     """ this will be the fastapi sort of bash script for windows
     can apply this if i change paths to linux and create a linux bash to setup a new api
     when i add a new table to models on website database adds database name a underscore then table name to the table name-
     create a inbound rull if windows on big white to allow the other computers to connect ot it use
     AI Overview
Learn more
To allow traffic on port 8000 through Windows Firewall, you need to create an inbound rule to allow the connection. Here's how
    """
     print('fast api!')
 def setup_pyautogui_listneer_env_on_big_black(self):
     """need to install all necessary dependencies to get listener to ru
     cd /home/jross77/Documents/Coding
     python3 -m venv env
     pip install psycopg2-binary
     pip install pyautogui
     
     """
 def setup_new_phone_app(self):
     """ copy and create a new  react native phone app"""
 def automatically_add_new_api_to_django(self):
     """automatically edit views,
     edit urls, 
     edit models
     to add search  and add template code to each of these files
     run make migrations as remote bash"""
 def automatically_add_new_page_to_django(self):
     """ """
 def send_sequence_of_gui_scripts_to_people_to_connect_and_build_connections_in_a_city(self):
     """create a sequence of gui scripts to execute in sequence to message 
     people in a given city to advertise or build connections in that city]
 follow a specific pattern in how you approach building connections in a city 
 and what you say to people to get certain effects-
use email use everything for this """
     
 def pip_installs_for_big_black_to_run_pyautogui_and_setup_local_sql_access_setup_ssh_in_other_comps(self):
     """this is to be installed like this
     #!/bin/bash
     python3 -m venv env
     source env/bin/activate
cd /home/jross77/Documents/generate_pyauto_gui_files
source env/bin/activate
pip install psycopg2-binary
pip install pyautogui
# reconfigure the database on bigblack to access it locally with pyautogui for genernative model
sudo -u postgres psql
\l to list databases available on the server
canlawaccessible
use \q to quit
\c canlawaccessible  to access canlawaccessible
\dt for tables
NEED TO USE postgres as user and not add host or port to get postgres to grab stuff lcoally
host = 'localhost'  # E.g., '192.168.1.100' or 'your-database-server.com'
#port = '5432'  # Default PostgreSQL port
dbname = 'canlawaccessible'  # E.g., 'myprojectdb'
user = 'postgres'  # E.g., 'myuser'
password = 'MeganisGreat'  # E.g., 'mypassword'
try:
    self.conn = psycopg2.connect(#host=host,
    #port=port,
    dbname=dbname,
    user=user,
    password=password) 
    
$sudo nano /etc/postgresql/14/main/pg_ident.conf
https://stackoverflow.com/questions/69676009/psql-error-connection-to-server-on-socket-var-run-postgresql-s-pgsql-5432
$sudo nano /etc/postgresql/14/main/pg_hba.conf

GRANT ALL PRIVILEGES ON DATABASE canlawaccessible TO jross77;
SOLUTION FOR DEALING WITH MUTLIPLE SYS ARGS
arg_list=sys.argv
for i, arg in enumerate(arg_list):
    if i ==0: 
        continue
    if i ==1:
        script_name_to_use=arg
        continue       
    else:
        script_name_to_use+=" "+arg
        continue       
print(script_name_to_use)
to get pyautogui to work on linux neeed to do the below code:
import os
os.environ['DISPLAY'] = ':0'
import pyautogui
### setup ssh certicates key gen on all other computers
install ssh 
ssh-keygen -t rsa -b 4096 -C "rossgrove77@gmail.com"# if no key on laptop
ssh-copy-id {username}@{host}
ssh-copy-id jross77@192.168.2.233
"""
     
                
         
         
     
     
     
 
class business_process_management_functions_g2child(business_process_management_functions_gchild):
 def __init__(self):
  ''' '''
  self.sql_switch=0
  self.spacy_switch=0
  import psycopg2
  self.conn = psycopg2.connect(dbname='can_law_accessible', user='postgres', password='Meganiscute')
  self.cur = self.conn.cursor()
 def start_flip_related_processes_at_home(self):
     """pkill -9 python: linux command to kill all current processes in linux"""
     self.law_society_practice_script()
     self.ssh_into_all_other_computers()
     self.start_instagram_automatic_creator()
     self.start_facebook_automatic_creator()
     self.start_linkedin_automatic_creator()
     self.start_ddns_listner()
     self.start_web_crawler()
     self.start_selenium_scrapers()
     self.goverment_rss_feed_listner()
     self.upload_code_base_to_other_computers()
     self.create_bash_script_for_other_computer()
     self.run_bash_script_on_other_computers()
     self.grab_journal_articles_books_and_patents_to_keep_up_with_cutting_edge_tech_feed_into_psp()
     self.retrieve_data_from_chat_gpt()
     self.set_up_tor_for_requests()
     self.search_common_crawl()
     self.send_messages_over_instagram()
     self.send_messages_over_facebook()
     self.send_messages_over_other_platforms()
     self.retrieve_emails()# to run ai over
     self.send_emails()
     self.find_grants_to_apply_to()
     self.write_grant_applications_and_automcially_apply()
     self.start_website()
     self.start_website_on_main_website_server()
     self.setup_nginx_to_run_multiple_websites()
     self.retrieve_data_from_website_database()
     self.upload_data_from_website_database()
     self.setup_website_and_ssh()
     self.create_table_on_remote_server()
     self.create_pyautogui_webscraped_content_table()
     self.retrieve_data_from_pyautogui_website_database()
     self.upload_data_from_pyautogui_website_database()
     self.pyautogui_table_listner_to_convert_into_coding_problem_solving_info()
     self.ssh_pyautogui_script_other_computer()
     self.chatgpt_ssh_script()
     self.setup_llm_model_from_lm_studio()
     self.query_llm_from_lm_studio()
     self.update_computer_to_run_ssh_certificate_with_other_computer()
     self.update_computer_to_run_postgresql()
     self.ip_address_table_creator()
     self.ip_address_look_up_table_creator()
     self.bash_script_template_creator()
     self.insert_into_ip_address_table()
     self.modify_values_in_sql()
     self.create_master_pyautogui_table()
     self.create_light_pyautogui_table()
     self.create_light_pyautogui_table()
     self.create_used_id_pyautogui_table()
     self.delete_info_from_table()
     self.problem_solving_program_action_logic()
     self.create_table_on_local_database()
     self.prompt_chat_gpt_2()
     self.mark_as_used_id()
     self.setup_website_and_api_to_run_llamma()# can run this on big white if needed too with rocm and cuda
     self.query_website_and_api_running_llamma()
     self.create_table_sql()
     self.create_prompt_table()
     self.upload_prompts()
     self.categorize_all_websites_to_perform_speicfic_actions_on_like_apply_for_grants()
     self.check_terms_and_conditions_program_on_website_before_crawl()
     self.create_website_world_map_and_real_world_map_to_figure_out_actions_to_take()
     self.create_automated_psp_coding_table()
     self.automatically_sign_up_for_all_free_trials_in_world()
     self.create_auto_psp_table()
     self.setup_tailwind_django()
     self.select_all_data_from_one_table_insert_into_table_in_other_database()
     self.setup_computer_to_run_fast_api()
     self.transfer_pyautogui_creation_program_to_other_computers()
     self.create_pyautogui_exe_files_table_on_server()
     self.transfer_over_and_run_pyautogui_creation_program()
     self.setup_open_hands()
     self.test_script_to_fix_mouse_scaling()
     self.start_up_website_on_local_network()
     self.start_up_website_on_internet()
     self.update_website_code_and_restart_website()
     self.create_and_run_bash_file()
     self.start_up_all_websites_on_server_on_internet()
     self.start_up_all_websites_on_server_on_local_network()
     self.update_all_website_code_and_restart_websites()
     self.start_up_all_apis()
     self.update_and_start_up_all_apis()
     self.update_and_start_single_api()
     self.startup_single_api()
     self.setup_website_on_remote_server()
     self.copy_website_or_api_remote_server_to_local_server()
     self.update_all_websites_from_single_website()
     self.duplicate_contents_of_one_folder_in_other_folders_bash()
     self.record_mods_to_files_local_to_remote_server_for_django_websites()
     self.copy_remote_server_file_to_local_computer()
     self.change_gunicorn_port_binding_on_all_websites()
     self.duplicate_sub_contents_of_one_folder_in_other_folders_bash()
     self.change_setting_django_to_run_on_local_network()
     self.change_setting_django_to_run_on_internet()
     self.set_up_multi_sites_nginx_gunicorn_systemd()# will use the record mods to files local here multiple times
     self.business_idea_folder_website_creator_and_business_creator_using_psp_pipeline()
     self.sudo_remove_bash()
     self.modify_file_locally()
     self.add_tailwind_template_to_set_up_django_website()
     self.build_phone_app_for_business()
     self.transfer_psp_remote_pc()
     self.use_penetration_tesing_tools_on_server_to_test_security()
     self.generate_all_category_business_list()
     self.keep_updating_and_stealing_existing_business_work_and_final_product_funnel_work_into_program()
     self.add_customized_template_files_website_dir()
     self.build_on_top_of_existing_business_in_category_and_constantly_update_and_reverse_engineer_business_products_and_add_to_business()
     self.start_hacking_with_virtual_box()
     self.reverse_engineer_and_keep_up_dated_all_business_on_stock_market()
     self.make_final_production_changes_to_website_files()
     self.add_api_for_psp_to_all_websites()
     self.re_sub_and_create_new_file()
     self.create_remote_database_pyautogui()
     self.check_latest_port_number_and_assign_website_next_port_number()
     self.build_news_feed_automatic_updater()
     self.reverse_engineer_and_keep_up_dated_all_business_in_economy_historticlly_and_present()
     self.market_research_program()
     self.transfer_updated_search_function_data_and_code_to_big_white_start_api()
     self.create_local_pyautogui_page_action_table()
     self.create_remote_pyautogui_page_action_table()
     self.create_website_usable_pyautogui_table()
     self.create_big_black_usable_pyautogui_table()
     self.create_big_black_pyautogui_action_table()
     self.check_rows_in_table_on_remote_server()
     self.check_rows_in_action_table_on_remote_server()
     self.pyautogui_website_computer_creation_listener()
     self.backup_both_pyauto_action_and_usable_table_to_big_black_from_website_among_oher_tables()
     self.add_secret_key_from_website_server_to_big_black()
     self.create_pyautogui_file_of_inputs_and_video_venv()
     self.transfer_psp_search_function_api_to_big_white()
     self.activate_psp_search_function_api_on_big_white()
     self.send_sequence_of_gui_scripts_to_people_to_connect_and_build_connections_in_a_city()



     


     
     

     


     
 def set_up_ubuntu_computer_to_run_code(self):
     """ """
     self.upload_code_base_to_other_computers()
     self.run_bash_script_on_other_computers("start_up_commands_to_run_python_code_and_grab_data_from_website_database_dont_store_everyhting")
 def update_ubuntu_computer_run_code(self):
     
    """ """
    self.upload_code_base_to_other_computers()
    self.upload_applicable_sql_database_table_to_other_computers()
    
 def get_history_of_commands_run_to_create_bash_file(self):
    """Linux or Unix and type history to list all commands copy into bash file and use here """
    print('history | cut -c 8-')
    
    
     
     
 def business_process_management(self):
  ''' '''
  processes_status=self.start_processes()
  ended_process_status=self.end_processes()
  new_process_name=self.create_new_processes()