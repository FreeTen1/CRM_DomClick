from django.urls import path

from CRM.views import IndexView, WorkerList

urlpatterns = [
    path('', IndexView.as_view()),
]