from django.urls import path
from .views import homepage, menu, chisiamo, variabili, index

urlpatterns = [
    path('welcome/', homepage, name='home'),
    path('menu/', menu, name='menu'),
    path('chisiamo/', chisiamo, name='chisiamo'),
    path('variabili/', variabili, name='variabili'),
    path('index/', index, name='index'),
]