# ImportAvailability200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ImportAvailability200ResponseData**](ImportAvailability200ResponseData.md) |  | 

## Example

```python
from sm_content_api.models.import_availability200_response import ImportAvailability200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAvailability200Response from a JSON string
import_availability200_response_instance = ImportAvailability200Response.from_json(json)
# print the JSON string representation of the object
print(ImportAvailability200Response.to_json())

# convert the object into a dict
import_availability200_response_dict = import_availability200_response_instance.to_dict()
# create an instance of ImportAvailability200Response from a dict
import_availability200_response_form_dict = import_availability200_response.from_dict(import_availability200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


