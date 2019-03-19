from django.template.defaultfilters import register
from study.models import *


@register.simple_tag(name='get_tot_words')
def get_tot_words(cat):
    return  WordList.objects.filter(word_id__contains=cat).count()


@register.simple_tag(name='get_tot_lwords')
def get_tot_lwords(username, cat):
    return Progress.objects.get_lwords(username, cat).count()


@register.simple_tag(name='get_tot_rewords')
def get_tot_rewords(username, cat):
    return Progress.objects.get_review_words(username, cat).filter(correct__lt=3).count()


@register.filter(name='get_lword_num')
def get_lword_num(l_word_nums, category):
    print(category)
    l_word_num = l_word_nums.get(category=category).current_lword_no
    if l_word_num:
        return l_word_num
    else:
        # l_word_num -= 1
        l_word_num += 1
        return l_word_num
