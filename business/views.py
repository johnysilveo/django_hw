from django.shortcuts import render

def business(request):
    return render(request, "business/business.html")

def honda(request):
    return render(request, "business/honda.html")

def toyota(request):
    return render(request, "business/toyota.html")

def lexus(request):
    return render(request, "business/lexus.html")
