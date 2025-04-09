from django.test import TestCase
from .models import Dog
from django.contrib.auth.models import User
from django.urls import reverse

class SimpleTest(TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)

class DogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="tester", password="pass")
        cls.dog = Dog.objects.create(dog_name="Willow", owner=cls.user)

    def test_str_returns_dog_name(self):
        self.assertEqual(str(self.dog), "Willow")

    def test_get_absolute_url(self):
        expected_url = reverse("dog_detail", kwargs={"pk": self.dog.pk})
        self.assertEqual(self.dog.get_absolute_url(), expected_url)
