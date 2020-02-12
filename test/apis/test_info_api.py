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

class TestInfoApi(TestContext):
    """InfoApi unit tests"""

    def test_get_supported_conversion_types(self):
        """
        Test case for supported_conversion_types

        """
        request = GetSupportedConversionTypesRequest()
        data = self.info_api.get_supported_conversion_types(request)

        for entry in data:
            self.assertFalse(entry.source_format == "")
            self.assertTrue(len(entry.target_formats) > 0)

    def test_get_document_metadata(self):
        """
        Test case for get_document_metadata

        """

        test_file = TestFile.four_pages_docx()
        file_path = test_file.folder + test_file.file_name
        request = GetDocumentMetadataRequest(file_path)
        data = self.info_api.get_document_metadata(request)

        self.assertTrue(data.page_count == 4)

if __name__ == '__main__':
    unittest.main()
