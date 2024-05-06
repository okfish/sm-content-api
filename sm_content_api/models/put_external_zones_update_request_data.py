# coding: utf-8

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from sm_content_api.models.zone_coordinates import ZoneCoordinates
from typing import Optional, Set
from typing_extensions import Self

class PutExternalZonesUpdateRequestData(BaseModel):
    """
    PutExternalZonesUpdateRequestData
    """ # noqa: E501
    coordinates: Optional[List[ZoneCoordinates]] = None
    status: Optional[StrictBool] = Field(default=None, description="Включена зона или выключена")
    __properties: ClassVar[List[str]] = ["coordinates", "status"]

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
        """Create an instance of PutExternalZonesUpdateRequestData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in coordinates (list)
        _items = []
        if self.coordinates:
            for _item in self.coordinates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['coordinates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PutExternalZonesUpdateRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "coordinates": [ZoneCoordinates.from_dict(_item) for _item in obj["coordinates"]] if obj.get("coordinates") is not None else None,
            "status": obj.get("status")
        })
        return _obj


