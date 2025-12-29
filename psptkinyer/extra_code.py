# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:24:44 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

# what is the process to create a step and solve a problem with the web
# steps lead towards solution by looking at variables/web and using tools helps to solve whatever problem
# step 1 look at problem which is web
# step 2 pick variables from web to perform transformations on
# use tool or question to detertine type of transformation and type of variables to use
#with alloted noun or thing or thing invovled with the problem
# step 3 note type of  transformation
# step 4 note objectives moved towards through this transformation
# step 5 write down step taken in moving towards solution
# we aqre trying to maxmizing also certain qualtities of the problem reducing their negativity and in this reducing optimizing
# think of each step as a function on current situation with a output state which is hopefully moves towards positive objectives
# is this the best process using everything correctly


#def move_text_method_creation_box(self,event):
#    """ move a objective """
    
    
    
#def record_method_step(self,event):
#    """ record a step in the box  once we have come up with it"""
    
    
#def record_question_or_tool_or_qualitity_oridea_used_in_creating_method_step(self,event):
#    """ """
 # need to write in something if a qualitity is like 2 letters away it is same
 # need to account for connecting different qualtiies of different parts of the webb, and how to do this.
 # will write in a if statement that if this already exists in the lsit then i will do x
 # get better way to view the web in case this doesn't work like a form uniform way to see qualities when working in method
 
 # develop a function to print out all the values at each step of code, really need to learn how to use a debugger for this in the future to save time


 #self.text_box.destroy()
 #self.frame8.config(bg="white")
                     
 #yy=self.frame8.winfo_height()
 #xx=self.frame8.winfo_width()
 #self.label11 = tk.Label(master=self.frame8,bg="white",height=yy,width=xx)
 #self.label11.grid()   

    #def download_method(self,event):
    #    """ once a method is completely written upload it to the database"""
    
     #if title_of_text == "":
         #if title_of_text != "":
         # use title_of_text
         


      #def sub_method_box_2(self):
      #    frame.grid(row=i, column=j, padx=5, pady=5)
          

      #    button_list=[decrease,increase,decrease,decrease,decrease,decrease,decrease,decrease,decrease,decrease]
      #    text_list=["conn","update","import","","","","","",""]
      #    text_box = tk.Text(master=frame)
      #    text_box.grid()
         
          
     
     
     
         
     
     # reuse old text
 
 
     
# frame 3

# objectives
# replacing web results 5
    # 2 and 4
    # category will ensure the correct text is uploaded, frame to the right frame
    # frame 1 is connected objects leave this alone
    #frame2 is questions we need to change the questions asked but leave everything else
    # frame3 possilbe objects need to completely change this 
    # frame 4 tools relist
    # will need to remove framr1 want to keep it in tact
    
    
    #questions - replace current listed questions questions
        # sub method  replace current sub-method
        # tools
        # web reuslts to objectives #objectives for bottom right one


        # recreate info and add content

   
    #tk.Label(self.frame1)
    #i,j=0,0
    #current_galaxies_connected_list=quad.import_tools_problems_or_existing_ideas(2)
    #self.generate_side_lists_2("Connected Objects",current_galaxies_connected_list,self.frame1)
    #self.side_lists("Connected Objects",current_galaxies_connected_list,self.frame1)
    #frames={self.frame1:11,self.frame2:12,self.frame3:13,self.frame4:14,self.frame5:15}
    # will need to remove framr1 want to keep it in tact
    #for  frame, category in frames.items():
    #    for widget in frame.winfo_children():
    #        print(widget)
    #        widget.destroy()
    
   
    
    #self.frame2:12,self.frame3:13,self.frame4:14
    # frame 1 is connected objects leave this alone
    #frame2 is questions we need to change the questions asked but leave everything else
    # frame3 possilbe objects need to completely change this 
    # frame 4 tools relist
    # frame 5 is web results dealt with this
    
            
    
    {}
   
    ,self.frame3:13
    ,self.frame4:14
    for widget in self.frame5.winfo_children():
        print(widget)
        widget.destroy()
    generate_side_lists_method_design(self.frame5,"objectives",category)
    
    
  
    
    
   
            
    
    

    

    
    # get all textbox label objects
    
for i in range(3):
    for j in range(0, 3):
        if i==0 and j==0:# existing galaxies to draw on  # on left side all the way down
            self.frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            current_galaxies_connected_list=quad.import_tools_problems_or_existing_ideas(2)
            quad.side_lists("Current Connected Objects",current_galaxies_connected_list,self.frame1)
            continue
        
        if i==0 and j ==2: # questions I need to ask to form connections
            self.frame2  = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            questions_list=quad.import_tools_problems_or_existing_ideas(4)
            quad.side_lists("Questions",questions_list,self.frame2)
            continue
        if i==1 and j==0:# existing galaxies to draw on  # on left side all the way down
            self.frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            existing_objects_in_database_list=quad.import_tools_problems_or_existing_ideas(7)
            quad.side_lists("Possible Objects",existing_objects_in_database_list,self.frame3)
            # will have to set function values somehow
            continue
        if i ==2 and j==0:
            self.frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            tools_list=quad.import_tools_problems_or_existing_ideas(10)
            quad.side_lists("Tools",tools_list,self.frame4)
            continue
            
      
        if i==2 and j==2:
            self.frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            objectives_list=quad.import_tools_problems_or_existing_ideas(5)
            quad.side_lists("Web-Results",objectives_list,self.frame5)
            continue