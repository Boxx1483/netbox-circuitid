from django.contrib import admin
from .models import CircuitID, CableCircuitID

@admin.register(CircuitID)
class CircuitIDAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(CableCircuitID)
class CableCircuitIDAdmin(admin.ModelAdmin):
    list_display = ('cable', 'circuit_id')
