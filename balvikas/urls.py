from django.urls import path
from .import views
from.forms import *


urlpatterns = [
    path('abvms/',views.Add_BalVikas_Members_subscription,name="abvms"),
    path('ebvms/<int:id>/',views.Edit_BalVikas_Members_subscription,name="ebvms"),
    path('dbvms/<int:id>/',views.Delete_BalVikas_Members_subscription,name="dbvms"),
    path('sbvms/',views.Show_BalVikas_Members_Subscription,name='sbvms'),
    path('abvm/',views.Add_BalVikas_Members,name='abvm'),
    
]