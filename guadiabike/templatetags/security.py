# -*- coding: UTF-8-*-
__author__ = 'antonio'

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except Exception:
        group = None

    return True if group in user.groups.all() else False


def has_group_administradores(user):
    return has_group(user, 'administradores')