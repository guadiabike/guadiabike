# -*- coding: UTF-8-*-

from django.contrib import admin
from binky_media import models


class ImagenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'link', 'actived')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id', 'nombre', 'descripcion', 'link', 'actived'),
        }),
    )

    ordering = ('id',)


admin.site.register(models.Imagen, ImagenAdmin)