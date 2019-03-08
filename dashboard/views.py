from django.shortcuts import render
from study.models import * 
# Create your views here.
def dashboard_view(request):
	lists= List.objects.all()
	context= {'user':request.user,'lists':lists}
	return render(request,'dashboard/page.html',context)