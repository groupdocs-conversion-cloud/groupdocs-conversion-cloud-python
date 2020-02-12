# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfLoadOptions.py">
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
        'remove_embedded_files': 'bool',
        'password': 'str',
        'hide_pdf_annotations': 'bool',
        'flatten_all_fields': 'bool'
    }

    attribute_map = {
        'remove_embedded_files': 'RemoveEmbeddedFiles',
        'password': 'Password',
        'hide_pdf_annotations': 'HidePdfAnnotations',
        'flatten_all_fields': 'FlattenAllFields'
    }

    def __init__(self, remove_embedded_files=None, password=None, hide_pdf_annotations=None, flatten_all_fields=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfLoadOptions"""  # noqa: E501

        self._remove_embedded_files = None
        self._password = None
        self._hide_pdf_annotations = None
        self._flatten_all_fields = None

        if remove_embedded_files is not None:
            self.remove_embedded_files = remove_embedded_files
        if password is not None:
            self.password = password
        if hide_pdf_annotations is not None:
            self.hide_pdf_annotations = hide_pdf_annotations
        if flatten_all_fields is not None:
            self.flatten_all_fields = flatten_all_fields

        base = super(PdfLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
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
