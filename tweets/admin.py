from django.contrib import admin

from tweets.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'content', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    
    class Meta:
        model = Tweet

admin.site.register(Tweet,TweetAdmin)