# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:08:23 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import os
import re
import unicodedata
regex = re.compile(r'[\n\r\t]')


with open(r"E:\Legislation\Kupchak v. Dayson Holdings Ltd., 1965 CanLII 497 (BC CA).txt", "r", encoding="utf8") as f:
    with open(r"E:\HPSCANS\Kupchak v. Dayson Holdings Ltd., 1965 CanLII 497 (BC CA).txt","w", encoding="utf8") as outfile:
        read_file= f.read()
        f= read_file.replace("\n"," ")
        ff= f.replace("\t"," ")
        fff= ff.replace("\r"," ")
        new_str = unicodedata.normalize("NFKD", fff)
        outfile.write(new_str)
        