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
class InsertOreForm(ModelForm):
	class Meta:
		model = Ore
		fields = ('progetto','data','ora_inizio','ora_fine','note','collaboratore')
		widgets = {
			'data': forms.DateInput(attrs={'id':'id-data'}),
                        'ora_inizio': forms.TimeInput(),
		}
		
class ReportOreForm(ModelForm):
	class Meta:
		model = Ore
		fields = ('progetto','data')
		widgets = {
			'data': forms.DateInput(attrs={'id':'id-data'}),
		}

class InsertDiarioForm(ModelForm):
        class Meta:
                model = Diario0
                fields = ('progetto','data','testo','link','tipo','firma')
                widgets = {
                        'data': forms.DateInput(attrs={'id':'id-data'}),
                        'testo': forms.Textarea(attrs={'id':'id-textarea'}),
                }

class CercaDiarioForm(ModelForm):
        class Meta:
                model = Diario0
                fields = ('progetto','data','tipo','firma')
                required = {
                        'data' : False,
                        'tipo' : False,
                        'firma': False,
                }
                        
                widgets = {
                        'data': forms.DateInput(attrs={'id':'id-data'}),
                        
                }
class CercaDiarioForm2(ModelForm):
         class Meta:
                model = Diario0
                fields = ('progetto','data','tipo',)
                required = {
                        'data' : False,
                        'tipo' : False,
                        
                }
                        
                widgets = {
                        'data': forms.DateInput(attrs={'id':'id-data'}),
                        
                }
       
       
class CercaDiarioForm3(forms.Form):
       LISTA_TIPI = [
                ('','------'),  #questa riga serve per avere la possibilità di togliere questo filtro di ricerca
                ('in','consegna/ricezione'),
                ('tr','incontro/colloquio/avviso/email/posta'),
                ('nb','sviluppo/nota/promemoria'),
                ('td','todo/da fare'),
                ]
         
       progetto=forms.ChoiceField()
       data=forms.DateField(required = False, widget=forms.DateInput(attrs={'id':'id-data'}))
       tipo=forms.ChoiceField(choices=LISTA_TIPI, required = False)

