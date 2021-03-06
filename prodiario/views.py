from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Diario
from regore.models import Progetto
from .formulari import InsertDiarioForm, CercaDiarioForm, CercaDiarioForm2

from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def diario_list(request):
    diarios=Diario.objects.latest('id')
    def errorHandle(error):
        f = CercaDiarioForm2()
        return render_to_response( 'prodiario/error.html',{
         'error' : error,
         'form' : f,
        })
    if (request.method == 'POST'):
        f=CercaDiarioForm2(request.POST)
        if f.is_valid():
            post = request.POST
            progetto_selezionato = f.cleaned_data['progetto_01']
            data_da = post['data']
            tipo = post['tipo']
            #firma = post['firma']
            sz= Diario.objects.filter(progetto_01 = progetto_selezionato).order_by('data')
            progetto=sz[0].progetto_01
            if tipo:
                sz= Diario.objects.filter(progetto_01 = progetto_selezionato,tipo = tipo).order_by('data')
            
            f = CercaDiarioForm2()
            #f.fields['progetto_01'].queryset = Progetto.objects.filter(archivio=False, privato=False).order_by('-anno')
        
               #sz= Diario.objects.filter(progetto = progetto_selezionato, data__gte = data_da,tipo = tipo, firma = firma).order_by('data')
            return render(request, 'prodiario/diario_list.html', {'diarios': sz, 'progetto':progetto})
    f = CercaDiarioForm2()
    #f.fields['progetto_01'].queryset = Progetto.objects.filter(archivio=False, privato=False).order_by('-anno')
    return render(request, 'prodiario/diario_search.html', {'form':f,})

@csrf_exempt
def addDiario(request):
    diarios=Diario.objects.latest('id')
    def errorHandle(error):
        form = InsertDiarioForm()
        return render_to_response( 'prodiario/error.html',{
         'error' : error,
         'form' : form,
        })
    if (request.method == 'POST'):
        form=InsertDiarioForm(request.POST)
        if form.is_valid():
            form.cleaned_data['data']
            form.cleaned_data['progetto_01']
            form.cleaned_data['testo']
            form.cleaned_data['link']
            form.cleaned_data['tipo']
            form.cleaned_data['firma']
            new_diario=form.save()
        else:
            error = u'form is invalid'
            return errorHandle(error)
        diarios=Diario.objects.latest('id')
        form = InsertDiarioForm(initial={'firma':request.user})
        form.fields['progetto_01'].queryset = Progetto.objects.filter(archivio=False, privato=False).order_by('-anno')
    else:
        form = InsertDiarioForm(initial={'firma':request.user})
        form.fields['progetto_01'].queryset = Progetto.objects.filter(archivio=False, privato=False).order_by('-anno')
    return render(request, 'prodiario/addDiario.html',{'form': form,'selezione': diarios,  })
