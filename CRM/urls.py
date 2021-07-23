from django.urls import path

from CRM.views import IndexView, WorkerList, ClientList, QueryList, WorkersUpdate, WorkersDelete, WorkersCreate

urlpatterns = [
    path('', IndexView.as_view()),
    path('workers', WorkerList.as_view()),
    path('workers/add', WorkersCreate.as_view()),
    path('workers/<int:pk>', WorkersUpdate.as_view()),
    path('workers/delete/<int:pk>', WorkersDelete.as_view()),
    path('clients', ClientList.as_view()),
    path('queries', QueryList.as_view()),
]