from django import template

register = template.Library()

def format_datetime(dt):
    return dt.strftime('%A, %d %B %Y %H:%M:%S %z')

register.filter('dtformat', format_datetime)
