from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^experiment_1a$', 'experiment_1.views.index_a'),
    url(r'^experiment_1b$', 'experiment_1.views.index_b'),
    url(r'jstest/$', direct_to_template, {'template': 'specrunner.html'}),
    url(r'admin/', include(admin.site.urls))
)
