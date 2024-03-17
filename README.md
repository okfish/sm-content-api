# sm-content-api
Sbermarket API для мерчантов и ресторанов.

Позволяет управлять:
- ассортиментом товаров;
- меню;
- остатками товаров в магазинах;
- доступностью блюд;
- ценами и акциями на товары и блюда.

Базовый URL для запросов: `https://merchant-api.sbermarket.ru`

## Authentication

API для мерчантов для получения access tokens. 
Порядок работы 
    1. Получить access token, выполнив POST /auth/token по oAuth 2.0 flow (client credentials)

For more information, please visit [https://docs.sbermarket.ru/](https://docs.sbermarket.ru/)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sm_content_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sm_content_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sm_content_api
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)



# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 
    grant_type = 'grant_type_example' # str | 

    try:
        # Получение JWT токена
        api_response = await api_instance.get_token(client_id, client_secret, grant_type)
        print("The response of AuthenticationApi->get_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://merchant-api.sbermarket.ru*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**get_token**](docs/AuthenticationApi.md#get_token) | **POST** /auth/token | Получение JWT токена
*ImportApi* | [**import_availability**](docs/ImportApi.md#import_availability) | **PUT** /api/v1/import/availability | Указать доступность товаров/блюд
*ImportApi* | [**import_categories**](docs/ImportApi.md#import_categories) | **PUT** /api/v1/import/categories | Создать или обновить категорию товаров
*ImportApi* | [**import_offers**](docs/ImportApi.md#import_offers) | **PUT** /api/v1/import/offers | Создать или обновить товар
*ImportApi* | [**import_options_groups**](docs/ImportApi.md#import_options_groups) | **PUT** /api/v1/import/options-groups | Создать или обновить наборы опций блюд (для ресторанов)
*ImportApi* | [**import_prices**](docs/ImportApi.md#import_prices) | **PUT** /api/v1/import/prices | Обновить цену товаров
*ImportApi* | [**upload_offer_image**](docs/ImportApi.md#upload_offer_image) | **POST** /api/v1/import/offer-images | Загружает изображение товара (оффера)


## Documentation For Models

 - [Attribute](docs/Attribute.md)
 - [Availability](docs/Availability.md)
 - [Category](docs/Category.md)
 - [CommonDataObjectsProblemDetails](docs/CommonDataObjectsProblemDetails.md)
 - [CommonDataObjectsProblemDetailsInvalidParamsInner](docs/CommonDataObjectsProblemDetailsInvalidParamsInner.md)
 - [Error](docs/Error.md)
 - [GetToken200Response](docs/GetToken200Response.md)
 - [Image](docs/Image.md)
 - [ImportAvailability200Response](docs/ImportAvailability200Response.md)
 - [ImportAvailability200ResponseData](docs/ImportAvailability200ResponseData.md)
 - [ImportAvailabilityRequest](docs/ImportAvailabilityRequest.md)
 - [ImportCategoriesRequest](docs/ImportCategoriesRequest.md)
 - [ImportOffersRequest](docs/ImportOffersRequest.md)
 - [ImportOptionsGroupsRequest](docs/ImportOptionsGroupsRequest.md)
 - [ImportPricesRequest](docs/ImportPricesRequest.md)
 - [Offer](docs/Offer.md)
 - [OfferPrice](docs/OfferPrice.md)
 - [OfferPricePrice](docs/OfferPricePrice.md)
 - [OfferPricePricePromo](docs/OfferPricePricePromo.md)
 - [Option](docs/Option.md)
 - [OptionsGroup](docs/OptionsGroup.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oAuth2ClientCredentials"></a>
### oAuth2ClientCredentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author

okfish@yandex.ru


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.2a
- Package version: 1.0.0
- Generator version: 7.5.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen