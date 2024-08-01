# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="OperationResult.py">
#   Copyright (c) 2003-2024 Aspose Pty Ltd
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

class OperationResult(object):
    """
    Operation status result
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'method': 'str',
        'status': 'str',
        'created': 'datetime',
        'started': 'datetime',
        'failed': 'datetime',
        'canceled': 'datetime',
        'finished': 'datetime',
        'result': 'list[StoredConvertedResult]',
        'error': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'method': 'Method',
        'status': 'Status',
        'created': 'Created',
        'started': 'Started',
        'failed': 'Failed',
        'canceled': 'Canceled',
        'finished': 'Finished',
        'result': 'Result',
        'error': 'Error'
    }

    def __init__(self, id=None, method=None, status=None, created=None, started=None, failed=None, canceled=None, finished=None, result=None, error=None, **kwargs):  # noqa: E501
        """Initializes new instance of OperationResult"""  # noqa: E501

        self._id = None
        self._method = None
        self._status = None
        self._created = None
        self._started = None
        self._failed = None
        self._canceled = None
        self._finished = None
        self._result = None
        self._error = None

        if id is not None:
            self.id = id
        if method is not None:
            self.method = method
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if started is not None:
            self.started = started
        if failed is not None:
            self.failed = failed
        if canceled is not None:
            self.canceled = canceled
        if finished is not None:
            self.finished = finished
        if result is not None:
            self.result = result
        if error is not None:
            self.error = error
    
    @property
    def id(self):
        """
        Gets the id.  # noqa: E501


        :return: The id.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id.


        :param id: The id.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    
    @property
    def method(self):
        """
        Gets the method.  # noqa: E501


        :return: The method.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method.


        :param method: The method.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["Convert", "ConvertAndSave"]  # noqa: E501
        if not method.isdigit():	
            if method not in allowed_values:
                raise ValueError(
                    "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                    .format(method, allowed_values))
            self._method = method
        else:
            self._method = allowed_values[int(method) if six.PY3 else long(method)]
    
    @property
    def status(self):
        """
        Gets the status.  # noqa: E501


        :return: The status.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status.


        :param status: The status.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Created", "Started", "Failed", "Canceled", "Finished"]  # noqa: E501
        if not status.isdigit():	
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                    .format(status, allowed_values))
            self._status = status
        else:
            self._status = allowed_values[int(status) if six.PY3 else long(status)]
    
    @property
    def created(self):
        """
        Gets the created.  # noqa: E501


        :return: The created.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created.


        :param created: The created.  # noqa: E501
        :type: datetime
        """
        self._created = created
    
    @property
    def started(self):
        """
        Gets the started.  # noqa: E501


        :return: The started.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """
        Sets the started.


        :param started: The started.  # noqa: E501
        :type: datetime
        """
        self._started = started
    
    @property
    def failed(self):
        """
        Gets the failed.  # noqa: E501


        :return: The failed.  # noqa: E501
        :rtype: datetime
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed.


        :param failed: The failed.  # noqa: E501
        :type: datetime
        """
        self._failed = failed
    
    @property
    def canceled(self):
        """
        Gets the canceled.  # noqa: E501


        :return: The canceled.  # noqa: E501
        :rtype: datetime
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """
        Sets the canceled.


        :param canceled: The canceled.  # noqa: E501
        :type: datetime
        """
        self._canceled = canceled
    
    @property
    def finished(self):
        """
        Gets the finished.  # noqa: E501


        :return: The finished.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished.


        :param finished: The finished.  # noqa: E501
        :type: datetime
        """
        self._finished = finished
    
    @property
    def result(self):
        """
        Gets the result.  # noqa: E501


        :return: The result.  # noqa: E501
        :rtype: list[StoredConvertedResult]
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result.


        :param result: The result.  # noqa: E501
        :type: list[StoredConvertedResult]
        """
        self._result = result
    
    @property
    def error(self):
        """
        Gets the error.  # noqa: E501


        :return: The error.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error.


        :param error: The error.  # noqa: E501
        :type: str
        """
        self._error = error

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
        if not isinstance(other, OperationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
