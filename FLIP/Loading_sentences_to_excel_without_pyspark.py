# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:04:16 2023

@author: rossg
"""
from nltk.tokenize import sent_tokenize
import openpyxl
with open(r"E:\Legislation\Winko v. British Columbia (Forensic Psychiatric Institute) 7602.txt", encoding = "utf8" ) as f:
    ff=f.read()
    
    sentences_of_text=sent_tokenize(ff)



    wb = openpyxl.load_workbook(r'E:\Kimlichcova\Sparrow_excell3.xlsx')
    sheet = wb.active
    Column_A = sheet['A'] 
    leng_of_columna= len(Column_A)
    print(leng_of_columna)



    for i, sentence in enumerate(sentences_of_text):
        leng_of_columna += 1
        
        sheet[f'A{leng_of_columna}'] = sentence

        
wb.save(r"E:\Kimlichcova\Sparrow_excell3.xlsx")
       

    