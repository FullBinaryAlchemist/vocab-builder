from django.shortcuts import render
from study.models import *
from dashboard.models import *
from django.db.models import Q
# Create your views here.
#Generate tests for a given list where 
def generate_test(request,list):
	pass

def info(request, test_id):
	all_words= TestsData.objects.filter(Q(test_id=test_id) & Q(user=request.user)) #Getting all the words from TestsData
	test=Tests.objects.get(test_data__test_id=test_id, test_data__user=request.user) #Getting the corresponding Tests object
	date=test.test_date.strftime("%Y-%m-%d %H:%M:%S")
	context= {'all_words':all_words,'test':test,'date':date, 'test_id':test_id}
	return render(request,'testmode/info.html',context)