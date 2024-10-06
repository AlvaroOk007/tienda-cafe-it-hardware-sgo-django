from django import template
register = template.Library()

@register.filter
def dividir(value, arg):
    return value / arg

