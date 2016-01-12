# Create your views here.
from principal.forms import *
from django.shortcuts import render_to_response
from models import *
from django.template import RequestContext
from tienda.recomendaciones import *
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

# def productos_usuario(request):
#     
#     if request.method == "POST":
#         busca_us = BusquedaForm(request.POST)
#         if busca_us.is_valid():
#             nombre_us = busca_us.cleaned_data["nombre_usuario"]
#             usuario_r = Usuario.objects.filter(username__contains=nombre_us)[0]
#             lista = usuario_r.puntuacion_set.all()
#             # puntuaciones=Puntuacion.objects.filter(usuario=usuario_r)
#             result = render_to_response("productos_use.html", {"puntuaciones":lista})
#         else:
#             result = render_to_response("busqueda_form.html", {"form":busca_us})
#             
#     else:
#         busca_us = BusquedaForm()
#         result = render_to_response("busqueda_prod.html", {"form":busca_us}, context_instance=RequestContext(request))
#     return result
