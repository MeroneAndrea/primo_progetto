from django.db import models

class Genere_ma(models.Model):
    genere= models.CharField(max_length=20)

    def __str__(self):
        return self.genere
    class Meta: 
        verbose_name="Genere"
        verbose_name_plural="Generi"

class Autore_ma (models.Model):
    nome= models.CharField(max_length=20)
    cognome= models.CharField(max_length=20)

    def __str__(self):
        return self.cognome
    class Meta: 
        verbose_name="Autore"
        verbose_name_plural="Autori"

class Libro_ma (models.Model): 
    titolo = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=20)
    autore = models.ForeignKey(Autore_ma, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere_ma)

    def __str__(self):
       return self.titolo

    class Meta: 
        verbose_name="Libro"
        verbose_name_plural="Libri"






