from django.urls import path

from .views import register
from .views import login_user
from .views import logout_user
from .views import show_todolist
from .views import create_task
from .views import set_is_finished
from .views import delete_task


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('set_is_finished/<int:id>', set_is_finished, name='set_is_finished'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]