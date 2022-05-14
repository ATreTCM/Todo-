from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import TodoDb
from .forms import TasksForm


@login_required
def createView(request):
    User = get_user_model()
    users = list(User.objects.all())
    if request.method == 'POST':
        task_form = TasksForm(request.POST, request.FILES)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.save()
            if task.slave:
                for u in users:
                    if str(u) in task.slave:
                        send_mail(
                            'Завдання',
                            'Для вас є нове завдання',
                            u.email,
                            ['atret1988@gmail.com']
                        )
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


