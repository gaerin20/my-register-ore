# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from django.contrib.admin import widgets
from datetime import date

# Tipi base.
class Collaboratore(models.Model):
        nome = models.CharField(max_length=20)
        cognome = models.CharField(max_length=20)
        def __str__(self):
                return u"%s %s" %(self.nome, self.cognome)
        class Meta:
                verbose_name_plural = "Collaboratore"


class Progetto(models.Model):
	anno = models.DateField("%Y")
	nome = models.CharField(max_length=200)
	luogo = models.CharField(max_length=100)
	protocollo = models.CharField(max_length=6)        
	def __str__(self):
		return u"%s %s" %(self.protocollo, self.nome)
	class Meta:
		verbose_name_plural = "Progetti"


class Diario(models.Model):
        data = models.DateField()
        progetto = models.ForeignKey(Progetto,on_delete=models.CASCADE,)
        testo = models.TextField()
        tipo = models.CharField(max_length=100)
        firma = models.ForeignKey(Collaboratore,on_delete=models.CASCADE,)
        def __str__(self):
                return u"%s %s" %(self.data, self.progetto)
        class Meta:
                verbose_name_plural = "Diario"


		
# classi per form.
