# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="TxtLoadOptions.py">
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

from groupdocs_conversion_cloud.models import LoadOptions

class TxtLoadOptions(LoadOptions):
    """
    Txt document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'detect_numbering_with_whitespaces': 'bool',
        'trailing_spaces_options': 'str',
        'leading_spaces_options': 'str',
        'encoding': 'str'
    }

    attribute_map = {
        'detect_numbering_with_whitespaces': 'DetectNumberingWithWhitespaces',
        'trailing_spaces_options': 'TrailingSpacesOptions',
        'leading_spaces_options': 'LeadingSpacesOptions',
        'encoding': 'Encoding'
    }

    def __init__(self, detect_numbering_with_whitespaces=None, trailing_spaces_options=None, leading_spaces_options=None, encoding=None, **kwargs):  # noqa: E501
        """Initializes new instance of TxtLoadOptions"""  # noqa: E501

        self._detect_numbering_with_whitespaces = None
        self._trailing_spaces_options = None
        self._leading_spaces_options = None
        self._encoding = None

        if detect_numbering_with_whitespaces is not None:
            self.detect_numbering_with_whitespaces = detect_numbering_with_whitespaces
        if trailing_spaces_options is not None:
            self.trailing_spaces_options = trailing_spaces_options
        if leading_spaces_options is not None:
            self.leading_spaces_options = leading_spaces_options
        if encoding is not None:
            self.encoding = encoding

        base = super(TxtLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def detect_numbering_with_whitespaces(self):
        """
        Gets the detect_numbering_with_whitespaces.  # noqa: E501

        Allows to specify how numbered list items are recognized when plain text document is converted. The default value is true.  # noqa: E501

        :return: The detect_numbering_with_whitespaces.  # noqa: E501
        :rtype: bool
        """
        return self._detect_numbering_with_whitespaces

    @detect_numbering_with_whitespaces.setter
    def detect_numbering_with_whitespaces(self, detect_numbering_with_whitespaces):
        """
        Sets the detect_numbering_with_whitespaces.

        Allows to specify how numbered list items are recognized when plain text document is converted. The default value is true.  # noqa: E501

        :param detect_numbering_with_whitespaces: The detect_numbering_with_whitespaces.  # noqa: E501
        :type: bool
        """
        if detect_numbering_with_whitespaces is None:
            raise ValueError("Invalid value for `detect_numbering_with_whitespaces`, must not be `None`")  # noqa: E501
        self._detect_numbering_with_whitespaces = detect_numbering_with_whitespaces
    
    @property
    def trailing_spaces_options(self):
        """
        Gets the trailing_spaces_options.  # noqa: E501

        Gets or sets preferred option of a trailing space handling. Default value is Trim.  # noqa: E501

        :return: The trailing_spaces_options.  # noqa: E501
        :rtype: str
        """
        return self._trailing_spaces_options

    @trailing_spaces_options.setter
    def trailing_spaces_options(self, trailing_spaces_options):
        """
        Sets the trailing_spaces_options.

        Gets or sets preferred option of a trailing space handling. Default value is Trim.  # noqa: E501

        :param trailing_spaces_options: The trailing_spaces_options.  # noqa: E501
        :type: str
        """
        if trailing_spaces_options is None:
            raise ValueError("Invalid value for `trailing_spaces_options`, must not be `None`")  # noqa: E501
        allowed_values = ["Preserve", "Trim"]  # noqa: E501
        if not trailing_spaces_options.isdigit():	
            if trailing_spaces_options not in allowed_values:
                raise ValueError(
                    "Invalid value for `trailing_spaces_options` ({0}), must be one of {1}"  # noqa: E501
                    .format(trailing_spaces_options, allowed_values))
            self._trailing_spaces_options = trailing_spaces_options
        else:
            self._trailing_spaces_options = allowed_values[int(trailing_spaces_options) if six.PY3 else long(trailing_spaces_options)]
    
    @property
    def leading_spaces_options(self):
        """
        Gets the leading_spaces_options.  # noqa: E501

        Gets or sets preferred option of a leading space handling. Default value is ConvertToIndent.  # noqa: E501

        :return: The leading_spaces_options.  # noqa: E501
        :rtype: str
        """
        return self._leading_spaces_options

    @leading_spaces_options.setter
    def leading_spaces_options(self, leading_spaces_options):
        """
        Sets the leading_spaces_options.

        Gets or sets preferred option of a leading space handling. Default value is ConvertToIndent.  # noqa: E501

        :param leading_spaces_options: The leading_spaces_options.  # noqa: E501
        :type: str
        """
        if leading_spaces_options is None:
            raise ValueError("Invalid value for `leading_spaces_options`, must not be `None`")  # noqa: E501
        allowed_values = ["ConvertToIndent", "Preserve", "Trim"]  # noqa: E501
        if not leading_spaces_options.isdigit():	
            if leading_spaces_options not in allowed_values:
                raise ValueError(
                    "Invalid value for `leading_spaces_options` ({0}), must be one of {1}"  # noqa: E501
                    .format(leading_spaces_options, allowed_values))
            self._leading_spaces_options = leading_spaces_options
        else:
            self._leading_spaces_options = allowed_values[int(leading_spaces_options) if six.PY3 else long(leading_spaces_options)]
    
    @property
    def encoding(self):
        """
        Gets the encoding.  # noqa: E501

        Gets or sets the encoding that will be used when loading Txt document. Can be null. Default is null.  # noqa: E501

        :return: The encoding.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding.

        Gets or sets the encoding that will be used when loading Txt document. Can be null. Default is null.  # noqa: E501

        :param encoding: The encoding.  # noqa: E501
        :type: str
        """
        self._encoding = encoding

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
        if not isinstance(other, TxtLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
