from django.shortcuts import render

def index(request):
    context = {
        'title':"Python DTL"

    }
    return render(request, 'blog/index.html',context=context)
