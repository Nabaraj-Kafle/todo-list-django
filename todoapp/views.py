from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView , FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Task

class CustomLoginView(LoginView):
    template_name = 'todoapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name='todoapp/register.html'
    form_class =UserCreationForm 
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')  

    def form_valid(self, form):
        user =form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form) 
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated :
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tasks'] =context['tasks'].filter(user=self.request.user)
        context['count'] =context['tasks'].filter(complete=False).count()

        # Get status filter from GET parameter
        status_filter = self.request.GET.get('status')  # Check for a status filter in the URL
        
        if status_filter:
            # Filter based on the selected status
            context['tasks'] = context['tasks'].filter(status=status_filter)


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith= search_input)

        context['search_input']= search_input
        context['status_filter'] = status_filter  # Pass the current filter to the template


        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/task.html'

class TaskCreate(LoginRequiredMixin, CreateView) :
    model = Task
    fields = ['title', 'description', 'complete', 'due_date', 'status', 'category']    
    success_url = reverse_lazy('tasks')
    

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView) :
    model = Task
    fields = ['title', 'description', 'complete','due_date', 'status', 'category']     
    success_url = reverse_lazy('tasks')

    def get_object(self, queryset=None):
        # Ensure we get the task to update
        return get_object_or_404(Task, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.user = self.request.user  # Ensure the task belongs to the logged-in user
        return super().form_valid(form)

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('tasks')  








            











    