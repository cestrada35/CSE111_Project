"""
This is urls for app
"""
from django.urls import path

from . import views


urlpatterns = [
    path('games/', views.game_list, name='game_list'),
    path('devs/', views.developer_list, name='developer_list'),
    path('pubs/', views.publisher_list, name='publisher_list'),
    path('salestime/', views.salestime_list, name='salestime_list'),
    path('nation/', views.nation_list, name='nation_list'),
    path('region/', views.region_list, name='region_list'),
    path('game/<int:pk>/', views.game_details, name='game_details'),
    path('developer/<int:pk>/', views.developer_details, name='developer_details'),
    path('publisher/<int:pk>/', views.publisher_details, name='developer_details'),
    path('salestime/<int:pk>/', views.salestime_details, name='salestime_details'),
    path('nations/<int:pk>/', views.nation_details, name='nation_details'),
    path('regions/<int:pk>/', views.region_details, name='region_details'),
    path('search/', views.searching, name='search'),
]
