from django import template

register = template.Library()

f_list = []


@register.simple_tag
def abs_featured(item):
    f_list.append(item)
    return f_list


@register.simple_tag
def clear_featured():
    f_list.clear()
    return f_list
