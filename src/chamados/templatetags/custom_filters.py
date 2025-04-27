from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def format_timedelta(td):
    if td is None:
        return "Não definido"

    days = td.days
    seconds = td.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    if days > 0:
        return f"{days} dias, {hours} horas, {minutes} minutos"
    elif hours > 0:
        return f"{hours} horas, {minutes} minutos"
    else:
        return f"{minutes} minutos"
