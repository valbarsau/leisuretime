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
    lector = csv.reader(open("BX-Users.csv", "rb"), delimiter=";")
    
    for i, fila in enumerate(lector):
        
        if i>0:
            print i
            id_us=fila[0]
            nombre_u="user"+str(id_us)
            print nombre_u
            passw=django.contrib.auth.hashers.make_password(nombre_u)
            Usuario.objects.create(username=nombre_u,password=passw,id_usuario=id_us,localizacion=unicode(fila[1], errors="replace"))
           
almacena_usuario()
        
         

     
    
    
          
