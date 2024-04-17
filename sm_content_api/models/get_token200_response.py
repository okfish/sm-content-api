# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GetToken200Response(BaseModel):
    """
    GetToken200Response
    """ # noqa: E501
    access_token: StrictStr
    expires_in: Union[StrictFloat, StrictInt]
    refresh_expires_in: Optional[Union[StrictFloat, StrictInt]] = None
    token_type: StrictStr
    not_before_policy: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="not-before-policy")
    scopes: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["access_token", "expires_in", "refresh_expires_in", "token_type", "not-before-policy", "scopes"]

    @field_validator('token_type')
    def token_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Bearer']):
            raise ValueError("must be one of enum values ('Bearer')")
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
        """Create an instance of GetToken200Response from a JSON string"""
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
        """Create an instance of GetToken200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_token": obj.get("access_token"),
            "expires_in": obj.get("expires_in"),
            "refresh_expires_in": obj.get("refresh_expires_in"),
            "token_type": obj.get("token_type"),
            "not-before-policy": obj.get("not-before-policy"),
            "scopes": obj.get("scopes")
        })
        return _obj


