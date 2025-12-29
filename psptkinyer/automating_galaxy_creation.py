# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 02:01:13 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
import requests
import os
class factors_analysis():
    def __init__(self):
        """ all the varaibles we will use for this project """ 
        self.factors_dictionary={}
        self.definiton_dic_with_nouns={}
        self.definiton_dic={}
        self.definiton_dic_with_nouns_and_task={}
        
        
    def upload_and_clean_factors_file(self):
        """ bring the text file  """
        import re
        with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\business plan\factors_list.txt", "r") as f:
            textt=(f.read())
        factors_and_title_list=re.split("\n",textt)
        title=''
        for factor_or_title in factors_and_title_list:
            if ">>>" in factor_or_title:
                title=factor_or_title
                title=re.sub(r"[^a-zA-Z\s]", " ",title)
                title=re.sub("  ", " ",title)
                self.factors_dictionary[title]=[]
            else:
                factor=re.sub(r"[^a-zA-Z\s]", " ",factor_or_title)
                factor=re.sub("  ", " ",factor)
                self.factors_dictionary[title].append(factor)
        return self.factors_dictionary

    def webscrap_dicitonary(self):
        import pickle
        from selenium import webdriver
        from bs4 import BeautifulSoup
        
        def grab_html(word):
            """ get a link and then retrieve and process html"""
            link= "https://www.merriam-webster.com/dictionary/"+ word
            driver.get(link) #the pages link must be inserted here
            html= driver.execute_script("return document.documentElement.outerHTML")
            sel_soup = BeautifulSoup(html, 'html.parser')
            return sel_soup
        def check_if_word_on_website(htmll_soup):
            """ check whether it is a link that does not have a possible word matching """
            not_in_dictionary = htmll_soup.find_all("p", {"class": "spelling-suggestion-text"})
            return not_in_dictionary
        def word_found_to_exist(word,sel_soup):
            """ if there is a word that we recongize found in the dictionary page retrieve it and store its definiton """
            case_history_results = sel_soup.find_all("span", {"class": "dtText"})
            textt_to_add=""
            if case_history_results:
                for result in case_history_results:
                    textt=result.get_text()
                    textt_to_add += " " + textt  
                textt_to_add=textt_to_add.replace(":","")
                self.definiton_dic[word]=textt_to_add
            return self.definiton_dic
        def word_not_exist(htmll_soup):
            """ if there is no word found retrieve other possilbe words and then return the first one"""
            possilbe_spellings=htmll_soup.find_all("p", {"class": "spelling-suggestions"})
            for i, spelling in enumerate(possilbe_spellings):
                spellingtry=spelling.get_text()
                return spellingtry
            
        driver= webdriver.Firefox()
        for category,factor_list in self.factors_dictionary.items():
            for factor1 in factor_list:
                htmll_soup=grab_html(factor1)
                not_existing=check_if_word_on_website(htmll_soup)
                if not_existing:
                    word=word_not_exist(htmll_soup)
                    try:
                        htmll_soup=grab_html(word)
                    except:
                        continue
                self.definiton_dic=word_found_to_exist(factor1,htmll_soup)   
        
                
        driver.quit()  
        #with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\business plan\definition_list.pickle","wb") as f6: #1
        #    pickle.dump(self.definiton_dic, f6, pickle.HIGHEST_PROTOCOL)
    # need to make sure words are spelled right
    # step 2  get nouns and key pos parts
    def get_nouns(self: dict) -> dict:
        """ get the corresponding nouns in the dictionary """
        import pickle
        #with open(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\business plan\definition_list.pickle","rb") as f7: #1
        #    self.definiton_dic=pickle.load(f7)
        #return self.definiton_dic
        import spacy
        nlp = spacy.load("en_core_web_trf")
        import en_core_web_trf
        nlp = en_core_web_trf.load()
        for factor, defintion in self.definiton_dic.items():
            nouns_from_definition_list=[]
            doc = nlp(defintion)
            # print([ (w.text, w.pos_) for w in doc])
            for part_of_speech_parts in doc :
                if part_of_speech_parts.pos_ == "NOUN" or  part_of_speech_parts.pos_ == "PROPN":
                    nouns_from_definition_list.append(part_of_speech_parts.text) # str str
            self.definiton_dic_with_nouns[factor]=[defintion,nouns_from_definition_list]
        return self.definiton_dic_with_nouns