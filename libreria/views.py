from django.shortcuts import render, get_object_or_404
from .models import Genere_ma, Autore_ma, Libro_ma
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 

def home(request):
    Genere= Genere_ma.objects.all()
    Autore=Autore_ma.objects.all()
    Libro= Libro_ma.objects.all()
    context={"Generi": generi, "Autori": autori, "Libro": libri}
    print(context)
    return render(request, "home.html", context)

class AutoreDetailViewCB(DetailView): 
    model=autore
    template_name="autore_detail.html"

class AutoreListView(ListView): 
    model=autore
    template_name="lista_articoli.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["autori"]= Autore_ma.objects.all()
        return context

class GenereDetailViewCB(DetailView): 
    model=Genere
    template_name="Genere_detail.html"

class GenereListView(ListView): 
    model=Genere
    template_name="lista_Generi.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["Generi"]= Genere_ma.objects.all()
        return context

class LibroDetailViewCB(DetailView): 
    model=Libro
    template_name="Libro_detail.html"

class GenereListView(ListView): 
    model=Libro
    template_name="lista_Libri.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["Libri"]= Libro_ma.objects.all()
        return context
