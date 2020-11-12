# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from groupdocs_conversion_cloud.auth import Auth
from groupdocs_conversion_cloud.api_client import ApiClient
from groupdocs_conversion_cloud.api_exception import ApiException
from groupdocs_conversion_cloud.configuration import Configuration

class ConvertApi(object):
    """
    GroupDocs.Conversion Cloud API

    :param configuration: API configuration
    """

    def __init__(self, configuration):
        api_client = ApiClient(configuration)

        self.auth = Auth(configuration, api_client)
        self.api_client = api_client
        self.configuration = configuration

    def close(self):  # noqa: E501
        """
        Closes thread pool. This method should be called when 
        methods are executed asynchronously (is_async=True is passed as parameter)
        and this instance of ConvertApi is not going to be used any more.
        """
        if self.api_client is not None:
            if(self.api_client.pool is not None):
                self.api_client.pool.close()
                self.api_client.pool.join()
                self.api_client.pool = None

    @classmethod
    def from_keys(cls, app_sid, app_key):
        """
        Initializes new instance of ConvertApi with API keys

        :param app_sid Application identifier (App SID)
        :param app_key Application private key (App Key)
        """
        configuration = Configuration(app_sid, app_key)
        return ConvertApi(configuration)

    @classmethod
    def from_config(cls, configuration):
        """
        Initializes new instance of ConvertApi with configuration options

        :param configuration API configuration
        """
        return ConvertApi(configuration)
    
    def convert_document(self, request,**kwargs):  # noqa: E501
        """Converts specified input document to format specified in the convertSettings with specified options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ConvertSettings convert_settings: (required)
        :return: list[StoredConvertedResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._convert_document_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._convert_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _convert_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Converts specified input document to format specified in the convertSettings with specified options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ConvertDocumentRequest request object with parameters
        :return: list[StoredConvertedResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'convert_settings' is set
        if request.convert_settings is None:
            raise ValueError("Missing the required parameter `convert_settings` when calling `convert_document`")  # noqa: E501

        collection_formats = {}
        path = '/conversion'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.convert_settings is not None:
            body_params = request.convert_settings
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'list[StoredConvertedResult]',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def convert_document_download(self, request,**kwargs):  # noqa: E501
        """Converts specified input document to format specified in the convertSettings with specified options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ConvertSettings convert_settings: (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._convert_document_download_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._convert_document_download_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _convert_document_download_with_http_info(self, request, **kwargs):  # noqa: E501
        """Converts specified input document to format specified in the convertSettings with specified options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ConvertDocumentRequest request object with parameters
        :return: list[StoredConvertedResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'convert_settings' is set
        if request.convert_settings is None:
            raise ValueError("Missing the required parameter `convert_settings` when calling `convert_document`")  # noqa: E501

        collection_formats = {}
        path = '/conversion'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.convert_settings is not None:
            body_params = request.convert_settings
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def convert_document_direct(self, request,**kwargs):  # noqa: E501
        """Converts input document file to format specified  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str format: Requested conversion format (required)
        :param file file: Input file to convert (required)
        :param int from_page: Page start conversion from
        :param int pages_count: Number of pages to convert
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._convert_document_direct_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._convert_document_direct_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _convert_document_direct_with_http_info(self, request, **kwargs):  # noqa: E501
        """Converts input document file to format specified  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ConvertDocumentDirectRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_document_direct" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `convert_document_direct`")  # noqa: E501
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `convert_document_direct`")  # noqa: E501

        collection_formats = {}
        path = '/conversion'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('fromPage') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromPage' + '}'), request.from_page if request.from_page is not None else '')
        else:
            if request.from_page is not None:
                query_params.append((self.__downcase_first_letter('fromPage'), request.from_page))  # noqa: E501
        if self.__downcase_first_letter('pagesCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('pagesCount' + '}'), request.pages_count if request.pages_count is not None else '')
        else:
            if request.pages_count is not None:
                query_params.append((self.__downcase_first_letter('pagesCount'), request.pages_count))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return str
        else:
            return s[0].lower() + s[1:]

# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="convert_document_request.py">
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
# --------------------------------------------------------------------------------

class ConvertDocumentRequest(object):
    """
    Request model for convert_document operation.
    :param convert_settings 
    """

    def __init__(self, convert_settings):
        """Initializes new instance of ConvertDocumentRequest."""  # noqa: E501
        self.convert_settings = convert_settings
# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="convert_document_direct_request.py">
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
# --------------------------------------------------------------------------------

class ConvertDocumentDirectRequest(object):
    """
    Request model for convert_document_direct operation.
    :param format Requested conversion format
    :param file Input file to convert
    :param from_page Page start conversion from
    :param pages_count Number of pages to convert
    """

    def __init__(self, format, file, from_page=None, pages_count=None):
        """Initializes new instance of ConvertDocumentDirectRequest."""  # noqa: E501
        self.format = format
        self.file = file
        self.from_page = from_page
        self.pages_count = pages_count
