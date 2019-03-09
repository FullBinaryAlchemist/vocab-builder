from django.template.defaultfilters import register
from study.models import *


@register.simple_tag(name='get_value')
def get_value(cat):
    return  WordList.objects.filter(word_id__contains=cat).count()
