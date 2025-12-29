# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 22:49:26 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""




        for sentence1_verb in doc1[1]:
            for sentence2_verb in doc2[1]:
                temp_verb_sim_list=[]
                temp_verb_sim_list_word=[]
                previous_sim_v=0
               
                
    
                for verb_1 in sentence1_verb[0]:
                    previous_sim_v=0
                    verb_11=""
                    verb_22=""
                    for verb_2 in sentence2_verb[0]:
                        sim=float(self.cos(verb_1[0],verb_2[0]))
                        #sim=float(torch.dot(verb_1[0],verb_2[0]))

                        # only append the max sim value
                        #temp_verb_sim_list_word.append([verb_1[2],verb_2[2],sim])
                        if sim>previous_sim_v:
                            previous_sim_v=sim
                            verb_11=verb_1[2]
                            
                            verb_22=verb_2[2]
                            
                    temp_verb_sim_list.append(previous_sim_v)
                    temp_verb_sim_list_word.append([verb_11,verb_22,previous_sim_v])


                        
                if temp_verb_sim_list:
                    
                    print('hi')

                
                    verb_dic_comparison[f"{sentence1_verb[1]}:{sentence2_verb[1]}"]= temp_verb_sim_list
                    self.verb_dic_comparison_word[f"{sentence1_verb[1]}:{sentence2_verb[1]}"]=temp_verb_sim_list_word
                    

                        
              
                
                
                
        # for a sentence to be usable does it have to have nouns and verbs  ?      
        for key_noun, value_noun in noun_dic_comparison.items():
            for key_verb, value_verb in verb_dic_comparison.items():
                if key_noun == key_verb:
                    value_noun.extend(value_verb)
                    sentence_simialrity =sum(value_noun)/len(value_noun)
                    document_sim_scores[key_noun]=sentence_simialrity
                    continue
      
        return document_sim_scores 
       

     
           