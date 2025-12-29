from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from django.shortcuts import render
#from .models import Case_Meta_Data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
import sys
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
#sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\psp_website\psp\tkinyer')
#sys.path.append(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Documents\Coding\psp_website\psp\auto_coding_psp\search_functions')

#from problem_solving_project_gui_website import buttons_per_quadrant

#from django.db.models import Q
from .extra_functions import extra_functions
from .extra_functions import extra_functions_child
from .extra_functions import extra_functions_gchild
from .extra_functions import extra_functions_g2_child

extra=extra_functions()
extra_c=extra_functions_child()
extra_g=extra_functions_gchild()
extra_g2=extra_functions_g2_child()

from .models import schedule_pyautogui_script_searches
from .models import generate_pyautogui_script_searches
from .models import psp_search_api_searches
from .models import user_page_searches
from .models import user_api_searches

from .models import scheduled_pyautogui_scripts
from .models import pyautogui_other_computer_completed_generation_table
from .models import pyautogui_page_action_table_2
from .models import pyautogui_page_action_table_3
from .models import schedule_task_table
from .models import task_info_table
from .models import related_task_table
from .models import gui_script_table


from .models import projects_info_table
from .models import projects_files_table
from .models import project_schedule_table
from .models import message_table
from .models import profile_messages_table
from .models import project_type_table
from .models import connections_requests_table
from .models import similar_projects_connections_table


from .models import profile_general_info_table
from .models import personal_projects_table
from .models import profile_photo_table
from .models import profile_resume_table

from .models import profile_notification_table

from .models import projects_files_table

