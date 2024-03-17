# OptionsGroup

Группа опций (для ресторанов)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_offer_id** | **str** | Идентификатор базового блюда, для которого создаётся группа | 
**id** | **str** | Уникальный идентификатор набора опций | 
**max_amount** | **int** | Максимальное количество опций, которое можно выбрать в рамках группы. 0, если ограничения нет. | 
**min_amount** | **int** | Минимальное количество опций, которое можно выбрать в рамках группы | 
**name** | **str** | Название набора опций | 
**options** | [**List[Option]**](Option.md) | Массив с опциями | 

## Example

```python
from sm_content_api.models.options_group import OptionsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGroup from a JSON string
options_group_instance = OptionsGroup.from_json(json)
# print the JSON string representation of the object
print(OptionsGroup.to_json())

# convert the object into a dict
options_group_dict = options_group_instance.to_dict()
# create an instance of OptionsGroup from a dict
options_group_form_dict = options_group.from_dict(options_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


