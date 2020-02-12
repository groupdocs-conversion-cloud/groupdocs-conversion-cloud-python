# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="CsvLoadOptions.py">
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

class CsvLoadOptions(LoadOptions):
    """
    Csv document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'separator': 'str',
        'is_multi_encoded': 'bool',
        'has_formula': 'bool',
        'convert_numeric_data': 'bool',
        'convert_date_time_data': 'bool',
        'encoding': 'str'
    }

    attribute_map = {
        'separator': 'Separator',
        'is_multi_encoded': 'IsMultiEncoded',
        'has_formula': 'HasFormula',
        'convert_numeric_data': 'ConvertNumericData',
        'convert_date_time_data': 'ConvertDateTimeData',
        'encoding': 'Encoding'
    }

    def __init__(self, separator=None, is_multi_encoded=None, has_formula=None, convert_numeric_data=None, convert_date_time_data=None, encoding=None, **kwargs):  # noqa: E501
        """Initializes new instance of CsvLoadOptions"""  # noqa: E501

        self._separator = None
        self._is_multi_encoded = None
        self._has_formula = None
        self._convert_numeric_data = None
        self._convert_date_time_data = None
        self._encoding = None

        if separator is not None:
            self.separator = separator
        if is_multi_encoded is not None:
            self.is_multi_encoded = is_multi_encoded
        if has_formula is not None:
            self.has_formula = has_formula
        if convert_numeric_data is not None:
            self.convert_numeric_data = convert_numeric_data
        if convert_date_time_data is not None:
            self.convert_date_time_data = convert_date_time_data
        if encoding is not None:
            self.encoding = encoding

        base = super(CsvLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def separator(self):
        """
        Gets the separator.  # noqa: E501

        Delimiter of a Csv file  # noqa: E501

        :return: The separator.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """
        Sets the separator.

        Delimiter of a Csv file  # noqa: E501

        :param separator: The separator.  # noqa: E501
        :type: str
        """
        if separator is None:
            raise ValueError("Invalid value for `separator`, must not be `None`")  # noqa: E501
        self._separator = separator
    
    @property
    def is_multi_encoded(self):
        """
        Gets the is_multi_encoded.  # noqa: E501

        True means the file contains several encodings  # noqa: E501

        :return: The is_multi_encoded.  # noqa: E501
        :rtype: bool
        """
        return self._is_multi_encoded

    @is_multi_encoded.setter
    def is_multi_encoded(self, is_multi_encoded):
        """
        Sets the is_multi_encoded.

        True means the file contains several encodings  # noqa: E501

        :param is_multi_encoded: The is_multi_encoded.  # noqa: E501
        :type: bool
        """
        if is_multi_encoded is None:
            raise ValueError("Invalid value for `is_multi_encoded`, must not be `None`")  # noqa: E501
        self._is_multi_encoded = is_multi_encoded
    
    @property
    def has_formula(self):
        """
        Gets the has_formula.  # noqa: E501

        Indicates whether text is formula if it starts with \"=\"  # noqa: E501

        :return: The has_formula.  # noqa: E501
        :rtype: bool
        """
        return self._has_formula

    @has_formula.setter
    def has_formula(self, has_formula):
        """
        Sets the has_formula.

        Indicates whether text is formula if it starts with \"=\"  # noqa: E501

        :param has_formula: The has_formula.  # noqa: E501
        :type: bool
        """
        if has_formula is None:
            raise ValueError("Invalid value for `has_formula`, must not be `None`")  # noqa: E501
        self._has_formula = has_formula
    
    @property
    def convert_numeric_data(self):
        """
        Gets the convert_numeric_data.  # noqa: E501

        Indicates whether the string in the file is converted to numeric. Default is True  # noqa: E501

        :return: The convert_numeric_data.  # noqa: E501
        :rtype: bool
        """
        return self._convert_numeric_data

    @convert_numeric_data.setter
    def convert_numeric_data(self, convert_numeric_data):
        """
        Sets the convert_numeric_data.

        Indicates whether the string in the file is converted to numeric. Default is True  # noqa: E501

        :param convert_numeric_data: The convert_numeric_data.  # noqa: E501
        :type: bool
        """
        if convert_numeric_data is None:
            raise ValueError("Invalid value for `convert_numeric_data`, must not be `None`")  # noqa: E501
        self._convert_numeric_data = convert_numeric_data
    
    @property
    def convert_date_time_data(self):
        """
        Gets the convert_date_time_data.  # noqa: E501

        Indicates whether the string in the file is converted to date. Default is True  # noqa: E501

        :return: The convert_date_time_data.  # noqa: E501
        :rtype: bool
        """
        return self._convert_date_time_data

    @convert_date_time_data.setter
    def convert_date_time_data(self, convert_date_time_data):
        """
        Sets the convert_date_time_data.

        Indicates whether the string in the file is converted to date. Default is True  # noqa: E501

        :param convert_date_time_data: The convert_date_time_data.  # noqa: E501
        :type: bool
        """
        if convert_date_time_data is None:
            raise ValueError("Invalid value for `convert_date_time_data`, must not be `None`")  # noqa: E501
        self._convert_date_time_data = convert_date_time_data
    
    @property
    def encoding(self):
        """
        Gets the encoding.  # noqa: E501

        File encoding  # noqa: E501

        :return: The encoding.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding.

        File encoding  # noqa: E501

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
        if not isinstance(other, CsvLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
