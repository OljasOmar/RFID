__author__ = 'oljekenzo'

from django.conf.urls import url
from .import views



urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^book/(?P<rfidValue>\w+)$', views.book_info),
    url(r'^user/(?P<barcodeValue>\w+)$', views.user_info),

]
