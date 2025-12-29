def process_crawl_data(self,sel_soup,person_comp_info_dic_with_action_list,intital_link):
        """ """
        import re
        import time
        import copy
        print(f"intital_link {intital_link}")
        person_comp_info_dic_with_action={         
            "action":"",
            
            "action_temporal_placement_in_life_list":"#",               
            ### action qualities
            "user_time_past_use_of_action_list":[],
            "user_past_actions_list":[],
            "action_geo_locations":[],
            "time_to_complete_action":0,
            "other_losses":[],
            "other_gains":[],
            "monetary_cost_of_action":0,
            "monetary_gain_of_action":0,
            "risk_of_failing":[],
            "expected_roi":[],
            "tools_needed":[],
            "legality":[],
            "action_objects":{},
            "number_of_people_impacted":[],
            "position_of_other_people_places_and_things":[],# consider other people places and things for counter actions
            # run through all info in action dic to better choose actions


            "tools_required_to_perform_action":[],
            "skills_required_to_perform_action":[],
            "resources_required_to_perform_action":[],# if dont have hte resources to take action need to add extra sub step to acquire them
            "location_needed_to_take_action":[],# default will be any but sometimes might be a country or a place or a city
            "other_things_effected":[],
            "transformations":[], # that can be applied to action besides current 1
            "alternative_actions":[],# super important because will allow us to see all alternatives and compare effects
            "alternative_next_action_lists":[],


            "sub_steps_to_complete_actions":[] ,
            "alternative_strategy_sub_step_lists_to_complete_actions":[] ,# figure out best strategy if possible

            "last_action_list":[] ,# like driving car would be big indicator of what shoudl do next
         # use concepts from different fileds to rank action
           # like in _allnce or engineering or law
           # sequentally go through each action in your head, look at factors/qualtities of actions
           #then assign a score for that action
           #then based on scored actions choose an action to take
            ### guide perosnal info qualities during action 
            "organization_or_human":[],
            "age":[],
             "height":[],
             "date":[],
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
              "money":[],
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
              "link":[], }
        #print(' make sure the first noun group/subject of sentence or pronoun is a person or organzaion if i do that im good or if atleast a proper noun is in the sentence ')
        #print('use qualtites from spacy in whatever way necessary to get best result so noun groups whatever works or using parsing trees')
        # edit the below at one point
        #print(' need to add in re patterns to search for if psosible for action sentneces to get better action sentences and if not do a neural net')
        #print('key is parsing action sentences let do it boys and do referential phrasing sentecnes and fix these')
        re_action_sentence_patterns_list=[".*",
            ]
        person_comp_info_dic_with_action_copy=copy.deepcopy(person_comp_info_dic_with_action)
        page_text=sel_soup.text
        doc = self.nlp(page_text) 
        #so alogrhim will go
        # check first noun chink
        # if noun chunk has person/org  or pronoun good 
        # else not action senetece unless
        # has a proper noun somewhere esle
        
        
        #for chunk in doc.noun_chunks:
        #    print(chunk.text, chunk.root.text, chunk.root.dep_,
        #            chunk.root.head.text)
        #for token in doc:
        #    print(token.text, token.dep_, token.head.text, token.head.pos_,
        #            [child for child in token.children])
            
            

        action_sentence=False 
        sentence_action_type_dic={}
        sentence=""
        counterr=0
        action_sentence_value="not action sentence"
        pos_list=[]
        pos_dic={}
        entity_text_dic={}
        #for token in doc:
        #    pos_dic.append({token.text:token.pos_})
        #    pos_list.append(token.pos_)
        for ent in doc.ents:
            #print(f"{ent.text},{ent.label_}")
            #print('hehe')
            textt=ent.text
            labell=ent.label_
            if " " in textt:
                textt_list=textt.split()
            else:
                textt_list=[textt]
            for textt in textt_list:
                if ent.label_ == "PERSON":
                    entity_text_dic[ent.text]="PERSON"
                if ent.label_ == "ORG":
                    entity_text_dic[ent.text] = "ORG"                
                if ent.label_ == "DATE":
                    entity_text_dic[ent.text] = "DATE"
                if ent.label_ == "MONEY":
                    entity_text_dic[ent.text] = "MONEY"         
                continue                
        for token in doc:
            #print(token.text, token.pos_)
            # if there is pronoun in sentence
            if token.text in entity_text_dic:
                token_label=entity_text_dic[token.text]
                if token_label=="PERSON" or token_label=="ORG":
                    if token.pos_=="PROPN" or token.pos_=="PRON":
                        action_sentence_value="action sentence"

            if sentence != "":
                sentence+=f" {token.text}"
            else:
                sentence=f"{token.text}"  
            #if token.text=="."  # may want to change back to this one
            if "." in token.text :# will need to test htis one
                if action_sentence_value=="action sentence":
                    for pattern in re_action_sentence_patterns_list:
                        result=re.search(pattern,sentence)
                        if result:
                            # need to remove footnotes
                            counterr+=1
                            # if scraper takes too long need to cancel it
                            #print('checking actions sentences gathered to improve process crawll data function')
                            #print(entity_text_dic)
                            sentence=re.sub(r"[\n\r]"," ",sentence)
                            sentence=re.sub(r"\s\s+","  ",sentence)
                            #sentence=sentence[:200]# may need to change this
                            sentence=sentence# may need to change this
                            #input(f"{sentence}")
                            person_comp_info_dic_with_action["action"]=sentence
                            person_comp_info_dic_with_action["action_temporal_placement_in_life_list"]=counterr
                            person_comp_info_dic_with_action["link"]=intital_link
                            person_comp_info_dic_with_action_list.append(person_comp_info_dic_with_action) 
                            # clear the dicitonary
                            person_comp_info_dic_with_action=copy.copy(person_comp_info_dic_with_action_copy)
                            break
                        else:
                            continue

                sentence="" 
                action_sentence_value="not action sentence"                           
            if token.pos_== "PRON":
                action_sentence_value="action sentence"
                # action sentence
                #action_sentence=True
                #print('hi')
                continue
       
        print(' add this function for sub action data  to get all action space self.OLD_generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_OLD()')
        print(' self.OLD_generate_problem_dag_from_current_position_figure_out_best_actions_you_can_take_OLD()')
        print(person_comp_info_dic_with_action_list)
        input()

        return person_comp_info_dic_with_action_list
    # will reduce down the pattern space soon
    # if can ge thtis to work can get sub action to work
    # patterns to exclude or patterns to exclude which is easier
    # maybe just identify subject verb object
    # and then accept all senteces which have a specfic object we want
    # if the subhect of the sentence is something wew ant keep the sentence
    # i want the subject of the sentence to be a  person or organizaion 
    # if i can get that pattern i am good
    
    # so figure out a way to identify that
    # so first couple words in sentence need to a organizaion or person
    # so the first noun group should be a person or organizaion
    
    
    # so figure out a way to do that
    #  noun_chunks_list = [chunk.text for chunk in doc.noun_chunks]
    # so in this noun chunk should be a person or orgnaizaion
    # if proper noun at end though its fine
    # BAD Articles are intended to consist primarily of prose , though they may contain some lists .
    #Fashion activism was coined by Celine Semaan.
    # good
    # BAD Science activism may include efforts to better communicate the benefits of science or ensure continued funding for scientific research
    # maybe just swap out noun group and it works
    #print(person_comp_info_dic_with_action_list)
    #input("hi my name is jeff")
    #print(token.text)
    #print(f"sentence: {sentence}")
    #print('meow')
                                        
                    #print('for pattern in re_action_sentence_patterns_list:')
                    #print('')
                    #print('')
                    #print('if action sentnece pattern not in pattern list continue')

    #page_line_list=page_text.splitlines()
    #code_chunk_end_line_number_list=[]
    #temp_code_lines_in_code_chunk=[]
    #temp_code_chunk=""
    #last_page_line_type="text"
    #for page_line_number,page_line_text in enumerate(page_line_list):
    #    non_space_match=re.search(non_space_matcher,page_line_text)