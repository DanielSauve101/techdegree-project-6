from django import template

import random

from rocks.models import Mineral


register = template.Library()


@register.simple_tag
def random_mineral():
    mineral_count = Mineral.objects.all().count()
    return random.randint(1, mineral_count)


@register.filter('name_modifier')
def name_modifier(str):
    return str.replace('_', ' ')
