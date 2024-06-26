# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Category(BaseModel):
    """
    Данные о категории товаров
    """ # noqa: E501
    id: StrictStr = Field(description="Уникальный идентификатор категории в вашей системе")
    name: StrictStr = Field(description="Название категории")
    parent_id: Optional[StrictStr] = Field(default=None, description="Уникальный идентификатор родительской категории в вашей системе")
    position: StrictInt = Field(description="Номер сортировки категории - чем меньше число, тем выше (раньше) она отображается на экране пользователя")
    status: Optional[StrictStr] = Field(default='ACTIVE', description="Обозначение активности категории у мерчанта")
    __properties: ClassVar[List[str]] = ["id", "name", "parent_id", "position", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'INACTIVE', 'DELETE']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'DELETE')")
        return value

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
        """Create an instance of Category from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Category from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "parent_id": obj.get("parent_id"),
            "position": obj.get("position"),
            "status": obj.get("status") if obj.get("status") is not None else 'ACTIVE'
        })
        return _obj


