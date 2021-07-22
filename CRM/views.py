from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from CRM.models import Worker, Client, Query


class IndexView(TemplateView):
    template_name = 'index.html'


class WorkerList(ListView):
    model = Worker
    template_name = 'worker_list.html'
    context_object_name = 'workers'
    queryset = Worker.objects.all()
