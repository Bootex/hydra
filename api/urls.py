from django.conf.urls import url

from . import views


app_name = 'api'

urlpatterns = [
    # ex: /dash/
    url(r'^$', views.index, name='index'),

    url(r'^hadoop_status/$',views.hadoop_status,name='hadoop_status'),
    url(r'^node_status/$', views.hadoop_node_status, name='node_status'),

    url(r'^db_status/$', views.db_status, name='db_status'),
    url(r'^db_log/$', views.db_log, name='db_log'),
]
