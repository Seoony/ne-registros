from django.db import models
from socios.models import Socio
from tipo_deporte.models import TipoDeporte

# Create your models here.
class FichaInscripcion(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    tipo_deporte = models.ForeignKey(TipoDeporte, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    monto_inscripcion = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.CharField(max_length=1, default="A")

    def __str__(self):
        return self.socio.nombres + " - " + self.tipo_deporte.nombre
    
    class Meta:
        verbose_name = "Ficha de Inscripcion"
        verbose_name_plural = "Fichas de Inscripciones"
        ordering = ['id']