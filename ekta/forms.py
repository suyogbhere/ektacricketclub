from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation




#Signup form
class Signupform(UserCreationForm):
    password1= forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        labels={"first_name":"First Name","last_name":"Last Name","email":"Email"}
        widgets={"username":forms.TextInput(attrs={"class":"form-control"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),
                 }

#Password Changeform
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('जुना पासवर्ड'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label=_('नवीन पासवर्ड'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("नवीन पासवर्ड तपासा"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))

#custom date widget
class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'


#Ekta member Subscription form
class EktaMemberSubscriptionForm(forms.ModelForm):
    # Date= forms.DateField(widget=Dateinput)
    class Meta:
        model = Ekta_Member_Subscription 
        fields = '__all__'
        labels = {'Subscription':'वर्गणी(₹)', 'Name':'नाव', 'Year':'वर्ष','Date':'तारीख'}
        widgets={
            'Name': forms.Select(attrs={'class':'form-select'}),
            'Subscription': forms.NumberInput(attrs={'class':'form-control'}),
            'Year': forms.Select(attrs={'class':'form-select'}),
            'Date': DateTimeInput(attrs={'class':'form-control'})
        }

#Ekta Member form
class MemberForm(forms.ModelForm):
    class Meta:
        model = EktaMember
        fields = '__all__'
        labels = {'Name':'नाव'}
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
        }

#Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Subject':forms.TextInput(attrs={'class':'form-control'}),
            'Message':forms.Textarea(attrs={'class':'form-control', 'rows':4,'cols':10}),
        }

        labels={
            'Name':'तुमचे नाव', 'Email':'ई-मेल', 'Subject':'विषय', 'Message':'मेसेज' 
        }


#photo upload forms
#Cricket Member form
class CricketMemberForm(forms.ModelForm):
    class Meta:
        model = Cricket_Member
        fields = '__all__'
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
            'Photo': forms.FileInput(attrs={'class':'form-control'})
        }
        labels={
            'Name':'नाव', 'Discription':'वर्णन', 'Photo':'फोटो'
        }

class Birthday_Photo_form(forms.ModelForm):
    class Meta:
        model = Birthday_Photos
        fields = '__all__'
        widgets={
            'Photo': forms.FileInput(attrs={'class':'form-control'})
        }
        labels={
            'Photo':'फोटो'
        }

class Social_photo_form(forms.ModelForm):
    class Meta:
        model = Social_photo_upload
        fields = '__all__'
        widgets={
            'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
            'Photo': forms.FileInput(attrs={'class':'form-control'})
        }
        labels={
            'Discription':'वर्णन', 'Photo':'फोटो'
        }

class Cultural_photo_form(forms.ModelForm):
    class Meta:
        model = Cultural_photo_upload
        fields = '__all__'
        widgets={
            'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
            'Photo': forms.FileInput(attrs={'class':'form-control'})
        }
        labels={
            'Discription':'वर्णन', 'Photo':'फोटो'
        }
    
class Educational_photo_form(forms.ModelForm):
    class Meta:
        model = Educational_photo_upload
        fields = '__all__'
        widgets={
            'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
            'Photo': forms.FileInput(attrs={'class':'form-control'})
        }
        labels={
            'Discription':'वर्णन', 'Photo':'फोटो'
        }


class Annual_Meeting_form(forms.ModelForm):
    class Meta:
        model = Annual_Meeting
        fields = '__all__'
        widgets = {
            'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
            'Date': DateTimeInput(attrs={'class':'form-control'}),
            'Image': forms.FileInput(attrs={'class':'form-control'}),
        }
        labels={
            'Image':'फोटो', 'Date':'तारीख','Discription':'वर्णन'
        }


class Annual_Function_form(forms.ModelForm):
    class Meta:
        model = Annual_Meeting
        fields = '__all__'
        widgets = {
            'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
            'Date': DateTimeInput(attrs={'class':'form-control'}),
            'Image': forms.FileInput(attrs={'class':'form-control'}),
        }
        labels={
            'Image':'फोटो', 'Date':'तारीख','Discription':'वर्णन'
        }



# class Executive_board_form(forms.ModelForm):
#     class Meta:
#         model = Executive_board
#         fields = '__all__'
#         widgets={
#             'Discription': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3}),
#             'Photo': forms.FileInput(attrs={'class':'form-control'})
#         }
#         labels={
#             'Discription':'वर्णन', 'Photo':'फोटो'
#         }



Player_skill=[
    ('फलंदाज','फलंदाज'),
    ('गोलंदाज','गोलंदाज'),
    ('अष्टपैलू','अष्टपैलू'),
    ('यष्टिरक्षक','यष्टिरक्षक')
]

class DateInput(forms.DateInput):
    input_type = 'date'


class Hpl_registration_form(forms.ModelForm):
    class Meta:
        model = Hpl_registration
        fields = ['Full_Name','DOB','contact','t_shirt_Size', 'player_skill']
        widgets = { 
            'Full_Name': forms.TextInput(attrs={'class':'form-control'}),
            'DOB': DateInput(attrs={'class':'form-control'}),
            'contact' : forms.TextInput(attrs={'class':'form-control'}),
            't_shirt_Size' : forms.NumberInput(attrs={'class':'form-control'}),
            'player_skill' : forms.Select(attrs={'class':'form-control'})
        }
        labels={
            'Full_Name':'संपूर्ण नाव',
            'DOB': 'जन्मतारीख',
            'contact': 'संपर्क',
            't_shirt_Size': 'टि शर्ट साईज',
            'player_skill': 'खेळाडूचे कौशल्य'
        }

   