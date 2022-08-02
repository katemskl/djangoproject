from django.urls import path

from . import views

urlpatterns = [
    path('current_time/', views.current_time, name='time'),
    path('multi_table/', views.multiplication, name='table'),
    path('date_of_day/', views.date_of_day, name='date')
]