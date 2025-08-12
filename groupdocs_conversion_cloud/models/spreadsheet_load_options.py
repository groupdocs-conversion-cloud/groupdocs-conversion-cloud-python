# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="SpreadsheetLoadOptions.py">
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
        'clear_custom_document_properties': 'bool',
        'clear_built_in_document_properties': 'bool',
        'rows_per_page': 'int',
        'columns_per_page': 'int',
        'auto_fit_rows': 'bool',
        'all_columns_in_one_page_per_sheet': 'bool',
        'culture_info': 'str',
        'check_excel_restriction': 'bool',
        'password': 'str',
        'skip_empty_rows_and_columns': 'bool',
        'convert_range': 'str',
        'optimize_pdf_size': 'bool',
        'one_page_per_sheet': 'bool',
        'show_hidden_sheets': 'bool',
        'show_grid_lines': 'bool',
        'font_substitutes': 'dict(str, str)',
        'default_font': 'str',
        'sheet_indexes': 'list[int]',
        'sheets': 'list[str]',
        'print_comments': 'str',
        'reset_font_folders': 'bool'
    }

    attribute_map = {
        'clear_custom_document_properties': 'ClearCustomDocumentProperties',
        'clear_built_in_document_properties': 'ClearBuiltInDocumentProperties',
        'rows_per_page': 'RowsPerPage',
        'columns_per_page': 'ColumnsPerPage',
        'auto_fit_rows': 'AutoFitRows',
        'all_columns_in_one_page_per_sheet': 'AllColumnsInOnePagePerSheet',
        'culture_info': 'CultureInfo',
        'check_excel_restriction': 'CheckExcelRestriction',
        'password': 'Password',
        'skip_empty_rows_and_columns': 'SkipEmptyRowsAndColumns',
        'convert_range': 'ConvertRange',
        'optimize_pdf_size': 'OptimizePdfSize',
        'one_page_per_sheet': 'OnePagePerSheet',
        'show_hidden_sheets': 'ShowHiddenSheets',
        'show_grid_lines': 'ShowGridLines',
        'font_substitutes': 'FontSubstitutes',
        'default_font': 'DefaultFont',
        'sheet_indexes': 'SheetIndexes',
        'sheets': 'Sheets',
        'print_comments': 'PrintComments',
        'reset_font_folders': 'ResetFontFolders'
    }

    def __init__(self, clear_custom_document_properties=None, clear_built_in_document_properties=None, rows_per_page=None, columns_per_page=None, auto_fit_rows=None, all_columns_in_one_page_per_sheet=None, culture_info=None, check_excel_restriction=None, password=None, skip_empty_rows_and_columns=None, convert_range=None, optimize_pdf_size=None, one_page_per_sheet=None, show_hidden_sheets=None, show_grid_lines=None, font_substitutes=None, default_font=None, sheet_indexes=None, sheets=None, print_comments=None, reset_font_folders=None, **kwargs):  # noqa: E501
        """Initializes new instance of SpreadsheetLoadOptions"""  # noqa: E501

        self._clear_custom_document_properties = None
        self._clear_built_in_document_properties = None
        self._rows_per_page = None
        self._columns_per_page = None
        self._auto_fit_rows = None
        self._all_columns_in_one_page_per_sheet = None
        self._culture_info = None
        self._check_excel_restriction = None
        self._password = None
        self._skip_empty_rows_and_columns = None
        self._convert_range = None
        self._optimize_pdf_size = None
        self._one_page_per_sheet = None
        self._show_hidden_sheets = None
        self._show_grid_lines = None
        self._font_substitutes = None
        self._default_font = None
        self._sheet_indexes = None
        self._sheets = None
        self._print_comments = None
        self._reset_font_folders = None

        if clear_custom_document_properties is not None:
            self.clear_custom_document_properties = clear_custom_document_properties
        if clear_built_in_document_properties is not None:
            self.clear_built_in_document_properties = clear_built_in_document_properties
        if rows_per_page is not None:
            self.rows_per_page = rows_per_page
        if columns_per_page is not None:
            self.columns_per_page = columns_per_page
        if auto_fit_rows is not None:
            self.auto_fit_rows = auto_fit_rows
        if all_columns_in_one_page_per_sheet is not None:
            self.all_columns_in_one_page_per_sheet = all_columns_in_one_page_per_sheet
        if culture_info is not None:
            self.culture_info = culture_info
        if check_excel_restriction is not None:
            self.check_excel_restriction = check_excel_restriction
        if password is not None:
            self.password = password
        if skip_empty_rows_and_columns is not None:
            self.skip_empty_rows_and_columns = skip_empty_rows_and_columns
        if convert_range is not None:
            self.convert_range = convert_range
        if optimize_pdf_size is not None:
            self.optimize_pdf_size = optimize_pdf_size
        if one_page_per_sheet is not None:
            self.one_page_per_sheet = one_page_per_sheet
        if show_hidden_sheets is not None:
            self.show_hidden_sheets = show_hidden_sheets
        if show_grid_lines is not None:
            self.show_grid_lines = show_grid_lines
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes
        if default_font is not None:
            self.default_font = default_font
        if sheet_indexes is not None:
            self.sheet_indexes = sheet_indexes
        if sheets is not None:
            self.sheets = sheets
        if print_comments is not None:
            self.print_comments = print_comments
        if reset_font_folders is not None:
            self.reset_font_folders = reset_font_folders

        base = super(SpreadsheetLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def clear_custom_document_properties(self):
        """
        Gets the clear_custom_document_properties.  # noqa: E501

        Clear custom document properties. Default is false.  # noqa: E501

        :return: The clear_custom_document_properties.  # noqa: E501
        :rtype: bool
        """
        return self._clear_custom_document_properties

    @clear_custom_document_properties.setter
    def clear_custom_document_properties(self, clear_custom_document_properties):
        """
        Sets the clear_custom_document_properties.

        Clear custom document properties. Default is false.  # noqa: E501

        :param clear_custom_document_properties: The clear_custom_document_properties.  # noqa: E501
        :type: bool
        """
        if clear_custom_document_properties is None:
            raise ValueError("Invalid value for `clear_custom_document_properties`, must not be `None`")  # noqa: E501
        self._clear_custom_document_properties = clear_custom_document_properties
    
    @property
    def clear_built_in_document_properties(self):
        """
        Gets the clear_built_in_document_properties.  # noqa: E501

        Clear built-in document properties. Default is false.  # noqa: E501

        :return: The clear_built_in_document_properties.  # noqa: E501
        :rtype: bool
        """
        return self._clear_built_in_document_properties

    @clear_built_in_document_properties.setter
    def clear_built_in_document_properties(self, clear_built_in_document_properties):
        """
        Sets the clear_built_in_document_properties.

        Clear built-in document properties. Default is false.  # noqa: E501

        :param clear_built_in_document_properties: The clear_built_in_document_properties.  # noqa: E501
        :type: bool
        """
        if clear_built_in_document_properties is None:
            raise ValueError("Invalid value for `clear_built_in_document_properties`, must not be `None`")  # noqa: E501
        self._clear_built_in_document_properties = clear_built_in_document_properties
    
    @property
    def rows_per_page(self):
        """
        Gets the rows_per_page.  # noqa: E501

        Split a worksheet into pages by rows. Default is 0, no pagination.  # noqa: E501

        :return: The rows_per_page.  # noqa: E501
        :rtype: int
        """
        return self._rows_per_page

    @rows_per_page.setter
    def rows_per_page(self, rows_per_page):
        """
        Sets the rows_per_page.

        Split a worksheet into pages by rows. Default is 0, no pagination.  # noqa: E501

        :param rows_per_page: The rows_per_page.  # noqa: E501
        :type: int
        """
        if rows_per_page is None:
            raise ValueError("Invalid value for `rows_per_page`, must not be `None`")  # noqa: E501
        self._rows_per_page = rows_per_page
    
    @property
    def columns_per_page(self):
        """
        Gets the columns_per_page.  # noqa: E501

        Split a worksheet into pages by columns. Default is 0, no pagination.  # noqa: E501

        :return: The columns_per_page.  # noqa: E501
        :rtype: int
        """
        return self._columns_per_page

    @columns_per_page.setter
    def columns_per_page(self, columns_per_page):
        """
        Sets the columns_per_page.

        Split a worksheet into pages by columns. Default is 0, no pagination.  # noqa: E501

        :param columns_per_page: The columns_per_page.  # noqa: E501
        :type: int
        """
        if columns_per_page is None:
            raise ValueError("Invalid value for `columns_per_page`, must not be `None`")  # noqa: E501
        self._columns_per_page = columns_per_page
    
    @property
    def auto_fit_rows(self):
        """
        Gets the auto_fit_rows.  # noqa: E501

        Autofits all rows when converting  # noqa: E501

        :return: The auto_fit_rows.  # noqa: E501
        :rtype: bool
        """
        return self._auto_fit_rows

    @auto_fit_rows.setter
    def auto_fit_rows(self, auto_fit_rows):
        """
        Sets the auto_fit_rows.

        Autofits all rows when converting  # noqa: E501

        :param auto_fit_rows: The auto_fit_rows.  # noqa: E501
        :type: bool
        """
        if auto_fit_rows is None:
            raise ValueError("Invalid value for `auto_fit_rows`, must not be `None`")  # noqa: E501
        self._auto_fit_rows = auto_fit_rows
    
    @property
    def all_columns_in_one_page_per_sheet(self):
        """
        Gets the all_columns_in_one_page_per_sheet.  # noqa: E501

        If AllColumnsInOnePagePerSheet is true, all column content of one sheet will output to only one page in result. The width of paper size of pagesetup will be invalid, and the other settings of pagesetup will still take effect.               # noqa: E501

        :return: The all_columns_in_one_page_per_sheet.  # noqa: E501
        :rtype: bool
        """
        return self._all_columns_in_one_page_per_sheet

    @all_columns_in_one_page_per_sheet.setter
    def all_columns_in_one_page_per_sheet(self, all_columns_in_one_page_per_sheet):
        """
        Sets the all_columns_in_one_page_per_sheet.

        If AllColumnsInOnePagePerSheet is true, all column content of one sheet will output to only one page in result. The width of paper size of pagesetup will be invalid, and the other settings of pagesetup will still take effect.               # noqa: E501

        :param all_columns_in_one_page_per_sheet: The all_columns_in_one_page_per_sheet.  # noqa: E501
        :type: bool
        """
        if all_columns_in_one_page_per_sheet is None:
            raise ValueError("Invalid value for `all_columns_in_one_page_per_sheet`, must not be `None`")  # noqa: E501
        self._all_columns_in_one_page_per_sheet = all_columns_in_one_page_per_sheet
    
    @property
    def culture_info(self):
        """
        Gets the culture_info.  # noqa: E501

        System culture info at the time file is loaded  # noqa: E501

        :return: The culture_info.  # noqa: E501
        :rtype: str
        """
        return self._culture_info

    @culture_info.setter
    def culture_info(self, culture_info):
        """
        Sets the culture_info.

        System culture info at the time file is loaded  # noqa: E501

        :param culture_info: The culture_info.  # noqa: E501
        :type: str
        """
        self._culture_info = culture_info
    
    @property
    def check_excel_restriction(self):
        """
        Gets the check_excel_restriction.  # noqa: E501

        Whether check restriction of excel file when user modify cells related objects. For example, excel does not allow inputting string value longer than 32K. When you input a value longer than 32K, if this property is true, you will get an Exception. If this property is false, we will accept your input string value as the cell's value so that later you can output the complete string value for other file formats such as CSV. However, if you have set such kind of value that is invalid for excel file format, you should not save the workbook as excel file format later. Otherwise there may be unexpected error for the generated excel file.               # noqa: E501

        :return: The check_excel_restriction.  # noqa: E501
        :rtype: bool
        """
        return self._check_excel_restriction

    @check_excel_restriction.setter
    def check_excel_restriction(self, check_excel_restriction):
        """
        Sets the check_excel_restriction.

        Whether check restriction of excel file when user modify cells related objects. For example, excel does not allow inputting string value longer than 32K. When you input a value longer than 32K, if this property is true, you will get an Exception. If this property is false, we will accept your input string value as the cell's value so that later you can output the complete string value for other file formats such as CSV. However, if you have set such kind of value that is invalid for excel file format, you should not save the workbook as excel file format later. Otherwise there may be unexpected error for the generated excel file.               # noqa: E501

        :param check_excel_restriction: The check_excel_restriction.  # noqa: E501
        :type: bool
        """
        if check_excel_restriction is None:
            raise ValueError("Invalid value for `check_excel_restriction`, must not be `None`")  # noqa: E501
        self._check_excel_restriction = check_excel_restriction
    
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
    def optimize_pdf_size(self):
        """
        Gets the optimize_pdf_size.  # noqa: E501

        If True and converting to Pdf the conversion is optimized for better file size than print quality.               # noqa: E501

        :return: The optimize_pdf_size.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_pdf_size

    @optimize_pdf_size.setter
    def optimize_pdf_size(self, optimize_pdf_size):
        """
        Sets the optimize_pdf_size.

        If True and converting to Pdf the conversion is optimized for better file size than print quality.               # noqa: E501

        :param optimize_pdf_size: The optimize_pdf_size.  # noqa: E501
        :type: bool
        """
        if optimize_pdf_size is None:
            raise ValueError("Invalid value for `optimize_pdf_size`, must not be `None`")  # noqa: E501
        self._optimize_pdf_size = optimize_pdf_size
    
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
    def sheet_indexes(self):
        """
        Gets the sheet_indexes.  # noqa: E501

        List of sheet indexes to convert. The indexes must be zero-based  # noqa: E501

        :return: The sheet_indexes.  # noqa: E501
        :rtype: list[int]
        """
        return self._sheet_indexes

    @sheet_indexes.setter
    def sheet_indexes(self, sheet_indexes):
        """
        Sets the sheet_indexes.

        List of sheet indexes to convert. The indexes must be zero-based  # noqa: E501

        :param sheet_indexes: The sheet_indexes.  # noqa: E501
        :type: list[int]
        """
        self._sheet_indexes = sheet_indexes
    
    @property
    def sheets(self):
        """
        Gets the sheets.  # noqa: E501

        List of sheet names to convert  # noqa: E501

        :return: The sheets.  # noqa: E501
        :rtype: list[str]
        """
        return self._sheets

    @sheets.setter
    def sheets(self, sheets):
        """
        Sets the sheets.

        List of sheet names to convert  # noqa: E501

        :param sheets: The sheets.  # noqa: E501
        :type: list[str]
        """
        self._sheets = sheets
    
    @property
    def print_comments(self):
        """
        Gets the print_comments.  # noqa: E501

        Represents the way comments are printed with the sheet. Default is PrintNoComments.  # noqa: E501

        :return: The print_comments.  # noqa: E501
        :rtype: str
        """
        return self._print_comments

    @print_comments.setter
    def print_comments(self, print_comments):
        """
        Sets the print_comments.

        Represents the way comments are printed with the sheet. Default is PrintNoComments.  # noqa: E501

        :param print_comments: The print_comments.  # noqa: E501
        :type: str
        """
        if print_comments is None:
            raise ValueError("Invalid value for `print_comments`, must not be `None`")  # noqa: E501
        allowed_values = ["PrintInPlace", "PrintNoComments", "PrintSheetEnd", "PrintWithThreadedComments"]  # noqa: E501
        if not print_comments.isdigit():	
            if print_comments not in allowed_values:
                raise ValueError(
                    "Invalid value for `print_comments` ({0}), must be one of {1}"  # noqa: E501
                    .format(print_comments, allowed_values))
            self._print_comments = print_comments
        else:
            self._print_comments = allowed_values[int(print_comments) if six.PY3 else long(print_comments)]
    
    @property
    def reset_font_folders(self):
        """
        Gets the reset_font_folders.  # noqa: E501

        Reset font folders before loading document  # noqa: E501

        :return: The reset_font_folders.  # noqa: E501
        :rtype: bool
        """
        return self._reset_font_folders

    @reset_font_folders.setter
    def reset_font_folders(self, reset_font_folders):
        """
        Sets the reset_font_folders.

        Reset font folders before loading document  # noqa: E501

        :param reset_font_folders: The reset_font_folders.  # noqa: E501
        :type: bool
        """
        if reset_font_folders is None:
            raise ValueError("Invalid value for `reset_font_folders`, must not be `None`")  # noqa: E501
        self._reset_font_folders = reset_font_folders

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
