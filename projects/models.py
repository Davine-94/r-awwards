import math
from django.db import models
from PIL import Image
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator

class Project(models.Model):
  publisher = models.ForeignKey(User, on_delete=models.CASCADE)
  tag = models.CharField(max_length=50, blank=True, null=True)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = CloudinaryField('image')
  # image = models.ImageField(upload_to='profile_pics')
  link = models.URLField(max_length=200)
  country = models.CharField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.title

  def save_project(self):
    return self.save()

  @classmethod
  def get_project(cls, pk):
    project = cls.objects.get(id=pk)
    return project

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})


class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
  content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
  usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
  average = models.DecimalField(decimal_places=1,max_digits=4)
  

  def __str__(self):
    return f'{self.user.username} Votes'
  

  def get_project_ratings(cls, pk):
    ratings = cls.objects.filter(project=pk)
    return ratings
  

  def user_average_rating(self):
    average = (self.design + self.content + self.usability)/3
    return average
  
  def criteria_average(self, pk):
    all_votes = Rating.objects.filter(project=pk)

    usability = []
    design = []
    content = []

    for i in all_votes:
      usability.append(i.usability)
      design.append(i.design)
      content.append(i.content) 

    if len(usability) > 0 or len(design)>0 or len(content)>0:
      average_usability = round(sum(usability)/len(usability),1) 
      average_design = round(sum(design)/len(design),1)
      average_content = round(sum(content)/len(content),1) 
    
    else:
      average_content=0.0
      average_design=0.0
      average_usability=0.0
      average_rating = 0.0

    return {
      'usability':average_usability,
      'design':average_design,
      'content':average_content,
    }
  
  


    



  




  

