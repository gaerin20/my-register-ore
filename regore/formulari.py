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
