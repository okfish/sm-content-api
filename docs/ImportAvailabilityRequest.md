# ImportAvailabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Availability]**](Availability.md) | Массив с данными о доступности товаров/блюд | 

## Example

```python
from sm_content_api.models.import_availability_request import ImportAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAvailabilityRequest from a JSON string
import_availability_request_instance = ImportAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print(ImportAvailabilityRequest.to_json())

# convert the object into a dict
import_availability_request_dict = import_availability_request_instance.to_dict()
# create an instance of ImportAvailabilityRequest from a dict
import_availability_request_form_dict = import_availability_request.from_dict(import_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


