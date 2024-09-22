from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
# from django.db.models.signals import post_save
# from rest_framework.authtoken.models import Token

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/profile_pictures', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_users', blank=True)


    def __str__(self):
        return self.username


# In my initial implementation, I had set django signals to listen to CustomUser
# whenever it saves to create a token for the new user. Moving this to serializer

# # Generate a token each time a new user is created
# @receiver(post_save, sender=CustomUser)
# def create_custom_user(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)