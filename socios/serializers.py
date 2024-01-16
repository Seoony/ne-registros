from rest_framework import serializers
from .models import Socio

class SocioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nombres = serializers.CharField(required=True, allow_blank=False, max_length=50)
    apellidos = serializers.CharField(required=True, allow_blank=False, max_length=50)
    dni = serializers.CharField(required=True, allow_blank=False, max_length=8)
    
    def create(self, validated_data):
        """
        Create and return a new `Socio` instance, given the validated data.
        """
        return Socio.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Socio` instance, given the validated data.
        """
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.save()
        return instance