# coding: utf-8

"""
    Content and Auth API

    Sbermarket API для мерчантов и ресторанов.  Позволяет управлять: - ассортиментом товаров; - меню; - остатками товаров в магазинах; - доступностью блюд; - ценами и акциями на товары и блюда.  Базовый URL для запросов: `https://merchant-api.sbermarket.ru`  API для мерчантов для получения access tokens. # Порядок работы 1. Получить access token, выполнив POST /auth/token по oAuth 2.0 flow (client credentials)

    The version of the OpenAPI document: 0.0.2a
    Contact: merchant.api@sbermarket.ru
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class Option(BaseModel):
    """
    Опции блюда
    """ # noqa: E501
    offer_id: StrictStr = Field(description="Идентификатор опции/добавки/основы (эта опция должна передаваться ещё как отдельное блюдо/оффер с меткой is_option=true)")
    selected: StrictBool = Field(description="Включена ли данная опция по умолчанию")
    __properties: ClassVar[List[str]] = ["offer_id", "selected"]

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
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Option from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
        """Create an instance of Option from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offer_id": obj.get("offer_id"),
            "selected": obj.get("selected")
        })
        return _obj


