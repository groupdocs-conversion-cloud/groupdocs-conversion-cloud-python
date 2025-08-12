# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WebLoadOptions.py">
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
        'base_path': 'str',
        'encoding': 'str',
        'skip_external_resources': 'bool',
        'use_pdf': 'bool',
        'rendering_mode': 'str',
        'zoom': 'int',
        'page_layout': 'str',
        'custom_css_style': 'str'
    }

    attribute_map = {
        'page_numbering': 'PageNumbering',
        'base_path': 'BasePath',
        'encoding': 'Encoding',
        'skip_external_resources': 'SkipExternalResources',
        'use_pdf': 'UsePdf',
        'rendering_mode': 'RenderingMode',
        'zoom': 'Zoom',
        'page_layout': 'PageLayout',
        'custom_css_style': 'CustomCssStyle'
    }

    def __init__(self, page_numbering=None, base_path=None, encoding=None, skip_external_resources=None, use_pdf=None, rendering_mode=None, zoom=None, page_layout=None, custom_css_style=None, **kwargs):  # noqa: E501
        """Initializes new instance of WebLoadOptions"""  # noqa: E501

        self._page_numbering = None
        self._base_path = None
        self._encoding = None
        self._skip_external_resources = None
        self._use_pdf = None
        self._rendering_mode = None
        self._zoom = None
        self._page_layout = None
        self._custom_css_style = None

        if page_numbering is not None:
            self.page_numbering = page_numbering
        if base_path is not None:
            self.base_path = base_path
        if encoding is not None:
            self.encoding = encoding
        if skip_external_resources is not None:
            self.skip_external_resources = skip_external_resources
        if use_pdf is not None:
            self.use_pdf = use_pdf
        if rendering_mode is not None:
            self.rendering_mode = rendering_mode
        if zoom is not None:
            self.zoom = zoom
        if page_layout is not None:
            self.page_layout = page_layout
        if custom_css_style is not None:
            self.custom_css_style = custom_css_style

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
    def base_path(self):
        """
        Gets the base_path.  # noqa: E501

        The base path/url for the html  # noqa: E501

        :return: The base_path.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """
        Sets the base_path.

        The base path/url for the html  # noqa: E501

        :param base_path: The base_path.  # noqa: E501
        :type: str
        """
        self._base_path = base_path
    
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
    def skip_external_resources(self):
        """
        Gets the skip_external_resources.  # noqa: E501

        If true all external resource will not be loading  # noqa: E501

        :return: The skip_external_resources.  # noqa: E501
        :rtype: bool
        """
        return self._skip_external_resources

    @skip_external_resources.setter
    def skip_external_resources(self, skip_external_resources):
        """
        Sets the skip_external_resources.

        If true all external resource will not be loading  # noqa: E501

        :param skip_external_resources: The skip_external_resources.  # noqa: E501
        :type: bool
        """
        if skip_external_resources is None:
            raise ValueError("Invalid value for `skip_external_resources`, must not be `None`")  # noqa: E501
        self._skip_external_resources = skip_external_resources
    
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
    
    @property
    def zoom(self):
        """
        Gets the zoom.  # noqa: E501


        :return: The zoom.  # noqa: E501
        :rtype: int
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom.


        :param zoom: The zoom.  # noqa: E501
        :type: int
        """
        if zoom is None:
            raise ValueError("Invalid value for `zoom`, must not be `None`")  # noqa: E501
        self._zoom = zoom
    
    @property
    def page_layout(self):
        """
        Gets the page_layout.  # noqa: E501

        Specifies the page layout options when loading web documents  # noqa: E501

        :return: The page_layout.  # noqa: E501
        :rtype: str
        """
        return self._page_layout

    @page_layout.setter
    def page_layout(self, page_layout):
        """
        Sets the page_layout.

        Specifies the page layout options when loading web documents  # noqa: E501

        :param page_layout: The page_layout.  # noqa: E501
        :type: str
        """
        if page_layout is None:
            raise ValueError("Invalid value for `page_layout`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "ScaleToPageWidth", "ScaleToPageHeight"]  # noqa: E501
        if not page_layout.isdigit():	
            if page_layout not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_layout` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_layout, allowed_values))
            self._page_layout = page_layout
        else:
            self._page_layout = allowed_values[int(page_layout) if six.PY3 else long(page_layout)]
    
    @property
    def custom_css_style(self):
        """
        Gets the custom_css_style.  # noqa: E501


        :return: The custom_css_style.  # noqa: E501
        :rtype: str
        """
        return self._custom_css_style

    @custom_css_style.setter
    def custom_css_style(self, custom_css_style):
        """
        Sets the custom_css_style.


        :param custom_css_style: The custom_css_style.  # noqa: E501
        :type: str
        """
        self._custom_css_style = custom_css_style

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
