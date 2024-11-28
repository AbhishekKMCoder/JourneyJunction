from django.db import models

# Create your models here.



class LoginDb(models.Model):
    full_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Recommended to use hashed passwords
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.BooleanField(default=False)  # Add this field for admin/user differentiation

    def __str__(self):
        return self.username
class UserProfile(models.Model):
    name = models.CharField(max_length=100)  # Name field
    location = models.CharField(max_length=200)  # Location field
    email = models.EmailField()  # Email field with validation and uniqueness

    def __str__(self):
        return self.name
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"