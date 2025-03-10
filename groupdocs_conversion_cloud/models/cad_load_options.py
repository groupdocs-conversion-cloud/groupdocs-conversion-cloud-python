# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="CadLoadOptions.py">
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

class CadLoadOptions(LoadOptions):
    """
    Options for loading CAD documents
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'layout_names': 'list[str]',
        'background_color': 'str',
        'draw_type': 'str'
    }

    attribute_map = {
        'layout_names': 'LayoutNames',
        'background_color': 'BackgroundColor',
        'draw_type': 'DrawType'
    }

    def __init__(self, layout_names=None, background_color=None, draw_type=None, **kwargs):  # noqa: E501
        """Initializes new instance of CadLoadOptions"""  # noqa: E501

        self._layout_names = None
        self._background_color = None
        self._draw_type = None

        if layout_names is not None:
            self.layout_names = layout_names
        if background_color is not None:
            self.background_color = background_color
        if draw_type is not None:
            self.draw_type = draw_type

        base = super(CadLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def layout_names(self):
        """
        Gets the layout_names.  # noqa: E501

        Render specific CAD layouts  # noqa: E501

        :return: The layout_names.  # noqa: E501
        :rtype: list[str]
        """
        return self._layout_names

    @layout_names.setter
    def layout_names(self, layout_names):
        """
        Sets the layout_names.

        Render specific CAD layouts  # noqa: E501

        :param layout_names: The layout_names.  # noqa: E501
        :type: list[str]
        """
        self._layout_names = layout_names
    
    @property
    def background_color(self):
        """
        Gets the background_color.  # noqa: E501

        Gets or sets a background color.  # noqa: E501

        :return: The background_color.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color.

        Gets or sets a background color.  # noqa: E501

        :param background_color: The background_color.  # noqa: E501
        :type: str
        """
        self._background_color = background_color
    
    @property
    def draw_type(self):
        """
        Gets the draw_type.  # noqa: E501

        Gets or sets type of drawing.  # noqa: E501

        :return: The draw_type.  # noqa: E501
        :rtype: str
        """
        return self._draw_type

    @draw_type.setter
    def draw_type(self, draw_type):
        """
        Sets the draw_type.

        Gets or sets type of drawing.  # noqa: E501

        :param draw_type: The draw_type.  # noqa: E501
        :type: str
        """
        if draw_type is None:
            raise ValueError("Invalid value for `draw_type`, must not be `None`")  # noqa: E501
        allowed_values = ["UseDrawColor", "UseObjectColor"]  # noqa: E501
        if not draw_type.isdigit():	
            if draw_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `draw_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(draw_type, allowed_values))
            self._draw_type = draw_type
        else:
            self._draw_type = allowed_values[int(draw_type) if six.PY3 else long(draw_type)]

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
        if not isinstance(other, CadLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
