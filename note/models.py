from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


# Create your models here.
class Note(models.Model):
    # always reference the User class using setting conf
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    value = models.IntegerField(max_length=255)
    def __str__(self):
        return "your note is %s" % self.value

# class used to add more
# informations to the user
# without modifying the User class
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True)
    # fields we want to add to user
    is_devops = True
    url = models.URLField()
# method used to create a profile
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# signal that will
# trigger user profile creation once a user is created
post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
