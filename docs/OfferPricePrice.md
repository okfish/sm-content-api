# OfferPricePrice

Цена товара

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **decimal.Decimal** | Количество (сумма) | 
**currency** | **str** | Валюта в формате ISO-4217 (три большие буквы) | 

## Example

```python
from sm_content_api.models.offer_price_price import OfferPricePrice

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPricePrice from a JSON string
offer_price_price_instance = OfferPricePrice.from_json(json)
# print the JSON string representation of the object
print(OfferPricePrice.to_json())

# convert the object into a dict
offer_price_price_dict = offer_price_price_instance.to_dict()
# create an instance of OfferPricePrice from a dict
offer_price_price_form_dict = offer_price_price.from_dict(offer_price_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


