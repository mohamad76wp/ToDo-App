from django import forms
from .models import Task
from django.forms import ModelForm


class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','complete']

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    