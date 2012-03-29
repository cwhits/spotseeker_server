from django.utils import unittest
from django.test.client import Client
from spotseeker_server.models import Spot

class SpotGETTest(unittest.TestCase):
    def setUp(self):
        spot = Spot.objects.create( name = "This is for testing GET" )
        spot.save()
        self.spot = spot

    def test_invalid_id(self):
        c = Client()
        response = c.get("/api/v1/spot/bad_id")
        self.assertEquals(response.status_code, 404, "Rejects a non-numeric id")

    def test_invalid_id_too_high(self):
        c = Client()
        url = "/api/v1/spot/%s" % (self.spot.pk + 10000)
        response = c.get(url)
        self.assertEquals(response.status_code, 404, "Spot ID too high")