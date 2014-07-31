# -*- coding: UTF-8-*-

from django.db import models


# Modalidad: Carretera, BTT, etc
class Modalidad(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'