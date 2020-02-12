# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="api_exception.py">
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

import json

class ApiException(Exception):
    """
    API exception
    """

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.code = http_resp.status

            try:
                data = json.loads(http_resp.data)
                
                error = data.get("error")
                error_api = data.get("Error")
                
                if error is not None:
                    self.message = error
                elif error_api is not None:
                    self.message = error_api.get("Message") if error_api.get("Message") is not None else http_resp.data
                else:
                    self.message = http_resp.data   
            except ValueError:
                self.message = http_resp.data
        else:
            self.code = status
            self.message = reason

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Message: {1}\n".format(self.code, self.message)

        return error_message
