from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  instance.profile.save()


#the post_save signal is fired when an object is saved. In this case, we would like to use the post_save signal when a user is created. The user model acts as the sender.

#the receiver takes in two args. the signal and the sender.

# @receiver(post_save, sender=User)# means when user is saved send this signal.the receiver is this create profile function
# def create_profile(sender, instance, created, **kwargs):
#   if created:
#     Profile.objects.create(user=instance)
  

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#   instance.profile.save()














