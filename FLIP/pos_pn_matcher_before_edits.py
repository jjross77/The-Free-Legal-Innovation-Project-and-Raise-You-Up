# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:07:15 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

def pos_and_pn_matcher_and_uploader(self): # need to make this more robust to ensure no information is lost in the process
    """ matching tokens with pos tags to generate data for labels and pos ffn, need to match all of these and push to pos match database"""
    import re
    #counterr=0
    word_list=[word[0].lower() for word in self.sentence_info[5]]
    #print(len(word_list))

    for i, token in enumerate(self.sentence_info[0]): # need to check if the embedding is lined up
        if "Ġ" in token:
            token=token.replace("Ġ", "")

        token=token.lower()
        
        if token in word_list:
            index_of_word=word_list.index(token)
            word=self.sentence_info[5][index_of_word][0]
            pos_tag=self.sentence_info[5][index_of_word][1]
            proper_noun_tag=self.sentence_info[5][index_of_word][2]
            #print(word)
            #print(pos_tag)
            #print(proper_noun_tag)
            #print(token)
            #counterr+=1
            #print(counterr)


            self.cur.execute( f""" INSERT INTO pos_labels (word,embedding,pos_tag)
                        VALUES ('{word}','{str(self.sentence_info[4][i])}','{str(pos_tag)}');""")
                        
            self.cur.execute( f""" INSERT INTO proper_noun_labels (word,embedding,proper_noun_labels)
                        VALUES ('{word}','{str(self.sentence_info[4][i])}','{str(proper_noun_tag)}');""")
            

            continue
        else: # need to figure out how to do we breaks so that we don't lose words
        #for not used words
            print(token)
            solved=0
            for letter in token:
                if solved==1:
                    break
                print(letter)
                
                for word_1 in word_list:
                    print(word_1)
                    
                    
                    
                    if letter in word_1:
                        print(f"{letter} has been matched with{word_1} ")
                        
                        
                        token_in_word=re.search(rf"{token}",word_1)
                        if token_in_word:
                            print(f"{word_1} has token inside of it {token} ")
                            #get initial piece and assign it the proper values 
                            
                            word_part_associated_with_token=word_1[token_in_word.span(0)[0]:token_in_word.span(0)[1]]
                            print(f"{word_part_associated_with_token} this is the part of the word")
                            
                            index_of_word=word_list.index(word_1)
                            #modify this index and produce an index next to it
                            pos_tag=self.sentence_info[5][index_of_word][1]
                            print(pos_tag)
                            
                            proper_noun_tag=self.sentence_info[5][index_of_word][2]
                            print(proper_noun_tag)
                            
                            self.cur.execute( f""" INSERT INTO pos_labels (word,embedding,pos_tag)
                                        VALUES ('{word_part_associated_with_token}','{str(self.sentence_info[4][i])}','{str(pos_tag)}');""")
                            
                                        
                            self.cur.execute( f""" INSERT INTO proper_noun_labels (word,embedding,proper_noun_labels)
                                        VALUES ('{word_part_associated_with_token}','{str(self.sentence_info[4][i])}','{str(proper_noun_tag)}');""")

                            # now need to modify the list and apply the labels to this
                            #.append new part and modify existing part this next stage we append the first part we modify
                            # incredibly important to match the i
                            if token_in_word.span(0)[0]==0:
                                
                                
                                
                                all_letters_to_right_of_match=word_1[token_in_word.span(0)[1]:]
                                print(all_letters_to_right_of_match)
                                self.sentence_info[5].append([all_letters_to_right_of_match,pos_tag,proper_noun_tag])
                                word_list.append(all_letters_to_right_of_match)
                                solved=1
                                break
                                
                                
                                #right of end
                                
                            if token_in_word.span(0)[0]!=0:
                                
                                
                                #left of start
                                all_letters_to_left_of_match=word_1[:token_in_word.span(0)[0]]
                                print(all_letters_to_left_of_match)
                                self.sentence_info[5].append([all_letters_to_left_of_match,pos_tag,proper_noun_tag])
                                word_list.append(all_letters_to_left_of_match)

                                
                                #right of start
                                all_letters_to_right_of_match=word_1[token_in_word.span(0)[1]:]
                                print(all_letters_to_right_of_match)
                                self.sentence_info[5].append([all_letters_to_right_of_match,pos_tag,proper_noun_tag])
                                word_list.append(all_letters_to_right_of_match)
                                solved=1
                                break
                            # how does this interact with the original


                        continue
                    continue

   
                
    self.conn.commit()