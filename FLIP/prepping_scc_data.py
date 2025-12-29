# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 05:45:18 2022

@author: rossg
"""
import os
import re
import unicodedata
regex = re.compile(r'[\n\r\t]')

path = os.path.join(fr"D:\SCC", "test")
path_new = os.path.join(fr"D:\SCC", "new")



files=os.listdir(path)
for i, file in enumerate(files):
    f=os.path.join(rf"{path}",f"{file}")
    with open(f, "r", encoding="utf8") as f:
        with open(rf"{path_new}\3{file}","w", encoding="utf8") as outfile:
            read_file= f.read()
            f= read_file.replace("\n"," ")
            ff= f.replace("\t"," ")
            fff= ff.replace("\r"," ")
            new_str = unicodedata.normalize("NFKD", fff)
            outfile.write(new_str)
        
        
        