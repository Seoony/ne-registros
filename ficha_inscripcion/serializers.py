from rest_framework.serializers import ModelSerializer
from ficha_inscripcion.models import FichaInscripcion
from socios.serializers import SimplifiedSocioSerializer
from tipo_deporte.serializers import SimplifiedTipoDeporteSerializer

class FichaInscripcionSerializer(ModelSerializer):
  
  class Meta:
    model = FichaInscripcion
    fields = '__all__'
    
class ShowFichaInscripcionSerializer(ModelSerializer):
  socio = SimplifiedSocioSerializer(many=False)
  tipo_deporte = SimplifiedTipoDeporteSerializer(many=False)
  class Meta:
    model = FichaInscripcion
    fields = '__all__'