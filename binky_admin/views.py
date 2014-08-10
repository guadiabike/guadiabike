# -*- coding: UTF-8-*-

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, render_to_response, redirect
from forms import UserInvitationForm
from django.template import RequestContext
from guadiabike.templatetags import security
from django.core.mail import EmailMessage
from guadiabike.common.mail import InvitationMail
from binky_user import models


@login_required
@user_passes_test(security.has_group_administradores)
def binky_admin_index(request):
    return render(request, 'binky_admin/page/index.html')


@login_required
def binky_admin_user_invitation(request):
    if request.method == 'POST':
        formulario = UserInvitationForm(request.POST)
        if formulario.is_valid():

            try:
                # Creamos la invitación.
                nuevaInvitacion = models.Invitacion()
                nuevaInvitacion.correo = formulario.cleaned_data['correo']
                nuevaInvitacion.nombre = formulario.cleaned_data['nombre']

                nuevaInvitacion.save()

                # Enviamos el mensaje al usuario.
                url = request.build_absolute_uri('/user/invitation/' + nuevaInvitacion.uuid)

                nombre = formulario.cleaned_data['nombre']
                template = InvitationMail(nombre, url)

                msg = EmailMessage(u'Invitación Guadiabike BTT', template.getMail(), to=[formulario.cleaned_data['correo']])
                msg.content_subtype = "html"
                msg.send()

                message = u'Invitación enviada correctamente a ' + \
                          formulario.cleaned_data['correo'] + u' con mensaje "' + \
                          formulario.cleaned_data['mensaje'] + u'".'

            except Exception:
                message = u'No ha sido posible crear la invitación para ' + formulario.cleaned_data['correo']

            return render(request, 'binky_admin/page/message.html', {"message": message})

    else:
        formulario = UserInvitationForm()

    return render_to_response('binky_admin/page/user_invitation.html',
                              {'formulario': formulario},
                              context_instance=RequestContext(request))
