from django.db import models
from django.db.models import Q
# Create your models here.

#general search tables
class schedule_pyautogui_script_searches(models.Model):
    """ j"""  
    script_name_search = models.CharField(max_length=20000)
    script_activation_time_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)

    computer_name= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
class generate_pyautogui_script_searches(models.Model):
    """ j"""  
    script_nam_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
class psp_search_api_searches(models.Model):
    """ j"""  
    psp_search = models.CharField(max_length=20000)
    type_of_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)
    def __str__(self):
        return self.name

###user tables  
class user_schedule_pyautogui_searches(models.Model):
    """ j"""  
    script_nam_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
class user_generate_pyautogui_searches(models.Model):
    """ j"""  
    psp_search = models.CharField(max_length=20000)
    type_of_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)
    def __str__(self):
        return self.name    
class user_api_searches(models.Model):
    """ j"""  
    script_name_search = models.CharField(max_length=20000)
    script_activation_time_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)

    computer_name= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
    
class user_page_searches(models.Model):
    """ j"""  
    page_name = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)

    computer_name= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
    
class user_strategy_table(models.Model):
    """ j"""  
    script_name_search = models.CharField(max_length=20000)
    script_activation_time_search = models.CharField(max_length=20000)
    search_time = models.CharField(max_length=20000)

    computer_name= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
    
### schedule_tables 
class user_schedule_task_table(models.Model):
    """ j"""  
    idd=models.CharField(max_length=20000,default="")
    problem_being_solved = models.CharField(max_length=20000)
    problem_tree_placement = models.CharField(max_length=20000)
    problem_id = models.CharField(max_length=20000)
    question_or_tool_for_strategy = models.CharField(max_length=20000)
    problem_web_variables = models.CharField(max_length=20000)
    transformations = models.CharField(max_length=20000)
    effects = models.CharField(max_length=20000)
    time_found = models.CharField(max_length=20000)
    actions = models.CharField(max_length=20000)
    objectives = models.CharField(max_length=20000)
    time= models.CharField(max_length=20000)
    date= models.CharField(max_length=20000)
    global_time=models.CharField(max_length=20000)
    user_info= models.CharField(max_length=20000)
    def __str__(self):
        return self.name

class schedule_task_table(models.Model):
    """ set this into the correct format so can instantly add it to calender"""  
    idd=models.CharField(max_length=20000,default="")
    profile_name=models.CharField(max_length=20000)
    problem_being_solved = models.CharField(max_length=20000)
    global_time= models.CharField(max_length=20000)
    time= models.CharField(max_length=20000)
    date= models.CharField(max_length=20000)
    last_notification_sent_time = models.CharField(max_length=20000)
    
    def __str__(self):
        return self.name  
    
### messages tables
class message_table(models.Model):
    """ j"""  
    idd=models.CharField(max_length=20000,default="")
    
    chat_name=models.CharField(max_length=20000,default="")
    user_messagining= models.CharField(max_length=20000)
    user_image = models.CharField(max_length=20000)
    message_content= models.CharField(max_length=20000)
    message_date= models.CharField(max_length=20000)
    message_time= models.CharField(max_length=20000)
    
    users_with_access_to_chat_list= models.CharField(max_length=20000)

    notification_sent_time = models.CharField(max_length=20000)
    


    
    def __str__(self):
        return self.name  
    
class profile_messages_table(models.Model):
    """ j""" 
    #thsi is for dealing with group chats
    profile_name=models.CharField(max_length=20000,default="")   
    users_with_access_to_chat_list= models.CharField(max_length=20000)
    chat_name=models.CharField(max_length=20000,default="")
    #chat name will be the name of the user
    chat_image = models.CharField(max_length=20000)
    chat_slogan = models.CharField(max_length=20000)   
    last_message_time= models.CharField(max_length=20000)
    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  
    
