from django import template
register = template.Library()

def add(n1, n2):
    return n1 + n2

register.filter('add',add)