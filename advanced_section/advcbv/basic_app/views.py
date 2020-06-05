from django.shortcuts import render
from django.views.generic import (
    View, TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView)
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from django.urls import reverse

from django.urls import reverse_lazy

# Create your views here.

# def index(request):
#     return render(request,'basic_app/index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASE VIEW ARE COOL')


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inject'] = 'BASIC INJECTION!'
#         return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = "basic_app/school_detail.html"

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse(''))

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")