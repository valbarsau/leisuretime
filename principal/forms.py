'''
Created on 27/11/2015

@author: valentin
'''
from django import forms
from principal.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        widgets={"username":forms.TextInput(attrs={'class': u'form-control'}),
                 "email":forms.TextInput(attrs={'class': u'form-control'}),
        "first_name":forms.TextInput(attrs={'class': u'form-control'}),
        "last_name":forms.TextInput(attrs={'class': u'form-control'}),
        }
    def save(self, commit=True):
        usuario = super(UserForm, self).save(commit=False)
        # user.username=self.cleaned_data["username"]
        password = self.cleaned_data["password1"]
        usuario.set_password(password)
        if commit:
            usuario.save()
        return usuario

class PuntuacionForm(forms.ModelForm):
    
    class Meta:
        model = Puntuacion
        fields = ("puntuacion",)
        #declaramos un widget para poder escoger el tipo de input y modificar los atributos de las tags
        widgets={"puntuacion":forms.TextInput(attrs={'class': u'form-control'})
                 }
    def save(self,usuario,libro,commit=True):
        puntuacion = super(PuntuacionForm, self).save(commit=False)
        
        
        puntuacion.usuario=usuario
        puntuacion.libro=libro
        
        if commit:
            puntuacion.save()
        return puntuacion