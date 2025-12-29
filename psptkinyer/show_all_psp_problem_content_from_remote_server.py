# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 08:13:15 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
# -*- coding: utf-8 -*-\nCreated on 2025-01-13 1736798069.0574346  @author: yyyyyyyyyyyyyyyyyyyy
if __name__ == '__main__':
 import sys
 sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
 from tab_problem_window_content_functions import tab_problem_window_content_functions
 tab_prob=tab_problem_window_content_functions()
 problem_name=sys.argv[1]#this should be the problem name
 print(problem_name)
 tab_prob.show_all_psp_problem_content_from_remote_server(problem_name)
 
 
