from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # prof_pic = models.ImageField(upload_to='profile_pictures', default='default.png')
  prof_pic = CloudinaryField('image')
  bio = models.TextField(max_length=250, blank=True)
  created_at = models.DateField(auto_now_add=True)
  update_at = models.DateField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} Profile'




