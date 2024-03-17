# OfferPricePricePromo

Акционная цена товара

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **decimal.Decimal** | Количество (сумма) | 
**currency** | **str** | Валюта в формате ISO-4217 (три большие буквы) | 

## Example

```python
from sm_content_api.models.offer_price_price_promo import OfferPricePricePromo

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPricePricePromo from a JSON string
offer_price_price_promo_instance = OfferPricePricePromo.from_json(json)
# print the JSON string representation of the object
print(OfferPricePricePromo.to_json())

# convert the object into a dict
offer_price_price_promo_dict = offer_price_price_promo_instance.to_dict()
# create an instance of OfferPricePricePromo from a dict
offer_price_price_promo_form_dict = offer_price_price_promo.from_dict(offer_price_price_promo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


