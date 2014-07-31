# -*- coding: UTF-8-*-

from django.contrib import admin
from binky_calendar import models


class DificultadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'nombre', 'descripcion'),
        }),
    )

    ordering = ('id',)


class EventoTipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'nombre', 'descripcion'),
        }),
    )

    ordering = ('id',)


class RutaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'imagen_principal', 'tiempo',
                    'distancia', 'desnivel_acumulado',
                    'dificultad', 'calorias', 'modalidad',
                    )
    list_filter = ('dificultad', 'nombre')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'nombre', 'descripcion', 'modalidad', 'imagen_principal'),
        }),
        ('Datos del recorrido', {
            'fields': ('tiempo', 'distancia', 'desnivel_acumulado', 'dificultad', 'calorias', ),
        }),
    )
    ordering = ('id',)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'eventoTipo', 'comentario', 'hora', 'ruta',
                    )
    list_filter = ('eventoTipo', )
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'eventoTipo', 'ruta', ),
        }),
        ('Información de la salida', {
            'fields': ('hora', 'comentario', ),
        }),
    )
    ordering = ('id',)


class AsisteEventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'evento', 'asiste')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'user', 'evento', 'asiste'),
        }),
    )

    ordering = ('id',)

admin.site.register(models.Dificultad, DificultadAdmin)
admin.site.register(models.EventoTipo, EventoTipoAdmin)
admin.site.register(models.Ruta, RutaAdmin)
admin.site.register(models.Evento, EventoAdmin)
admin.site.register(models.AsisteEvento, AsisteEventoAdmin)

