from django.shortcuts import render, get_object_or_404
from . models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from intranet.decorators import role_required
from .forms import *
from .filters import adypu_filter
from django.urls import reverse
from django.contrib import messages


def index_bos(request, id=None):
    if request.method == "GET":
        data = adypu_data.objects.all()
        myFilter = adypu_filter(request.GET, queryset=data)
        data = myFilter.qs
        context = {}
        context['myfilter'] = myFilter
        context['data'] = data
    return render(request, 'control/bos.html', context)



def input_bos(request):
    if request.method == "GET":
        return render(request, 'control/inputbos.html')
    if request.method == "POST":
        sub_name = request.POST['sub_name']
        sub_code = request.POST['sub_code']
        course_type = request.POST['course_type']
        year_code = request.POST['year_code']
        school_name = request.POST['school_name']
        special = request.POST['special']
        data = adypu_data.objects.create(subject_name=sub_name, subject_code=sub_code, course_type=course_type, year_of_coding=year_code, school_name=school_name, specialization=special)
        if data:
            return HttpResponseRedirect(reverse('BOS'))
        else:
            return HttpResponse("Not sucessful")





