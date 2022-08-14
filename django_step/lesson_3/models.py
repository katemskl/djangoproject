import base64

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.TextField(max_length=30)
    descriptions = models.TextField(max_length=100)


class Car(models.Model):
    title = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    millage = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    base_64 = models.CharField(max_length=60000, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')


class PhoneNote(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    notes = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name} {self.surname}'


class User(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Products(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(decimal_places=3, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    components = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(max_length=30)
    descriptions = models.TextField(max_length=300)

    def __str__(self):
        return self.title
