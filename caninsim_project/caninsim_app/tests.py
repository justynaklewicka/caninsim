from django.test import TestCase
from .models import Dog
from django.contrib.auth.models import User
from django.urls import reverse

class SimpleTest(TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)

class DogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass")

    def test_str_returns_dog_name(self):
        dog = Dog.objects.create(dog_name="Shadowfang", owner=self.user)
        self.assertEqual(str(dog), "Shadowfang")

    def test_get_absolute_url(self):
        dog = Dog.objects.create(dog_name="Willow", owner=self.user)
        expected_url = reverse("dog_detail", kwargs={"pk": dog.pk})
        self.assertEqual(dog.get_absolute_url(), expected_url)
