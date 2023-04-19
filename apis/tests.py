from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase

from pages.models import Blog
# Create your tests here.


class APITests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.blog = Blog.objects.create(
            title = 'Django Blog API',
            author = self.user,
            body = 'this is first blog',
        )
    
    def test_api_listview(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertContains(response, self.blog)

    