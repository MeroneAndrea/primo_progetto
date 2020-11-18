from django.http import HttpResponse

# Create your views here.
def home(request): 
    return HttpResponse("<h1>Home page news!</h1>")