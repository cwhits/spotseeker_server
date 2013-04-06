""" Copyright 2012, 2013 UW Information Technology, University of Washington

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from spotseeker_server.views.rest_dispatch import RESTDispatch, RESTException
from spotseeker_server.models import SpotImage, Spot
from django.http import HttpResponse
from spotseeker_server.require_auth import *
from PIL import Image


class AddImageView(RESTDispatch):
    """ Saves a SpotImage for a particular Spot on POST to /api/v1/spot/<spot id>/image.
    """
    @user_auth_required
    def POST(self, request, spot_id):
        spot = Spot.objects.get(pk=spot_id)

        if not "image" in request.FILES:
            raise RESTException("No image", 400)

        args = {}
        args['upload_app'] = request.META.get('SS_OAUTH_CONSUMER_NAME', '')
        args['upload_user'] = request.META.get('SS_OAUTH_USER', '')
        args['description'] = request.POST.get('description', '')
        args['image'] = request.FILES['image']

        image = spot.spotimage_set.create(**args)

        response = HttpResponse()
        response.status_code = 201
        response["Location"] = image.rest_url()

        return response
