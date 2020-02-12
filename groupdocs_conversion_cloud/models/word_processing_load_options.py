# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WordProcessingLoadOptions.py">
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

class WordProcessingLoadOptions(LoadOptions):
    """
    WordProcessing document load options
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
        'auto_font_substitution': 'bool',
        'font_substitutes': 'dict(str, str)',
        'password': 'str',
        'hide_word_tracked_changes': 'bool',
        'hide_comments': 'bool',
        'bookmarks_outline_level': 'int',
        'headings_outline_levels': 'int',
        'expanded_outline_levels': 'int'
    }

    attribute_map = {
        'default_font': 'DefaultFont',
        'auto_font_substitution': 'AutoFontSubstitution',
        'font_substitutes': 'FontSubstitutes',
        'password': 'Password',
        'hide_word_tracked_changes': 'HideWordTrackedChanges',
        'hide_comments': 'HideComments',
        'bookmarks_outline_level': 'BookmarksOutlineLevel',
        'headings_outline_levels': 'HeadingsOutlineLevels',
        'expanded_outline_levels': 'ExpandedOutlineLevels'
    }

    def __init__(self, default_font=None, auto_font_substitution=None, font_substitutes=None, password=None, hide_word_tracked_changes=None, hide_comments=None, bookmarks_outline_level=None, headings_outline_levels=None, expanded_outline_levels=None, **kwargs):  # noqa: E501
        """Initializes new instance of WordProcessingLoadOptions"""  # noqa: E501

        self._default_font = None
        self._auto_font_substitution = None
        self._font_substitutes = None
        self._password = None
        self._hide_word_tracked_changes = None
        self._hide_comments = None
        self._bookmarks_outline_level = None
        self._headings_outline_levels = None
        self._expanded_outline_levels = None

        if default_font is not None:
            self.default_font = default_font
        if auto_font_substitution is not None:
            self.auto_font_substitution = auto_font_substitution
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes
        if password is not None:
            self.password = password
        if hide_word_tracked_changes is not None:
            self.hide_word_tracked_changes = hide_word_tracked_changes
        if hide_comments is not None:
            self.hide_comments = hide_comments
        if bookmarks_outline_level is not None:
            self.bookmarks_outline_level = bookmarks_outline_level
        if headings_outline_levels is not None:
            self.headings_outline_levels = headings_outline_levels
        if expanded_outline_levels is not None:
            self.expanded_outline_levels = expanded_outline_levels

        base = super(WordProcessingLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for Words document. The following font will be used if a font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for Words document. The following font will be used if a font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
    @property
    def auto_font_substitution(self):
        """
        Gets the auto_font_substitution.  # noqa: E501

        If AutoFontSubstitution is disabled, GroupDocs.Conversion uses the DefaultFont for the substitution of missing fonts. If AutoFontSubstitution is enabled, GroupDocs.Conversion evaluates all the related fields in FontInfo (Panose, Sig etc) for the missing font and finds the closest match among the available font sources. Note that font substitution mechanism will override the DefaultFont in cases when FontInfo for the missing font is available in the document. The default value is True.  # noqa: E501

        :return: The auto_font_substitution.  # noqa: E501
        :rtype: bool
        """
        return self._auto_font_substitution

    @auto_font_substitution.setter
    def auto_font_substitution(self, auto_font_substitution):
        """
        Sets the auto_font_substitution.

        If AutoFontSubstitution is disabled, GroupDocs.Conversion uses the DefaultFont for the substitution of missing fonts. If AutoFontSubstitution is enabled, GroupDocs.Conversion evaluates all the related fields in FontInfo (Panose, Sig etc) for the missing font and finds the closest match among the available font sources. Note that font substitution mechanism will override the DefaultFont in cases when FontInfo for the missing font is available in the document. The default value is True.  # noqa: E501

        :param auto_font_substitution: The auto_font_substitution.  # noqa: E501
        :type: bool
        """
        if auto_font_substitution is None:
            raise ValueError("Invalid value for `auto_font_substitution`, must not be `None`")  # noqa: E501
        self._auto_font_substitution = auto_font_substitution
    
    @property
    def font_substitutes(self):
        """
        Gets the font_substitutes.  # noqa: E501

        Substitute specific fonts when converting Words document.  # noqa: E501

        :return: The font_substitutes.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._font_substitutes

    @font_substitutes.setter
    def font_substitutes(self, font_substitutes):
        """
        Sets the font_substitutes.

        Substitute specific fonts when converting Words document.  # noqa: E501

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
    def hide_word_tracked_changes(self):
        """
        Gets the hide_word_tracked_changes.  # noqa: E501

        Hide markup and track changes for Word documents  # noqa: E501

        :return: The hide_word_tracked_changes.  # noqa: E501
        :rtype: bool
        """
        return self._hide_word_tracked_changes

    @hide_word_tracked_changes.setter
    def hide_word_tracked_changes(self, hide_word_tracked_changes):
        """
        Sets the hide_word_tracked_changes.

        Hide markup and track changes for Word documents  # noqa: E501

        :param hide_word_tracked_changes: The hide_word_tracked_changes.  # noqa: E501
        :type: bool
        """
        if hide_word_tracked_changes is None:
            raise ValueError("Invalid value for `hide_word_tracked_changes`, must not be `None`")  # noqa: E501
        self._hide_word_tracked_changes = hide_word_tracked_changes
    
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
    def bookmarks_outline_level(self):
        """
        Gets the bookmarks_outline_level.  # noqa: E501

        Specifies the default level in the document outline at which to display Word bookmarks. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :return: The bookmarks_outline_level.  # noqa: E501
        :rtype: int
        """
        return self._bookmarks_outline_level

    @bookmarks_outline_level.setter
    def bookmarks_outline_level(self, bookmarks_outline_level):
        """
        Sets the bookmarks_outline_level.

        Specifies the default level in the document outline at which to display Word bookmarks. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :param bookmarks_outline_level: The bookmarks_outline_level.  # noqa: E501
        :type: int
        """
        if bookmarks_outline_level is None:
            raise ValueError("Invalid value for `bookmarks_outline_level`, must not be `None`")  # noqa: E501
        self._bookmarks_outline_level = bookmarks_outline_level
    
    @property
    def headings_outline_levels(self):
        """
        Gets the headings_outline_levels.  # noqa: E501

        Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the document outline. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :return: The headings_outline_levels.  # noqa: E501
        :rtype: int
        """
        return self._headings_outline_levels

    @headings_outline_levels.setter
    def headings_outline_levels(self, headings_outline_levels):
        """
        Sets the headings_outline_levels.

        Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the document outline. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :param headings_outline_levels: The headings_outline_levels.  # noqa: E501
        :type: int
        """
        if headings_outline_levels is None:
            raise ValueError("Invalid value for `headings_outline_levels`, must not be `None`")  # noqa: E501
        self._headings_outline_levels = headings_outline_levels
    
    @property
    def expanded_outline_levels(self):
        """
        Gets the expanded_outline_levels.  # noqa: E501

        Specifies how many levels in the document outline to show expanded when the file is viewed. Default is 0. Valid range is 0 to 9. Note that this options will not work when saving to XPS.  # noqa: E501

        :return: The expanded_outline_levels.  # noqa: E501
        :rtype: int
        """
        return self._expanded_outline_levels

    @expanded_outline_levels.setter
    def expanded_outline_levels(self, expanded_outline_levels):
        """
        Sets the expanded_outline_levels.

        Specifies how many levels in the document outline to show expanded when the file is viewed. Default is 0. Valid range is 0 to 9. Note that this options will not work when saving to XPS.  # noqa: E501

        :param expanded_outline_levels: The expanded_outline_levels.  # noqa: E501
        :type: int
        """
        if expanded_outline_levels is None:
            raise ValueError("Invalid value for `expanded_outline_levels`, must not be `None`")  # noqa: E501
        self._expanded_outline_levels = expanded_outline_levels

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
        if not isinstance(other, WordProcessingLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
