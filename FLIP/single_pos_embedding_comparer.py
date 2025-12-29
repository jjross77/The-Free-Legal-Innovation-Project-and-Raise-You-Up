# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 00:17:44 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

def cosine_simairlity_pos_embeddings(self, doc1, doc2): # noun and verb done seperately
    """ check cosine simailirty of all sentences in two  documents comparing nouns against other nouns and verbs against verbs output list of cosine simialrities of each and also sentence level averages"""
    # we will use dot product and multiply sentences in their matrix form
    import torch
    noun_dic_comparison={}
    verb_dic_comparison = {}
   
    
    document_sim_scores={}
    for sentence_1_noun in doc1[0]:
        for sentence_2_noun in doc2[0]:
            
            temp_sentence_sim_list_noun=[]
            temp_sentence_sim_list_noun_word=[]
            

            for noun_1 in sentence_1_noun[0]:
                temp_word_sim_list_noun=[]
                temp_sentence_sim_list_noun_word=[]
                
                #previous_sim_n=0
                #noun_11=""
                #noun_22=""
                
                for noun_2 in sentence_2_noun[0]:
                        #sim=float(self.cos(noun_1[0],noun_2[0]))
                        sim=float(torch.dot(noun_1[0],noun_2[0]))
                        
                        #     make a list for each second setnece word word compared against  the first sentence word
                        
                        temp_word_sim_list_noun.append(sim)
                        # each word can be used only once
                        # use the max of each word
                        # use next highest word if that word is used
                        temp_word_list.append([noun_1[2],noun_2[2]])

                temp_sentence_sim_list_noun.append(temp_word_sim_list_noun)
                temp_sentence_word_list.append(temp_word_list)
                
               
                
               
            #perform sentence operation
            
            
            
            
            
            for i, word_sims_n, words_of_sims in  zip(range(len(temp_sentence_sim_list_noun)),temp_sentence_sim_list_noun,temp_sentence_word_list):
                
                highest_cosine_for_single_word_index=max(word_sims_n[2]).index()
                
                highest_cosine_for_single_word= temp_sentence_sim_list_noun[i][0][highest_cosine_for_single_word_index] # max value for this word of first sentnece
                
                if temp_sentence_sim_list_noun[i][1] not in used_word_list: # use 1 here to correspond to the second word 

                    used_word_list.append(temp_sentence_sim_list_noun)
                    continue
                
                
                if temp_sentence_sim_list_noun[i][1]  in used_word_list:
                    #search to make sure that this is the highest one of this particular word
                    
                    #used_word_list.append(temp_sentence_sim_list_noun)
                    continue 

                    
                
                
                

                
                    
                 
                

                #find(max for a speicifc word)
                #if word already in use:
                #    get next highest word
                #    for that partiruclar word, 
                    
                
                
            
            
            #temp_sentence_sim_list_noun_word.append([noun_11,noun_22,previous_sim_n])



            if temp_sentence_sim_list_noun:
                print('h')
                noun_dic_comparison[f"{sentence_1_noun[1]}:{sentence_2_noun[1]}"]= temp_sentence_sim_list_noun
                self.noun_dic_comparison_word[f"{sentence_1_noun[1]}:{sentence_2_noun[1]}"]=temp_sentence_sim_list_noun_word
                