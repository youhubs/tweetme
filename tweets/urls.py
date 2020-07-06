from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("<int:tweet_id>", views.tweet, name="tweet"),
    path("<int:tweet_id>/delete", views.delete, name="delete")
]