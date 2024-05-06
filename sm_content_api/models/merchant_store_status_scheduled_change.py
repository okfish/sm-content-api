# coding: utf-8

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class MerchantStoreStatusScheduledChange(BaseModel):
    """
    Информация о планируемом изменении статуса торговой точки
    """ # noqa: E501
    change_at: datetime = Field(description="Дата и время (в формате RFC 3339) запланированного изменения статуса торговой точки ")
    status: StrictStr = Field(description="Статус store:  **ACTIVE** - доступен для заказов.  **INACTIVE** - временно не доступен для заказов. При этом, торговая точка отображается в результатах поиска с подписью о временной недоступности для заказов.  **DISCONNECTED** - отключен от системы СберМаркет. В этом случае торговая точка не отображается в результатах поиска на витрине СМ.  **PAUSED** - временно недоступен для заказов. В этом случае торговая точка отображается в результатах поиска на витрине СМ, но окна доставки отключаются до указанного времени. ")
    __properties: ClassVar[List[str]] = ["change_at", "status"]

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
        """Create an instance of MerchantStoreStatusScheduledChange from a JSON string"""
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
        """Create an instance of MerchantStoreStatusScheduledChange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "change_at": obj.get("change_at"),
            "status": obj.get("status")
        })
        return _obj


