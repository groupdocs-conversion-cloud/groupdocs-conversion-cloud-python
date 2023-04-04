# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WordProcessingConvertOptions.py">
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

class WordProcessingConvertOptions(ConvertOptions):
    """
    Options for to word processing conversion
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'width': 'int',
        'height': 'int',
        'dpi': 'float',
        'password': 'str',
        'zoom': 'int',
        'pdf_recognition_mode': 'str',
        'page_size': 'str',
        'page_orientation': 'str'
    }

    attribute_map = {
        'width': 'Width',
        'height': 'Height',
        'dpi': 'Dpi',
        'password': 'Password',
        'zoom': 'Zoom',
        'pdf_recognition_mode': 'PdfRecognitionMode',
        'page_size': 'PageSize',
        'page_orientation': 'PageOrientation'
    }

    def __init__(self, width=None, height=None, dpi=None, password=None, zoom=None, pdf_recognition_mode=None, page_size=None, page_orientation=None, **kwargs):  # noqa: E501
        """Initializes new instance of WordProcessingConvertOptions"""  # noqa: E501

        self._width = None
        self._height = None
        self._dpi = None
        self._password = None
        self._zoom = None
        self._pdf_recognition_mode = None
        self._page_size = None
        self._page_orientation = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if dpi is not None:
            self.dpi = dpi
        if password is not None:
            self.password = password
        if zoom is not None:
            self.zoom = zoom
        if pdf_recognition_mode is not None:
            self.pdf_recognition_mode = pdf_recognition_mode
        if page_size is not None:
            self.page_size = page_size
        if page_orientation is not None:
            self.page_orientation = page_orientation

        base = super(WordProcessingConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Desired page width after conversion  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Desired page width after conversion  # noqa: E501

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

        Desired page height after conversion  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Desired page height after conversion  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def dpi(self):
        """
        Gets the dpi.  # noqa: E501

        Desired page DPI after conversion. The default resolution is: 96dpi  # noqa: E501

        :return: The dpi.  # noqa: E501
        :rtype: float
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """
        Sets the dpi.

        Desired page DPI after conversion. The default resolution is: 96dpi  # noqa: E501

        :param dpi: The dpi.  # noqa: E501
        :type: float
        """
        if dpi is None:
            raise ValueError("Invalid value for `dpi`, must not be `None`")  # noqa: E501
        self._dpi = dpi
    
    @property
    def password(self):
        """
        Gets the password.  # noqa: E501

        Set this property if you want to protect the converted document with a password  # noqa: E501

        :return: The password.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password.

        Set this property if you want to protect the converted document with a password  # noqa: E501

        :param password: The password.  # noqa: E501
        :type: str
        """
        self._password = password
    
    @property
    def zoom(self):
        """
        Gets the zoom.  # noqa: E501

        Specifies the zoom level in percentage. Default is 100. Default zoom is supported till Microsoft Word 2010. Starting from Microsoft Word 2013 default zoom is no longer set to document, instead it appears to use the zoom factor of the last document that was opened.  # noqa: E501

        :return: The zoom.  # noqa: E501
        :rtype: int
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom.

        Specifies the zoom level in percentage. Default is 100. Default zoom is supported till Microsoft Word 2010. Starting from Microsoft Word 2013 default zoom is no longer set to document, instead it appears to use the zoom factor of the last document that was opened.  # noqa: E501

        :param zoom: The zoom.  # noqa: E501
        :type: int
        """
        if zoom is None:
            raise ValueError("Invalid value for `zoom`, must not be `None`")  # noqa: E501
        self._zoom = zoom
    
    @property
    def pdf_recognition_mode(self):
        """
        Gets the pdf_recognition_mode.  # noqa: E501

        Recognition mode when converting from pdf  # noqa: E501

        :return: The pdf_recognition_mode.  # noqa: E501
        :rtype: str
        """
        return self._pdf_recognition_mode

    @pdf_recognition_mode.setter
    def pdf_recognition_mode(self, pdf_recognition_mode):
        """
        Sets the pdf_recognition_mode.

        Recognition mode when converting from pdf  # noqa: E501

        :param pdf_recognition_mode: The pdf_recognition_mode.  # noqa: E501
        :type: str
        """
        if pdf_recognition_mode is None:
            raise ValueError("Invalid value for `pdf_recognition_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Textbox", "Flow"]  # noqa: E501
        if not pdf_recognition_mode.isdigit():	
            if pdf_recognition_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `pdf_recognition_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(pdf_recognition_mode, allowed_values))
            self._pdf_recognition_mode = pdf_recognition_mode
        else:
            self._pdf_recognition_mode = allowed_values[int(pdf_recognition_mode) if six.PY3 else long(pdf_recognition_mode)]
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        Page size  # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        Page size  # noqa: E501

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
        if not isinstance(other, WordProcessingConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
