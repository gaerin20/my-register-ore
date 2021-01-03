from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import *
from formulari import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse,  HttpResponseNotModified
from django.http import HttpResponseBadRequest
from django.utils.encoding import smart_str
import csv


@csrf_exempt
#@login_required()
def addOre(request):
	note = None
    	oggi=datetime.date.today()
	delta=datetime.timedelta(days=7)
	datalimite=oggi - delta
	query="SELECT id, data, progetto_id, data, ora_inizio, ora_fine, (ora_fine - ora_inizio) as totale FROM register_ore where data > (current_date - integer '7')"
	sz = Ore.objects.raw(query)

	def errorHandle(error):
		form = InsertOreForm()
		return render_to_response( 'error.html',{
		 'error' : error,
		 'form' : form,
		})
	if (request.method == 'POST'):
		post = request.POST
		progetto = post['progetto']
		data = post['data']
		ora_inizio = post['ora_inizio']
		ora_fine = post['ora_fine']
		note = post['note']
		f = InsertOreForm(request.POST)
		if f.is_valid():
			new_ore=f.save()
		else:
			error = u'form is invalid'
			return errorHandle(error)
	else:
		f = InsertOreForm()
	return render_to_response('register/addOre.html',{'form':f,'selezione':sz,  })

@csrf_exempt
#@login_required()
def reportOre(request):
	note = None
    	query="SELECT id, data, progetto_id, data, ora_inizio, ora_fine, (ora_fine - ora_inizio) as totale FROM register_ore order by progetto_id, data"
	sz1 = Ore.objects.raw(query)

	def errorHandle(error):
		return render_to_response( 'error.html',{
		 'error' : error,
		 })

	return render_to_response('reportOre2.html',{'selezione':sz1,  })
@csrf_exempt
#@login_required()
def export_csv(request):
	filename = "ore.csv"
    	query="SELECT id, data, progetto_id, data, ora_inizio, ora_fine, (ora_fine - ora_inizio) as totale FROM register_ore order by progetto_id, data"
	sz1 = Ore.objects.raw(query)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename='+filename
	writer = csv.writer(response)
	response.write(u'\ufeff'.encode('utf8'))
	writer.writerow([
		smart_str(u"ID"),
		smart_str(u"progetto_id"),
		smart_str(u"data"),
		smart_str(u"ora_inizio"),
		smart_str(u"ora_fine"),
		smart_str(u"totale"),
	])
	for obj in sz1:
		writer.writerow([
			smart_str(obj.id),
			smart_str(obj.progetto),
			smart_str(obj.data),
			smart_str(obj.ora_inizio),
			smart_str(obj.ora_fine),
			smart_str(obj.totale),
		])
	return response
@csrf_exempt
def testData(request):
	return render_to_response('testData.html',{})
@csrf_exempt
def reportOreND(request):
	filename = "oreND.csv"
	
	def errorHandle(error):
		form = ReportOreForm()
		return render_to_response( 'error.html',{
		'error': error,
		'form' : form,
		})
	if (request.method == 'POST'):
		post = request.POST
		progetto_selezionato = post['progetto']
		data_da = post['data']
		f= ReportOreForm()
		sz = Ore.objects.filter(progetto = progetto_selezionato, data__gte = data_da)
		return render_to_response('reportOreND.html',{'form':f,'selezione':sz,  })
	else:
		f = ReportOreForm()
		return render_to_response('reportOreND.html',{'form':f,})
