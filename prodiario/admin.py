from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Collaboratore
from .models import Progetto
from .models import Diario


admin.site.register(Collaboratore)
admin.site.register(Progetto)
admin.site.register(Diario)
