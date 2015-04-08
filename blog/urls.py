from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'jblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.BlogIndex.as_view(), name="index"),
]
