from django import template

from study.models import *

register= template.Library()

@register.simple_tag
def total_words(list):
	return WordList.objects.filter(word_id__contains=list).count()
	
@register.inclusion_tag("dashboard/progress.html")
def show_progress(user,list):
	learned_words_c= Progress.objects.get_lwords(user, list).count()
	total_words_c=total_words(list)
	review_words_c= Progress.objects.get_review_words(user,list).count()
	return {'list':list,'lwc':learned_words_c,'twc':total_words_c,'rwc': review_words_c} 

