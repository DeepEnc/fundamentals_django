from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class AppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ('ag', 'agriculture'),
        ('so', 'social'),
        ('ec', 'eco'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
    price = models.IntegerField(default=30)
    description = models.TextField(default='')

def __str__(self):
    return self.name

class AppReview(models.Model):
    app = models.ForeignKey(AppVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'


class AppStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    app_varieties = models.ManyToManyField(AppVariety, related_name='appstores')

def __str__(self):
    return self.name

class AppCertificate(models.Model):
    app = models.OneToOneField(AppVariety, on_delete=models.CASCADE, related_name='certificates')
    certificates_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

def __str__(self):
    return f'Certificate for {self.name.app}'
