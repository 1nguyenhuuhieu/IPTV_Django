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
    path('stream/<int:stream_id>/', views.stream, name='stream'),
    path('confirm/<int:group_id>/', views.confirm, name='confirm'),
    path('ungroup/<int:group_id>/', views.ungroup, name='ungroup'),
]
