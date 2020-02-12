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

class TestFolderApi(TestContext):
    """FolderApi unit tests"""

    def test_get_list_files(self):
        request = GetFilesListRequest("WordProcessing")
        data = self.folder_api.get_files_list(request)
        self.assertGreater(len(data.value), 0)

    def test_copy_move_folder(self):
        # Create temp folder
        request = CreateFolderRequest("temp")
        self.folder_api.create_folder(request)        
        # Copy folder
        request = CopyFolderRequest("temp", "temp1")
        self.folder_api.copy_folder(request)   
        # Check copied folder
        request = ObjectExistsRequest("temp1")        
        data = self.storage_api.object_exists(request)
        self.assertTrue(data.exists)
        self.assertTrue(data.is_folder)
        # Move folder
        request = MoveFolderRequest("temp1", "temp2")
        self.folder_api.move_folder(request)   
        # Check moved folder
        request = ObjectExistsRequest("temp1")        
        data = self.storage_api.object_exists(request)
        self.assertFalse(data.exists)
        request = ObjectExistsRequest("temp2")        
        data = self.storage_api.object_exists(request)
        self.assertTrue(data.exists)   
        # Delete temp folders  
        request = DeleteFolderRequest("temp", None, True)
        self.folder_api.delete_folder(request)
        request = DeleteFolderRequest("temp2", None, True)
        self.folder_api.delete_folder(request)        

if __name__ == '__main__':
    unittest.main()
