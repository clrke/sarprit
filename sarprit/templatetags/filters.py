from django import template

register = template.Library()

@register.filter
def percentage(value):
    return "%.2f%%" % (value * 100)
