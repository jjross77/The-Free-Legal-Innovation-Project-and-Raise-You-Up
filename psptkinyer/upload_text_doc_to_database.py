# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 18:07:47 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import os
os.chdir(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads')
import organizing_thoughts_program
idea_object=organizing_thoughts_program.idea_organizer()
directory="phone_notes"


#dog=idea_object.fix_text_doc(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Pictures\screen_shots_fixed.txt")   
idea_object.upload_text_doc(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\ideas_folder\phone_notes\phone_notes.txt")
#print(dog)
#idea_object.update_idea_table()


