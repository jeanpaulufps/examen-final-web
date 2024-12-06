from django.urls import path
from . import views

urlpatterns = [
    path('api/matricular/<int:curso_id>/', views.matricular_estudiante, name='matricular_estudiante'),
    path('api/estudiantes/<int:curso_id>/', views.listar_estudiantes, name='listar_estudiantes'),
    path('', views.listar_cursos, name='listar_cursos'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]
