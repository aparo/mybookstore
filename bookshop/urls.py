from django.conf.urls import patterns, url

urlpatterns = patterns('bookshop.views',
    url(r'^$', "index", name='index'),
    url(r'^(?P<book_id>\d+)$', "detail", name='detail')
)

