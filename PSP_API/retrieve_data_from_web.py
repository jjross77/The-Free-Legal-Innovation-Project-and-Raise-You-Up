# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 10:55:39 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""


def retreive_problem_data_from_web(self,problemmm):
     import re
     import requests
     import pickle
     from selenium import webdriver
     from bs4 import BeautifulSoup
     from selenium.webdriver.common.by import By
     from selenium.webdriver.common.keys import Keys
     import time
     from selenium.webdriver.firefox.options import Options as FirefoxOptions
     links_of_dif_docs=[]
     saved_link_list=[]
     saved_text_from_website_and_link_list=[]
     link = r"https://html.duckduckgo.com/html/"
     question_striped=problemmm.strip()
     question_to_search_for=re.sub(r"\?","",question_striped)
     question_to_search_for=re.sub(r"\n"," ",question_striped)
     question_to_search_for=re.sub(r"\s+"," ",question_striped)

     question_to_search_for=question_to_search_for[:80]
     # run it as a subprocess or multi process
     

     #print(question_to_search_for)
     #input('checking whether prompt is ok here')

     #striped_problem=problem_recorded.strip()
     #problem_to_search_for=re.sub(r"\?","",striped_problem)
     firefox_options = FirefoxOptions()
     firefox_options.headless = True
     driver= webdriver.Firefox(options=firefox_options)
     #driver= webdriver.Firefox()
     session = requests.Session()
     headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
     'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
     'Accept':'text/html,application/xhtml+xml,application/xml;'
     'q=0.9,image/webp,*/*;q=0.8'}

     driver.get(link) #the pages link must be inserted here
     content = driver.find_element(By.CLASS_NAME, 'search__input')
     content.send_keys(f"{question_to_search_for}")
     content.send_keys(Keys.ENTER)
     time.sleep(2)
     #print(content)
     html= driver.execute_script("return document.documentElement.outerHTML")
     sel_soup = BeautifulSoup(html, 'html.parser')
     links_of_dif_docs= sel_soup.findAll("a") 
     #print(links_of_dif_docs)
     if links_of_dif_docs:
         #print('hi')
         for link_found in links_of_dif_docs:
             try:
                 if link_found:
                     final_link=link_found.get('href')
                     if final_link not in saved_link_list:
                         #print(final_link)
                         if final_link:
                             if "https" in final_link:
                                 saved_link_list.append(final_link)
                             else:
                                 continue
             except:
                 continue
             
         for link_finals in saved_link_list:
             try:
                 req = session.get(link_finals, headers=headers)
                 soup = BeautifulSoup(req.text)
                 p_tag_text=soup.get_text()
                 #print(p_tag_text)
                 saved_text_from_website_and_link_list.append([str(p_tag_text),link_finals])
             
             except:
                 continue
         driver.quit()
         return saved_text_from_website_and_link_list
 # process text throw out trash vs non trash
 # divide using sentnece non sentence
 # reuse processing text from project
 # reuse from business class

#retreive_problem_data_from_web()

from multiprocessing import Process, Queue
def worker_function(queue_obj, data_in):
    result = data_in * 2
    queue_obj.put(result)

# if can forward orginal dictionary
# then run this and fill the rest here im good    
import sys
import json
print('heheh')
problemm=sys.argv[1]
loaded_prob=json.loads(problemm)
print(type(loaded_prob))
print('meow')
print(loaded_prob)

