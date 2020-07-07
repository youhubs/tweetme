from random import randint
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE) # "Tweet"
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL) # self!!
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many users can have many tweets
    likes = models.ManyToManyField(User, related_name="liking_users", blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": randint(0, 100),
        }