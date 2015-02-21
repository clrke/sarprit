from django import template

register = template.Library()

@register.filter
def percentage(value):
    return "%.2f%%" % (value * 100)

@register.filter
def sentiment(value):
	if value == 0:
	   return "Negative"
	elif value == 2:
		return "Positive"
	else:
 		return "Neutral"
