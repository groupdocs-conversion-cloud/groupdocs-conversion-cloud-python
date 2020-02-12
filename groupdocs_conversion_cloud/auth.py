# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="auth.py">
#   Copyright (c) 2003-2020 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

from __future__ import absolute_import

import six
import datetime

from groupdocs_conversion_cloud.api_client import ApiClient 

class Auth(object):
    """
    API authorization

    :param configuration: API configuration
    :param api_client: API client
    """

    def __init__(self, configuration, api_client):
        self.configuration = configuration
        self.api_client = api_client
        self._access_token = None

    def get_auth_settings(self):
        access_token = self._get_access_token()        

        auth_settings = {
            'type': 'oauth2',
            'in': 'header',
            'key': 'Authorization',
            'value': 'Bearer ' + access_token
        }

        return auth_settings

    def _get_access_token(self):
        if self._access_token is None:
            self._request_access_token()
           
        return self._access_token

    def _request_access_token(self):
        request_url = "/connect/token"
        header_params = {
            'Accept': 'application/json', 
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        form_params = [
            ('grant_type', 'client_credentials'), 
            ('client_id', self.configuration.app_sid),
            ('client_secret', self.configuration.app_key)
        ]
        
        data = self.api_client.call_api(
            resource_path = request_url, 
            method = 'POST',
            header_params = header_params,
            post_params = form_params,
            response_type = 'object',
            _return_http_data_only = True,
            _append_api_version = False
        )

        self._update_tokens(data)    

    def _update_tokens(self, data):
        self._access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
