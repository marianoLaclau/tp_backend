from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Accede a los valores dentro de un diccionario."""
    return dictionary.get(key)