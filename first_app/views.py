from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from first_app import models
from django.urls import reverse_lazy

class IndexView(ListView):
    context_object_name = 'musitian_list'
    model = models.Musitian 
    template_name = 'first_app/index.html'

class DetailView(DetailView):
    context_object_name = 'musitian'
    model = models.Musitian
    template_name = 'first_app/detail.html'

class AddMusitian(CreateView):
    fields = ('first_name', 'last_name', 'instument')
    model = models.Musitian
    template_name = 'first_app/musitian_form.html'

class UpdateMusitian(UpdateView):
    fields = ('first_name', 'last_name',)
    model = models.Musitian
    template_name = 'first_app/musitian_form.html'

class DeleteMusitian(DeleteView):
    context_object_name = 'musitian'
    model = models.Musitian
    success_url = reverse_lazy("first_app:index")
    template_name = 'first_app/delete_musitian.html'