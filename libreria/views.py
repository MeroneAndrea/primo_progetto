from django.shortcuts import render, get_object_or_404
from .models import Genere_ma, Autore_ma, Libro_ma
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 


def autoreDetailView(request, pk): 
    autore=get_object_or_404(Autore_ma, pk=pk)
    context={"autore": autore}
    return render(request, "autore_detail.html", context)

class AutoreDetailViewCB(DetailView): 
    model=Autore_ma
    template_name="autore_detail.html"

class LibroListView(ListView): 
    model=Libro_ma
    template_name="lista_libri.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["libri"]= Libro_ma.objects.all()
        return context
        
def index(request):

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'lista_libri.html', context=context)