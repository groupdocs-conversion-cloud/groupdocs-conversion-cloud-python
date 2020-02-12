# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="DocumentMetadata.py">
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

class DocumentMetadata(object):
    """
    Contains a document metadata 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_type': 'str',
        'page_count': 'int',
        'size': 'int',
        'width': 'int',
        'height': 'int',
        'horizontal_resolution': 'int',
        'vertical_resolution': 'int',
        'bits_per_pixel': 'int',
        'title': 'str',
        'author': 'str',
        'created_date': 'datetime',
        'modified_date': 'datetime',
        'layers': 'list[str]',
        'is_password_protected': 'bool'
    }

    attribute_map = {
        'file_type': 'FileType',
        'page_count': 'PageCount',
        'size': 'Size',
        'width': 'Width',
        'height': 'Height',
        'horizontal_resolution': 'HorizontalResolution',
        'vertical_resolution': 'VerticalResolution',
        'bits_per_pixel': 'BitsPerPixel',
        'title': 'Title',
        'author': 'Author',
        'created_date': 'CreatedDate',
        'modified_date': 'ModifiedDate',
        'layers': 'Layers',
        'is_password_protected': 'IsPasswordProtected'
    }

    def __init__(self, file_type=None, page_count=None, size=None, width=None, height=None, horizontal_resolution=None, vertical_resolution=None, bits_per_pixel=None, title=None, author=None, created_date=None, modified_date=None, layers=None, is_password_protected=None, **kwargs):  # noqa: E501
        """Initializes new instance of DocumentMetadata"""  # noqa: E501

        self._file_type = None
        self._page_count = None
        self._size = None
        self._width = None
        self._height = None
        self._horizontal_resolution = None
        self._vertical_resolution = None
        self._bits_per_pixel = None
        self._title = None
        self._author = None
        self._created_date = None
        self._modified_date = None
        self._layers = None
        self._is_password_protected = None

        if file_type is not None:
            self.file_type = file_type
        if page_count is not None:
            self.page_count = page_count
        if size is not None:
            self.size = size
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if horizontal_resolution is not None:
            self.horizontal_resolution = horizontal_resolution
        if vertical_resolution is not None:
            self.vertical_resolution = vertical_resolution
        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if layers is not None:
            self.layers = layers
        if is_password_protected is not None:
            self.is_password_protected = is_password_protected
    
    @property
    def file_type(self):
        """
        Gets the file_type.  # noqa: E501

        Document file type  # noqa: E501

        :return: The file_type.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """
        Sets the file_type.

        Document file type  # noqa: E501

        :param file_type: The file_type.  # noqa: E501
        :type: str
        """
        self._file_type = file_type
    
    @property
    def page_count(self):
        """
        Gets the page_count.  # noqa: E501

        Gets pages count if applicable to the current document format  # noqa: E501

        :return: The page_count.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count.

        Gets pages count if applicable to the current document format  # noqa: E501

        :param page_count: The page_count.  # noqa: E501
        :type: int
        """
        if page_count is None:
            raise ValueError("Invalid value for `page_count`, must not be `None`")  # noqa: E501
        self._page_count = page_count
    
    @property
    def size(self):
        """
        Gets the size.  # noqa: E501

        Document bytes size  # noqa: E501

        :return: The size.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size.

        Document bytes size  # noqa: E501

        :param size: The size.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        self._size = size
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Returns detected width if applicable to the current document format  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Returns detected width if applicable to the current document format  # noqa: E501

        :param width: The width.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        Returns detected height if applicable to the current document format  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Returns detected height if applicable to the current document format  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def horizontal_resolution(self):
        """
        Gets the horizontal_resolution.  # noqa: E501

        Returns detected horizontal resolution if applicable to the current document format  # noqa: E501

        :return: The horizontal_resolution.  # noqa: E501
        :rtype: int
        """
        return self._horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """
        Sets the horizontal_resolution.

        Returns detected horizontal resolution if applicable to the current document format  # noqa: E501

        :param horizontal_resolution: The horizontal_resolution.  # noqa: E501
        :type: int
        """
        if horizontal_resolution is None:
            raise ValueError("Invalid value for `horizontal_resolution`, must not be `None`")  # noqa: E501
        self._horizontal_resolution = horizontal_resolution
    
    @property
    def vertical_resolution(self):
        """
        Gets the vertical_resolution.  # noqa: E501

        Returns detected vertical resolution if applicable to the current document format  # noqa: E501

        :return: The vertical_resolution.  # noqa: E501
        :rtype: int
        """
        return self._vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """
        Sets the vertical_resolution.

        Returns detected vertical resolution if applicable to the current document format  # noqa: E501

        :param vertical_resolution: The vertical_resolution.  # noqa: E501
        :type: int
        """
        if vertical_resolution is None:
            raise ValueError("Invalid value for `vertical_resolution`, must not be `None`")  # noqa: E501
        self._vertical_resolution = vertical_resolution
    
    @property
    def bits_per_pixel(self):
        """
        Gets the bits_per_pixel.  # noqa: E501

        Returns detected bits per pixel if applicable to the current document format  # noqa: E501

        :return: The bits_per_pixel.  # noqa: E501
        :rtype: int
        """
        return self._bits_per_pixel

    @bits_per_pixel.setter
    def bits_per_pixel(self, bits_per_pixel):
        """
        Sets the bits_per_pixel.

        Returns detected bits per pixel if applicable to the current document format  # noqa: E501

        :param bits_per_pixel: The bits_per_pixel.  # noqa: E501
        :type: int
        """
        if bits_per_pixel is None:
            raise ValueError("Invalid value for `bits_per_pixel`, must not be `None`")  # noqa: E501
        self._bits_per_pixel = bits_per_pixel
    
    @property
    def title(self):
        """
        Gets the title.  # noqa: E501

        Returns document title width if applicable to the current document format  # noqa: E501

        :return: The title.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title.

        Returns document title width if applicable to the current document format  # noqa: E501

        :param title: The title.  # noqa: E501
        :type: str
        """
        self._title = title
    
    @property
    def author(self):
        """
        Gets the author.  # noqa: E501

        Returns detected document author if applicable to the current document format  # noqa: E501

        :return: The author.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author.

        Returns detected document author if applicable to the current document format  # noqa: E501

        :param author: The author.  # noqa: E501
        :type: str
        """
        self._author = author
    
    @property
    def created_date(self):
        """
        Gets the created_date.  # noqa: E501

        Returns detected document creation date if it's applicable to the current document format  # noqa: E501

        :return: The created_date.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date.

        Returns detected document creation date if it's applicable to the current document format  # noqa: E501

        :param created_date: The created_date.  # noqa: E501
        :type: datetime
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501
        self._created_date = created_date
    
    @property
    def modified_date(self):
        """
        Gets the modified_date.  # noqa: E501

        Returns detected document modification date if applicable to the current document format  # noqa: E501

        :return: The modified_date.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date.

        Returns detected document modification date if applicable to the current document format  # noqa: E501

        :param modified_date: The modified_date.  # noqa: E501
        :type: datetime
        """
        if modified_date is None:
            raise ValueError("Invalid value for `modified_date`, must not be `None`")  # noqa: E501
        self._modified_date = modified_date
    
    @property
    def layers(self):
        """
        Gets the layers.  # noqa: E501

        Returns list of layer names if applicable to the current document format  # noqa: E501

        :return: The layers.  # noqa: E501
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """
        Sets the layers.

        Returns list of layer names if applicable to the current document format  # noqa: E501

        :param layers: The layers.  # noqa: E501
        :type: list[str]
        """
        self._layers = layers
    
    @property
    def is_password_protected(self):
        """
        Gets the is_password_protected.  # noqa: E501

        Is document password protected  # noqa: E501

        :return: The is_password_protected.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_protected

    @is_password_protected.setter
    def is_password_protected(self, is_password_protected):
        """
        Sets the is_password_protected.

        Is document password protected  # noqa: E501

        :param is_password_protected: The is_password_protected.  # noqa: E501
        :type: bool
        """
        if is_password_protected is None:
            raise ValueError("Invalid value for `is_password_protected`, must not be `None`")  # noqa: E501
        self._is_password_protected = is_password_protected

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
        if not isinstance(other, DocumentMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
