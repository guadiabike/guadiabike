# -*- coding: UTF-8-*-
__author__ = 'Antonio'

from django.forms import ModelForm
from django import forms


class UserInvitationForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    correo = forms.EmailField(label='Correo eléctronico de invitado', required=True, error_messages={'required': 'Correo electrónico es requerido.'})
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje para invitado', required=False)

