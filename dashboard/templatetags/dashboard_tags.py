from django import template

from study.models import *

register= template.Library()

@register.inclusion_tag("")