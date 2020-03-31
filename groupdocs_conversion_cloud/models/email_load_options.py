# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="EmailLoadOptions.py">
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

class EmailLoadOptions(LoadOptions):
    """
    Options for loading Email documents
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_header': 'bool',
        'display_from_email_address': 'bool',
        'display_email_address': 'bool',
        'display_to_email_address': 'bool',
        'display_cc_email_address': 'bool',
        'display_bcc_email_address': 'bool',
        'time_zone_offset': 'str',
        'convert_attachments': 'bool',
        'field_labels': 'list[FieldLabel]',
        'preserve_original_date': 'bool'
    }

    attribute_map = {
        'display_header': 'DisplayHeader',
        'display_from_email_address': 'DisplayFromEmailAddress',
        'display_email_address': 'DisplayEmailAddress',
        'display_to_email_address': 'DisplayToEmailAddress',
        'display_cc_email_address': 'DisplayCcEmailAddress',
        'display_bcc_email_address': 'DisplayBccEmailAddress',
        'time_zone_offset': 'TimeZoneOffset',
        'convert_attachments': 'ConvertAttachments',
        'field_labels': 'FieldLabels',
        'preserve_original_date': 'PreserveOriginalDate'
    }

    def __init__(self, display_header=None, display_from_email_address=None, display_email_address=None, display_to_email_address=None, display_cc_email_address=None, display_bcc_email_address=None, time_zone_offset=None, convert_attachments=None, field_labels=None, preserve_original_date=None, **kwargs):  # noqa: E501
        """Initializes new instance of EmailLoadOptions"""  # noqa: E501

        self._display_header = None
        self._display_from_email_address = None
        self._display_email_address = None
        self._display_to_email_address = None
        self._display_cc_email_address = None
        self._display_bcc_email_address = None
        self._time_zone_offset = None
        self._convert_attachments = None
        self._field_labels = None
        self._preserve_original_date = None

        if display_header is not None:
            self.display_header = display_header
        if display_from_email_address is not None:
            self.display_from_email_address = display_from_email_address
        if display_email_address is not None:
            self.display_email_address = display_email_address
        if display_to_email_address is not None:
            self.display_to_email_address = display_to_email_address
        if display_cc_email_address is not None:
            self.display_cc_email_address = display_cc_email_address
        if display_bcc_email_address is not None:
            self.display_bcc_email_address = display_bcc_email_address
        if time_zone_offset is not None:
            self.time_zone_offset = time_zone_offset
        if convert_attachments is not None:
            self.convert_attachments = convert_attachments
        if field_labels is not None:
            self.field_labels = field_labels
        if preserve_original_date is not None:
            self.preserve_original_date = preserve_original_date

        base = super(EmailLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def display_header(self):
        """
        Gets the display_header.  # noqa: E501

        Option to display or hide the email header. Default: true  # noqa: E501

        :return: The display_header.  # noqa: E501
        :rtype: bool
        """
        return self._display_header

    @display_header.setter
    def display_header(self, display_header):
        """
        Sets the display_header.

        Option to display or hide the email header. Default: true  # noqa: E501

        :param display_header: The display_header.  # noqa: E501
        :type: bool
        """
        if display_header is None:
            raise ValueError("Invalid value for `display_header`, must not be `None`")  # noqa: E501
        self._display_header = display_header
    
    @property
    def display_from_email_address(self):
        """
        Gets the display_from_email_address.  # noqa: E501

        Option to display or hide \"from\" email address. Default: true  # noqa: E501

        :return: The display_from_email_address.  # noqa: E501
        :rtype: bool
        """
        return self._display_from_email_address

    @display_from_email_address.setter
    def display_from_email_address(self, display_from_email_address):
        """
        Sets the display_from_email_address.

        Option to display or hide \"from\" email address. Default: true  # noqa: E501

        :param display_from_email_address: The display_from_email_address.  # noqa: E501
        :type: bool
        """
        if display_from_email_address is None:
            raise ValueError("Invalid value for `display_from_email_address`, must not be `None`")  # noqa: E501
        self._display_from_email_address = display_from_email_address
    
    @property
    def display_email_address(self):
        """
        Gets the display_email_address.  # noqa: E501

        Option to display or hide email address. Default: true  # noqa: E501

        :return: The display_email_address.  # noqa: E501
        :rtype: bool
        """
        return self._display_email_address

    @display_email_address.setter
    def display_email_address(self, display_email_address):
        """
        Sets the display_email_address.

        Option to display or hide email address. Default: true  # noqa: E501

        :param display_email_address: The display_email_address.  # noqa: E501
        :type: bool
        """
        if display_email_address is None:
            raise ValueError("Invalid value for `display_email_address`, must not be `None`")  # noqa: E501
        self._display_email_address = display_email_address
    
    @property
    def display_to_email_address(self):
        """
        Gets the display_to_email_address.  # noqa: E501

        Option to display or hide \"to\" email address. Default: true  # noqa: E501

        :return: The display_to_email_address.  # noqa: E501
        :rtype: bool
        """
        return self._display_to_email_address

    @display_to_email_address.setter
    def display_to_email_address(self, display_to_email_address):
        """
        Sets the display_to_email_address.

        Option to display or hide \"to\" email address. Default: true  # noqa: E501

        :param display_to_email_address: The display_to_email_address.  # noqa: E501
        :type: bool
        """
        if display_to_email_address is None:
            raise ValueError("Invalid value for `display_to_email_address`, must not be `None`")  # noqa: E501
        self._display_to_email_address = display_to_email_address
    
    @property
    def display_cc_email_address(self):
        """
        Gets the display_cc_email_address.  # noqa: E501

        Option to display or hide \"Cc\" email address. Default: false  # noqa: E501

        :return: The display_cc_email_address.  # noqa: E501
        :rtype: bool
        """
        return self._display_cc_email_address

    @display_cc_email_address.setter
    def display_cc_email_address(self, display_cc_email_address):
        """
        Sets the display_cc_email_address.

        Option to display or hide \"Cc\" email address. Default: false  # noqa: E501

        :param display_cc_email_address: The display_cc_email_address.  # noqa: E501
        :type: bool
        """
        if display_cc_email_address is None:
            raise ValueError("Invalid value for `display_cc_email_address`, must not be `None`")  # noqa: E501
        self._display_cc_email_address = display_cc_email_address
    
    @property
    def display_bcc_email_address(self):
        """
        Gets the display_bcc_email_address.  # noqa: E501

        Option to display or hide \"Bcc\" email address. Default: false  # noqa: E501

        :return: The display_bcc_email_address.  # noqa: E501
        :rtype: bool
        """
        return self._display_bcc_email_address

    @display_bcc_email_address.setter
    def display_bcc_email_address(self, display_bcc_email_address):
        """
        Sets the display_bcc_email_address.

        Option to display or hide \"Bcc\" email address. Default: false  # noqa: E501

        :param display_bcc_email_address: The display_bcc_email_address.  # noqa: E501
        :type: bool
        """
        if display_bcc_email_address is None:
            raise ValueError("Invalid value for `display_bcc_email_address`, must not be `None`")  # noqa: E501
        self._display_bcc_email_address = display_bcc_email_address
    
    @property
    def time_zone_offset(self):
        """
        Gets the time_zone_offset.  # noqa: E501

        Gets or sets the Coordinated Universal Time (UTC) offset for the message dates. This property defines the time zone difference, between the localtime and UTC.  # noqa: E501

        :return: The time_zone_offset.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_offset

    @time_zone_offset.setter
    def time_zone_offset(self, time_zone_offset):
        """
        Sets the time_zone_offset.

        Gets or sets the Coordinated Universal Time (UTC) offset for the message dates. This property defines the time zone difference, between the localtime and UTC.  # noqa: E501

        :param time_zone_offset: The time_zone_offset.  # noqa: E501
        :type: str
        """
        self._time_zone_offset = time_zone_offset
    
    @property
    def convert_attachments(self):
        """
        Gets the convert_attachments.  # noqa: E501

        Option to convert attachments in source email or not. Default: false.  # noqa: E501

        :return: The convert_attachments.  # noqa: E501
        :rtype: bool
        """
        return self._convert_attachments

    @convert_attachments.setter
    def convert_attachments(self, convert_attachments):
        """
        Sets the convert_attachments.

        Option to convert attachments in source email or not. Default: false.  # noqa: E501

        :param convert_attachments: The convert_attachments.  # noqa: E501
        :type: bool
        """
        if convert_attachments is None:
            raise ValueError("Invalid value for `convert_attachments`, must not be `None`")  # noqa: E501
        self._convert_attachments = convert_attachments
    
    @property
    def field_labels(self):
        """
        Gets the field_labels.  # noqa: E501

        The mapping between email message field and field text representation  # noqa: E501

        :return: The field_labels.  # noqa: E501
        :rtype: list[FieldLabel]
        """
        return self._field_labels

    @field_labels.setter
    def field_labels(self, field_labels):
        """
        Sets the field_labels.

        The mapping between email message field and field text representation  # noqa: E501

        :param field_labels: The field_labels.  # noqa: E501
        :type: list[FieldLabel]
        """
        self._field_labels = field_labels
    
    @property
    def preserve_original_date(self):
        """
        Gets the preserve_original_date.  # noqa: E501

        Defines whether need to keep original date header string in mail message when saving or not (Default value is true)  # noqa: E501

        :return: The preserve_original_date.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_original_date

    @preserve_original_date.setter
    def preserve_original_date(self, preserve_original_date):
        """
        Sets the preserve_original_date.

        Defines whether need to keep original date header string in mail message when saving or not (Default value is true)  # noqa: E501

        :param preserve_original_date: The preserve_original_date.  # noqa: E501
        :type: bool
        """
        if preserve_original_date is None:
            raise ValueError("Invalid value for `preserve_original_date`, must not be `None`")  # noqa: E501
        self._preserve_original_date = preserve_original_date

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
        if not isinstance(other, EmailLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
