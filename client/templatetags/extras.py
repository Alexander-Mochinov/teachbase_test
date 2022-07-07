from django import template


register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Получение значения словаря в шаблонезаторе django"""
    
    return dictionary.get(
        key
    )
