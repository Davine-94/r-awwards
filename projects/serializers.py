from rest_framework import serializers
from .models import Project, Rating

class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ['id', 'title', 'description','image', 'link', 'publisher']
  
class RatingSerializer(serializers.ModelSerializer):

  class Meta:
    model = Rating
    fields = ['id', 'user', 'project','design','content','usability']
