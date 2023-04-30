from django.db import models
import datetime

# Create your models here.
class BalVikas_Member(models.Model):
    Name = models.CharField(max_length=100,null=False)        #_('Text')
    def __str__(self):
        return self.Name


YEAR_CHOICES = []
for y in range(2015, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((y,y))

class BalVikas_Member_Subscription(models.Model):
    Name = models.ForeignKey(BalVikas_Member, on_delete=models.CASCADE)
    Subscription = models.IntegerField()
    Date = models.DateTimeField()
    Year = models.IntegerField(('year'), choices=YEAR_CHOICES,default=datetime.datetime.now().year)  

    def __str__(self):
        return '%s %s %s' %(self.Name, self.Subscription, self.Year)