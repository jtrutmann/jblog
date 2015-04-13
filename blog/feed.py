from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPosts(Feed):
    title = "J Blog"
    link = "/feed/"
    description = "Latest Post from J Blog"

    def items(self):
        return Entry.objects.published()[:5]