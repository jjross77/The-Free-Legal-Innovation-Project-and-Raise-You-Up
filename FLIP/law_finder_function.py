# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:41:16 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

from pipe_line_to_process_documents3 import document_vectorizer
import re
# need to test the pos function

document_vectorizer2=document_vectorizer()
found_law_in_document=[]
document_vectorizer2.get_next_document("16036")
text=document_vectorizer2.upload_text()
law_list=document_vectorizer2.document_law
text=document_vectorizer2.pre_process_text(text)
document_vectorizer2.pre_process_law()
law_label_dic=document_vectorizer2.pre_law_list_creator_0()
text=document_vectorizer2.divide_doc_into_sentences(text)
text=document_vectorizer2.generate_contexualized_sentences(text)
for sentence in text:
    inputs=document_vectorizer2.tokenize_document(sentence)
    outputs=document_vectorizer2.generate_embeddings(inputs[0])
    pos_sentence=document_vectorizer2.pos_data_creator(sentence[1])
    found_law=document_vectorizer2.pre_law_data_creator_1(sentence[1])
    #print(sentence[1])
    #print(found_law)
    found_law=document_vectorizer2.pre_law_data_creator_2(sentence[1],found_law,law_label_dic)
    #print(found_law)
    #print(found_law)
    #print(pos_sentence[1].text)
    law_data=document_vectorizer2.law_data_creator(pos_sentence[1],found_law)
    
    document_vectorizer2.law_matcher_and_uploader(law_data)

        

    #print(dog2)
    #print(dog2)
    





#negatives are all the other parts of speech that should not be included, but the ultimate say will be this 
#so we will assign pos and then we will assign these and certain categories of pos will be postive and others will be wrong
#what are the categories
#all others that we don't know for a specific category we just don't label for now or deal with
# like num
#lets label the cateogries
#certain categories not goo with= punc,pron,part,intj,ADJ,ADP,sym,verb,X
#certain categories don't know= num,noun,propernoun', # don't use these
# got to figure out what v is classifed as
#part,
                    

                
                
                

            
                # need to prevent the searching of the name of the respondnet or people invoved in the case cause this will yield bad results
                


       
        # search document
        


# what to do with single numbers
# will often be no law so put in if statement