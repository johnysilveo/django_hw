import random

from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
from django.views import View



def index(request):
    now = datetime.datetime.now()
    context = {'title': 'Python DTL', 'now': now}
    # 'myList' = [one,two,tree]
    return render(request, 'helloweb/index.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1> Current date time {now}")


class CurrentDateTimeView(View):
    def get(self,request):
        now = datetime.datetime.now()
        return HttpResponse(f"<h1> Current date time (Class) {now}")


def random_sayings(request):
    sayings = [
        "We are what we repeatedly do. Excellence, then, is not an act, but a habit. — Aristotle",
        "Imagination is more important than knowledge. — Albert Einstein",
        "Be the change that you wish to see in the world. — Mahatma Gandhi",
        "It always seems impossible until it is done. — Nelson Mandela",
        "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
        "It does not matter how slowly you go as long as you do not stop. — Confucius",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
        "Nothing in life is to be feared, it is only to be understood. — Marie Curie",
        "The unexamined life is not worth living. — Socrates",
        "I have a dream. — Martin Luther King Jr."
    ]

    chosen = random.choice(sayings)
    return HttpResponse(chosen)
def song_string(request):
    lyrics = 'whaaaaaat'

    return render(request, 'helloweb/song_string.html', {f'song':{lyrics}})



def home(request):
    return render(request, "helloweb/home.html")

def news(request):
    return render(request, "helloweb/news.html")

def management(request):
    return render(request, "helloweb/management.html")

def facts(request):
    return render(request, "helloweb/facts.html")

def contacts(request):
    return render(request, "helloweb/contacts.html")

def history_index(request):
    return render(request, "helloweb/history.html")

def history_people(request):
    return render(request, "helloweb/history_people.html")

def history_photos(request):
    return render(request, "helloweb/history_photos.html")

