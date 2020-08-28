# GroupDocs.Conversion Cloud Python SDK
Python package for communicating with the GroupDocs.Conversion Cloud API

## Requirements

Python 2.7 or 3.4+

## Installation
Install `groupdocs-conversion-cloud` with [PIP](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/) by:

```sh
pip install groupdocs-conversion-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools): 

```sh
python setup.py install
```

## Getting Started

Please follow the [installation procedure](#installation) and then run following:

```python
# Import module
import groupdocs_conversion_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
app_sid = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
app_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Create instance of the API
api = groupdocs_conversion_cloud.InfoApi.from_keys(app_sid, app_key)

try:
    # Retrieve supported conversion types
    request = groupdocs_conversion_cloud.GetSupportedConversionTypesRequest()
    response = api.get_supported_conversion_types(request)

    # Print out supported conversion types
    print("Supported conversion types:")
    for format in response:
        print('{0} to [{1}]'.format(format.source_format, ', '.join(format.target_formats))) 
except groupdocs_conversion_cloud.ApiException as e:
    print("Exception when calling get_supported_conversion_types: {0}".format(e.message))
```

## Licensing
GroupDocs.Conversion Cloud Python SDK licensed under [MIT License](http://github.com/groupdocs-conversion-cloud/groupdocs-conversion-cloud-python/LICENSE).

[Home](https://www.groupdocs.cloud/) | [Product Page](https://products.groupdocs.cloud/conversion/python) | [Docs](https://docs.groupdocs.cloud/conversion/) | [Demos](https://products.groupdocs.app/conversion/family) | [API Reference](https://apireference.groupdocs.cloud/conversion/) | [Examples](https://github.com/groupdocs-conversion-cloud/groupdocs-conversion-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/conversion/) | [Free Support](https://forum.groupdocs.cloud/c/conversion) | [Free Trial](https://purchase.groupdocs.cloud/trial)
