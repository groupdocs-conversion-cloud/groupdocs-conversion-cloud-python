# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfConvertOptions.py">
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

from groupdocs_conversion_cloud.models import ConvertOptions

class PdfConvertOptions(ConvertOptions):
    """
    Options for to PDF conversion
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'width': 'int',
        'height': 'int',
        'dpi': 'float',
        'password': 'str',
        'margin_top': 'int',
        'margin_bottom': 'int',
        'margin_left': 'int',
        'margin_right': 'int',
        'pdf_format': 'str',
        'remove_pdfa_compliance': 'bool',
        'zoom': 'int',
        'linearize': 'bool',
        'link_duplicate_streams': 'bool',
        'remove_unused_objects': 'bool',
        'remove_unused_streams': 'bool',
        'compress_images': 'bool',
        'image_quality': 'int',
        'unembed_fonts': 'bool',
        'grayscale': 'bool',
        'center_window': 'bool',
        'direction': 'str',
        'display_doc_title': 'bool',
        'fit_window': 'bool',
        'hide_menu_bar': 'bool',
        'hide_tool_bar': 'bool',
        'hide_window_ui': 'bool',
        'non_full_screen_page_mode': 'str',
        'page_layout': 'str',
        'page_mode': 'str',
        'rotate': 'str',
        'watermark_options': 'WatermarkOptions'
    }

    attribute_map = {
        'width': 'Width',
        'height': 'Height',
        'dpi': 'Dpi',
        'password': 'Password',
        'margin_top': 'MarginTop',
        'margin_bottom': 'MarginBottom',
        'margin_left': 'MarginLeft',
        'margin_right': 'MarginRight',
        'pdf_format': 'PdfFormat',
        'remove_pdfa_compliance': 'RemovePdfaCompliance',
        'zoom': 'Zoom',
        'linearize': 'Linearize',
        'link_duplicate_streams': 'LinkDuplicateStreams',
        'remove_unused_objects': 'RemoveUnusedObjects',
        'remove_unused_streams': 'RemoveUnusedStreams',
        'compress_images': 'CompressImages',
        'image_quality': 'ImageQuality',
        'unembed_fonts': 'UnembedFonts',
        'grayscale': 'Grayscale',
        'center_window': 'CenterWindow',
        'direction': 'Direction',
        'display_doc_title': 'DisplayDocTitle',
        'fit_window': 'FitWindow',
        'hide_menu_bar': 'HideMenuBar',
        'hide_tool_bar': 'HideToolBar',
        'hide_window_ui': 'HideWindowUI',
        'non_full_screen_page_mode': 'NonFullScreenPageMode',
        'page_layout': 'PageLayout',
        'page_mode': 'PageMode',
        'rotate': 'Rotate',
        'watermark_options': 'WatermarkOptions'
    }

    def __init__(self, width=None, height=None, dpi=None, password=None, margin_top=None, margin_bottom=None, margin_left=None, margin_right=None, pdf_format=None, remove_pdfa_compliance=None, zoom=None, linearize=None, link_duplicate_streams=None, remove_unused_objects=None, remove_unused_streams=None, compress_images=None, image_quality=None, unembed_fonts=None, grayscale=None, center_window=None, direction=None, display_doc_title=None, fit_window=None, hide_menu_bar=None, hide_tool_bar=None, hide_window_ui=None, non_full_screen_page_mode=None, page_layout=None, page_mode=None, rotate=None, watermark_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfConvertOptions"""  # noqa: E501

        self._width = None
        self._height = None
        self._dpi = None
        self._password = None
        self._margin_top = None
        self._margin_bottom = None
        self._margin_left = None
        self._margin_right = None
        self._pdf_format = None
        self._remove_pdfa_compliance = None
        self._zoom = None
        self._linearize = None
        self._link_duplicate_streams = None
        self._remove_unused_objects = None
        self._remove_unused_streams = None
        self._compress_images = None
        self._image_quality = None
        self._unembed_fonts = None
        self._grayscale = None
        self._center_window = None
        self._direction = None
        self._display_doc_title = None
        self._fit_window = None
        self._hide_menu_bar = None
        self._hide_tool_bar = None
        self._hide_window_ui = None
        self._non_full_screen_page_mode = None
        self._page_layout = None
        self._page_mode = None
        self._rotate = None
        self._watermark_options = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if dpi is not None:
            self.dpi = dpi
        if password is not None:
            self.password = password
        if margin_top is not None:
            self.margin_top = margin_top
        if margin_bottom is not None:
            self.margin_bottom = margin_bottom
        if margin_left is not None:
            self.margin_left = margin_left
        if margin_right is not None:
            self.margin_right = margin_right
        if pdf_format is not None:
            self.pdf_format = pdf_format
        if remove_pdfa_compliance is not None:
            self.remove_pdfa_compliance = remove_pdfa_compliance
        if zoom is not None:
            self.zoom = zoom
        if linearize is not None:
            self.linearize = linearize
        if link_duplicate_streams is not None:
            self.link_duplicate_streams = link_duplicate_streams
        if remove_unused_objects is not None:
            self.remove_unused_objects = remove_unused_objects
        if remove_unused_streams is not None:
            self.remove_unused_streams = remove_unused_streams
        if compress_images is not None:
            self.compress_images = compress_images
        if image_quality is not None:
            self.image_quality = image_quality
        if unembed_fonts is not None:
            self.unembed_fonts = unembed_fonts
        if grayscale is not None:
            self.grayscale = grayscale
        if center_window is not None:
            self.center_window = center_window
        if direction is not None:
            self.direction = direction
        if display_doc_title is not None:
            self.display_doc_title = display_doc_title
        if fit_window is not None:
            self.fit_window = fit_window
        if hide_menu_bar is not None:
            self.hide_menu_bar = hide_menu_bar
        if hide_tool_bar is not None:
            self.hide_tool_bar = hide_tool_bar
        if hide_window_ui is not None:
            self.hide_window_ui = hide_window_ui
        if non_full_screen_page_mode is not None:
            self.non_full_screen_page_mode = non_full_screen_page_mode
        if page_layout is not None:
            self.page_layout = page_layout
        if page_mode is not None:
            self.page_mode = page_mode
        if rotate is not None:
            self.rotate = rotate
        if watermark_options is not None:
            self.watermark_options = watermark_options

        base = super(PdfConvertOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Desired page width in pixels after conversion  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Desired page width in pixels after conversion  # noqa: E501

        :param width: The width.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        Desired page height in pixels after conversion  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Desired page height in pixels after conversion  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def dpi(self):
        """
        Gets the dpi.  # noqa: E501

        Desired page DPI after conversion. The default resolution is: 96dpi  # noqa: E501

        :return: The dpi.  # noqa: E501
        :rtype: float
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """
        Sets the dpi.

        Desired page DPI after conversion. The default resolution is: 96dpi  # noqa: E501

        :param dpi: The dpi.  # noqa: E501
        :type: float
        """
        if dpi is None:
            raise ValueError("Invalid value for `dpi`, must not be `None`")  # noqa: E501
        self._dpi = dpi
    
    @property
    def password(self):
        """
        Gets the password.  # noqa: E501

        Set this property if you want to protect the converted document with a password  # noqa: E501

        :return: The password.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password.

        Set this property if you want to protect the converted document with a password  # noqa: E501

        :param password: The password.  # noqa: E501
        :type: str
        """
        self._password = password
    
    @property
    def margin_top(self):
        """
        Gets the margin_top.  # noqa: E501

        Desired page top margin in pixels after conversion  # noqa: E501

        :return: The margin_top.  # noqa: E501
        :rtype: int
        """
        return self._margin_top

    @margin_top.setter
    def margin_top(self, margin_top):
        """
        Sets the margin_top.

        Desired page top margin in pixels after conversion  # noqa: E501

        :param margin_top: The margin_top.  # noqa: E501
        :type: int
        """
        if margin_top is None:
            raise ValueError("Invalid value for `margin_top`, must not be `None`")  # noqa: E501
        self._margin_top = margin_top
    
    @property
    def margin_bottom(self):
        """
        Gets the margin_bottom.  # noqa: E501

        Desired page bottom margin in pixels after conversion  # noqa: E501

        :return: The margin_bottom.  # noqa: E501
        :rtype: int
        """
        return self._margin_bottom

    @margin_bottom.setter
    def margin_bottom(self, margin_bottom):
        """
        Sets the margin_bottom.

        Desired page bottom margin in pixels after conversion  # noqa: E501

        :param margin_bottom: The margin_bottom.  # noqa: E501
        :type: int
        """
        if margin_bottom is None:
            raise ValueError("Invalid value for `margin_bottom`, must not be `None`")  # noqa: E501
        self._margin_bottom = margin_bottom
    
    @property
    def margin_left(self):
        """
        Gets the margin_left.  # noqa: E501

        Desired page left margin in pixels after conversion  # noqa: E501

        :return: The margin_left.  # noqa: E501
        :rtype: int
        """
        return self._margin_left

    @margin_left.setter
    def margin_left(self, margin_left):
        """
        Sets the margin_left.

        Desired page left margin in pixels after conversion  # noqa: E501

        :param margin_left: The margin_left.  # noqa: E501
        :type: int
        """
        if margin_left is None:
            raise ValueError("Invalid value for `margin_left`, must not be `None`")  # noqa: E501
        self._margin_left = margin_left
    
    @property
    def margin_right(self):
        """
        Gets the margin_right.  # noqa: E501

        Desired page right margin in pixels after conversion  # noqa: E501

        :return: The margin_right.  # noqa: E501
        :rtype: int
        """
        return self._margin_right

    @margin_right.setter
    def margin_right(self, margin_right):
        """
        Sets the margin_right.

        Desired page right margin in pixels after conversion  # noqa: E501

        :param margin_right: The margin_right.  # noqa: E501
        :type: int
        """
        if margin_right is None:
            raise ValueError("Invalid value for `margin_right`, must not be `None`")  # noqa: E501
        self._margin_right = margin_right
    
    @property
    def pdf_format(self):
        """
        Gets the pdf_format.  # noqa: E501

        Set the pdf format of the converted document.  # noqa: E501

        :return: The pdf_format.  # noqa: E501
        :rtype: str
        """
        return self._pdf_format

    @pdf_format.setter
    def pdf_format(self, pdf_format):
        """
        Sets the pdf_format.

        Set the pdf format of the converted document.  # noqa: E501

        :param pdf_format: The pdf_format.  # noqa: E501
        :type: str
        """
        if pdf_format is None:
            raise ValueError("Invalid value for `pdf_format`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "PdfA_1A", "PdfA_1B", "PdfA_2A", "PdfA_3A", "PdfA_2B", "PdfA_2U", "PdfA_3B", "PdfA_3U", "v1_3", "v1_4", "v1_5", "v1_6", "v1_7", "PdfX_1A", "PdfX3"]  # noqa: E501
        if not pdf_format.isdigit():	
            if pdf_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `pdf_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(pdf_format, allowed_values))
            self._pdf_format = pdf_format
        else:
            self._pdf_format = allowed_values[int(pdf_format) if six.PY3 else long(pdf_format)]
    
    @property
    def remove_pdfa_compliance(self):
        """
        Gets the remove_pdfa_compliance.  # noqa: E501

        Remove Pdf-A Compliance  # noqa: E501

        :return: The remove_pdfa_compliance.  # noqa: E501
        :rtype: bool
        """
        return self._remove_pdfa_compliance

    @remove_pdfa_compliance.setter
    def remove_pdfa_compliance(self, remove_pdfa_compliance):
        """
        Sets the remove_pdfa_compliance.

        Remove Pdf-A Compliance  # noqa: E501

        :param remove_pdfa_compliance: The remove_pdfa_compliance.  # noqa: E501
        :type: bool
        """
        if remove_pdfa_compliance is None:
            raise ValueError("Invalid value for `remove_pdfa_compliance`, must not be `None`")  # noqa: E501
        self._remove_pdfa_compliance = remove_pdfa_compliance
    
    @property
    def zoom(self):
        """
        Gets the zoom.  # noqa: E501

        Specifies the zoom level in percentage. Default is 100.  # noqa: E501

        :return: The zoom.  # noqa: E501
        :rtype: int
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom.

        Specifies the zoom level in percentage. Default is 100.  # noqa: E501

        :param zoom: The zoom.  # noqa: E501
        :type: int
        """
        if zoom is None:
            raise ValueError("Invalid value for `zoom`, must not be `None`")  # noqa: E501
        self._zoom = zoom
    
    @property
    def linearize(self):
        """
        Gets the linearize.  # noqa: E501

        Linearize PDF Document for the Web  # noqa: E501

        :return: The linearize.  # noqa: E501
        :rtype: bool
        """
        return self._linearize

    @linearize.setter
    def linearize(self, linearize):
        """
        Sets the linearize.

        Linearize PDF Document for the Web  # noqa: E501

        :param linearize: The linearize.  # noqa: E501
        :type: bool
        """
        if linearize is None:
            raise ValueError("Invalid value for `linearize`, must not be `None`")  # noqa: E501
        self._linearize = linearize
    
    @property
    def link_duplicate_streams(self):
        """
        Gets the link_duplicate_streams.  # noqa: E501

        Link duplicate streams  # noqa: E501

        :return: The link_duplicate_streams.  # noqa: E501
        :rtype: bool
        """
        return self._link_duplicate_streams

    @link_duplicate_streams.setter
    def link_duplicate_streams(self, link_duplicate_streams):
        """
        Sets the link_duplicate_streams.

        Link duplicate streams  # noqa: E501

        :param link_duplicate_streams: The link_duplicate_streams.  # noqa: E501
        :type: bool
        """
        if link_duplicate_streams is None:
            raise ValueError("Invalid value for `link_duplicate_streams`, must not be `None`")  # noqa: E501
        self._link_duplicate_streams = link_duplicate_streams
    
    @property
    def remove_unused_objects(self):
        """
        Gets the remove_unused_objects.  # noqa: E501

        Remove unused objects  # noqa: E501

        :return: The remove_unused_objects.  # noqa: E501
        :rtype: bool
        """
        return self._remove_unused_objects

    @remove_unused_objects.setter
    def remove_unused_objects(self, remove_unused_objects):
        """
        Sets the remove_unused_objects.

        Remove unused objects  # noqa: E501

        :param remove_unused_objects: The remove_unused_objects.  # noqa: E501
        :type: bool
        """
        if remove_unused_objects is None:
            raise ValueError("Invalid value for `remove_unused_objects`, must not be `None`")  # noqa: E501
        self._remove_unused_objects = remove_unused_objects
    
    @property
    def remove_unused_streams(self):
        """
        Gets the remove_unused_streams.  # noqa: E501

        Remove unused streams  # noqa: E501

        :return: The remove_unused_streams.  # noqa: E501
        :rtype: bool
        """
        return self._remove_unused_streams

    @remove_unused_streams.setter
    def remove_unused_streams(self, remove_unused_streams):
        """
        Sets the remove_unused_streams.

        Remove unused streams  # noqa: E501

        :param remove_unused_streams: The remove_unused_streams.  # noqa: E501
        :type: bool
        """
        if remove_unused_streams is None:
            raise ValueError("Invalid value for `remove_unused_streams`, must not be `None`")  # noqa: E501
        self._remove_unused_streams = remove_unused_streams
    
    @property
    def compress_images(self):
        """
        Gets the compress_images.  # noqa: E501

        If CompressImages set to true, all images in the document are recompressed. The compression is defined by the ImageQuality property.  # noqa: E501

        :return: The compress_images.  # noqa: E501
        :rtype: bool
        """
        return self._compress_images

    @compress_images.setter
    def compress_images(self, compress_images):
        """
        Sets the compress_images.

        If CompressImages set to true, all images in the document are recompressed. The compression is defined by the ImageQuality property.  # noqa: E501

        :param compress_images: The compress_images.  # noqa: E501
        :type: bool
        """
        if compress_images is None:
            raise ValueError("Invalid value for `compress_images`, must not be `None`")  # noqa: E501
        self._compress_images = compress_images
    
    @property
    def image_quality(self):
        """
        Gets the image_quality.  # noqa: E501

        Value in percent where 100% is unchanged quality and image size. To decrease the image size, use ImageQuality less than 100               # noqa: E501

        :return: The image_quality.  # noqa: E501
        :rtype: int
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """
        Sets the image_quality.

        Value in percent where 100% is unchanged quality and image size. To decrease the image size, use ImageQuality less than 100               # noqa: E501

        :param image_quality: The image_quality.  # noqa: E501
        :type: int
        """
        if image_quality is None:
            raise ValueError("Invalid value for `image_quality`, must not be `None`")  # noqa: E501
        self._image_quality = image_quality
    
    @property
    def unembed_fonts(self):
        """
        Gets the unembed_fonts.  # noqa: E501

        Make fonts not embedded if set to true  # noqa: E501

        :return: The unembed_fonts.  # noqa: E501
        :rtype: bool
        """
        return self._unembed_fonts

    @unembed_fonts.setter
    def unembed_fonts(self, unembed_fonts):
        """
        Sets the unembed_fonts.

        Make fonts not embedded if set to true  # noqa: E501

        :param unembed_fonts: The unembed_fonts.  # noqa: E501
        :type: bool
        """
        if unembed_fonts is None:
            raise ValueError("Invalid value for `unembed_fonts`, must not be `None`")  # noqa: E501
        self._unembed_fonts = unembed_fonts
    
    @property
    def grayscale(self):
        """
        Gets the grayscale.  # noqa: E501

        Convert a PDF from RGB colorspace to Grayscale  # noqa: E501

        :return: The grayscale.  # noqa: E501
        :rtype: bool
        """
        return self._grayscale

    @grayscale.setter
    def grayscale(self, grayscale):
        """
        Sets the grayscale.

        Convert a PDF from RGB colorspace to Grayscale  # noqa: E501

        :param grayscale: The grayscale.  # noqa: E501
        :type: bool
        """
        if grayscale is None:
            raise ValueError("Invalid value for `grayscale`, must not be `None`")  # noqa: E501
        self._grayscale = grayscale
    
    @property
    def center_window(self):
        """
        Gets the center_window.  # noqa: E501

        Specify whether position of the document's window will be centered on the screen. Default: false.  # noqa: E501

        :return: The center_window.  # noqa: E501
        :rtype: bool
        """
        return self._center_window

    @center_window.setter
    def center_window(self, center_window):
        """
        Sets the center_window.

        Specify whether position of the document's window will be centered on the screen. Default: false.  # noqa: E501

        :param center_window: The center_window.  # noqa: E501
        :type: bool
        """
        if center_window is None:
            raise ValueError("Invalid value for `center_window`, must not be `None`")  # noqa: E501
        self._center_window = center_window
    
    @property
    def direction(self):
        """
        Gets the direction.  # noqa: E501

        Sets reading order of text: L2R (left to right) or R2L (right to left). Default: L2R.  # noqa: E501

        :return: The direction.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction.

        Sets reading order of text: L2R (left to right) or R2L (right to left). Default: L2R.  # noqa: E501

        :param direction: The direction.  # noqa: E501
        :type: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501
        allowed_values = ["L2R", "R2L"]  # noqa: E501
        if not direction.isdigit():	
            if direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(direction, allowed_values))
            self._direction = direction
        else:
            self._direction = allowed_values[int(direction) if six.PY3 else long(direction)]
    
    @property
    def display_doc_title(self):
        """
        Gets the display_doc_title.  # noqa: E501

        Specifying whether document's window title bar should display document title. Default: false.  # noqa: E501

        :return: The display_doc_title.  # noqa: E501
        :rtype: bool
        """
        return self._display_doc_title

    @display_doc_title.setter
    def display_doc_title(self, display_doc_title):
        """
        Sets the display_doc_title.

        Specifying whether document's window title bar should display document title. Default: false.  # noqa: E501

        :param display_doc_title: The display_doc_title.  # noqa: E501
        :type: bool
        """
        if display_doc_title is None:
            raise ValueError("Invalid value for `display_doc_title`, must not be `None`")  # noqa: E501
        self._display_doc_title = display_doc_title
    
    @property
    def fit_window(self):
        """
        Gets the fit_window.  # noqa: E501

        Specify whether document window must be resized to fit the first displayed page. Default: false.  # noqa: E501

        :return: The fit_window.  # noqa: E501
        :rtype: bool
        """
        return self._fit_window

    @fit_window.setter
    def fit_window(self, fit_window):
        """
        Sets the fit_window.

        Specify whether document window must be resized to fit the first displayed page. Default: false.  # noqa: E501

        :param fit_window: The fit_window.  # noqa: E501
        :type: bool
        """
        if fit_window is None:
            raise ValueError("Invalid value for `fit_window`, must not be `None`")  # noqa: E501
        self._fit_window = fit_window
    
    @property
    def hide_menu_bar(self):
        """
        Gets the hide_menu_bar.  # noqa: E501

        Specify whether menu bar should be hidden when document is active. Default: false.  # noqa: E501

        :return: The hide_menu_bar.  # noqa: E501
        :rtype: bool
        """
        return self._hide_menu_bar

    @hide_menu_bar.setter
    def hide_menu_bar(self, hide_menu_bar):
        """
        Sets the hide_menu_bar.

        Specify whether menu bar should be hidden when document is active. Default: false.  # noqa: E501

        :param hide_menu_bar: The hide_menu_bar.  # noqa: E501
        :type: bool
        """
        if hide_menu_bar is None:
            raise ValueError("Invalid value for `hide_menu_bar`, must not be `None`")  # noqa: E501
        self._hide_menu_bar = hide_menu_bar
    
    @property
    def hide_tool_bar(self):
        """
        Gets the hide_tool_bar.  # noqa: E501

        Specifying whether toolbar should be hidden when document is active. Default: false.  # noqa: E501

        :return: The hide_tool_bar.  # noqa: E501
        :rtype: bool
        """
        return self._hide_tool_bar

    @hide_tool_bar.setter
    def hide_tool_bar(self, hide_tool_bar):
        """
        Sets the hide_tool_bar.

        Specifying whether toolbar should be hidden when document is active. Default: false.  # noqa: E501

        :param hide_tool_bar: The hide_tool_bar.  # noqa: E501
        :type: bool
        """
        if hide_tool_bar is None:
            raise ValueError("Invalid value for `hide_tool_bar`, must not be `None`")  # noqa: E501
        self._hide_tool_bar = hide_tool_bar
    
    @property
    def hide_window_ui(self):
        """
        Gets the hide_window_ui.  # noqa: E501

        Specify whether user interface elements should be hidden when document is active. Default: false.  # noqa: E501

        :return: The hide_window_ui.  # noqa: E501
        :rtype: bool
        """
        return self._hide_window_ui

    @hide_window_ui.setter
    def hide_window_ui(self, hide_window_ui):
        """
        Sets the hide_window_ui.

        Specify whether user interface elements should be hidden when document is active. Default: false.  # noqa: E501

        :param hide_window_ui: The hide_window_ui.  # noqa: E501
        :type: bool
        """
        if hide_window_ui is None:
            raise ValueError("Invalid value for `hide_window_ui`, must not be `None`")  # noqa: E501
        self._hide_window_ui = hide_window_ui
    
    @property
    def non_full_screen_page_mode(self):
        """
        Gets the non_full_screen_page_mode.  # noqa: E501

        Sets page mode, specifying how to display the document on exiting full-screen mode.  # noqa: E501

        :return: The non_full_screen_page_mode.  # noqa: E501
        :rtype: str
        """
        return self._non_full_screen_page_mode

    @non_full_screen_page_mode.setter
    def non_full_screen_page_mode(self, non_full_screen_page_mode):
        """
        Sets the non_full_screen_page_mode.

        Sets page mode, specifying how to display the document on exiting full-screen mode.  # noqa: E501

        :param non_full_screen_page_mode: The non_full_screen_page_mode.  # noqa: E501
        :type: str
        """
        if non_full_screen_page_mode is None:
            raise ValueError("Invalid value for `non_full_screen_page_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["UseNone", "UseOutlines", "UseThumbs", "FullScreen", "UseOC", "UseAttachments"]  # noqa: E501
        if not non_full_screen_page_mode.isdigit():	
            if non_full_screen_page_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `non_full_screen_page_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(non_full_screen_page_mode, allowed_values))
            self._non_full_screen_page_mode = non_full_screen_page_mode
        else:
            self._non_full_screen_page_mode = allowed_values[int(non_full_screen_page_mode) if six.PY3 else long(non_full_screen_page_mode)]
    
    @property
    def page_layout(self):
        """
        Gets the page_layout.  # noqa: E501

        Sets page layout which shall be used when the document is opened.  # noqa: E501

        :return: The page_layout.  # noqa: E501
        :rtype: str
        """
        return self._page_layout

    @page_layout.setter
    def page_layout(self, page_layout):
        """
        Sets the page_layout.

        Sets page layout which shall be used when the document is opened.  # noqa: E501

        :param page_layout: The page_layout.  # noqa: E501
        :type: str
        """
        if page_layout is None:
            raise ValueError("Invalid value for `page_layout`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "SinglePage", "OneColumn", "TwoColumnLeft", "TwoColumnRight", "TwoPageLeft", "TwoPageRight"]  # noqa: E501
        if not page_layout.isdigit():	
            if page_layout not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_layout` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_layout, allowed_values))
            self._page_layout = page_layout
        else:
            self._page_layout = allowed_values[int(page_layout) if six.PY3 else long(page_layout)]
    
    @property
    def page_mode(self):
        """
        Gets the page_mode.  # noqa: E501

        Sets page mode, specifying how document should be displayed when opened.  # noqa: E501

        :return: The page_mode.  # noqa: E501
        :rtype: str
        """
        return self._page_mode

    @page_mode.setter
    def page_mode(self, page_mode):
        """
        Sets the page_mode.

        Sets page mode, specifying how document should be displayed when opened.  # noqa: E501

        :param page_mode: The page_mode.  # noqa: E501
        :type: str
        """
        if page_mode is None:
            raise ValueError("Invalid value for `page_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["UseNone", "UseOutlines", "UseThumbs", "FullScreen", "UseOC", "UseAttachments"]  # noqa: E501
        if not page_mode.isdigit():	
            if page_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_mode, allowed_values))
            self._page_mode = page_mode
        else:
            self._page_mode = allowed_values[int(page_mode) if six.PY3 else long(page_mode)]
    
    @property
    def rotate(self):
        """
        Gets the rotate.  # noqa: E501

        Rotate page  # noqa: E501

        :return: The rotate.  # noqa: E501
        :rtype: str
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """
        Sets the rotate.

        Rotate page  # noqa: E501

        :param rotate: The rotate.  # noqa: E501
        :type: str
        """
        if rotate is None:
            raise ValueError("Invalid value for `rotate`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "On90", "On180", "On270"]  # noqa: E501
        if not rotate.isdigit():	
            if rotate not in allowed_values:
                raise ValueError(
                    "Invalid value for `rotate` ({0}), must be one of {1}"  # noqa: E501
                    .format(rotate, allowed_values))
            self._rotate = rotate
        else:
            self._rotate = allowed_values[int(rotate) if six.PY3 else long(rotate)]
    
    @property
    def watermark_options(self):
        """
        Gets the watermark_options.  # noqa: E501

        Watermark specific options  # noqa: E501

        :return: The watermark_options.  # noqa: E501
        :rtype: WatermarkOptions
        """
        return self._watermark_options

    @watermark_options.setter
    def watermark_options(self, watermark_options):
        """
        Sets the watermark_options.

        Watermark specific options  # noqa: E501

        :param watermark_options: The watermark_options.  # noqa: E501
        :type: WatermarkOptions
        """
        self._watermark_options = watermark_options

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
        if not isinstance(other, PdfConvertOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
