# sm_content_api.ImportApi

All URIs are relative to *https://merchant-api.sbermarket.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_availability**](ImportApi.md#import_availability) | **PUT** /api/v1/import/availability | Указать доступность товаров/блюд
[**import_categories**](ImportApi.md#import_categories) | **PUT** /api/v1/import/categories | Создать или обновить категорию товаров
[**import_offers**](ImportApi.md#import_offers) | **PUT** /api/v1/import/offers | Создать или обновить товар
[**import_options_groups**](ImportApi.md#import_options_groups) | **PUT** /api/v1/import/options-groups | Создать или обновить наборы опций блюд (для ресторанов)
[**import_prices**](ImportApi.md#import_prices) | **PUT** /api/v1/import/prices | Обновить цену товаров
[**upload_offer_image**](ImportApi.md#upload_offer_image) | **POST** /api/v1/import/offer-images | Загружает изображение товара (оффера)


# **import_availability**
> ImportAvailability200Response import_availability(import_availability_request)

Указать доступность товаров/блюд

В одном запросе можно передать до 1000 записей. Каждая запись — это отдельный элемент в массиве.  В одном запросе, можно передавать информацию о доступности в разных магазинах, ограничение составляет до 10 уникальных магазинов.  ***rate-limiting*** - максимальная частота запросов составляет 10 запросов в секунду. В случаях, когда лимит будет превышен, сервер вернёт ошибку с кодом 429. 

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import sm_content_api
from sm_content_api.models.import_availability200_response import ImportAvailability200Response
from sm_content_api.models.import_availability_request import ImportAvailabilityRequest
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.ImportApi(api_client)
    import_availability_request = sm_content_api.ImportAvailabilityRequest() # ImportAvailabilityRequest | 

    try:
        # Указать доступность товаров/блюд
        api_response = await api_instance.import_availability(import_availability_request)
        print("The response of ImportApi->import_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_availability_request** | [**ImportAvailabilityRequest**](ImportAvailabilityRequest.md)|  | 

### Return type

[**ImportAvailability200Response**](ImportAvailability200Response.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат выполнения запроса на создание/изменение данных |  -  |
**400** | Некорректно указаны данные в запросе |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_categories**
> ImportAvailability200Response import_categories(import_categories_request)

Создать или обновить категорию товаров

В одном запросе можно передать до 1000 категорий. Каждая категория — это отдельный элемент в массиве.  ***rate-limiting*** - максимальная частота запросов составляет 10 запросов в секунду. В случаях, когда лимит будет превышен, сервер вернёт ошибку с кодом 429. 

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import sm_content_api
from sm_content_api.models.import_availability200_response import ImportAvailability200Response
from sm_content_api.models.import_categories_request import ImportCategoriesRequest
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.ImportApi(api_client)
    import_categories_request = sm_content_api.ImportCategoriesRequest() # ImportCategoriesRequest | 

    try:
        # Создать или обновить категорию товаров
        api_response = await api_instance.import_categories(import_categories_request)
        print("The response of ImportApi->import_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_categories_request** | [**ImportCategoriesRequest**](ImportCategoriesRequest.md)|  | 

### Return type

[**ImportAvailability200Response**](ImportAvailability200Response.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат выполнения запроса на создание/изменение данных |  -  |
**400** | Некорректно указаны данные в запросе |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_offers**
> ImportAvailability200Response import_offers(import_offers_request)

Создать или обновить товар

В одном запросе можно передать до 1000 товаров. Каждый товар — это отдельный элемент в массиве.  ***rate-limiting*** - максимальная частота запросов составляет 10 запросов в секунду. В случаях, когда лимит будет превышен, сервер вернёт ошибку с кодом 429. 

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import sm_content_api
from sm_content_api.models.import_availability200_response import ImportAvailability200Response
from sm_content_api.models.import_offers_request import ImportOffersRequest
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.ImportApi(api_client)
    import_offers_request = sm_content_api.ImportOffersRequest() # ImportOffersRequest | 

    try:
        # Создать или обновить товар
        api_response = await api_instance.import_offers(import_offers_request)
        print("The response of ImportApi->import_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_offers_request** | [**ImportOffersRequest**](ImportOffersRequest.md)|  | 

### Return type

[**ImportAvailability200Response**](ImportAvailability200Response.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат выполнения запроса на создание/изменение данных |  -  |
**400** | Некорректно указаны данные в запросе |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_options_groups**
> ImportAvailability200Response import_options_groups(import_options_groups_request)

Создать или обновить наборы опций блюд (для ресторанов)

В одном запросе можно передать до 1000 наборов. Каждый набор опций — это отдельный элемент в массиве.  ***rate-limiting*** - максимальная частота запросов составляет 10 запросов в секунду. В случаях, когда лимит будет превышен, сервер вернёт ошибку с кодом 429. 

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import sm_content_api
from sm_content_api.models.import_availability200_response import ImportAvailability200Response
from sm_content_api.models.import_options_groups_request import ImportOptionsGroupsRequest
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.ImportApi(api_client)
    import_options_groups_request = sm_content_api.ImportOptionsGroupsRequest() # ImportOptionsGroupsRequest | 

    try:
        # Создать или обновить наборы опций блюд (для ресторанов)
        api_response = await api_instance.import_options_groups(import_options_groups_request)
        print("The response of ImportApi->import_options_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_options_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_options_groups_request** | [**ImportOptionsGroupsRequest**](ImportOptionsGroupsRequest.md)|  | 

### Return type

[**ImportAvailability200Response**](ImportAvailability200Response.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат выполнения запроса на создание/изменение данных |  -  |
**400** | Некорректно указаны данные в запросе |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_prices**
> ImportAvailability200Response import_prices(import_prices_request)

Обновить цену товаров

В одном запросе можно передать до 1000 товаров. Каждая цена — это отдельный элемент в массиве.  В одном запросе, можно передавать информацию о ценах и акциях в разных магазинах, ограничение составляет до 10 уникальных магазинов.  ***rate-limiting*** - максимальная частота запросов составляет 10 запросов в секунду. В случаях, когда лимит будет превышен, сервер вернёт ошибку с кодом 429. 

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import sm_content_api
from sm_content_api.models.import_availability200_response import ImportAvailability200Response
from sm_content_api.models.import_prices_request import ImportPricesRequest
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.ImportApi(api_client)
    import_prices_request = sm_content_api.ImportPricesRequest() # ImportPricesRequest | 

    try:
        # Обновить цену товаров
        api_response = await api_instance.import_prices(import_prices_request)
        print("The response of ImportApi->import_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_prices_request** | [**ImportPricesRequest**](ImportPricesRequest.md)|  | 

### Return type

[**ImportAvailability200Response**](ImportAvailability200Response.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат выполнения запроса на создание/изменение данных |  -  |
**400** | Некорректно указаны данные в запросе |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_offer_image**
> upload_offer_image(image=image, offer_id=offer_id, position=position)

Загружает изображение товара (оффера)

Загрузка изображения оффера.  Загрузка фотографий должна осуществляться только после того, как была передана информация об офферах.  ***rate-limiting*** - максимальная частота запросов составляет 10 запросов в секунду. В случаях, когда лимит будет превышен, сервер вернёт ошибку с кодом 429.  Необходимо отправить обычный POST запрос с Content-Type multipart/form-data, содержащую файл с картинкой и метаинформацией, описанной ниже. 

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import sm_content_api
from sm_content_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://merchant-api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_content_api.Configuration(
    host = "https://merchant-api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with sm_content_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_content_api.ImportApi(api_client)
    image = None # bytearray | Изображение (optional)
    offer_id = 'offer_id_example' # str | ID оффера (optional)
    position = 56 # int | Позиция (optional)

    try:
        # Загружает изображение товара (оффера)
        await api_instance.upload_offer_image(image=image, offer_id=offer_id, position=position)
    except Exception as e:
        print("Exception when calling ImportApi->upload_offer_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **bytearray**| Изображение | [optional] 
 **offer_id** | **str**| ID оффера | [optional] 
 **position** | **int**| Позиция | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Изображение оффера успешно загружено |  -  |
**400** |  |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

