# ImportOptionsGroupsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OptionsGroup]**](OptionsGroup.md) | Массив с данными наборов опций блюд (для ресторанов) | 

## Example

```python
from sm_content_api.models.import_options_groups_request import ImportOptionsGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOptionsGroupsRequest from a JSON string
import_options_groups_request_instance = ImportOptionsGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(ImportOptionsGroupsRequest.to_json())

# convert the object into a dict
import_options_groups_request_dict = import_options_groups_request_instance.to_dict()
# create an instance of ImportOptionsGroupsRequest from a dict
import_options_groups_request_form_dict = import_options_groups_request.from_dict(import_options_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


