from django.db import models
from apps.partida.models import Jugadores

#Almacena los tiposde cartas
class Tipo(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre)

#Almacena las partidas
class Cartas(models.Model):
    nombre = models.CharField(max_length=80)
    tipo   = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre)
    
class Cartas_Ocultas(models.Model):
    carta_des = models.PositiveSmallIntegerField()
    carta_mod = models.PositiveSmallIntegerField()
    carta_err = models.PositiveSmallIntegerField()

    
