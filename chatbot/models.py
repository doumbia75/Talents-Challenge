from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Compte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jetons = models.CharField(max_length=128)
    image = models.ImageField(upload_to="image",blank=True, null=True)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    reponse = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(auto_now_add=True)
