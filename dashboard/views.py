from django.shortcuts import render, redirect
from study.models import *
from dashboard.models import *
from testmode.views import info
from testmode.urls import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = '/login/')
def dashboard_view(request):
    """lists = List.objects.all()
    tests = Tests.objects.filter(test_data__user=request.user).order_by("-test_date")[:5]
    context = {'user': request.user, 'lists': lists, 'tests': tests}
    return render(request, 'dashboard/page.html', context)"""
    categories = List.objects.all()
    # get user
    username = request.user.username
    # get learning word number
    if CurrentWord.objects.all().count() < categories.count():
        for category in categories:
            print(category)
            CurrentWord.objects.create(user=request.user, category=category)
    l_word_nums = CurrentWord.objects.filter(user=request.user)

    print(l_word_nums)

    context = {
        'categories': categories, 'username': username, 'l_word_nums': l_word_nums,
    }
    return render(request, 'dashboard/page.html', context)


def info_redirect(request, test_id):
    return redirect('info', test_id=test_id)
