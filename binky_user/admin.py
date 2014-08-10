# -*- coding: UTF-8-*-

from django.contrib import admin
from binky_user import models


class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nombre', 'correo', 'fecha', 'utilizada', 'estaActiva')
    readonly_fields = ('uuid',)
    fieldsets = (
        (None, {
            'fields': ('uuid', 'nombre', 'correo', 'fecha'),
        }),
    )


admin.site.register(models.Invitacion, InvitacionAdmin)