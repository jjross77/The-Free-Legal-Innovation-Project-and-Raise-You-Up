# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 00:03:53 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

 if name_in_a_case:
         
     name_in_a_case1=name_in_a_case.group(1)
     
     name_in_a_case2=name_in_a_case.group(2)
 if name_in_a_case:
     law2.append(name_in_a_case2)
     law2.append(name_in_a_case1)
 print(f" this is law2{law2}")
name_in_a_case=re.search(r"(.*) v\.? (.*),", law2)





 import re
 """ find all words that correspond to law words before we scrap them for pos and save them as labeled data for training law model"""
 self.document_law
 found_law_in_document=[]

 
 for mm in re.finditer(r"((\s\(?[A-Z\.,][A-Za-z\.\,\'\&\-.\(\)é]*)+\(?\)?(\s[a-z\.&]+)?\)?\)?\(?(\s[A-Z][a-z\.]*)*\)?\sv\.?(\s*\(?[A-Z\.][A-Za-z\.\'\&\-\’é]*)+\)*(\s[A-Za-z\-]+)*(\s[A-Z]*[\’a-zA-Z\.\'\&-]*)+\)?)",sentence_4):
     print(mm.group(0))
     in_remover = re.search(r"(.*)(\s?[iI]n)+(\s.*)",mm.group(0)) 
     
     if in_remover:
         print(in_remover.group(0))
         print(in_remover.group(3))

         in_remover=in_remover.group(3)
         
         #Justice, General Division, in Baziuk v. BDO Dunwoody Ward
         #Baziuk v. BDO Dunwoody Ward
         #hi i'm a dog BDO Dunwoody Ward

         leng_of_part_in_doc= int(mm.end())-int(mm.start())
         length_to_remove= leng_of_part_in_doc- len(in_remover)
         print(length_to_remove)
         
         new_start=int(mm.start())+length_to_remove
         print(f"hi i'm a dog {sentence_4[new_start:int(mm.end())]}")
         if sentence_4[new_start:int(mm.end())]==in_remover:
             law_words= re.findall("\w", in_remover)
             if law_words:
                 for wordl in law_words:
                     found_law_in_document.append(wordl)
                     continue
             #found_law_in_document.append([new_start,int(mm.end()),in_remover])
             
         continue 

     if sentence_4[int(mm.start()):int(mm.end())]==mm.group(0):
         
         law_words= re.findall("\w", mm.group(0))
         if law_words:
             for wordl in law_words:
                 found_law_in_document.append(wordl)
                 continue
         
         #found_law_in_document.append([int(mm.start()),int(mm.end()),mm.group(0)])
         
         
         
         
         
         
         
         
         
for mm in re.finditer(r"((\s\(?[A-Z\.,][A-Za-z\.\,\'\&\-.\(\)é]*)+\(?\)?(\s[a-z\.&]+)?\)?\)?\(?(\s[A-Z][a-z\.]*)*\)?\sv\.?(\s*\(?[A-Z\.][A-Za-z\.\'\&\-\’é]*)+\)*(\s[A-Za-z\-]+)*(\s[A-Z]*[\’a-zA-Z\.\'\&-]*)+\)?)",text):
    print(mm.group(0))
    in_remover = re.search(r"(.*)(\s?[iI]n)+(\s.*)",mm.group(0)) 
    
    if in_remover:
        print(in_remover.group(0))
        print(in_remover.group(3))

        in_remover=in_remover.group(3)
        
        #Justice, General Division, in Baziuk v. BDO Dunwoody Ward
        #Baziuk v. BDO Dunwoody Ward
        #hi i'm a dog BDO Dunwoody Ward

        leng_of_part_in_doc= int(mm.end())-int(mm.start())
        length_to_remove= leng_of_part_in_doc- len(in_remover)
        print(length_to_remove)
        new_start=int(mm.start())+length_to_remove
        print(f"hi i'm a dog {text[new_start:int(mm.end())]}")
        if text[new_start:int(mm.end())]==in_remover:
            found_law_in_document.append([new_start,int(mm.end()),in_remover])
            continue
        continue 

    if text[int(mm.start()):int(mm.end())]==mm.group(0):
        found_law_in_document.append([int(mm.start()),int(mm.end()),mm.group(0)])
for sentence in text:
    info_list, pos_tags=document_vectorizer2.pos_data_creator(sentence)
    
            

    


        
if law_list:
    law_list=law_list[1:]
    law_list="#0"+law_list+"#1000"
    law_list=re.findall(r"#\d+.*?#\d+",law_list)
    #take case name perform operation ensure the names do not come up
    
    # what to do if we start geting proper nouns that don't belong to a case, we will need to check the data we are feeding in and make sure when we train the nextwork we don't do this accdientally 
    


    for law in law_list:
        
        law2=re.sub(r"#\d+",r"",law)
        law2=re.sub(r"\d\d\d\d-\d\d-\d\d", "",law2)
        law2= re.sub(r"\(not available on CanLII\)","",law2)
        law2=re.sub(r"\s\s+", r" ", law2)
        name_in_a_case=re.search(r"(.*) v\.? (.*),", law2)
        #current_case_name=re.search(r"(.*) v\.? (.*),", self.document_name)

        
        if name_in_a_case:
                
            name_in_a_case1=name_in_a_case.group(1)
            
            name_in_a_case2=name_in_a_case.group(2)

        law2=law2.split(",")
        
        if name_in_a_case:
            law2.append(name_in_a_case2)
            law2.append(name_in_a_case1)

        for law_matches in law2:
            re.sub(r",","",law_matches)   
        
            for m in re.finditer(rf"{law_matches}",text):
                found_law_in_document.append([int(m.start()),int(m.end()),law_matches])
                
