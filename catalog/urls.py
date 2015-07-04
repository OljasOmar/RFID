__author__ = 'oljekenzo'

from django.conf.urls import url
from .import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^public/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    #url(r'^$', views.upload_pic)

]
