  
from django.urls import path
from .views import esempio_if,esempio_ifelse, esempio_elif, esempio_for
app_name = 'seconda_app'
urlpatterns = [
    path('if', esempio_if, name='if'),
    path('ifelse', esempio_ifelse, name='ifelse'),
    path('ifelif', esempio_elif, name='elif'),
    path('for', esempio_for, name='for'),
]