# Availability

Данные о доступности товара/блюда

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Данные о доступности товара | 
**active_from** | **str** | Дата начала действия записи о доступности | [optional] 
**active_to** | **str** | Дата начала действия записи о доступности | [optional] 
**intraday_active_from** | **str** | Начало ограничения доступности по времени внутри дня (Например товары для завтрака) | [optional] 
**intraday_active_to** | **str** | Конец ограничения доступности по времени внутри дня (Например товары для завтрака) | [optional] 
**offer_id** | **str** | Уникальный идентификатор товара в вашей системе | 
**outlet_id** | **str** | Уникальный идентификатор магазина/ресторана в вашей системе | 

## Example

```python
from sm_content_api.models.availability import Availability

# TODO update the JSON string below
json = "{}"
# create an instance of Availability from a JSON string
availability_instance = Availability.from_json(json)
# print the JSON string representation of the object
print(Availability.to_json())

# convert the object into a dict
availability_dict = availability_instance.to_dict()
# create an instance of Availability from a dict
availability_form_dict = availability.from_dict(availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


