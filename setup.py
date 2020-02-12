# coding: utf-8

import sys
import datetime

from setuptools import setup, find_packages  # noqa: H301

NAME = "groupdocs-conversion-cloud"
VERSION = "20.2"

# Append current time to the version when publishing to test environment
if "--test" in sys.argv:
    VERSION += "." + datetime.datetime.now().strftime("%Y%m%d%H%M")
    sys.argv.remove("--test")

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
TEST_REQUIRES = ["asposestoragecloud >= 1.0.5"]

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name=NAME,
    version=VERSION,
    description="GroupDocs.Conversion Cloud Python SDK",
	author="GroupDocs",
    author_email="support@groupdocs.cloud",
    url="http://github.com/groupdocs-conversion-cloud/groupdocs-conversion-cloud-python",
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
	],
    keywords=["groupdocs", "conversion", "cloud", "python", "sdk"],
    install_requires=REQUIRES,
	tests_require=TEST_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
