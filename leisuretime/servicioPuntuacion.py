'''
Created on 27/12/2015

@author: valentin
'''
from selenium import webdriver
import sys
import bs4
import re
import os
from datetime import datetime
from principal.models import *
import csv
from django.db import IntegrityError
import django.contrib.auth.hashers


def almacena_usuario():
    lector = csv.reader(open("BX-ratings.csv", "rb"), delimiter=";")
    
    for i, fila in enumerate(lector):
        
        if i>0:
            print i
            id_us=fila[0]
            
            usuario_r=Usuario.objects.get(id_usuario=int(id_us))
            libros=Libro.objects.filter(isbn__contains=fila[1])
            #passw=django.contrib.auth.hashers.make_password(nombre_u)
            if usuario_r and len(libros)>0:
                libro_r=libros[0]
                Puntuacion.objects.create(usuario=usuario_r,libro=libro_r,puntuacion=int(fila[2]))
           
almacena_usuario()
        
         

     
    
    
          
