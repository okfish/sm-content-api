# Offer

Данные о продаваемом товаре

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[Attribute]**](Attribute.md) | Дополнительные атрибуты/параметры товара | [optional] 
**barcodes** | **List[str]** | Штрихкоды для весовых товаров | [optional] 
**categories_ids** | **List[str]** | Массив с идентификаторами категорий к которым относится товар | [optional] 
**description** | **str** | Описание товара | [optional] 
**id** | **str** | Уникальный идентификатор товара в вашей системе | 
**images** | [**List[Image]**](Image.md) | Изображения товара | [optional] 
**items_per_pack** | **int** | Количество товаров в упаковке | [optional] [default to 1]
**name** | **str** | Наиментование товара | 
**pack_type** | **str** | Тип упаковки, допустимые значения: per_item, per_kilo | [optional] [default to 'per_item']
**position** | **int** | Номер сортировки товара/блюда в категории - чем меньше число, тем выше (раньше) отображение на экране пользователя | 
**status** | **str** | Обозначение активности оффера у мерчанта | [default to 'ACTIVE']

## Example

```python
from sm_content_api.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_form_dict = offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


