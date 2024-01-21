from rest_framework.serializers import ModelSerializer
from ficha_inscripcion.models import FichaInscripcion

class FichaInscripcionSerializer(ModelSerializer):
    class Meta:
        model = FichaInscripcion
        fields = '__all__'