# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from sm_content_api.models.option import Option
from typing import Optional, Set
from typing_extensions import Self

class OptionsGroup(BaseModel):
    """
    Группа опций (для ресторанов)
    """ # noqa: E501
    base_offer_id: StrictStr = Field(description="Идентификатор базового блюда, для которого создаётся группа")
    id: StrictStr = Field(description="Уникальный идентификатор набора опций")
    max_amount: StrictInt = Field(description="Максимальное количество опций, которое можно выбрать в рамках группы. 0, если ограничения нет.")
    min_amount: StrictInt = Field(description="Минимальное количество опций, которое можно выбрать в рамках группы")
    name: StrictStr = Field(description="Название набора опций")
    options: List[Option] = Field(description="Массив с опциями")
    __properties: ClassVar[List[str]] = ["base_offer_id", "id", "max_amount", "min_amount", "name", "options"]

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
        """Create an instance of OptionsGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OptionsGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base_offer_id": obj.get("base_offer_id"),
            "id": obj.get("id"),
            "max_amount": obj.get("max_amount"),
            "min_amount": obj.get("min_amount"),
            "name": obj.get("name"),
            "options": [Option.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None
        })
        return _obj


