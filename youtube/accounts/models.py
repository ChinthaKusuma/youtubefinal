from django.db import models
from django.db.models import Model
from django.db.models.signals import post_save
from videos.models import Video
from django.contrib.auth.models import User

class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    saved_videos = models.ManyToManyField(Video, null=True, blank=True, related_name="saved_videos")

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    # user.profile.save() >> destiny.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)