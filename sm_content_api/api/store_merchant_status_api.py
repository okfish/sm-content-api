# coding: utf-8

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from sm_content_api.models.get_store_merchant_status200_response import GetStoreMerchantStatus200Response

from sm_content_api.api_client import ApiClient, RequestSerialized
from sm_content_api.api_response import ApiResponse
from sm_content_api.rest import RESTResponseType
from sm_content_api.auth import refresh_expired_token

class StoreMerchantStatusApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    @refresh_expired_token()
    async def get_store_merchant_status(
        self,
        retail_chain_slug: Annotated[str, Field(strict=True, description="Человекочитаемый идентификатор торговой сети мерчанта")],
        merchant_store_id: Annotated[StrictStr, Field(description="идентификатор торговой точки мерчанта")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetStoreMerchantStatus200Response:
        """Статус торговой точки, установленный мерчантом

        Запрос на получение статуса торговой точки, установленного мерчантом

        :param retail_chain_slug: Человекочитаемый идентификатор торговой сети мерчанта (required)
        :type retail_chain_slug: str
        :param merchant_store_id: идентификатор торговой точки мерчанта (required)
        :type merchant_store_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_store_merchant_status_serialize(
            retail_chain_slug=retail_chain_slug,
            merchant_store_id=merchant_store_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetStoreMerchantStatus200Response",
            '400': "CommonDataObjectsProblemDetailsV1",
            '422': "CommonDataObjectsProblemDetailsV1",
            '429': "CommonDataObjectsProblemDetailsV1",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_store_merchant_status_with_http_info(
        self,
        retail_chain_slug: Annotated[str, Field(strict=True, description="Человекочитаемый идентификатор торговой сети мерчанта")],
        merchant_store_id: Annotated[StrictStr, Field(description="идентификатор торговой точки мерчанта")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetStoreMerchantStatus200Response]:
        """Статус торговой точки, установленный мерчантом

        Запрос на получение статуса торговой точки, установленного мерчантом

        :param retail_chain_slug: Человекочитаемый идентификатор торговой сети мерчанта (required)
        :type retail_chain_slug: str
        :param merchant_store_id: идентификатор торговой точки мерчанта (required)
        :type merchant_store_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_store_merchant_status_serialize(
            retail_chain_slug=retail_chain_slug,
            merchant_store_id=merchant_store_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetStoreMerchantStatus200Response",
            '400': "CommonDataObjectsProblemDetailsV1",
            '422': "CommonDataObjectsProblemDetailsV1",
            '429': "CommonDataObjectsProblemDetailsV1",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_store_merchant_status_without_preload_content(
        self,
        retail_chain_slug: Annotated[str, Field(strict=True, description="Человекочитаемый идентификатор торговой сети мерчанта")],
        merchant_store_id: Annotated[StrictStr, Field(description="идентификатор торговой точки мерчанта")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Статус торговой точки, установленный мерчантом

        Запрос на получение статуса торговой точки, установленного мерчантом

        :param retail_chain_slug: Человекочитаемый идентификатор торговой сети мерчанта (required)
        :type retail_chain_slug: str
        :param merchant_store_id: идентификатор торговой точки мерчанта (required)
        :type merchant_store_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_store_merchant_status_serialize(
            retail_chain_slug=retail_chain_slug,
            merchant_store_id=merchant_store_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetStoreMerchantStatus200Response",
            '400': "CommonDataObjectsProblemDetailsV1",
            '422': "CommonDataObjectsProblemDetailsV1",
            '429': "CommonDataObjectsProblemDetailsV1",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_store_merchant_status_serialize(
        self,
        retail_chain_slug,
        merchant_store_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if retail_chain_slug is not None:
            _path_params['retail_chain_slug'] = retail_chain_slug
        if merchant_store_id is not None:
            _path_params['merchant_store_id'] = merchant_store_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/retail-chains/{retail_chain_slug}/stores/{merchant_store_id}/merchant-status',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


    @validate_call
    @refresh_expired_token()
    async def put_store_retailer_status(
        self,
        retail_chain_slug: Annotated[str, Field(strict=True, description="Человекочитаемый идентификатор торговой сети мерчанта")],
        merchant_store_id: Annotated[StrictStr, Field(description="идентификатор торговой точки мерчанта")],
        get_store_merchant_status200_response: Annotated[Optional[GetStoreMerchantStatus200Response], Field(description="Запрос на изменение статуса store")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetStoreMerchantStatus200Response:
        """Изменение статуса store мерчантом

        Запрос на изменение статуса торговой точки:  **ACTIVE** -- готова принимать заказы от СберМаркет  **INACTIVE** -- временно не готова принимать заказы от СберМаркет  В структуре **scheduled_change** можно указать планируемое включения или отключения торговой точки  Использовать данный метод мерчант может только при формате работы с Сбермаркет: \"Внешняя сборка\" или \"Внешняя доставка\". 

        :param retail_chain_slug: Человекочитаемый идентификатор торговой сети мерчанта (required)
        :type retail_chain_slug: str
        :param merchant_store_id: идентификатор торговой точки мерчанта (required)
        :type merchant_store_id: str
        :param get_store_merchant_status200_response: Запрос на изменение статуса store
        :type get_store_merchant_status200_response: GetStoreMerchantStatus200Response
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_store_retailer_status_serialize(
            retail_chain_slug=retail_chain_slug,
            merchant_store_id=merchant_store_id,
            get_store_merchant_status200_response=get_store_merchant_status200_response,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetStoreMerchantStatus200Response",
            '400': "CommonDataObjectsProblemDetailsV1",
            '403': None,
            '422': "CommonDataObjectsProblemDetailsV1",
            '429': "CommonDataObjectsProblemDetailsV1",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def put_store_retailer_status_with_http_info(
        self,
        retail_chain_slug: Annotated[str, Field(strict=True, description="Человекочитаемый идентификатор торговой сети мерчанта")],
        merchant_store_id: Annotated[StrictStr, Field(description="идентификатор торговой точки мерчанта")],
        get_store_merchant_status200_response: Annotated[Optional[GetStoreMerchantStatus200Response], Field(description="Запрос на изменение статуса store")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetStoreMerchantStatus200Response]:
        """Изменение статуса store мерчантом

        Запрос на изменение статуса торговой точки:  **ACTIVE** -- готова принимать заказы от СберМаркет  **INACTIVE** -- временно не готова принимать заказы от СберМаркет  В структуре **scheduled_change** можно указать планируемое включения или отключения торговой точки  Использовать данный метод мерчант может только при формате работы с Сбермаркет: \"Внешняя сборка\" или \"Внешняя доставка\". 

        :param retail_chain_slug: Человекочитаемый идентификатор торговой сети мерчанта (required)
        :type retail_chain_slug: str
        :param merchant_store_id: идентификатор торговой точки мерчанта (required)
        :type merchant_store_id: str
        :param get_store_merchant_status200_response: Запрос на изменение статуса store
        :type get_store_merchant_status200_response: GetStoreMerchantStatus200Response
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_store_retailer_status_serialize(
            retail_chain_slug=retail_chain_slug,
            merchant_store_id=merchant_store_id,
            get_store_merchant_status200_response=get_store_merchant_status200_response,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetStoreMerchantStatus200Response",
            '400': "CommonDataObjectsProblemDetailsV1",
            '403': None,
            '422': "CommonDataObjectsProblemDetailsV1",
            '429': "CommonDataObjectsProblemDetailsV1",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def put_store_retailer_status_without_preload_content(
        self,
        retail_chain_slug: Annotated[str, Field(strict=True, description="Человекочитаемый идентификатор торговой сети мерчанта")],
        merchant_store_id: Annotated[StrictStr, Field(description="идентификатор торговой точки мерчанта")],
        get_store_merchant_status200_response: Annotated[Optional[GetStoreMerchantStatus200Response], Field(description="Запрос на изменение статуса store")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Изменение статуса store мерчантом

        Запрос на изменение статуса торговой точки:  **ACTIVE** -- готова принимать заказы от СберМаркет  **INACTIVE** -- временно не готова принимать заказы от СберМаркет  В структуре **scheduled_change** можно указать планируемое включения или отключения торговой точки  Использовать данный метод мерчант может только при формате работы с Сбермаркет: \"Внешняя сборка\" или \"Внешняя доставка\". 

        :param retail_chain_slug: Человекочитаемый идентификатор торговой сети мерчанта (required)
        :type retail_chain_slug: str
        :param merchant_store_id: идентификатор торговой точки мерчанта (required)
        :type merchant_store_id: str
        :param get_store_merchant_status200_response: Запрос на изменение статуса store
        :type get_store_merchant_status200_response: GetStoreMerchantStatus200Response
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_store_retailer_status_serialize(
            retail_chain_slug=retail_chain_slug,
            merchant_store_id=merchant_store_id,
            get_store_merchant_status200_response=get_store_merchant_status200_response,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetStoreMerchantStatus200Response",
            '400': "CommonDataObjectsProblemDetailsV1",
            '403': None,
            '422': "CommonDataObjectsProblemDetailsV1",
            '429': "CommonDataObjectsProblemDetailsV1",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _put_store_retailer_status_serialize(
        self,
        retail_chain_slug,
        merchant_store_id,
        get_store_merchant_status200_response,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if retail_chain_slug is not None:
            _path_params['retail_chain_slug'] = retail_chain_slug
        if merchant_store_id is not None:
            _path_params['merchant_store_id'] = merchant_store_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if get_store_merchant_status200_response is not None:
            _body_params = get_store_merchant_status200_response


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/retail-chains/{retail_chain_slug}/stores/{merchant_store_id}/merchant-status',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


