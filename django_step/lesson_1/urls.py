from django.urls import path, include

from . import views

urlpatterns = [
    path('my_first_url/', views.my_first_url),
    path('first_render/', views.first_render),
    path('words/', views.show_words),
    path('first_context/', views.first_context),
    path('first_param/<str:name>/', views.hello_name),
    path('star_wars_home/', views.star_wars_home, name='home'),
    path('star_wars_page/<str:name>/', views.star_wars_page, name='star_page')
]