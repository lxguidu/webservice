# encoding: utf-8

from django.conf.urls import patterns, url
from .views import service

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eshop.views.home', name='home'),
    
    (r'^$', service),
    url(r'^wsdl$', service),
)