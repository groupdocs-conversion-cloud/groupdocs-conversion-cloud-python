# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_file.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
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

class TestFile:
    """Test file"""

    @classmethod
    def one_page_docx(cls):
        f = TestFile()
        f.file_name = "one-page.docx"
        f.folder = "words\\docx\\"
        return f

    @classmethod
    def not_exist(cls):
        f = TestFile()
        f.file_name = "not-exist.docx"
        f.folder = "somefolder\\"
        return f

    @classmethod
    def password_protected_docx(cls):
        f = TestFile()
        f.file_name = "password-protected.docx"
        f.folder = "words\\docx\\"
        f.password = "password"
        return f

    @classmethod
    def two_hidden_pages_vsd(cls):
        f = TestFile()
        f.file_name = "two-hidden-pages.vsd"
        f.folder = "diagram\\vsd\\"
        return f

    @classmethod
    def with_hidden_rows_and_columns(cls):
        f = TestFile()
        f.file_name = "with-hidden-rows-and-columns.xlsx"
        f.folder = "cells\\xlsx\\"
        return f

    @classmethod
    def three_layouts_dwf(cls):
        f = TestFile()
        f.file_name = "three-layouts.dwf"
        f.folder = "cad\\dwf\\"
        return f

    @classmethod
    def project_mpp(cls):
        f = TestFile()
        f.file_name = "sample.mpp"
        f.folder = "project\\mpp\\"
        return f

    @classmethod
    def uses_custom_font_pptx(cls):
        f = TestFile()
        f.file_name = "uses-custom-font.pptx"
        f.folder = "slides\\pptx\\"
        return f

    @classmethod
    def font_ttf(cls):
        f = TestFile()
        f.file_name = "foo.ttf"
        f.folder = "font\\ttf\\"
        return f

    @classmethod
    def four_pages_docx(cls):
        f = TestFile()
        f.file_name = "four-pages.docx"
        f.folder = "words\\docx\\"
        return f


    @classmethod
    def get_test_files(cls):
        return [
            cls.one_page_docx(),
            cls.password_protected_docx(),
            cls.two_hidden_pages_vsd(),
            cls.with_hidden_rows_and_columns(),
            cls.three_layouts_dwf(),
            cls.project_mpp(),
            cls.uses_custom_font_pptx(),
            cls.font_ttf(),
            cls.four_pages_docx()            
        ]

