from django import template

from study.models import *
from dashboard.models import *
from django.db.models import Q
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

@register.inclusion_tag("dashboard/test.html")
def show_test_history(user,test):
	test_id= test.test_data.test_id
	total_words= TestsData.objects.filter(Q(test_id=test_id) & Q(user=user)).count()
	score= test.getscore()
	date=test.test_date.strftime("%Y-%m-%d %H:%M:%S")
	return {'test_id':test_id,'date':date,'twc':total_words,'sc': score} 

