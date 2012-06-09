from django import template

register = template.Library()

@register.filter
def get_message(value, arg):
    """add some prefix for the given string"""
    return arg + str(value)
