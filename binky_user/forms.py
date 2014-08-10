# -*- coding: UTF-8-*-
__author__ = 'Antonio'

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms.util import ErrorList

class UserInvitationForm(forms.Form):
    nombre = forms.CharField(widget=forms.HiddenInput(), label='Nombre', required=True)
    correo = forms.CharField(widget=forms.HiddenInput(), label='Correo', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña', required=True,
                               error_messages={'required': 'Contraseña es obligatoria.'})
    repassword = forms.CharField(widget=forms.PasswordInput(), label='Repite contraseña', required=True,
                                 error_messages={'required': 'Repite contraseña es obligatoria.'})

    def clean_correo(self):

        correo = self.cleaned_data['correo']

        try:
            if User.objects.filter(username=correo).exists():
                raise ValidationError("Existe un usuario con ese correo dado de alta")

        except User.DoesNotExist:
            return correo

        return correo

    def clean(self):

        form_data = self.cleaned_data

        if form_data.get('password', '') != '' and form_data.get('repassword', '') != '' \
                and form_data.get('password', '') != form_data.get('repassword', ''):

            if not 'password' in self._errors:
                self._errors['password'] = ErrorList()
                self._errors['password'].append('Contraseñas no coinciden')

        return form_data