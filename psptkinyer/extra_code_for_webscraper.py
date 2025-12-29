# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:23:54 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

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