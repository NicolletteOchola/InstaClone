from django.db import models
from django.test import TestCase
from .models import Profile, Image, Comment
from django.contrib.auth.models import User

# Create your tests here.

class ImageTestCase(TestCase):
  def setUp(self):
    self.image= Image(image_name = 'Beagle', description ='Lovely dog', image_file ='images/beagle.jpg', location = self.new_location)
    self.image.save_image()

 def test_save_images(self):
    self.image.save_image()
    all_images = Image.objects.all()
    self.assertTrue(len(all_images) > 0)