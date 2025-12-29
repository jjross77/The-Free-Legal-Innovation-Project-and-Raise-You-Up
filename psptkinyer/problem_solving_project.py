# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 01:51:30 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
# end goal to help improve my life by developing methods that are better and faster which i continually build upon

# we all a shit ton of idea text goal is to use it in some way to create the problem solving method
# and create a program to do this
# i want to create a program aid that can help me get this done
# i need to sort through the 100s of page of ideas and perform a operation to put what i think are tools in a list
# questions in a list
# table of sql with different columns outlinign what the thing is and which list of things it belongs to

# what patterns exist in the data there are words periods commas that is not linear

#xproblem solving method
#+method 

# write down all the methods and Idea for different problem I have come up with that I need to solve
# write down all the tools that I have up with to solve problems
# put everything into lists at different stages
# use this thing on a daily basis as a process to follow both either to use qiickly or slowly to then create another proess
# we would have a list of questions we would ask to make connections
# we would have a list of tools we would use to work with the information that we connect
# we would have a database of hierarical concept or galaxies that we would draw upon in any given problem that comes up when we start outling a problem
# how do i use this cluster fuck of 120 apges and engage with it, do i sort it what do i do with it

from organizing_thoughts_program import idea_organizer
from pipe_line_to_process_documents6 import document_vectorizer
class problem_solving_pipeline(document_vectorizer,idea_organizer):
    def __init__(self):
       super(document_vectorizer, self).__init__()
       """ problem solving pipeline for adding to lists of various parts of the pipeline from the ideas in the ideas table""" 
       
       
        
        
        
    def process_search_to_generate_list_of_characeristics_to_divide_text(self, all_search_results):
        """ this will change the uploaded text into a workable format to be better pre processed after being uploaded from the database """
        import en_core_web_trf

        prob=problem_solving_pipeline()
        all_searches=prob.retrieve_ideas_from_database("tool")
        nlp = en_core_web_trf.load()
        #print([ (w.text, w.pos_) for w in doc])

        for search in all_searches:
            pre_processed_text=prob.pre_process_text(search[5])
            sentenced_text=prob.divide_doc_into_sentences(pre_processed_text)
            for sentence in sentenced_text:
                pos_unmodified_sentence = nlp(sentence)
                for part_of_speech_parts in pos_unmodified_sentence:
                    
                    print(part_of_speech_parts.pos_)
                    print(part_of_speech_parts)
    def create_divide_into_categories_to_get_labels(self):
        
    def divide_into_categories_with_neural_net(self, all_search_results):
        # methods
        # tools
        # questions
        #
        
                    
                    

            
        
        
        
        
        
    

#prob= pro    
#try using the sentence breaker to break it up
#find part of speech with spacy and break it up use my programs deberta model to get pos.



# how am i going to store this method in a way i can best use it with a interface
# what about a learning interface
# need to find information on the internet i can use and transform it into useful examples like history
# find ways to take things and get the underlying processes with a program or methods taken
# find for example with inventing the light bulb or completing an action
# need to find examples of connections out in nature and ideas, examples of ideas that could be connected to and other tools used
 

# goal is to form galaxies on computer and then have galaxies available for when implementing prolbem solving process
# produce a interface that is generated to help me solve problems
# use recorded examples of concepts i have learned and explained
# recorded examples of prbolems i have solved while coding or else where and solutions and whole pipeline and process i took to sovle them
# find other times peoples solved problems and apply these to examples in order to build best system and methods to solve problems.
# find better methods at recording these things and gertting them into a unifrom format by applying method and finding examples that already exist
# find method to change 
# table of methods divided into steps
# process that was taken to form methods and galaxies used and created around solving the problem
# basically find way to easily record the whole process, interface for storing galaxies with tables and lists 
# then developing program to stores these in a orgnaized format in a database like from some not word program like a text
# dont want to use word in case i lose access need to build around something else
