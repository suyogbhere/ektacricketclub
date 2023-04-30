from django import forms
from .models import *


#custom datetime widget
class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'

#BalVikas member Subscription form
class BalVikasMemberSubscriptionForm(forms.ModelForm):
    class Meta:
        model = BalVikas_Member_Subscription 
        fields = '__all__'
        labels = {'Subscription':'वर्गणी(₹)', 'Name':'नाव', 'Year':'वर्ष','Date':'तारीख'}
        widgets={
            'Name': forms.Select(attrs={'class':'form-select'}),
            'Subscription': forms.NumberInput(attrs={'class':'form-control'}),
            'Year': forms.Select(attrs={'class':'form-select'}),
            'Date': DateTimeInput(attrs={'class':'form-control'})
        }

#BalVIkas Member form
class BalVikasMemberForm(forms.ModelForm):
    class Meta:
        model = BalVikas_Member
        fields = '__all__'
        labels = {'Name':'नाव'}
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
        }

