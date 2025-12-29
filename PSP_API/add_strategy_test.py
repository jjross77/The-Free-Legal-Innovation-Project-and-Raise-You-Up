# -*- coding: utf-8 -*-\nCreated on 2025-03-08 1741491446.7385254  @author: yyyyyyyyyyyyyyyyyyyy
if __name__ == '__main__':
 import sys
 sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\apis\psp_search_function_api\psp_search_function_api')
 from psp_search_function_api_functions import search_functions_gchild
 from psp_search_function_api_functions import search_functions_g2_child

 print("""for pos of a sentence do both noun chinks as seperate and use all words after the intital noun chunk as part of that noun chunk
       and then include a seperate noun chunk after that if it has a verb proceeding)""")
 search=search_functions_gchild()
 search_g=search_functions_g2_child()

 problemm=""
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
       "places_lived":[],
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
       "income":[]}
 typee="life"
 
 sorted_action_list=search_g.add_strategy(problemm,typee, user_positional_info_dic,objective="helping the most people")
 # this is for testing web crawl and getting that to work
 #input()

