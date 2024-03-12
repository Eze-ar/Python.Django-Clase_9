from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    #defino metadatos
    class Meta:
        ordering = ['nombre']
    #defino metodos
    def __str__(self):
        return f'{self.nombre} / {self.email}'

