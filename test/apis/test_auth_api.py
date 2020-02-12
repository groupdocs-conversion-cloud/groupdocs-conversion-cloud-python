# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_auth_api.py">
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

import unittest
import warnings

import six

from groupdocs_conversion_cloud import Configuration, InfoApi, ApiException, GetSupportedConversionTypesRequest
from test.test_settings import TestSettings

class TestAuthApi(unittest.TestCase):
    """ViewerApi unit tests"""

    def setUp(self):
        if six.PY3:
            warnings.simplefilter("ignore", ResourceWarning)

    def init_api(self, app_sid, app_key):
        configuration = Configuration(app_sid, app_key)
        configuration.api_base_url = TestSettings.API_BASE_URL
        
        return InfoApi.from_config(configuration)

    def test_auth_error_when_app_sid_not_found(self):
        """Test case to check handling of authentication errors"""
        
        app_sid = "test"
        app_key = "test"
        
        info_api = self.init_api(app_sid, app_key)
        request = GetSupportedConversionTypesRequest()
        with self.assertRaises(ApiException) as context:
            info_api.get_supported_conversion_types(request)

        self.assertEqual("invalid_client", context.exception.message)
    
    def test_auth_error_when_app_key_not_found(self):
        """Test case to check handling of authentication errors"""
        
        app_sid = TestSettings.APP_SID
        app_key = "test"
        
        info_api = self.init_api(app_sid, app_key)
        request = GetSupportedConversionTypesRequest()
        with self.assertRaises(ApiException) as context:
            info_api.get_supported_conversion_types(request)

        self.assertEqual("invalid_client", context.exception.message)

if __name__ == '__main__':
    unittest.main()
