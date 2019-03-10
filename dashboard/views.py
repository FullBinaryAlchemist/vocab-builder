from django.shortcuts import render
from study.models import *


# Create your views here.
def dashboard_view(request):
    lists = List.objects.all()
    tests = Test.objects.filter(test_data__user=request.user).order_by("-test_date")[:5]
    context = {'user': request.user, 'lists': lists, 'tests': tests}
    return render(request, 'dashboard/page.html', context)
