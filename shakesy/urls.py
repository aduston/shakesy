from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^experiment_1$', 'experiment_1.views.index'),
    url(r'js_tests/$', direct_to_template, {'template': 'SpecRunner.html'})
)
