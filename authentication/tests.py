from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.serializers import SongSerializer
from authentication.models import Song

# Create your tests here.

class SongViewTest(APITestCase):

    def setUp(self):
        create=Song(name="Rishabh",duration = 250 )
        create.save()

    def test_song(self):
        value = {
        "name" : "Ajay",
        "duration": 40,
        }
        response = self.client.post("/api/song/", data=value)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)