class connections_requests_history_table(models.Model):
    """ j"""  
    profile_requested=models.CharField(max_length=20000,default="")
    profile_requester=models.CharField(max_length=20000,default="")

    profile_image = models.CharField(max_length=20000)
    profile_slogan = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)
    

    global_time= models.CharField(max_length=20000)
    notification_sent = models.CharField(max_length=20000)

    def __str__(self):
        return self.name  
    
    
class connections_requests_table(models.Model):
    """ j"""  
    profile_requested=models.CharField(max_length=20000,default="")
    profile_requester=models.CharField(max_length=20000,default="")

    profile_image = models.CharField(max_length=20000)
    profile_slogan = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)
    

    global_time= models.CharField(max_length=20000)
    notification_sent_time = models.CharField(max_length=20000)

    def __str__(self):
        return self.name  
    
    
class similar_projects_connections_table(models.Model):
    """ j""" 
    similar_project_list=models.CharField(max_length=20000,default="")
    project_name=models.CharField(max_length=20000,default="")
    
    last_notification_sent_time=models.CharField(max_length=20000,default="")

    
    profile_image = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)
    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  
   
### profile content tables

class profile_notification_table(models.Model):
    """ j"""  
    profile_name=models.CharField(max_length=20000,default="")
    notification_title = models.CharField(max_length=20000)
    notification_content = models.CharField(max_length=20000)
    notification_link = models.CharField(max_length=20000)
    global_time= models.CharField(max_length=20000)
    post_notification_time= models.CharField(max_length=20000)

    def __str__(self):
        return self.name    

 
class profile_general_info_table(models.Model):
    """ j"""  
    profile_name=models.CharField(max_length=20000,default="")
    profile_image = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)
    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  

class personal_projects_table(models.Model):
    """ j"""  
    profile_name=models.CharField(max_length=20000,default="")
    profile_image = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)

    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  
class profile_group_projects_tables(models.Model):
    """ j"""  
    profile_name=models.CharField(max_length=20000,default="")
    profile_image = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)

    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  
class profile_photo_table(models.Model):
    """ j"""  
    profile_name=models.CharField(max_length=20000,default="")
    profile_image = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)

    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  
class profile_resume_table(models.Model):
    """ j"""  
    profile_name=models.CharField(max_length=20000,default="")
    profile_image = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)

    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name  

    
### general projects tables
class project_type_table(models.Model):
    """ j"""  
    idd=models.CharField(max_length=20000,default="")
    project_type_name = models.CharField(max_length=20000)
    project_type_image = models.CharField(max_length=20000)

    global_time= models.CharField(max_length=20000)
    def __str__(self):
        return self.name 
    
class project_schedule_table(models.Model):
    """ j""" 
    problem_being_solved = models.CharField(max_length=20000)
    project_name = models.CharField(max_length=20000)
    tools= models.CharField(max_length=20000)
    global_time= models.CharField(max_length=20000)
    time= models.CharField(max_length=20000)
    date= models.CharField(max_length=20000)
    last_edit_time= models.CharField(max_length=20000)
    last_edit_user= models.CharField(max_length=20000)
    last_notification_sent_time= models.CharField(max_length=20000)


    
    def __str__(self):
        return self.name

class projects_info_table(models.Model):
    """ j"""  
    project_name = models.CharField(max_length=20000)
    main_project_photo = models.CharField(max_length=20000)
    project_description = models.CharField(max_length=20000)
    other_project_photos = models.CharField(max_length=20000)
    users_on_project= models.CharField(max_length=20000)

    
    
class projects_files_table(models.Model):
    """ j"""  
    project_name = models.CharField(max_length=20000)
    project_file = models.CharField(max_length=20000)
    project_file_description = models.CharField(max_length=20000)
    def __str__(self):
        return self.name 
    



    






    
