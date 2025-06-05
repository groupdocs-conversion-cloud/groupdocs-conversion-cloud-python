# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PresentationLoadOptions.py">
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

class PresentationLoadOptions(LoadOptions):
    """
    Presentation document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'preserve_document_structure': 'bool',
        'clear_custom_document_properties': 'bool',
        'clear_built_in_document_properties': 'bool',
        'depth': 'int',
        'convert_owned': 'bool',
        'convert_owner': 'bool',
        'show_hidden_slides': 'bool',
        'default_font': 'str',
        'font_substitutes': 'dict(str, str)',
        'password': 'str',
        'comments_position': 'str',
        'notes_position': 'str'
    }

    attribute_map = {
        'preserve_document_structure': 'PreserveDocumentStructure',
        'clear_custom_document_properties': 'ClearCustomDocumentProperties',
        'clear_built_in_document_properties': 'ClearBuiltInDocumentProperties',
        'depth': 'Depth',
        'convert_owned': 'ConvertOwned',
        'convert_owner': 'ConvertOwner',
        'show_hidden_slides': 'ShowHiddenSlides',
        'default_font': 'DefaultFont',
        'font_substitutes': 'FontSubstitutes',
        'password': 'Password',
        'comments_position': 'CommentsPosition',
        'notes_position': 'NotesPosition'
    }

    def __init__(self, preserve_document_structure=None, clear_custom_document_properties=None, clear_built_in_document_properties=None, depth=None, convert_owned=None, convert_owner=None, show_hidden_slides=None, default_font=None, font_substitutes=None, password=None, comments_position=None, notes_position=None, **kwargs):  # noqa: E501
        """Initializes new instance of PresentationLoadOptions"""  # noqa: E501

        self._preserve_document_structure = None
        self._clear_custom_document_properties = None
        self._clear_built_in_document_properties = None
        self._depth = None
        self._convert_owned = None
        self._convert_owner = None
        self._show_hidden_slides = None
        self._default_font = None
        self._font_substitutes = None
        self._password = None
        self._comments_position = None
        self._notes_position = None

        if preserve_document_structure is not None:
            self.preserve_document_structure = preserve_document_structure
        if clear_custom_document_properties is not None:
            self.clear_custom_document_properties = clear_custom_document_properties
        if clear_built_in_document_properties is not None:
            self.clear_built_in_document_properties = clear_built_in_document_properties
        if depth is not None:
            self.depth = depth
        if convert_owned is not None:
            self.convert_owned = convert_owned
        if convert_owner is not None:
            self.convert_owner = convert_owner
        if show_hidden_slides is not None:
            self.show_hidden_slides = show_hidden_slides
        if default_font is not None:
            self.default_font = default_font
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes
        if password is not None:
            self.password = password
        if comments_position is not None:
            self.comments_position = comments_position
        if notes_position is not None:
            self.notes_position = notes_position

        base = super(PresentationLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def preserve_document_structure(self):
        """
        Gets the preserve_document_structure.  # noqa: E501

        Determines whether the document structure should be preserved when converting     to PDF (default is false).  # noqa: E501

        :return: The preserve_document_structure.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_document_structure

    @preserve_document_structure.setter
    def preserve_document_structure(self, preserve_document_structure):
        """
        Sets the preserve_document_structure.

        Determines whether the document structure should be preserved when converting     to PDF (default is false).  # noqa: E501

        :param preserve_document_structure: The preserve_document_structure.  # noqa: E501
        :type: bool
        """
        if preserve_document_structure is None:
            raise ValueError("Invalid value for `preserve_document_structure`, must not be `None`")  # noqa: E501
        self._preserve_document_structure = preserve_document_structure
    
    @property
    def clear_custom_document_properties(self):
        """
        Gets the clear_custom_document_properties.  # noqa: E501

        Value indicating whether custom document properties should be cleared.  # noqa: E501

        :return: The clear_custom_document_properties.  # noqa: E501
        :rtype: bool
        """
        return self._clear_custom_document_properties

    @clear_custom_document_properties.setter
    def clear_custom_document_properties(self, clear_custom_document_properties):
        """
        Sets the clear_custom_document_properties.

        Value indicating whether custom document properties should be cleared.  # noqa: E501

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

        Value indicating whether built in document properties should be cleared.  # noqa: E501

        :return: The clear_built_in_document_properties.  # noqa: E501
        :rtype: bool
        """
        return self._clear_built_in_document_properties

    @clear_built_in_document_properties.setter
    def clear_built_in_document_properties(self, clear_built_in_document_properties):
        """
        Sets the clear_built_in_document_properties.

        Value indicating whether built in document properties should be cleared.  # noqa: E501

        :param clear_built_in_document_properties: The clear_built_in_document_properties.  # noqa: E501
        :type: bool
        """
        if clear_built_in_document_properties is None:
            raise ValueError("Invalid value for `clear_built_in_document_properties`, must not be `None`")  # noqa: E501
        self._clear_built_in_document_properties = clear_built_in_document_properties
    
    @property
    def depth(self):
        """
        Gets the depth.  # noqa: E501

        Option to control how many levels in depth to perform conversion     Default: 1  # noqa: E501

        :return: The depth.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth.

        Option to control how many levels in depth to perform conversion     Default: 1  # noqa: E501

        :param depth: The depth.  # noqa: E501
        :type: int
        """
        if depth is None:
            raise ValueError("Invalid value for `depth`, must not be `None`")  # noqa: E501
        self._depth = depth
    
    @property
    def convert_owned(self):
        """
        Gets the convert_owned.  # noqa: E501

        Option to control whether the owned documents in the documents container must     be converted  # noqa: E501

        :return: The convert_owned.  # noqa: E501
        :rtype: bool
        """
        return self._convert_owned

    @convert_owned.setter
    def convert_owned(self, convert_owned):
        """
        Sets the convert_owned.

        Option to control whether the owned documents in the documents container must     be converted  # noqa: E501

        :param convert_owned: The convert_owned.  # noqa: E501
        :type: bool
        """
        if convert_owned is None:
            raise ValueError("Invalid value for `convert_owned`, must not be `None`")  # noqa: E501
        self._convert_owned = convert_owned
    
    @property
    def convert_owner(self):
        """
        Gets the convert_owner.  # noqa: E501

        Option to control whether the documents container itself must be converted If     this property is true the documents container will be the first converted document     Default is true  # noqa: E501

        :return: The convert_owner.  # noqa: E501
        :rtype: bool
        """
        return self._convert_owner

    @convert_owner.setter
    def convert_owner(self, convert_owner):
        """
        Sets the convert_owner.

        Option to control whether the documents container itself must be converted If     this property is true the documents container will be the first converted document     Default is true  # noqa: E501

        :param convert_owner: The convert_owner.  # noqa: E501
        :type: bool
        """
        if convert_owner is None:
            raise ValueError("Invalid value for `convert_owner`, must not be `None`")  # noqa: E501
        self._convert_owner = convert_owner
    
    @property
    def show_hidden_slides(self):
        """
        Gets the show_hidden_slides.  # noqa: E501

        Show hidden slides.  # noqa: E501

        :return: The show_hidden_slides.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_slides

    @show_hidden_slides.setter
    def show_hidden_slides(self, show_hidden_slides):
        """
        Sets the show_hidden_slides.

        Show hidden slides.  # noqa: E501

        :param show_hidden_slides: The show_hidden_slides.  # noqa: E501
        :type: bool
        """
        if show_hidden_slides is None:
            raise ValueError("Invalid value for `show_hidden_slides`, must not be `None`")  # noqa: E501
        self._show_hidden_slides = show_hidden_slides
    
    @property
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for rendering the presentation. The following font will be used if a presentation font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for rendering the presentation. The following font will be used if a presentation font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
    @property
    def font_substitutes(self):
        """
        Gets the font_substitutes.  # noqa: E501

        Substitute specific fonts when converting Slides document.  # noqa: E501

        :return: The font_substitutes.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._font_substitutes

    @font_substitutes.setter
    def font_substitutes(self, font_substitutes):
        """
        Sets the font_substitutes.

        Substitute specific fonts when converting Slides document.  # noqa: E501

        :param font_substitutes: The font_substitutes.  # noqa: E501
        :type: dict(str, str)
        """
        self._font_substitutes = font_substitutes
    
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
    def comments_position(self):
        """
        Gets the comments_position.  # noqa: E501

        Represents the way comments are printed with the slide. Default is None.  # noqa: E501

        :return: The comments_position.  # noqa: E501
        :rtype: str
        """
        return self._comments_position

    @comments_position.setter
    def comments_position(self, comments_position):
        """
        Sets the comments_position.

        Represents the way comments are printed with the slide. Default is None.  # noqa: E501

        :param comments_position: The comments_position.  # noqa: E501
        :type: str
        """
        if comments_position is None:
            raise ValueError("Invalid value for `comments_position`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Bottom", "Right"]  # noqa: E501
        if not comments_position.isdigit():	
            if comments_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `comments_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(comments_position, allowed_values))
            self._comments_position = comments_position
        else:
            self._comments_position = allowed_values[int(comments_position) if six.PY3 else long(comments_position)]
    
    @property
    def notes_position(self):
        """
        Gets the notes_position.  # noqa: E501

        Represents the way notes are printed with the slide. Default is None.  # noqa: E501

        :return: The notes_position.  # noqa: E501
        :rtype: str
        """
        return self._notes_position

    @notes_position.setter
    def notes_position(self, notes_position):
        """
        Sets the notes_position.

        Represents the way notes are printed with the slide. Default is None.  # noqa: E501

        :param notes_position: The notes_position.  # noqa: E501
        :type: str
        """
        if notes_position is None:
            raise ValueError("Invalid value for `notes_position`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "BottomTruncated", "BottomFull"]  # noqa: E501
        if not notes_position.isdigit():	
            if notes_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `notes_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(notes_position, allowed_values))
            self._notes_position = notes_position
        else:
            self._notes_position = allowed_values[int(notes_position) if six.PY3 else long(notes_position)]

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
        if not isinstance(other, PresentationLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
