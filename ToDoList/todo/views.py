from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
       return reverse_lazy('todo:tasklist')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'placeholder': 'Username...'})
        form.fields['password'].widget.attrs.update({'placeholder': 'Password...'})
        return form


class Register(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo:tasklist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'placeholder': 'Username...'})
        form.fields['password1'].widget.attrs.update({'placeholder': 'Password...'})
        form.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Paswword...'})
        return form


def index(request):
    context = {}
    return render(request, 'todo/index.html', context)


@login_required(login_url='/todo/login/')
def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks,
               }
    return render(request, 'todo/tasks.html', context)





#Adding extra context
#https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/tasklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['tasks'].filter(user=self.request.user)

        selected_category = self.request.GET.get('category_filter', '')
        if selected_category:
            tasks = tasks.filter(category_id=selected_category)

        context['tasks'] = tasks
        context['categories'] = Category.objects.all()
        context['selected_category'] = int(selected_category) if selected_category else None
        return context

class TaskDetail(DetailView, LoginRequiredMixin):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'

class TaskCreate(CreateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    #fields = ['title', 'content', 'category', 'priority']
    template_name = 'todo/create_task_form.html'
    success_url = reverse_lazy('todo:tasklist')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({'placeholder': 'New task...'})
        form.fields['content'].widget.attrs.update({'placeholder': 'Add Description...'})
        form.fields['priority'].widget.attrs.update({'class': 'priorityCheckbox'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    #fields = ['title', 'content', 'category', 'priority', 'complete']
    success_url = reverse_lazy('todo:tasklist')
    template_name = 'todo/task_form.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({'placeholder': 'Task...'})
        form.fields['content'].widget.attrs.update({'placeholder': 'Description...'})
        form.fields['priority'].widget.attrs.update({'class': 'priorityCheckbox'})
        form.fields['complete'].widget.attrs.update({'class': 'completeCheckbox'})
        return form


class TaskDelete(DeleteView, LoginRequiredMixin):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo:tasklist')
    template_name = 'todo/task_confirm_delete.html'
















