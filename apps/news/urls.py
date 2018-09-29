from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/', include(([
        url(r'^$', views.NewsList.as_view(), name='list'),
        # url(r'^edit/(?P<pk>[0-9]+)/$', NewsDetail.as_view(), name='edit'),
        # path('create/', views.edit, name='create'),
        url(r'^(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name='detail'),
        url(r'^(?P<pk>[0-9]+)/status/$', views.delete_status_news, name='delete_status'),
        url(r'^(?P<pk>[0-9]+)/data/$', views.delete_data_news, name='delete_data'),
        # path('(?P<pk>[0-9]+)/status/', NewsDetail.as_view(), name='delete_status'),
    ], 'api'), namespace='api')),
]
