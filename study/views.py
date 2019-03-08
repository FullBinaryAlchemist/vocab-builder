from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def tostudy(request):
	return redirect('study')


def study(request):
	list_type = List.objects.all()
	context = {
		'list_type': list_type,
	}
	return render(request, 'study/study.html', context)


def learn(request):
    # learn_words =
    context = {
        'learn_words': 'a'
    }
    return render(request, 'study/base.html', context)
