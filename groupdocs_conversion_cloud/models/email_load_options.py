# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="EmailLoadOptions.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
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
        'display_bcc_email_address': 'bool'
    }

    attribute_map = {
        'display_header': 'DisplayHeader',
        'display_from_email_address': 'DisplayFromEmailAddress',
        'display_email_address': 'DisplayEmailAddress',
        'display_to_email_address': 'DisplayToEmailAddress',
        'display_cc_email_address': 'DisplayCcEmailAddress',
        'display_bcc_email_address': 'DisplayBccEmailAddress'
    }

    def __init__(self, display_header=None, display_from_email_address=None, display_email_address=None, display_to_email_address=None, display_cc_email_address=None, display_bcc_email_address=None, **kwargs):  # noqa: E501
        """Initializes new instance of EmailLoadOptions"""  # noqa: E501

        self._display_header = None
        self._display_from_email_address = None
        self._display_email_address = None
        self._display_to_email_address = None
        self._display_cc_email_address = None
        self._display_bcc_email_address = None

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
