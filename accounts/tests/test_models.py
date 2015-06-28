__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.timezone import now

User = get_user_model()


class UserModelTest(TestCase):
    def test_user_unicode_representation(self):
        user = User.objects.create_user(
            first_name='Jason',
            last_name='Parent',
            username='parentj@eab.com',
            email='parentj@eab.com',
            password='password',
            last_login=now()
        )

        self.assertEqual(unicode(user), user.get_full_name())
        self.assertEqual(unicode(user), 'Jason Parent')