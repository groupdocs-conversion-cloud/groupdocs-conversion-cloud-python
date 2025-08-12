# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfLoadOptions.py">
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

class PdfLoadOptions(LoadOptions):
    """
    Pdf document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'clear_built_in_document_properties': 'bool',
        'clear_custom_document_properties': 'bool',
        'page_numbering': 'bool',
        'flatten_all_fields': 'bool',
        'hide_pdf_annotations': 'bool',
        'default_font': 'str',
        'password': 'str',
        'remove_javascript': 'bool',
        'remove_embedded_files': 'bool',
        'font_substitutes': 'dict(str, str)'
    }

    attribute_map = {
        'clear_built_in_document_properties': 'ClearBuiltInDocumentProperties',
        'clear_custom_document_properties': 'ClearCustomDocumentProperties',
        'page_numbering': 'PageNumbering',
        'flatten_all_fields': 'FlattenAllFields',
        'hide_pdf_annotations': 'HidePdfAnnotations',
        'default_font': 'DefaultFont',
        'password': 'Password',
        'remove_javascript': 'RemoveJavascript',
        'remove_embedded_files': 'RemoveEmbeddedFiles',
        'font_substitutes': 'FontSubstitutes'
    }

    def __init__(self, clear_built_in_document_properties=None, clear_custom_document_properties=None, page_numbering=None, flatten_all_fields=None, hide_pdf_annotations=None, default_font=None, password=None, remove_javascript=None, remove_embedded_files=None, font_substitutes=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfLoadOptions"""  # noqa: E501

        self._clear_built_in_document_properties = None
        self._clear_custom_document_properties = None
        self._page_numbering = None
        self._flatten_all_fields = None
        self._hide_pdf_annotations = None
        self._default_font = None
        self._password = None
        self._remove_javascript = None
        self._remove_embedded_files = None
        self._font_substitutes = None

        if clear_built_in_document_properties is not None:
            self.clear_built_in_document_properties = clear_built_in_document_properties
        if clear_custom_document_properties is not None:
            self.clear_custom_document_properties = clear_custom_document_properties
        if page_numbering is not None:
            self.page_numbering = page_numbering
        if flatten_all_fields is not None:
            self.flatten_all_fields = flatten_all_fields
        if hide_pdf_annotations is not None:
            self.hide_pdf_annotations = hide_pdf_annotations
        if default_font is not None:
            self.default_font = default_font
        if password is not None:
            self.password = password
        if remove_javascript is not None:
            self.remove_javascript = remove_javascript
        if remove_embedded_files is not None:
            self.remove_embedded_files = remove_embedded_files
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes

        base = super(PdfLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def clear_built_in_document_properties(self):
        """
        Gets the clear_built_in_document_properties.  # noqa: E501

        Clear built-in document properties  # noqa: E501

        :return: The clear_built_in_document_properties.  # noqa: E501
        :rtype: bool
        """
        return self._clear_built_in_document_properties

    @clear_built_in_document_properties.setter
    def clear_built_in_document_properties(self, clear_built_in_document_properties):
        """
        Sets the clear_built_in_document_properties.

        Clear built-in document properties  # noqa: E501

        :param clear_built_in_document_properties: The clear_built_in_document_properties.  # noqa: E501
        :type: bool
        """
        if clear_built_in_document_properties is None:
            raise ValueError("Invalid value for `clear_built_in_document_properties`, must not be `None`")  # noqa: E501
        self._clear_built_in_document_properties = clear_built_in_document_properties
    
    @property
    def clear_custom_document_properties(self):
        """
        Gets the clear_custom_document_properties.  # noqa: E501

        Clear custom document properties  # noqa: E501

        :return: The clear_custom_document_properties.  # noqa: E501
        :rtype: bool
        """
        return self._clear_custom_document_properties

    @clear_custom_document_properties.setter
    def clear_custom_document_properties(self, clear_custom_document_properties):
        """
        Sets the clear_custom_document_properties.

        Clear custom document properties  # noqa: E501

        :param clear_custom_document_properties: The clear_custom_document_properties.  # noqa: E501
        :type: bool
        """
        if clear_custom_document_properties is None:
            raise ValueError("Invalid value for `clear_custom_document_properties`, must not be `None`")  # noqa: E501
        self._clear_custom_document_properties = clear_custom_document_properties
    
    @property
    def page_numbering(self):
        """
        Gets the page_numbering.  # noqa: E501

        Enable or disable generation of page numbering in converted document. Default:     false  # noqa: E501

        :return: The page_numbering.  # noqa: E501
        :rtype: bool
        """
        return self._page_numbering

    @page_numbering.setter
    def page_numbering(self, page_numbering):
        """
        Sets the page_numbering.

        Enable or disable generation of page numbering in converted document. Default:     false  # noqa: E501

        :param page_numbering: The page_numbering.  # noqa: E501
        :type: bool
        """
        if page_numbering is None:
            raise ValueError("Invalid value for `page_numbering`, must not be `None`")  # noqa: E501
        self._page_numbering = page_numbering
    
    @property
    def flatten_all_fields(self):
        """
        Gets the flatten_all_fields.  # noqa: E501

        Flatten all the fields of the PDF form  # noqa: E501

        :return: The flatten_all_fields.  # noqa: E501
        :rtype: bool
        """
        return self._flatten_all_fields

    @flatten_all_fields.setter
    def flatten_all_fields(self, flatten_all_fields):
        """
        Sets the flatten_all_fields.

        Flatten all the fields of the PDF form  # noqa: E501

        :param flatten_all_fields: The flatten_all_fields.  # noqa: E501
        :type: bool
        """
        if flatten_all_fields is None:
            raise ValueError("Invalid value for `flatten_all_fields`, must not be `None`")  # noqa: E501
        self._flatten_all_fields = flatten_all_fields
    
    @property
    def hide_pdf_annotations(self):
        """
        Gets the hide_pdf_annotations.  # noqa: E501

        Hide annotations in Pdf documents  # noqa: E501

        :return: The hide_pdf_annotations.  # noqa: E501
        :rtype: bool
        """
        return self._hide_pdf_annotations

    @hide_pdf_annotations.setter
    def hide_pdf_annotations(self, hide_pdf_annotations):
        """
        Sets the hide_pdf_annotations.

        Hide annotations in Pdf documents  # noqa: E501

        :param hide_pdf_annotations: The hide_pdf_annotations.  # noqa: E501
        :type: bool
        """
        if hide_pdf_annotations is None:
            raise ValueError("Invalid value for `hide_pdf_annotations`, must not be `None`")  # noqa: E501
        self._hide_pdf_annotations = hide_pdf_annotations
    
    @property
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for Pdf document. The following font will be used if a font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for Pdf document. The following font will be used if a font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
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
    def remove_javascript(self):
        """
        Gets the remove_javascript.  # noqa: E501

        Remove javascript  # noqa: E501

        :return: The remove_javascript.  # noqa: E501
        :rtype: bool
        """
        return self._remove_javascript

    @remove_javascript.setter
    def remove_javascript(self, remove_javascript):
        """
        Sets the remove_javascript.

        Remove javascript  # noqa: E501

        :param remove_javascript: The remove_javascript.  # noqa: E501
        :type: bool
        """
        if remove_javascript is None:
            raise ValueError("Invalid value for `remove_javascript`, must not be `None`")  # noqa: E501
        self._remove_javascript = remove_javascript
    
    @property
    def remove_embedded_files(self):
        """
        Gets the remove_embedded_files.  # noqa: E501

        Remove embedded files  # noqa: E501

        :return: The remove_embedded_files.  # noqa: E501
        :rtype: bool
        """
        return self._remove_embedded_files

    @remove_embedded_files.setter
    def remove_embedded_files(self, remove_embedded_files):
        """
        Sets the remove_embedded_files.

        Remove embedded files  # noqa: E501

        :param remove_embedded_files: The remove_embedded_files.  # noqa: E501
        :type: bool
        """
        if remove_embedded_files is None:
            raise ValueError("Invalid value for `remove_embedded_files`, must not be `None`")  # noqa: E501
        self._remove_embedded_files = remove_embedded_files
    
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
        if not isinstance(other, PdfLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
