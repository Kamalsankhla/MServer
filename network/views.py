from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def home_view(request):
# 	return HttpResponse("<h1>home page is working fine</h1>")


def home_view(request):
	return render(request,"home.html", {}) 

def network(request):
	return render(request,"network.html", {})

def check_network(request):
	return HttpResponse("<h1>checking</h1>")
    # return render(request,"network.html", context)	

def service(request):
	return render(request,"service.html", {})

def logs(request):
	return render(request,"logs.html", {})

def load(request):
	return render(request,"load.html", {})