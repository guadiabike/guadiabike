# -*- coding: UTF-8-*-

from django.contrib import admin
from binky_calendar import models


class ModalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'nombre', 'descripcion'),
        }),
    )

    ordering = ('id',)

admin.site.register(models.Modalidad, ModalidadAdmin)
