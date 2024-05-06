# coding: utf-8

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sm_content_api.models.store_location import StoreLocation
from sm_content_api.models.store_sm_status import StoreSmStatus
from typing import Optional, Set
from typing_extensions import Self

class Store(BaseModel):
    """
    Информация о торговой точке, включающая идентификаторы в разных системах (СберМаркет, Мерчант), адрес и статус торговой точки на витрине СберМаркета
    """ # noqa: E501
    assembly_type: Optional[StrictStr] = Field(default=None, description="Тип сборки:  **EXTERNAL**: сборка выполняется мерчантом  **BY_SBERMARKET**: сборка выполняется СберМаркетом ")
    hook_type: Optional[StrictStr] = Field(default=None, description="Тип Хука:  **IMMEDIATELY**: Хук выполняется сразу после создания  **LATER**: Хук выполняется в день доставки  **BEFORE**: Хук выполняется перед началом слота ")
    id: StrictStr = Field(description="Уникальный идентификатор торговой точки в СберМаркете")
    integration_kind: StrictStr = Field(description="Тип интеграции торговой точки со СберМаркетом:  **ASSEMBLY_BY_MERCHANT_DELIVERY_BY_MERCHANT**: сборка и доставка выполняются мерчантом  **ASSEMBLY_BY_MERCHANT_DELIVERY_BY_SM**: сборка выполняется мерчантом; доставка выполняется СберМаркетом  **ASSEMBLY_BY_SM_DELIVERY_BY_SM**: сборка и доставка выполняются СберМаркетом ")
    location: StoreLocation
    merchant_store_id: Optional[StrictStr] = Field(default=None, description="Идентификатор торговой точки мерчанта")
    sm_status: StoreSmStatus
    __properties: ClassVar[List[str]] = ["assembly_type", "hook_type", "id", "integration_kind", "location", "merchant_store_id", "sm_status"]

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
        """Create an instance of Store from a JSON string"""
        return cls.model_validate_json(json_str)

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sm_status
        if self.sm_status:
            _dict['sm_status'] = self.sm_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Store from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assembly_type": obj.get("assembly_type"),
            "hook_type": obj.get("hook_type"),
            "id": obj.get("id"),
            "integration_kind": obj.get("integration_kind"),
            "location": StoreLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "merchant_store_id": obj.get("merchant_store_id"),
            "sm_status": StoreSmStatus.from_dict(obj["sm_status"]) if obj.get("sm_status") is not None else None
        })
        return _obj


