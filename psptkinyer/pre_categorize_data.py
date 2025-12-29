# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:45:57 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from organizing_thoughts_program import idea_organizer
import copy
org=idea_organizer()
data=org.upload_all_data_from_database_into_python()
org.pre_categorize_based_on_key_words_and_other_parameters(data)