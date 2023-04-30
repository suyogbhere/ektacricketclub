from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import *
from .models import *
from .filters import BalVikas_Member_Subscription_Filter
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
import csv
# Create your views here.

# Show All Member Subscription 
@csrf_protect
def Show_BalVikas_Members_Subscription(request):
    if request.user.is_authenticated:
        fm1 = BalVikas_Member_Subscription.objects.all()
        fm2 = BalVikas_Member.objects.all()
        myfilter = BalVikas_Member_Subscription_Filter(request.POST, queryset=fm1)
        fm1 = myfilter.qs
        return render(request,'balvikas/show_balvikas_members_subscription.html',{'form1':fm1, 'form2':fm2,'SBVMS':'active', 'myfilter':myfilter})
    else:
        return HttpResponseRedirect("/login/")


@csrf_protect
def Add_BalVikas_Members_subscription(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=BalVikasMemberSubscriptionForm(request.POST)
            if fm.is_valid():
                nm=fm.cleaned_data['Name']
                sb=fm.cleaned_data['Subscription']
                yy=fm.cleaned_data['Year']
                dd=fm.cleaned_data['Date']
                data=BalVikas_Member_Subscription(Name=nm,Subscription=sb,Year=yy,Date=dd)
                data.save()
                messages.success(request,'वर्गणी जमा झाली !!!')
                return HttpResponseRedirect("/sbvms/")
        else:
            fm=BalVikasMemberSubscriptionForm()
        return render(request,'balvikas/add_balvikas_members_subscription.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")

@csrf_protect
def Add_BalVikas_Members(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=BalVikasMemberForm(request.POST)
            if fm.is_valid():
                nm=fm.cleaned_data['Name']
                data=BalVikas_Member(Name=nm)
                data.save()
                messages.success(request,'सभासद नोंद झाला!!!')
                return HttpResponseRedirect("/sbvms/")
        else:
            fm=BalVikasMemberForm()
        return render(request,'balvikas/add_balvikas_members.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


def Delete_BalVikas_Members_subscription(request,id):
    if request.method == 'POST':
        pi = BalVikas_Member_Subscription.objects.get(pk=id)
        pi.delete()
        messages.error(request,'सभासद वर्गणी डीलीट केली!!!!!')
        return HttpResponseRedirect('/sbvms/')

@csrf_protect
def Edit_BalVikas_Members_subscription(request,id):
    if request.method == 'POST':
        pi = BalVikas_Member_Subscription.objects.get(pk=id)
        fm1 = BalVikasMemberForm(request.POST, instance=pi)
        if fm1.is_valid():
            fm1.save()
            messages.success(request,'वर्गणीमध्ये बदल झाला!!!!!')
            return HttpResponseRedirect('/sbvms/')
    else:
        pi = BalVikas_Member_Subscription.objects.get(pk=id)
        fm1 = BalVikasMemberForm(instance=pi)
    return render(request,'balvikas/Edit_balvikas_members_subscription.html',{'form':fm1})


#download Bal Member subscription 
def BalVikas_export_to_csv(request):
    ems = BalVikas_Member_Subscription.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="BalVikas_export.csv"'
    writer = csv.writer(response)   
    writer.writerow(['ID','Name','Subscription','Date','Year'])
    for bms in ems:
        writer.writerow([bms.id,bms.Name, bms.Subscription, bms.Year])
    return response