from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/', include(([
        url(r'^$', views.TopicsList.as_view(), name='list'),
        url(r'^(?P<pk>[0-9]+)/$', views.TopicsDetail.as_view(), name='detail'),
    ], 'api'), namespace='api')),
]
