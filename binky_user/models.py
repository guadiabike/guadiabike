# -*- coding: UTF-8-*-
from django.db import models
from datetime import date, timedelta
import uuid


class Invitacion(models.Model):
    uuid = models.CharField(default=uuid.uuid4(), max_length=36, primary_key=True)
    correo = models.EmailField(max_length=250, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(default=date.today(), blank=False)
    utilizada = models.BooleanField(default=False, blank=False, null=False)

    def estaActiva(self):
        return not self.utilizada and self.fecha >= date.today()-timedelta(days=1)

    estaActiva.short_description = "Está activa la invitación"

    def __unicode__(self):
        return self.correo

    class Meta:
        verbose_name = 'Invitación para usuario'
        verbose_name_plural = 'Invitaciones usuarios'