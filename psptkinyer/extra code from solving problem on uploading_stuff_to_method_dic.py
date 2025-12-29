# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:55:30 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

          
        #if title_of_text== "Ideas":
        #    print('meow')
        #    print("hi")
        #    self.listbox6 = tk.Listbox(frame_name,width=60)
        #    self.listbox6.grid(row=1,column=0, columnspan=3)
        #    # 2 will need to be different key to add to objectives list
        #    self.listbox6.bind("2", self.record_idea_used_for_method)
        #    self.listbox6.bind('3',self.transport_to_method_window)
        #    self.listbox6.bind("4",self.switch_to_previous_galaxy)
        #    for i in range(10):
        #        dog='woo'
        #        self.listbox6.insert(tk.END,f'{dog}')
        
        
# for sub methods
#self.listboxsub_method.delete(0, tk.END) # paste 9
#label_listt=self.import_tools_problems_or_existing_ideas(9)
#for i2, idea in enumerate(label_listt): 
#    ideaa=idea[2:-2]
# solve this it looks like
# adding questions/tools notes
# this is the next problem
# ask what is the problem look at variables and then gather information and then step by step procedure and implment
# problem: tool list is not popping up
# this is a dcitionary created in another function
# we must to access this list and make sure that when we press 2 that it adds to this list, currently it is not
# interacting with tools and ideas listboxes to add to this list so button there is probably the answer
# go to function and listboxes identify whole pipeline and see which part might be messing up to bring
# this information to this spot first check al places where this shows up
 #self.frame7:9

     
 #if category==15:
 #    self.generate_side_lists_method_design(frame,category, title_of_text="Current Method Steps")
     # 15 is a throwaway category just to rename the window in this case might need to change thsi in the future
 #if category== ideas:
 #    self.generate_side_lists_method_design(frame,category, title_of_text="Current Method Steps")
 
   # thsi is the functionnresponsble and it uses generate side list so i need to locate hte error of why
   # its not uploading in this
   for j in range(0, 3):
       
      
       
       # create a indivudal label for each 
       if i==0 and j==0:# existing galaxies to draw on  # on left side all the way down
           quad.frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           current_galaxies_connected_list=quad.import_tools_problems_or_existing_ideas(2)
           quad.side_lists("Current Connected Objects",current_galaxies_connected_list,quad.frame1)
           continue
       if i==0 and j==1:
           
           quad.frame8 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           quad.main_problem_window()
           continue
       if i==0 and j ==2: # questions I need to ask to form connections
           quad.frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           questions_list=quad.import_tools_problems_or_existing_ideas(4)
           quad.side_lists("Questions",questions_list,quad.frame2)
           continue
       if i==1 and j==0:# existing galaxies to draw on  # on left side all the way down
           quad.frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           existing_objects_in_database_list=quad.import_tools_problems_or_existing_ideas(7)
           quad.side_lists("Possible Objects",existing_objects_in_database_list,quad.frame3)
           
           # will have to set function values somehow
           continue
       if i ==1 and j==1:
           quad.frame6 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           quad.qualitites_boxes("Object and Qualities of Selected Object","Web Objects And Ideas",level=0)
           continue
       if i==1 and j ==2:
           quad.frame7 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           quad.sub_method_box_1()   
       if i ==2 and j==0:
           quad.frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           tools_list=quad.import_tools_problems_or_existing_ideas(10)
           quad.side_lists("Tools",tools_list,quad.frame4)
           continue
           
       if i ==2 and j==1:
           frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           quad.qualitites_boxes("Edit-or-Create-Sentences","Develop-Sub-Method",level=1 )
           continue
       if i==2 and j==2:
           quad.frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
           objectives_list=quad.import_tools_problems_or_existing_ideas(14) # need to make this work
           quad.side_lists("Web-Results",objectives_list,quad.frame5)
           continue