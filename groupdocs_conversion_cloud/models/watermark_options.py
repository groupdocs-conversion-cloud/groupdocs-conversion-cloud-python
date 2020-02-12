# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WatermarkOptions.py">
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

class WatermarkOptions(object):
    """
    Options for settings watermark to the converted document
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str',
        'font_name': 'str',
        'font_size': 'int',
        'color': 'str',
        'width': 'int',
        'height': 'int',
        'top': 'int',
        'left': 'int',
        'rotation_angle': 'int',
        'transparency': 'float',
        'background': 'bool',
        'image': 'str'
    }

    attribute_map = {
        'text': 'Text',
        'font_name': 'FontName',
        'font_size': 'FontSize',
        'color': 'Color',
        'width': 'Width',
        'height': 'Height',
        'top': 'Top',
        'left': 'Left',
        'rotation_angle': 'RotationAngle',
        'transparency': 'Transparency',
        'background': 'Background',
        'image': 'Image'
    }

    def __init__(self, text=None, font_name=None, font_size=None, color=None, width=None, height=None, top=None, left=None, rotation_angle=None, transparency=None, background=None, image=None, **kwargs):  # noqa: E501
        """Initializes new instance of WatermarkOptions"""  # noqa: E501

        self._text = None
        self._font_name = None
        self._font_size = None
        self._color = None
        self._width = None
        self._height = None
        self._top = None
        self._left = None
        self._rotation_angle = None
        self._transparency = None
        self._background = None
        self._image = None

        if text is not None:
            self.text = text
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if color is not None:
            self.color = color
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if top is not None:
            self.top = top
        if left is not None:
            self.left = left
        if rotation_angle is not None:
            self.rotation_angle = rotation_angle
        if transparency is not None:
            self.transparency = transparency
        if background is not None:
            self.background = background
        if image is not None:
            self.image = image
    
    @property
    def text(self):
        """
        Gets the text.  # noqa: E501

        Watermark text  # noqa: E501

        :return: The text.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text.

        Watermark text  # noqa: E501

        :param text: The text.  # noqa: E501
        :type: str
        """
        self._text = text
    
    @property
    def font_name(self):
        """
        Gets the font_name.  # noqa: E501

        Watermark font name if text watermark is applied  # noqa: E501

        :return: The font_name.  # noqa: E501
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """
        Sets the font_name.

        Watermark font name if text watermark is applied  # noqa: E501

        :param font_name: The font_name.  # noqa: E501
        :type: str
        """
        self._font_name = font_name
    
    @property
    def font_size(self):
        """
        Gets the font_size.  # noqa: E501

        Watermark font name if text watermark is applied  # noqa: E501

        :return: The font_size.  # noqa: E501
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """
        Sets the font_size.

        Watermark font name if text watermark is applied  # noqa: E501

        :param font_size: The font_size.  # noqa: E501
        :type: int
        """
        if font_size is None:
            raise ValueError("Invalid value for `font_size`, must not be `None`")  # noqa: E501
        self._font_size = font_size
    
    @property
    def color(self):
        """
        Gets the color.  # noqa: E501

        Watermark font color if text watermark is applied  # noqa: E501

        :return: The color.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color.

        Watermark font color if text watermark is applied  # noqa: E501

        :param color: The color.  # noqa: E501
        :type: str
        """
        self._color = color
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Watermark width  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Watermark width  # noqa: E501

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

        Watermark height  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Watermark height  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def top(self):
        """
        Gets the top.  # noqa: E501

        Watermark top position  # noqa: E501

        :return: The top.  # noqa: E501
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        Sets the top.

        Watermark top position  # noqa: E501

        :param top: The top.  # noqa: E501
        :type: int
        """
        if top is None:
            raise ValueError("Invalid value for `top`, must not be `None`")  # noqa: E501
        self._top = top
    
    @property
    def left(self):
        """
        Gets the left.  # noqa: E501

        Watermark left position  # noqa: E501

        :return: The left.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Sets the left.

        Watermark left position  # noqa: E501

        :param left: The left.  # noqa: E501
        :type: int
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501
        self._left = left
    
    @property
    def rotation_angle(self):
        """
        Gets the rotation_angle.  # noqa: E501

        Watermark rotation angle  # noqa: E501

        :return: The rotation_angle.  # noqa: E501
        :rtype: int
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """
        Sets the rotation_angle.

        Watermark rotation angle  # noqa: E501

        :param rotation_angle: The rotation_angle.  # noqa: E501
        :type: int
        """
        if rotation_angle is None:
            raise ValueError("Invalid value for `rotation_angle`, must not be `None`")  # noqa: E501
        self._rotation_angle = rotation_angle
    
    @property
    def transparency(self):
        """
        Gets the transparency.  # noqa: E501

        Watermark transparency. Value between 0 and 1. Value 0 is fully visible, value 1 is invisible.  # noqa: E501

        :return: The transparency.  # noqa: E501
        :rtype: float
        """
        return self._transparency

    @transparency.setter
    def transparency(self, transparency):
        """
        Sets the transparency.

        Watermark transparency. Value between 0 and 1. Value 0 is fully visible, value 1 is invisible.  # noqa: E501

        :param transparency: The transparency.  # noqa: E501
        :type: float
        """
        if transparency is None:
            raise ValueError("Invalid value for `transparency`, must not be `None`")  # noqa: E501
        self._transparency = transparency
    
    @property
    def background(self):
        """
        Gets the background.  # noqa: E501

        Indicates that the watermark is stamped as background. If the value is true, the watermark is layed at the bottom. By default is false and the watermark is layed on top.  # noqa: E501

        :return: The background.  # noqa: E501
        :rtype: bool
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background.

        Indicates that the watermark is stamped as background. If the value is true, the watermark is layed at the bottom. By default is false and the watermark is layed on top.  # noqa: E501

        :param background: The background.  # noqa: E501
        :type: bool
        """
        if background is None:
            raise ValueError("Invalid value for `background`, must not be `None`")  # noqa: E501
        self._background = background
    
    @property
    def image(self):
        """
        Gets the image.  # noqa: E501

        Image watermark  # noqa: E501

        :return: The image.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image.

        Image watermark  # noqa: E501

        :param image: The image.  # noqa: E501
        :type: str
        """
        self._image = image

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
        if not isinstance(other, WatermarkOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
