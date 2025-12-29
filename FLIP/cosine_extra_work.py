# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:25:58 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

  if  sim_matrix2.size(dim=1)==1:                    
      current_index=sim_matrix44.index(max(sim_matrix44))
      print(current_index)
      current_value=sim_matrix44[current_index]
      used_rows.append(current_value)
      used_indexes.append(current_index)
      noun_dic_comparison[f"{sentence_1_noun[0][0][1]}:{sentence_2_noun[0][0][1]}"]= [used_rows,used_indexes]
      continue
                print('woo')
                
                print(column)
                current_index=column.index(max(column))
                print(current_index)
                current_value=column[current_index]
                print(current_value)

                if current_index in used_indexes:
                    print('we;ve been used')
                    
                    previous_word_use_index_in_used_indexes=used_indexes.index(current_index)
                    # this the value of the previous words index in the finals index list
                    # need to findt the index of the word that is being replaced here
                    
                    
                    past_value_at_index=used_rows[previous_word_use_index_in_used_indexes]
                    

                    if current_value > past_value_at_index:
                        
                        used_rows[previous_word_use_index_in_used_indexes]=current_value
                        used_indexes[previous_word_use_index_in_used_indexes]=current_index
                        ###
                        
                        
                        #DEAL WITH CURRENT VALUE
                        
                       
                        

                        #DEAL WITH PAST VALUe that has been replaced
                        #find the column that corresponds to the changed word
                        # this is the index is the used word_list that we have changed
                        
                        sim_matrix_modified[previous_word_use_index_in_used_indexes].remove(past_value_at_index)
                        
                        #check all the next highest value and so on to see if it is  in usedllist and if it is higher
                        # make sure it is extra correct

                        column_of_changed_word=sim_matrix_modified[previous_word_use_index_in_used_indexes]
                        updated_max_value=max(column_of_changed_word)
                        column_of_unchanged_word= sim_matrix[previous_word_use_index_in_used_indexes]
                        print(column_of_unchanged_word)
                        updated_index=column_of_unchanged_word.index(updated_max_value)
                        
                        while True:
                            print('hello')
                            if updated_index not in used_indexes:
                                break
                            
                            if updated_index in used_indexes:
                                
                                previous_word_use_index_in_used_indexes=used_indexes.index(updated_index)
                                
                                
                                past_value_at_index=used_rows[previous_word_use_index_in_used_indexes]
                                

                                if updated_max_value>past_value_at_index:
                                    break
                                    
                                  
                                    
                                if updated_max_value<=past_value_at_index:
                                    #next highest value
                                    sim_matrix_modified[previous_word_use_index_in_used_indexes].remove(updated_max_value)
                                    
                                    #check all the next highest value and so on to see if it is  in usedllist and if it is higher
                                    # make sure it is extra correct

                                    column_of_changed_word=sim_matrix_modified[previous_word_use_index_in_used_indexes]
                                    updated_max_value=max(column_of_changed_word)
                                    column_of_unchanged_word= sim_matrix[previous_word_use_index_in_used_indexes]
                                    updated_index=column_of_unchanged_word.index(updated_max_value)
                                    
                                    
                                 
                                    

                        used_rows[previous_word_use_index_in_used_indexes]=updated_max_value
                        used_indexes[previous_word_use_index_in_used_indexes]=updated_index
                        continue
                        
                        

                        




                    if current_value <= past_value_at_index:
                        filler_prevent=0
                        print(current_value)
                        print(past_value_at_index)
                        # never query sim_matrix_modified_for_index
                        print(sim_matrix_modified[ii])

                        sim_matrix_modified[ii].remove(current_value)
                        print(sim_matrix_modified[ii])
                        print('yo')
                        
                        column_of_changed_word=sim_matrix_modified[ii]
                        
                        updated_max_value=max(column_of_changed_word)
                        column_of_unchanged_word= sim_matrix[ii]
                        print(column_of_unchanged_word)
                        updated_index=column_of_unchanged_word.index(updated_max_value)
                        print(updated_index)
                        column_temp=ii

                        while True:
                           
 
                            if updated_index not in used_indexes:
                                break
                            
                            if updated_index in used_indexes:
                                print('hi')
                                
                                previous_word_use_index_in_used_indexes=used_indexes.index(updated_index)
                                print(previous_word_use_index_in_used_indexes)

                                past_value_at_index=used_rows[previous_word_use_index_in_used_indexes]
                                

                                if updated_max_value>=past_value_at_index:
                                    break

                                if updated_max_value<past_value_at_index:
                                    #need to get rid of updated max value
                                    # how to backpropagate

                                    sim_matrix_modified[column_temp].remove(updated_max_value)
                                    
                                    #check all the next highest value and so on to see if it is  in usedllist and if it is higher
                                    # make sure it is extra correct
                                    if len(sim_matrix_modified[column_temp])==0:
                                        filler_prevent=1
                                        break
                                        

                                    column_of_changed_word=sim_matrix_modified[column_temp]
                                    updated_max_value=max(column_of_changed_word)
                                    column_of_unchanged_word= sim_matrix[column_temp]
                                    updated_index=column_of_unchanged_word.index(updated_max_value)
            
                        if filler_prevent!=0:
                            used_rows[previous_word_use_index_in_used_indexes]=updated_max_value
                            used_indexes[previous_word_use_index_in_used_indexes]=updated_index
                            continue
                            
                       
                        

                if current_index not in used_indexes:
                    used_rows.append(current_value)
                    used_indexes.append(current_index)
                    print(f"this is the used value : {used_rows}")
                    print(f"this is the index used  : {used_indexes}")


                    continue
                