# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ConsumptionResult.py">
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

class ConsumptionResult(object):
    """
    Metered license consumption information
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'credit': 'float',
        'quantity': 'float',
        'billed_api_calls': 'float'
    }

    attribute_map = {
        'credit': 'Credit',
        'quantity': 'Quantity',
        'billed_api_calls': 'BilledApiCalls'
    }

    def __init__(self, credit=None, quantity=None, billed_api_calls=None, **kwargs):  # noqa: E501
        """Initializes new instance of ConsumptionResult"""  # noqa: E501

        self._credit = None
        self._quantity = None
        self._billed_api_calls = None

        if credit is not None:
            self.credit = credit
        if quantity is not None:
            self.quantity = quantity
        if billed_api_calls is not None:
            self.billed_api_calls = billed_api_calls
    
    @property
    def credit(self):
        """
        Gets the credit.  # noqa: E501

        Amount of used credits  # noqa: E501

        :return: The credit.  # noqa: E501
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """
        Sets the credit.

        Amount of used credits  # noqa: E501

        :param credit: The credit.  # noqa: E501
        :type: float
        """
        if credit is None:
            raise ValueError("Invalid value for `credit`, must not be `None`")  # noqa: E501
        self._credit = credit
    
    @property
    def quantity(self):
        """
        Gets the quantity.  # noqa: E501

        Amount of MBs processed  # noqa: E501

        :return: The quantity.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity.

        Amount of MBs processed  # noqa: E501

        :param quantity: The quantity.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        self._quantity = quantity
    
    @property
    def billed_api_calls(self):
        """
        Gets the billed_api_calls.  # noqa: E501

        Billed API calls number  # noqa: E501

        :return: The billed_api_calls.  # noqa: E501
        :rtype: float
        """
        return self._billed_api_calls

    @billed_api_calls.setter
    def billed_api_calls(self, billed_api_calls):
        """
        Sets the billed_api_calls.

        Billed API calls number  # noqa: E501

        :param billed_api_calls: The billed_api_calls.  # noqa: E501
        :type: float
        """
        if billed_api_calls is None:
            raise ValueError("Invalid value for `billed_api_calls`, must not be `None`")  # noqa: E501
        self._billed_api_calls = billed_api_calls

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
        if not isinstance(other, ConsumptionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
