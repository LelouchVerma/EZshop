from django import template

register = template.Library()

@register.filter(name = 'currency')
def currency(n):
    return "Rs. " + str(n)

@register.filter(name = 'multipy')
@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1