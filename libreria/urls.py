from django.urls import path
from .views import LibroListView, AutoreDetailViewCB

app_name="libreria"

urlpatterns=[
    path("lista_libri/",LibroListView.as_view(), name="lista_libri"),
    path("autore/<int:pk>", AutoreDetailViewCB.as_view(), name="autore_detail"),
]