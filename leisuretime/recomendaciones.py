'''
Created on 08/01/2016

@author: valentin
'''
import pickle
from principal.models import *
import recommendations

def calcula_valoraciones():
    users = Usuario.objects.all()
    usuarios_libros = {}
    for usuario in users:
      
        libros_p = {}
        for puntuacion in usuario.puntuacion_set.all():
        
            libros_p[puntuacion.libro] = puntuacion.puntuacion
    
        usuarios_libros[usuario.id] = libros_p
    #print usuarios_libros
    pickle.dump(usuarios_libros, open( "diccionario.p", "wb" ))

def recomienda(id_usuario):
    usuarios_libros={}
    try:
        usuarios_libros=pickle.load( open( "diccionario.p", "rb" ) )
        if not id_usuario in usuarios_libros.keys():
            calcula_valoraciones()
            usuarios_libros=pickle.load( open( "diccionario.p", "rb" ) )
    except IOError:
        calcula_valoraciones()
        usuarios_libros=pickle.load( open( "diccionario.p", "rb" ) )
        
            
    return recommendations.getRecommendations(usuarios_libros, id_usuario)
#busca usuarios a los que se les pueda recomendar
def encuentra_ids():
    for i in range(45,300):
        try:
            if len(recomienda(i))>0:
                usuario=Usuario.objects.get(id=i)
                print usuario
        except Exception:
            pass    
