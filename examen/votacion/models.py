from django.db import models

# Create your models here.

from django.db import models

class Encuesta(models.Model):
    pregunta = models.CharField(max_length=255, verbose_name="Pregunta")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return self.pregunta

class Opcion(models.Model):
    texto = models.CharField(max_length=255, verbose_name="Texto de la opción")
    numero_votos = models.PositiveIntegerField(default=0, verbose_name="Número de votos")
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name="opciones", verbose_name="Encuesta")

    def __str__(self):
        return f"{self.texto} ({self.numero_votos} votos)"

