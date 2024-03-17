# OfferPrice

Данные о цене товара

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Уникальный идентификатор товара в вашей системе | 
**outlet_id** | **str** | Уникальный идентификатор магазина/ресторана в вашей системе | 
**price** | [**OfferPricePrice**](OfferPricePrice.md) |  | 
**price_promo** | [**OfferPricePricePromo**](OfferPricePricePromo.md) |  | [optional] 
**promo_end_at** | **datetime** | Дата окончания действия акционной цены | [optional] 
**promo_start_at** | **datetime** | Дата начала действия акционной цены | [optional] 
**vat** | **str** | Размер налога на добавленную стоимость (НДС) &lt;br&gt; &#x60;NO_VAT&#x60; - Без НДС &lt;br&gt; &#x60;VAT0&#x60; - НДС 0% &lt;br&gt; &#x60;VAT10&#x60; - НДС 10% &lt;br&gt; &#x60;VAT20&#x60; - НДС 20% &lt;br&gt; | 

## Example

```python
from sm_content_api.models.offer_price import OfferPrice

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPrice from a JSON string
offer_price_instance = OfferPrice.from_json(json)
# print the JSON string representation of the object
print(OfferPrice.to_json())

# convert the object into a dict
offer_price_dict = offer_price_instance.to_dict()
# create an instance of OfferPrice from a dict
offer_price_form_dict = offer_price.from_dict(offer_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


