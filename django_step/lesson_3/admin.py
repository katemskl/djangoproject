from django.contrib import admin
from .models import Car, PhoneNote, Category, Comment, User, Products

# Register your models here.

admin.site.register(Car)
admin.site.register(PhoneNote)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Products)
