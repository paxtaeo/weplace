from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import User

class MyUserCreationForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
       model = User
       fields = ['username']

class UserCreate(generic.edit.CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('accounts:register-done')

class UserCreateDone(generic.TemplateView):
    template_name = 'registration/register_done.html'
