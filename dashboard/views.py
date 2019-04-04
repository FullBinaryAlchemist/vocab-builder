from django.shortcuts import render, redirect
from study.models import *
from dashboard.models import *
from testmode.views import info
from testmode.urls import *


# Create your views here.
def dashboard_view(request):
    lists = List.objects.all()
    tests = Tests.objects.filter(test_data__user=request.user).order_by("-test_date")[:5]
    context = {'user': request.user, 'lists': lists, 'tests': tests}
    return render(request, 'dashboard/page.html', context)


def info_redirect(request, test_id):
    return redirect('info', test_id=test_id)
