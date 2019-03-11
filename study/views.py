from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from .forms import ReviewForm
import os

# Create your views here.
l_word_number = 0  # initially passed to study
r_word_number = 0  #


def get_lword_num():
	global l_word_number
	os.chdir('/home/rohan/djpro/vocab-builder/study')
	num = open('data.txt', 'r')
	l_word_number = int(num.read())
	num.close()
	os.chdir('/home/rohan/djpro/vocab-builder')
	return l_word_number


def set_lword_number(number):
	os.chdir('/home/rohan/djpro/vocab-builder/study')
	num = open('data.txt', 'r+')
	num.truncate(0)
	num.write('{0}'.format(number))
	num.close()
	os.chdir('/home/rohan/djpro/vocab-builder')


def get_rword_num():
	return r_word_number


def tostudy(request):
	return redirect('study')


def study(request):
	# get all categories
	categories = List.objects.all()

	# get user
	username = request.user.username

	# get learning word number
	if get_lword_num() > 0:  # user goes to study page leaving learning page in between
		l_word_num = get_lword_num()-1
	else:
		l_word_num = get_lword_num()
	print(l_word_num)
	context = {
		'categories': categories, 'username': username, 'l_word_num': l_word_num,
	}
	return render(request, 'study/study.html', context)


def learn(request, l_word_num):

	if request.method == 'POST':

		set_lword_number(l_word_num)
		print(l_word_num)
		# get selected category
		category = request.POST.get('category')
		# print(category)

		# get unlearned words
		learn_words = Progress.objects.get_unwords(request.user.username, category)
		# print(learn_words)

		if l_word_num == learn_words.count():
			set_lword_number(0)
			for word in learn_words:
				Progress.objects.create(user=request.user, word_id=word, learned=False, correct=0, wrong=0)
			# return redirect('review', get_rword_num())
		context = {
			'learn_words': learn_words, 'category': category, 'l_word_num': l_word_num,
		}
		return render(request, 'study/learn.html', context)
	else:
		return redirect('study')


def review(request, r_word_num):
	if request.method == 'POST':
		global r_word_number
		# print(request.POST)
		# print(r_word_num)
		# get selected category
		category = request.POST.get('category')
		print(category)

		review_words = Progress.objects.get_review_words(request.user.username, category).order_by('correct')
		if r_word_num > review_words.count():
			r_word_number = 0
			return redirect('review')
		else:
			form = ReviewForm
			context = {
				'review_words': review_words, 'category': category, 'r_word_num': r_word_num, 'from': form,
			}
			return render(request, 'study/review.html', context)
	else:
		return redirect('study')

