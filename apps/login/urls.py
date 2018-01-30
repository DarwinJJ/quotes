from django.conf.urls import url
from views import *
# from django.contrib import admin

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^register$', register, name = 'registration'),
    url(r'^success$', success, name = 'success'),
    url(r'^login$', login, name = 'login'),
    url(r'^logout$', logout, name = 'logout')
    # url(r'^admin/', admin.site.urls),
]