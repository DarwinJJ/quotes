from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^home$', home, name = "home"),
    url(r'^add_to_list/(?P<id>\d+)$', add_to_list, name = "add_to_list"),
    url(r'^add_quote$', add_quote, name= "add_quote"),
    url(r'^remove/(?P<id>\d+)$', remove, name="remove"),
    url(r'^user/(?P<id>\d+)$', user, name = "user"),
]