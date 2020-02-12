# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_context.py">
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

import glob
import json
import os
import tempfile
import unittest
import warnings
import threading
import six

from groupdocs_conversion_cloud import Configuration, ConvertApi, InfoApi, StorageApi, FileApi, FolderApi
from groupdocs_conversion_cloud import ObjectExistsRequest, UploadFileRequest, DeleteFolderRequest
from test.test_settings import TestSettings
from test.test_file import TestFile

class TestContext(unittest.TestCase):
    OUT_FOLDER="converted"

    convert_api = None
    info_api = None
    storage_api = None
    file_api = None
    folder_api = None
    _test_files_uploaded = False

    def setUp(self):
        if six.PY3:
            warnings.simplefilter("ignore", ResourceWarning)

        self._init_api()
        self._upload_test_files()

    def tearDown(self):
        self._remove_folder_in_storage(self.OUT_FOLDER)
        self._close_api_thread_pool()

    def get_test_file_path(self, file):
        test_files = "test\\test_files"
        test_file_path = os.path.join(test_files, file.folder, file.file_name) 

        return test_file_path

    def to_json_file(self, obj):
        obj_dict = { obj.attribute_map[attr]: getattr(obj, attr)
                     for attr, _ in six.iteritems(obj.swagger_types)
                     if hasattr(obj, attr) and getattr(obj, attr) is not None }

        json_str = json.dumps(obj_dict)

        temp_file = tempfile.NamedTemporaryFile("w", delete = False)

        json_file = temp_file.file
        json_file.write(json_str)
        json_file.close()

        return temp_file.name

    def _close_api_thread_pool(self):
        self.convert_api.close()
        self.info_api.close()
        self.storage_api.close()
        self.file_api.close()
        self.folder_api.close()

    def _remove_folder_in_storage(self, folder):
        request = DeleteFolderRequest(folder, None, True)
        self.folder_api.delete_folder(request)
        return

    def _upload_test_files(self):
        if TestContext._test_files_uploaded:
            return

        for test_file in TestFile.get_test_files():
            local_file_path = self.get_test_file_path(test_file)
            remote_file_path = test_file.folder + test_file.file_name            
            exist_request = ObjectExistsRequest(remote_file_path)
            response = self.storage_api.object_exists(exist_request)
            if not response.exists:
                print('Upload file: ' + remote_file_path)
                request = UploadFileRequest(remote_file_path, local_file_path)
                self.file_api.upload_file(request)

        TestContext._test_files_uploaded = True

    def _init_api(self):
        if self.convert_api is None:
            configuration = Configuration(TestSettings.APP_SID, TestSettings.APP_KEY)
            configuration.api_base_url = TestSettings.API_BASE_URL
            #configuration.debug = True
            self.convert_api = ConvertApi.from_config(configuration)
            self.info_api = InfoApi.from_config(configuration)
            self.storage_api = StorageApi.from_config(configuration)
            self.file_api = FileApi.from_config(configuration)
            self.folder_api = FolderApi.from_config(configuration)
