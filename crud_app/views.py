# crud_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Persona
from .forms import PersonaForm

# R: Leer (Listar todos) - Mapeada a la URL principal (/)
def persona_list(request):
    personas = Persona.objects.all()
    # Renderiza el template que muestra la lista
    return render(request, 'crud_app/persona_list.html', {'personas': personas})

# C: Crear & U: Actualizar (Maneja el formulario para ambos)
def persona_form(request, id=None):
    # Si hay un 'id', estamos editando; si no, estamos creando
    if id:
        persona = get_object_or_404(Persona, pk=id)
    else:
        persona = None

    # Inicializa el formulario con datos POST (si los hay) o con la instancia de Persona
    form = PersonaForm(request.POST or None, instance=persona)

    if request.method == 'POST' and form.is_valid():
        # Guarda la nueva persona o actualiza la existente
        form.save()
        # Redirige a la lista después de guardar
        return redirect('persona_list')

    # Renderiza el template del formulario
    return render(request, 'crud_app/persona_form.html', {'form': form})

# D: Eliminar
@require_POST # Solo permite solicitudes POST (más seguro para eliminar)
def persona_delete(request, id):
    persona = get_object_or_404(Persona, pk=id)
    persona.delete()
    return redirect('persona_list')