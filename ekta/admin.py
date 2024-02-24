from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(EktaMember)
class MemberAdmin(admin.ModelAdmin):
    list_display =['id', 'Name']

@admin.register(Ekta_Member_Subscription)
class EktaMemberSubsriptionAdmin(admin.ModelAdmin):
    list_display =['id', 'Name', 'Subscription', 'Date', 'Year']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['Name', 'Email', 'Subject', 'Message']

@admin.register(Cricket_Member)
class CricketMemberAdmin(admin.ModelAdmin):
    list_display =['id', 'Name', 'Discription', 'Photo']

@admin.register(Birthday_Photos)
class Birthday_PhotosAdmin(admin.ModelAdmin):
    list_display =['id','Photo']

@admin.register(Social_photo_upload)
class Social_photo_uploadAdmin(admin.ModelAdmin):
    list_display =['id', 'Discription', 'Photo']

@admin.register(Cultural_photo_upload)
class Cultural_photo_uploadAdmin(admin.ModelAdmin):
    list_display =['id', 'Discription', 'Photo']

@admin.register(Educational_photo_upload)
class Educational_photo_uploadAdmin(admin.ModelAdmin):
    list_display =['id', 'Discription', 'Photo']

@admin.register(Annual_Meeting)
class Annual_MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','Image','Date','Discription']

@admin.register(Annual_Function)
class Annual_FunctionAdmin(admin.ModelAdmin):
    list_display = ['id','Image','Date','Discription']

#work in progress
# @admin.register(Executive_board)
# class Executive_board_Admin(admin.ModelAdmin):
#     list_display =['id', 'Name', 'Position']
    
       
@admin.register(Hpl_registration)
class Hpl_registrationAdmin(admin.ModelAdmin):
    list_display = ['id','Full_Name','DOB','contact','player_skill','t_shirt_Size']