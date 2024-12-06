from rest_framework import serializers
from .models import Encuesta, Opcion

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['id', 'texto', 'numero_votos']

class EncuestaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ['id', 'pregunta', 'fecha_creacion', 'opciones']
