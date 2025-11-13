from django.contrib import admin
from .models import Vaca, Produccion, EventoSanitario

@admin.register(Vaca)
class VacaAdmin(admin.ModelAdmin):
    list_display = ('numero_identificacion', 'nombre', 'raza', 'fecha_nacimiento', 'corral_actual')
    search_fields = ('numero_identificacion', 'nombre', 'raza')

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('vaca', 'fecha_registro', 'cantidad_litros', 'turno')

@admin.register(EventoSanitario)
class EventoSanitarioAdmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'fecha_evento', 'veterinario', 'costo', 'dias_retiro', 'notas')

from .models import Personal, Ventas

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'puesto', 'salario', 'contacto')
    search_fields = ('nombre', 'apellido', 'puesto')

@admin.register(Ventas)
class VentasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'producto', 'cantidad', 'precio_unidad', 'precio_total', 'vendedor')
    search_fields = ('producto',)
