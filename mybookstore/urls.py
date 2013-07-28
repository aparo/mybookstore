from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url="shop/")),
    url(r'^shop/', include('bookshop.urls', namespace="shop")),
    url(r'^admin/', include(admin.site.urls)),
)

