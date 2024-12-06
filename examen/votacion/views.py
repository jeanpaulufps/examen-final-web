from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Encuesta, Opcion
from .serializers import EncuestaSerializer

class VotarOpcion(APIView):
    def post(self, request, opcion_id):
        opcion = get_object_or_404(Opcion, id=opcion_id)
        opcion.numero_votos += 1
        opcion.save()
        return Response({"mensaje": "Voto registrado exitosamente."}, status=status.HTTP_200_OK)

class VerResultados(APIView):
    def get(self, request, encuesta_id):
        encuesta = get_object_or_404(Encuesta, id=encuesta_id)
        serializer = EncuestaSerializer(encuesta)
        return Response(serializer.data, status=status.HTTP_200_OK)
