# ImportCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Category]**](Category.md) | Массив с данными категорий товаров | 

## Example

```python
from sm_content_api.models.import_categories_request import ImportCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCategoriesRequest from a JSON string
import_categories_request_instance = ImportCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(ImportCategoriesRequest.to_json())

# convert the object into a dict
import_categories_request_dict = import_categories_request_instance.to_dict()
# create an instance of ImportCategoriesRequest from a dict
import_categories_request_form_dict = import_categories_request.from_dict(import_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


