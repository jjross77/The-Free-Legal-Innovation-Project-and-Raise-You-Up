# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:31:53 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""


input()

todayy=date.today()
code_file_name_only=previous_active_window+str(todayy)+ "  "+str(timeee)
code_file_name_only=re.sub(r"[ -\.]","_",code_file_name_only)
code_file_name_path=root_folder+"\\"+previous_active_window+"\\"+ code_file_name_only+".py"
code_file_name_no_path_for_function_import=code_file_name_only  