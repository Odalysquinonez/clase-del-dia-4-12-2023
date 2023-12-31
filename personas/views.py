from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.models import Persona


def detallePersona(request,id):
   # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona,pk=id)
    return render(request, 'personas/detalle.html',{'persona':persona})


PersonaForm = modelform_factory(Persona,exclude=[])


def nuevaPersona (request):
    if request.method == 'POST': #crear objeto
        formaPersona = PersonaForm(request.POST) #formulario lleno
        if formaPersona.is_valid():
           formaPersona.save()
           return redirect('inicio')

        else: #cuando hay formulario con errores
            return render(request, 'personas/nuevo.html',{'formaPersona':formaPersona})


    else: #solicitar formulario GET
        formaPersona = PersonaForm()
        return render(request, 'personas/nuevo.html',{'formaPersona':formaPersona})