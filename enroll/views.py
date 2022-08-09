from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudenResgitration
from .models import User
# Create your views here.

#This Function show and add
def add_show(request):
    if request.method =='POST':
        fm = StudenResgitration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['company']
            reg = User(name=nm,email=em,company=pw)
            reg.save()
    else:
        fm = StudenResgitration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})

#This Function Will Delete

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#This Function will update/edit

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudenResgitration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudenResgitration(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})