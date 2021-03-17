from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse


# Create your views here.

def contatti (request): 
    #*************************************vecchia contatti (L23)***********************
    #form=FormContatto()
    #context={"form": form}
    #return render(request, "contatto.html", context)
    #**************************************nuovo (L24)*********************************
    
    if request.method == "POST": #se la richiesta è di tipo post, possiamo processare i dati
        form = FormContatto(request.POST) #creiamo l'istanza del form e la popoliamo con i dati della POST request(processo di binding)

        #is valid() controlla se il form inserito è valido
        if form.is_valid(): 
            #!RICORDA! cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di python
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            return HttpResponse("<h1> Grazie per averci contattato! </h1>")
    else:
        form = FormContatto()

    context = {"form":form}
    return render (request, "contatto.html", context)

