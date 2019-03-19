from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import timedelta
from .models import *
import os
# Create your views here.


"""def get_word_num(index):
    #read integer from data.txt file-->get l_word_num or r_word_num

    os.chdir('/home/rohan/djpro/vocab-builder/study')
    with open('data.txt', 'r') as num:
        number = int(num.readline().split()[index])
    os.chdir('/home/rohan/djpro/vocab-builder')
    return number


def set_word_number(number, index):
    #number-->word number the user is currently learning or  reviewing

    os.chdir('/home/rohan/djpro/vocab-builder/study')
    with open('data.txt', 'r') as data:
        num = data.readline().split()
    num[index] = str(number)
    with open('data.txt', 'w') as data:
        data.write(' '.join(num))
    os.chdir('/home/rohan/djpro/vocab-builder')"""


def tostudy(request):
    return redirect('study')


def study(request):
    # get all categories
    categories = List.objects.all()
    # get user
    username = request.user.username
    # get learning word number
    if CurrentWord.objects.all().count() < categories.count():
        # print("hoo")
        for category in categories:
            print(category)
            CurrentWord.objects.create(user=request.user, category=category)
    l_word_nums = CurrentWord.objects.filter(user=request.user)
    # print(l_word_nums)

    # reviewing word number
    r_word_num = 0

    context = {
        'categories': categories, 'username': username, 'l_word_nums': l_word_nums, 'r_word_num': r_word_num,
    }
    return render(request, 'study/study.html', context)


def learn(request, l_word_num):
    if request.method == 'POST':

        # get selected category
        category = request.POST.get('category')
        print(category)

        # get unlearned words
        learn_words = WordList.objects.get_words(request.user.username, category)
        # print(learn_words)

        # set_word_number(l_word_num, 0)
        word_num = CurrentWord.objects.get(user=request.user, category=category)
        word_num.current_lword_no = l_word_num
        word_num.save()

        # reviewing word number
        r_word_num = 0

        user = request.user
        context = {
            'learn_words': learn_words, 'category': category, 'l_word_num': l_word_num, 'r_word_num': r_word_num, 'user': user,
        }
        return render(request, 'study/learn.html', context)
    else:
        return redirect('study')


def set_word_progress(review_words, is_correct):
    # print(is_correct)
    word = review_words[0].word_id.word
    progress_word = review_words.get(word_id__word=word)
    if is_correct:
        progress_word.correct += 1
        progress_word.save()
        if progress_word.correct == 3:
            progress_word.learned = True
        progress_word.interval = timezone.now() + timedelta(seconds=10)
        progress_word.save()
    else:
        progress_word.wrong += 1
        progress_word.interval = timezone.now()
        progress_word.save()


def review(request, r_word_num):

    if request.method == 'POST' and r_word_num == 1:
        category = request.POST.get('category')
        learn_words = WordList.objects.get_words(request.user.username, category)
        # move words learned in learning mode to Progress table
        l_word_num = CurrentWord.objects.get(user=request.user, category=category).current_lword_no
        if l_word_num == learn_words.count() and l_word_num != 0:  # l_word_num = get_word_num(0)
            for word in learn_words:
                Progress.objects.create(user=request.user, word_id=word, learned=False, correct=0, wrong=0, interval=timezone.now())
            # set_word_number(0, 0)
            word_num = CurrentWord.objects.get(user=request.user, category=category)
            word_num.current_lword_no = 0
            word_num.save()

    if request.method == 'POST' or r_word_num == 1:
        print(request.POST)

        # upgrade progress of the word
        if request.POST.get('user_word_data') is not None:
            user_word_data = request.POST.get('user_word_data')
            user_word, category = user_word_data.split(',')
            print(category, user_word)
            # if get_word_num(1):
            if CurrentWord.objects.get(user=request.user, category=category).current_rword_no:
                review_words = Progress.objects.get_review_words(request.user.username, category).filter(correct__lt=3).order_by('correct', 'wrong')
                print(review_words)
                word = review_words[0].word_id.word
                if user_word == word:
                    is_correct = True
                else:
                    is_correct = False
                set_word_progress(review_words, is_correct)
                if review_words.count() == 0:
                    # set_word_number(0, 1)
                    word_num = CurrentWord.objects.get(user=request.user, category=category)
                    word_num.current_rword_no = 0
                    word_num.save()
                    return redirect('study')

        # set_word_number(r_word_num, 1)
        word_num = CurrentWord.objects.get(user=request.user, category=category)
        word_num.current_rword_no = r_word_num
        word_num.save()

        # get review words
        review_words = Progress.objects.get_review_words(request.user.username, category).filter(correct__lt=3).order_by('correct', 'wrong')

        context = {
            'review_words': review_words, 'category': category, 'r_word_num': r_word_num,
        }
        return render(request, 'study/review.html', context)
    else:
        return redirect('study')

