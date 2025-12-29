# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:09:36 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

def parse_email(email_address: str) -> str | None:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username
    return None
#In the example above, the parse_email() function has a conditional statement that checks if the email address
#passed as an argument contains the at sign (@). If it does, then the function splits on that symbol to extract the elements
#before and after the at sign, stores them in local variables, and returns the username. 
#If the argument doesn’t contain an at sign, then the return value is None, indicating an invalid email address.
def parse_email(email_address: str) -> tuple[str, str] | None:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username, domain
    return None
