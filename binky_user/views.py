# -*- coding: UTF-8-*-

from django.shortcuts import render
from forms import UserInvitationForm
from django.template import RequestContext
from models import Invitacion
from django.http import Http404
from django.contrib.auth.models import User


def binky_user_user_invitation(request, invitation_uuid):

    invitacion_activa = False

    try:
        # Obtenemos la información de la invitación
        invitacion = Invitacion.objects.get(uuid=invitation_uuid)

        if invitacion.estaActiva():

            invitacion_activa = True

            if request.method == 'POST':

                invitacion_activa = True
                formulario = UserInvitationForm(request.POST)
                if formulario.is_valid():

                    # Damos de alta al usuario.
                    nuevoUsuario = User.objects.create_user(
                        username=formulario.cleaned_data['correo'],
                        password=formulario.cleaned_data['password'],
                        email=formulario.cleaned_data['correo']
                    )
                    nuevoUsuario.save()

                    # Desactivamos la invitación
                    invitacion.utilizada = True
                    invitacion.save()

                    return render(request, 'binky_user/page/user_invitation_ok.html',
                                  {'formulario': formulario, 'uuid': invitation_uuid,
                                   'invitacion_activa': invitacion_activa},
                                  context_instance=RequestContext(request))

            else:
                formulario = UserInvitationForm()
                formulario.fields['nombre'].initial = invitacion.nombre
                formulario.fields['correo'].initial = invitacion.correo

    except Invitacion.DoesNotExist:
        raise Http404

    return render(request, 'binky_user/page/user_invitation.html',
                              {'formulario': formulario, 'uuid': invitation_uuid,
                               'invitacion_activa': invitacion_activa},
                              context_instance=RequestContext(request))