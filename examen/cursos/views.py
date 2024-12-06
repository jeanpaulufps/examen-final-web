from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Curso, Estudiante
from .serializers import EstudianteSerializer, CursoSerializer
from django.shortcuts import get_object_or_404, redirect
from .forms import MatricularEstudianteForm


# Create your views here.

@api_view(['POST'])
def matricular_estudiante(request, curso_id):
    try:
        curso = Curso.objects.get(id=curso_id)
    except Curso.DoesNotExist:
        return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    # Verificar si el estudiante está presente en los datos de la solicitud
    if request.method == 'POST':
        estudiante_data = request.data
        # Crear o obtener al estudiante
        estudiante, created = Estudiante.objects.get_or_create(
            email=estudiante_data['email'],
            defaults={'nombre': estudiante_data['nombre']}
        )

        # Matricular al estudiante en el curso
        estudiante.cursos.add(curso)

        # Serializar los datos del estudiante
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def listar_estudiantes(request, curso_id):
    try:
        curso = Curso.objects.get(id=curso_id)
    except Curso.DoesNotExist:
        return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    estudiantes = curso.estudiantes.all()  # Relación de muchos a muchos

    # Serializar la lista de estudiantes
    serializer = EstudianteSerializer(estudiantes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiantes = curso.estudiantes.all()

    if request.method == 'POST':
        form = MatricularEstudianteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            
            # Crear el estudiante o buscar si ya existe
            estudiante, created = Estudiante.objects.get_or_create(
                email=email,
                defaults={'nombre': nombre}
            )
            
            # Matricular al estudiante en el curso
            estudiante.cursos.add(curso)
            return redirect('detalle_curso', curso_id=curso.id)
    else:
        form = MatricularEstudianteForm()

    return render(request, 'detalle_curso.html', {
        'curso': curso,
        'estudiantes': estudiantes,
        'form': form
    })
