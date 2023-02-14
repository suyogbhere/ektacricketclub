from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BalVikas_Member)
class BalVikas_MemberAdmin(admin.ModelAdmin):
    list_display =['id', 'Name']

@admin.register(BalVikas_Member_Subscription)
class BalVikas_MemberSubsriptionAdmin(admin.ModelAdmin):
    list_display =['id', 'Name', 'Subscription', 'Date', 'Year']