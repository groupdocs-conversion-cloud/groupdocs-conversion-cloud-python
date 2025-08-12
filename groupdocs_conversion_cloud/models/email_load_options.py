# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="EmailLoadOptions.py">
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
        'preserve_original_date': 'bool',
        'field_labels': 'list[FieldLabel]',
        'time_zone_offset': 'str',
        'display_sent': 'bool',
        'display_subject': 'bool',
        'display_attachments': 'bool',
        'display_email_addresses': 'bool',
        'display_bcc_email_address': 'bool',
        'display_cc_email_address': 'bool',
        'display_to_email_address': 'bool',
        'display_from_email_address': 'bool',
        'display_header': 'bool',
        'default_font': 'str',
        'font_substitutes': 'dict(str, str)'
    }

    attribute_map = {
        'preserve_original_date': 'PreserveOriginalDate',
        'field_labels': 'FieldLabels',
        'time_zone_offset': 'TimeZoneOffset',
        'display_sent': 'DisplaySent',
        'display_subject': 'DisplaySubject',
        'display_attachments': 'DisplayAttachments',
        'display_email_addresses': 'DisplayEmailAddresses',
        'display_bcc_email_address': 'DisplayBccEmailAddress',
        'display_cc_email_address': 'DisplayCcEmailAddress',
        'display_to_email_address': 'DisplayToEmailAddress',
        'display_from_email_address': 'DisplayFromEmailAddress',
        'display_header': 'DisplayHeader',
        'default_font': 'DefaultFont',
        'font_substitutes': 'FontSubstitutes'
    }

    def __init__(self, preserve_original_date=None, field_labels=None, time_zone_offset=None, display_sent=None, display_subject=None, display_attachments=None, display_email_addresses=None, display_bcc_email_address=None, display_cc_email_address=None, display_to_email_address=None, display_from_email_address=None, display_header=None, default_font=None, font_substitutes=None, **kwargs):  # noqa: E501
        """Initializes new instance of EmailLoadOptions"""  # noqa: E501

        self._preserve_original_date = None
        self._field_labels = None
        self._time_zone_offset = None
        self._display_sent = None
        self._display_subject = None
        self._display_attachments = None
        self._display_email_addresses = None
        self._display_bcc_email_address = None
        self._display_cc_email_address = None
        self._display_to_email_address = None
        self._display_from_email_address = None
        self._display_header = None
        self._default_font = None
        self._font_substitutes = None

        if preserve_original_date is not None:
            self.preserve_original_date = preserve_original_date
        if field_labels is not None:
            self.field_labels = field_labels
        if time_zone_offset is not None:
            self.time_zone_offset = time_zone_offset
        if display_sent is not None:
            self.display_sent = display_sent
        if display_subject is not None:
            self.display_subject = display_subject
        if display_attachments is not None:
            self.display_attachments = display_attachments
        if display_email_addresses is not None:
            self.display_email_addresses = display_email_addresses
        if display_bcc_email_address is not None:
            self.display_bcc_email_address = display_bcc_email_address
        if display_cc_email_address is not None:
            self.display_cc_email_address = display_cc_email_address
        if display_to_email_address is not None:
            self.display_to_email_address = display_to_email_address
        if display_from_email_address is not None:
            self.display_from_email_address = display_from_email_address
        if display_header is not None:
            self.display_header = display_header
        if default_font is not None:
            self.default_font = default_font
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes

        base = super(EmailLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
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
    def display_sent(self):
        """
        Gets the display_sent.  # noqa: E501

        Option to display or hide sent date/time in the header. Default: true.  # noqa: E501

        :return: The display_sent.  # noqa: E501
        :rtype: bool
        """
        return self._display_sent

    @display_sent.setter
    def display_sent(self, display_sent):
        """
        Sets the display_sent.

        Option to display or hide sent date/time in the header. Default: true.  # noqa: E501

        :param display_sent: The display_sent.  # noqa: E501
        :type: bool
        """
        if display_sent is None:
            raise ValueError("Invalid value for `display_sent`, must not be `None`")  # noqa: E501
        self._display_sent = display_sent
    
    @property
    def display_subject(self):
        """
        Gets the display_subject.  # noqa: E501

        Option to display or hide subject in the header. Default: true.  # noqa: E501

        :return: The display_subject.  # noqa: E501
        :rtype: bool
        """
        return self._display_subject

    @display_subject.setter
    def display_subject(self, display_subject):
        """
        Sets the display_subject.

        Option to display or hide subject in the header. Default: true.  # noqa: E501

        :param display_subject: The display_subject.  # noqa: E501
        :type: bool
        """
        if display_subject is None:
            raise ValueError("Invalid value for `display_subject`, must not be `None`")  # noqa: E501
        self._display_subject = display_subject
    
    @property
    def display_attachments(self):
        """
        Gets the display_attachments.  # noqa: E501

        Option to display or hide attachments in the header. Default: true.  # noqa: E501

        :return: The display_attachments.  # noqa: E501
        :rtype: bool
        """
        return self._display_attachments

    @display_attachments.setter
    def display_attachments(self, display_attachments):
        """
        Sets the display_attachments.

        Option to display or hide attachments in the header. Default: true.  # noqa: E501

        :param display_attachments: The display_attachments.  # noqa: E501
        :type: bool
        """
        if display_attachments is None:
            raise ValueError("Invalid value for `display_attachments`, must not be `None`")  # noqa: E501
        self._display_attachments = display_attachments
    
    @property
    def display_email_addresses(self):
        """
        Gets the display_email_addresses.  # noqa: E501


        :return: The display_email_addresses.  # noqa: E501
        :rtype: bool
        """
        return self._display_email_addresses

    @display_email_addresses.setter
    def display_email_addresses(self, display_email_addresses):
        """
        Sets the display_email_addresses.


        :param display_email_addresses: The display_email_addresses.  # noqa: E501
        :type: bool
        """
        if display_email_addresses is None:
            raise ValueError("Invalid value for `display_email_addresses`, must not be `None`")  # noqa: E501
        self._display_email_addresses = display_email_addresses
    
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
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for Email document. The following font will be used if a font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for Email document. The following font will be used if a font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
    @property
    def font_substitutes(self):
        """
        Gets the font_substitutes.  # noqa: E501

        List of font substitutes.  # noqa: E501

        :return: The font_substitutes.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._font_substitutes

    @font_substitutes.setter
    def font_substitutes(self, font_substitutes):
        """
        Sets the font_substitutes.

        List of font substitutes.  # noqa: E501

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
        if not isinstance(other, EmailLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
