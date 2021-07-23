from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from CRM.forms import WorkerForm, ClientForm, QueryForm
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


class ClientsCreate(CreateView):
    template_name = 'update.html'
    form_class = ClientForm
    success_url = '/clients'


class ClientsUpdate(UpdateView):
    template_name = 'update.html'
    form_class = ClientForm
    success_url = '/clients'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Client.objects.get(pk=id)


class ClientsDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Client.objects.all()
    success_url = '/clients'


# заявки
class QueryList(ListView):
    model = Query
    queryset = Query.objects.all()
    template_name = 'query_list.html'
    context_object_name = 'queries'


class QuerysCreate(CreateView):
    template_name = 'update.html'
    form_class = QueryForm
    success_url = '/queries'


class QuerysUpdate(UpdateView):
    template_name = 'update.html'
    form_class = QueryForm
    success_url = '/queries'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Query.objects.get(pk=id)


class QuerysDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Query.objects.all()
    success_url = '/queries'