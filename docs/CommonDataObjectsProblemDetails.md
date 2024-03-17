# CommonDataObjectsProblemDetails

Common data object for describing an error details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | человекочитаемое описание ошибки, объясняющее причины текущей ситуации возникновения ошибки. Запрещено парсить клиентом, только для пояснения ошибки разработчику | [optional] 
**invalid_params** | [**List[CommonDataObjectsProblemDetailsInvalidParamsInner]**](CommonDataObjectsProblemDetailsInvalidParamsInner.md) | обязательное только для ответа 400. Список ошибок для переданных полей | [optional] 
**status** | **int** | HTTP-код статуса, соответствует соответствующему коду ответа сервера. Нужно для систем | 
**title** | **str** | человекочитаемое описание сути проблемы, не должно изменяться для различных появлений данной проблемы, за исключением случаев локализации | 
**type** | **str** | уникальный идентификатор ошибки. Должно коротко, но понятно отражать суть ошибки. На него опирается потребитель(фронтенд) при принятии решения | 

## Example

```python
from sm_content_api.models.common_data_objects_problem_details import CommonDataObjectsProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDataObjectsProblemDetails from a JSON string
common_data_objects_problem_details_instance = CommonDataObjectsProblemDetails.from_json(json)
# print the JSON string representation of the object
print(CommonDataObjectsProblemDetails.to_json())

# convert the object into a dict
common_data_objects_problem_details_dict = common_data_objects_problem_details_instance.to_dict()
# create an instance of CommonDataObjectsProblemDetails from a dict
common_data_objects_problem_details_form_dict = common_data_objects_problem_details.from_dict(common_data_objects_problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


