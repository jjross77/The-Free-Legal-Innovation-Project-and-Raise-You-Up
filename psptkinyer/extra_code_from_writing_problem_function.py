# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:55:13 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
 
        
        
        # record the tool or question or web search result that led to the idea or connection
        # record method more broadly that active in the whole program
        # record a question used to form a given conenction when problem solving
        # record it in database for connections
        # what do i want to record as much as I can
        # the main box should be for only problems and the sub boxes are for ideas and other methods
        # divide into pos or divide and only keep nouns and verbs and then search database for possible objects that have same or similar nouns and verbs and use nueral network for this
        # differnet operations depending on differnt clicks that appear in the box
        # the differnet things i want to do with the text like create objects send 
    #def 
    # we need to record how we do each thing so we can automate it as much as possible
    # think of different hotkeys that could be performed on highlighted text when connecting ideas
    #different hotkeys we could write as tools become more useful and depending on specifci quesitons
    # we want to note the question which led to a certain connections and record this so we cna automate everything later.
    
    
    def automatically_web_search_once_problem_written(self):
        """ once a problem is outlined and we go into start connecting problem we will have the program automcially generate a web search result idea list"""
        
        
        
        
    def record_time_auto_update(self): # do the same thing as taking data from box and updating or creating a column in table just on a timer and record time
        """ after a certain time or certain key strokes save time and all data currently in the program to various tables"""
        # certain logic for each of the five text-windows
        import time
        #if 50 key strokes or 1 minute then update databases for each of the windows
        # in order to do this and update and record all textboxes need to know what each of them contain and how they work
        # top text box is problems that i have defined
        # left top is qualtities and there objects attached form would be  first word is object or words then some symbol
        # then a list of different qualities or ideas attached to that object.
        # should have a list of qualtities to possiblity attach to
        #; to seperste object and then [ to seperate qualtities in the list
        # seperated by brackets like this[
        # qualtities list of different objects
        # what should i put in the top right box
        #def record_every_step_saving_sorting_data_automaically(self):
        #    """ record the question used to form a connection"""
        
        # key strokes 50
        
        
    #to database updating database from the 
    # 5 text windows have them all have various functions to update and procedure depending on the content of the window
    #

        #objects seperated by ; and qualtities by = sign

       
        # start of problem have a question or tool then would if using only a single word then next object or layer is this question or word
        # the idea is intital stage is quesiton; next stage is using a tool is single word from question ; next stage is another tool is qualtites of this word
        # strcture of objects written are ; to seperate objects from qualtities and then [ to seperate qualtities from qualtitess

         
      
      
        
    
    #def export_object_to_new_table(self,event):
    #      """record the object created or connected to  and its qualtities """
         

        
        
        
    #def store_object_in_connected_object_window_by_question_or_tool(self,event):
    #    """ once having recorded the question or tool used I will then store the object
    #    I have selected or written into the connected objects window and dictionary, 
    #    with its linked question or tool """
    #    import re
    #    from ctypes import windll
    #    content=window.selection_get()
        #re.split(';')
        #re.split('=')
        
        #time_created =time.time()
         # assume tool or question is the same unless updated
         
        #[{self.problem_recorded:[[time_created][tool_question,quality,time_qualitity_found],[tool_question,quality],[tool_question,quality],[tool_question,quality]]}]
        #add to list
        #if new qualitity as root
        #qualitity=x
        #.append({quality:[[tool_question,quality],[tool_question,quality],[tool_question,quality],[tool_question,quality]]})
        # append to list within quality
        #.append()
        #{quality:[[tool_question,quality],[tool_question,quality],[tool_question,quality],[tool_question,quality]]}]
        
         
         #{quality:[[tool_question,quality],[tool_question,quality],[tool_question,quality],[tool_question,quality]]}]
         

        # first make sure you have a question or tool to branch out from
        
        #problem_dictionary={problem or object:self.recorded_question_or_tool,[qualtiies_list]}
        # goal is to connect it in a web but in dictionart form with the links being questions
        # all coming from the intital problem
        #[{problem:[[tool_question,quality],[tool_question,quality],[tool_question,quality],[tool_question,quality]]}
        #{quality:[[tool_question,quality],[tool_question,quality],[tool_question,quality],[tool_question,quality]]}]
        #save_problem_object  
        
        # so we would always have the root ; and then the qualtities and then they would be stored in the window
        
        
        
      
        # the root of the dicontary is the problem
        # we would expand out by looking at words of the problem but would connect these words as seperate objects with questions or tools connecting them
        # write in the question
        # we would then create attach an object and as a bridge write down the tool or question we used to get to that object
        # we would then expand out and connect more objects to the qualties of that object
        #write down the question and then store it somewhere in the dicitonary
        
        
        # we need to find a way to use this thing effectively in the method design window
        
        # stored dictionary of qualtites and objects
        # make the connections stored dicontary and update it as making connections
        # find a way to get access to existing problems
        # when a sentence does not make sense need to combine the sentence proceeding it with it and update database
        
        
        # store the connections stored dictonary in proble mdatabase
        #def store_connections_between_objects_qualities_or_themselves(self,action):
        #    """ """
    def record_object_created(self,event):
        """record the object created or connected to  and its qualtities """
        # objects will be in the form of a dictonary
        import re
        from ctypes import windll
        content=window.selection_get()
        re.split(';')
        re.split('=')

    def export__final_problem_galaxy(self,event):
        """ once web is fully complete store the web in the problem_database"""
        # send the galaxy to both databases in cases of a crash save everything need to write a function for this
        import re
        import time
        modified_text=self.text_box0.get('1.0', 'end')
        finish_time_object=time.time()
        try:
            objectt_and_qualities=re.split(';',modified_text)
            qualities_list=re.split('=', objectt_and_qualities[1] )
            objectt=objectt_and_qualities[0]
            qualities_list=str(qualities_list)
            qualities_list=re.sub('\'',"",qualities_list)
            qualities_list=re.sub('\"',"",qualities_list)
            print(f"{objectt}:{qualities_list}")
        except Exception as e:
            print(e) 
        self.cur.execute( f""" INSERT INTO galaxies_table (problem_or_idea_root,qualities,tool_or_question_used_per_qualitity,finish_time,start_time)
                     VALUES ('{objectt}','{qualities_list}','{str(self.recorded_question_or_tool)}','{str(finish_time_object)}','{str(self.starting_time_object)}');""")
        self.conn.commit()
        
        
        
