from django.utils import unittest
from django.test.client import Client
from spotseeker_server.models import Spot, SpotAvailableHours
import simplejson as json

class SpotHoursPOSTTest(unittest.TestCase):

    def test_hours(self):

        post_obj = {
            'name': "This spot has available hours",
            'capacity': "4",
            'available_hours': {
                'monday': [ [ "00:00", "10:00" ], [ "11:00", "14:00" ] ],
                'tuesday': [ [ "11:00", "14:00" ] ],
                'wednesday': [ [ "11:00", "14:00" ] ],
                'thursday': [ [ "11:00", "14:00" ] ],
                'friday': [ [ "11:00", "14:00" ] ],
                'saturday': [ ],
                'sunday': [ [ "11:00", "14:00" ] ],
            }
        }


        c = Client()
        response = c.post("/api/v1/spot/", json.dumps(post_obj) , content_type="application/json")

        get_response = c.get(response["Location"])

        self.assertEquals(get_response.status_code, 200, "OK in response to GETing the new spot")

        spot_dict = json.loads(get_response.content)

        self.maxDiff = None
        self.assertEquals(spot_dict["available_hours"], post_obj["available_hours"], "Data from the web service matches the data for the spot")
        self.assertEquals(spot_dict["name"], post_obj["name"], "Data from the web service matches the data for the spot")
        self.assertEquals(spot_dict["capacity"], post_obj["capacity"], "Data from the web service matches the data for the spot")



