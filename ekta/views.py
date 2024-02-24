from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from ekta.forms import Signupform,MyPasswordChangeForm,DateTimeInput,EktaMemberSubscriptionForm,MemberForm,ContactForm,CricketMemberForm,Birthday_Photo_form,Social_photo_form,Cultural_photo_form,Educational_photo_form,Annual_Meeting_form,Annual_Function_form,Hpl_registration_form
from ekta.models import EktaMember,Ekta_Member_Subscription,Contact,Cricket_Member,Birthday_Photos,Social_photo_upload,Cultural_photo_upload,Educational_photo_upload,Annual_Meeting,Annual_Function,Hpl_registration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .filters import Ekta_Member_Subscription_Filter
import csv


# Create your views here.
# Home page
def home(request):
    img = Birthday_Photos.objects.all()
    context={'home':'active','img':img}
    return render(request,'ekta1/home.html',context)

def cricket(request):
    img=Cricket_Member.objects.all()
    context={'education':'active', 'img':img}
    return render(request,'ekta1/cricket.html',context)

def birthday(request):
    img=Birthday_Photos.objects.all()
    context={'education':'active', 'img':img}
    return render(request,'ekta1/home.html',context)

def educational(request):
    img=Educational_photo_upload.objects.all()
    context={'education':'active', 'img':img}
    return render(request,'ekta1/educational.html',context)

def cultural(request):
    img=Cultural_photo_upload.objects.all()
    context={'cultural':'active', 'img':img}
    return render(request,'ekta1/cultural.html',context)

def social(request):
    img=Social_photo_upload.objects.all()
    context={'social':'active', 'img':img}
    return render(request,'ekta1/social.html',context)


#Signup form
@csrf_protect
def user_signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation !! Account Created successfully')
            form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = Signupform()
    return render(request,'ekta1/signup.html',{'signup':'active','form':form})

#User Login

def user_login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user.is_staff:
                login(request,user)
                messages.success(request,'log in successfully!!!')
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request,'माफ करा, तुम्ही अजून एकता क्रिकेट क्लबचे सदस्य नाही आहात. एकता क्रिकेट क्लबच्या प्रशासकाशी संपर्क साधा!!!!')
    else:
        fm=AuthenticationForm()
    return render(request,'ekta1/login.html',{'login':'active','form':fm})

#User Logout
@login_required
@csrf_protect
def user_logout(request):
    logout(request)
    messages.success(request,'Log Out successfully!!!')
    return HttpResponseRedirect("/login/")

#Contact Page
def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank you for your feedback !!!')
    else:
        fm = ContactForm()
    return render(request,'ekta1/contact.html',{'contact':'active','form':fm})

@csrf_protect
@csrf_exempt
def dashboard(request):
    if request.user.is_authenticated:
        context={'dashboard':'active'}
        return render(request,'ekta1/dashboard.html',context)
    else:
        return HttpResponseRedirect("/login/")


