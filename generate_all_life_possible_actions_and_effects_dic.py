# -*- coding: utf-8 -*-\nCreated on 2025-03-08 1741491446.7385254  @author: yyyyyyyyyyyyyyyyyyyy
if __name__ == '__main__':
 import sys
 sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api')
 from psp_search_function_api_functions import search_functions_gchild
 search=search_functions_gchild()
 search.generate_all_life_possible_actions_and_effects_dic()
 # this is for testing web crawl and getting that to work
 #input()
 # iterate through selected actions on page divide into action lsits and speerate strategies using some filter function to order 
 #and sub divide action use htis for both main actions generated on a wiki page and sub action generated on other pages
#search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved



    