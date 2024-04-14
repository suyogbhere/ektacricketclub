import django_filters
from .models import *
from django import forms

YEAR_CHOICES = [((f"{y}-{y+1}"),f"{y}-{y+1}") for y in range(2015,datetime.datetime.now().year+1)]

#Model Name filter
class BalVikas_Member_Subscription_Filter(django_filters.FilterSet):
    Name = django_filters.ModelChoiceFilter(
            queryset=BalVikas_Member.objects.all(),
            label='नाव',
            empty_label='नाव',
            widget=forms.Select(attrs={'class': 'form-control'}) )
    Subscription = django_filters.NumberFilter(
            label='वर्गणी',
            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Year = django_filters.ChoiceFilter(
            choices=YEAR_CHOICES,
            label='वर्ष',
            empty_label='वर्ष',
            widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = BalVikas_Member_Subscription
        fields = ['Name', 'Subscription', 'Year']

