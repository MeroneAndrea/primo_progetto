from django import forms
from .models import Contatto
from django.core.exceptions import ValidationError
class FormContatto(forms.ModelForm): 
    #nome = forms.CharField()
    #cognome = forms.CharField()
    #email = forms.EmailField()
    #contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "area testuale"}))
    class Meta: 
        model=Contatto
        fields="__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'compila questo campo', 'class': 'form-control'}),
            'cognome' : forms.TextInput(attrs={'placeholder': 'compila questo campo', 'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'placeholder': 'compila questo campo', 'class': 'form-control'}),
            'contenuto' : forms.TextInput(attrs={'placeholder': 'area testuale scrivi pure, almeno 20 caratteri', 'class': 'form-control'}),
        }

    def clean_contenuto(self): #nome funzione: clean_nomecampodavalidare
        dati=self.cleaned_data["contenuto"]
        if "parola" in dati: #parola non è ammesso
            raise ValidationError("il contenuto inserito viola le norme del sito!")
        if len(dati)<20:
            raise ValidationError("il contenuto è troppo breve!")
        return dati