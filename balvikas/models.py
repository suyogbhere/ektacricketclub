from django.db import models
import datetime

# Create your models here.
class BalVikas_Member(models.Model):
    Name = models.CharField(max_length=100,null=False)        #_('Text')
    def __str__(self):
        return self.Name


YEAR_CHOICES = [((f"{y}-{y+1}"),f"{y}-{y+1}") for y in range(2015,datetime.datetime.now().year+1)]

class BalVikas_Member_Subscription(models.Model):
    Name = models.ForeignKey(BalVikas_Member, on_delete=models.CASCADE)
    Subscription = models.IntegerField()
    Date = models.DateTimeField()
    Year = models.CharField(max_length=100, choices=YEAR_CHOICES)  

    def __str__(self):
        return '%s %s %s' %(self.Name, self.Subscription, self.Year)