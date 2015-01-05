# -*- coding: UTF-8-*-

from django.db import models
from datetime import datetime


# Imagen
class Imagen(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=False)
    actived = models.BooleanField(default=True)
    udate = models.DateField(default=datetime.now(), editable=False)

    def __unicode__(self):
        return self.link

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'