### other psp related tables    
class gui_script_table(models.Model):
    keyboard_or_mouse_list = models.CharField(max_length=400000)
    press_scroll_move_list = models.CharField(max_length=400000)
    timee_list= models.CharField(max_length=400000 )
    active_window_name_list= models.CharField(max_length=400000 )
    path_to_frame_list= models.CharField(max_length=400000 )
    spacing_to_add_list= models.CharField(max_length=400000)
    key_value_list= models.CharField(max_length=400000)
    active_window_url_list= models.CharField(max_length=400000)
    
    script_name= models.CharField(max_length=400000)
    computer_name= models.CharField(max_length=400000)
    other_associated_files= models.CharField(max_length=400000)
    script_description=models.CharField(max_length=400000)
    generated_or_not=models.CharField(max_length=400000)
    def __str__(self):
        return self.name
    
class task_info_table(models.Model):
    problem_being_solved = models.CharField(max_length=400000)
    document = models.CharField(max_length=400000)
    document_content= models.CharField(max_length=400000 )
    def __str__(self):
        return self.name
    
class related_task_table(models.Model):
    problem_being_solved= models.CharField(max_length=400000)
    related_task= models.CharField(max_length=400000)
    
class scheduled_pyautogui_scripts(models.Model):
    """ j"""  
    action_page_script_name = models.CharField(max_length=20000)
    time = models.CharField(max_length=20000)
    date = models.CharField(max_length=20000)
    script_activation_time = models.CharField(max_length=20000)
    computer_name= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
    
class pyautogui_other_computer_completed_generation_table(models.Model):
    """ j"""  
    idd=models.CharField(max_length=20000,default="")
    script_name = models.CharField(max_length=20000)
    timee = models.CharField(max_length=20000)
    computer_name= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
    
class pyautogui_page_action_table_2(models.Model):
    """ j"""  
    keyboard_or_mouse_list = models.CharField(max_length=400000)
    press_scroll_move_list = models.CharField(max_length=400000)
    timee_list= models.CharField(max_length=400000 )
    active_window_name_list= models.CharField(max_length=400000 )
    path_to_frame_list= models.CharField(max_length=400000 )
    spacing_to_add_list= models.CharField(max_length=400000)
    key_value_list= models.CharField(max_length=400000)
    active_window_url_list= models.CharField(max_length=400000)
    
    script_name= models.CharField(max_length=400000)
    computer_name= models.CharField(max_length=400000)
    other_associated_files= models.CharField(max_length=400000)
    def __str__(self):
        return self.name
class pyautogui_page_action_table_3(models.Model):
    """ j"""  
    keyboard_or_mouse_list = models.CharField(max_length=400000)
    press_scroll_move_list = models.CharField(max_length=400000)
    timee_list= models.CharField(max_length=400000 )
    active_window_name_list= models.CharField(max_length=400000 )
    path_to_frame_list= models.CharField(max_length=400000 )
    spacing_to_add_list= models.CharField(max_length=400000)
    key_value_list= models.CharField(max_length=400000)
    active_window_url_list= models.CharField(max_length=400000)
    
    script_name= models.CharField(max_length=400000)
    computer_name= models.CharField(max_length=400000)
    other_associated_files= models.CharField(max_length=400000)
    script_description=models.CharField(max_length=400000)
    def __str__(self):
        return self.name
    
    
class auto_problem_table(models.Model):
    """ j"""  
    idd=models.CharField(max_length=20000,default="")
    problem_question_or_task = models.CharField(max_length=20000)
    specific_problem_or_object = models.CharField(max_length=20000)
    tool_or_question_per_conn_list= models.CharField(max_length=20000 )
    qualitity_list= models.CharField(max_length=20000 )
    transformations= models.CharField(max_length=20000 )
    objectives= models.CharField(max_length=20000)
    time_created_conn= models.CharField(max_length=20000)
    initial_creation= models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    

class auto_strategy_table(models.Model):
    """ j"""
    idd=models.CharField(max_length=20000,default="")
     
    problem_being_solved = models.CharField(max_length=20000)
    problem_id = models.CharField(max_length=20000)
    question_or_tool_for_strategy = models.CharField(max_length=20000)
    problem_web_variables = models.CharField(max_length=20000)
    transformations = models.CharField(max_length=20000)
    effects = models.CharField(max_length=20000)
    objectts = models.CharField(max_length=20000)
    time_found = models.CharField(max_length=20000)
    actions = models.CharField(max_length=20000)
    problem_tree_placement = models.CharField(max_length=20000)
    def __str__(self):
        return self.name



