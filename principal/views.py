# Create your views here.
from principal.forms import *
from django.shortcuts import render_to_response
from models import *
from django.template import RequestContext
from principal.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from leisuretime.recomendaciones import *
from leisuretime import recomendaciones
def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))

def registrar(request):

    result = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            result = HttpResponseRedirect("/")
        else:
            result = render_to_response("registro.html", {"form":form}, context_instance=RequestContext(request))
    else:
        form = UserForm()
        result = render_to_response("registro.html", {"form":form}, context_instance=RequestContext(request))
    return result


def entrar(request):

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        # if form.is_valid():
        usuario = request.POST["username"]
        clave = request.POST["password"]
        acceso = authenticate(username=usuario, password=clave)
       
        if acceso is not None:
            if acceso.is_active:
                login(request, acceso)
                result = render_to_response("privado.html", context_instance=RequestContext(request))
            else:
                    result = render_to_response("no_activo.html")
        else:
            result = render_to_response("no_activo.html")
            
    else:
        form = AuthenticationForm()
        result = render_to_response("entrar.html", {"form":form}, context_instance=RequestContext(request))
    return result

@login_required(login_url='/user/entrar')
def cierre_sesion(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url='/user/entrar')
def libros_usuario(request):

    
    user = request.user
    if(user.is_authenticated()):
        usuario = Usuario.objects.get(id=user.id)
        lista = usuario.puntuacion_set.all()
        result = render_to_response("libros_use.html", {"puntuaciones":lista}, context_instance=RequestContext(request))
    return result



@login_required(login_url='/user/entrar')
def libros_no_puntuados(request):

    
    
    user = request.user
    if(user.is_authenticated()):
        usuario_r = Usuario.objects.get(id=user.id)
        lista = Libro.objects.exclude(puntuacion__usuario=usuario_r)
        
        
        
        result = render_to_response("libros_no.html", {"libros":lista}, context_instance=RequestContext(request))
    return result

def info(request,id_libro):
    libro=Libro.objects.get(id=id_libro)
    result = render_to_response("libro_info.html", {"libro":libro}, context_instance=RequestContext(request))
    return result
@login_required(login_url='/user/entrar')    
def recomienda(request):
    user=request.user
    usuario_r = Usuario.objects.get(id=user.id)
    libros_t=recomendaciones.recomienda(usuario_r.id)
    libros=[]
    for libro in libros_t:
        libros.append(libro[1])
    if len(libros)>10:
        libros=libros[:10]
    result = render_to_response("libros.html", {"libros":libros}, context_instance=RequestContext(request))
    return result
@login_required(login_url='/user/entrar')
def puntuar(request,id_libro):

    result = None
    if request.method == "POST":
        form = PuntuacionForm(request.POST)
        if form.is_valid():
           
            usuario = Usuario.objects.get(id=request.user.id)
            libro=Libro.objects.get(id=int(id_libro))
            form.save(usuario,libro)
            result = HttpResponseRedirect("/")
        else:
            result = render_to_response("puntuacion_form.html", {"id":id_libro,"form":form}, context_instance=RequestContext(request))
    else:
        form = PuntuacionForm()
        
        result = render_to_response("puntuacion_form.html", {"id":id_libro,"form":form}, context_instance=RequestContext(request))
    return result

def listar(request):
    libros=Libro.objects.all()
    result = render_to_response("libros.html", {"libros":libros}, context_instance=RequestContext(request))
    return result

