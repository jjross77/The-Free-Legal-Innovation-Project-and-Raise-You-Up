# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:49:32 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

 def proper_noun_matcher_and_uploader(self,proper_noun_list):# need to make this more robust STILL NEED TO CREATE THIS
 #TEST THIS TOMORROW and also develop a new way to match words from pos and the normal pipeline so none are missed, bascially test pos pipeline
 
     """find the given position of a proper noun and save it to the proper noun database in order to clean the text"""
     if proper_noun_list:
         
         for i, token in enumerate(self.sentence_info[0]):
             if "Ġ" in token:
                 token=token.replace("Ġ", "")
             for word in proper_noun_list:
                 if token== word[0]:
                     #print(f"{token},{word[0]}")
                     #embedding_made_to_list=self.sentence_info[4][i].tolist()  
                     
                     #print(embedding_made_to_list)
                     self.cur.execute( f""" INSERT INTO proper_noun_labels (word,embedding,proper_noun_labels)
                                 VALUES ('{self.sentence_info[0][i]}','{str(self.sentence_info[4][i])}','{word[1]}');""")

                     break
         
         self.conn.commit()