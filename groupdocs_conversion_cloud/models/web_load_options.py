# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WebLoadOptions.py">
#   Copyright (c) 2003-2024 Aspose Pty Ltd
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

class WebLoadOptions(LoadOptions):
    """
    Html document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_numbering': 'bool',
        'encoding': 'str',
        'use_pdf': 'bool',
        'rendering_mode': 'str'
    }

    attribute_map = {
        'page_numbering': 'PageNumbering',
        'encoding': 'Encoding',
        'use_pdf': 'UsePdf',
        'rendering_mode': 'RenderingMode'
    }

    def __init__(self, page_numbering=None, encoding=None, use_pdf=None, rendering_mode=None, **kwargs):  # noqa: E501
        """Initializes new instance of WebLoadOptions"""  # noqa: E501

        self._page_numbering = None
        self._encoding = None
        self._use_pdf = None
        self._rendering_mode = None

        if page_numbering is not None:
            self.page_numbering = page_numbering
        if encoding is not None:
            self.encoding = encoding
        if use_pdf is not None:
            self.use_pdf = use_pdf
        if rendering_mode is not None:
            self.rendering_mode = rendering_mode

        base = super(WebLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def page_numbering(self):
        """
        Gets the page_numbering.  # noqa: E501

        Enable or disable generation of page numbering in converted document. Default: false  # noqa: E501

        :return: The page_numbering.  # noqa: E501
        :rtype: bool
        """
        return self._page_numbering

    @page_numbering.setter
    def page_numbering(self, page_numbering):
        """
        Sets the page_numbering.

        Enable or disable generation of page numbering in converted document. Default: false  # noqa: E501

        :param page_numbering: The page_numbering.  # noqa: E501
        :type: bool
        """
        if page_numbering is None:
            raise ValueError("Invalid value for `page_numbering`, must not be `None`")  # noqa: E501
        self._page_numbering = page_numbering
    
    @property
    def encoding(self):
        """
        Gets the encoding.  # noqa: E501

        Get or sets the encoding to be used when loading the web document. If the property is null the encoding will be determined from document character set attribute  # noqa: E501

        :return: The encoding.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding.

        Get or sets the encoding to be used when loading the web document. If the property is null the encoding will be determined from document character set attribute  # noqa: E501

        :param encoding: The encoding.  # noqa: E501
        :type: str
        """
        self._encoding = encoding
    
    @property
    def use_pdf(self):
        """
        Gets the use_pdf.  # noqa: E501

        Use pdf for the conversion. Default: false  # noqa: E501

        :return: The use_pdf.  # noqa: E501
        :rtype: bool
        """
        return self._use_pdf

    @use_pdf.setter
    def use_pdf(self, use_pdf):
        """
        Sets the use_pdf.

        Use pdf for the conversion. Default: false  # noqa: E501

        :param use_pdf: The use_pdf.  # noqa: E501
        :type: bool
        """
        if use_pdf is None:
            raise ValueError("Invalid value for `use_pdf`, must not be `None`")  # noqa: E501
        self._use_pdf = use_pdf
    
    @property
    def rendering_mode(self):
        """
        Gets the rendering_mode.  # noqa: E501

        Controls how HTML content is rendered. Default: AbsolutePositioning  # noqa: E501

        :return: The rendering_mode.  # noqa: E501
        :rtype: str
        """
        return self._rendering_mode

    @rendering_mode.setter
    def rendering_mode(self, rendering_mode):
        """
        Sets the rendering_mode.

        Controls how HTML content is rendered. Default: AbsolutePositioning  # noqa: E501

        :param rendering_mode: The rendering_mode.  # noqa: E501
        :type: str
        """
        if rendering_mode is None:
            raise ValueError("Invalid value for `rendering_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Flow", "AbsolutePositioning"]  # noqa: E501
        if not rendering_mode.isdigit():	
            if rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(rendering_mode, allowed_values))
            self._rendering_mode = rendering_mode
        else:
            self._rendering_mode = allowed_values[int(rendering_mode) if six.PY3 else long(rendering_mode)]

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
        if not isinstance(other, WebLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