class code_base_table(models.Model):
    """ j""" 
    idd=models.CharField(max_length=20000,default="")
    glossary_definiton = models.CharField(max_length=20000)
    line_of_code = models.CharField(max_length=20000)
    code_base_function = models.CharField(max_length=20000)
    code_file_name = models.CharField(max_length=20000)
    glossary_website = models.CharField(max_length=20000)
    class_name = models.CharField(max_length=20000)
    line_number_in_file = models.CharField(max_length=20000)
    commented_function = models.CharField(max_length=20000)
    docstring = models.CharField(max_length=20000)
    time_stamp = models.CharField(max_length=20000)
    glossary_definition_gpt = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    


class code_base_all_version_info(models.Model):
    """j """ 
    idd=models.CharField(max_length=20000,default="")
     
    glossary_definiton = models.CharField(max_length=20000)
    line_of_code = models.CharField(max_length=20000)
    code_base_function = models.CharField(max_length=20000)
    code_file_name = models.CharField(max_length=20000)
    glossary_website = models.CharField(max_length=20000)
    class_name = models.CharField(max_length=20000)
    line_number_in_file = models.CharField(max_length=20000)
    commented_function = models.CharField(max_length=20000)
    docstring = models.CharField(max_length=20000)
    time_stamp = models.CharField(max_length=20000)
    glossary_definition_gpt = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    


class ip_address_table_info_on_servers(models.Model):
    """j """ 
    idd=models.CharField(max_length=20000,default="")
     
    computer_name = models.CharField(max_length=20000)
    ip_number = models.CharField(max_length=20000)
    user_name = models.CharField(max_length=20000)
    computer_password = models.CharField(max_length=20000)
    dbnames = models.CharField(max_length=20000)
    tables_in_database = models.CharField(max_length=20000)
    data_base_password = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    


    
class galaxies_table(models.Model):
    """ j"""
    idd=models.CharField(max_length=20000,default="")
     
    problem_or_idea_root = models.CharField(max_length=20000)
    qualities = models.CharField(max_length=20000)
    tool_or_question_used_per_qualitity = models.CharField(max_length=20000)
    start_time = models.CharField(max_length=20000)
    finish_time = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    

    
    
class ideas(models.Model):
    """j """
    idd=models.CharField(max_length=20000,default="")
     
    date = models.CharField(max_length=20000)
    idea_number_group = models.CharField(max_length=20000)
    idea_category = models.CharField(max_length=20000)
    key_terms = models.CharField(max_length=20000)
    paragraph = models.CharField(max_length=20000)
    paragraph_number = models.CharField(max_length=20000)
    file_name = models.CharField(max_length=20000)
    directory = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    

 

class ideas2(models.Model):
    """j """ 
    idd=models.CharField(max_length=20000,default="")
     
    date = models.CharField(max_length=20000)
    idea_number_group = models.CharField(max_length=20000)
    idea_category = models.CharField(max_length=20000)
    key_terms = models.CharField(max_length=20000)
    paragraph = models.CharField(max_length=20000)
    paragraph_number = models.CharField(max_length=20000)
    file_name = models.CharField(max_length=20000)
    
    directory = models.CharField(max_length=20000)
    sentences = models.CharField(max_length=20000)
    pos = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    


class ideas_table_3(models.Model):
    """ j""" 
    idd=models.CharField(max_length=20000,default="")
     
    sentence = models.CharField(max_length=20000)
    paragraph = models.CharField(max_length=20000)
    paragraph_number = models.CharField(max_length=20000)
    file_name = models.CharField(max_length=20000)
    directory = models.CharField(max_length=20000)
    pos = models.CharField(max_length=20000)
    labels = models.CharField(max_length=20000)
    updated_label = models.CharField(max_length=20000)
    updated_sentence = models.CharField(max_length=20000)
    finish_time = models.CharField(max_length=20000)
    start_time = models.CharField(max_length=20000)
    
    
    


    
    
   
