# ImportOffersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Offer]**](Offer.md) | Массив с данными товаров | 

## Example

```python
from sm_content_api.models.import_offers_request import ImportOffersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOffersRequest from a JSON string
import_offers_request_instance = ImportOffersRequest.from_json(json)
# print the JSON string representation of the object
print(ImportOffersRequest.to_json())

# convert the object into a dict
import_offers_request_dict = import_offers_request_instance.to_dict()
# create an instance of ImportOffersRequest from a dict
import_offers_request_form_dict = import_offers_request.from_dict(import_offers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


