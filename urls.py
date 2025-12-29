"""
URL configuration for canlawaccessible project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import sys
from django.conf import settings
from django.conf.urls.static import static

# caution: path[0] is reserved for script path (or '' in REPL)
#home_path = r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Music'
#legal_issues_app_path = '\canlawaccessible'
#app1_path=home_path+legal_issues_app_path
#print(app1_path)
# this adds the other folder to the current folders path so we can access the files in it
#sys.path.insert(1, app1_path)



import psp_website.views
# general structure of views is 1: Urlpath, 2:the name of the specific view, and a name= kwarg referring to the name of the view refering to the url
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    #path("signup/", psp_website.views.HomePage.signup, name="signup"),
    #path("login/", psp_website.views.HomePage.login, name="login"),
    # makes like auth si taking care of most of this
    #http://127.0.0.1:8000/accounts/login/ to login

    
    path('', psp_website.views.HomePage.website_name, name="website_name"), 
    path('searched_text', psp_website.views.HomePage.search),
    # base3 references the name and then the name sends it to a paritucalr view referecned in path      
    path('question_answered/', psp_website.views.HomePage.question_answered, name='question_answered'),  # New URL pattern for cases
    path('register/', psp_website.views.HomePage.register, name='register'),

    
    path('contribute/', psp_website.views.HomePage.contribute, name='contribute'),  # New URL pattern for cases
    path('inbox/', psp_website.views.HomePage.inbox, name='inbox'),  # New URL pattern for cases
    path('connect/', psp_website.views.HomePage.connect, name='connect'),  # New URL pattern for cases
    path('schedule/', psp_website.views.HomePage.schedule, name='schedule'),  # New URL pattern for cases
    path('notifications/', psp_website.views.HomePage.notifications, name='notifications'),  # New URL pattern for cases
    path('profile/', psp_website.views.HomePage.profile, name='profile'),  # New URL pattern for cases
    
    path('thrift/', psp_website.views.HomePage.thrift, name='thrift'),  # New URL pattern for cases


    

    path('submit-data/', psp_website.views.HomePage.submit_data, name='submit_data'), # submit form
    path('contact/', psp_website.views.HomePage.contact, name='contact'),
    path('get_persons/', psp_website.views.HomePage.get_persons, name='get_persons'),
    path('task-search-api/', psp_website.views.HomePage.task_search_api, name='task_search_api'), # submit form
    path('set-current-task/', psp_website.views.HomePage.set_current_task, name='set_current_task'), # submit form
    
    
    path('upload-month-data/', psp_website.views.HomePage.upload_month_data, name='upload_month_data'), # submit form

    path('perform-gui-script-action/', psp_website.views.HomePage.perform_gui_script_action, name='perform_gui_script_action'), # submit form
    
    path('modify-info/', psp_website.views.HomePage.modify_info, name='modify_info'), # submit form
    path('start-a-project/', psp_website.views.HomePage.start_a_project, name='start_a_project'), # submit form

    
    ##thsi should be the url we use for all projects created in database
    path("projects/<str:project_title>/", psp_website.views.HomePage.return_project_page, name="return_project_page"),
    path("profiles/<str:profile_name>/", psp_website.views.HomePage.return_project_page, name="return_project_page"),



    






#The include function is a shortcut that allows you to combine URL configurations.  Here, we’ve created a separate URL configuration
#for the reviews app and have added it to our project-level URL
#configuration.        
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)