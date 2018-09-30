from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/', include(([
        url(r'^$', views.NewsList.as_view(), name='list'),
        url(r'^(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name='detail'),
        url(r'^(?P<pk>[0-9]+)/status/$', views.delete_status_news, name='delete_status'),
        url(r'^(?P<pk>[0-9]+)/data/$', views.delete_data_news, name='delete_data'),
    ], 'api'), namespace='api')),
]
