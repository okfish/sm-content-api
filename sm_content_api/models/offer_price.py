# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from sm_content_api.models.offer_price_price import OfferPricePrice
from sm_content_api.models.offer_price_price_promo import OfferPricePricePromo
from typing import Optional, Set
from typing_extensions import Self

class OfferPrice(BaseModel):
    """
    Данные о цене товара
    """ # noqa: E501
    offer_id: StrictStr = Field(description="Уникальный идентификатор товара в вашей системе")
    outlet_id: StrictStr = Field(description="Уникальный идентификатор магазина/ресторана в вашей системе")
    price: OfferPricePrice
    price_promo: Optional[OfferPricePricePromo] = None
    promo_end_at: Optional[datetime] = Field(default=None, description="Дата окончания действия акционной цены")
    promo_start_at: Optional[datetime] = Field(default=None, description="Дата начала действия акционной цены")
    vat: StrictStr = Field(description="Размер налога на добавленную стоимость (НДС) <br> `NO_VAT` - Без НДС <br> `VAT0` - НДС 0% <br> `VAT10` - НДС 10% <br> `VAT20` - НДС 20% <br>")
    __properties: ClassVar[List[str]] = ["offer_id", "outlet_id", "price", "price_promo", "promo_end_at", "promo_start_at", "vat"]

    @field_validator('vat')
    def vat_validate_enum(cls, value):
        """Validates the enum"""
        if value not in {'NO_VAT', 'VAT0', 'VAT10', 'VAT20'}:
            raise ValueError("must be one of enum values ('NO_VAT', 'VAT0', 'VAT10', 'VAT20')")
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
        """Create an instance of OfferPrice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price_promo
        if self.price_promo:
            _dict['price_promo'] = self.price_promo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OfferPrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offer_id": obj.get("offer_id"),
            "outlet_id": obj.get("outlet_id"),
            "price": OfferPricePrice.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "price_promo": OfferPricePricePromo.from_dict(obj["price_promo"]) if obj.get("price_promo") is not None else None,
            "promo_end_at": obj.get("promo_end_at"),
            "promo_start_at": obj.get("promo_start_at"),
            "vat": obj.get("vat")
        })
        return _obj


