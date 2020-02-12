# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="SpreadsheetLoadOptions.py">
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

class SpreadsheetLoadOptions(LoadOptions):
    """
    Spreadsheet document load options
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
        'show_grid_lines': 'bool',
        'show_hidden_sheets': 'bool',
        'one_page_per_sheet': 'bool',
        'convert_range': 'str',
        'skip_empty_rows_and_columns': 'bool',
        'password': 'str',
        'hide_comments': 'bool'
    }

    attribute_map = {
        'default_font': 'DefaultFont',
        'font_substitutes': 'FontSubstitutes',
        'show_grid_lines': 'ShowGridLines',
        'show_hidden_sheets': 'ShowHiddenSheets',
        'one_page_per_sheet': 'OnePagePerSheet',
        'convert_range': 'ConvertRange',
        'skip_empty_rows_and_columns': 'SkipEmptyRowsAndColumns',
        'password': 'Password',
        'hide_comments': 'HideComments'
    }

    def __init__(self, default_font=None, font_substitutes=None, show_grid_lines=None, show_hidden_sheets=None, one_page_per_sheet=None, convert_range=None, skip_empty_rows_and_columns=None, password=None, hide_comments=None, **kwargs):  # noqa: E501
        """Initializes new instance of SpreadsheetLoadOptions"""  # noqa: E501

        self._default_font = None
        self._font_substitutes = None
        self._show_grid_lines = None
        self._show_hidden_sheets = None
        self._one_page_per_sheet = None
        self._convert_range = None
        self._skip_empty_rows_and_columns = None
        self._password = None
        self._hide_comments = None

        if default_font is not None:
            self.default_font = default_font
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes
        if show_grid_lines is not None:
            self.show_grid_lines = show_grid_lines
        if show_hidden_sheets is not None:
            self.show_hidden_sheets = show_hidden_sheets
        if one_page_per_sheet is not None:
            self.one_page_per_sheet = one_page_per_sheet
        if convert_range is not None:
            self.convert_range = convert_range
        if skip_empty_rows_and_columns is not None:
            self.skip_empty_rows_and_columns = skip_empty_rows_and_columns
        if password is not None:
            self.password = password
        if hide_comments is not None:
            self.hide_comments = hide_comments

        base = super(SpreadsheetLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for Cells document. The following font will be used if a font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for Cells document. The following font will be used if a font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
    @property
    def font_substitutes(self):
        """
        Gets the font_substitutes.  # noqa: E501

        Substitute specific fonts when converting Cells document.  # noqa: E501

        :return: The font_substitutes.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._font_substitutes

    @font_substitutes.setter
    def font_substitutes(self, font_substitutes):
        """
        Sets the font_substitutes.

        Substitute specific fonts when converting Cells document.  # noqa: E501

        :param font_substitutes: The font_substitutes.  # noqa: E501
        :type: dict(str, str)
        """
        self._font_substitutes = font_substitutes
    
    @property
    def show_grid_lines(self):
        """
        Gets the show_grid_lines.  # noqa: E501

        Show grid lines when converting Excel files  # noqa: E501

        :return: The show_grid_lines.  # noqa: E501
        :rtype: bool
        """
        return self._show_grid_lines

    @show_grid_lines.setter
    def show_grid_lines(self, show_grid_lines):
        """
        Sets the show_grid_lines.

        Show grid lines when converting Excel files  # noqa: E501

        :param show_grid_lines: The show_grid_lines.  # noqa: E501
        :type: bool
        """
        if show_grid_lines is None:
            raise ValueError("Invalid value for `show_grid_lines`, must not be `None`")  # noqa: E501
        self._show_grid_lines = show_grid_lines
    
    @property
    def show_hidden_sheets(self):
        """
        Gets the show_hidden_sheets.  # noqa: E501

        Show hidden sheets when converting Excel files  # noqa: E501

        :return: The show_hidden_sheets.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_sheets

    @show_hidden_sheets.setter
    def show_hidden_sheets(self, show_hidden_sheets):
        """
        Sets the show_hidden_sheets.

        Show hidden sheets when converting Excel files  # noqa: E501

        :param show_hidden_sheets: The show_hidden_sheets.  # noqa: E501
        :type: bool
        """
        if show_hidden_sheets is None:
            raise ValueError("Invalid value for `show_hidden_sheets`, must not be `None`")  # noqa: E501
        self._show_hidden_sheets = show_hidden_sheets
    
    @property
    def one_page_per_sheet(self):
        """
        Gets the one_page_per_sheet.  # noqa: E501

        If OnePagePerSheet is true the content of the sheet will be converted to one page in the PDF document. Default value is true.  # noqa: E501

        :return: The one_page_per_sheet.  # noqa: E501
        :rtype: bool
        """
        return self._one_page_per_sheet

    @one_page_per_sheet.setter
    def one_page_per_sheet(self, one_page_per_sheet):
        """
        Sets the one_page_per_sheet.

        If OnePagePerSheet is true the content of the sheet will be converted to one page in the PDF document. Default value is true.  # noqa: E501

        :param one_page_per_sheet: The one_page_per_sheet.  # noqa: E501
        :type: bool
        """
        if one_page_per_sheet is None:
            raise ValueError("Invalid value for `one_page_per_sheet`, must not be `None`")  # noqa: E501
        self._one_page_per_sheet = one_page_per_sheet
    
    @property
    def convert_range(self):
        """
        Gets the convert_range.  # noqa: E501

        Convert specific range when converting to other than cells format. Example: \"D1:F8\"  # noqa: E501

        :return: The convert_range.  # noqa: E501
        :rtype: str
        """
        return self._convert_range

    @convert_range.setter
    def convert_range(self, convert_range):
        """
        Sets the convert_range.

        Convert specific range when converting to other than cells format. Example: \"D1:F8\"  # noqa: E501

        :param convert_range: The convert_range.  # noqa: E501
        :type: str
        """
        self._convert_range = convert_range
    
    @property
    def skip_empty_rows_and_columns(self):
        """
        Gets the skip_empty_rows_and_columns.  # noqa: E501

        Skips empty rows and columns when converting. Default is True.  # noqa: E501

        :return: The skip_empty_rows_and_columns.  # noqa: E501
        :rtype: bool
        """
        return self._skip_empty_rows_and_columns

    @skip_empty_rows_and_columns.setter
    def skip_empty_rows_and_columns(self, skip_empty_rows_and_columns):
        """
        Sets the skip_empty_rows_and_columns.

        Skips empty rows and columns when converting. Default is True.  # noqa: E501

        :param skip_empty_rows_and_columns: The skip_empty_rows_and_columns.  # noqa: E501
        :type: bool
        """
        if skip_empty_rows_and_columns is None:
            raise ValueError("Invalid value for `skip_empty_rows_and_columns`, must not be `None`")  # noqa: E501
        self._skip_empty_rows_and_columns = skip_empty_rows_and_columns
    
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
        if not isinstance(other, SpreadsheetLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
