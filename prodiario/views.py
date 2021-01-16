from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Diario

def diario_list(request):
    diarios = Diario.object.all().order_by('progetto')
    return render(request, 'prodiario/diario_list.html', {'diarios': diarios})
