# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WordProcessingLoadOptions.py">
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

class WordProcessingLoadOptions(LoadOptions):
    """
    WordProcessing document load options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_font': 'str',
        'font_substitutes': 'dict(str, str)',
        'password': 'str',
        'hide_word_tracked_changes': 'bool',
        'bookmarks_outline_level': 'int',
        'headings_outline_levels': 'int',
        'expanded_outline_levels': 'int',
        'clear_custom_document_properties': 'bool',
        'clear_built_in_document_properties': 'bool',
        'depth': 'int',
        'convert_owned': 'bool',
        'convert_owner': 'bool',
        'auto_hyphenation': 'bool',
        'hyphenate_caps': 'bool',
        'page_numbering': 'bool',
        'preserve_document_structure': 'bool',
        'skip_external_resources': 'bool',
        'use_text_shaper': 'bool',
        'preserve_form_fields': 'bool',
        'comment_display_mode': 'str',
        'keep_date_field_original_value': 'bool',
        'update_fields': 'bool',
        'update_page_layout': 'bool',
        'embed_true_type_fonts': 'bool',
        'font_info_substitution_enabled': 'bool',
        'font_config_substitution_enabled': 'bool',
        'font_name_substitution_enabled': 'bool',
        'show_full_commenter_name': 'bool'
    }

    attribute_map = {
        'default_font': 'DefaultFont',
        'font_substitutes': 'FontSubstitutes',
        'password': 'Password',
        'hide_word_tracked_changes': 'HideWordTrackedChanges',
        'bookmarks_outline_level': 'BookmarksOutlineLevel',
        'headings_outline_levels': 'HeadingsOutlineLevels',
        'expanded_outline_levels': 'ExpandedOutlineLevels',
        'clear_custom_document_properties': 'ClearCustomDocumentProperties',
        'clear_built_in_document_properties': 'ClearBuiltInDocumentProperties',
        'depth': 'Depth',
        'convert_owned': 'ConvertOwned',
        'convert_owner': 'ConvertOwner',
        'auto_hyphenation': 'AutoHyphenation',
        'hyphenate_caps': 'HyphenateCaps',
        'page_numbering': 'PageNumbering',
        'preserve_document_structure': 'PreserveDocumentStructure',
        'skip_external_resources': 'SkipExternalResources',
        'use_text_shaper': 'UseTextShaper',
        'preserve_form_fields': 'PreserveFormFields',
        'comment_display_mode': 'CommentDisplayMode',
        'keep_date_field_original_value': 'KeepDateFieldOriginalValue',
        'update_fields': 'UpdateFields',
        'update_page_layout': 'UpdatePageLayout',
        'embed_true_type_fonts': 'EmbedTrueTypeFonts',
        'font_info_substitution_enabled': 'FontInfoSubstitutionEnabled',
        'font_config_substitution_enabled': 'FontConfigSubstitutionEnabled',
        'font_name_substitution_enabled': 'FontNameSubstitutionEnabled',
        'show_full_commenter_name': 'ShowFullCommenterName'
    }

    def __init__(self, default_font=None, font_substitutes=None, password=None, hide_word_tracked_changes=None, bookmarks_outline_level=None, headings_outline_levels=None, expanded_outline_levels=None, clear_custom_document_properties=None, clear_built_in_document_properties=None, depth=None, convert_owned=None, convert_owner=None, auto_hyphenation=None, hyphenate_caps=None, page_numbering=None, preserve_document_structure=None, skip_external_resources=None, use_text_shaper=None, preserve_form_fields=None, comment_display_mode=None, keep_date_field_original_value=None, update_fields=None, update_page_layout=None, embed_true_type_fonts=None, font_info_substitution_enabled=None, font_config_substitution_enabled=None, font_name_substitution_enabled=None, show_full_commenter_name=None, **kwargs):  # noqa: E501
        """Initializes new instance of WordProcessingLoadOptions"""  # noqa: E501

        self._default_font = None
        self._font_substitutes = None
        self._password = None
        self._hide_word_tracked_changes = None
        self._bookmarks_outline_level = None
        self._headings_outline_levels = None
        self._expanded_outline_levels = None
        self._clear_custom_document_properties = None
        self._clear_built_in_document_properties = None
        self._depth = None
        self._convert_owned = None
        self._convert_owner = None
        self._auto_hyphenation = None
        self._hyphenate_caps = None
        self._page_numbering = None
        self._preserve_document_structure = None
        self._skip_external_resources = None
        self._use_text_shaper = None
        self._preserve_form_fields = None
        self._comment_display_mode = None
        self._keep_date_field_original_value = None
        self._update_fields = None
        self._update_page_layout = None
        self._embed_true_type_fonts = None
        self._font_info_substitution_enabled = None
        self._font_config_substitution_enabled = None
        self._font_name_substitution_enabled = None
        self._show_full_commenter_name = None

        if default_font is not None:
            self.default_font = default_font
        if font_substitutes is not None:
            self.font_substitutes = font_substitutes
        if password is not None:
            self.password = password
        if hide_word_tracked_changes is not None:
            self.hide_word_tracked_changes = hide_word_tracked_changes
        if bookmarks_outline_level is not None:
            self.bookmarks_outline_level = bookmarks_outline_level
        if headings_outline_levels is not None:
            self.headings_outline_levels = headings_outline_levels
        if expanded_outline_levels is not None:
            self.expanded_outline_levels = expanded_outline_levels
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
        if auto_hyphenation is not None:
            self.auto_hyphenation = auto_hyphenation
        if hyphenate_caps is not None:
            self.hyphenate_caps = hyphenate_caps
        if page_numbering is not None:
            self.page_numbering = page_numbering
        if preserve_document_structure is not None:
            self.preserve_document_structure = preserve_document_structure
        if skip_external_resources is not None:
            self.skip_external_resources = skip_external_resources
        if use_text_shaper is not None:
            self.use_text_shaper = use_text_shaper
        if preserve_form_fields is not None:
            self.preserve_form_fields = preserve_form_fields
        if comment_display_mode is not None:
            self.comment_display_mode = comment_display_mode
        if keep_date_field_original_value is not None:
            self.keep_date_field_original_value = keep_date_field_original_value
        if update_fields is not None:
            self.update_fields = update_fields
        if update_page_layout is not None:
            self.update_page_layout = update_page_layout
        if embed_true_type_fonts is not None:
            self.embed_true_type_fonts = embed_true_type_fonts
        if font_info_substitution_enabled is not None:
            self.font_info_substitution_enabled = font_info_substitution_enabled
        if font_config_substitution_enabled is not None:
            self.font_config_substitution_enabled = font_config_substitution_enabled
        if font_name_substitution_enabled is not None:
            self.font_name_substitution_enabled = font_name_substitution_enabled
        if show_full_commenter_name is not None:
            self.show_full_commenter_name = show_full_commenter_name

        base = super(WordProcessingLoadOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def default_font(self):
        """
        Gets the default_font.  # noqa: E501

        Default font for Words document. The following font will be used if a font is missing.  # noqa: E501

        :return: The default_font.  # noqa: E501
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font.

        Default font for Words document. The following font will be used if a font is missing.  # noqa: E501

        :param default_font: The default_font.  # noqa: E501
        :type: str
        """
        self._default_font = default_font
    
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
    def hide_word_tracked_changes(self):
        """
        Gets the hide_word_tracked_changes.  # noqa: E501

        Hide markup and track changes for Word documents  # noqa: E501

        :return: The hide_word_tracked_changes.  # noqa: E501
        :rtype: bool
        """
        return self._hide_word_tracked_changes

    @hide_word_tracked_changes.setter
    def hide_word_tracked_changes(self, hide_word_tracked_changes):
        """
        Sets the hide_word_tracked_changes.

        Hide markup and track changes for Word documents  # noqa: E501

        :param hide_word_tracked_changes: The hide_word_tracked_changes.  # noqa: E501
        :type: bool
        """
        if hide_word_tracked_changes is None:
            raise ValueError("Invalid value for `hide_word_tracked_changes`, must not be `None`")  # noqa: E501
        self._hide_word_tracked_changes = hide_word_tracked_changes
    
    @property
    def bookmarks_outline_level(self):
        """
        Gets the bookmarks_outline_level.  # noqa: E501

        Specifies the default level in the document outline at which to display Word bookmarks. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :return: The bookmarks_outline_level.  # noqa: E501
        :rtype: int
        """
        return self._bookmarks_outline_level

    @bookmarks_outline_level.setter
    def bookmarks_outline_level(self, bookmarks_outline_level):
        """
        Sets the bookmarks_outline_level.

        Specifies the default level in the document outline at which to display Word bookmarks. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :param bookmarks_outline_level: The bookmarks_outline_level.  # noqa: E501
        :type: int
        """
        if bookmarks_outline_level is None:
            raise ValueError("Invalid value for `bookmarks_outline_level`, must not be `None`")  # noqa: E501
        self._bookmarks_outline_level = bookmarks_outline_level
    
    @property
    def headings_outline_levels(self):
        """
        Gets the headings_outline_levels.  # noqa: E501

        Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the document outline. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :return: The headings_outline_levels.  # noqa: E501
        :rtype: int
        """
        return self._headings_outline_levels

    @headings_outline_levels.setter
    def headings_outline_levels(self, headings_outline_levels):
        """
        Sets the headings_outline_levels.

        Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the document outline. Default is 0. Valid range is 0 to 9.  # noqa: E501

        :param headings_outline_levels: The headings_outline_levels.  # noqa: E501
        :type: int
        """
        if headings_outline_levels is None:
            raise ValueError("Invalid value for `headings_outline_levels`, must not be `None`")  # noqa: E501
        self._headings_outline_levels = headings_outline_levels
    
    @property
    def expanded_outline_levels(self):
        """
        Gets the expanded_outline_levels.  # noqa: E501

        Specifies how many levels in the document outline to show expanded when the file is viewed. Default is 0. Valid range is 0 to 9. Note that this options will not work when saving to XPS.  # noqa: E501

        :return: The expanded_outline_levels.  # noqa: E501
        :rtype: int
        """
        return self._expanded_outline_levels

    @expanded_outline_levels.setter
    def expanded_outline_levels(self, expanded_outline_levels):
        """
        Sets the expanded_outline_levels.

        Specifies how many levels in the document outline to show expanded when the file is viewed. Default is 0. Valid range is 0 to 9. Note that this options will not work when saving to XPS.  # noqa: E501

        :param expanded_outline_levels: The expanded_outline_levels.  # noqa: E501
        :type: int
        """
        if expanded_outline_levels is None:
            raise ValueError("Invalid value for `expanded_outline_levels`, must not be `None`")  # noqa: E501
        self._expanded_outline_levels = expanded_outline_levels
    
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
    def depth(self):
        """
        Gets the depth.  # noqa: E501

        Option to control how many levels in depth to perform conversion. Default: 1.  # noqa: E501

        :return: The depth.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth.

        Option to control how many levels in depth to perform conversion. Default: 1.  # noqa: E501

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

        Option to control whether the owned documents in the documents container must be converted  # noqa: E501

        :return: The convert_owned.  # noqa: E501
        :rtype: bool
        """
        return self._convert_owned

    @convert_owned.setter
    def convert_owned(self, convert_owned):
        """
        Sets the convert_owned.

        Option to control whether the owned documents in the documents container must be converted  # noqa: E501

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

        Option to control whether the documents container itself must be converted If this property is true the documents container will be the first converted document. Default is true.  # noqa: E501

        :return: The convert_owner.  # noqa: E501
        :rtype: bool
        """
        return self._convert_owner

    @convert_owner.setter
    def convert_owner(self, convert_owner):
        """
        Sets the convert_owner.

        Option to control whether the documents container itself must be converted If this property is true the documents container will be the first converted document. Default is true.  # noqa: E501

        :param convert_owner: The convert_owner.  # noqa: E501
        :type: bool
        """
        if convert_owner is None:
            raise ValueError("Invalid value for `convert_owner`, must not be `None`")  # noqa: E501
        self._convert_owner = convert_owner
    
    @property
    def auto_hyphenation(self):
        """
        Gets the auto_hyphenation.  # noqa: E501

        Gets or sets value determining whether automatic hyphenation is turned on for the document. Default value for this property is false.  # noqa: E501

        :return: The auto_hyphenation.  # noqa: E501
        :rtype: bool
        """
        return self._auto_hyphenation

    @auto_hyphenation.setter
    def auto_hyphenation(self, auto_hyphenation):
        """
        Sets the auto_hyphenation.

        Gets or sets value determining whether automatic hyphenation is turned on for the document. Default value for this property is false.  # noqa: E501

        :param auto_hyphenation: The auto_hyphenation.  # noqa: E501
        :type: bool
        """
        if auto_hyphenation is None:
            raise ValueError("Invalid value for `auto_hyphenation`, must not be `None`")  # noqa: E501
        self._auto_hyphenation = auto_hyphenation
    
    @property
    def hyphenate_caps(self):
        """
        Gets the hyphenate_caps.  # noqa: E501

        Gets or sets value determining whether words written in all capital letters are hyphenated. Default value for this property is true.  # noqa: E501

        :return: The hyphenate_caps.  # noqa: E501
        :rtype: bool
        """
        return self._hyphenate_caps

    @hyphenate_caps.setter
    def hyphenate_caps(self, hyphenate_caps):
        """
        Sets the hyphenate_caps.

        Gets or sets value determining whether words written in all capital letters are hyphenated. Default value for this property is true.  # noqa: E501

        :param hyphenate_caps: The hyphenate_caps.  # noqa: E501
        :type: bool
        """
        if hyphenate_caps is None:
            raise ValueError("Invalid value for `hyphenate_caps`, must not be `None`")  # noqa: E501
        self._hyphenate_caps = hyphenate_caps
    
    @property
    def page_numbering(self):
        """
        Gets the page_numbering.  # noqa: E501

        Enable or disable generation of page numbering in converted document. Default: false  # noqa: E501

        :return: The page_numbering.  # noqa: E501
        :rtype: bool
        """
        return self._page_numbering

    @page_numbering.setter
    def page_numbering(self, page_numbering):
        """
        Sets the page_numbering.

        Enable or disable generation of page numbering in converted document. Default: false  # noqa: E501

        :param page_numbering: The page_numbering.  # noqa: E501
        :type: bool
        """
        if page_numbering is None:
            raise ValueError("Invalid value for `page_numbering`, must not be `None`")  # noqa: E501
        self._page_numbering = page_numbering
    
    @property
    def preserve_document_structure(self):
        """
        Gets the preserve_document_structure.  # noqa: E501

        Determines whether the document structure should be preserved when converting to PDF (default is false).  # noqa: E501

        :return: The preserve_document_structure.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_document_structure

    @preserve_document_structure.setter
    def preserve_document_structure(self, preserve_document_structure):
        """
        Sets the preserve_document_structure.

        Determines whether the document structure should be preserved when converting to PDF (default is false).  # noqa: E501

        :param preserve_document_structure: The preserve_document_structure.  # noqa: E501
        :type: bool
        """
        if preserve_document_structure is None:
            raise ValueError("Invalid value for `preserve_document_structure`, must not be `None`")  # noqa: E501
        self._preserve_document_structure = preserve_document_structure
    
    @property
    def skip_external_resources(self):
        """
        Gets the skip_external_resources.  # noqa: E501

        If true all external resource will not be loading. Default is true.  # noqa: E501

        :return: The skip_external_resources.  # noqa: E501
        :rtype: bool
        """
        return self._skip_external_resources

    @skip_external_resources.setter
    def skip_external_resources(self, skip_external_resources):
        """
        Sets the skip_external_resources.

        If true all external resource will not be loading. Default is true.  # noqa: E501

        :param skip_external_resources: The skip_external_resources.  # noqa: E501
        :type: bool
        """
        if skip_external_resources is None:
            raise ValueError("Invalid value for `skip_external_resources`, must not be `None`")  # noqa: E501
        self._skip_external_resources = skip_external_resources
    
    @property
    def use_text_shaper(self):
        """
        Gets the use_text_shaper.  # noqa: E501

        Specifies whether to use a text shaper for better kerning display. Default is false.  # noqa: E501

        :return: The use_text_shaper.  # noqa: E501
        :rtype: bool
        """
        return self._use_text_shaper

    @use_text_shaper.setter
    def use_text_shaper(self, use_text_shaper):
        """
        Sets the use_text_shaper.

        Specifies whether to use a text shaper for better kerning display. Default is false.  # noqa: E501

        :param use_text_shaper: The use_text_shaper.  # noqa: E501
        :type: bool
        """
        if use_text_shaper is None:
            raise ValueError("Invalid value for `use_text_shaper`, must not be `None`")  # noqa: E501
        self._use_text_shaper = use_text_shaper
    
    @property
    def preserve_form_fields(self):
        """
        Gets the preserve_form_fields.  # noqa: E501

        Specifies whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text. Default is false.  # noqa: E501

        :return: The preserve_form_fields.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_form_fields

    @preserve_form_fields.setter
    def preserve_form_fields(self, preserve_form_fields):
        """
        Sets the preserve_form_fields.

        Specifies whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text. Default is false.  # noqa: E501

        :param preserve_form_fields: The preserve_form_fields.  # noqa: E501
        :type: bool
        """
        if preserve_form_fields is None:
            raise ValueError("Invalid value for `preserve_form_fields`, must not be `None`")  # noqa: E501
        self._preserve_form_fields = preserve_form_fields
    
    @property
    def comment_display_mode(self):
        """
        Gets the comment_display_mode.  # noqa: E501

        Specifies how comments should be displayed in the output document. Default is Balloon.  # noqa: E501

        :return: The comment_display_mode.  # noqa: E501
        :rtype: str
        """
        return self._comment_display_mode

    @comment_display_mode.setter
    def comment_display_mode(self, comment_display_mode):
        """
        Sets the comment_display_mode.

        Specifies how comments should be displayed in the output document. Default is Balloon.  # noqa: E501

        :param comment_display_mode: The comment_display_mode.  # noqa: E501
        :type: str
        """
        if comment_display_mode is None:
            raise ValueError("Invalid value for `comment_display_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Hidden", "Balloon", "Annotation"]  # noqa: E501
        if not comment_display_mode.isdigit():	
            if comment_display_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `comment_display_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(comment_display_mode, allowed_values))
            self._comment_display_mode = comment_display_mode
        else:
            self._comment_display_mode = allowed_values[int(comment_display_mode) if six.PY3 else long(comment_display_mode)]
    
    @property
    def keep_date_field_original_value(self):
        """
        Gets the keep_date_field_original_value.  # noqa: E501

        Keep original value of date field. Default: false  # noqa: E501

        :return: The keep_date_field_original_value.  # noqa: E501
        :rtype: bool
        """
        return self._keep_date_field_original_value

    @keep_date_field_original_value.setter
    def keep_date_field_original_value(self, keep_date_field_original_value):
        """
        Sets the keep_date_field_original_value.

        Keep original value of date field. Default: false  # noqa: E501

        :param keep_date_field_original_value: The keep_date_field_original_value.  # noqa: E501
        :type: bool
        """
        if keep_date_field_original_value is None:
            raise ValueError("Invalid value for `keep_date_field_original_value`, must not be `None`")  # noqa: E501
        self._keep_date_field_original_value = keep_date_field_original_value
    
    @property
    def update_fields(self):
        """
        Gets the update_fields.  # noqa: E501

        Update fields after loading. Default: false  # noqa: E501

        :return: The update_fields.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """
        Sets the update_fields.

        Update fields after loading. Default: false  # noqa: E501

        :param update_fields: The update_fields.  # noqa: E501
        :type: bool
        """
        if update_fields is None:
            raise ValueError("Invalid value for `update_fields`, must not be `None`")  # noqa: E501
        self._update_fields = update_fields
    
    @property
    def update_page_layout(self):
        """
        Gets the update_page_layout.  # noqa: E501

        Update page layout after loading. Default: false  # noqa: E501

        :return: The update_page_layout.  # noqa: E501
        :rtype: bool
        """
        return self._update_page_layout

    @update_page_layout.setter
    def update_page_layout(self, update_page_layout):
        """
        Sets the update_page_layout.

        Update page layout after loading. Default: false  # noqa: E501

        :param update_page_layout: The update_page_layout.  # noqa: E501
        :type: bool
        """
        if update_page_layout is None:
            raise ValueError("Invalid value for `update_page_layout`, must not be `None`")  # noqa: E501
        self._update_page_layout = update_page_layout
    
    @property
    def embed_true_type_fonts(self):
        """
        Gets the embed_true_type_fonts.  # noqa: E501

        If EmbedTrueTypeFonts is true, GroupDocs.Conversion Cloud embed true type fonts in the output document. Default: true  # noqa: E501

        :return: The embed_true_type_fonts.  # noqa: E501
        :rtype: bool
        """
        return self._embed_true_type_fonts

    @embed_true_type_fonts.setter
    def embed_true_type_fonts(self, embed_true_type_fonts):
        """
        Sets the embed_true_type_fonts.

        If EmbedTrueTypeFonts is true, GroupDocs.Conversion Cloud embed true type fonts in the output document. Default: true  # noqa: E501

        :param embed_true_type_fonts: The embed_true_type_fonts.  # noqa: E501
        :type: bool
        """
        if embed_true_type_fonts is None:
            raise ValueError("Invalid value for `embed_true_type_fonts`, must not be `None`")  # noqa: E501
        self._embed_true_type_fonts = embed_true_type_fonts
    
    @property
    def font_info_substitution_enabled(self):
        """
        Gets the font_info_substitution_enabled.  # noqa: E501

        Automatically substitutes missing fonts based on FontInfo in the document. Default: false.  # noqa: E501

        :return: The font_info_substitution_enabled.  # noqa: E501
        :rtype: bool
        """
        return self._font_info_substitution_enabled

    @font_info_substitution_enabled.setter
    def font_info_substitution_enabled(self, font_info_substitution_enabled):
        """
        Sets the font_info_substitution_enabled.

        Automatically substitutes missing fonts based on FontInfo in the document. Default: false.  # noqa: E501

        :param font_info_substitution_enabled: The font_info_substitution_enabled.  # noqa: E501
        :type: bool
        """
        if font_info_substitution_enabled is None:
            raise ValueError("Invalid value for `font_info_substitution_enabled`, must not be `None`")  # noqa: E501
        self._font_info_substitution_enabled = font_info_substitution_enabled
    
    @property
    def font_config_substitution_enabled(self):
        """
        Gets the font_config_substitution_enabled.  # noqa: E501

        Automatically substitutes missing fonts based on FontConfig in the system. Default: false.  # noqa: E501

        :return: The font_config_substitution_enabled.  # noqa: E501
        :rtype: bool
        """
        return self._font_config_substitution_enabled

    @font_config_substitution_enabled.setter
    def font_config_substitution_enabled(self, font_config_substitution_enabled):
        """
        Sets the font_config_substitution_enabled.

        Automatically substitutes missing fonts based on FontConfig in the system. Default: false.  # noqa: E501

        :param font_config_substitution_enabled: The font_config_substitution_enabled.  # noqa: E501
        :type: bool
        """
        if font_config_substitution_enabled is None:
            raise ValueError("Invalid value for `font_config_substitution_enabled`, must not be `None`")  # noqa: E501
        self._font_config_substitution_enabled = font_config_substitution_enabled
    
    @property
    def font_name_substitution_enabled(self):
        """
        Gets the font_name_substitution_enabled.  # noqa: E501

        Automatically substitutes missing fonts based on the font name. Default: false.  # noqa: E501

        :return: The font_name_substitution_enabled.  # noqa: E501
        :rtype: bool
        """
        return self._font_name_substitution_enabled

    @font_name_substitution_enabled.setter
    def font_name_substitution_enabled(self, font_name_substitution_enabled):
        """
        Sets the font_name_substitution_enabled.

        Automatically substitutes missing fonts based on the font name. Default: false.  # noqa: E501

        :param font_name_substitution_enabled: The font_name_substitution_enabled.  # noqa: E501
        :type: bool
        """
        if font_name_substitution_enabled is None:
            raise ValueError("Invalid value for `font_name_substitution_enabled`, must not be `None`")  # noqa: E501
        self._font_name_substitution_enabled = font_name_substitution_enabled
    
    @property
    def show_full_commenter_name(self):
        """
        Gets the show_full_commenter_name.  # noqa: E501

        Show full commenter name in comments. Default is false.  # noqa: E501

        :return: The show_full_commenter_name.  # noqa: E501
        :rtype: bool
        """
        return self._show_full_commenter_name

    @show_full_commenter_name.setter
    def show_full_commenter_name(self, show_full_commenter_name):
        """
        Sets the show_full_commenter_name.

        Show full commenter name in comments. Default is false.  # noqa: E501

        :param show_full_commenter_name: The show_full_commenter_name.  # noqa: E501
        :type: bool
        """
        if show_full_commenter_name is None:
            raise ValueError("Invalid value for `show_full_commenter_name`, must not be `None`")  # noqa: E501
        self._show_full_commenter_name = show_full_commenter_name

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
        if not isinstance(other, WordProcessingLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
