# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ImageConvertOptions.py">
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

class ImageConvertOptions(ConvertOptions):
    """
    Options for to Image conversion
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
        'horizontal_resolution': 'int',
        'vertical_resolution': 'int',
        'grayscale': 'bool',
        'rotate_angle': 'int',
        'use_pdf': 'bool',
        'watermark_options': 'WatermarkOptions',
        'brightness': 'int',
        'contrast': 'int',
        'gamma': 'float',
        'flip_mode': 'str'
    }

    attribute_map = {
        'width': 'Width',
        'height': 'Height',
        'horizontal_resolution': 'HorizontalResolution',
        'vertical_resolution': 'VerticalResolution',
        'grayscale': 'Grayscale',
        'rotate_angle': 'RotateAngle',
        'use_pdf': 'UsePdf',
        'watermark_options': 'WatermarkOptions',
        'brightness': 'Brightness',
        'contrast': 'Contrast',
        'gamma': 'Gamma',
        'flip_mode': 'FlipMode'
    }

    def __init__(self, width=None, height=None, horizontal_resolution=None, vertical_resolution=None, grayscale=None, rotate_angle=None, use_pdf=None, watermark_options=None, brightness=None, contrast=None, gamma=None, flip_mode=None, **kwargs):  # noqa: E501
        """Initializes new instance of ImageConvertOptions"""  # noqa: E501

        self._width = None
        self._height = None
        self._horizontal_resolution = None
        self._vertical_resolution = None
        self._grayscale = None
        self._rotate_angle = None
        self._use_pdf = None
        self._watermark_options = None
        self._brightness = None
        self._contrast = None
        self._gamma = None
        self._flip_mode = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if horizontal_resolution is not None:
            self.horizontal_resolution = horizontal_resolution
        if vertical_resolution is not None:
            self.vertical_resolution = vertical_resolution
        if grayscale is not None:
            self.grayscale = grayscale
        if rotate_angle is not None:
            self.rotate_angle = rotate_angle
        if use_pdf is not None:
            self.use_pdf = use_pdf
        if watermark_options is not None:
            self.watermark_options = watermark_options
        if brightness is not None:
            self.brightness = brightness
        if contrast is not None:
            self.contrast = contrast
        if gamma is not None:
            self.gamma = gamma
        if flip_mode is not None:
            self.flip_mode = flip_mode

        base = super(ImageConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Desired image width after conversion  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Desired image width after conversion  # noqa: E501

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

        Desired image height after conversion  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Desired image height after conversion  # noqa: E501

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

        Desired image horizontal resolution after conversion. The default resolution is the resolution of the input file or 96dpi  # noqa: E501

        :return: The horizontal_resolution.  # noqa: E501
        :rtype: int
        """
        return self._horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """
        Sets the horizontal_resolution.

        Desired image horizontal resolution after conversion. The default resolution is the resolution of the input file or 96dpi  # noqa: E501

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

        Desired image vertical resolution after conversion. The default resolution is the resolution of the input file or 96dpi  # noqa: E501

        :return: The vertical_resolution.  # noqa: E501
        :rtype: int
        """
        return self._vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """
        Sets the vertical_resolution.

        Desired image vertical resolution after conversion. The default resolution is the resolution of the input file or 96dpi  # noqa: E501

        :param vertical_resolution: The vertical_resolution.  # noqa: E501
        :type: int
        """
        if vertical_resolution is None:
            raise ValueError("Invalid value for `vertical_resolution`, must not be `None`")  # noqa: E501
        self._vertical_resolution = vertical_resolution
    
    @property
    def grayscale(self):
        """
        Gets the grayscale.  # noqa: E501

        Convert to grayscale image  # noqa: E501

        :return: The grayscale.  # noqa: E501
        :rtype: bool
        """
        return self._grayscale

    @grayscale.setter
    def grayscale(self, grayscale):
        """
        Sets the grayscale.

        Convert to grayscale image  # noqa: E501

        :param grayscale: The grayscale.  # noqa: E501
        :type: bool
        """
        if grayscale is None:
            raise ValueError("Invalid value for `grayscale`, must not be `None`")  # noqa: E501
        self._grayscale = grayscale
    
    @property
    def rotate_angle(self):
        """
        Gets the rotate_angle.  # noqa: E501

        Image rotation angle   # noqa: E501

        :return: The rotate_angle.  # noqa: E501
        :rtype: int
        """
        return self._rotate_angle

    @rotate_angle.setter
    def rotate_angle(self, rotate_angle):
        """
        Sets the rotate_angle.

        Image rotation angle   # noqa: E501

        :param rotate_angle: The rotate_angle.  # noqa: E501
        :type: int
        """
        if rotate_angle is None:
            raise ValueError("Invalid value for `rotate_angle`, must not be `None`")  # noqa: E501
        self._rotate_angle = rotate_angle
    
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
    
    @property
    def brightness(self):
        """
        Gets the brightness.  # noqa: E501

        Adjust image brightness  # noqa: E501

        :return: The brightness.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """
        Sets the brightness.

        Adjust image brightness  # noqa: E501

        :param brightness: The brightness.  # noqa: E501
        :type: int
        """
        if brightness is None:
            raise ValueError("Invalid value for `brightness`, must not be `None`")  # noqa: E501
        self._brightness = brightness
    
    @property
    def contrast(self):
        """
        Gets the contrast.  # noqa: E501

        Adjust image contrast  # noqa: E501

        :return: The contrast.  # noqa: E501
        :rtype: int
        """
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        """
        Sets the contrast.

        Adjust image contrast  # noqa: E501

        :param contrast: The contrast.  # noqa: E501
        :type: int
        """
        if contrast is None:
            raise ValueError("Invalid value for `contrast`, must not be `None`")  # noqa: E501
        self._contrast = contrast
    
    @property
    def gamma(self):
        """
        Gets the gamma.  # noqa: E501

        Adjust image gamma  # noqa: E501

        :return: The gamma.  # noqa: E501
        :rtype: float
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """
        Sets the gamma.

        Adjust image gamma  # noqa: E501

        :param gamma: The gamma.  # noqa: E501
        :type: float
        """
        if gamma is None:
            raise ValueError("Invalid value for `gamma`, must not be `None`")  # noqa: E501
        self._gamma = gamma
    
    @property
    def flip_mode(self):
        """
        Gets the flip_mode.  # noqa: E501

        Image flip mode  # noqa: E501

        :return: The flip_mode.  # noqa: E501
        :rtype: str
        """
        return self._flip_mode

    @flip_mode.setter
    def flip_mode(self, flip_mode):
        """
        Sets the flip_mode.

        Image flip mode  # noqa: E501

        :param flip_mode: The flip_mode.  # noqa: E501
        :type: str
        """
        if flip_mode is None:
            raise ValueError("Invalid value for `flip_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "FlipX", "FlipY", "FlipXY"]  # noqa: E501
        if not flip_mode.isdigit():	
            if flip_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `flip_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(flip_mode, allowed_values))
            self._flip_mode = flip_mode
        else:
            self._flip_mode = allowed_values[int(flip_mode) if six.PY3 else long(flip_mode)]

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
        if not isinstance(other, ImageConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
