from django.conf.urls import patterns, url

from vigilum import views

urlpatterns = patterns('',
    url(r'^login', views.login, name='login'),
    url(r'^index',views.index,name='index'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^police_api',views.police_api,name='police_api'),
)
