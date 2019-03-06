from django.shortcuts import render
from .models import *
# Create your views here.

def learn(request):

	#learn_words = 
	context={
		'learn_words':'a' 
	}
	return render(request, 'study/base.html', context)
