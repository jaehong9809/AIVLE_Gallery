from django.test import TestCase, Client
from GalleryUser.models import User
# Create your tests here.

class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create_user("test99", "test99@mail.com", "qwer")
        User.objects.create_superuser("admin2", "admin@mail.com", "qwer")

    def test_user(self):
        user = User.objects.get(pk = "test99")
        self.assertEqual(user.email, "test99@mail.com")

    def test_superuser(self):
        user = User.objects.get(pk = "admin2")
        self.assertEqual(user.is_superuser, True)