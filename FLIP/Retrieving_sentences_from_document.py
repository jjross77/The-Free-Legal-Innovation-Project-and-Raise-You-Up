# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 00:00:24 2023

@author: rossg
"""

import pyperclip
import keyboard
from ctypes import windll
import unicodedata
import os
os.chdir(r"D:\Legislation")

while True:
    keyboard.wait("]")#wait for escape key to be pressed
    if keyboard.read_key() == ']': 
        sentence2=pyperclip.paste()
        f= sentence2.replace("\n"," ")
        ff= f.replace("\t"," ")
        fff= ff.replace("\r"," ")
        new_str = unicodedata.normalize("NFKD", fff)
        
        with open(r"D:\Kimlichcova\Facts_from_all_cases.txt", mode = 'a' , encoding = "utf8") as f:
            f.write(new_str)
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
    
            

