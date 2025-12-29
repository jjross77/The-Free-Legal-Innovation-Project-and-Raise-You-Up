# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:50:21 2023

@author: rossg
"""
    sheet[f'F{starting_row_value}']= str(zero_list2)

if label2 == 4:
    
    print("Assign a value if you think is the key interpreted is a important legal concept that should be a category broader legal concept.")            
    stopper2= 0
    while stopper2 != "y": 
            
            print(temp_list)
            print(" Type Q to quit. If you think you don't need to add a value hit Y")
            print("CLICK  ENTER OR SOME NON NUMERIC VALUE")
            stopper2 = input()
            if stopper2 =="q":
                break
            print("Select a word in the sentence to label as the interpreted value in the sentence.")
            select_word_in_sentence = int(input())
            zero_list2[select_word_in_sentence]= 1
            print(split_sen[select_word_in_sentence])                
            print(" Type Y to quit. Type N to continue on the same part of sentence. Type S to go back to the sentence level.")
            stopper2 = input()
            if stopper2 == "y":
                break
            if stopper2 == "n":
                helper_to_stopper2 = 0
                for i in range(100):
                    helper_to_stopper2 += 1
                    current_word= select_word_in_sentence + helper_to_stopper2
                    print(split_sen[current_word])
                    print("Press A to quit this section else press anything to add the value to the current grouping")
                    new_value=input()
                    if new_value != "a":
                        zero_list2[current_word]= 1
                    if new_value == "a":
                        break
            if stopper2 == "s":
                continue     
    
sheet[f'F{starting_row_value}'] = str(zero_list2)