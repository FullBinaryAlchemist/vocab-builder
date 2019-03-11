from django.template.defaultfilters import register
from study.models import *
from study import views


@register.simple_tag(name='get_tot_words')
def get_tot_words(cat):
    return  WordList.objects.filter(word_id__contains=cat).count()


@register.simple_tag(name='get_tot_lwords')
def get_tot_lwords(username, cat):
    return Progress.objects.get_lwords(username, cat).count()


@register.simple_tag(name='get_tot_rewords')
def get_tot_rewords(username, cat):
    return Progress.objects.get_review_words(username, cat).count()


@register.filter(name='get_word')
def get_word(words, word_num):  # words = learn_words
    # print(words[word_num - 1].word)
    return words[word_num-1].word


@register.filter(name='get_def')
def get_def(words, word_num):  # words = learn_words
    return words[word_num-1].definition


@register.simple_tag(name='goto_url')
def goto_url(learn_words_count, l_word_num):
    if l_word_num < learn_words_count:
        return 'learn', l_word_num
    else:
        views.get_lword_num = 0
        return 'review', views.get_rword_num
