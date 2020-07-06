from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:tweet_id>", views.tweet, name="tweet"),
    path("/add", views.add, name="add")
]