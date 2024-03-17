# Option

Опции блюда

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Идентификатор опции/добавки/основы (эта опция должна передаваться ещё как отдельное блюдо/оффер с меткой is_option&#x3D;true) | 
**selected** | **bool** | Включена ли данная опция по умолчанию | 

## Example

```python
from sm_content_api.models.option import Option

# TODO update the JSON string below
json = "{}"
# create an instance of Option from a JSON string
option_instance = Option.from_json(json)
# print the JSON string representation of the object
print(Option.to_json())

# convert the object into a dict
option_dict = option_instance.to_dict()
# create an instance of Option from a dict
option_form_dict = option.from_dict(option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


