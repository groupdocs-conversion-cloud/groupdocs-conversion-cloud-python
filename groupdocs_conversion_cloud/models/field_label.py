# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="FieldLabel.py">
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

class FieldLabel(object):
    """
    Represents field label 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field': 'str',
        'label': 'str'
    }

    attribute_map = {
        'field': 'Field',
        'label': 'Label'
    }

    def __init__(self, field=None, label=None, **kwargs):  # noqa: E501
        """Initializes new instance of FieldLabel"""  # noqa: E501

        self._field = None
        self._label = None

        if field is not None:
            self.field = field
        if label is not None:
            self.label = label
    
    @property
    def field(self):
        """
        Gets the field.  # noqa: E501

        The field name  # noqa: E501

        :return: The field.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field.

        The field name  # noqa: E501

        :param field: The field.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        allowed_values = ["Start", "TabField", "Subject", "ShowTimeAs", "Sent", "RequiredAttendees", "RecurrencePattern", "Recurrence", "PageHeader", "Organizer", "Location", "Importance", "From", "End", "Bcc", "Attachments", "To"]  # noqa: E501
        if not field.isdigit():	
            if field not in allowed_values:
                raise ValueError(
                    "Invalid value for `field` ({0}), must be one of {1}"  # noqa: E501
                    .format(field, allowed_values))
            self._field = field
        else:
            self._field = allowed_values[int(field) if six.PY3 else long(field)]
    
    @property
    def label(self):
        """
        Gets the label.  # noqa: E501

        The label e.g. \"Sender\"  # noqa: E501

        :return: The label.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label.

        The label e.g. \"Sender\"  # noqa: E501

        :param label: The label.  # noqa: E501
        :type: str
        """
        self._label = label

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
        if not isinstance(other, FieldLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
