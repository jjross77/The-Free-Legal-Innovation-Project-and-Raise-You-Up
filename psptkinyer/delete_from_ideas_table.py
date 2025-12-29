# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:51:30 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

#delete from edited ideas table
def delete_from_edited_table(starting_idd, ending_id=0):
    import psycopg2

    conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
    cur = conn.cursor()
    #if ending_id!=0:
    cur.execute(f"""DELETE  FROM   ideas_table_3 WHERE id >{starting_idd} ;""")
    #else:
    #    cur.execute(f"""DELETE  FROM   ideas_table_3 WHERE id >{starting_idd} and id < {ending_id} ;""")
    conn.commit()
    #self.conn.close()
    cur.close()
        
    return "hello"

    
delete_from_edited_table(1)

    
    
