from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tweets/<int:tweet_id>", views.tweet, name="tweet"),
]