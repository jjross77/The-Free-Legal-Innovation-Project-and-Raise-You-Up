# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:49:07 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

if word:
    if "." or "(" or ")" or "[" or "]" in word:
        word=re.sub(r"\(",r"",word)
        word=re.sub(r"\)",r"",word)
        word=re.sub(r"\[",r"",word)
        word=re.sub(r"\]",r"",word)
        word=re.sub(r"\.",r"",word)

        
        
        
        temp_sequence_list.append(word)
        continue