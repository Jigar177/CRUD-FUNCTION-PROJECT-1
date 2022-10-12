from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.

# This function will add new item and show all items.
def add_show(request):
    if request.method == 'POST':
        print('DATA VALIDATED')
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm,email= em,password= pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stude = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stud':stude})  


# this function will update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)     
    return render(request, 'enroll/updatestudent.html',{'form':fm})

# this function will delete data.

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')






   
