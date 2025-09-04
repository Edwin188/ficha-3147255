from django.contrib import admin
from .models import actividad

class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", )

# Register your models here.
admin.site.register(actividad, ActividadAdmin)
