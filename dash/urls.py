from django.conf.urls import url

from . import views


app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$',views.login_check, name='login_check'),
    url(r'^register/$', views.register, name='register'),

    url(r'^todo/$',views.todo, name='todo'),

    url(r'^hadoop_status/',views.hadoop_status, name='hadoop_status'),
    url(r'^node_status/', views.hadoop_info, name='node_status'),

    url(r'^db_status/$',views.db_status, name='db_status'),
    url(r'^db_log/$',views.db_log, name='db_log'),
]