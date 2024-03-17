# sm_content_api.AuthenticationApi

All URIs are relative to *https://merchant-api.sbermarket.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](AuthenticationApi.md#get_token) | **POST** /auth/token | Получение JWT токена


# **get_token**
> GetToken200Response get_token(client_id, client_secret, grant_type)

Получение JWT токена

Запрос на получение JWT токена

### Example


```python
import sm_content_api
from sm_content_api.models.get_token200_response import GetToken200Response
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
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **grant_type** | **str**|  | 

### Return type

[**GetToken200Response**](GetToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешное создание получение токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

