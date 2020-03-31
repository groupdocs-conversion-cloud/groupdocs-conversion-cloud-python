# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="HtmlConvertOptions.py">
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

class HtmlConvertOptions(ConvertOptions):
    """
    Options for to Html conversion
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'use_pdf': 'bool',
        'fixed_layout': 'bool',
        'fixed_layout_show_borders': 'bool',
        'zoom': 'int',
        'watermark_options': 'WatermarkOptions'
    }

    attribute_map = {
        'use_pdf': 'UsePdf',
        'fixed_layout': 'FixedLayout',
        'fixed_layout_show_borders': 'FixedLayoutShowBorders',
        'zoom': 'Zoom',
        'watermark_options': 'WatermarkOptions'
    }

    def __init__(self, use_pdf=None, fixed_layout=None, fixed_layout_show_borders=None, zoom=None, watermark_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of HtmlConvertOptions"""  # noqa: E501

        self._use_pdf = None
        self._fixed_layout = None
        self._fixed_layout_show_borders = None
        self._zoom = None
        self._watermark_options = None

        if use_pdf is not None:
            self.use_pdf = use_pdf
        if fixed_layout is not None:
            self.fixed_layout = fixed_layout
        if fixed_layout_show_borders is not None:
            self.fixed_layout_show_borders = fixed_layout_show_borders
        if zoom is not None:
            self.zoom = zoom
        if watermark_options is not None:
            self.watermark_options = watermark_options

        base = super(HtmlConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
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
    def fixed_layout(self):
        """
        Gets the fixed_layout.  # noqa: E501

        If true fixed layout will be used e.g. absolutely positioned html elements Default:  true  # noqa: E501

        :return: The fixed_layout.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_layout

    @fixed_layout.setter
    def fixed_layout(self, fixed_layout):
        """
        Sets the fixed_layout.

        If true fixed layout will be used e.g. absolutely positioned html elements Default:  true  # noqa: E501

        :param fixed_layout: The fixed_layout.  # noqa: E501
        :type: bool
        """
        if fixed_layout is None:
            raise ValueError("Invalid value for `fixed_layout`, must not be `None`")  # noqa: E501
        self._fixed_layout = fixed_layout
    
    @property
    def fixed_layout_show_borders(self):
        """
        Gets the fixed_layout_show_borders.  # noqa: E501

        Show page borders when converting to fixed layout. Default is True  # noqa: E501

        :return: The fixed_layout_show_borders.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_layout_show_borders

    @fixed_layout_show_borders.setter
    def fixed_layout_show_borders(self, fixed_layout_show_borders):
        """
        Sets the fixed_layout_show_borders.

        Show page borders when converting to fixed layout. Default is True  # noqa: E501

        :param fixed_layout_show_borders: The fixed_layout_show_borders.  # noqa: E501
        :type: bool
        """
        if fixed_layout_show_borders is None:
            raise ValueError("Invalid value for `fixed_layout_show_borders`, must not be `None`")  # noqa: E501
        self._fixed_layout_show_borders = fixed_layout_show_borders
    
    @property
    def zoom(self):
        """
        Gets the zoom.  # noqa: E501

        Specifies the zoom level in percentage. Default is 100.  # noqa: E501

        :return: The zoom.  # noqa: E501
        :rtype: int
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom.

        Specifies the zoom level in percentage. Default is 100.  # noqa: E501

        :param zoom: The zoom.  # noqa: E501
        :type: int
        """
        if zoom is None:
            raise ValueError("Invalid value for `zoom`, must not be `None`")  # noqa: E501
        self._zoom = zoom
    
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
        if not isinstance(other, HtmlConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
