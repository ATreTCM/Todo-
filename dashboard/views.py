from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TodoDb
from .forms import TasksForm


@login_required
def createView(request):
    if request.method == 'POST':
        task_form = TasksForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('dashboard:list')
    else:
        task_form = TasksForm()
    return render(request, 'dashboard/create.html', {'task_form': task_form})


class TdListView(LoginRequiredMixin, ListView):
    model = TodoDb
    template_name = 'dashboard/list.html'
    context_object_name = 'list_content'
    raise_exception = True


class TdDetailView(LoginRequiredMixin, DetailView):
    model = TodoDb
    template_name = 'dashboard/details.html'
    context_object_name = 'detail_content'
    raise_exception = True


class TdUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoDb
    template_name = 'dashboard/update.html'
    fields = ['author',
              'header',
              'content',
              'slave',
              'photo',
              ]
    raise_exception = True


class TdDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoDb
    success_url = '/'
    template_name = 'dashboard/delete.html'
    raise_exception = True


