# Category

Данные о категории товаров

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Уникальный идентификатор категории в вашей системе | 
**name** | **str** | Название категории | 
**parent_id** | **str** | Уникальный идентификатор родительской категории в вашей системе | [optional] 
**position** | **int** | Номер сортировки категории - чем меньше число, тем выше (раньше) она отображается на экране пользователя | 
**status** | **str** | Обозначение активности категории у мерчанта | [optional] [default to 'ACTIVE']

## Example

```python
from sm_content_api.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_form_dict = category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


