# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from sm_content_api.models.common_data_objects_problem_details_invalid_params_inner import CommonDataObjectsProblemDetailsInvalidParamsInner
from typing import Optional, Set
from typing_extensions import Self

class CommonDataObjectsProblemDetails(BaseModel):
    """
    Common data object for describing an error details
    """ # noqa: E501
    detail: Optional[StrictStr] = Field(default=None, description="человекочитаемое описание ошибки, объясняющее причины текущей ситуации возникновения ошибки. Запрещено парсить клиентом, только для пояснения ошибки разработчику")
    invalid_params: Optional[List[CommonDataObjectsProblemDetailsInvalidParamsInner]] = Field(default=None, description="обязательное только для ответа 400. Список ошибок для переданных полей")
    status: Annotated[int, Field(le=599, strict=True, ge=100)] = Field(description="HTTP-код статуса, соответствует соответствующему коду ответа сервера. Нужно для систем")
    title: Annotated[str, Field(min_length=1, strict=True)] = Field(description="человекочитаемое описание сути проблемы, не должно изменяться для различных появлений данной проблемы, за исключением случаев локализации")
    type: Annotated[str, Field(min_length=1, strict=True)] = Field(description="уникальный идентификатор ошибки. Должно коротко, но понятно отражать суть ошибки. На него опирается потребитель(фронтенд) при принятии решения")
    __properties: ClassVar[List[str]] = ["detail", "invalid_params", "status", "title", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CommonDataObjectsProblemDetails from a JSON string"""
        return cls.model_validate_json(json_str)

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in invalid_params (list)
        _items = []
        if self.invalid_params:
            for _item in self.invalid_params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invalid_params'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonDataObjectsProblemDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "detail": obj.get("detail"),
            "invalid_params": [CommonDataObjectsProblemDetailsInvalidParamsInner.from_dict(_item) for _item in obj["invalid_params"]] if obj.get("invalid_params") is not None else None,
            "status": obj.get("status"),
            "title": obj.get("title"),
            "type": obj.get("type")
        })
        return _obj


