# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PresentationLoadOptions.py">
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

from groupdocs_conversion_cloud.models import LoadOptions

class PresentationLoadOptions(LoadOptions):
    """
    Presentation document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_font': 'str',
        'font_substitutes': 'dict(str, str)',
        'password': 'str',
        'hide_comments': 'bool',
        'show_hidden_slides': 'bool'
    }

    attribute_map = {
        'default_font': 'DefaultFont',
        'font_substitutes': 'FontSubstitutes',
        'password': 'Password',
        'hide_comments': 'HideComments',
        'show_hidden_slides': 'ShowHiddenSlides'
    }

    def __init__(self, default_font=None, font_substitutes=None, password=None, hide_comments=None, show_hidden_slides=None, **kwargs):  # noqa: E501
        """Initializes new instance of PresentationLoadOptions"""  # noqa: E501

        self._default_font = None
        self._font_substitutes = None
        self._password = None
        self._hide_comments = None
        self._show_hidden_slides = None

        if default_font is not None:
            self.default_font = default_font
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes
        if password is not None:
            self.password = password
        if hide_comments is not None:
            self.hide_comments = hide_comments
        if show_hidden_slides is not None:
            self.show_hidden_slides = show_hidden_slides

        base = super(PresentationLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for rendering the presentation. The following font will be used if a presentation font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for rendering the presentation. The following font will be used if a presentation font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
    @property
    def font_substitutes(self):
        """
        Gets the font_substitutes.  # noqa: E501

        Substitute specific fonts when converting Slides document.  # noqa: E501

        :return: The font_substitutes.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._font_substitutes

    @font_substitutes.setter
    def font_substitutes(self, font_substitutes):
        """
        Sets the font_substitutes.

        Substitute specific fonts when converting Slides document.  # noqa: E501

        :param font_substitutes: The font_substitutes.  # noqa: E501
        :type: dict(str, str)
        """
        self._font_substitutes = font_substitutes
    
    @property
    def password(self):
        """
        Gets the password.  # noqa: E501

        Set password to unprotect protected document  # noqa: E501

        :return: The password.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password.

        Set password to unprotect protected document  # noqa: E501

        :param password: The password.  # noqa: E501
        :type: str
        """
        self._password = password
    
    @property
    def hide_comments(self):
        """
        Gets the hide_comments.  # noqa: E501

        Hide comments  # noqa: E501

        :return: The hide_comments.  # noqa: E501
        :rtype: bool
        """
        return self._hide_comments

    @hide_comments.setter
    def hide_comments(self, hide_comments):
        """
        Sets the hide_comments.

        Hide comments  # noqa: E501

        :param hide_comments: The hide_comments.  # noqa: E501
        :type: bool
        """
        if hide_comments is None:
            raise ValueError("Invalid value for `hide_comments`, must not be `None`")  # noqa: E501
        self._hide_comments = hide_comments
    
    @property
    def show_hidden_slides(self):
        """
        Gets the show_hidden_slides.  # noqa: E501

        Show hidden slides  # noqa: E501

        :return: The show_hidden_slides.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_slides

    @show_hidden_slides.setter
    def show_hidden_slides(self, show_hidden_slides):
        """
        Sets the show_hidden_slides.

        Show hidden slides  # noqa: E501

        :param show_hidden_slides: The show_hidden_slides.  # noqa: E501
        :type: bool
        """
        if show_hidden_slides is None:
            raise ValueError("Invalid value for `show_hidden_slides`, must not be `None`")  # noqa: E501
        self._show_hidden_slides = show_hidden_slides

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
        if not isinstance(other, PresentationLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
