from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_iptv, name='login'),
    path('logout/', views.logout_iptv, name='logout'),
    path('register/', views.register_iptv, name='register'),
    path('profile/', views.profile, name='profile'),
    path('group/', views.group, name='group'),
]
