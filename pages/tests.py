from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Blog
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.blog = Blog.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )
    
    def test_string_representation(self):
        blog = Blog(title='A sample title')
        self.assertAlmostEqual(str(blog),blog.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(),'/blog/1/')

    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'A good title')
        self.assertEqual(f'{self.blog.author}', 'testuser')
        self.assertEqual(f'{self.blog.body}','Nice body content')


    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_blog_detail_view(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_blog_create_view(self):
        response = self.client.post(reverse('blog_new'), {
            'title':'New title',
            'body' : 'New text',
            'author' : self.user.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Blog.objects.last().title, 'New title')
        self.assertEqual(Blog.objects.last().body,'New text')

    def test_blog_update_view(self):
        response = self.client.post(reverse('blog_edit',args='1'),{
            'title' : 'Updated title',
            'body' : 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_blog_delete_view(self):
        response = self.client.post(
            reverse('blog_delete',args='1'))
        self.assertEqual(response.status_code, 302)

