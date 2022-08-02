from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('head/', views.head, name='head'),
    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts'),
    path('history/<str:page>/', views.history_extra, name='history+'),
    path('history/', views.history, name='history'),
]