class labels_for_idea_program(models.Model):
    """ j"""
    idd=models.CharField(max_length=20000,default="")
    paragraph = models.CharField(max_length=20000)
    labels = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    
    
   

class labels_for_idea_program_2(models.Model):
    """ j"""  
    idd=models.CharField(max_length=20000,default="")
    paragraph = models.CharField(max_length=20000)
    paragraph_number = models.CharField(max_length=20000)
    file_name = models.CharField(max_length=20000)
    
    directory = models.CharField(max_length=20000)
    pos = models.CharField(max_length=20000)
    
    
    label = models.CharField(max_length=20000)
    
    
    sentence = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    
  
    
class problem_tree_table(models.Model):
    """j """
    idd=models.CharField(max_length=20000,default="")
     
    problem_being_solved = models.CharField(max_length=20000)
    problem_tree_placement = models.CharField(max_length=20000)


    problem_id = models.CharField(max_length=20000)
    question_or_tool_for_strategy = models.CharField(max_length=20000)
    problem_web_variables = models.CharField(max_length=20000)
    transformations = models.CharField(max_length=20000)
    effects = models.CharField(max_length=20000)
    time_found = models.CharField(max_length=20000)
    actions = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    
   
    
class problem_table(models.Model):
    """j """ 
    idd=models.CharField(max_length=20000,default="")
     
    problem_question_or_task = models.CharField(max_length=20000)
    specific_problem_or_object = models.CharField(max_length=20000)
    tool_or_question_per_conn_list= models.CharField(max_length=20000 )
    qualitity_list= models.CharField(max_length=20000 )
    objectives= models.CharField(max_length=20000)
    time_created_conn= models.CharField(max_length=20000)
    initial_creation= models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    
  


class prompt_table(models.Model):
    """j """
    idd=models.CharField(max_length=20000,default="")
    prompt = models.CharField(max_length=20000)
    prompt_type = models.CharField(max_length=20000)
    timee = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    

 
    
class methods_table(models.Model):
    """j """
    idd=models.CharField(max_length=20000,default="")
    problem_being_solved = models.CharField(max_length=20000)
    method_step = models.CharField(max_length=20000)
    question_or_tool_for_method = models.CharField(max_length=20000)
    ideas_from_web = models.CharField(max_length=20000)
    objectives_maxmized = models.CharField(max_length=20000)
    temporal_placement = models.CharField(max_length=20000)
    time_method_found = models.CharField(max_length=20000)
    strategy_action = models.CharField(max_length=20000)
    action_related_to_strategy = models.CharField(max_length=20000)    
    past_problem_connection = models.CharField(max_length=20000)
    problem_preventing_action = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    

class strategy_table(models.Model):
    """ j"""
    idd=models.CharField(max_length=20000,default="")
    problem_being_solved = models.CharField(max_length=20000)
    strat_delimiter=models.CharField(max_length=20000)
    step_delimiter=models.CharField(max_length=20000)
    problem_tree_placement = models.CharField(max_length=20000)
    problem_id = models.CharField(max_length=20000)
    question_or_tool_for_strategy = models.CharField(max_length=20000)
    problem_web_variables = models.CharField(max_length=20000)
    transformations = models.CharField(max_length=20000)
    effects = models.CharField(max_length=20000)
    time_found = models.CharField(max_length=20000)
    task = models.CharField(max_length=20000)
    typee = models.CharField(max_length=20000)
    def __str__(self):
        return self.name
    
    
   

class problem_solving_screen_recording_table(models.Model):
    idd=models.CharField(max_length=20000,default="")
    problem_question_or_task = models.CharField(max_length=20000)
    path_to_screenshot = models.CharField(max_length=20000)
    active_window_name= models.CharField(max_length=20000 )
    timee= models.CharField(max_length=20000 )
    def __str__(self):
        return self.name
    
    
    



       

