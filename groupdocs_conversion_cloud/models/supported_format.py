# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="SupportedFormat.py">
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

import pprint
import re  # noqa: F401

import six

class SupportedFormat(object):
    """
    Represents information about supported conversion for SourceFormat
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_format': 'str',
        'target_formats': 'list[str]'
    }

    attribute_map = {
        'source_format': 'SourceFormat',
        'target_formats': 'TargetFormats'
    }

    def __init__(self, source_format=None, target_formats=None, **kwargs):  # noqa: E501
        """Initializes new instance of SupportedFormat"""  # noqa: E501

        self._source_format = None
        self._target_formats = None

        if source_format is not None:
            self.source_format = source_format
        if target_formats is not None:
            self.target_formats = target_formats
    
    @property
    def source_format(self):
        """
        Gets the source_format.  # noqa: E501

        Gets or sets source format  # noqa: E501

        :return: The source_format.  # noqa: E501
        :rtype: str
        """
        return self._source_format

    @source_format.setter
    def source_format(self, source_format):
        """
        Sets the source_format.

        Gets or sets source format  # noqa: E501

        :param source_format: The source_format.  # noqa: E501
        :type: str
        """
        self._source_format = source_format
    
    @property
    def target_formats(self):
        """
        Gets the target_formats.  # noqa: E501

        Gets or sets target formats  # noqa: E501

        :return: The target_formats.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_formats

    @target_formats.setter
    def target_formats(self, target_formats):
        """
        Sets the target_formats.

        Gets or sets target formats  # noqa: E501

        :param target_formats: The target_formats.  # noqa: E501
        :type: list[str]
        """
        self._target_formats = target_formats

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
        if not isinstance(other, SupportedFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
