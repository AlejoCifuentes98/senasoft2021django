from django.db import models


#Almacena los tiposde cartas
class Tipo(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre)

#Almacena las partidas
class Cartas(models.Model):
    nombre = models.CharField(max_length=80)
    tipo   = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='cards')
    def __str__(self):
        return str(self.nombre)
    
