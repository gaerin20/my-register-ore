from django.contrib import admin

# Register your models here.
from .models import Committente
from .models import Progetto
from .models import Preventivo
from .models import Fattura
from .models import Ore

admin.site.register(Committente)
admin.site.register(Progetto)
admin.site.register(Preventivo)
admin.site.register(Fattura)
admin.site.register(Ore)

