from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from intranet.decorators import role_required
from .models import *
from django.urls import reverse
from django.contrib import messages
import csv
from .forms import *
from .filters import answers_filter

# Create your views here.
@login_required(login_url="/login/")

def index(request):
    context = {}
    placement = Placements.objects.all()
    context['title'] = 'Companies'
    context['placement'] = placement
    return render(request, 'control/placead.html', context)

@login_required(login_url="/login/")
def details(request, id=None):
    if request.method == "GET":
        try:
            placement = Placements.objects.get(id=id)
        except:
            raise Http404
        form =ans_form()
        context = {}
        context['placement'] = placement
        context['form'] = form
        return render(request, 'student/detail.html', context)
    if request.method == "POST":
        user_id = request.user
        form = ans_form(request.POST)
    if form.is_valid():
        post = form.save()
        post.save()
        messages.success(request, "Successful")

            
def answer(request, id=None):
    if request.method == "GET":
        placement = Placements.objects.get(id=id)
        answer = Answer.objects.all()
        myFilter = answers_filter(request.GET, queryset=answer)
        answer = myFilter.qs
        context ={}
        context['myfilter'] = myFilter
        context['answer'] = answer
        context['user'] = request.user
        return render(request, 'control/answer.html', context)


def answer_backup(request):
    if request.method == "POST":
        response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Usernumber', 'URN', 'First Name', 'Last Name', 'Company'])
    for ans in Answer.objects.all().values_list('placement','user','username', 'firstname', 'lastname'):
        writer.writerow(ans)
    response['Content-Disposition'] = 'attachment; filename="student_names.csv"'
    return response


@login_required(login_url="/login/")
def single_choice(request, id=None):
    if request.method == 'POST':
        form = ans_form(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse('placement'))
    else:
        form = ans_form()
    return render(request, 'student/detail.html', {'form': form})



@login_required(login_url="/login/")
@role_required(allowed_roles = "Admin")
def add_placement(request):
    return render(request, 'control/add.html')


@login_required(login_url="/login/")
@role_required(allowed_roles = "Admin")
def create_placement(request):
    title = request.POST["title"]
    info = request.POST["info"]
    creator = request.user
    start_date = request.POST["start_date"]
    end_date = request.POST["end_date"]
    start_time = request.POST["start_time"]
    end_time = request.POST["end_time"]

    placement_info = Placements(title=title, information=info, created_by=creator, 
    start_date=start_date, end_date=end_date, start_time=start_time, end_time=end_time)
    placement_info.save()
    messages.success(request, "Successful")
    return render(request, 'control/add.html')

@login_required(login_url="/login/")
@role_required(allowed_roles = "Admin")
def placement_delete(request, id=None):
    placement = Placements.objects.get(id=id)
    
    if request.method == 'POST':
        placement.delete()
        messages.success(request, "Successful")
        return HttpResponseRedirect(reverse('placement'))
    else:
        context = {}
        context['placement'] = placement
        return render(request, 'control/delete.html', context)



def add_choice(request):
    if request.method == 'POST':
        form = choice_form(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse('add_choice'))
    else:
        form = choice_form()
    return render(request, 'control/add_choice.html', {'form': form})