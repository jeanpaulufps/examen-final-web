from django.urls import path
from votacion import views

urlpatterns = [
    path('api/votar/<int:opcion_id>/', views.VotarOpcion.as_view(), name='votar_opcion'),
    path('api/resultados/<int:encuesta_id>/', views.VerResultados.as_view(), name='ver_resultados'),
    path('', views.ListaEncuestasView.as_view(), name='lista_encuestas'),
    path('encuesta/<int:pk>/', views.DetalleEncuestaView.as_view(), name='detalle_encuesta'),
    path('encuesta/<int:pk>/votar/', views.votar, name='votar'),
]
