from django.db import models

# Create your models here.
class TipoDeporte(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=1, default="A")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Deporte"
        verbose_name_plural = "Tipos de Deportes"
        ordering = ['id']