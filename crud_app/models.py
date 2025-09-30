from django.db import models # <-- Solo esta importación al inicio

CIUDADES = [
    ('MDE', 'Medellín'),
    ('BOG', 'Bogotá'),
    ('CAL', 'Cali'),
    ('BCN', 'Barcelona'),
    ('UIO', 'Quito'),
    ('GYE', 'Guayaquil'),
]

GENERO_OPCIONES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]

class Persona(models.Model):
    dni = models.CharField(max_length=10, unique=True, verbose_name="DNI/Cédula")
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")

    genero = models.CharField(
        max_length=1,
        choices=GENERO_OPCIONES,
        default='M'
    )

    ciudad = models.CharField(
        max_length=3,
        choices=CIUDADES,
        default='MDE'
    )

    class Meta:
        verbose_name_plural = "Personas"
        ordering = ['apellidos']

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.dni})"