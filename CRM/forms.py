from django.forms import ModelForm
from .models import Worker


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('__all__')
