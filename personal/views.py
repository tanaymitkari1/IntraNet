from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .filters import sub_filter
from django.contrib import messages
from cart.cart import Cart
# Create your views here.

def myprofile(request):
    student_name = User.objects.filter(groups="11")
    my_subject = credit_reg.objects.filter(student=request.user)
    certis = certificates.objects.filter(user=request.user)
    context = {}
    context["list"]= my_subject
    context["certis"] = certis
    context['students'] = student_name
    return render(request, "myprofile.html", context)


def sub_list(request):
    if request.method == 'POST':
        form = ans_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('credit_registration'))
        else:
            return render(request, 'student/creditreg.html', {"form":form})
    else:
        form=ans_form()
        return render(request, 'student/creditreg.html', {"form":form})


def certi(request):
    user = request.user
    certi = request.FILES["certi"]
    data = certificates(user=user, image=certi)
    data.save()
    messages.success(request, "Successful")
    return redirect(reverse('myprofile'))


def del_sub(request, id=None):
    subs = credit_reg.objects.get(id=id)
    subs.delete()
    return HttpResponseRedirect(reverse('myprofile'))

def certi_delete(request, id=None):
    certis = certificates.objects.get(id=id)
    certis.delete()
    return HttpResponseRedirect(reverse('myprofile'))

"""
def creditreg(request, **kwargs):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    subs = Subject.objects.filter(id=kwargs.get('item_id', "")).first()
    sub_item, status = sub_ans.objects.get_or_create(sub_name=subs)
    student_credit, status = Subject.objects.get_or_create()
    credit_final, status = credit.objects.get_or_create(student=user_profile)
    credit_final.subs.add(student_credit)
    messsages.info(request, "Credit sucessfully subscribe")
    return redirect(reverse('savecredit'))

"""


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