from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def tostudy(request):
	return redirect('study')


def study(request):
	# get all categories
	categories = List.objects.all()

	# get learned words
	words_learned = 0

	# get no. of ques remained for reviewing
	tot_review_que = 0

	context = {
		'categories': categories, 'words_learned': words_learned, 'tot_review_que': tot_review_que,
	}
	return render(request, 'study/study.html', context)


def learn(request):

	if request.method == 'POST':
		# get selected category
		selected_cat = request.POST['category']

		# get words to learn
		words = 'a'

		context = {
			'words': words, 'selected_cat': selected_cat,
		}
		return render(request, 'study/learn.html', context)
	else:
		return redirect('study')


def review(request):
	# learn_words =
	context = {
		'learn_words': 'a'
	}
	return render(request, 'study/learn.html', context)

