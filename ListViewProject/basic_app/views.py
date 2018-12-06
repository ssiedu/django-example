from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView,
                                    UpdateView, DeleteView)
from basic_app import models
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'
    template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('school_name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('school_name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')