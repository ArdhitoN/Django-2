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
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import Input_Form

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

