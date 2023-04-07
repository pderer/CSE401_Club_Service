from django.urls import path
from . import views


urlpatterns = [
    # root path
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('home/', views.home, name='home'),
    path('home/notice/<int:id>/', views.notice, name='notice'),
    path('home/manual/<int:id>/', views.manual, name='manual'),

    path('home/club/<int:club_id>/', views.club_main, name='club_main'),
    path('home/club/<int:club_id>/blog/<int:blog_id>/', views.blog, name='blog'),
    path('home/club/<int:club_id>/blog/create/', views.blog_create, name='blog_create'),
    path('home/club/<int:club_id>/blog/modify/<int:blog_id>/', views.blog_modify, name='blog_modify'),
    path('home/club/<int:club_id>/blog/delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('home/club/<int:club_id>/calendar/create/', views.calendar_create, name='calendar_create'),
    path('home/club/<int:club_id>/calendar/modify/<int:calendar_id>/', views.calendar_modify, name='calendar_modify'),
    path('home/club/<int:club_id>/calendar/delete/<int:calendar_id>/', views.calendar_delete, name='calendar_delete'),
    path('home/club/<int:club_id>/list/create/', views.list_create, name='list_create'),
    path('home/club/<int:club_id>/list/modify/<int:list_id>/', views.list_modify, name='list_modify'),
    path('home/club/<int:club_id>/list/delete/<int:list_id>/', views.list_delete, name='list_delete'),
]