__author__ = 'antonio'

from django import template
from django.template.base import Node
import datetime
from ..models import Evento, AsisteEvento

register = template.Library()


@register.tag
def evento_next(parser, token):
    return EventoNextNode()


@register.tag
def evento_last(parser, token):
    return EventoLastNode()


@register.tag
def evento_detalle(parser, token):
    return EventoDetalleNode()


class EventoNextNode(Node):
    def __init__(self, templ='binky_calendar/_tags/evento_next.html'):
        super(EventoNextNode, self).__init__()
        self.template = templ

    def render(self, context):
        nAsistentes = 0
        confirmado = False
        asiste = False
        evento_id = None
        try:
            # Obtenemos la siguiente ruta reciente.
            p = Evento.objects.filter(hora__gte=datetime.datetime.now())[0]
            evento_id = p.id
            nAsistentes = len(AsisteEvento.objects.filter(evento_id=evento_id, asiste=True))

            # Comprobamos si el evento existe.
            try:
                asistencia = AsisteEvento.objects.get(user_id=context['request'].user.id, evento_id=evento_id)
                confirmado = True
                asiste = asistencia.asiste
            except AsisteEvento.DoesNotExist:
                confirmado = False

        except IndexError:
            p = None

        t = template.loader.get_template(self.template)

        context.update({'nextruta': p, 'evento_id': evento_id, 'nAsistentes': nAsistentes, 'confirmado': confirmado,
                        'asiste': asiste})

        return t.render(context)


class EventoLastNode(Node):
    def __init__(self, templ='binky_calendar/_tags/evento_last.html'):
        super(EventoLastNode, self).__init__()
        self.template = templ

    def render(self, context):
        nAsistentes = 0
        evento_id = None
        try:
            # Obtenemos la siguiente ruta reciente.
            p = Evento.objects.filter(hora__lte=datetime.datetime.now()).order_by('-hora')[0]
            evento_id = p.id
            nAsistentes = len(AsisteEvento.objects.filter(evento_id=evento_id, asiste=True))

        except IndexError:
            p = None

        t = template.loader.get_template(self.template)

        context.update({'nextruta': p, 'evento_id': evento_id, 'nAsistentes': nAsistentes})

        return t.render(context)


class EventoDetalleNode(Node):
    def __init__(self, templ='binky_calendar/_tags/evento_detalle.html'):
        super(EventoDetalleNode, self).__init__()
        self.template = templ

    def render(self, context):
        try:
            # Obtenemos la siguiente ruta reciente.
            p = Evento.objects.filter(hora__gte=datetime.datetime.now())[0]

        except IndexError:
            p = None

        t = template.loader.get_template(self.template)

        context.update({'nextruta': p})

        return t.render(context)