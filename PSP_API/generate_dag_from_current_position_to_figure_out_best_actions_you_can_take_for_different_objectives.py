# -*- coding: utf-8 -*-\nCreated on 2025-03-08 1741491446.7385254  @author: yyyyyyyyyyyyyyyyyyyy
if __name__ == '__main__':
 import sys
 sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api')
 from psp_search_function_api_functions import search_functions_gchild
 search=search_functions_gchild()
 table_name="guide_person_positional_info_with_action_info"
 user_positional_info_dic={

     "age":[],
      "height":[],
      "organization_or_human":[],

       "birth_date":[],
       "property":[],
       "personalty":[],
       "connections":[],
       "followers":[],
       "messages":[],
       "skills":[],           
       "work_experience":[],
       "degrees":[],
       "books_read":[],
       "marriage_status":[],
       "skills":[],
       "life_actions":[],
       "search_history":[],
       "assets":[],# like money etc
       "liaibities":[],
       "glasses":[],
       "race":[],
       "gender":[],
       "education":[],
       "friends_and_there_qualities":[],
       "employment_history":[],
       "photo":[],
       "pronouns":[],
       "email":[],
       "places_lived":[],#  geolocation as value
       "profile_photo":[],
       "photos":[],
       "licenses_certificates":[],
       "volunteering":[],
       "skills":[],
       "honours_and_awards":[],
       "interests":[],
       "groups":[],
       "newsletters":[],
       "about_paragraph":[],
       "projects_worked_on":[],
       "projects_interested_in":[],
       "personality_type":[],
       "family_members_and_family_members_qualities":[],
       "phone_info_phone_numbers_contacts":[],
       "other_social_media_info":[],
       "phone_info_phone_numbers_contacts":[],
       "pets":[],
       "animals":[],
       "plants":[],
       "buying_history":[],
       "selling_history":[],
       "financial_history":[],
       "profile_views_info":[],
       "people_who_searched_info":[],
       "physical_disability":[],
       "mental_disability":[],
       "religion":[],
       "web_search_history":[],
       "age":[],
       "record_of_offenses":[],
       "nationality":[],
       "income":[], }
 
 guide_person_positional_info_dic_with_action={
     "action":"",
     "generalized_action":[],
     "action_temporal_placement_in_life_list":1,
     "noun_and_verb_chunk_list":[],
     "noun_and_verb_chunk_pos_list":[],
     
     ### action qualities
     "user_time_past_use_of_action_list":[],
     "user_past_actions_list":[],
     "action_geo_locations":[],
     "time_to_complete_action":0,
     "other_losses":[],
     "object":[],
     "other_gains":[],
     "monetary_cost_of_action":0,
     "monetary_gain_of_action":0,
     "risk_of_failing":[],
     "expected_roi":[],
     "tools_needed":[],
     "legality":[],
     "tools_required_to_perform_action":[],
     "skills_required_to_perform_action":[],
     "resources_required_to_perform_action":[],
     "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
     "other_things_effected":[],
     "transformations":[], # that can be applied to action besides current 1
     "alternative_actions":[],
     "alternative_next_action_lists":[],
     "intital_page_text":[],

     "number_of_people_impacted":[],
     "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
     # run through all info in action dic to better choose actions


     "sub_steps_to_complete_actions":[] ,
     "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

     "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
     
     ### guide perosnal info qualities  during action 
     "organization_or_human":[],

     "age":[],
      "height":[],
       "birth_date":[],
       "property":[],
       "personalty":[],
       "connections":[],
       "followers":[],
       "messages":[],
       "skills":[],           
       "work_experience":[],
       "degrees":[],
       "books_read":[],
       "marriage_status":[],
       "skills":[],
       "life_actions":[],
       "search_history":[],
       "assets":[],# like money etc
       "liaibities":[],
       "glasses":[],
       "race":[],
       "gender":[],
       "education":[],
       "friends_and_there_qualities":[],
       "employment_history":[],
       "photo":[],
       "pronouns":[],
       "email":[],
       "places_lived":[],#  geolocation as value
       "profile_photo":[],
       "photos":[],
       "licenses_certificates":[],
       "volunteering":[],
       "skills":[],
       "honours_and_awards":[],
       "interests":[],
       "groups":[],
       "newsletters":[],
       "about_paragraph":[],
       "projects_worked_on":[],
       "projects_interested_in":[],
       "personality_type":[],
       "family_members_and_family_members_qualities":[],
       "phone_info_phone_numbers_contacts":[],
       "other_social_media_info":[],
       "phone_info_phone_numbers_contacts":[],
       "pets":[],
       "animals":[],
       "plants":[],
       "buying_history":[],
       "selling_history":[],
       "financial_history":[],
       "profile_views_info":[],
       "people_who_searched_info":[],
       "physical_disability":[],
       "mental_disability":[],
       "religion":[],
       "web_search_history":[],
       "age":[],
       "record_of_offenses":[],
       "nationality":[],
       "income":[],
       "link":[],
       }
 column_list=list(guide_person_positional_info_dic_with_action.keys())
 search.all_guide_life_action_list_with_effects_list_list=search.retrieve_data_from_local_database(table_name,"",column_list,testing=False)
 
 all_guide_life_action_list_with_effects_dic=search.process_sql_data_for_searches(search.all_guide_life_action_list_with_effects_list_list,column_list)     
 searched_life_dags_list_list=search.generate_dag_from_current_position_to_figure_out_best_actions_you_can_take_for_different_objectives(user_positional_info_dic,all_guide_life_action_list_with_effects_dic, objective="")#sort different best life dags by objective 

 input()
#search.generate_dag_from_current_position_to_figure_out_best_actions_you_can_take_for_different_objectives()
 # this is for testing web crawl and getting that to work
 #input()
 # iterate through selected actions on page divide into action lsits and speerate strategies using some filter function to order 
 #and sub divide action use htis for both main actions generated on a wiki page and sub action generated on other pages
#search_actions_using_various_objectives_like_amount_of_people_impacted_most_money_look_at_alternative_actions_effect_and_objects_involved



    