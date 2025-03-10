# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PersonalStorageLoadOptions.py">
#   Copyright (c) Aspose Pty Ltd
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

class PersonalStorageLoadOptions(LoadOptions):
    """
    Options for loading personal storage documents.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'folder': 'str',
        'depth': 'int'
    }

    attribute_map = {
        'folder': 'Folder',
        'depth': 'Depth'
    }

    def __init__(self, folder=None, depth=None, **kwargs):  # noqa: E501
        """Initializes new instance of PersonalStorageLoadOptions"""  # noqa: E501

        self._folder = None
        self._depth = None

        if folder is not None:
            self.folder = folder
        if depth is not None:
            self.depth = depth

        base = super(PersonalStorageLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def folder(self):
        """
        Gets the folder.  # noqa: E501

        Folder which to be processed Default is Inbox  # noqa: E501

        :return: The folder.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder.

        Folder which to be processed Default is Inbox  # noqa: E501

        :param folder: The folder.  # noqa: E501
        :type: str
        """
        self._folder = folder
    
    @property
    def depth(self):
        """
        Gets the depth.  # noqa: E501

        Controls how many levels in depth to perform conversion  # noqa: E501

        :return: The depth.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth.

        Controls how many levels in depth to perform conversion  # noqa: E501

        :param depth: The depth.  # noqa: E501
        :type: int
        """
        if depth is None:
            raise ValueError("Invalid value for `depth`, must not be `None`")  # noqa: E501
        self._depth = depth

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
        if not isinstance(other, PersonalStorageLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
