from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from CRM.forms import WorkerForm
from CRM.models import Worker, Client, Query


class IndexView(TemplateView):
    template_name = 'index.html'


# работники
class WorkerList(ListView):
    model = Worker
    queryset = Worker.objects.all()
    template_name = 'worker_list.html'
    context_object_name = 'workers'


class WorkersCreate(CreateView):
    template_name = 'update.html'
    form_class = WorkerForm
    success_url = '/workers'


class WorkersUpdate(UpdateView):
    template_name = 'update.html'
    form_class = WorkerForm
    success_url = '/workers'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Worker.objects.get(pk=id)


class WorkersDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Worker.objects.all()
    success_url = '/workers'
    context_object_name = 'worker'


# клиенты
class ClientList(ListView):
    model = Client
    queryset = Client.objects.all()
    template_name = 'client_list.html'
    context_object_name = 'clients'


# заявки
class QueryList(ListView):
    model = Query
    queryset = Query.objects.all()
    template_name = 'query_list.html'
    context_object_name = 'queries'
