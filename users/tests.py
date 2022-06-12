from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
    self.user1 = User.objects.create_user(username='testUser', email='test@gmail.com', password='ssap1234')
  
  def test_instance(self):
    self.assertTrue(isinstance(self.user1, User))
  
  def test_instance(self):
    self.assertTrue(isinstance(self.user1.profile, Profile))
