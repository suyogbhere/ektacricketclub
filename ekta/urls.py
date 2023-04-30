from django.urls import path
from .import views
from.forms import *


urlpatterns = [
    path('', views.home,name="home"),
    path('cricket/', views.cricket,name="cricket"),
    path('education/', views.educational,name="education"),
    path('cultural/', views.cultural,name="cultural"),
    path('social/', views.social,name="social"),
    path('eb/',views.Executive_Board,name="eb"),
    path('contact/', views.contact,name="contact"),
    path('signup/', views.user_signup,name="signup"),
    path('login/', views.user_login,name="login"),
    path('cp/',views.Change_Password,name='cp'),
    path('logout/', views.user_logout,name="logout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('aems/',views.Add_Ekta_Members_subscription,name="aems"),
    path('eems/<int:id>/',views.Edit_Ekta_Members_subscription,name="eems"),
    path('ecmp/<int:id>/',views.Edit_Cricket_member_photo,name="ecmp"),
    path('ebp/<int:id>/',views.Edit_Birthday_photo,name="ebp"),
    path('dems/<int:id>/',views.Delete_Ekta_Members_subscription,name="dems"),
    path('dfs/<int:id>/',views.Delete_Feedback_Suggestion,name="dfs"),
    path('dcmp/<int:id>/',views.Delete_Cricket_member_photo,name="dcmp"),
    path('dep/<int:id>/',views.Delete_Educational_photo,name="dep"),
    path('dbp/<int:id>/',views.Delete_Birthday_photo,name="dbp"),
    path('dcp/<int:id>/',views.Delete_Cultural_photo,name="dcp"),
    path('dsp/<int:id>/',views.Delete_Social_photo,name="dsp"),
    path('sems/',views.Show_Ekta_Members_Subscription,name='sems'),
    path('sfs/',views.Show_Feedback_Suggestion,name='sfs'),
    path('aem/',views.Add_Ekta_Members,name='aem'),
    path('ucm/',views.Upload_Cricket_Members,name="ucm"),
    path('ubp/',views.Upload_Birthday_Photo,name="ubp"),
    path('uep/',views.Upload_Educational_photo,name="uep"),
    path('ucp/',views.Upload_Cultural_photo,name="ucp"),
    path('usp/',views.Upload_Social_photo,name="usp"),
    path('aam', views.Add_Annual_Meeting_page, name='aam'),
    path('sam', views.Show_Annual_Meeting_page, name='sam'),
    path('eetc', views.Ekta_export_to_csv, name="eetc"),
    path('eet', views.Ekta_export_to_csv1, name="eet"),
    
    
]