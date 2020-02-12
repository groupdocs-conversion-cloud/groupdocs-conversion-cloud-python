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

import unittest

from groupdocs_conversion_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestStorageApi(TestContext):
    """StorageApi unit tests"""

    def test_get_disc_usage(self):
        request = GetDiscUsageRequest()
        data = self.storage_api.get_disc_usage(request)
        self.assertGreater(data.total_size, 0)
        self.assertGreater(data.used_size, 0)

    def test_get_storage_exist(self):
        request = StorageExistsRequest("First Storage")
        data = self.storage_api.storage_exists(request)
        self.assertTrue(data.exists) 

    def test_get_file_versions(self):
        test_file = TestFile.one_page_docx()
        request = GetFileVersionsRequest(test_file.folder + test_file.file_name)        
        data = self.storage_api.get_file_versions(request)
        self.assertGreater(len(data.value), 0)

    def test_get_object_exists(self):
        test_file = TestFile.one_page_docx()
        request = ObjectExistsRequest(test_file.folder + test_file.file_name)        
        data = self.storage_api.object_exists(request)
        self.assertTrue(data.exists)
        self.assertFalse(data.is_folder)

if __name__ == '__main__':
    unittest.main()
