# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ConvertSettings.py">
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

class ConvertSettings(object):
    """
    Defines conversion request
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage_name': 'str',
        'file_path': 'str',
        'format': 'str',
        'load_options': 'LoadOptions',
        'convert_options': 'ConvertOptions',
        'output_path': 'str'
    }

    attribute_map = {
        'storage_name': 'StorageName',
        'file_path': 'FilePath',
        'format': 'Format',
        'load_options': 'LoadOptions',
        'convert_options': 'ConvertOptions',
        'output_path': 'OutputPath'
    }

    def __init__(self, storage_name=None, file_path=None, format=None, load_options=None, convert_options=None, output_path=None, **kwargs):  # noqa: E501
        """Initializes new instance of ConvertSettings"""  # noqa: E501

        self._storage_name = None
        self._file_path = None
        self._format = None
        self._load_options = None
        self._convert_options = None
        self._output_path = None

        if storage_name is not None:
            self.storage_name = storage_name
        if file_path is not None:
            self.file_path = file_path
        if format is not None:
            self.format = format
        if load_options is not None:
            self.load_options = load_options
        if convert_options is not None:
            self.convert_options = convert_options
        if output_path is not None:
            self.output_path = output_path
    
    @property
    def storage_name(self):
        """
        Gets the storage_name.  # noqa: E501

        StorageName which contains the file  # noqa: E501

        :return: The storage_name.  # noqa: E501
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        """
        Sets the storage_name.

        StorageName which contains the file  # noqa: E501

        :param storage_name: The storage_name.  # noqa: E501
        :type: str
        """
        self._storage_name = storage_name
    
    @property
    def file_path(self):
        """
        Gets the file_path.  # noqa: E501

        Gets or sets absolute path to a file in the storage  # noqa: E501

        :return: The file_path.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the file_path.

        Gets or sets absolute path to a file in the storage  # noqa: E501

        :param file_path: The file_path.  # noqa: E501
        :type: str
        """
        if file_path is None:
            raise ValueError("Invalid value for `file_path`, must not be `None`")  # noqa: E501
        if file_path is not None and len(file_path) < 1:
            raise ValueError("Invalid value for `file_path`, length must be greater than or equal to `1`")  # noqa: E501
        self._file_path = file_path
    
    @property
    def format(self):
        """
        Gets the format.  # noqa: E501

        Gets or sets requested conversion format  # noqa: E501

        :return: The format.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format.

        Gets or sets requested conversion format  # noqa: E501

        :param format: The format.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        if format is not None and len(format) < 1:
            raise ValueError("Invalid value for `format`, length must be greater than or equal to `1`")  # noqa: E501
        self._format = format
    
    @property
    def load_options(self):
        """
        Gets the load_options.  # noqa: E501

        Gets or sets format specific load options for source file  # noqa: E501

        :return: The load_options.  # noqa: E501
        :rtype: LoadOptions
        """
        return self._load_options

    @load_options.setter
    def load_options(self, load_options):
        """
        Sets the load_options.

        Gets or sets format specific load options for source file  # noqa: E501

        :param load_options: The load_options.  # noqa: E501
        :type: LoadOptions
        """
        self._load_options = load_options
    
    @property
    def convert_options(self):
        """
        Gets the convert_options.  # noqa: E501

        Gets or sets format specific convert options for output file  # noqa: E501

        :return: The convert_options.  # noqa: E501
        :rtype: ConvertOptions
        """
        return self._convert_options

    @convert_options.setter
    def convert_options(self, convert_options):
        """
        Sets the convert_options.

        Gets or sets format specific convert options for output file  # noqa: E501

        :param convert_options: The convert_options.  # noqa: E501
        :type: ConvertOptions
        """
        self._convert_options = convert_options
    
    @property
    def output_path(self):
        """
        Gets the output_path.  # noqa: E501

        Gets or sets converted file save path  # noqa: E501

        :return: The output_path.  # noqa: E501
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """
        Sets the output_path.

        Gets or sets converted file save path  # noqa: E501

        :param output_path: The output_path.  # noqa: E501
        :type: str
        """
        self._output_path = output_path

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
        if not isinstance(other, ConvertSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
