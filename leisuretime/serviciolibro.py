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




         
        
def descarga(url, nombre_fich, driver):
    
    salida = open(nombre_fich, 'w')
    # driver = webdriver.Firefox()
    driver.get(url)
    s = driver.page_source.encode(sys.stdout.encoding, errors="replace")
    salida.write(s)
    # driver.close()
    salida.close()
    return s


def descarga_principal():
    driver = webdriver.Firefox()
    
    try:
        os.mkdir("libros")
    except Exception:
        print "Carpeta ya existente"
    
   
        
    descarga_books(driver)
    
    driver.close()

def descarga_book(isbn, id, driver):
    caracteres=10-len(isbn)
    url = "http://www.goodreads.com/search?query=" +"0"*caracteres +isbn
    nombre_fich = "libros/" + str(id) + ".txt"
    descarga(url, nombre_fich, driver)
    
    

def parsea_descripcion(soup):
    descripcion = soup.find("div", id="description")
    descripcion_t = ""
    if descripcion:
        opciones = descripcion.find_all("span")
        if len(opciones) == 2:
            descripcion_t = opciones[1].get_text()
        else:
            descripcion_t = opciones[0].get_text()
    return descripcion_t
    
def almacena_generos(libro, soup):
    geners_aux = []
    element = soup.find("div", class_="elementList")
    
    
    if element:
        caja = element.find_parent(class_="bigBoxBody")
        generos = caja.find_all(class_="left")
        
        for genero in generos:
            cat = genero.find("a").get_text()
           
        
            genero_r = Genero.objects.get_or_create(categoria=cat)[0]
            
        
    
            geners_aux.append(genero_r)
        libro.generos.add(*geners_aux)


     
    
    
          
def descarga_books(driver):
    
    lector = csv.reader(open("BX-Books.csv", "rb"), delimiter=";")
    
    for i, fila in enumerate(lector):
        if i > 0:
            descarga_book(fila[0], i, driver)
        


#descarga_principal()


def almacena_libro(fila, indice):

    nombreaut = fila[2]
    tituloaux = fila[1]
    isbnaux = fila[0]
    anyoaux = fila[3]
    nombreedit = fila[4]
    archivo = open("libros/" + str(indice) + ".txt")
    soup = bs4.BeautifulSoup(archivo.read(), "html.parser")
    archivo.close()
   
    autor_r = Autor.objects.get_or_create(nombre=nombreaut)[0]
    
         
   
    editorial_r = Editorial.objects.get_or_create(nombre=nombreedit)[0]
    
    
    
    descripcion_r = parsea_descripcion(soup)
    libro = Libro.objects.create(autor=autor_r, descripcion=descripcion_r, anyo=int(anyoaux), titulo=tituloaux, isbn=isbnaux, editorial=editorial_r)
    
    almacena_generos(libro, soup)

        
def almacena_libros():
    
    lector = csv.reader(open("BX-Books.csv", "rb"), delimiter=";")
    
    for i, fila in enumerate(lector):
        
        if  i > 0:
            print i
            almacena_libro(fila, i)
            
almacena_libros()
