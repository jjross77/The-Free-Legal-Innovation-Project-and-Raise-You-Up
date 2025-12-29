# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 00:06:50 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

if number== list_of_listboxes[self.listbox2]:
    print('2')

    # access specific item in 
    # access specific value in item
    
if number==list_of_listboxes[self.listbox3]:
    print('3')

    # access specific item in 
    # access specific value in item
    
if number==list_of_listboxes[self.listbox4]:
    print('4')

    # access specific item in 
    # access specific value in item
    
if number==list_of_listboxes[self.listbox5]:
    print('5')

    
#if number==list_of_listboxes[self.listbox6]:
#    print('6')

    
    
if number==list_of_listboxes[self.listboxsub_method]:
    print('sub')

  # problem how to access the elements in teh various listboxes
 
      
      
  # each listbox has its own value
  # 6 listboxes

  # everyone wants to buy a house in the gta they all want the same thing
  
  # if this key is pressed anywhere the screen enter this sort of 

  # possible objects
  # ` this accesses the special hotkeys window
  # so you dont' have to move cursor from window
  # see how you could do this better
  # give listbox number to access
  # then item in list box
  # then if want to access a qualtity of a thing
  # then perform an action in that listbox
  # can perform action through this hotkey system like pressing 2 to do the things
  #listbox1
  
  # specifiy listbox
  #specify number of element
  # if a qualtitiy list or multistep element specifhy number in list
  # perform operation
  # step 1 develop funciton to add a galaxy and its qualtities and then relist the qualtites 
  #as possible objects qualtites
  #if there are any to the problem
  # will need to update the current object lists too
  
  
  # extra stuff from before
  # put comma in between to identify qualtities
  # problem how are we going to access qualitites of existing galaxies here more easily solve the problem here
  # and reuse them and add them to a problem
  # maybe once we have added a object it will automatically connect qualtities of that object but 
  #not those objects qualtities 
  # maybe have to build in option to remove qualtites
  # connect to the that object up to the
  # update object list to get at a objects qualtities once I have added it to the web
  # adding these items at the top and marking them as unique in some way
  # so update list will solve the problem in relisting each time we add a object to current connected objects
  # and problem web
  
  # step 1 develop funciton to add a galaxy and its qualtities and then relist the qualtites 
  #as possible objects qualtites
  #if there are any to the problem
  # will need to update the current object lists too
  # step 2 
  # step 3 
  # step 4 
  # step 5
    if len(numbers_search_list)>3: # this is the value or qualitiy in the item
        # combine all numbers after 0 and 1
        # need to add a marker for 
        
        last_value_to_search=numbers_search_list[2:]
        merged_numbers="".join(last_value_to_search)
        search_value=int(merged_numbers)
        seelect_specific_qualities= qualities_list[search_value]

    list_of_listboxes
    listbox_number
    
    


    # find first instance of more than grab everything in the string behind it 1\d and then grab all of these
    # then 
    # just use comma to seperate values if i want to add only 1 for second value to correspond to item in listbox
    if int(numbers_search_list[0])== list_of_listboxes[self.listbox1]:
        # remember to change this to right listbox after whcih is 1 correspond to the listbox after ==
        list_box_content= self.listbox2.get(0, tk.END)
        print(list_box_content)
        
       
        
        if len(numbers_search_list)>2: # this is the item in the listbox need to deal with multiple numbers
        # combine the whole value
        
        # check for marker
            # check for this value
            # default is two values unless we add a seocnd one
            objectt_and_qualities=re.split(';',list_box_content[int(numbers_search_list[2])])
            objecttt=objectt_and_qualities[0]
            # if we want the object root how do we get that
            print(objecttt)
            qualities_list=re.split(',',objectt_and_qualities[1])
            if len(numbers_search_list)>3: # this is the value or qualitiy in the item
                # combine all numbers after 0 and 1
                # need to add a marker for 
                
                last_value_to_search=numbers_search_list[2:]
                merged_numbers="".join(last_value_to_search)
                search_value=int(merged_numbers)
                seelect_specific_qualities= qualities_list[search_value]
                # combine all the numbers

            else: # only one last number
                seelect_specific_qualities= qualities_list[numbers_search_list[2]]

            print(seelect_specific_qualities)
        if len(numbers_search_list)==2:
            # grab the whole object not just a part
            
            print('hi') 
                # retrieve object root     
            print(seelect_specific_qualities)
             # delete numbers, reenter info and selected item into listbox
            #len_of_search=len(numbers_search_list)
            print(numbers_search_list)
            #print(len_of_search)
            #modified_text=str(modified_text).split(numbers_search_list)
            #modified_text=modified_text[:-len_of_search]# delete from the end
            print(modified_text)