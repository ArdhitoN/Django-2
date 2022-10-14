from urllib import request
from django.shortcuts import render
from .models import Task

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

# For cookies
import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from .forms import Input_Form


from django.core import serializers

from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_objects = Task.objects.filter(user = request.user)
    context  = {
        'todolist_list' : todolist_objects,
        # 'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            #response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    #response.delete_cookie('last_login')
    return response

def create_task(request):
    response = {'input_form' : Input_Form}
    if request.method == 'POST':
        user = request.user
        form = Input_Form(request.POST or None)
        form.instance.date = datetime.datetime.now()
        form.instance.user = user
        if(form.is_valid and request.method == 'POST'):
            form.save()
            # return HttpResponseRedirect('/todolist')
        # else:
        #     return HttpResponseRedirect('/todolist')
    
    return render(request, 'create-task.html', response)

def delete_task(request, id):
    task_objects = Task.objects.get(pk=id)
    task_objects.delete()

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def set_status(request, id):
    task_object = Task.objects.get(pk=id)
    if(task_object.is_finished):
        task_object.is_finished = False
    else:
        task_object.is_finished = True
    task_object.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))
   
def show_json(request):
    print("asijdoasdjka")
    todolist_objects = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", todolist_objects), content_type="application/json")

# def add_task(request):
#     response = {'input_form' : Input_Form}
#     if request.method == 'POST':
#         userLogged = request.user
#         form = Input_Form(request.POST or None)
#         form.instance.date = datetime.datetime.now()
#         form.instance.user = userLogged
#         if(form.is_valid):
#             dataFields = form.cleaned_data
#             todo = Task.objects.create(**dataFields, user=userLogged)
#             response = {
#                 "pk":todo.pk,
#                 "fields":{
#                     "title": todo.title,
#                     "description":todo.description,
#                     "date":todo.date,
#                     "is_finished":todo.is_finished
#                 }
#             }

#     return JsonResponse(response)
def add_task(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = datetime.datetime.now()

        new_task = Task(user=user, title=title, description=description, date=date)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()



def delete_task_async(request, id):
    if(request.method == 'GET'):
        task_objects = Task.objects.get(pk=id)
        task_objects.delete()

        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()