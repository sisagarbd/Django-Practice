from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import View, TemplateView, ListView, DetailView
from first_app import models

class IndexView(ListView):
    context_object_name = 'musitian_list'
    model = models.Musitian 
    template_name = 'first_app/index.html'

class DetailView(DetailView):
    context_object_name = 'musitian'
    model = models.Musitian
    template_name = 'first_app/detail.html'