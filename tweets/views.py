from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def tweet(request, tweet_id):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>Hello { tweet_id } - { obj.content }</h1>")
