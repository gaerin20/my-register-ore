# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from .models import *
from django import forms
from django.forms import ModelForm
#from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateTimeInput
from django.contrib.admin import widgets
from datetime import date


# classi per form.
class InsertDiarioForm(ModelForm):
        class Meta:
                model = Diario
                fields = ('progetto','data','testo','link','tipo','firma')
                widgets = {
                        'data': forms.DateInput(attrs={'id':'id-data'}),
                        'testo': forms.Textarea(attrs={'id':'id-textarea'}),
                }

class CercaDiarioForm(ModelForm):
        class Meta:
                model = Diario
                fields = ('progetto','data','tipo','firma')
                required = {
                        'data' : False,
                        'tipo' : False,
                        'firma': False,
                }
                        
                widgets = {
                        'data': forms.DateInput(attrs={'id':'id-data'}),
                        
                }
class CercaDiarioForm2(forms.Form):
       LISTA_TIPI = [
                ('','------'),  #questa riga serve per avere la possibilità di togliere questo filtro di ricerca
                ('co','consegna'),
                ('em','email'),
                ('in','incontro'),
                ('sv','sviluppo'),
                ('ev','evento'),
                ('no','nota'),
                ]
       #formo lista progetti
       qs_pro=Progetto.objects.all()  #per avere una lista progetti da cui sceglere
       LISTA_PROGETTI=[]
       for obj in qs_pro:
               LISTA_PROGETTI.append((obj.id,obj))  #obj.id , obj perchè la lista Choices eve essere una lista di coppie key, value
       #analogamente formo lista dei collaboratori      
       #qs_collab=Collaboratori.objects.all() 
       #LISTA_COLLABORATORI=[('','-----'),]
       #for obj in qs_collab:
               #LISTA_COLLABORATORI.append((obj.nome[0]+obj.cognome[0],obj)) 

       progetto=forms.ChoiceField(choices=LISTA_PROGETTI)
       data=forms.DateField(required = False, widget=forms.DateInput(attrs={'id':'id-data'}))
       tipo=forms.ChoiceField(choices=LISTA_TIPI, required = False)
       #firma=forms.ChoiceField(choices=LISTA_COLLABORATORI, required = False)
