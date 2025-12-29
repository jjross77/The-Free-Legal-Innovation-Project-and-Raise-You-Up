# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 01:20:19 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from organizing_thoughts_program import idea_organizer
import copy
org=idea_organizer()
new_data=org.merge_two_table("ideas2","labels_for_idea_program")
dog=org.identify_patterns(new_data)