import django_filters
from .models import *
from django import forms

YEAR_CHOICES = []
for y in range(1995, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((y,y))

#Model Name filter
class BalVikas_Member_Subscription_Filter(django_filters.FilterSet):
    Name = django_filters.ModelChoiceFilter(queryset=BalVikas_Member.objects.all(), label='नाव')
    Subscription = django_filters.NumberFilter(label='वर्गणी')
    Year = django_filters.ChoiceFilter(choices=YEAR_CHOICES, label='वर्ष')

    class Meta:
        model = BalVikas_Member_Subscription
        fields = ['Name', 'Subscription', 'Year']

       