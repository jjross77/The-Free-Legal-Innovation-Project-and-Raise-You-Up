# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:37:56 2023

@author: rossg
"""

# Loop will print all columns name
# THIS ONE WORKS FOR THE NUMBER COLUMN LIST
#if cell_obj.value != None:
    #
    # USE THIS WHEN LOADING THE NUBMER ROW COLUMN 4 
    #x= json.loads(cell_obj.value)
    #column4_dic[i] = x
#wb = load_workbook(filename=path)
#sheet = wb.active
#Column_A = sheet['A'] 
#Column_B = sheet['B']  # length that we start labeling again when we reopen the file. 
#leng_of_columna= len(Column_A)
#leng_of_columnB= len(Column_B)

#wb_obj = openpyxl.load_workbook(path)
 
#es = wb_obj.active
#max_col = es.max_column
#max_row= es.max_row 

import time
import sys
import json
import subprocess


    #import ast could be a solution we might try another day

    # don't need to reload column 4 to data because you can apply the tokenizer from nltk again on intital column and should be fine
    # do this when feeding the input tokens with the labels for later processing. 

    # Give the location of the file