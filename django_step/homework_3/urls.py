from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.main_page, name='main'),
    path('main/<str:page>/', views.main_extra, name='main+'),
    path('main/writers/<str:writer>/', views.writers_extra, name='writer'),
    path('main/writers/<str:writer>/<str:book>/', views.writer_book, name='writer_book'),
    path('main/books/<str:place>/', views.books_extra, name='books')
]
