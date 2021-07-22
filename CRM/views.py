from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from CRM.models import Worker, Client, Query


class IndexView(TemplateView):
    template_name = 'index.html'


class WorkerList(ListView):
    model = Worker
    queryset = Worker.objects.all()
    template_name = 'worker_list.html'
    context_object_name = 'workers'


class ClientList(ListView):
    model = Client
    queryset = Client.objects.all()
    template_name = 'client_list.html'
    context_object_name = 'clients'


class QueryList(ListView):
    model = Query
    queryset = Query.objects.all()
    template_name = 'query_list.html'
    context_object_name = 'queries'
