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
from regore.models import Progetto
# Tipi base.
class Progetto_00(models.Model):
	anno = models.DateField("%Y")
	nome = models.CharField(max_length=200)
	luogo = models.CharField(max_length=100)
	protocollo = models.CharField(max_length=6)
	archivio = models.BooleanField(default = False, null = True, blank = True,)
	privato = models.BooleanField(default = False, null = True, blank = True,)
	def __str__(self):
		return u"%s %s" %(self.protocollo, self.nome)
	class Meta:
		verbose_name_plural = "Progetti"


class Diario(models.Model):
        DIARIO_TIPO = [
                ('co','consegna'),
                ('em','email'),
                ('in','incontro'),
                ('sv','sviluppo'),
                ('ev','evento'),
                ('no','nota'),
                ]
        data = models.DateField()
        progetto_00 = models.ForeignKey(Progetto_00,null=True,blank=True, on_delete=models.CASCADE,)
        progetto_01=models.ForeignKey(Progetto,null=True,blank=True,on_delete=models.CASCADE,)
        testo = models.TextField()
        link= models.URLField(blank=True,)
        tipo = models.CharField(max_length=100,choices=DIARIO_TIPO)
        firma = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,)
        def __str__(self):
                return u"%s %s" %(self.data, self.progetto_01)
        class Meta:
                verbose_name_plural = "Diario"


		
# classi per form.
