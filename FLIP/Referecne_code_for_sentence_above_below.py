# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:04:15 2023

@author: rossg
"""

sen_wait = sen_wait - 1
if sen_wait == 0:
    if "2" in str(zero_list):
        print("How many sentences below relate to the case being referenced?")

        print(f"{c}")
        sen_wait = num_of_sen_below= int(input())
        print('Are there  sentences above that relate to the reference press Y for YES or any other key?')
        num_of_sen_above = 0
        sen_relate_y_n=input()
        if sen_relate_y_n == "y":
            num_of_sen_above = int(input())
sheet[f'G{starting_row_value}'] = num_of_sen_above
sheet[f'H{starting_row_value}'] = num_of_sen_below
    
