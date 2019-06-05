from django import template

import random

from rocks.models import Mineral


register = template.Library()


@register.simple_tag
def random_mineral():
    mineral_count = Mineral.objects.all().count()
    return random.randint(1, mineral_count)
