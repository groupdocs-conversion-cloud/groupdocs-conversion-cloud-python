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
import os

from groupdocs_conversion_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestConvertApi(TestContext):
    """ConvertApi unit tests"""

    def test_convert_document(self):
        """
        Test case for convert_document

        """
        test_file = TestFile.one_page_docx()
        settings = ConvertSettings()
        settings.file_path = test_file.folder + test_file.file_name
        settings.format = "jpg"
        settings.output_path = self.OUT_FOLDER
        request = ConvertDocumentRequest(settings)
        data = self.convert_api.convert_document(request)
        self.assertTrue(len(data) > 0)
        self.assertTrue(data[0].size > 0)

    def test_convert_document_download(self):
        """
        Test case for convert_document with file result

        """
        test_file = TestFile.one_page_docx()
        settings = ConvertSettings()
        settings.file_path = test_file.folder + test_file.file_name
        settings.format = "pdf"
        request = ConvertDocumentRequest(settings)
        data = self.convert_api.convert_document_download(request)
        self.assertGreater(os.path.getsize(data), 0)

    def test_convert_document_direct(self):
        """
        Test case for convert_document with file result without using cloud storage

        """
        test_file = TestFile.four_pages_docx()
        local_file_path = self.get_test_file_path(test_file)
        format = "pdf"
        
        request = ConvertDocumentDirectRequest(format, local_file_path)
        data = self.convert_api.convert_document_direct(request)
        self.assertGreater(os.path.getsize(data), 0)        

if __name__ == '__main__':
    unittest.main()
