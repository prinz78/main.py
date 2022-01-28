from django.shortcuts import render
from .form import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
