# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ConvertOptions.py">
#   Copyright (c) 2003-2024 Aspose Pty Ltd
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

import pprint
import re  # noqa: F401

import six

class ConvertOptions(object):
    """
    ConvertOptions base
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'from_page': 'int',
        'pages_count': 'int',
        'pages': 'list[int]',
        'watermark_options': 'WatermarkOptions'
    }

    attribute_map = {
        'from_page': 'FromPage',
        'pages_count': 'PagesCount',
        'pages': 'Pages',
        'watermark_options': 'WatermarkOptions'
    }

    def __init__(self, from_page=None, pages_count=None, pages=None, watermark_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of ConvertOptions"""  # noqa: E501

        self._from_page = None
        self._pages_count = None
        self._pages = None
        self._watermark_options = None

        if from_page is not None:
            self.from_page = from_page
        if pages_count is not None:
            self.pages_count = pages_count
        if pages is not None:
            self.pages = pages
        if watermark_options is not None:
            self.watermark_options = watermark_options
    
    @property
    def from_page(self):
        """
        Gets the from_page.  # noqa: E501

        Start conversion from FromPage page  # noqa: E501

        :return: The from_page.  # noqa: E501
        :rtype: int
        """
        return self._from_page

    @from_page.setter
    def from_page(self, from_page):
        """
        Sets the from_page.

        Start conversion from FromPage page  # noqa: E501

        :param from_page: The from_page.  # noqa: E501
        :type: int
        """
        if from_page is None:
            raise ValueError("Invalid value for `from_page`, must not be `None`")  # noqa: E501
        self._from_page = from_page
    
    @property
    def pages_count(self):
        """
        Gets the pages_count.  # noqa: E501

        Number of pages to convert  # noqa: E501

        :return: The pages_count.  # noqa: E501
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """
        Sets the pages_count.

        Number of pages to convert  # noqa: E501

        :param pages_count: The pages_count.  # noqa: E501
        :type: int
        """
        if pages_count is None:
            raise ValueError("Invalid value for `pages_count`, must not be `None`")  # noqa: E501
        self._pages_count = pages_count
    
    @property
    def pages(self):
        """
        Gets the pages.  # noqa: E501

        Convert specific pages. The list contains the page indexes of the pages to be converted  # noqa: E501

        :return: The pages.  # noqa: E501
        :rtype: list[int]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages.

        Convert specific pages. The list contains the page indexes of the pages to be converted  # noqa: E501

        :param pages: The pages.  # noqa: E501
        :type: list[int]
        """
        self._pages = pages
    
    @property
    def watermark_options(self):
        """
        Gets the watermark_options.  # noqa: E501

        Watermark specific options  # noqa: E501

        :return: The watermark_options.  # noqa: E501
        :rtype: WatermarkOptions
        """
        return self._watermark_options

    @watermark_options.setter
    def watermark_options(self, watermark_options):
        """
        Sets the watermark_options.

        Watermark specific options  # noqa: E501

        :param watermark_options: The watermark_options.  # noqa: E501
        :type: WatermarkOptions
        """
        self._watermark_options = watermark_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
