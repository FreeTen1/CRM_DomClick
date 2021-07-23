from django.urls import path

from CRM.views import IndexView, WorkerList, ClientList, QueryList, WorkersUpdate, WorkersDelete, WorkersCreate, \
    ClientsCreate, ClientsDelete, ClientsUpdate, QuerysCreate, QuerysUpdate, QuerysDelete

urlpatterns = [
    path('', IndexView.as_view()),
    path('workers', WorkerList.as_view()),
    path('workers/add', WorkersCreate.as_view()),
    path('workers/<int:pk>', WorkersUpdate.as_view()),
    path('workers/delete/<int:pk>', WorkersDelete.as_view()),

    path('clients', ClientList.as_view()),
    path('clients/add', ClientsCreate.as_view()),
    path('clients/<int:pk>', ClientsUpdate.as_view()),
    path('clients/delete/<int:pk>', ClientsDelete.as_view()),

    path('queries', QueryList.as_view()),
    path('queries/add', QuerysCreate.as_view()),
    path('queries/<int:pk>', QuerysUpdate.as_view()),
    path('queries/delete/<int:pk>', QuerysDelete.as_view()),
]