# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 08:16:33 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

if __name__ == '__main__':
    import sys
    from multiprocessing import Process


    # Add your directory to the Python path
    sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
    #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
    # going to affect them when they age
    #from Problems_functions import problems_functions
    #from Problems_functions import methods_window_program
    from record_screen_for_additonal_problem_data_and_send_to_sql import record_screen_for_additonal_problem_data_and_send_to_sql_l
    record_screen=record_screen_for_additonal_problem_data_and_send_to_sql_l()
    record_screen.record_screen_for_additonal_problem_data_and_send_to_sql_function("")
    input()
    #process = Process(target=record_screen.record_screen_for_additonal_problem_data_and_send_to_sql)            
    #process.start()
    