from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import *



# Create your views here.
def eca(request):
    context = {}
    workshop = add_eca.objects.all()
    context['workshop'] = workshop
    return render(request, 'eca.html', context)

def add_workshop(request):
    if request.method == 'GET':
        return render(request, 'control/add_workshop.html')
    if request.method == 'POST':
        title = request.POST["title"]
        info = request.POST["info"]
        stdt = request.POST["start_date"]
        eddt = request.POST["end_date"]
        data = add_eca.objects.create(title=title, information=info, start_date=stdt, end_date=eddt)
        if data:
            messages.success(request, "sucessful")
            return HttpResponseRedirect(reverse('add_workshop'))


def workshop_delete(request, id=None):
    workshop = get_object_or_404(add_eca, id=id)
    if request.method == 'POST':
        workshop.delete()
        return HttpResponseRedirect(reverse('eca'))
    else:
        context = {}
        context['workshop'] = workshop
        return render(request, 'control/workshop_delete.html', context)

def workshop_details(request, id=None):
    if request.method == 'GET':
        try:
            workshop = add_eca.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['workshop'] = workshop
        return render(request, 'student/workshop_detail.html', context)
    if request.method == "POST":
        user_id = request.user_id
        data = Student_list.objectes.create(user=user_id)
        if data:
            message.sucess(request, "sucessful")
            return HttpResponseRedirect(reverse('eca'))