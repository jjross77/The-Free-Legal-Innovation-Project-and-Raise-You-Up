# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:10:15 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os
import re
import time
import torch
os.chdir(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Kimlichcova")
from pipe_line_to_process_documents2 import document_vectorizer
document_vectorizer=document_vectorizer()
chosen_document=document_vectorizer.decide_which_document_to_upload()
print(chosen_document)
document_text=document_vectorizer.upload_text(chosen_document)
print(document_vectorizer.document_name)
previous_document_id=document_vectorizer.document_id
print(previous_document_id)
dog=document_vectorizer.get_next_document(previous_document_id)
print(document_vectorizer.document_id)
dog=document_vectorizer.get_next_document(document_vectorizer.document_id)
print(document_vectorizer.document_id)

