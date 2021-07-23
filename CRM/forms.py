from django.forms import ModelForm
from .models import Worker, Client, Query


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('__all__')


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')


class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ('__all__')