from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import timedelta
from .models import *
import os
from django.contrib.auth.decorators import login_required
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


def landing(request):
    return render(request, 'study/landing.html', {})


def tostudy(request):
    return redirect('study')


def save_num(user, category, wordnum, mode):
    word_num = CurrentWord.objects.get(user=user, category=category)
    if mode == 'learn':
        word_num.current_lword_no = wordnum
        word_num.save()
    elif mode == 'review':
        word_num.current_rword_no = wordnum
        word_num.save()

@login_required(login_url = '/login/')
def study(request):
    print("Inside study")
    # get all categories
    categories = List.objects.all()
    # get user
    username = request.user.username
    # get learning word number
    if CurrentWord.objects.filter(user=request.user).all().count() < categories.count():
        for category in categories:
            print(category)
            CurrentWord.objects.create(user=request.user, category=category)
    l_word_nums = CurrentWord.objects.filter(user=request.user)

    print(l_word_nums)

    # initializing review word num and learn word num to 0
    for category in categories:
        save_num(request.user, category, 0, 'learn')
        save_num(request.user, category, 0, 'review')
    r_word_num = 0

    context = {
        'categories': categories, 'username': username, 'l_word_nums': l_word_nums, 'r_word_num': r_word_num,
    }
    return render(request, 'study/study.html', context)

@login_required(login_url = '/login/')
def go_learn(request):
    categories = List.objects.all()
    username = request.user.username
    if CurrentWord.objects.filter(user=request.user).all().count() < categories.count():
        for category in categories:
            print(category)
            CurrentWord.objects.create(user=request.user, category=category)
    l_word_nums = CurrentWord.objects.filter(user=request.user)
    for category in categories:
        save_num(request.user, category, 0, 'learn')
    context = {
        'categories': categories, 'username': username, 'l_word_nums': l_word_nums,
    }
    return render(request, 'study/go_learn.html', context)

@login_required(login_url = '/login/')
def go_review(request):
    categories = List.objects.all()
    username = request.user.username

    # initializing review word num and learn word num to 0
    for category in categories:
        save_num(request.user, category, 0, 'review')
    r_word_num = 0

    context = {
        'categories': categories, 'username': username, 'r_word_num': r_word_num,
    }
    return render(request, 'study/go_review.html', context)

@login_required(login_url = '/login/')
def learn(request, l_word_num):

    print("Inside learn")
    if request.method == 'POST':
        # print("post:", request.POST)
        # print("get:", request.GET)
        # get selected category
        category = request.POST.get('category')

        # get unlearned words
        learn_words = WordList.objects.get_words(request.user.username, category)
        # print(learn_words)

        # set_word_number(l_word_num, 0)
        word_num = CurrentWord.objects.get(user=request.user, category=category)

        if l_word_num <= word_num.current_lword_no:
            l_word_num = 0
            save_num(request.user, category, l_word_num, 'learn')
            return redirect('study')
        save_num(request.user, category, l_word_num, 'learn')

        # reviewing word number
        save_num(request.user, category, 0, 'review')
        r_word_num = 0

        user = request.user
        context = {
            'learn_words': learn_words, 'category': category, 'l_word_num': l_word_num, 'r_word_num': r_word_num, 'user': user,

            'word_num':  word_num,
        }
        return render(request, 'study/learn.html', context)
    elif request.method == "GET":

        # set_word_number(l_word_num, 0)
        print(request.GET)
        category = request.GET.get('category')

        # get unlearned words
        learn_words = WordList.objects.get_words(request.user.username, category)
        # print(learn_words)

        word_num = CurrentWord.objects.get(user=request.user, category=category)
        save_num(request.user, category, l_word_num, 'learn')

        r_word_num = 0

        user = request.user
        context = {
            'learn_words': learn_words, 'category': category, 'l_word_num': l_word_num, 'r_word_num': r_word_num,
            'user': user, 'word_num': word_num,
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
        progress_word.interval = timezone.now() + timedelta(hours=1)
        progress_word.save()
    else:
        progress_word.wrong += 1
        progress_word.interval = timezone.now()
        progress_word.save()


def check_ans(user, category, user_word):
    if CurrentWord.objects.get(user=user, category=category).current_rword_no:
        review_words = Progress.objects.get_review_words(user.username, category).filter(correct__lt=3).order_by('correct', 'wrong')
        print(review_words)
        word = review_words[0].word_id.word
        if user_word.lower() == word.lower():
            is_correct = True
        else:
            is_correct = False
        set_word_progress(review_words, is_correct)
        if review_words.count() == 0:
            # set_word_number(0, 1)
            word_num = CurrentWord.objects.get(user=user, category=category)
            word_num.current_rword_no = 0
            word_num.save()

@login_required(login_url = '/login/')
def review(request, r_word_num):
    if request.method == 'POST':

        if request.POST.get('category') is not None:
            category = request.POST.get('category')
        else:
            user_word_data = request.POST.get('user_word_data')
            category = user_word_data.split(',')[1]

        word_num = CurrentWord.objects.get(user=request.user, category=category)
        if word_num.current_rword_no >= r_word_num and word_num.current_rword_no != 0:
            # if user refreshes
            print("hi")
            print("1",request.POST,request.GET)
            if request.POST.get('user_word_data') is not None:
                user_word_data = request.POST.get('user_word_data')
                user_word = user_word_data.split(',')[0]
                check_ans(request.user, category, user_word)
            return redirect('study')
        else:
            if r_word_num == 1:
                category = request.POST.get('category')
                learn_words = WordList.objects.get_words(request.user.username, category)
                # move words learned in learning mode to Progress table
                if word_num.current_lword_no == learn_words.count() and word_num.current_lword_no != 0:  # l_word_num = get_word_num(0)
                    for word in learn_words:
                        Progress.objects.create(user=request.user, word_id=word, learned=False, correct=0, wrong=0, interval=timezone.now())
                    # set_word_number(0, 0)
                    word_num.current_lword_no = 0
                    word_num.save()

            # upgrade progress of the word
            print("2",request.POST)
            if request.POST.get('user_word_data') is not None:
                user_word_data = request.POST.get('user_word_data')
                user_word = user_word_data.split(',')[0]
                print(category, user_word)
                check_ans(request.user, category, user_word)
                review_words = Progress.objects.get_review_words(request.user.username, category).filter(correct__lt=3).order_by('correct', 'wrong')
                if review_words.count() == 0:
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

