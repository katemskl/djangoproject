from django.urls import path, re_path

from . import views

urlpatterns = [
    path('my_first_url/', views.my_first_url),
    path('first_render/', views.first_render),
    path('words/', views.show_words),
    path('first_context/', views.first_context),
    path('first_param/<str:name>/', views.hello_name),
    path('star_wars_home/', views.star_wars_home, name='home'),
    path('star_wars_page/<str:name>/', views.star_wars_page, name='star_page'),
    re_path(r'^birthday/(?P<year>[12][90][023456789]\d)/$', views.check_birthday),
    re_path(r'^phone/(?P<number>\+380\d{9})/$', views.check_number)
]