# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PsdConvertOptions.py">
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

from groupdocs_conversion_cloud.models import ImageConvertOptions

class PsdConvertOptions(ImageConvertOptions):
    """
    Psd convert options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel_bits_count': 'int',
        'channels_count': 'int',
        'color_mode': 'str',
        'compression_method': 'str',
        'version': 'int'
    }

    attribute_map = {
        'channel_bits_count': 'ChannelBitsCount',
        'channels_count': 'ChannelsCount',
        'color_mode': 'ColorMode',
        'compression_method': 'CompressionMethod',
        'version': 'Version'
    }

    def __init__(self, channel_bits_count=None, channels_count=None, color_mode=None, compression_method=None, version=None, **kwargs):  # noqa: E501
        """Initializes new instance of PsdConvertOptions"""  # noqa: E501

        self._channel_bits_count = None
        self._channels_count = None
        self._color_mode = None
        self._compression_method = None
        self._version = None

        if channel_bits_count is not None:
            self.channel_bits_count = channel_bits_count
        if channels_count is not None:
            self.channels_count = channels_count
        if color_mode is not None:
            self.color_mode = color_mode
        if compression_method is not None:
            self.compression_method = compression_method
        if version is not None:
            self.version = version

        base = super(PsdConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def channel_bits_count(self):
        """
        Gets the channel_bits_count.  # noqa: E501

        Bits count per color channel  # noqa: E501

        :return: The channel_bits_count.  # noqa: E501
        :rtype: int
        """
        return self._channel_bits_count

    @channel_bits_count.setter
    def channel_bits_count(self, channel_bits_count):
        """
        Sets the channel_bits_count.

        Bits count per color channel  # noqa: E501

        :param channel_bits_count: The channel_bits_count.  # noqa: E501
        :type: int
        """
        if channel_bits_count is None:
            raise ValueError("Invalid value for `channel_bits_count`, must not be `None`")  # noqa: E501
        self._channel_bits_count = channel_bits_count
    
    @property
    def channels_count(self):
        """
        Gets the channels_count.  # noqa: E501

        Color channels count  # noqa: E501

        :return: The channels_count.  # noqa: E501
        :rtype: int
        """
        return self._channels_count

    @channels_count.setter
    def channels_count(self, channels_count):
        """
        Sets the channels_count.

        Color channels count  # noqa: E501

        :param channels_count: The channels_count.  # noqa: E501
        :type: int
        """
        if channels_count is None:
            raise ValueError("Invalid value for `channels_count`, must not be `None`")  # noqa: E501
        self._channels_count = channels_count
    
    @property
    def color_mode(self):
        """
        Gets the color_mode.  # noqa: E501

        Psd color mode  # noqa: E501

        :return: The color_mode.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """
        Sets the color_mode.

        Psd color mode  # noqa: E501

        :param color_mode: The color_mode.  # noqa: E501
        :type: str
        """
        if color_mode is None:
            raise ValueError("Invalid value for `color_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Bitmap", "Grayscale", "Indexed", "Rgb", "Cmyk", "Multichannel", "Duotone", "Lab"]  # noqa: E501
        if not color_mode.isdigit():	
            if color_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `color_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(color_mode, allowed_values))
            self._color_mode = color_mode
        else:
            self._color_mode = allowed_values[int(color_mode) if six.PY3 else long(color_mode)]
    
    @property
    def compression_method(self):
        """
        Gets the compression_method.  # noqa: E501

        Psd compression method  # noqa: E501

        :return: The compression_method.  # noqa: E501
        :rtype: str
        """
        return self._compression_method

    @compression_method.setter
    def compression_method(self, compression_method):
        """
        Sets the compression_method.

        Psd compression method  # noqa: E501

        :param compression_method: The compression_method.  # noqa: E501
        :type: str
        """
        if compression_method is None:
            raise ValueError("Invalid value for `compression_method`, must not be `None`")  # noqa: E501
        allowed_values = ["Raw", "Rle", "ZipWithoutPrediction", "ZipWithPrediction"]  # noqa: E501
        if not compression_method.isdigit():	
            if compression_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression_method` ({0}), must be one of {1}"  # noqa: E501
                    .format(compression_method, allowed_values))
            self._compression_method = compression_method
        else:
            self._compression_method = allowed_values[int(compression_method) if six.PY3 else long(compression_method)]
    
    @property
    def version(self):
        """
        Gets the version.  # noqa: E501

        Psd file version  # noqa: E501

        :return: The version.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version.

        Psd file version  # noqa: E501

        :param version: The version.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        self._version = version

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
        if not isinstance(other, PsdConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
