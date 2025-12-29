# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 05:56:24 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

class generate_and_open_blender_problem_web_and_tree_functions():
    """ """
    def __init__(self):
        """ """
        
        
    def open_blender(self):
         """ """
         import subprocess
         import os
         file_path=r"C:\temp\hi.blend"
         blender_exe_path=r"C:\Program Files\Blender Foundation\Blender 4.1"
         os.chdir(blender_exe_path)
         subprocess.Popen(["blender.exe", r"C:\temp\hi.blend"])
         #subprocess.run(["cd", "C:\Program Files\Blender Foundation\Blender 4.1"])
         #open blender
         #C:\Program Files\Blender Foundation\Blender 4.1
         # this is where blender execute is
         #import subprocess
         #“blender.exe your_file_path. blend”.
         # add script to clipboard generated
         # paste script into console
         # save file
         #bpy.ops.wm.save_as_mainfile(filepath=file_path)# save blender file
         #bpy.ops.wm.open_mainfile(filepath=r"C:\temp\hi.blend")
    def get_access_to_blender_terminal(self):
         """ """
         import pyautogui
         import time
         from PIL import ImageGrab
         import numpy as np
         import pytesseract
         pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
         saved_screen_shots_text_list=[]
         time.sleep(1.044762420654297)
         pyautogui.moveTo(1179, 1072)
         pyautogui.moveTo(41, 834)
         time.sleep(0.9368200302124023)
         print('Pressed(41, 834): 3')
         print('hi [C:\temp\hi.blend] - Blender 4.1')
         self.wait_till_template_present(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\pyautogui_script_106\template1729648676.2845876.png')
    
    def make_it_easier_to_start_working_on_sub_problem_action_in_problem_tree_in_tkinyer(self):
        """make it so you can write into this problem right away """
    
    # blender problem tree functions
   
    def upload_blender_problem_tree_data_from_sql(self):
        """ problem_tree_problem_strat_list_action_list_dictionary : # key[problem]=[strats[actions]] list of list strats and actions"""
        import re
        import copy
        import time
        self.temp_all_strategy_action_list_dictionary={}
        
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table ;""")
        all_strategy_table_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(all_strategy_table_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if problem_being_solved==self.problem_recorded:
                continue# this ensures that we accdinteally double up
            if action_list:
                action_list=re.split(",",action_list[1:-1])
            if problem_being_solved not in self.temp_all_strategy_action_list_dictionary:
                self.temp_all_strategy_action_list_dictionary[problem_being_solved]=[] 
            self.temp_all_strategy_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available  
        #
        
        # repeat this process recursing each action
        # as deep as necessary until certain there are no other strategies witht hat aciton name
        # in the given tree
        self.problem_tree_problem_strat_list_action_list_dictionary={}
        time_qualitity_found =time.time()
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        specific_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(specific_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if action_list:
                action_list=re.split(",",action_list[1:-1])
            if problem_being_solved not in self.problem_tree_problem_strat_list_action_list_dictionary:
                self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved]=[] 
            self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available 
            if action_list:
                action_list_list2=[]
                action_list_list2.append(action_list)
                while True: 
                    if action_list_list2==[]:
                        break
                    action_list_list=action_list_list2
                    action_list_list2=[]
                    for action_listtt in action_list_list:
                        for actionnn in action_listtt:
                            print('ACTION LIST')
                            print(action_listtt)
                            print('ACTION ')
                            # make it so that
                            # it adds to the intital strat line block as seperate tree

                            print(actionnn)
                            if actionnn in self.temp_all_strategy_action_list_dictionary:# check if problem key for the action
                                if actionnn not in self.problem_tree_problem_strat_list_action_list_dictionary:
                                    self.problem_tree_problem_strat_list_action_list_dictionary[actionnn]=[] 
                                action_list2=self.temp_all_strategy_action_list_dictionary[actionnn]
                                if action_list2:
                                    for actionn_mini_list in action_list2:
                                        print(actionn_mini_list)
                                        self.problem_tree_problem_strat_list_action_list_dictionary[actionnn].append(actionn_mini_list)# list of list of strats available 
                                        action_list_list2.append(actionn_mini_list)
                                
                            
                                            
                                        
                                    
                                
                                
   
        #[problem]=[strats[actions]]
        # first get all sub actions
        # then with this list check through other strategy
        # data and if they have sub trees add these in as
        # strats below these strats
        # find sub strategy trees
        # repeat this process as necessary
        # because could be multiple trees deep
        print(self.temp_all_strategy_action_list_dictionary)
        print(self.problem_tree_problem_strat_list_action_list_dictionary)
        return self.problem_tree_problem_strat_list_action_list_dictionary
        # broader principles guding action are in methods table
        #actual actiosn are in strategies table
        #self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM methods_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
        #methods_info= self.cur.fetchall()
    # NEED TO MODIFY ALL OF THESE FOR PROBLEM TREE
   
    def generate_spacing_list_around_cube_problem_tree(self,current_cube_location):
        """ this list will be used as guidance to place other cubes around intital cube"""
        #import random
        possible_cube_placement_list=[]
        #current_cube_location=(1,2,3)
        current_x=current_cube_location[0]
        current_y=current_cube_location[1]
        current_z=current_cube_location[2]
        #x_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        #y_range_list=list(range(0,self.range_cube_distance_list_generation_value,3)) # 0 to 10
        #z_range_list=list(range(0,self.range_cube_distance_list_generation_value,3)) # 0 to 10
        
        x_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        y_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        z_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10



        for x_coridinate in x_range_list:
            for y_coridinate in y_range_list:
                for z_coridinate in z_range_list:
                    possible_future_x=current_x+x_coridinate
                    possible_future_y=current_y+y_coridinate
                    possible_future_z=current_z+z_coridinate
                    possible_cube_placement_list.append((possible_future_x,possible_future_y,possible_future_z))
                    
        #random.shuffle(possible_cube_placement_list) 
        return possible_cube_placement_list
    
    def find_where_to_place_cube_in_blender_problem_tree(self,possible_cube_placement_list,current_cube_location=[0,0,0]):# test this
        """ this will take the possible cube placement list and select a value that works from it
        NEED TO TEST THIS to these if recursion works here"""
        #print(possible_cube_placement_list)
        for i21, cube_placement in enumerate(possible_cube_placement_list):
            if i21==len(possible_cube_placement_list)-1:# this is in case that there is not enough space in the list of positions to place objects    #and this will create more space
                self.range_cube_distance_list_generation_value+=20
                #ERROR IS HERE need to make this function work generating more spaces 
                # WOO!
                # need to think this one out
                possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)
                current_cube_location=self.find_where_to_place_cube_in_blender(possible_cube_placement_list) # this should recurse is necessary
                return current_cube_location
            if cube_placement in self.used_square_location_list:
                continue
            else:
                current_cube_location=cube_placement   
                break
        return current_cube_location
    
    def find_which_cube_to_attach_to_in_current_web_problem_tree(self,action_placement_in_list):
        """figure out how and where to connect """
        action_placement_in_list=int(action_placement_in_list)
        cube_to_attached_to__in_current_web_location=None
        if action_placement_in_list==0:
            cube_to_attached_to__in_current_web_location=(0,0,0)# need to change these names 
            return self.problem_recorded, cube_to_attached_to__in_current_web_location
        else:
            for intital_cube_text in self.blender_problem_tree_dictionary.keys():
                intital_cube_location=self.blender_problem_tree_dictionary[intital_cube_text]["current_cube_location"]
                if intital_cube_text== self.action_listttt[action_placement_in_list-1]:
                    cube_to_attached_to__in_current_web_location=intital_cube_location# need to change these names 
                    return intital_cube_text,cube_to_attached_to__in_current_web_location 
        
    ## NEED TO MODIFY THESE
    def find_intital_cube_to_attach_to_in_current_web_problem_tree(self,problem_name_key):
        """ need to test this"""
        cube_to_attached_to__in_current_web_location=None

        for intital_cube_text in self.blender_problem_tree_dictionary.keys():
            intital_cube_location=self.blender_problem_tree_dictionary[intital_cube_text]["current_cube_location"]
            if problem_name_key == intital_cube_text:
                cube_to_attached_to__in_current_web_location=intital_cube_location# need to change these names
                return problem_name_key, cube_to_attached_to__in_current_web_location
                break        
        intital_cube_location=self.blender_problem_tree_dictionary[self.problem_recorded]["current_cube_location"]
        cube_to_attached_to__in_current_web_location=(0,0,0)
        return self.problem_recorded,cube_to_attached_to__in_current_web_location
        
    
    
    
    
    def generate_blender_commands_problem_tree_sub(self,problem_name_key,action_listtt):
         """ self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}"""
         import copy
         self.action_listttt=action_listtt
         action_listtt2=copy.deepcopy(action_listtt)
         #print(f"action list: {action_listtt}")
         # find intital cube to attach to of the proibelm being solved
         cube_to_attach_to_name,cube_to_attached_to__in_current_web_location=self.find_intital_cube_to_attach_to_in_current_web_problem_tree(problem_name_key)
         current_cube_location=cube_to_attached_to__in_current_web_location
         for i82, action in zip(range(len(action_listtt2)),action_listtt2):
             shortened_action_name=action[13:]
             shortened_action_name=shortened_action_name[:20]
             # use the placement of the cube we determined witht he inttial placement function for first go
             possible_cube_placement_list=self.generate_spacing_list_around_cube_problem_tree(current_cube_location)  
             current_cube_location=self.find_where_to_place_cube_in_blender(possible_cube_placement_list)
             self.upload_blender_cube_and_text(current_cube_location,action,problem_treee=True,shortened_action_name=shortened_action_name)
             self.upload_blender_cube_edge_connection(action,cube_to_attach_to_name,cube_to_attached_to__in_current_web_location,current_cube_location,problem_treee=True)
             cube_to_attach_to_name=action
             self.used_object_name_list.append(action)

         #if cube_to_attach_to_name==self.problem_recorded:
                 #shortened_problem_name=problem_name_key[13:]
                 #shortened_problem_name=shortened_problem_name[:20]
                 #print(shortened_problem_name)
                 #possible_cube_placement_list=self.generate_spacing_list_around_cube(cube_to_attached_to__in_current_web_location)
                 #current_cube_location=self.find_where_to_place_cube_in_blender(current_cube_location=cube_to_attached_to__in_current_web_location)# fix this
                 #self.upload_blender_cube_and_text(current_cube_location,problem_name_key,problem_treee=True,shortened_action_name=shortened_problem_name)
                 
                 #self.upload_blender_cube_edge_connection(problem_name_key,cube_to_attach_to_name,cube_to_attached_to__in_current_web_location,current_cube_location,problem_treee=True)
                 #self.used_object_name_list.append(problem_name_key)
                 #cube_to_attach_to_name=problem_name_key
                 #possible_cube_placement_list=self.generate_spacing_list_around_cube_problem_tree(cube_to_attached_to__in_current_web_location)

                 
             
             
         #else:
         #    current_cube_location=cube_to_attached_to__in_current_web_location
         #    cube_to_attach_to_name=problem_name_key


        
                 # use intital attachement location and then iterate on rest
             # find how to attach subseqent cubes
             # change for where to attach and then 
             # reuse old algo
             #print(f"action list: {action_listtt}")
             #current_cube_location=self.find_where_to_place_cube_in_blender_problem_tree(possible_cube_placement_list)

   
                
             
    def generate_blender_commands_problem_tree_2(self):
        """ """
        import copy
        self.problem_tree_problem_strat_list_action_list_dictionary=self.upload_blender_problem_tree_data_from_sql()# creates self qualtity dictionary as welll
        self.blender_problem_tree_dictionary={} # leaving as blender problem web dictionary to avoiud other problems
        self.range_cube_distance_list_generation_value=6# test changing this
        self.used_square_location_list=[]
        self.used_objectt_list=[]
        saved_edge_locaiton_list=[]
        # this delete adds to command str to delete allitems currently in the scene
        self.blender_command_str_list=[]
        edge_value_tuple=(0,1)
        self.blender_command_str_list.append(f"import bpy, bmesh\nfaces = []\nname = 'Text Color'\ntext_from_cube_distance=2\nfor ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() ")
        self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
        self.blender_command_str_list.append(f'\nmaterial = bpy.data.materials.new(name+"_material")')
        self.blender_command_str_list.append(f'\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)')
        self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
        self.blender_command_str_list.append("\ncol_name='Collection'")
        self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")       
        # create color material for text
        
        # upload an intital cube named after the problem as root to blender command list
        current_cube_location=(0,0,0)
        self.upload_blender_cube_and_text(current_cube_location,self.problem_recorded,problem_treee=True,shortened_action_name=self.problem_recorded[10:])
        self.used_object_name_list.append(self.problem_recorded)
        # upload intital problem to blender and add to problem dicitonary
        # end state== cubes are added and connected to an existing strategy
        # rather than added from zero sort of like with problem web
        for i3, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary.items()):
            for action_listt in strategy_list:
                self.generate_blender_commands_problem_tree_sub(problem_name_key,action_listt)
        
 
    
        
     
        
     
        
     
            
        
        
        
        
        
        
        
        
    def generate_blender_commands_problem_tree(self):
        """ """
        import copy
        self.problem_tree_problem_strat_list_action_list_dictionary=self.upload_blender_problem_tree_data_from_sql()# creates self qualtity dictionary as welll
        self.blender_problem_tree_dictionary={} # leaving as blender problem web dictionary to avoiud other problems
        self.range_cube_distance_list_generation_value=6# test changing this
        self.used_square_location_list=[]
        self.used_objectt_list=[]
        saved_edge_locaiton_list=[]
        # this delete adds to command str to delete allitems currently in the scene
        self.blender_command_str_list=[]
        self.blender_command_str_list.append("import bpy, bmesh\nfor ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() ")
        self.blender_command_str_list.append("\nedges_list = [{edge_value_tuple}]")
        
        # create color material for text
        
        # upload an intital cube named after the problem as root to blender command list
        current_cube_location=(0,0,0)
        self.upload_blender_cube_and_text(current_cube_location,self.problem_recorded,problem_treee=True,shortened_action_name=self.problem_recorded[10:])
        # upload intital problem to blender and add to problem dicitonary
        # end state== cubes are added and connected to an existing strategy
        # rather than added from zero sort of like with problem web
        self.problem_tree_problem_strat_list_action_list_dictionary2=copy.deepcopy(self.problem_tree_problem_strat_list_action_list_dictionary)
        
        
        
        
        
        
        
        for i, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary2.items()):
            for i6, action_listt in enumerate(strategy_list):
                for i2,actionnnn in enumerate(action_listt):
                    self.problem_tree_problem_strat_list_action_list_dictionary[problem_name_key][i6][i2]=f"{i2}: {actionnnn}"    
        
        for i3, (problem_name_key,strategy_list) in enumerate(self.problem_tree_problem_strat_list_action_list_dictionary.items()):
            for action_listt in strategy_list:
                self.generate_blender_commands_problem_tree_sub(action_listt)

                
 
    
 
 
    
    ### Blender web functions
    def upload_blender_cube_and_text(self,cube_location,intital_cube_text,problem_treee=False,shortened_action_name=""):
        """ create cube and store information in blender problem dictionary"""
         #self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}
        ### clear selection
        #self.blender_command_str+="\nfor obj in bpy.data.collections['MonkeyCollect'].all_objects:"
        #self.blender_command_str+=f"\n obj.select_set(False)"
        ## data storage part
        if problem_treee==False:
            text_from_cube_distance=2
            #self.blender_command_str_list.append("\nimport bpy, bmesh")
            self.blender_command_str_list.append(f"\ncube=bpy.ops.mesh.primitive_cube_add(location={cube_location})")
            self.blender_command_str_list.append(f"\nbpy.data.objects['Cube.001'].name='{intital_cube_text}_cube'")
            #self.blender_command_str_list.append("\ntext_from_cube_distance=2")
            self.blender_command_str_list.append('\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")')
            self.blender_command_str_list.append(f'\nmyFontOb = bpy.data.objects.new("{intital_cube_text}",myFontCurve,)')
            self.blender_command_str_list.append(f'\nmyFontOb.data.body = "{intital_cube_text}"')
            self.blender_command_str_list.append('\nbpy.context.collection.objects.link(myFontOb)')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].location.x = {cube_location[0]+text_from_cube_distance}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].location.y = {cube_location[1]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].location.z = {cube_location[2]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{intital_cube_text}"].rotation_euler[0] = 1.5')
            #self.blender_command_str_list.append('\nname = "Text Color"')
            self.blender_command_str_list.append('\nmyFontCurve.materials.append(material)')


            self.used_square_location_list.append(cube_location)
            self.blender_problem_web_dictionary[intital_cube_text]={"current_cube_location":cube_location}
            self.blender_problem_web_dictionary[intital_cube_text]["edge_information"]={}
            
        if problem_treee==True:
            text_from_cube_distance=2
            self.blender_command_str_list.append("\nimport bpy, bmesh")
            self.blender_command_str_list.append(f"\ncube=bpy.ops.mesh.primitive_cube_add(location={cube_location})")
            self.blender_command_str_list.append(f"\nbpy.data.objects['Cube.001'].name='{intital_cube_text}_cube'")
            self.blender_command_str_list.append("\ntext_from_cube_distance=2")
            self.blender_command_str_list.append('\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")')
            self.blender_command_str_list.append(f'\nmyFontOb = bpy.data.objects.new("{shortened_action_name}",myFontCurve,)')
            self.blender_command_str_list.append(f'\nmyFontOb.data.body = "{intital_cube_text}"')
            self.blender_command_str_list.append('\nbpy.context.collection.objects.link(myFontOb)')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].location.x = {cube_location[0]+text_from_cube_distance}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].location.y = {cube_location[1]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].location.z = {cube_location[2]}')
            self.blender_command_str_list.append(f'\nbpy.data.objects["{shortened_action_name}"].rotation_euler[0] = 1.5')
            self.blender_command_str_list.append('\nname = "Text Color"')
            self.blender_command_str_list.append('\nmaterial = bpy.data.materials.new(name+"_material")')
            self.blender_command_str_list.append('\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)')
            self.blender_command_str_list.append('\nmyFontCurve.materials.append(material)')
            self.used_square_location_list.append(cube_location)
            self.blender_problem_tree_dictionary[intital_cube_text]={"current_cube_location":cube_location}
            self.blender_problem_tree_dictionary[intital_cube_text]["edge_information"]={}





            #self.blender_command_str+="\nimport bpy, bmesh"
            #self.blender_command_str+=f"\ncube=bpy.ops.mesh.primitive_cube_add(location={cube_location})"
            #self.blender_command_str+=f"\nbpy.data.objects['Cube.001'].name='{shortened_action_name}_cube'"
            #self.blender_command_str+="\ntext_from_cube_distance=2"
            ##### LEAVE THIS
            # now get text to work
            #self.blender_command_str+='\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")'
            
            

            
            #self.blender_command_str+=f'\nmyFontOb = bpy.data.objects.new("{shortened_action_name}",myFontCurve,)'


            #self.blender_command_str+=f'\nmyFontOb.data.body = "{intital_cube_text}"'
            #self.blender_command_str+='\nbpy.context.collection.objects.link(myFontOb)'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].location.x = {cube_location[0]+text_from_cube_distance}'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].location.y = {cube_location[1]}'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].location.z = {cube_location[2]}'
            #self.blender_command_str+=f'\nbpy.data.objects["{shortened_action_name}"].rotation_euler[0] = 1.5'
            
            
            
            # add color to the text
            #self.blender_command_str+='\nname = "Text Color"'
            #self.blender_command_str+='\nmaterial = bpy.data.materials.new(name+"_material")'
            #self.blender_command_str+='\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)'
            #self.blender_command_str+='\nmyFontCurve.materials.append(material)'
            #self.blender_command_str+='\nmyFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")'

            
            #name = "Poly Line"
            #material = bpy.data.materials.new(name+"_material")
            #material.diffuse_color = (10.0,2.0,0.0,10.0)
            #myFontCurve.materials.append(material)
            #myFontCurve.bevel_depth = 0.2


            #bpy.context.object.rotation_euler[0] = 0.401426

            
            
        
        
        # deselect all objects
       

        #self.blender_command_str+="\n "

        #for obj in bpy.context.selected_objects:
        #for obj in bpy.data.collections['MonkeyCollect'].all_objects:
        #    obj.select_set(False)
                
        #self.blender_command_str+=f"\n bpy.data.objects[obj].select = False"

        # PROBLEM YTOMORROW FIND WAY TO ADD CUBE IN SO CAN NAME IT

        #bpy.data.objects["Cube.001"].name="haha"
        #self.blender_command_str+=f"\nbpy.data.objects[-2].name='{intital_cube_text}'"

        
        #new_obj = bpy.data.objects.new('new_obj', None) 
        #new_obj.location = (x[index],y[index],z[index])
        #bpy.context.scene.objects.link(new_obj)
        #object = bpy.data.objects.get('OldName')
        
        #self.blender_command_str+=f"\nobject = bpy.data.objects.get('Cube.001')"
        #self.blender_command_str+=f"\nobject.name = '{intital_cube_text}'"
        #self.blender_command_str+=f"\nobject.location = {cube_location}"


        
        #self.blender_command_str+=f"\ncube = bpy.context.selected_objects[0]"
        #self.blender_command_str+=f"\ncube.name = '{intital_cube_text}'"
        ####
        
        
        #for obj in bpy.data.collections['MonkeyCollect'].all_objects:
        #    obj.select_set(False)
        #self.blender_command_str+="\nfor obj in bpy.context.selected_objects:"
        #self.blender_command_str+=f"\n bpy.data.objects[obj].select = False"
        #self.blender_command_str+=f"\nbpy.data.objects['{intital_cube_text}'].select = False"

        
        
        #self.blender_command_str+="\nimport bpy, bmesh"
        #self.blender_command_str+=f"\nbpy.ops.mesh.primitive_cube_add()"
        #self.blender_command_str+=f"\ncube = bpy.context.selected_objects[-1]"
        #self.blender_command_str+=f"\ncube.name = '{intital_cube_text}'"
        #self.blender_command_str+=f"\ncube.location = {cube_location}"


        
        
        #cube = bpy.context.selected_objects[0]
        #cube.name = "MyLittleCube

        
        
        
        ### super important do not erase this!
        #import bpy, bmesh
        #bpy.ops.mesh.primitive_cube_add(location=cube_location)
        #text_from_cube_distance=2
        #bpy.ops.object.text_add(location=(x+text_from_cube_distance,y,z))
        #ob=bpy.context.object
        #ob.data.body = object_text
        #self.blender_command_str+="\nbpy.ops.object.text_add(location=(x+text_from_cube_distance,y,z))"
        #self.blender_command_str+="\nob=bpy.context.object"
        #self.blender_command_str+=f"\nob.data.body = '{intital_cube_text}'"
    def upload_blender_cube_edge_connection(self,intital_cube_text,attached_cube_text,intital_cube_location,attached_cube_location,problem_treee=False):
        """record_names of lines in blender problem dcitionary created to modify later to show effects of actions """
         #self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}
         ## upload to blender part
        # need to deal with
        
        # data storage part
        edge_value_tuple=(0,1)
        if problem_treee==False:
            #self.blender_command_str_list.append("\nimport bpy, bmesh")
            #self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
            self.blender_command_str_list.append(f"\nvertices_list=[{intital_cube_location},{attached_cube_location}]")
            #self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
            #self.blender_command_str_list.append("\nfaces = []")
            self.blender_command_str_list.append("\nnew_mesh = bpy.data.meshes.new('new_mesh')")
            self.blender_command_str_list.append("\nnew_mesh.from_pydata(vertices_list, edges_list, faces)")
            #self.blender_command_str_list.append("\nnew_mesh.update()")
            self.blender_command_str_list.append(f"\nnew_line = bpy.data.objects.new(f'edge', new_mesh)")
            #self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")
            self.blender_command_str_list.append("\ncol.objects.link(new_line)")
            self.blender_problem_web_dictionary[intital_cube_text]["edge_information"][attached_cube_text]={"edge_object_name":f'edge{intital_cube_text}:::{attached_cube_text}',"intital_cube_text":intital_cube_text, "attached_cube_text":attached_cube_text,"intital_cube_location":intital_cube_location,"attached_cube_location":attached_cube_location}
        if problem_treee==True:
            self.blender_command_str_list.append("\nimport bpy, bmesh")
            self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
            self.blender_command_str_list.append(f"\nvertices_list=[{intital_cube_location},{attached_cube_location}]")
            self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
            self.blender_command_str_list.append("\nfaces = []")
            self.blender_command_str_list.append("\nnew_mesh = bpy.data.meshes.new('new_mesh')")
            self.blender_command_str_list.append("\nnew_mesh.from_pydata(vertices_list, edges_list, faces)")
            self.blender_command_str_list.append("\nnew_mesh.update()")
            self.blender_command_str_list.append(f"\nnew_line = bpy.data.objects.new(f'edge{intital_cube_text}:::{attached_cube_text}', new_mesh)")
            self.blender_command_str_list.append("\ncol_name='Collection'")
            self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")
            self.blender_command_str_list.append("\ncol.objects.link(new_line)")
            self.blender_problem_tree_dictionary[intital_cube_text]["edge_information"][attached_cube_text]={"edge_object_name":f'edge{intital_cube_text}:::{attached_cube_text}',"intital_cube_text":intital_cube_text, "attached_cube_text":attached_cube_text,"intital_cube_location":intital_cube_location,"attached_cube_location":attached_cube_location}

            
            
            #self.blender_command_str+="\nimport bpy, bmesh"
            #self.blender_command_str+="\nedge_value_tuple=(0,1)"
            #self.blender_command_str+=f"\nvertices_list=[{intital_cube_location},{attached_cube_location}]"
            #elf.blender_command_str+=f"\nedges_list = [{edge_value_tuple}]"
            #self.blender_command_str+="\nfaces = []"
            #self.blender_command_str+="\nnew_mesh = bpy.data.meshes.new('new_mesh')"
            #self.blender_command_str+="\nnew_mesh.from_pydata(vertices_list, edges_list, faces)"
            #self.blender_command_str+="\nnew_mesh.update()"
            #self.blender_command_str+=f"\nnew_line = bpy.data.objects.new(f'edge{intital_cube_text}:::{attached_cube_text}', new_mesh)"
            #self.blender_command_str+="\ncol_name='Collection'"
            #self.blender_command_str+="\ncol = bpy.data.collections.get(col_name)"
            #self.blender_command_str+="\ncol.objects.link(new_line)"
            
            # add color STILL NEED TO FIGURE OUT HOW TO GIVE MESH COLO%
            #self.blender_command_str+='\nname = "Text Color"'
            #self.blender_command_str+='\nmaterial = bpy.data.materials.new(name+"_material")'
            #self.blender_command_str+='\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)'
            #self.blender_command_str+='\nnew_mesh.materials.append(material)'
            
  
            
            
            

            
        #### this is super important do not erase this
        #import bpy, bmesh
        #edge_value_tuple=(0,1)# this connect the first and second vertics in the list  line vertices list
        #vertices_list=[intital_cube_placement,current_cube_location]
        #edges_list = [edge_value_tuple]# numbers refer to the vertice location in the list i think
        #faces = []
        #new_mesh = bpy.data.meshes.new('new_mesh')
        #new_mesh.from_pydata(line_vertices, edges_list, faces)
        #new_mesh.update()
        #new_line = bpy.data.objects.new(f'edge{i}', new_mesh)
        #col_name="Collection"
        #col = bpy.data.collections.get(col_name)  
        #col.objects.link(new_line) # this links to an existing collection
    def genereate_blender_node_and_edge_lists(self,amount_of_node_to_displayed=1000,effects_web=False,methods_problem_recorded="",strategy_list=[]):# amount of node displayed is to deal with overloading blender
        """use auto problem table here instead now """
        import re
        import copy
        import time
        self.node_qualitity_dictionary={}
        time_qualitity_found =time.time()
        node_counter=0
        if effects_web==True:
            self.problem_recorded=methods_problem_recorded
            # may need to change this not keep same problem
            print('EFFECT WEB')
            print(methods_problem_recorded)
            print(strategy_list)
            self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{methods_problem_recorded}';""")
            problem_objects_and_qualtity_list= self.cur.fetchall()
            self.strategy_recorded
            for i16,objecttt in enumerate(problem_objects_and_qualtity_list):
                specific_problem_or_object= objecttt[0]
                qualitity_list= objecttt[1]
                #print('obect and qual')
                #print(specific_problem_or_object)
                #print(qualitity_list)
                if specific_problem_or_object==self.problem_recorded:# need to make sure add intital probelm and qualtites
                    print(qualitity_list)
                    if qualitity_list:
                        qualitity_list=re.split(",",qualitity_list[1:-1])
                        
                    self.node_qualitity_dictionary[specific_problem_or_object]=[]  
                    for i10, qualityy2 in enumerate(qualitity_list):# limiting to 10 for now add more as necessary
                        node_counter+=1
                        if qualityy2 in self.node_qualitity_dictionary[specific_problem_or_object]:
                            continue
                        else:
                            self.node_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   
                    continue  
                for actionnn in strategy_list:
                    if specific_problem_or_object not in actionnn:
                        continue
                    else:
                        #print("object found in action")
                        #print(specific_problem_or_object)
                        #print(actionnn)
                        #if node_counter>=amount_of_node_to_displayed:# need to test this
                        #    break
                        if qualitity_list:
                            qualitity_list=re.split(",",qualitity_list[1:-1])
                        if specific_problem_or_object not in self.node_qualitity_dictionary:
                            node_counter+=1
                            self.node_qualitity_dictionary[specific_problem_or_object]=[]  
                        for i10, qualityy2 in enumerate(qualitity_list[:20]):# limiting to 10 for now add more as necessary
                            node_counter+=1
                            if qualityy2 in self.node_qualitity_dictionary[specific_problem_or_object]:
                                continue
                            else:
                                self.node_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   
                        break
                    
                        

            
        if effects_web==False:# starting from probelm recorded
            print(f"problem recroded {self.problem_recorded}")
            #?? how do i improve the problem solving program'
            # add intital problem object when creating objects for auto_problem_table
            self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM auto_problem_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
            problem_objects_and_qualtity_list= self.cur.fetchall()
            #print(problem_objects_and_qualtity_list)
            # what now
            for i16,objecttt in enumerate(problem_objects_and_qualtity_list):
                print(node_counter)

                if node_counter>=amount_of_node_to_displayed:
                    break
                specific_problem_or_object= objecttt[0]
                qualitity_list= objecttt[1]
                node_counter+=1 # objectt
                if qualitity_list:
                    qualitity_list=re.split(",",qualitity_list[1:-1])
                if specific_problem_or_object not in self.node_qualitity_dictionary:
                    self.node_qualitity_dictionary[specific_problem_or_object]=[]  
                for i10, qualityy2 in enumerate(qualitity_list):
                    node_counter+=1
                    #qualitityy=qualityy2[1]
                    if qualityy2 in self.node_qualitity_dictionary[specific_problem_or_object]:
                        continue
                    else:
                        self.node_qualitity_dictionary[specific_problem_or_object].append(qualityy2)   
            
        
        print(self.node_qualitity_dictionary)
        return self.node_qualitity_dictionary
    def generate_spacing_list_around_cube(self,current_cube_location):
        """ this list will be used as guidance to place other cubes around intital cube"""
        import random
        #rand_list=[]
        #n=10
        #for i in range(n):
        #    rand_list.append(random.randint(3,9))
        #print(rand_list)
        self.possible_cube_placement_list=[]
        current_x=current_cube_location[0]
        current_y=current_cube_location[1]
        current_z=current_cube_location[2]
        x_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        y_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        z_range_list=list(range(-self.range_cube_distance_list_generation_value,self.range_cube_distance_list_generation_value,3))# -10 to 10
        for x_coridinate in x_range_list:
            for y_coridinate in y_range_list:
                for z_coridinate in z_range_list:
                    possible_future_x=current_x+x_coridinate
                    possible_future_y=current_y+y_coridinate
                    possible_future_z=current_z+z_coridinate
                    self.possible_cube_placement_list.append((possible_future_x,possible_future_y,possible_future_z))
                            
        random.shuffle(self.possible_cube_placement_list) 
        return self.possible_cube_placement_list
    
    # THESE TWO FUNCTION NEED TO WORK ON  
    def find_where_to_place_cube_in_blender(self,current_cube_location=[0,0,0]):
        """ this will take the possible cube placement list and select a value that works from it
        NEED TO TEST THIS to these if recursion works here"""
        #print(possible_cube_placement_list)
        for i21, cube_placement in enumerate(self.possible_cube_placement_list):
            if cube_placement not in self.used_square_location_list:
                current_cube_location=cube_placement   
                break
            if i21==len(self.possible_cube_placement_list)-1:# this is in case that there is not enough space in the list of positions to place objects    #and this will create more space
                self.range_cube_distance_list_generation_value+=10
                self.possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)
                current_cube_location=self.find_where_to_place_cube_in_blender() # this should recurse is necessary
                return current_cube_location
            
            
        return current_cube_location
    
    def find_which_cube_to_attach_to_in_current_web(self,objecttt,qualtity_list):
        """figure out how and where to connect """
        cube_to_attached_to__in_current_web_location=None
        for intital_cube_text in self.blender_problem_web_dictionary.keys():
            intital_cube_location=self.blender_problem_web_dictionary[intital_cube_text]["current_cube_location"]
            if objecttt == intital_cube_text:
                cube_to_attached_to__in_current_web_location=intital_cube_location# need to change these names  
                break
                
           
        if cube_to_attached_to__in_current_web_location:
            return objecttt, cube_to_attached_to__in_current_web_location 
        else:
            intital_cube_location=self.blender_problem_web_dictionary[self.problem_recorded]["current_cube_location"]
            cube_to_attached_to__in_current_web_location=(0,0,0)
            return self.problem_recorded,cube_to_attached_to__in_current_web_location
        
        
        #intital_cube_text=edge_cube_names[intital_cube_text]["edge_information"]["intital_cube_text"]
        #current_cube_text=edge_cube_names[intital_cube_text]["edge_information"]["current_cube_text"]
        #intital_cube_location=self.blender_problem_web_dictionary[edge_cube_names][intital_cube_text]["edge_information"]["intital_cube_location"]
        #current_cube_location=edge_cube_names[intital_cube_text]["edge_information"]["current_cube_location"]
        # need to create blender dicitonary
        # have to create blender problem web dicitonary first
        #self.blender_problem_web_dictionary[intital_cube_text]={"current_cube_location":cube_location}
        #self.blender_problem_web_dictionary[intital_cube_text]["edge_information"][edge_cube_text]={"intital_cube_text":intital_cube_text, "current_cube_text":current_cube_text,"intital_cube_location":intital_cube_location,"current_cube_location":current_cube_location}
        
        #existing_cube_location=blender_problem_web_dictionary[cube_to_attach_to_text]["current_cube_location"]
        
        
       # for existing_cube_text in blender_problem_web_dictionary.keys():
        #    existing_cube_location=blender_problem_web_dictionary[objecttt]["current_cube_location"]
        #    
         #   blender_problem_web_dictionary[existing_cube_text]["edge_information"]
          #  self.node_qualitity_dictionary()
            

        
        #cube_location=blender_problem_web_dictionary[current_objecttt]["current_cube_location"]
        # connect to the first cube that it would be a qualtity, and if no qualtity then just connect to og problem web
        # eventually need to add connections to the proper cubes though        
        # if no match found

    def upload_objectts_and_qual_to_blenderr_and_modify_blender_problem_dictionary(self,objecttt,qualtity_list):
         """ self.blender_problem_web_dictionary={objectt name : {objectt_name:cube_name,{qual:edge_name}}"""
         
         if objecttt==self.problem_recorded:# this is hte root of the web
             current_cube_location=(0,0,0)
             self.upload_blender_cube_and_text(current_cube_location,objecttt)
             self.used_object_name_list.append(objecttt)
             
         if objecttt in self.used_object_name_list:
             print('hi')
             cube_to_attach_to_name,current_cube_location=self.find_which_cube_to_attach_to_in_current_web(objecttt,qualtity_list)
             
         else:
             cube_to_attach_to_name=self.problem_recorded
             cube_to_attached_to__in_current_web_location=(0,0,0)
             self.possible_cube_placement_list=self.generate_spacing_list_around_cube(cube_to_attached_to__in_current_web_location)
             current_cube_location=self.find_where_to_place_cube_in_blender()
             self.upload_blender_cube_and_text(current_cube_location,objecttt)
             self.upload_blender_cube_edge_connection(cube_to_attach_to_name,objecttt,cube_to_attached_to__in_current_web_location,current_cube_location)
             self.used_object_name_list.append(objecttt)
             edge_str=f"{cube_to_attach_to_name}:{objecttt}"
             self.used_edge_name_list.append(edge_str)

   
         for qualitityy in qualtity_list:
             if qualitityy in self.used_object_name_list:
                 #print('meow')
                 edge_str=f"{objecttt}:{qualitityy}"
                 edge_str_reverse=f"{qualitityy}:{objecttt}"
                 cube_to_attach_to_name,qual_cube_location=self.find_which_cube_to_attach_to_in_current_web(qualitityy,qualtity_list)
                 self.upload_blender_cube_edge_connection(objecttt,qualitityy,current_cube_location,qual_cube_location)
                 self.used_edge_name_list.append(edge_str)
                 if edge_str_reverse in self.used_edge_name_list:# check if edge in blender already exists
                     print('hio')
                     continue
                 
 
             else:
                 self.possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)
                 qual_cube_location=self.find_where_to_place_cube_in_blender(current_cube_location=current_cube_location)
                 self.upload_blender_cube_and_text(qual_cube_location,qualitityy)
                 self.upload_blender_cube_edge_connection(objecttt,qualitityy,current_cube_location,qual_cube_location)
                 self.used_object_name_list.append(qualitityy)
                 edge_str=f"{objecttt}:{qualitityy}"
                 self.used_edge_name_list.append(edge_str)
      
                 
             #print(qualitityy)
             #edge_str_reverse=f"{qualitityy}:{objecttt}"
             #if edge_str_reverse in self.used_edge_name_list:# check if edge in blender already exists
             #    print('hio')
             #    continue
             #if edge_str in self.used_edge_name_list:
             #    print('hio')
             #    continue
             #else:
             
            
    def generate_blender_commands_problem_web(self, effects_web=False,methods_problem_recorded="",strategy_list=[]):
        """ """
        #self.problem_recorded=problem_recorded
        print(f" problemee {self.problem_recorded}")
        self.node_qualitity_dictionary=self.genereate_blender_node_and_edge_lists(amount_of_node_to_displayed=100,effects_web=effects_web,methods_problem_recorded=methods_problem_recorded,strategy_list=strategy_list)# creates self qualtity dictionary as welll
        #import bpy, bmesh
        #from random import randint
        #used_object_list=[]
        self.blender_problem_web_dictionary={}
        self.range_cube_distance_list_generation_value=6# test changing this
        current_cube_location=(0,0,0)
        #self.possible_cube_placement_list=self.generate_spacing_list_around_cube(current_cube_location)#
        self.used_square_location_list=[]
        self.used_object_name_list=[]
        self.used_edge_name_list=[]
        saved_edge_locaiton_list=[]
        # this delete adds to command str to delete allitems currently in the scene
        self.blender_command_str_list=[]
        edge_value_tuple=(0,1)
        self.blender_command_str_list.append(f"import bpy, bmesh\nfaces = []\nname = 'Text Color'\ntext_from_cube_distance=2\nfor ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() ")
        self.blender_command_str_list.append("\nedge_value_tuple=(0,1)")
        self.blender_command_str_list.append(f'\nmaterial = bpy.data.materials.new(name+"_material")')
        self.blender_command_str_list.append(f'\nmaterial.diffuse_color = (10.0,2.0,0.0,10.0)')
        self.blender_command_str_list.append(f"\nedges_list = [{edge_value_tuple}]")
        self.blender_command_str_list.append("\ncol_name='Collection'")

        self.blender_command_str_list.append("\ncol = bpy.data.collections.get(col_name)")

        
        
        # upload intital problem to blender and add to problem dicitonary
        intital_problem_qualtity_list=self.node_qualitity_dictionary[self.problem_recorded]
        print(intital_problem_qualtity_list)
        self.upload_objectts_and_qual_to_blenderr_and_modify_blender_problem_dictionary(self.problem_recorded,intital_problem_qualtity_list)
        for i, (objectt,qualitity_list) in enumerate(self.node_qualitity_dictionary.items()):
            if objectt==self.problem_recorded:
                continue
            print(i)
            #print(objectt)
            #print(qualitity_list)
            self.upload_objectts_and_qual_to_blenderr_and_modify_blender_problem_dictionary(objectt,qualitity_list)
            #remove all used values
            #for i21, cube_placement in enumerate(self.possible_cube_placement_list):
            #    if cube_placement not in self.used_square_location_list:
            #        self.possible_cube_placement_list=self.possible_cube_placement_list[i21:]
            #        break
                    
            
            
        
        # run this as a script basically in blender
        #intital_cube_problem_location=(0,0,0)
        #for ob in bpy.data.objects:
        #    print(ob.name)
        #    ob.select_set(True)
        #    bpy.ops.object.delete()     
    
        
    def execute_blender_command_list(self):
           """ """
           import pyautogui
           import pyperclip
           import time
           #self.blender_command_str="for ob in bpy.data.objects:\n print(ob.name)\n ob.select_set(True)\n bpy.ops.object.delete() "
           self.blender_command_str="".join(self.blender_command_str_list)
           print(len(self.blender_command_str_list))
           pyperclip.copy(self.blender_command_str)
           pyautogui.hotkey("ctrl","v")
           pyautogui.press("enter")
           pyautogui.press("enter")

           
           #pyperclip.copy(rf"filename = r'{python_script_name}'")
           #pyautogui.hotkey("ctrl","v")
           #pyautogui.press("enter")
           ## copy the problem to clipboard
           #pyperclip.copy(rf"problem_name = {self.problem_recorded}")
           #pyautogui.hotkey("ctrl","v")
           #pyautogui.press("enter")
           # run a script
           #time.sleep(0.5)
           #pyautogui.write("exec(compile(open(filename).read(), filename, 'exec'))")
           #pyautogui.press("enter")
           #exec(compile(open(filename).read(), filename, 'exec'))
           #pyperclip.copy(r"\\nexec(compile(open(filename).read(), filename, 'exec'))")
           #pyautogui.hotkey("ctrl","v")
           #pyautogui.press("enter")     
     # get the data problem tree dic and problem web dic
     # perform necessary operations on each object generate the web
     # placing it in the blender file accordingly
        
    def generate_and_open_blender_problem_web_and_tree(self,event):
        """ press 3 on first listbox  to generate problem tree and web DONE"""
        # run this externally?
        from multiprocessing import Process
        import sys
        sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\tkinyer')
        #People in their 40s, what’s something people in their 20s don’t realize is going to affect them when they age?
        # going to affect them when they age
        #from Problems_functions import problems_functions
        #from Problems_functions import methods_window_program
        from generate_and_open_blender_problem_web_and_tree import generate_and_open_blender_problem_web_and_tree_functions
        #from problem_solving_project_gui_10 import buttons_per_quadrant
        #buttons=buttons_per_quadrant()
        self.problem_recorded=window.selection_get()
        genn_blend_functions=generate_and_open_blender_problem_web_and_tree_functions()
        process = Process(target=genn_blend_functions.generate_and_open_blender_problem_web_and_tree_f,args=(self.problem_recorded,))
        #process = Process(target=buttons.auto_create_problem_web_and_galaxy,args=(self.problem_recorded,))
        process.start()
        # generate web
        #self.open_blender()
        #self.get_access_to_blender_terminal()
        #self.generate_blender_commands_problem_web()
        #self.execute_blender_command_list()
        #problem_web_script=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Building\tkinyer_building\genereate_problem_web.py"
        #self.execute_command_to_execute_python_script(problem_web_script)

        
        # generate tree
        #self.open_blender()
        #self.get_access_to_blender_terminal()
        #self.generate_blender_commands_problem_tree_2()
        #self.execute_blender_command_list()
        
       

        #self.execute_command_to_execute_python_script()
        ### add these following ones to a script to execute
        #self.generate_and_open_blender_problem_web_and_tree_sub_script()
        #self.generate_blender_problem_tree()
        #self.generate_blender_problem_web()
        #self.open_blender_problem_web()
        #self.open_blender_problem_tree()
        
    def check_for_template(self,template_location):
        """we will save the screenshot to disk and then upload it using cv2 imread """
        import cv2
        import numpy as np
        import pyautogui
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
        screenshot.save(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png")
        img_rgb = cv2.imread(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\automating_coding\pyautogui_files\screenshot.png")
        template = cv2.imread(template_location)
        h, w = template.shape[:-1] # get the first two dimensions
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)# match the tewmplate against the image to find all images # the matching formula we are using is tm coeff normed it basically miinus two matrix to see differences # and then norms them
        threshold = .9 # threshold amount of match of image on other image in this case 90
        location_of_template = np.where(res >= threshold) # this gets us any point that has a .9 or above
        return location_of_template ,h, w 
         
    def wait_till_template_present(self,template_path):
         import pyautogui
         import time
         from PIL import ImageGrab
         import numpy as np
         import pytesseract
         try:
             while True:
              time.sleep(1)
              #pyautogui.click(1700, 971)# this will un highlight a button this is the problem because it moves the cursor
              template_present_value,h, w=self.check_for_template(template_path)
              print(template_present_value)
              if template_present_value[0].any():
               pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))           
               break
              else:
               continue
             time.sleep(0.25)
         
         except:
            input("input here and move to next click needed so skip buttons that screw parts of script up so no restart")
            
    def click_button_once_found(self,template_path):
          """ """
          import pyautogui
          import time
          from PIL import ImageGrab
          import numpy as np
          import pytesseract
          while True:
           pyautogui.click(1700, 971)
           pyautogui.scroll(-1000)
           template_present_value,h, w=self.check_for_template(template_path)#template
           print(template_present_value)
           if template_present_value[0].any():
            pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
            template_present_value,h, w=self.check_for_template(template_path)#template
            if template_present_value[0].any():
                pyautogui.click(int(template_present_value[1][0]+w/2),int(template_present_value[0][0]+h/2))
                break
            else:
                break
           else:
            continue      
        
    def show_effects_of_strategy_in_problem_web(self):
         """ change color of the edges associated with certain objects in problem web"""
         self.blender_problem_web_dictionary[intital_cube_text]={"cube_location":cube_location}
         self.blender_problem_web_dictionary[intital_cube_text]["edge_information"][edge_cube_text]={"intital_cube_text":intital_cube_text, "current_cube_text":current_cube_text,"intital_cube_location":intital_cube_location,"current_cube_location":current_cube_location}\
    
    def upload_blender_problem_tree_data_from_sql_method_window(self):
        """ """
        import re
        import copy
        import time
        self.temp_all_strategy_action_list_dictionary={}
        
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table ;""")
        all_strategy_table_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(all_strategy_table_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if problem_being_solved==self.problem_recorded:
                continue# this ensures that we accdinteally double up
            if action_list:
                action_list=re.split(",",action_list[1:-1])
            if problem_being_solved not in self.temp_all_strategy_action_list_dictionary:
                self.temp_all_strategy_action_list_dictionary[problem_being_solved]=[] 
            self.temp_all_strategy_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available  
        #
        
        # repeat this process recursing each action
        # as deep as necessary until certain there are no other strategies witht hat aciton name
        # in the given tree
        self.problem_tree_problem_strat_list_action_list_dictionary={}
        time_qualitity_found =time.time()
        self.cur.execute(f"""SELECT problem_being_solved,actions FROM strategy_table WHERE problem_being_solved = '{self.problem_recorded}';""")
        specific_problem_action_list_data= self.cur.fetchall()
        for i16,objecttt in enumerate(specific_problem_action_list_data):
            problem_being_solved= objecttt[0]
            action_list= objecttt[1] 
            if action_list:
                action_list=re.split(",",action_list[1:-1])
            if problem_being_solved not in self.problem_tree_problem_strat_list_action_list_dictionary:
                self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved]=[] 
            self.problem_tree_problem_strat_list_action_list_dictionary[problem_being_solved].append(action_list)# list of list of strats available 
            if action_list:
                action_list_list2=[]
                action_list_list2.append(action_list)
                while True: 
                    if action_list_list2==[]:
                        break
                    action_list_list=action_list_list2
                    action_list_list2=[]
                    for action_listtt in action_list_list:
                        for actionnn in action_listtt:
                            print('ACTION LIST')
                            print(action_listtt)
                            print('ACTION ')
                            # make it so that
                            # it adds to the intital strat line block as seperate tree

                            print(actionnn)
                            if actionnn in self.temp_all_strategy_action_list_dictionary:# check if problem key for the action
                                if actionnn not in self.problem_tree_problem_strat_list_action_list_dictionary:
                                    self.problem_tree_problem_strat_list_action_list_dictionary[actionnn]=[] 
                                action_list2=self.temp_all_strategy_action_list_dictionary[actionnn]
                                if action_list2:
                                    for actionn_mini_list in action_list2:
                                        print(actionn_mini_list)
                                        self.problem_tree_problem_strat_list_action_list_dictionary[actionnn].append(actionn_mini_list)# list of list of strats available 
                                        action_list_list2.append(actionn_mini_list)
                                
                            
        #[problem]=[strats[actions]]
        # first get all sub actions
        # then with this list check through other strategy
        # data and if they have sub trees add these in as
        # strats below these strats
        # find sub strategy trees
        # repeat this process as necessary
        # because could be multiple trees deep
        print(self.temp_all_strategy_action_list_dictionary)
        print(self.problem_tree_problem_strat_list_action_list_dictionary)
        return self.problem_tree_problem_strat_list_action_list_dictionary
        # broader principles guding action are in methods table
        #actual actiosn are in strategies table
        #self.cur.execute(f"""SELECT specific_problem_or_object,qualitity_list FROM methods_table WHERE problem_question_or_task = '{self.problem_recorded}';""")
        #methods_info= self.cur.fetchall()                                    
                                        
         
    
    
   
         
                                              
          
                                              
          
                                              
    
         
    
    
    
        
    def generate_and_open_blender_problem_web_and_tree_f(self,problem_recorded):
        """ """
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.problem_recorded=problem_recorded
        # generate web
        self.open_blender()
        self.get_access_to_blender_terminal()
        self.generate_blender_commands_problem_web()
        self.execute_blender_command_list()
        #problem_web_script=r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\problem_solving_project\Building\tkinyer_building\genereate_problem_web.py"
        #self.execute_command_to_execute_python_script(problem_web_script)

        
        # generate tree
        self.open_blender()
        self.get_access_to_blender_terminal()
        self.generate_blender_commands_problem_tree_2()
        self.execute_blender_command_list()
    def generate_blender_effect_problem_web_for_strat_and_problem_tree_f(self,problem_recorded,strategy_recorded):
        import re
        import psycopg2
        self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
        self.cur = self.conn.cursor()
        self.strategy_recorded=strategy_recorded
        self.problem_recorded=problem_recorded
        
        self.strategy_recorded_list=re.split(",",self.strategy_recorded[1:-1])
        print('hi')
        self.open_blender()
        self.get_access_to_blender_terminal()
        self.generate_blender_commands_problem_web(effects_web=True,methods_problem_recorded=self.problem_recorded,strategy_list=self.strategy_recorded_list)
        self.execute_blender_command_list()
        
        # generate tree will modify tree to display mutliple levels next
        self.open_blender()
        self.get_access_to_blender_terminal()
        self.generate_blender_commands_problem_tree_2()
        self.execute_blender_command_list()
        
        

        
    
        
    