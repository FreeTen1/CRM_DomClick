from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from CRM.filters import QueriesFilter
from CRM.forms import WorkerForm, ClientForm, QueryForm
from CRM.models import Worker, Client, Query


@method_decorator(staff_member_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'


# работники
@method_decorator(staff_member_required, name='dispatch')
class WorkerList(ListView):
    model = Worker
    queryset = Worker.objects.all()
    template_name = 'worker_list.html'
    context_object_name = 'workers'


@method_decorator(staff_member_required, name='dispatch')
class WorkersCreate(CreateView):
    template_name = 'update.html'
    form_class = WorkerForm
    success_url = '/workers'


@method_decorator(staff_member_required, name='dispatch')
class WorkersUpdate(UpdateView):
    template_name = 'update.html'
    form_class = WorkerForm
    success_url = '/workers'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Worker.objects.get(pk=id)


@method_decorator(staff_member_required, name='dispatch')
class WorkersDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Worker.objects.all()
    success_url = '/workers'
    context_object_name = 'worker'


# клиенты
@method_decorator(staff_member_required, name='dispatch')
class ClientList(ListView):
    model = Client
    queryset = Client.objects.all()
    template_name = 'client_list.html'
    context_object_name = 'clients'


@method_decorator(staff_member_required, name='dispatch')
class ClientsCreate(CreateView):
    template_name = 'update.html'
    form_class = ClientForm
    success_url = '/clients'


@method_decorator(staff_member_required, name='dispatch')
class ClientsUpdate(UpdateView):
    template_name = 'update.html'
    form_class = ClientForm
    success_url = '/clients'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Client.objects.get(pk=id)


@method_decorator(staff_member_required, name='dispatch')
class ClientsDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Client.objects.all()
    success_url = '/clients'


# заявки
@method_decorator(staff_member_required, name='dispatch')
class QueryList(ListView):
    model = Query
    queryset = Query.objects.all()
    template_name = 'query_list.html'
    context_object_name = 'queries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = QueriesFilter(self.request.GET, queryset=self.get_queryset())
        return context


@method_decorator(staff_member_required, name='dispatch')
class QuerysCreate(CreateView):
    template_name = 'update.html'
    form_class = QueryForm
    success_url = '/queries'


@method_decorator(staff_member_required, name='dispatch')
class QuerysUpdate(UpdateView):
    template_name = 'update.html'
    form_class = QueryForm
    success_url = '/queries'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Query.objects.get(pk=id)


@method_decorator(staff_member_required, name='dispatch')
class QuerysDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Query.objects.all()
    success_url = '/queries'
