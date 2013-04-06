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

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import simplejson as json


class RESTException(Exception):
    """
    Can be thrown inside RESTful methods. Accepts a specific
    status code to use, or 500 by default.
    """
    def __init__(self, message, status_code):
        super(RESTException, self).__init__(message)
        self.status_code = status_code


class RESTFormInvalidError(RESTException):
    """Thrown when a form is invalid, and holds all the errors."""
    def __init__(self, form):
        super(RESTFormInvalidError, self).__init__("Form is invalid", 422)
        self.form = form


class RESTDispatch:
    """ Handles passing on the request to the correct view method based on the request type.
    """

    def run(self, *args, **named_args):
        request = args[0]
        method = request.META['REQUEST_METHOD']

        try:
            if "GET" == method and hasattr(self, "GET"):
                response = self.GET(*args, **named_args)
            elif "POST" == method and hasattr(self, "POST"):
                response = self.POST(*args, **named_args)
            elif "PUT" == method and hasattr(self, "PUT"):
                response = self.PUT(*args, **named_args)
            elif "DELETE" == method and hasattr(self, "DELETE"):
                response = self.DELETE(*args, **named_args)
            else:
                raise RESTException("Method not allowed", 405)

        except ObjectDoesNotExist as odne:
            response = HttpResponse(json.dumps({"error": odne.message}))
            response.status_code = 404
        except RESTFormInvalidError as fie:
            response = HttpResponse(json.dumps({"error": fie.form.errors}))
            response.status_code = fie.status_code
        except RESTException as rest_e:
            response = HttpResponse(json.dumps({"error": rest_e.message}))
            response.status_code = rest_e.status_code
        except Exception as e:
            response = HttpResponse(json.dumps({"error": e.message}))
            response.status_code = 500

        return response

    def validate_etag(self, request, obj):
        if not "HTTP_IF_MATCH" in request.META:
            if not "If_Match" in request.META:
                raise RESTException("If-Match header required", 400)
            else:
                request.META["HTTP_IF_MATCH"] = request.META["If_Match"]

        if request.META["HTTP_IF_MATCH"] != obj.etag:
            raise RESTException("Invalid ETag", 409)
