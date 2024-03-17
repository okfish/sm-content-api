# ImportPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OfferPrice]**](OfferPrice.md) | Массив с данными цен товаров | 

## Example

```python
from sm_content_api.models.import_prices_request import ImportPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPricesRequest from a JSON string
import_prices_request_instance = ImportPricesRequest.from_json(json)
# print the JSON string representation of the object
print(ImportPricesRequest.to_json())

# convert the object into a dict
import_prices_request_dict = import_prices_request_instance.to_dict()
# create an instance of ImportPricesRequest from a dict
import_prices_request_form_dict = import_prices_request.from_dict(import_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


