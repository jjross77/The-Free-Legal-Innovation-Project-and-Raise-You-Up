# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:13:16 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
coding_root=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding"

import os
dirr=os.listdir(coding_root)
print(dirr)

for dird in dirr:
    sub_dir=coding_root+"\\"+dird
    sub_dirr=os.listdir(sub_dir)
    print(sub_dirr)
input()