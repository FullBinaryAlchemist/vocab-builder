from django.template.defaultfilters import register
from study.models import *


@register.filter(name='get_unl_word')
def get_unl_word(words, word_num):  # words = learn_words
    return words[word_num-1].word


@register.filter(name='get_unl_def')
def get_unl_def(words, word_num):  # words = learn_words
    return words[word_num-1].definition
