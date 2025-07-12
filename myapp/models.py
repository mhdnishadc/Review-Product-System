# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Product(models.Model):  # Capitalize class names (Python convention)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    password = models.CharField(max_length=128, default="123456admin")  # Use Django's built-in password hashing
    username = models.CharField(max_length=150, default="admin", unique=True)  # Ensure username is unique
    def __str__(self):
        return self.username