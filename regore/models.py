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
class Committente(models.Model):
	nome = models.CharField(max_length=100)
	cognome = models.CharField(max_length=100)
	indirizzo = models.CharField(max_length=200)
	luogo = models.CharField(max_length=200)
	telefono = models.CharField(max_length=20)
	cellulare = models.CharField(max_length=20)
	email1 = models.EmailField(max_length=100)
	email2 = models.EmailField(max_length=100)
	codfisc = models.CharField(max_length=16)
	piva = models.CharField(max_length=11)
	referente = models.CharField(max_length=100)
	def __str__(self):
		return self.cognome
	class Meta:
		verbose_name_plural = "Committenti"

class Progetto(models.Model):
        anno = models.DateField("%Y")
        nome = models.CharField(max_length=200)
        luogo = models.CharField(max_length=100)
        committente = models.ForeignKey(Committente,on_delete=models.CASCADE,)
        archivio = models.BooleanField(default = False, null = True, blank = True,)
        def __str__(self):
                return self.nome
        class Meta:
                verbose_name_plural = "Progetti"

class Preventivo(models.Model):
	progetto = models.ForeignKey(Progetto,on_delete=models.CASCADE,)
	data = models.DateField()
	descrizione = models.TextField()
	importo = models.FloatField()
	def __str__(self):
		return u"%s %s" %(self.data, self.progetto)
	class Meta:
		verbose_name_plural = "Preventivi"

class Fattura(models.Model):
	progetto = models.ForeignKey(Progetto,on_delete=models.CASCADE,)
	nr = models.IntegerField()
	data = models.DateField()
	descrizione = models.TextField()
	importo = models.FloatField()
	def __str__(self):
		return u"%s %s %s" %(self.nr, self.data, self.progetto)
	class Meta:
		verbose_name_plural = "Fatture"

class Ore(models.Model):
	data = models.DateField()
	progetto = models.ForeignKey(Progetto,on_delete=models.CASCADE,)
	ora_inizio = models.TimeField()
	ora_fine = models.TimeField()
	note = models.TextField()
	collaboratore = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,)
	def __str__(self):
		return u"%s %s" %(self.data, self.progetto)
	class Meta:
		verbose_name_plural = "Ore"
		
# classi per form.