def select_which_dictionary_problem_galaxy_to_expand(self,event):
    # double click for implementation of this
    """ if we need to expand a different dictionary then we currently have in the window or modify a existing
    one we can select a different one with this function"""
    time_created =time.time()
    #select new current_object_or_problem
    #self.current_object_or_problem =
    # pick from list
    #self.problem_list_dictionary[]
    
    
#def save_object(self,event):
#    """ place object in objects table with its connected qualtites""" 
           
# save the time when doing each of these things and when making specific connections



#def create_problem_intital_problem_dictionary(self,event):
#    """start a new dictionary with the problem you have selected for this section """
#    time_created =time.time()
#    self.problem_list_dictionary=[{self.problem_recorded:[[time_created]]}]
#    print(self.problem_list_dictionary)
    


          
                
                
                #self.cur.execute( f""" UPDATE galaxies_table 
                #                 Set problem_or_idea_root= '{str(problem_or_object)}', qualities = '{str(qualitity_list)}',
                #                 tool_or_question_used_per_qualitity = '{str(tool_or_question_list)}', finish_time = '{str(time_created_list)}'
                #                 WHERE problem_question_or_task = '{str(self.problem_recorded)}' and specific_problem_or_object = '{str(problem_or_object)}';""")     
 
            # fix insert thing multiple times

           
            #        self.listbox1.insert(tk.END, f"{specific_problem_or_object};{qual1}=") 
            #        continue
                #if i == len(master_tool_or_question_per_conn_list):
                #    self.listbox1.insert(tk.END, f"{qual1}\n") 
                #    continue
            #    else:
            #        self.listbox1.insert(tk.END, f"{qual1}=") 
            #        continue
        
        #for conn,qual,time in zip(tool_or_question_per_conn_list,qualitity_list,time_created_conn):
            #master_tool_or_question_per_conn_list.append(conn)
            #master_time_created_conn.append(time)  
            #master_qualitity_str+=f"={qual}"
            #print(qual)
        #print(master_qualitity_str)
            
        #for i, conn1,qual1,time1 in zip(range(len(master_tool_or_question_per_conn_list)),master_tool_or_question_per_conn_list,master_qualitity_list,master_time_created_conn):
        #    if i ==0:


    #def create_new_qualitity__or_galaxy_dictionary(self,event):
    #     """ append a new dictionary to the list of dictionaries after the intital problem dictionary which
    #     this new dicitonary will have a key which is its main object which is a qualtity of the intital problem"""
    #     time_created =time.time()
    #    self.problem_list_dictionary.append({objectt:[[time_created]]})

#time_created_conn = entry[6]
#time_created_conn=re.split(",",time_created_conn[1:-1])
#reassemble the lists
#tool_or_question_per_conn_list = entry[3]
#tool_or_question_per_conn_list=re.split(",",tool_or_question_per_conn_list[1:-1])