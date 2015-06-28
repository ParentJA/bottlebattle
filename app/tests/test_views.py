__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.test import TestCase


class HomeViewTest(TestCase):
    def test_home_view_renders_home_template(self):
        response = self.client.get('/app/')
        self.assertTemplateUsed(response, 'app/home.html')