from django.shortcuts import render
from django.http import HttpResponse
from core.models import Joke
import requests


def home(request):
    context = {
        'jokes': Joke.objects.all()
    }
    return render(request, 'batata/home.html', context)


# Controller == View do Django
def joke(request):
    resp = requests.get('http://api.icndb.com/jokes/random')

    if resp.status_code == 200:
        joke_text = resp.json().get('value').get('joke')
        joke = Joke.objects.create(text=joke_text)
        print(joke, joke.pk)

    return HttpResponse(joke_text)
