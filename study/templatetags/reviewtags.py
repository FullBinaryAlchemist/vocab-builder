from django.template.defaultfilters import register
from study.models import *


@register.simple_tag(name='get_re_word')
def get_re_word(words):  # words = inProgress words
    return words[0].word_id.word


@register.simple_tag(name='get_re_def')
def get_re_def(words):  # words = inProgress words
    return words[0].word_id.definition
