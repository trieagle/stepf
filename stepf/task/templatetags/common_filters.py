from django import template

register = template.Library()

@register.filter
def add_prefix(value, arg):
    """add some prefix for the given string"""
    return arg + str(value)

