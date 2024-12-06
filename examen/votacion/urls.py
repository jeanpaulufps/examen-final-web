from django.urls import path
from .views import VotarOpcion, VerResultados

urlpatterns = [
    path('votar/<int:opcion_id>/', VotarOpcion.as_view(), name='votar_opcion'),
    path('resultados/<int:encuesta_id>/', VerResultados.as_view(), name='ver_resultados'),
]
