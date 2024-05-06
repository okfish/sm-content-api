# sm-content-api

## Content and Auth API

Sbermarket API для мерчантов и ресторанов.  
Позволяет управлять: 
    - ассортиментом товаров; 
    - меню; 
    - остатками товаров в магазинах; 
    - доступностью блюд; 
    - ценами и акциями на товары и блюда.  

Базовый URL для запросов: `https://merchant-api.sbermarket.ru`  

## Stores API

API для мерчантов для управления своими торговыми точками 

Порядок работы с Stores API  
1. Получить access token, выполнив (POST /auth/token) аутентификацию по oAuth 2.0 flow (client credentials) 
2. Получить список своих торговых точек выполнив запрос /retail-chains/{retail_chain_slug}/stores     
    - Где retail_chain_slug это идентификатор сети мерчанта полученный в СберМаркете     
    - Этот запрос возвращает постраничный список ваших stores, зарегистрированных в СберМаркете     
    - В поле \"id\" находится идентификатор store в системе СберМеркет     
    - В поле \"merchant_store_id\" находится идентификатор store в системе мерчанта       
    - Для получения или изменения данных по торговой точке необходимо предоставлять этот идентификатор 
      (merchant_store_id в пути к ресурсу) 
3. Указать дополнительные данные по торговой точке, которые зависят от типа интеграции с СберМаркетом 
   и вида торговой точки:     
    - при доставке мерчантом:       
    - PUT /retail-chains/{retail_chain_slug}/stores/{merchant_store_id}/merchant-status 
      (изменение статуса магазина)         
    - чтобы узнать текущий статус store в приложении СберМаркет используйте 
      GET /retail-chains/{retail_chain_slug}/stores/{merchant_store_id}           
      в поле sm_status.status указано доступен ли этот store в приложении СберМаркет для новых заказов    

Добавлены несколько методов для управления временем зоны доставки и ее активностью, 
а так же для запроса информации о торговых точках (ресторанах)

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
pip install git+https://github.com/okfish/sm-content-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/okfish/sm-content-api.git`)

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

As SM Content API doesn't have test sites, mock server needed for some tests, and you should implement it yourself. 
Otherwise, place your SM creds in the `.env.test` file to run tests with prod server

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

For more examples have a look at tests.


## Documentation for API Endpoints

All URIs are relative to *https://merchant-api.sbermarket.ru*

| Class               | Method | HTTP request | Description |
|---------------------| ------------- | ------------- | ------------- |
| *AuthenticationApi* | [**get_token**](docs/AuthenticationApi.md#get_token) | **POST** /auth/token | Получение JWT токена |
| *ImportApi*         | [**import_availability**](docs/ImportApi.md#import_availability) | **PUT** /api/v1/import/availability | Указать доступность товаров/блюд |
| *ImportApi*         | [**import_categories**](docs/ImportApi.md#import_categories) | **PUT** /api/v1/import/categories | Создать или обновить категорию товаров |
| *ImportApi*         | [**import_offers**](docs/ImportApi.md#import_offers) | **PUT** /api/v1/import/offers | Создать или обновить товар |
| *ImportApi*         | [**import_options_groups**](docs/ImportApi.md#import_options_groups) | **PUT** /api/v1/import/options-groups | Создать или обновить наборы опций блюд (для ресторанов) |
| *ImportApi*         | [**import_prices**](docs/ImportApi.md#import_prices) | **PUT** /api/v1/import/prices | Обновить цену товаров |
| *ImportApi*         | [**upload_offer_image**](docs/ImportApi.md#upload_offer_image) | **POST** /api/v1/import/offer-images | Загружает изображение товара (оффера) |


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
- **Authorization URL**: https://merchant-api.sbermarket.ru/auth/token
- **Scopes**:


## Author
Oleg Rybkin aka Fish
okfish@yandex.ru

with help of the [OpenAPI Generator](https://openapi-generator.tech) project:
- API version: 0.0.3a
- Package version: 0.2.0