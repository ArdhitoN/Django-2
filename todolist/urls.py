from django.urls import path

from .views import register
from .views import login_user
from .views import logout_user
from .views import show_todolist
from .views import create_task
from .views import set_status
from .views import delete_task
from .views import show_json
from .views import add_task
from .views import delete_task_async


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('set-status/<int:id>', set_status, name='set_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:id>', delete_task_async, name='delete_task_async'),
]