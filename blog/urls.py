from django.conf.urls import include, url, patterns
from django.contrib import admin
from . import views, feed

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'jblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
