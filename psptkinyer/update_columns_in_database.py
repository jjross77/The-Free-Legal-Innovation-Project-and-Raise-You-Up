# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:12:19 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
from organizing_thoughts_program import idea_organizer
org=idea_organizer()
#org.create_idea_table()
import psycopg2

conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
cur = conn.cursor()
all_data=org.upload_all_data_from_database_into_python()
# write to other database
for data in all_data :
    idd= data[0]
    paragraph=data[5]
    paragraph_number= data[6]
    file= data[7]
    directory= data[8]
    cur.execute( f""" INSERT INTO Ideas2 (id,paragraph,paragraph_number,file_name,directory)
                VALUES ({idd},'{str(paragraph)}','{str(paragraph_number)}', '{str(file)}','{str(directory)}');""")


conn.commit()
conn.close()
cur.close()   