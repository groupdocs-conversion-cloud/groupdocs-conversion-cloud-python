# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="XpsConvertOptions.py">
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

from groupdocs_conversion_cloud.models import ConvertOptions

class XpsConvertOptions(ConvertOptions):
    """
    Xps convert options
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
        'margin_top': 'int',
        'margin_bottom': 'int',
        'margin_left': 'int',
        'margin_right': 'int',
        'use_pdf': 'bool',
        'watermark_options': 'WatermarkOptions'
    }

    attribute_map = {
        'width': 'Width',
        'height': 'Height',
        'dpi': 'Dpi',
        'password': 'Password',
        'margin_top': 'MarginTop',
        'margin_bottom': 'MarginBottom',
        'margin_left': 'MarginLeft',
        'margin_right': 'MarginRight',
        'use_pdf': 'UsePdf',
        'watermark_options': 'WatermarkOptions'
    }

    def __init__(self, width=None, height=None, dpi=None, password=None, margin_top=None, margin_bottom=None, margin_left=None, margin_right=None, use_pdf=None, watermark_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of XpsConvertOptions"""  # noqa: E501

        self._width = None
        self._height = None
        self._dpi = None
        self._password = None
        self._margin_top = None
        self._margin_bottom = None
        self._margin_left = None
        self._margin_right = None
        self._use_pdf = None
        self._watermark_options = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if dpi is not None:
            self.dpi = dpi
        if password is not None:
            self.password = password
        if margin_top is not None:
            self.margin_top = margin_top
        if margin_bottom is not None:
            self.margin_bottom = margin_bottom
        if margin_left is not None:
            self.margin_left = margin_left
        if margin_right is not None:
            self.margin_right = margin_right
        if use_pdf is not None:
            self.use_pdf = use_pdf
        if watermark_options is not None:
            self.watermark_options = watermark_options

        base = super(XpsConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Desired page width in pixels after conversion  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Desired page width in pixels after conversion  # noqa: E501

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

        Desired page height in pixels after conversion  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Desired page height in pixels after conversion  # noqa: E501

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
    def margin_top(self):
        """
        Gets the margin_top.  # noqa: E501

        Desired page top margin in pixels after conversion  # noqa: E501

        :return: The margin_top.  # noqa: E501
        :rtype: int
        """
        return self._margin_top

    @margin_top.setter
    def margin_top(self, margin_top):
        """
        Sets the margin_top.

        Desired page top margin in pixels after conversion  # noqa: E501

        :param margin_top: The margin_top.  # noqa: E501
        :type: int
        """
        if margin_top is None:
            raise ValueError("Invalid value for `margin_top`, must not be `None`")  # noqa: E501
        self._margin_top = margin_top
    
    @property
    def margin_bottom(self):
        """
        Gets the margin_bottom.  # noqa: E501

        Desired page bottom margin in pixels after conversion  # noqa: E501

        :return: The margin_bottom.  # noqa: E501
        :rtype: int
        """
        return self._margin_bottom

    @margin_bottom.setter
    def margin_bottom(self, margin_bottom):
        """
        Sets the margin_bottom.

        Desired page bottom margin in pixels after conversion  # noqa: E501

        :param margin_bottom: The margin_bottom.  # noqa: E501
        :type: int
        """
        if margin_bottom is None:
            raise ValueError("Invalid value for `margin_bottom`, must not be `None`")  # noqa: E501
        self._margin_bottom = margin_bottom
    
    @property
    def margin_left(self):
        """
        Gets the margin_left.  # noqa: E501

        Desired page left margin in pixels after conversion  # noqa: E501

        :return: The margin_left.  # noqa: E501
        :rtype: int
        """
        return self._margin_left

    @margin_left.setter
    def margin_left(self, margin_left):
        """
        Sets the margin_left.

        Desired page left margin in pixels after conversion  # noqa: E501

        :param margin_left: The margin_left.  # noqa: E501
        :type: int
        """
        if margin_left is None:
            raise ValueError("Invalid value for `margin_left`, must not be `None`")  # noqa: E501
        self._margin_left = margin_left
    
    @property
    def margin_right(self):
        """
        Gets the margin_right.  # noqa: E501

        Desired page right margin in pixels after conversion  # noqa: E501

        :return: The margin_right.  # noqa: E501
        :rtype: int
        """
        return self._margin_right

    @margin_right.setter
    def margin_right(self, margin_right):
        """
        Sets the margin_right.

        Desired page right margin in pixels after conversion  # noqa: E501

        :param margin_right: The margin_right.  # noqa: E501
        :type: int
        """
        if margin_right is None:
            raise ValueError("Invalid value for `margin_right`, must not be `None`")  # noqa: E501
        self._margin_right = margin_right
    
    @property
    def use_pdf(self):
        """
        Gets the use_pdf.  # noqa: E501

        If true, the input firstly is converted to PDF and after that to desired format  # noqa: E501

        :return: The use_pdf.  # noqa: E501
        :rtype: bool
        """
        return self._use_pdf

    @use_pdf.setter
    def use_pdf(self, use_pdf):
        """
        Sets the use_pdf.

        If true, the input firstly is converted to PDF and after that to desired format  # noqa: E501

        :param use_pdf: The use_pdf.  # noqa: E501
        :type: bool
        """
        if use_pdf is None:
            raise ValueError("Invalid value for `use_pdf`, must not be `None`")  # noqa: E501
        self._use_pdf = use_pdf
    
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
        if not isinstance(other, XpsConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
