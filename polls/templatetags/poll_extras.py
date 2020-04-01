# encoding=utf-8

from django.template import Library

register = Library()


@register.filter()
def cut_all(var: str, arg: str):
    return var.replace(arg, '')
