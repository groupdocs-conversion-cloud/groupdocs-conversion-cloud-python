# GroupDocs.Conversion Cloud Python SDK

This repository contains GroupDocs.Conversion Cloud SDK for Python source code. This SDK has been developed to help you get started with using our document conversion REST API, allowing to seamlessly convert your documents to any format you need. With this single API, you can convert back and forth between over 50 types of documents and images, including all Microsoft Office and OpenDocument file formats, PDF documents, HTML, CAD, raster images and many more.

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

### Create an account
Creating an account is very simple. Go to Dashboard to create a free account.
We’re using Single Sign On across our websites, therefore, if you already have an account with our services, you can use it to also access the [Dashboard](https://dashboard.groupdocs.cloud).

### Create an API client app
Before you can make any requests to GroupDocs Cloud API you need to get a Client Id and a Client Secret. This will be used to invoke GroupDocs Cloud API. You can get it by creating a new [Application](https://dashboard.groupdocs.cloud/applications).

## Convert document

Please follow the [installation procedure](#installation) and then run following:

```python
# Import module
import groupdocs_conversion_cloud

# Get your clientId and clientSecret at https://dashboard.groupdocs.cloud (free registration is required).
client_id = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Create instance of the API
apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(client_id, client_secret)

# Prepare request
request = groupdocs_conversion_cloud.ConvertDocumentDirectRequest("pdf", "myFile.docx")

# Convert
result = apiInstance.convert_document_direct(request)

print("Document converted: " + result)

```

## Convert document using cloud storage

```python
# Import module
import groupdocs_conversion_cloud

# Get your clientId and clientSecret at https://dashboard.groupdocs.cloud (free registration is required).
client_id = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Create instances of the APIs
fileApi = groupdocs_conversion_cloud.FileApi.from_keys(client_id, client_secret)
convertApi = groupdocs_conversion_cloud.ConvertApi.from_keys(client_id, client_secret)

# Upload file
fileApi.upload_file(groupdocs_conversion_cloud.UploadFileRequest("myFile.docx", "myFile.docx"))

# Prepare convert settings
settings = groupdocs_conversion_cloud.ConvertSettings()
settings.file_path = "myFile.docx"
settings.format = "pdf"
settings.output_path = "converted"

# Convert
result = convertApi.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

print("Document converted: " + result)

# Download result
response = fileApi.download_file(groupdocs_conversion_cloud.DownloadFileRequest("converted/myFile.pdf", None))

```

## Licensing
GroupDocs.Conversion Cloud Python SDK licensed under [MIT License](http://github.com/groupdocs-conversion-cloud/groupdocs-conversion-cloud-python/LICENSE).

## Resources
+ [**Website**](https://www.groupdocs.cloud)
+ [**Product Home**](https://products.groupdocs.cloud/conversion)
+ [**Documentation**](https://docs.groupdocs.cloud/display/conversioncloud/Home)
+ [**Free Support Forum**](https://forum.groupdocs.cloud/c/conversion)
+ [**Blog**](https://blog.groupdocs.cloud/category/conversion)

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.groupdocs.cloud/c/conversion).