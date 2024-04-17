# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self


class Stock(BaseModel):
    """
    Данные об остатках товара
    """ # noqa: E501
    offer_id: StrictStr = Field(description="Идентификатор товара в вашей системе")
    outlet_id: StrictStr = Field(description="Идентификатор магазина/ресторана в вашей системе")
    stock: StrictStr = Field(description="Доступный для продажи остаток товаров")
    __properties: ClassVar[List[str]] = ["offer_id", "outlet_id", "stock"]

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
        """Create an instance of Stock from a JSON string"""
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
        """Create an instance of Stock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offer_id": obj.get("offer_id"),
            "outlet_id": obj.get("outlet_id"),
            "stock": obj.get("stock")
        })
        return _obj


