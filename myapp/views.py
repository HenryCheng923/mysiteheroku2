from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index', {})
def pylinkweb(request):
	return HttpResponse("Django讓python能方便連結網頁")
def deposits(request):
	return render(request,'E_10_1',{})
def result(request):
	pv=int(request.GET['amount'])
	i=float(request.GET['rate'])
	n=int(request.GET['period'])
	fv=str((pv*((1+i)**n)))
	return HttpResponse(fv)


    