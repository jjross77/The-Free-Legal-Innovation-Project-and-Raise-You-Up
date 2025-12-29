# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 12:10:09 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
def generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_for_different_objectives(self,problemmm,user_positional_info_dic,objective="help the most people"):
    """use personal info to generate life dag and sort on objective
    try to figure out best actions you can take for each specific objective 
    like to make the most money help most people or both
    make problem tree and problem  web clickable 
    make problem web into chess board think edward snowden surveillnce how goverment set up there stuff
    suggest different simialr problems using database search
    display methods related to problem and possible methods
    when open problem solving program open life dag and problem web empty file
    have button to change to specific problem
    may want to use the other algorhim we cameup with at one point
    to figure out all actions you coudl take for things in your life
    """ 
    # get sub step data from life problem dic to  generate a answer here
    example=[{"problem_being_solved":"life_position",
                               "strat_delimiter":'strat_delimiter',
                               "step_delimiter":'step_delimiter',
                               "task":"action",                         
                               "effects":"effects",
                               "typee":"objective"}]   
    import psycopg2
    self.conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
    self.cur = self.conn.cursor()
    print('''WE ARE USING THE SUB STEP DATA for an action
          in the guide_person_positional_info_dic_with_action  
          list sub_steps_to_complete_actions in order to suggest sub steps
          for an action and sorting using some critera
          ''')
    user_positional_info_dic["current_problem"]=problemmm
    sorted_problem_dags_dic_list=self.search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(self.all_guide_life_action_list_with_effects_dic,user_positional_info_dic,objective,search_type="life_dag",problem_search=problemmm)
    print('may need to change back to life dag at one point')

    #sorted_problem_dags_dic_list=self.search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved(self.all_guide_life_action_list_with_effects_dic,user_positional_info_dic,objective,search_type="life_dag",problem_search=problemmm)
    
    ### may need ot modify this        
    return sorted_problem_dags_dic_list
    
    
    
if search_type=="problem":
    #problemm=user_positional_info_dic["problem"]
    problemmm=user_positional_info_dic["current_problem"]
    # use this to rank life_action_list in respect of objective give it a score
    problemm_score=self.create_document_similarity_score(problemmm,life_action,typee="problem_search")
    guide_person_life_action_list_score=self.create_document_similarity_score(guide_person_personal_info,obejctive_doc,typee="get_guides_life_action_list_score_for_objective")
    user_personal_info_score=self.create_document_similarity_score(user_positional_info_context,obejctive_doc,typee="get_user_perosnal_info_score_for_objective")
    user_compared_to_guide_score=self.create_document_similarity_score(user_positional_info_context,guide_person_personal_info,typee="get_user_perosnal_info_score_for_guide_personal_info")
    action_with_respect_to_objective_score=self.create_document_similarity_score(life_action_context,obejctive_doc,typee="get_action_list_score_for_objective")
    print('''are you learning to to build or use a new method process or physical thing, 
          if yes look at all physical things processes that currently exist in this area and as many other areas
          as you can and reverse engineer as many as you can  but only look at  the best professitionals in 
          the fields ,   copy these and take these ideas to create a expert problem envrionment and either rebuild the 
          object or method or apply these ideas and build on top of them and synthesize them with other ideas 
          that you get from the  physcial things or methods that you look up to build better methods processes and physcial things ,
          for the problem glossary build glossary using glossary strategy and pattern strategy to generate ideas from these objects or processes 
          for problems which are strategy fifty six and thirty four  ''')
    self.consider_placement_of_other_people_places_and_things_when_choosing_action()
    weights = [14.424, 14.424, 14.421, 14.417,11.324]
    amount = [guide_person_life_action_list_score, user_personal_info_score, action_with_respect_to_objective_score,user_compared_to_guide_score]
    weighted_avg_score = np.average(amount, weights=weights)
    sorted_life_action_dic_for_objective[weighted_avg_score]=[life_action_list,effects,obejctive_doc] 