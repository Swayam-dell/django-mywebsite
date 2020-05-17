from django import template

register = template.library()
@register.filter(name = 'cut')
def cut(value,arg):
    return value.replace(arg,'')


register.filter('cut',cut)
