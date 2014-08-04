# -*- coding: UTF-8-*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta
from guadiabike.models import Modalidad
from django.utils import timezone


# Dificultad: Baja, Media, Alta, Muy Alta, etc
class Dificultad(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Dificultad'
        verbose_name_plural = 'Dificultad en rutas'


# Tipo de evento: entrenamiento, salida, etc
class EventoTipo(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de evento'
        verbose_name_plural = 'Tipos de eventos'


class Ruta(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(blank=False)
    imagen_principal = models.CharField(max_length=100, blank=False)
    tiempo = models.PositiveIntegerField(help_text="Tiempo en minutos.", null=True)
    distancia = models.PositiveIntegerField(help_text="Distancia total en kilómetros.", null=True)
    desnivel_acumulado = models.PositiveIntegerField(help_text="Desnivel acumulado en metros.", null=True)
    modalidad = models.ForeignKey(Modalidad)
    dificultad = models.ForeignKey(Dificultad)
    calorias = models.PositiveIntegerField(help_text='Calorías consumidas en kilocalorías.', null=True)
    mapa_url = models.CharField(help_text='Dirección URL del mapa.', max_length=1000, null=True, blank=True)
    imagen_perfil = models.CharField(max_length=100, blank=True, null=True)
    udate = models.DateField(default=datetime.now(), editable=False)
    uuser = models.ForeignKey(User, default=1, editable=False)
    uinformation = models.CharField(default='LOADDATA', max_length=200, editable=False)
    actived = models.BooleanField(default=True, editable=False)

    def tiempoFormateado(self):
        try:
            horas = self.tiempo / 60
            minutos = self.tiempo % 60
            return str(horas) + " horas " + str(minutos) + " minutos"
        except Exception:
            return "!"

    def desnivelAcumuladoFormateado(self):
        try:
            return str(self.desnivel_acumulado) + " metros"
        except Exception:
            return "!"

    def __unicode__(self):
        return u"%s %s kms" % (self.nombre,self.distancia)

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'


class Meteorologia(models.Model):
    fecha = models.DateField(primary_key=True)
    icono = models.CharField(max_length=250, null=True)
    precipitacion = models.PositiveIntegerField(null=True)
    temp_maxima = models.PositiveIntegerField(null=True)
    temp_minima = models.PositiveIntegerField(null=True)
    texto = models.CharField(max_length=100, null=True)
    humedad = models.PositiveIntegerField(null=True)
    viento = models.PositiveIntegerField(null=True)
    dir_viento = models.CharField(max_length=50, null=True)
    ico_viento = models.CharField(max_length=250, null=True)

    def __unicode__(self):
        return self.fecha + ' - ' + self.texto

    class Meta:
        verbose_name = 'Pronóstico meteorológico día'
        verbose_name_plural = 'Pronósticos meteorológicos'


class Evento(models.Model):
    comentario = models.TextField(blank=True, null=True)
    ruta = models.ForeignKey(Ruta)
    eventoTipo = models.ForeignKey(EventoTipo)
#    fecha = models.DateField(blank=False)
    hora = models.DateTimeField(blank=False)
    asistentes = models.ManyToManyField(User, through='AsisteEvento', related_name='asistentes')
    udate = models.DateField(default=datetime.now(), editable=False)
    uinformation = models.CharField(default='LOADDATA', max_length=200, editable=False)
    actived = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return u"%s %s" % (self.eventoTipo,self.ruta)

    def tiempoRestante(self):
        try:
            tiempo = self.hora - datetime.now()
            return str(tiempo.days) + " días restantes"
        except Exception:
            return "!"

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Salidas y entrenamientos'


class AsisteEvento(models.Model):
    user = models.ForeignKey(User)
    evento = models.ForeignKey(Evento)
    asiste = models.BooleanField(blank=False)
    udate = models.DateField(default=datetime.now(), editable=False)
    uinformation = models.CharField(default='LOADDATA', max_length=200, editable=False)

    def __unicode__(self):
        return str(self.user) + ' asistira al evento ' + str(self.evento)

    class Meta:
        verbose_name = 'Asiste a evento'
        verbose_name_plural = 'Asiste a evento'
        unique_together = (('user', 'evento'),)