from django import template

from rocks.models import Minerals


register = template.Library()


@register.simple_tag
def get_verbose_name(object, field_name):
    """Returns the verbose name from the model"""
    return object._meta.get_field(field_name).verbose_name
