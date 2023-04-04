# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="EBookConvertOptions.py">
#   Copyright (c) 2003-2023 Aspose Pty Ltd
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

from groupdocs_conversion_cloud.models import ConvertOptions

class EBookConvertOptions(ConvertOptions):
    """
    Ebook convert options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_size': 'str',
        'page_orientation': 'str'
    }

    attribute_map = {
        'page_size': 'PageSize',
        'page_orientation': 'PageOrientation'
    }

    def __init__(self, page_size=None, page_orientation=None, **kwargs):  # noqa: E501
        """Initializes new instance of EBookConvertOptions"""  # noqa: E501

        self._page_size = None
        self._page_orientation = None

        if page_size is not None:
            self.page_size = page_size
        if page_orientation is not None:
            self.page_orientation = page_orientation

        base = super(EBookConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        Specifies page size  # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        Specifies page size  # noqa: E501

        :param page_size: The page_size.  # noqa: E501
        :type: str
        """
        if page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "A3", "Statement", "Quarto", "Paper11x17", "Paper10x14", "Letter", "Legal", "Ledger", "Folio", "Executive", "EnvelopeDL", "Custom", "B5", "B4", "A5", "A4", "Tabloid"]  # noqa: E501
        if not page_size.isdigit():	
            if page_size not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_size` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_size, allowed_values))
            self._page_size = page_size
        else:
            self._page_size = allowed_values[int(page_size) if six.PY3 else long(page_size)]
    
    @property
    def page_orientation(self):
        """
        Gets the page_orientation.  # noqa: E501

        Specifies page orientation  # noqa: E501

        :return: The page_orientation.  # noqa: E501
        :rtype: str
        """
        return self._page_orientation

    @page_orientation.setter
    def page_orientation(self, page_orientation):
        """
        Sets the page_orientation.

        Specifies page orientation  # noqa: E501

        :param page_orientation: The page_orientation.  # noqa: E501
        :type: str
        """
        if page_orientation is None:
            raise ValueError("Invalid value for `page_orientation`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "Landscape", "Portrait"]  # noqa: E501
        if not page_orientation.isdigit():	
            if page_orientation not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_orientation` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_orientation, allowed_values))
            self._page_orientation = page_orientation
        else:
            self._page_orientation = allowed_values[int(page_orientation) if six.PY3 else long(page_orientation)]

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
        if not isinstance(other, EBookConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
