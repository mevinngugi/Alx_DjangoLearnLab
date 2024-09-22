from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/profile_pictures', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)


    def __str__(self):
        return self.username


# Generate a token each time a new user is created
@receiver(post_save, sender=CustomUser)
def create_custom_user(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)