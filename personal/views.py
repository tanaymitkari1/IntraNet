from django.shortcuts import render
from . models import *
from . forms import *
from django.contrib.auth.models import User
# Create your views here.

def myprofile(request):
    all_subs = Subject.objects.all()
    student_name = User.objects.filter(groups="11")
    context = {}
    context['students'] = student_name
    context['subject'] = all_subs
    return render(request, "myprofile.html", context)

def add_sub(request):
    if request.method == "POST":
        sub_form = subject_form(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return render(request, 'control/add_sub.html')
        else: 
            return render(request, 'control/add_sub.html', {"form": sub_form})
    else:
        sub_form=subject_form()
        return render(request, 'control/add_sub.html', {"form": sub_form})