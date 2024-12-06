from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import Encuesta, Opcion
from .serializers import EncuestaSerializer
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

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

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Encuesta, Opcion
import random

class ListaEncuestasView(ListView):
    model = Encuesta
    template_name = 'lista_encuestas.html'
    context_object_name = 'encuestas'

class DetalleEncuestaView(DetailView):
    model = Encuesta
    template_name = 'detalle_encuesta.html'
    context_object_name = 'encuesta'

def votar(request, pk):
    if request.method == "POST":
        opcion_id = request.POST.get('opcion')
        opcion = get_object_or_404(Opcion, id=opcion_id)
        opcion.numero_votos += 1
        opcion.save()
        return redirect('detalle_encuesta', pk=pk)
    return JsonResponse({"error": "Método no permitido"}, status=405)