from django.db import models
import datetime
from django.utils.translation import gettext as _

# Create your models here.

class EktaMember(models.Model):
    Name = models.CharField(max_length=100,null=False)        #_('Text')
    def __str__(self):
        return self.Name


YEAR_CHOICES = [((f"{y}-{y+1}"),f"{y}-{y+1}") for y in range(2015,datetime.datetime.now().year+1)]

class Ekta_Member_Subscription(models.Model):
    Name = models.ForeignKey(EktaMember, on_delete=models.CASCADE)
    Subscription = models.IntegerField()
    Date = models.DateTimeField()
    Year = models.CharField(max_length=100, choices=YEAR_CHOICES)  

    def __str__(self):
        return '%s %s %s' %(self.Name, self.Subscription, self.Year)


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=200)
    Message = models.CharField(max_length=250)

#Photo Upload all
class Cricket_Member(models.Model):
    Name = models.CharField(max_length=100)
    Discription = models.CharField(max_length=200, blank=True)
    Photo = models.ImageField(upload_to="Ekta_Boys_photo")

class Birthday_Photos(models.Model):
    Photo = models.ImageField(upload_to="Birthday_photo")


class Social_photo_upload(models.Model):
    Photo = models.ImageField(upload_to="Social_photo")
    Discription = models.CharField(max_length=200, blank=True)
    

class Cultural_photo_upload(models.Model):
    Photo = models.ImageField(upload_to="Cultural_photo")
    Discription = models.CharField(max_length=200, blank=True)

class Educational_photo_upload(models.Model):
    Photo = models.ImageField(upload_to="Educational_photo")
    Discription = models.CharField(max_length=200, blank=True)


class Annual_Meeting(models.Model):
    Image = models.ImageField(upload_to="Meeting_photo",null=True)
    Date = models.DateTimeField(null=True)
    Discription=models.CharField(max_length=250,null=True)

class Annual_Function(models.Model):
    Image = models.ImageField(upload_to="Function_photo",null=True)
    Date = models.DateTimeField(null=True)
    Discription=models.CharField(max_length=250,null=True)


# #work in progress
# class Position(models.Model):
#     Position = models.CharField(max_length=200, null=False)

# class Executive_board(models.Model):
#     Name = models.ImageField()
#     Position = models.ForeignKey(Position, on_delete=models.CASCADE)


Player_skill=[
        ('फलंदाज','फलंदाज'),
        ('गोलंदाज','गोलंदाज'),
        ('अष्टपैलू','अष्टपैलू'),
        ('यष्टिरक्षक','यष्टिरक्षक')
]

Money_Status=[
        ('PAID','PAID'),
        ('UNPAID','UNPAID')
]


class Hpl_registration(models.Model):
    Full_Name = models.CharField(max_length=200)
    DOB = models.DateField(max_length=100)
    contact = models.CharField(max_length=50, blank=True)
    player_skill = models.CharField(choices=Player_skill, max_length=100)
    t_shirt_Size = models.IntegerField()
    money_status = models.CharField(choices=Money_Status, max_length=100, default='UNPAID')