@csrf_protect
def Add_Ekta_Members_subscription(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=EktaMemberSubscriptionForm(request.POST)
            if fm.is_valid():
                nm=fm.cleaned_data['Name']
                sb=fm.cleaned_data['Subscription']
                yy=fm.cleaned_data['Year']
                dd=fm.cleaned_data['Date']
                data=Ekta_Member_Subscription(Name=nm,Subscription=sb,Year=yy,Date=dd)
                data.save()
                messages.success(request,'वर्गणी जमा झाली !!!')
                return HttpResponseRedirect("/sems/")
        else:
            fm=EktaMemberSubscriptionForm()
        return render(request,'ekta1/add_ekta_members_subscription.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")

@csrf_protect
def Add_Ekta_Members(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=MemberForm(request.POST)
            if fm.is_valid():
                nm=fm.cleaned_data['Name']
                data=EktaMember(Name=nm)
                data.save()
                messages.success(request,'सभासद नोंद झाला!!!')
                return HttpResponseRedirect("/sems/")
        else:
            fm=MemberForm()
        return render(request,'ekta1/add_ekta_members.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


# Show All Member Subscription 
@csrf_protect
def Show_Ekta_Members_Subscription(request):
    if request.user.is_authenticated:
        fm1 = Ekta_Member_Subscription.objects.all()
        fm2 = EktaMember.objects.all()
        myfilter = Ekta_Member_Subscription_Filter(request.POST, queryset=fm1)
        fm1 = myfilter.qs
        return render(request,'ekta1/show_ekta_members_subscription.html',{'form1':fm1, 'form2':fm2,'SEMS':'active', 'myfilter':myfilter})
    else:
        return HttpResponseRedirect("/login/")

def Show_Feedback_Suggestion(request):
    if request.user.is_authenticated:
        fm = Contact.objects.all()
        return render(request,'ekta1/show_feedback_suggestion.html',{'form':fm, 'SFS':'active'})
    else:
        return HttpResponseRedirect("/login/")


def Delete_Ekta_Members_subscription(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Ekta_Member_Subscription.objects.get(pk=id)
            pi.delete()
            messages.error(request,'सभासद वर्गणी डीलीट केली!!!!!')
            return HttpResponseRedirect('/sems/')
    else:
        return HttpResponseRedirect("/login/")

@csrf_protect
def Edit_Ekta_Members_subscription(request,id):
    if request.method == 'POST':
        pi = Ekta_Member_Subscription.objects.get(pk=id)
        fm1 = EktaMemberSubscriptionForm(request.POST, instance=pi)
        if fm1.is_valid():
            fm1.save()
            messages.success(request,'वर्गणीमध्ये बदल झाला!!!!!')
            return HttpResponseRedirect('/sems/')
    else:
        pi = Ekta_Member_Subscription.objects.get(pk=id)
        fm1 = EktaMemberSubscriptionForm(instance=pi)
    return render(request,'ekta1/Edit_ekta_members_subscription.html',{'form':fm1})

@csrf_protect
def Edit_Cricket_member_photo(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Cricket_Member.objects.get(pk=id)
            fm = CricketMemberForm(request.POST,request.FILES, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Update details Succefully!!!')
        else:
            pi = Cricket_Member.objects.get(pk=id)
            fm = CricketMemberForm(instance=pi)
        return render(request,'ekta1/Edit_Cricket_member_photo.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")
        

def Edit_Birthday_photo(request,id):
    if request.method == 'POST':
        pi = Birthday_Photos.objects.get(pk=id)
        fm = Birthday_Photo_form(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update photo Succefully!!!')
    else:
        pi = Birthday_Photos.objects.get(pk=id)
        fm = Birthday_Photo_form(instance=pi)
    return render(request,'ekta1/Edit_Birthday_photo.html',{'form':fm})

def Delete_Cricket_member_photo(request,id):
    if request.method == 'POST':
        pi = Cricket_Member.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/cricket/')

def Delete_Feedback_Suggestion(request,id):
    if request.method == 'POST':
        pi = Contact.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/sfs/')

def Delete_Birthday_photo(request,id):
    if request.method == 'POST':
        pi = Birthday_Photos.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/ubp/')

def Delete_Educational_photo(request,id):
    if request.method == 'POST':
        pi = Educational_photo_upload.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/education/')

def Delete_Cultural_photo(request,id):
    if request.method == 'POST':
        pi = Cultural_photo_upload.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/cultural/')

def Delete_Social_photo(request,id):
    if request.method == 'POST':
        pi = Social_photo_upload.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/social/')


# def Delete_Members(request,id):
#     if request.method == 'POST':
#         pi = Member.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/sms/')


def Change_Password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = MyPasswordChangeForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Change successfully!!!')
                return HttpResponseRedirect("/dashboard/")
            else:
                messages.error(request,'Please correct the error')
                return HttpResponseRedirect('/cp/')
        else:
            fm = MyPasswordChangeForm(user=request.user, label_suffix='')
        return render(request,'ekta1/password_change.html',{'form':fm, 'CP':'active'})
    else:
        return HttpResponseRedirect("/login/")
    

#Photo Upload All
@csrf_protect
def Upload_Cricket_Members(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=CricketMemberForm(request.POST, request.FILES)
            if fm.is_valid():
                nm=fm.cleaned_data['Name']
                ph=fm.cleaned_data['Photo']
                di=fm.cleaned_data['Discription']
                data=Cricket_Member(Name=nm, Discription=di, Photo=ph)
                data.save()
                messages.success(request,'Image Upload Successfully!!!')
                # fm=CricketMemberForm()
        else:
            fm=CricketMemberForm()
        return render(request,'ekta1/upload_cricket_photo.html',{'form':fm,'UCM':'active'})
    else:
        return HttpResponseRedirect("/login/")

@csrf_protect
def Upload_Birthday_Photo(request):
    if request.user.is_authenticated:
        img = Birthday_Photos.objects.all()
        if request.method == 'POST':
            fm=Birthday_Photo_form(request.POST, request.FILES)
            if fm.is_valid():
                ph=fm.cleaned_data['Photo']
                data=Birthday_Photos(Photo=ph)
                data.save()
                messages.success(request,'Image Upload Successfully!!!')
        else:
            fm=Birthday_Photo_form()
        return render(request,'ekta1/upload_birthday_photo.html',{'form':fm,'UBP':'active', 'img':img})
    else:
        return HttpResponseRedirect("/login/")

def Upload_Social_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=Social_photo_form(request.POST, request.FILES)
            if fm.is_valid():
                ph=fm.cleaned_data['Photo']
                di=fm.cleaned_data['Discription']
                data=Social_photo_upload(Discription=di, Photo=ph)
                data.save()
                messages.success(request,'Image Upload Successfully!!!')
        else:
            fm=Social_photo_form()
        return render(request,'ekta1/upload_social_photo.html',{'form':fm,'USP':'active'})
    else:
        return HttpResponseRedirect("/login/")

def Upload_Cultural_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=Cultural_photo_form(request.POST, request.FILES)
            if fm.is_valid():
                ph=fm.cleaned_data['Photo']
                di=fm.cleaned_data['Discription']
                data=Cultural_photo_upload(Discription=di, Photo=ph)
                data.save()
                messages.success(request,'Image Upload Successfully!!!')

        else:
            fm=Cultural_photo_form()
        return render(request,'ekta1/upload_cultural_photo.html',{'form':fm,'UCP':'active'})
    else:
        return HttpResponseRedirect("/login/")

def Upload_Educational_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=Educational_photo_form(request.POST, request.FILES)
            if fm.is_valid():
                ph=fm.cleaned_data['Photo']
                di=fm.cleaned_data['Discription']
                data=Educational_photo_upload(Discription=di, Photo=ph)
                data.save()
                messages.success(request,'Image Upload Successfully!!!')

        else:
            fm=Educational_photo_form()
        return render(request,'ekta1/upload_educational_photo.html',{'form':fm,'UEP':'active'})
    else:
        return HttpResponseRedirect("/login/")

def Executive_Board(request):
    context={'EB':'active'}
    return render(request,'ekta1/executive_board.html',context)

#add annual meetings
def Add_Annual_Meeting_page(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = Annual_Meeting_form(request.POST,request.FILES)
            if fm.is_valid():
                im = fm.cleaned_data['Image']
                dd = fm.cleaned_data['Date']
                di = fm.cleaned_data['Discription']
                data = Annual_Meeting(Image=im, Date=dd, Discription=di)
                data.save()
                messages.success(request,'meeting Detail Add Successfully!!!')
        else:
            fm = Annual_Meeting_form()
        return render(request, 'ekta1/add_annual_meetings.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")
        

#Show annual meeting
def Show_Annual_Meeting_page(request):
    if request.user.is_authenticated:
        fm= Annual_Meeting.objects.all()
        return render(request, 'ekta1/show_annual_meetings.html',{'SAM':'active','form':fm})
    else:
        return HttpResponseRedirect("/login/")

#Edit annual Meeting
def Edit_Annual_Meeting_page(request,id):
    if request.method == 'POST':
        pi = Annual_Meeting.objects.get(pk=id)
        fm = Annual_Meeting_form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update annual Meeting successfully!!!')
    else:
        pi = Annual_Meeting.objects.get(pk=id)
        fm = Annual_Meeting_form(instance=pi)
    return render(request,'ekta1/Edit_Annual_Meeting.html',{'form':fm})


# delete annual meetings
def Delete_Annual_Meeting_page(request,id):
    if request.method == 'POST':
        pi = Annual_Meeting.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/sam/')


#add annual meetings
def Add_Annual_Function_page(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = Annual_Function_form(request.POST,request.FILES)
            if fm.is_valid():
                im = fm.cleaned_data['Image']
                dd = fm.cleaned_data['Date']
                di = fm.cleaned_data['Discription']
                data = Annual_Function(Image=im, Date=dd, Discription=di)
                data.save()
                messages.success(request,'Function Detail Add Successfully!!!')
        else:
            fm = Annual_Meeting_form()
        return render(request, 'ekta1/add_annual_functions.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


#Edit annual Function
def Edit_Annual_Function_page(request,id):
    if request.method == 'POST':
        pi = Annual_Function.objects.get(pk=id)
        fm = Annual_Function_form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update annual function successfully!!!')
    else:
        pi = Annual_Function.objects.get(pk=id)
        fm = Annual_Function_form(instance=pi)
    return render(request,'ekta1/Edit_Annual_Function.html',{'form':fm})

# delete annual function
def Delete_Annual_Function_page(request,id):
    if request.method == 'POST':
        pi = Annual_Function.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/saf/')

#Show annual Function
def Show_Annual_Function_page(request):
    if request.user.is_authenticated:
        fm= Annual_Function.objects.all()
        return render(request, 'ekta1/show_annual_functions.html',{'SAF':'active','form':fm})
    else:
        return HttpResponseRedirect("/login/")


# work in progress
#download ekta Member subscription 
def Ekta_export_to_csv(request):
    ems = Ekta_Member_Subscription.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="Ekta_export.csv"'
    writer = csv.writer(response)   
    writer.writerow(['ID','Name','Subscription','Year'])
    for ems in ems:
        writer.writerow([ems.id,ems.Name, ems.Subscription, ems.Year])
    return response

#download ekta Member subscription 
def Ekta_export_to_csv1(request):
    ems = Ekta_Member_Subscription.objects.all()
    myfilter = Ekta_Member_Subscription_Filter(request.GET, queryset=ems).qs
    print(myfilter)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="Ekta_export.csv"'

    writer = csv.writer(response)   

    writer.writerow(['ID','Name','Subscription','Year'])

    # for i in myfilter.values_list('Name','Subscription','Year'):
    #     writer.writerow(i)
    for myfilters in myfilter:
        writer.writerow([myfilters.id, myfilters.Name, myfilters.Subscription, myfilters.Year])
    return response



#hpl registration
def hpl_registration(request):
    if request.method == 'POST':
        fm = Hpl_registration_form(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['Full_Name']
            DB = fm.cleaned_data['DOB']
            co = fm.cleaned_data['contact']
            ps = fm.cleaned_data['player_skill']
            ts = fm.cleaned_data['t_shirt_Size']
            data = Hpl_registration(Full_Name=fn, DOB=DB, contact=co, player_skill=ps, t_shirt_Size=ts)
            data.save()
            messages.success(request,'Form submited successfully !!!')
            return HttpResponseRedirect("/hpl/")
    else:
        fm = Hpl_registration_form()
    return render(request,'ekta1/hplform.html', {'form': fm})


#Show HPL form 
def Show_Hpl_registrationform(request):
        fm= Hpl_registration.objects.all()
        return render(request, 'ekta1/show_hpl_form.html',{'form':fm})
