from django.shortcuts import render
from dbapp.models import Student
from dbapp.forms import Studnetform
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
class HomePageView(ListView):
    model=Student
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Student
    form_class = Studnetform
    template_name = 'post.html'
    success_url = reverse_lazy('home')

