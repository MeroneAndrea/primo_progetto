
from django.urls import path
from .views import es_if,es_ifelse, es_elif, esfor
app_name = 'seconda_app'
urlpatterns = [
    path('if', es_if, name='if'),
    path('ifelse', es_ifelse, name='ifelse'),
    path('ifelif', es_elif, name='elif'),
    path('for', esfor, name='for'),
]