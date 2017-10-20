from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^login', auth_views.login,{'template_name': 'login.html'}, name='login'),
     url(r'^create', views.create, name='create'),

]