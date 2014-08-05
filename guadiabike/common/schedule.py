#!/usr/bin/python2.7
# -*- coding: UTF-8-*-
#
#
#
# Guadiabike Script Schedule

# DJANGO-POWERED

activate_this = '/home/guadiabike/.virtualenvs/django16/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

path = '/home/guadiabike/guadiabike'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'guadiabike.settings'


# Actualizamos la información de meteorología.



# Enviamos los correos de aviso a los usuarios para las próximas salidas.



# Enviamos los mensajes programados existentes para el día de hoy.