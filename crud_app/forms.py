# crud_app/forms.py
from django import forms
from .models import Persona
from datetime import date
from django.core.exceptions import ValidationError
import re # Módulo para usar expresiones regulares

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            # Widget para el DNI: fuerza solo números en el navegador (UX)
            'dni': forms.TextInput(attrs={'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")'}),
        }

    # ==========================================================
    # 1. VALIDACIÓN: DNI/CÉDULA (Solo números y Unicidad)
    # ==========================================================
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        
        # Validación 1.1: Asegura que sean solo dígitos
        if not dni.isdigit():
            raise ValidationError("El DNI/Cédula debe contener solo dígitos numéricos.")
            
        # Validación 1.2: Longitud mínima (opcional, ajusta si es necesario)
        if len(dni) < 5:
            raise ValidationError("El DNI debe tener al menos 5 caracteres.")

        # Validación 1.3: Unicidad (asegura que no exista otro DNI igual)
        if Persona.objects.filter(dni=dni).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este DNI/Cédula ya está registrado. Debe ser único.")

        return dni

    # ==========================================================
    # 2. VALIDACIÓN: NOMBRES (Solo letras y espacios)
    # ==========================================================
    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        # Expresión regular que solo permite letras (a-z, mayúsculas/minúsculas), acentos y espacios.
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombres):
            raise ValidationError("El nombre solo debe contener letras y espacios.")
        return nombres

    # ==========================================================
    # 3. VALIDACIÓN: APELLIDOS (Solo letras y espacios)
    # ==========================================================
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        # Expresión regular que solo permite letras, acentos y espacios.
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellidos):
            raise ValidationError("El apellido solo debe contener letras y espacios.")
        return apellidos

    # ==========================================================
    # 4. VALIDACIÓN: FECHA DE NACIMIENTO (Mayor de 18 años)
    # ==========================================================
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

        if fecha_nacimiento:
            hoy = date.today()
            # Calcula la edad
            edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

            if edad < 18:
                raise ValidationError("Debe ser mayor de 18 años para registrarse.")

        return fecha_nacimiento