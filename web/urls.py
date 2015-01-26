'''
Created on 29/11/2014

@author: plopez
'''

from django.conf.urls import patterns, url

from web import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)