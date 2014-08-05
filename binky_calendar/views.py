# -*- coding: UTF-8-*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from models import Evento, AsisteEvento
from django.views.decorators.csrf import requires_csrf_token


@login_required
def binky_calendar_evento_detalle(request, evento_id):

    try:
        p = Evento.objects.get(pk=evento_id)
    except Exception:
        p = None

    return render(request, 'binky_calendar/page/evento_detalle.html', {'nextruta': p})


# AJAX VIEWS
# -------------------------------------------------------------------------------------

@requires_csrf_token
@login_required
def binky_calendar_evento_asiste(request):

    confirmado = True
    asiste = False

    try:
        evento_id = request.GET['evento_id']
        user_id = request.GET['user_id']

        if request.GET['asiste'] == '1':
            asiste = True

        if request.GET['asiste'] == '2':
            borrado = True

        # Comprobamos si el evento existe.
        try:
            asistencia = AsisteEvento.objects.get(user_id=user_id, evento_id=evento_id)
            asistencia.asiste = asiste
            if borrado:
                asistencia.delete()
                confirmado = False
            else:
                asistencia.save()

        except AsisteEvento.DoesNotExist:
            asistencia = AsisteEvento()
            asistencia.user_id = user_id
            asistencia.evento_id = evento_id
            asistencia.asiste = asiste
            asistencia.save()

    except Exception:
        confirmado = False

    return render(request, 'binky_calendar/_ajax/evento_next_asistencia.html', { 'evento_id': evento_id, 'confirmado': confirmado, 'asiste': asiste})