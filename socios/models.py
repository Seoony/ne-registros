from django.db import models

# Create your models here.
class Socio(models.Model):
  nombres = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=50)
  dni = models.CharField(max_length=8)
  #telefono = models.IntegerField()
  #email = models.EmailField()
  #direccion = models.CharField(max_length=50)
  #fecha_nacimiento = models.DateField()
  #fecha_ingreso = models.DateField()
  estado = models.CharField(max_length=1, default="A")

  def __str__(self):
    return self.nombres + " " + self.apellidos

  class Meta:
    verbose_name_plural = "Socios"
    verbose_name = "Socio"
    ordering = ['id']