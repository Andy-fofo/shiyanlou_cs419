from django.conf.urls import pattens,include,url
from django.contrib import admin
from accounts import views

admin.autodiscover()

urlpattens=pattens('',
    url(r'^$',views.loin,name='login'),
    url(r'^login',views.logn,name='login'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^register',views.reister,name='register')
)
