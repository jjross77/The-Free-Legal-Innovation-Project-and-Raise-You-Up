# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:59:38 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import requests
from bs4 import BeautifulSoup

Legal_HTML = requests.get(r"https://www.canlii.org/en/bc/bcca/doc/1965/1965canlii497/1965canlii497.html?autocompleteStr=Kupchak%20v.%20Dayson%20Holdings%20Ltd&autocompletePos=1")
Re_Soup= BeautifulSoup(Legal_HTML.text, 'html.parser')
Text = Re_Soup.get_text()
with open(r"E:\Legislation\Kupchak v. Dayson Holdings Ltd., 1965 CanLII 497 (BC CA).txt", 'w', encoding="utf-8") as file:
    file.write(str(Text))
