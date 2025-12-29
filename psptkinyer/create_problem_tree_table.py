# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 03:30:22 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

if __name__ == '__main__':
    import sys
    sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\automate_email_account_creation a1.1.1.1.1.1')
    from automate_email_account_creation_functions import automate_email_account_creation_functions
    from automate_email_account_creation_functions import automate_email_account_creation_functions_child
    from automate_email_account_creation_functions import automate_email_account_creation_functions_gchild
    ema=automate_email_account_creation_functions()
    emac=automate_email_account_creation_functions_child()
    emagc=automate_email_account_creation_functions_gchild()
    column_name_data_type_dic={"email_name":"text",
                                "email_password":"text",
                                "github_user_name":"text",
                                "github_password":"text",
                                "time_stamp":"FLOAT",
                                "whatsapp":"text",
                                "facebook_username":"text",
                                "facebook_password":"text",
                                "whatsapp":"text",
                                "source_graph":"text",
                                "github_last_accessed":"FLOAT",
                                "email_last_accessed":"FLOAT"
                               }
    ema.create_table_sql(column_name_data_type_dic,table_name="git_and_emails")