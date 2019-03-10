from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def tostudy(request):
	return redirect('study')


def study(request):
	# get all categories
	categories = List.objects.all()

	# get learned words
	tot_words_learned = Progress.objects.get_lwords(request.user.username, categories).count()

	# get no. of ques remained for reviewing
	tot_review_que = Progress.objects.get_review_words(request.user.username, categories).count()

	context = {
		'categories': categories, 'tot_words_learned': tot_words_learned, 'tot_review_que': tot_review_que,
	}
	return render(request, 'study/study.html', context)


def learn(request):

	if request.method == 'POST':
		# get selected category
		selected_cat = request.POST['category']

		# get words to learn in terms of objects
		learn_words = 'a'#WordList.objects.get(word='abate')

		context = {
			'learn_words': learn_words, 'selected_cat': selected_cat,
		}
		return render(request, 'study/learn.html', context)
	else:
		return redirect('study')


def review(request):
	if request.method == 'POST':
		# get selected category
		selected_cat = request.POST['category']

		# get words to review
		review_words = 'a'

		context = {
			'words': review_words, 'selected_cat': selected_cat,
		}
		return render(request, 'study/learn.html', context)
	else:
		return redirect('study')

