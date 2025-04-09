from django.test import TestCase
from .models import Dog
from django.contrib.auth.models import User
from django.urls import reverse


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

    def test_index_view_counts(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['num_dogs'], 1)
        self.assertEqual(response.context['num_users'], 1)

    def test_dog_list_view(self):
        response = self.client.get(reverse('dogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dog.dog_name)

    def test_dog_detail_view(self):
        response = self.client.get(reverse('dog_detail', kwargs={'pk': self.dog.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dog.dog_name)

    def test_user_list_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_user_detail_view(self):
        response = self.client.get(reverse('user_detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
