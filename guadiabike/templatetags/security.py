# -*- coding: UTF-8-*-
__author__ = 'antonio'

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    ingroup = False
    try:
        group = Group.objects.get(name=group_name)
        if group in user.groups.all():
            ingroup = True
    except Exception:
        ingroup = False

    return ingroup


def has_group_administradores(user):
    return has_group(user, 'administradores')