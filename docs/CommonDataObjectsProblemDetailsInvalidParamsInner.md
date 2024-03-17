# CommonDataObjectsProblemDetailsInvalidParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | имя поля | 
**reason** | **str** | текст ошибки валидации поля | 

## Example

```python
from sm_content_api.models.common_data_objects_problem_details_invalid_params_inner import CommonDataObjectsProblemDetailsInvalidParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDataObjectsProblemDetailsInvalidParamsInner from a JSON string
common_data_objects_problem_details_invalid_params_inner_instance = CommonDataObjectsProblemDetailsInvalidParamsInner.from_json(json)
# print the JSON string representation of the object
print(CommonDataObjectsProblemDetailsInvalidParamsInner.to_json())

# convert the object into a dict
common_data_objects_problem_details_invalid_params_inner_dict = common_data_objects_problem_details_invalid_params_inner_instance.to_dict()
# create an instance of CommonDataObjectsProblemDetailsInvalidParamsInner from a dict
common_data_objects_problem_details_invalid_params_inner_form_dict = common_data_objects_problem_details_invalid_params_inner.from_dict(common_data_objects_problem_details_invalid_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


