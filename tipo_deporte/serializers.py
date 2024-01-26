from rest_framework.serializers import ModelSerializer
from tipo_deporte.models import TipoDeporte

class TipoDeporteSerializer(ModelSerializer):
  class Meta:
    model = TipoDeporte
    fields = '__all__'
    
class SimplifiedTipoDeporteSerializer(ModelSerializer):
  class Meta:
    model = TipoDeporte
    fields = ['id', 'nombre']