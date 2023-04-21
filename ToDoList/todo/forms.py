from django.forms import forms, ModelChoiceField
from django.forms import ModelForm

from .models import *


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'category', 'priority', 'complete']

    category = ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Category",
        required=False,
    )
