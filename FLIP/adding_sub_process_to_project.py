# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:04:35 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import subprocess
import sys
# sys.executable is the path to thr python exe file that your program was orgionalluy used with
result=subprocess.Popen([sys.executable, r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\h.py"], capture_output=True, text=True)

print("stdout:", result.stdout)
print("stderr:", result.stderr)

dictt_of_sentence = {"dog":0,"cat":2,"mat":3}
print(dictt_of_sentence.get("dog"))