from .models import auto_problem_table
from .models import auto_strategy_table
from .models import code_base_table
from .models import galaxies_table
from .models import ideas_table_3
from .models import problem_tree_table
from .models import problem_table
from .models import methods_table
from .models import strategy_table
from .models import problem_solving_screen_recording_table
from .models import prompt_table
#auto_problem_table
from django import forms
from django.views.generic import TemplateView

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
class HomePage(TemplateView):
    def search(request):
        print('hi') 
    def register(request):
          # Redirect to your home page or another desired page
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
    

        
    def website_name(request):
        # formating is table_name.column_in_models.item_type.objects.all
        # load last problem we were working on
        # need to onyl load relevent data to user so would look at user profile
        # then load applicable doing more speicfic searches data 
        #do this in the in future
        #?? how do i fix the current tables to have correct columns task info table sub task table related task
        #table current schedule table gui scheduled table gui scriptrs to scheudle
        #table gui_new_scripts_to_generate_table? ###kNzSoDvAdAsScNaMvCmF
        # translate these models into the format below
        ### user stuff
        import time
        search_time=time.time()
        username=""
        extra.current_task=""
        user_name=""
        password=""
        user_info=extra.get_user_info(user_name,password)
        if user_info:
            user_object = user_page_searches(username=username,search_time=search_time)  
            user_object.save()
            # use user info to upload correct values
            
            extra.current_task=""
            extra.task_info_list=[]
            extra.sub_task_list=[]
            extra.search_sort_based_on_user_info() 
            strategy_tablee = strategy_table.objects.all()
            for strategy_object in strategy_tablee:
                sub_task_list=[]
                problem_being_solved=strategy_object['problem_being_solved']
                strat_delimiter=strategy_object['strat_delimiter']
                step_delimiter=strategy_object['step_delimiter']
                actions=strategy_object['action']
                effects=strategy_object['effects']
                objectives=strategy_object['type']
                # parse result shere for different tables
                sub_task_list.append([problem_being_solved,actions.effects,objectives])
        else:
            #generic no login or user info
            extra.task_info_list_list=[["Search a task!","Search a task!","iterator_1","iterator_2"]]# leave these with a message because no repviosu login
            extra.task_info_list_list=[["Search a task!","Search a task!","iterator_1"]]# leave these with a message because no repviosu login

            #task_info_list=task_document, task_document_content
            extra.current_task=[["Search a Task!"]] # leave these with a message because no repviosu login
            extra.sub_task_list_list=[["Search a Task!","Search a Task!","Search a Task!","Search a Task!","Search a Task!","iterator","iterator"]] # leave these with a message because no repviosu login
            # sub_task_list=group,step,sub_task,effects,type# make step and group very small and under one column like 1.1 for step 1 of group 1

            #strategy_tablee = strategy_table.objects.all("problem_being_solved","actions","effects","objectives")
            sub_task_list=[]
            ### need ot figure out how to integrate this
            column_names_list=["Related_Task","",""]

            
            related_task_tablee = related_task_table.objects.values("problem_being_solved","related_task","id")

            related_task_list_list=[] 
            print(related_task_tablee)
            for i, related_task in enumerate(related_task_tablee):              
                problem_being_solved=related_task['problem_being_solved']
                related_taskk=related_task['related_task']
                idd=related_task['id']
                related_task_iterator=f"related_task:related_task:{idd}"
                row_task_iterator=f"row:related_task:{idd}"

                # parse result shere for different tables
                related_task_list_list.append([related_taskk,related_task_iterator,row_task_iterator])
                #related_task_list=related_task,sub_tasks,effects,type                
            related_task_list_list=related_task_list_list[:100]           
            # upload general website schedule
            scheduled_task_list_list=[] 
            #schedule_tablee = schedule_task_table.objects.all("problem_being_solved","time","date")           
            schedule_tablee = schedule_task_table.objects.values("problem_being_solved","time","date","global_time","id")
            schedule_tablee=extra.sort_scheduled_task_by_global_time(schedule_tablee)    

            #column_names_list=["Task","Date","Time","",""]
            if schedule_tablee:
                print('hi')
                print(schedule_tablee)
            else: 
                schedule_tablee=[]
                

            for i, scheduled_task in enumerate(schedule_tablee):
                problem_being_solved=scheduled_task['problem_being_solved']
                time=scheduled_task['time']
                date=scheduled_task['date']
                idd=scheduled_task["id"]
                task_scheduled_task_iterator=f"task:scheduled_task:{idd}"
                row_scheduled_task_iterator=f"row:scheduled_task:{idd}"

                scheduled_task_list_list.append([problem_being_solved,time,date, task_scheduled_task_iterator,
                 row_scheduled_task_iterator ])
                #current_schedule_list=task,sub_tasks,effects,type,time,date            
            #scheduled_pyautogui_scriptss = scheduled_pyautogui_scripts.objects.all()
                #scheduled_gui_script_list=gui_script_name, time,date
            #just check all the values  in row to avoid button issues
            #gui scripts to still generate and scripts generated
            gui_script_list_list=[]
            gui_script_tblee = gui_script_table.objects.values("script_name","script_description","id")
            for i3, gui_script in enumerate(gui_script_tblee):
                script_description=gui_script["script_description"]
                script_name=gui_script["script_name"]
                idd=gui_script["id"]
                scripts_iterator=f"script:scripts|:{idd}"
                scripts_iterator2=f"row:scripts|:{idd}"
                gui_script_list_list.append(script_name,script_description,scripts_iterator,scripts_iterator2)      
                

            
        ###create lists
        current_task=extra.current_task
        task_info_list=extra.task_info_list_list
        sub_task_list=extra.sub_task_list_list
        related_task_list=related_task_list_list
        current_schedule_list=scheduled_task_list_list
        gui_scripts_list=gui_script_list_list
        #example columns="""
        #current_task=current_task
        #task_info_list=task_document, task_document_content
        #sub_task_list=group,step,sub_task,effects,type# make step and group very small and under one column like 1.1 for step 1 of group 1
        #related_task_list=related_task,sub_tasks,effects,type
        #current_schedule_list=task,sub_tasks,effects,type,time,date
        #scheduled_gui_script_list=gui_script_name, time,date
        #gui_scripts_to_schedule_list=gui_script_name,script_description
        #scripts_to_generate_list=gui_script_name,script_description"""
        
        # note that type is the eqvualent of objectives
        table_info_dic = {"current_task":current_task,
        "task_info_list":task_info_list,
        "sub_task_list":sub_task_list,
        "related_task_list":related_task_list,
        "current_schedule_list":current_schedule_list,
        "gui_scripts_list":gui_scripts_list}
        return  render(request, 'website_name.html',table_info_dic) 
    def signup(request):
        #form_class = UserCreationForm
        #success_url = reverse_lazy("login")
        return render(request, 'signup.html') 
    
    def start_a_project(request):
        #form_class = UserCreationForm
        #success_url = reverse_lazy("login")
        return render(request, 'start_project.html') 
   
    def question_answered(request):
        # formating is table_name.column_in_models.item_type.objects.all
        # load last problem we were working on
        hehe=problem_table.objects.values_list('problem_question_or_task')
        table_name=""
        where_string=""
        #current_pyautogui_scripts_on_remote_server=search_g.retrieve_data_from_website_database(table_name,where_string)
        hehe=hehe[:10]
        hehe2=[]
        for problem in hehe:
            problem=problem[0]
            print(problem)

            hehe2.append(problem)
            
        iterator_list=[]
        table_list=["table_1"]
        table_name=table_list[0]
        for i in range(len(hehe2)):
            item_str=f"{i} {table_name}"
            iterator_list.append(item_str)
        mylist = zip(hehe2, iterator_list)
        context = {'mylist': mylist,}
        extra.problem_recorded=""
        print(extra.problem_recorded)

        base_view="hi"
        return  render(request, 'question_answered.html',context) 
    def get_persons(request):
        problem_list=problem_table.objects.values_list('problem_question_or_task')
        print(problem_list)
        print("filter the resutls here and upload only limited number of them using search")
        # filter results here
        person_list = [{'name': problem} for problem in problem_list]          
        return JsonResponse(person_list, safe=False) 

        
    
    ### finish these today! by 12 pm
    def return_profile_page(request,profile_name):
        #upload data
        if request.user.is_authenticated:
            #upload data
            profile_general_info_table_list = profile_general_info_table.objects.values("project_type_name","project_type_image")
            personal_projects_table_list = personal_projects_table.objects.values("project_name","main_project_photo","project_description","other_project_photos")
            profile_photo_table_list = profile_photo_table.objects.values("project_type_name","project_type_image")
            profile_resume_table_list = profile_resume_table.objects.values("project_name","main_project_photo","project_description","other_project_photos")
            #put into correct list dic format
            profile_info_dic={
                "profile_general_info_table_list":profile_general_info_table_list,
                "personal_projects_table_list":personal_projects_table_list,
                "profile_photo_table_list":profile_photo_table_list,
                "profile_resume_table_list":profile_resume_table_list,
                }
            profile_page_info_dic={'profile_info_list': profile_general_info_table_list}
            return  render(request, 'profile.html',profile_page_info_dic) 
        else:
            return render(request, 'registration/login.html') 
        #from .models import profile_general_info_table
        #from .models import personal_projects_table
        #from .models import profile_group_projects_table
        #from .models import profile_photo_table
        #from .models import profile_resume_table
    def create_project_page(request):
        print('meow')
    def edit_project_page(request):
        print('meow')
    def return_project_page(request,project_name):
        #upload_project related content        
        psp_info_dic=extra.load_in_psp_content()
        projects_info_table_list = projects_info_table.objects.get(title=project_name) 
        projects_files_table_list = projects_files_table.objects.get(title=project_name) 
        project_schedule_table_list = project_schedule_table.objects.get(title=project_name) 
        #projects_info_table_list
        projects_info_table_list_list=[]
        projects_additiona_photos_list_list=[]       
        # there should only be one entry so one time thoruh the loop here
        for i, projects_info in enumerate(projects_info_table_list):
            project_name=projects_info['project_name']
            main_project_photo=projects_info['main_project_photo']
            project_description=projects_info['project_description']
            other_project_photos=projects_info['other_project_photos']
            idd=projects_info["id"]
            task_scheduled_task_iterator=f"task:projects_info:{idd}"
            row_scheduled_task_iterator=f"row:projects_info:{idd}"
            projects_additiona_photos_list_list.append([project_name,
                                                  project_description,
                                                  main_project_photo,
                                                  row_scheduled_task_iterator ])
            # grab additonal photos we have saved on the project
            other_project_photos_list=other_project_photos.split(",")
            for other_photos in other_project_photos_list:
                projects_additiona_photos_list_list.append([other_photos])  
        #projects_files_table_list   
        projects_files_table_list_list=[]
        for i2, projects_files in enumerate(projects_files_table_list):
            project_name=projects_files['project_name']
            project_file=projects_files['project_file']
            project_file_description=projects_files['project_file_description']
            idd=projects_files["id"]
            task_scheduled_task_iterator=f"task:projects_files:{idd}"
            row_scheduled_task_iterator=f"row:projects_files:{idd}"
            projects_files_table_list_list.append([
                                                   project_file,
                                                   project_file_description,
                                                   task_scheduled_task_iterator,
                                                    ])   
        #project_schedule_table_list  
        project_schedule_table_list_list=[]
        for i3, project_schedule in enumerate(project_schedule_table_list):
            problem_being_solved=project_schedule['problem_being_solved']
            date=project_schedule['date']
            time=project_schedule['time']
            tools=project_schedule['tools']
            idd=project_schedule["id"]
            task_scheduled_task_iterator=f"task:project_schedule:{idd}"
            row_scheduled_task_iterator=f"row:project_schedule:{idd}"
            project_schedule_table_list_list.append([problem_being_solved,
                                                     date,
                                                     time,
                                                     tools,
                                                     task_scheduled_task_iterator,
                                                     row_scheduled_task_iterator ])
            
        #add to the file dic  the lists we created
        psp_info_dic["projects_info_table_list"]=projects_info_table_list
        psp_info_dic["projects_files_table_list"]=projects_files_table_list
        psp_info_dic["project_schedule_table_list"]=project_schedule_table_list_list
        psp_info_dic["projects_additiona_photos_list_list"]=projects_additiona_photos_list_list
        #upload_psp_page_related_info       
        return  render(request, 'project_page.html',psp_info_dic) 

    def contribute(request):
        #project catrgories
        #upload data
        upload_new_categories="true"# need to toggle this off at one point 
        if upload_new_categories=="true":
            project_type_table.objects.all().delete()
            extra.upload_project_categories_to_project_category_table()
            
        project_type_table_list = project_type_table.objects.values("project_type_name","project_type_image")
        projects_table_list = projects_info_table.objects.values("project_name","main_project_photo","project_description")
        projects_table_list=projects_table_list[:100]
        #put into correct list dic format

        contribute_info_dic={"project_type_list":project_type_table_list,
                             "projects_table_list":projects_table_list,}
        
        return  render(request, 'contribute.html', contribute_info_dic)
    
    
    
    def connect(request):
        #upload data
        # still need to figure out user stuff to get all these pages to work with users
        if request.user.is_authenticated:
            profile_name=""
            user_profile_info=""
            profile_name=""
            try:
                connections_requests_table_list=connections_requests_table.objects.get(profile_name=profile_name)
                similar_persons_connections_table_list = similar_projects_connections_table.objects.values("profile_name","profile_image","profile_slogan")
                relevent_connections_list=extra.find_relevent_connections(user_profile_info,similar_persons_connections_table_list)
            except connections_requests_table.DoesNotExist:
                pass
            #this is for testing
            connections_requests_table_list=[["s","s","s"],["s","s","s"]]
            relevent_connections_list=[["s","s","s"],["s","s","s"]]
            connect_info_dic={"connections_requests_table_list":connections_requests_table_list,
                              "similar_projects_connections_table_list":relevent_connections_list
                              }
            return  render(request, 'connect.html', connect_info_dic) 
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form}) 
    
    def notifications(request):
        #upload data
        if request.user.is_authenticated:
            profile_name=""
            user_profile_info=""
            profile_name=""
            try:
                profile_notification_table_list=profile_notification_table.objects.get(profile_name=profile_name)
            except profile_notification_table.DoesNotExist:
                pass
            #this is for testing
            profile_notification_table_list=[]
            profile_name=""
            #project_schedule_table_list  
            profile_notification_table_list_list=[]
            for i3, profile_notification in enumerate(profile_notification_table_list):
                notification_title=profile_notification['notification_title']
                notification_content=profile_notification['notification_content']
                notification_link=profile_notification['notification_link']
                idd=profile_notification["id"]
                task_scheduled_task_iterator=f"task:profile_notification:{idd}"
                row_scheduled_task_iterator=f"row:profile_notification:{idd}"
                profile_notification_table_list_list.append([notification_title,
                                                         notification_content,
                                                         notification_link,
                                                         task_scheduled_task_iterator])  
            #testing
            profile_notification_table_list_list=[["s","s","s","s"],["s","s","s","s"]]

            notifications_info_dic={"profile_notification_table_list":profile_notification_table_list_list}
            
            
            return render(request, 'notifications.html', notifications_info_dic) 
        
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form}) 
        
    def show_messages(request):
        delete_or_save_cell_value = request.GET.get('key1')
        column_text = request.GET.get('key2')
        current_task = request.GET.get('key3')
        
    def inbox(request):
        #upload data
        messages_table_to_generate_dynamically=""" for group chat messages
        make it so that users is a list that the program runs through
        in thed messages table so we can always add multiple users easily
        """
        messages_table_to_generate_dynamically="""<!-- messages_table -->
        <!-- occupy right side of screen -->
        <!-- load this in using javascript below is example -->
        <!-- example chat -->
        <h3 >Example chat to be generated dyanmically</h3>
        <div class="col-span-1 bg-blue-100 p-4 rounded-lg shadow-md">
              <table class="min-w-full table-auto border-collapse" id="profiles_messaged_table">
                <thead>
                  <tr class="bg-gray-200 text-gray-600">
                    <th class="px-6 py-3 text-left">Messages</th>
                  </tr>
                </thead>
                <tbody>
        {% for user_messagining, user_image,message_content,message_date,message_time, iterator1 in test_messages_table_list %}
                 <tr class="border-b border-gray-300 hover:bg-gray-100" onclick="show_messages()">
                  <td onclick="download_document()"  id='{{ profile_name }}' class="px-6 py-4">{{ profile_name }} </td>
                  <td class="px-6 py-4" > <img id="photo"class="text-lg font-semibold" src='{{ profile_image }}'></img> id='{{ iterator1 }}' </td>
                  <td onclick="download_document()"  id='{{ profile_name }}' class="px-6 py-4">{{ last_message }} </td>
                   <td onclick="download_document()"  id='{{ profile_name }}' class="px-6 py-4">{{ message_date }} </td>
                              <td onclick="download_document()"  id='{{ profile_name }}' class="px-6 py-4">{{ message_time }} </td>


                 </tr>
          {% endfor %}  """
        
        if request.user.is_authenticated:
            profile_messages_table_list=["","","","",""]
            sorted_profile_messages_table_list=["","","","",""]
            #message_table_list = message_table.objects.values("project_type_name")
            profile_name=""#get this from request eventually
            try:
                profile_messages_table_list=profile_messages_table.objects.get(profile_name=profile_name)
                sorted_profile_messages_table_list=extra.sort_profile_messages_by_date(profile_messages_table_list)
            except profile_messages_table.DoesNotExist:
                pass
            profile_messages_table_list=[["s","s","s","s","s"],["s","s","s","s","s"]]
            sorted_profile_messages_table_list=[["s","s","s","s","s"],["s","s","s","s","s"]]

            #profile_messages_table_list = profile_messages_table.objects.values("problem_being_solved","related_task","id")
            #put into correct list dic format
            test_messages_table_list=[["s","s","s","s"]]
            user_profile_info=""
            profile_name=""
            inbox_info_dic={"profile_messages_table_list":sorted_profile_messages_table_list,
                            "test_messages_table_list":test_messages_table_list}
            print('meow')

            print(inbox_info_dic)
            return  render(request, 'inbox.html', inbox_info_dic)
        
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form}) 
    def edit_profile(request):
        print('meow')
    def profile(request):  
        if request.user.is_authenticated:
            #upload data
            profile_general_info_table_list = profile_general_info_table.objects.values("project_type_name","project_type_image")
            personal_projects_table_list = personal_projects_table.objects.values("project_name","main_project_photo","project_description","other_project_photos")
            profile_photo_table_list = profile_photo_table.objects.values("project_type_name","project_type_image")
            profile_resume_table_list = profile_resume_table.objects.values("project_name","main_project_photo","project_description","other_project_photos")
            #put into correct list dic format
            profile_info_dic={
                "profile_general_info_table_list":profile_general_info_table_list,
                "personal_projects_table_list":personal_projects_table_list,
                "profile_photo_table_list":profile_photo_table_list,
                "profile_resume_table_list":profile_resume_table_list,
                }
            return  render(request, 'profile.html', profile_info_dic) 

        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form}) 
        
    def upload_month_data(request):
        import re
        current_year = request.GET.get('key1')
        current_month = request.GET.get('key2')
        import calendar
        import re
        number_day_name_dic={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
        from datetime import datetime
        schedule_task_date_list_dic={}
        current_year_month=f"{current_year},{current_month}"
        text_calendar = calendar.TextCalendar()
        text_calendar.setfirstweekday(calendar.SUNDAY)   
        num_days = calendar.monthrange(current_year, current_month)[1]
        #current_month_days = [str(datetime.date(current_year, current_month, day)+) for day in range(1, num_days+1)] 
        current_month_days=[]
        current_month_days_dic={}
        current_month_days_and_day_name=[]
        for day in text_calendar.itermonthdays2(current_year, current_month):
            day_in_month=day[0]          
            day_name=day[1]  
            current_month_day_date_time=str(datetime.date(current_year, current_month, day))
            current_month_days_dic[current_month_day_date_time]=[day_name,day_name]
        #upload data        
        
        schedule_task_table_list = schedule_task_table.objects.values("problem_being_solved","date","day_of_week","time","global_time")
        # match the task so it is grouped in a list with the date on calender    
        # group all the scheduled tasks on that date
        counterr=0
        for scheudled_task in schedule_task_table_list:
            if scheudled_task["date"] in current_month_days_dic:
                # fill in blanks for the month
                counterr+=1
                day_and_day_name=current_month_days_dic[scheudled_task["date"]]
                day_in_month=day_and_day_name[0]          
                day_name=day_and_day_name[1] 
                if day_in_month in schedule_task_date_list_dic:
                    schedule_task_date_list_dic[day_in_month][1].append(scheudled_task["problem_being_solved"])     
                else:
                    schedule_task_date_list_dic[day_in_month]=[day,[scheudled_task],scheudled_task["time"],day_name,counterr]

        #put into correct list dic format
        schedule_task_month_list= list(schedule_task_date_list_dic.values())
        schedule_info_dic = {
        'current_year_month':current_year_month,
        "schedule_task_month_list":schedule_task_month_list,
        }       
        return JsonResponse(schedule_task_month_list, safe=False)
    def generate_notifications(request):
        print('meow')
    
        
    def schedule(request):
        import calendar
        import re
        from datetime import datetime
        from datetime import date
        intital_fill_count=0
        number_day_name_dic={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
        number_month_name_dic={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

        schedule_task_date_list_dic={}
        final_schedule_list_list=[]
        current_month = datetime.now().month   
        current_year = datetime.now().year
        current_year_month=f"{current_year},{number_month_name_dic[current_month]}"
        text_calendar = calendar.TextCalendar()
        text_calendar.setfirstweekday(calendar.SUNDAY)   
        #num_days = calendar.monthrange(current_year, current_month)[1]
        #current_month_days = [str(datetime.date(current_year, current_month, day)+) for day in range(1, num_days+1)] 
        current_month_days=[]
        current_month_days_dic={}
        intital_fill_count=0
        current_month_days_and_day_name=[]
        current_month_days_dic["intital_filler"]=0
        schedule_task_table_list = schedule_task_table.objects.values("problem_being_solved","date","time","global_time")
        scheduled_task_dates_dic={}
        for scheudled_task in schedule_task_table_list:
            datee=scheudled_task["date"]
            problem_being_solved=scheudled_task["problem_being_solved"]
            timee=scheudled_task["time"]
            if  datee in scheduled_task_dates_dic:
                scheduled_task_dates_dic[datee].append([problem_being_solved,timee])
            else:
                scheduled_task_dates_dic[datee]=[[problem_being_solved,timee]]
       
        counterr=0
        for  day in text_calendar.itermonthdays2(current_year, current_month):
            counterr+=1           
            day_in_month=day[0]        
            day_name=day[1]  
            #print(type(day_in_month))
            #print(type(current_year))
            #print(type(current_month))
            if day_in_month==0:
                print('filler')
                intital_fill_count+=1
                # this keeps the columns oriented correctly
                current_month_days_dic["intital_filler"]=intital_fill_count
                final_schedule_list_list.append(["","","","",counterr])
            else:            
                current_month_day_date_time=str(date(current_year, current_month, day_in_month))
                if current_month_day_date_time in scheduled_task_dates_dic:
                    #get tasks info
                    print(scheduled_task_dates_dic)
                    print('meowww')
                    print(scheduled_task_dates_dic[current_month_day_date_time])

                    temp_scheduled_time_list=[]
                    temp_scheduled_task_list=[]
                    #=scheduled_task_dates_dic[current_month_day_date_time]
                    
                    for taskkkk in scheduled_task_dates_dic[current_month_day_date_time]:
                        print('hi')
                        print(taskkkk)

                        problem_being_solved=taskkkk[0]
                        time=taskkkk[1]
                        temp_scheduled_task_list.append(problem_being_solved)
                        temp_scheduled_time_list.append(time)
                    final_schedule_list_list.append([day_in_month,temp_scheduled_task_list,temp_scheduled_time_list,number_day_name_dic[day_name],counterr])
                else:
                    final_schedule_list_list.append([day_in_month,"","",number_day_name_dic[day_name],counterr])

                    
          
              
        #put into correct list dic format
        #schedule_task_month_list= list(schedule_task_date_list_dic.values())
        schedule_info_dic = {
        'current_year_month':current_year_month,
        "schedule_task_month_list":final_schedule_list_list,
        }
        return render(request, 'schedule.html',schedule_info_dic)

    ### this is the end of pages im working on today to get working
    def thrift(request):
        import calendar
        import re
        schedule_info_dic={}
        return render(request, 'thrift.html',schedule_info_dic)
        

    def modify_info(request):
        import re
        # will add this as a hyperlinks over the gui table
        # need to add id column to djnago and upload it correctly
        # need the actual id from database not a iterator
        #for the value
        table_column_dic={"task_info":["document","document_content"],
            "related_task":["related_task"],
                          "scheduled_task":["problem_being_solved","time","date"],
                          "sub_task":["step_delimiter","action","effects","type"],
                          "scheduled_scripts":["action_page_script_name","time","date"] }
        delete_or_save_cell_value = request.GET.get('key1')
        column_text = request.GET.get('key2')
        current_task = request.GET.get('key3')

        delete_or_save_cell_value_list=re.split(" ",delete_or_save_cell_value)
        delete_or_save=delete_or_save_cell_value_list[0]
        if delete_or_save=="Share":
            print('hi')
        if delete_or_save=="Share":
            print('hi')
        if delete_or_save=="Set Tool":
            print('use this to actually perform the task with an actual tool in the physical world in my house or actually perform the task on teh internet with gui or whatever')
            print('example tool will be the gui')
            print('example tool will be the ardunio board maker')


        if delete_or_save=="Share":
            print('hi')
            
        column_value=delete_or_save_cell_value_list[1]
        column_value_list=re.split(":",column_value)
        table_name=column_value_list[1]
        table_columns_name_dic=table_column_dic[table_name]
        #create_dic
        print(f'delete_or_save_cell_value_list{delete_or_save_cell_value_list}')
        print(f"column_value_list{column_value_list}")
        print(f"table_columns_name_dic{table_columns_name_dic}")
        print(f"table_name{table_name}")


        table_column_value_dic={}
        final_column_text_list=[]
        column_text_list=column_text.split("\t")
        print(f"column_text_list {column_text_list}")
        button_name_list=["save","delete","Share","Shared by","Connect"]
        for textt in column_text_list:
            if textt in button_name_list :
                continue
            else:
                final_column_text_list.append(textt) 
        print(f"final_column_text_list{final_column_text_list}")

        for i, column_text in enumerate(final_column_text_list):       
            table_column=table_columns_name_dic[i]
            table_column_value_dic[table_column]=column_text        
        print(delete_or_save_cell_value_list)
        print(f"table_column_value_dic{table_column_value_dic}")
        print(column_value_list)
        
        if delete_or_save=="delete":
            if table_name=="scheduled_task":
                print("s")
                record = schedule_task_table.objects.get(id=int(column_value_list[2]))
                record.delete() 
            if table_name=="related_task":
                record = related_task_table.objects.get(id=int(column_value_list[2]))
                record.delete() 
            if table_name=="scheduled_scripts":
                print("s")
                record = scheduled_pyautogui_scripts.objects.get(id=int(column_value_list[2]))
                record.delete() 
            if table_name=="task_info":
                print("s")
                record = task_info_table.objects.get(id=int(column_value_list[2]))
                record.delete() 
            if table_name=="sub_task":
                print("s")
                record = strategy_table.objects.get(id=int(column_value_list[2]))
                record.delete() 
                
                 
        if delete_or_save=="save":
            #record = schedule_task_table.objects.get(id=int(column_value_list[2]))
            #record.problem_being_solved = new_value # Replace new_value with the desired value
            if table_name=="scheduled_task":
                print("s")
                schedule_task_table.objects.filter(id=int(column_value_list[2])).update(**table_column_value_dic)

            if table_name=="related_task":
                print("s")
                related_task_table.objects.filter(id=int(column_value_list[2])).update(**table_column_value_dic)
            if table_name=="scheduled_scripts":
                print("s")
                scheduled_pyautogui_scripts.objects.filter(id=int(column_value_list[2])).update(**table_column_value_dic)
            if table_name=="task_info":
                print("s")
                task_info_table.objects.filter(id=int(column_value_list[2])).update(**table_column_value_dic)
            if table_name=="sub_task":
                print("s")
                record = strategy_table.objects.get(id=int(column_value_list[2]))
                record.delete() 
        print('update info on website')

        return HttpResponse("Thank you for your submission!")
        
    def perform_gui_script_action(request):
        # will add this as a hyperlinks over the gui table
        print('will add api here for psp')
        print("# will attach this view function to buttons  in generate table")
        import time
        script_name = request.GET.get('key1')
        if "schedule_pyautogui_script":
            # will add this as a hyperlinks over the gui table
            my_object = schedule_pyautogui_script_searches(script_name_search=psp_search, script_activation_time_search=activation_time,search_time=search_time)
            my_object.save()
            if user_info:
                user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
                user_object.save()    
            # execute the pyauogui commands
            sorted_scheduled_action_scripts=extra.schedule_pyautogui_action(psp_search,activation_time,activation_day)         
            #parse upload to add to tables
            schecudled_script_list=[{"table":"scheduled_script_table",
                                     "gui_script":sorted_scheduled_script["action_page_script_name"],
                                     "time":sorted_scheduled_script["time"],
                                     "date":sorted_scheduled_script["date"]}for sorted_scheduled_script in sorted_scheduled_action_scripts]
            return JsonResponse(schecudled_script_list, safe=False)
        
        if "generate_pyautogui_script" :
            my_object = generate_pyautogui_script_searches(script_nam_search=psp_search, search_time=search_time)
            my_object.save() 
            if user_info:
                user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
                user_object.save()               
            #execute_search
            gui_dic_list=extra.search_sort_gui_scripts(psp_search)
            # execute the pyauogui commands model this off of what is returned in scheudle pyautogui
            extra.generate_pyautogui_files_on_other_computers_from_big_black_using_website(gui_dic_list[0])         
            #parse upload to add to tables
            # just have single gui script table and have option to generate or execute for each script
            # just upload all scripts and if they still need to be generated add a button for this
            sorted_gui_script_list = [{"table":"gui_script_table",
                                "script_name":gui_script_info["script_name"],
                                "script_description":gui_script_info["script_description"],
                                "generated_or_not":gui_script_info["generated_or_not"],
                                } 
                               for gui_script_info in gui_dic_list]                
            # it is simply a list of dicitonaries where you can use the key values in a specific way
            #problem_list = [{"table":"updatetable1",'problem': problem} for problem in problem_list]
            return JsonResponse(sorted_gui_script_list, safe=False)          
   
    def set_current_task(request):
        from datetime import datetime
        import time
        import re
        global_time=time.time()
        today=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        date_time_list=re.split(" ", today)
        # add as hyperlink to set task on top of generayed set current task elements
        current_task = request.GET.get('key1')
        current_task_strats_dic_listt = strategy_table.objects.filter(problem_being_solved=current_task)
        task_info_listt=task_info_table.objects.filter(problem_being_solved=current_task)
        related_task_listt=related_task_table.objects.filter(problem_being_solved=current_task)       
        # store strategy table as indivdual actions
        # and then have extra columns corresponding to step and associed strat
        # convert into idnvidual strats and actions
        # only add problem to scheudle not all the other info  
        my_object = schedule_task_table(problem_being_solved=current_task,
                                   global_time=global_time,
                                   time=date_time_list[1],
                                   date=date_time_list[0])
        my_object.save()
        task_info_list=extra.reupload_task_info_to_html()
        return JsonResponse(task_info_list, safe=False)
        
  
    
    def generate_person_indivdual_life_dag_history_of_tasks_completed_in_their_life_and_effects_on_others(request):
      print('publish news articles comics aqnd use every median of communication to show person tasks and the effects of their tasks on the world and others throughout their life ')
      print('use every legal means to gather infromation and hacking if legal and pi ')
      print('generate strategies people could use to stop rich people from doing harm and discourage hurting people like law suit or counter tasks people could use to mitigate negastive effects of person tasks ')
      print('only publish about rich people and people above a certain net worth like 200k a year so people could change their behaviour and make them use their money for good')
      print('this is to prevent lying or omissions or distortions and focuses on what people do rather than who they are and therefore can stop bad tasks and encourage good tasks and not be discriminatory')
      print("""prevent evil and people lying or distorting reality by people like nethanyu or israel by 
            creating a indivduals life dag track the tasks they complete daily and publish this publicly if its not private info] 
            use different medians to document these people tasks like comics or news articles and keep a running history of tasks
            they do like hurting people or helping people and show effects of each task on the world] 
            use information in this running life dag to prosecute people for destroying the world or hurting people or reward people 
            for helping people] use this to stop evil and encourage good behaviour-""")
      import time
      big_white_host="192.168.2.214" 
      
    def task_search_api(request): # May include more arguments depending on URL parameters
      import time
      from datetime import datetime
      import re
      today=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
      date_time_list=re.split(" ", today)
      search_time=time.time()
      big_white_host="192.168.2.214"    
      psp_search = request.GET.get('key1')
      type_of_search= request.GET.get('key2')
      activation_time = request.GET.get('key3')
      activation_day=request.GET.get('key4')
      gui_type=request.GET.get('key5')  
      #user_name=request.GET.get('key6')    
      #password=request.GET.get('key7') 
      password="1234"
      user_name="meow"
      print('type of search is the objective guided by effects') 
      user_info=extra.get_user_info(user_name,password)
      ### search tasks  #FINISHED
      if gui_type=="search_tasks":
          #save search to database
          username=""
          if user_info:
              user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
              user_object.save()             
          # execute search
          tasks_dic_list=extra.search_sort_tasks(psp_search) 
          # upload to relevent tables info                        
          sorted_related_task_dic_list = [{"table":"related_task_table",
                                     "task":taskk["problem_being_solved"],
                                     } for taskk in tasks_dic_list]
          return JsonResponse(sorted_related_task_dic_list, safe=False) 
      ### search gui scripts FINISHED
      if gui_type=="search_gui_scripts":
          # save to database search
          username=""
          if user_info:
              user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
              user_object.save()               
          my_object = generate_pyautogui_script_searches(script_nam_search=psp_search, search_time=search_time)
          my_object.save()           
          # execute search
          gui_dic_list=extra.search_sort_gui_scripts(psp_search)
          #parse upload to add to tables
          # just have single gui script table and have option to generate or execute for each script
          # just upload all scripts and if they still need to be generated add a button for this
          sorted_gui_script_list = [{"table":"gui_script_table",
                              "script_name":gui_script_info["script_name"],
                              "script_description":gui_script_info["script_description"],
                              "generated_or_not":gui_script_info["generated_or_not"]
                              } 
                             for gui_script_info in gui_dic_list]                
          # it is simply a list of dicitonaries where you can use the key values in a specific way
          #problem_list = [{"table":"updatetable1",'problem': problem} for problem in problem_list]
          return JsonResponse(sorted_gui_script_list, safe=False)
      
          #problem_info_list.extend(strategy_search_results)  
      ### schedule task
      if gui_type=="schedule_task":# pyautogui scehdule search button is accruate
          # save to database search
          my_object = schedule_pyautogui_script_searches(script_name_search=psp_search, script_activation_time_search=activation_time,search_time=search_time)
          my_object.save()
          if user_info:
              user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
              user_object.save()    
          # execute the pyauogui commands
          sorted_scheduled_action_scripts=extra.schedule_task(psp_search,activation_time,activation_day)         
          #parse upload to add to tables
          schecudled_task_list=[{"table":"scheduled_task_table",
                                   "task":sorted_scheduled_script["problem_being_solved"],
                                   "time":sorted_scheduled_script["time"],
                                   "date":sorted_scheduled_script["date"]}for sorted_scheduled_script in sorted_scheduled_action_scripts]

          return JsonResponse(schecudled_task_list, safe=False)
      
      ### schedule gui scripts    
      if gui_type=="schedule_gui":# pyautogui scehdule search button is accruate
          # save to database search
          my_object = schedule_pyautogui_script_searches(script_name_search=psp_search, script_activation_time_search=activation_time,search_time=search_time)
          my_object.save()
          if user_info:
              user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
              user_object.save()    
          # execute the pyauogui commands
          sorted_scheduled_action_scripts=extra.schedule_pyautogui_action(psp_search,activation_time,activation_day)         
          #parse upload to add to tables
          schecudled_script_list=[{"table":"scheduled_script_table",
                                   "gui_script":sorted_scheduled_script["action_page_script_name"],
                                   "time":sorted_scheduled_script["time"],
                                   "date":sorted_scheduled_script["date"]}for sorted_scheduled_script in sorted_scheduled_action_scripts]
          return JsonResponse(schecudled_script_list, safe=False)
      
      ### generate seaerch results from api
      if gui_type=="generate_gui_script":
          my_object = generate_pyautogui_script_searches(script_nam_search=psp_search, search_time=search_time)
          my_object.save() 
          if user_info:
              user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
              user_object.save()               
          #execute_search
          gui_dic_list=extra.search_sort_gui_scripts(psp_search)
          # execute the pyauogui commands model this off of what is returned in scheudle pyautogui
          extra.generate_pyautogui_files_on_other_computers_from_big_black_using_website(gui_dic_list[0])         
          #parse upload to add to tables
          # just have single gui script table and have option to generate or execute for each script
          # just upload all scripts and if they still need to be generated add a button for this
          sorted_gui_script_list = [{"table":"gui_script_table",
                              "script_name":gui_script_info["script_name"],
                              "script_description":gui_script_info["script_description"],
                              "generated_or_not":gui_script_info["generated_or_not"],
                              } 
                             for gui_script_info in gui_dic_list]                
          # it is simply a list of dicitonaries where you can use the key values in a specific way
          #problem_list = [{"table":"updatetable1",'problem': problem} for problem in problem_list]
          return JsonResponse(sorted_gui_script_list, safe=False)
      else:
          #set task 
          # need to test thsi solution tomorrw then can try the rest
          # and upload data for it like a gen ai model
          #save search to database
          my_object = psp_search_api_searches(psp_search=psp_search,search_time=search_time)  
          my_object.save()
          if user_info:
              user_object = user_api_searches(psp_search=psp_search,search_time=search_time)  
              user_object.save()          
          # set as current task
          # scehdule task
          # run api query to grab documents
          all_task_info_dict_list_dic,edited_psp_search=extra.query_psp_search_api(psp_search,big_white_host,type_of_search=type_of_search)     
          # return relevent info to relevent tables
          ###task info table save api resonse
          #task info saves
          for task_info in all_task_info_dict_list_dic["task_info_listt"]:
              my_object = task_info_table(problem_being_solved=edited_psp_search,
                                         document=task_info["document"],
                                         document_content=task_info["document_content"],
                                         )
              my_object.save()
          ###schedule table save              
          my_object = schedule_task_table(problem_being_solved=edited_psp_search,
                                     global_time=search_time,
                                     time=date_time_list[1],
                                     date=date_time_list[0])
          my_object.save() 
          ###strategy table saves
          for actionn in all_task_info_dict_list_dic["current_task_strats_dic_listt"]  :
              my_object = strategy_table(problem_being_solved=edited_psp_search,
                                         strat_delimiter=actionn['strat_delimiter'],
                                         step_delimiter=actionn['step_delimiter'],
                                         task=actionn["task"],                         
                                         effects=actionn["effects"],
                                         typee=actionn["typee"],
                                         )
              my_object.save()           
          ### related task table saves
          for related_taskk in all_task_info_dict_list_dic["related_task_listt"]:
              my_object = related_task_table(problem_being_solved=edited_psp_search,
                                         related_task=related_taskk["related_task"])
              my_object.save()

          task_info_list=extra.reupload_task_info_to_html()
          return JsonResponse(task_info_list, safe=False)

    def submit_data(request):
        print(request)
        import json
        print(request)        
        if request.method == "POST":
            try:
            # Get the JSON data from the request
             data = json.loads(request.body)
             # You can process the data here (e.g., save to the database)
             print(data)
             print(data['problem'])
             
            except Exception as E:
                print(E) 
        return HttpResponse("Thank you for your submission!")
        
    
    
    
    def contact(request):
     if request.method == "POST":
        problem=request.POST.get('problem')
        print(problem)
            # Process form data (send email, save to DB, etc.)
        # Example: Send an email
        hehe=problem_table.objects.values_list('problem_question_or_task') # value_list produces it as a list

        context = {"hi":problem_table.objects.all(),
            "meow":problem_table.objects.filter(problem_question_or_task=2006),
            "problem_values":problem_table.objects.values_list('problem_question_or_task')}
        
        
        return render(request, 'f_window.html',{'context': context,'hehe':hehe})
        
        return HttpResponse("Thank you for your submission!")
            
            
     else:
        return HttpResponse("Form submission failed. Please check the data.")

   
  
     
   
    # i contains for case insensitive match
    #Entry.objects.get(headline__contains="Lennon")

    #Entry.objects.filter(blog__name="Beatles Blog")
    #Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008)
    #cases=Case_Meta_Data.objects.filter(Q(name__startswith="search_text") | Q(name__startswith="Idea"))

    #books = Case_Meta_Data.objects.filter()
    #Publisher.objects.filter(Q(name__startswith="New") & Q(name__endswith="Publisher"))
    #books = Case_Meta_Data.objects.all()
    
    #Entry.objects.filter(pub_date__year=2006)
    #one_entry = Entry.objects.get(pk=1)
    #cases=Case_Meta_Data.objects.filter(name__icontains=search_text)
    # produces a list as opposed to get which produces a single value
    #return render(request,"case_list.html",{"cases": case})

    #case = case.review_set.all()
    #if case.date =="":
    #    return render(request,"case_list.html",{"cases": cases})
    #    continue    
    
            
        
       


        
        
        