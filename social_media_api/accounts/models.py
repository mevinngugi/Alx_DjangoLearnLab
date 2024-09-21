from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/profile_pictures', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)


    def __str__(self):
        return self.username
        