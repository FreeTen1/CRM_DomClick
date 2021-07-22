from django.urls import path

from CRM.views import IndexView, WorkerList, ClientList, QueryList

urlpatterns = [
    path('', IndexView.as_view()),
    path('workers', WorkerList.as_view()),
    path('clients', ClientList.as_view()),
    path('queries', QueryList.as_view()),
]