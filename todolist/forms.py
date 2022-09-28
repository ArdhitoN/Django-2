from django import forms
from .models import Task


class Input_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 
            'description',
            ]

        labels = {
            'title' : 'Task Name',
            'description' : 'Task Description'
        }

        input_attrs = {
            'type' : 'text',
            'placeholder' : 'Nama Task',
        }

        input_attrs2 = {
            'type' : 'text',
            'placeholder' : 'Nama Task',
        }

        widgets = {
            'title' : forms.TextInput(),
            'description' : forms.TextInput(),
        }
