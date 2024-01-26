from rest_framework.serializers import ModelSerializer
from socios.models import Socio

class SocioSerializer(ModelSerializer):
  class Meta:
    model = Socio
    fields = '__all__'
    
class SimplifiedSocioSerializer(ModelSerializer):
  class Meta:
    model = Socio
    fields = ['id', 'nombres', 'apellidos']