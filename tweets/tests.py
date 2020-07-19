from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Tweet

User = get_user_model()

# Create your tests here.
class TweetTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tiger', password='tiger123')
        Tweet.objects.create(content="My 1st Tweet", user=self.user)
        Tweet.objects.create(content="My 2nd Tweet", user=self.user)
        Tweet.objects.create(content="My 3rd Tweet", user=self.user)

    def test_tweet_created(self):
        tweet = Tweet.objects.create(content="My 4nd Tweet", user=self.user)
        self.assertEqual(tweet.id, 4)
        self.assertEqual(tweet.user, self.user)
    
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='tiger123')  
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/tweets/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/tweets/action", {"id":1, "action":"like" })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes"), 1)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/tweets/action", {"id":2, "action":"like" })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes"), 1)
        response = client.post("/tweets/action", {"id":2, "action":"unlike" })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes"), 0)      

