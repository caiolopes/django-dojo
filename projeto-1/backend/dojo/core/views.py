from django.shortcuts import render
from django.http import HttpResponse
from core.models import Joke
import requests
import time


def home(request):
    context = {
        'jokes': Joke.objects.all()
    }
    return render(request, 'batata/home.html', context)


def get_and_save_joke():
    resp = requests.get('http://api.icndb.com/jokes/random')

    if resp.status_code == 200:
        joke_text = resp.json().get('value').get('joke')
        joke = Joke.objects.create(text=joke_text)
        print(joke, joke.pk)

    return joke_text



# Controller == View do Django
def joke(request):
    return HttpResponse(get_and_save_joke())

