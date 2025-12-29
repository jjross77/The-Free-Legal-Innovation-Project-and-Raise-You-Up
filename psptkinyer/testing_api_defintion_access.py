# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:21:42 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
import requests
import json # look up docs on this
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
#nltk.download('stopwords')
search_term= "cow"
api_link_search = r"https://www.merriam-webster.com/dictionary/" + search_term
session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
'Accept':'text/html,application/xhtml+xml,application/xml;'
'q=0.9,image/webp,*/*;q=0.8'}
req = session.get(api_link_search, headers=headers)
soup = BeautifulSoup(req.text)
mydivs = soup.find_all("span", {"class": "dtText"})
p_tag_text=mydivs[0].get_text()
print(p_tag_text)
find_word_pattern = re.compile(r"\w+")
word_list = find_word_pattern.findall(p_tag_text)
filtered_words = [word for word in word_list if word not in stopwords.words('english')]           
print(filtered_words)

