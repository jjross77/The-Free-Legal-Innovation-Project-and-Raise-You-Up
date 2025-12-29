# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:29:44 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
if __name__ == '__main__':
    import sys

    # Add your directory to the Python path
    sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
    #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
    # going to affect them when they age
    #from Problems_functions import problems_functions
    #from Problems_functions import methods_window_program
    from create_auto_create_problem_tree_and_web import create_auto_create_problem_tree_and_web
    
    auto_prob_web_tree=create_auto_create_problem_tree_and_web()
    my_input = sys.argv
    auto_prob_web_tree.problem_recorded=my_input[1]
    #auto_prob_web_tree.problem_recorded=r"how do i best write a essay"
    
    #problems=problems_functions()
    #buttons.problem_recorded=sys.argv[1]
    auto_prob_web_tree.automatically_add_web_search_result_to_problem_web_and_transformations_list(auto_prob_web_tree.problem_recorded)
    auto_prob_web_tree.auto_generate_and_problem_trees_from_problem_galaxy()
    
    