import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect # HttpResponseRedirect

from .forms import TweetForm
from .models import Tweet

# Create your views here.
def home(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)

def index(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,100) } for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list
    }
    return JsonResponse(data)

def tweet(request, tweet_id, *args, **kwargs):
    """
    REST API Endpoint
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404
    return JsonResponse(data, status=status)

def add(request):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        if next_url is not None:
            return redirect(next_url)
        form = TweetForm()
    return render(request, "components/form.html", context={"form": form})