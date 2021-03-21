from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
import datetime
from django.http import HttpRequest,HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .formulari import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse,  HttpResponseNotModified
from django.http import HttpResponseBadRequest
from django.utils.encoding import smart_str
from django.utils import timezone
import csv


@csrf_exempt
#@login_required()
def addOre(request):
        #note = None
        #sz = Ore.objects.filter(data__gte = (timezone.now() - timezone.timedelta(days=7)))
        sz=Ore.objects.latest('data','ora_fine')
        def errorHandle(error):
                form = InsertOreForm()
                return render_to_response( 'regore/error.html',{
                 'error' : error,
                 'form' : form,
                })
        if (request.method == 'POST'):
                
                form = InsertOreForm(request.POST)
                if form.is_valid():
                        form.cleaned_data['progetto']
                        form.cleaned_data['data']
                        form.cleaned_data['ora_inizio']
                        form.cleaned_data['ora_fine']
                        form.cleaned_data['note']
                        new_ore=form.save()
                        
                else:
                        error = u'form is invalid'
                        return errorHandle(error)
                sz=Ore.objects.latest('data','ora_fine')
                #post = request.POST
                #form = InsertOreForm({'progetto':post['progetto'], 'data':post['data']})
                form = InsertOreForm()
        else:
                form = InsertOreForm()
        return render_to_response('regore/addOre.html',{'form':form,'selezione':sz,  })
@csrf_exempt
#@login_required()
def reportOre(request):
        note = None
        query="SELECT id, data, progetto_id, data, ora_inizio, ora_fine, (ora_fine - ora_inizio) as totale FROM regore_ore order by progetto_id, data"
        sz1 = Ore.objects.raw(query)
        def errorHandle(error):
                return render_to_response( 'error.html',{
		'error' : error,
                })
        return render_to_response('regore/reportOre2.html',{'selezione':sz1,  })
def export_csv(request):
        filename = "ore.csv"
        sz1 = Ore.objects.order_by('progetto_id', 'data')
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
                
        ])
        for obj in sz1:
                writer.writerow([
                        smart_str(obj.id),
                        smart_str(obj.progetto),
                        smart_str(obj.data),
                        smart_str(obj.ora_inizio),
                        smart_str(obj.ora_fine),
                       
                ])
        return response
@csrf_exempt
def testData(request):
        return render_to_response('regore/testData.html',{})
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
                #la QuerySet sotto purtroppo non funziona perchè ora_fine - ora_inizio tralascia il computo dei minuti
                #sz = Ore.objects.filter(progetto = progetto_selezionato, data__gte = data_da).extra(select={'totale':"ora_fine - ora_inizio"})
                sz = Ore.objects.filter(progetto = progetto_selezionato, data__gte = data_da).order_by('data')
                #inizializzo una nuova tupla
                sz_t=[]
                for obj in sz:
                        dt0=obj.ora_inizio
                        dt1=obj.ora_fine
                        #trasformo le datetime.time in minuti e calcolo la durata
                        durata=(dt1.hour*60+dt1.minute)-(dt0.hour*60+dt0.minute)
                        #creo un nuovo oggetto datetime.time a partire dai minuti della durata usando il costruttore: datetime.time(H, m)
                        delta_dt=datetime.time(int(durata/60),durata%60)
                        #inizializzo un nuovo dizionario
                        obj1={}
                        #aggiungo i valori
                        obj1['data']=obj.data
                        obj1['progetto']=obj.progetto
                        obj1['ora_inizio']=obj.ora_inizio
                        obj1['ora_fine']=obj.ora_fine
                        obj1['totale']=delta_dt
                        obj1['note']=obj.note
                        #aggiungo il dizionario alla tupla che poi trasmetterò al template
                        sz_t.append(obj1)
                return render_to_response('regore/reportOreND.html',{'form':f,'selezione':sz_t,  })
        else:
                f = ReportOreForm()
                return render_to_response('regore/reportOreND.html',{'form':f,})
