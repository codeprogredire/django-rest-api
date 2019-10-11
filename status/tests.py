from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Status

# Create your tests here.
User = get_user_model()

class StatusTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='ground',email='fire@gmail.com')
        user.set_password('yahoo')
        user.save()

    def test_creating_status(self):
        user = User.objects.get(username='ground')
        obj = Status.objects.create(user=user,content='some cool content')
        self.assertEqual(obj.id,1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(),1)