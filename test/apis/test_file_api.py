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

class TestFileApi(TestContext):
    """FileApi unit tests"""

    def test_delete_file(self):
        # Delete file
        test_file = TestFile.one_page_docx()
        request = DeleteFileRequest(test_file.folder + test_file.file_name)
        data = self.file_api.delete_file(request)
        # Check
        request = ObjectExistsRequest(test_file.folder + test_file.file_name)        
        data = self.storage_api.object_exists(request)
        self.assertFalse(data.exists)        
        # Upload file
        local_file_path = self.get_test_file_path(test_file)
        request = UploadFileRequest(test_file.folder + test_file.file_name, local_file_path)
        self.file_api.upload_file(request)

    def test_download_file(self):
        test_file = TestFile.one_page_docx()
        request = DownloadFileRequest(test_file.folder + test_file.file_name)
        data = self.file_api.download_file(request)
        self.assertGreater(os.path.getsize(data), 0)

    def test_copy_move_file(self):
        test_file = TestFile.one_page_docx()
        full_name = test_file.folder + test_file.file_name        
        # Create temp folder
        request = CreateFolderRequest("temp")
        self.folder_api.create_folder(request)
        # Copy file
        dest_path = "temp/" + full_name
        request = CopyFileRequest(full_name, dest_path)
        self.file_api.copy_file(request)
        # Check copied file
        request = ObjectExistsRequest(dest_path)        
        data = self.storage_api.object_exists(request)
        self.assertTrue(data.exists)
        # Move file
        new_dest_path = "temp/" + full_name.replace("page", "page_1")
        request = MoveFileRequest(dest_path, new_dest_path)
        self.file_api.move_file(request)
        # Check moved file
        request = ObjectExistsRequest(new_dest_path)        
        data = self.storage_api.object_exists(request)
        self.assertTrue(data.exists)      
        # Delete temp folder  
        request = DeleteFolderRequest("temp", None, True)
        self.folder_api.delete_folder(request)        

if __name__ == '__main__':
    unittest.main()
