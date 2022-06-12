from django.test import TestCase
from .models import Project,Rating
from django.contrib.auth.models import User

class ProjectTestClass(TestCase):

  def setUp(self):
    self.user1 = User.objects.create_user(username='testUser', email='test@gmail.com', password='ssap1234')

    self.project1 = Project(title='test title', description='test instance for test class', image='photo.jpg', link='www.test.com', country='kenya', tag='navigation', publisher=self.user1)
    self.project1.save()
  

  def test_get_project(self):
    project = Project.get_project(self.project1.id)
    self.assertEqual(self.project1.title,"test title")

class RatingTestClass(TestCase):

  def setUp(self):
    self.user2 = User.objects.create_user(username='testRateUser', email='test@gmail.com', password='ssap1234')

    self.project1 = Project(title='test Rate title', description='test instance for rating class', image='photo.jpg', link='www.test.com', country='kenya', tag='navigation', publisher=self.user2)
    self.project2.save()

    self.rating1 = Rating(design = 4, usability = 8, content = 3, user=self.user2, project = self.project2)
    self.rating1.save()

    self.rating1.average = self.rating1.user_average_rating()
    self.ratin1.save()

    def test_average_ratings(self):
      self.assertEqual(self.rating1.average,5)

    def test_get_project_ratings(self):
      project = self.project2
      ratings = project.get_project_ratings()
      
      self.assertTrue(len(ratings)==1)


  







