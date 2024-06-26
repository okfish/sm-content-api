# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
# import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from sm_content_api.models.attribute import Attribute
from sm_content_api.models.image import Image
from typing import Optional, Set
from typing_extensions import Self

class Offer(BaseModel):
    """
    Данные о продаваемом товаре
    """ # noqa: E501
    attributes: Optional[List[Attribute]] = Field(default=None, description="Дополнительные атрибуты/параметры товара")
    barcodes: Optional[List[StrictStr]] = Field(default=None, description="Штрихкоды для весовых товаров")
    categories_ids: Optional[List[StrictStr]] = Field(default=None, description="Массив с идентификаторами категорий к которым относится товар")
    description: Optional[StrictStr] = Field(default=None, description="Описание товара")
    id: StrictStr = Field(description="Уникальный идентификатор товара в вашей системе")
    images: Optional[List[Image]] = Field(default=None, description="Изображения товара")
    items_per_pack: Optional[StrictInt] = Field(default=1, description="Количество товаров в упаковке")
    name: StrictStr = Field(description="Наиментование товара")
    pack_type: Optional[StrictStr] = Field(default='per_item', description="Тип упаковки, допустимые значения: per_item, per_kilo")
    position: StrictInt = Field(description="Номер сортировки товара/блюда в категории - чем меньше число, тем выше (раньше) отображение на экране пользователя")
    status: StrictStr = Field(description="Обозначение активности оффера у мерчанта")
    __properties: ClassVar[List[str]] = ["attributes", "barcodes", "categories_ids", "description", "id", "images", "items_per_pack", "name", "pack_type", "position", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACTIVE', 'INACTIVE']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE')")
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
        """Create an instance of Offer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Offer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributes": [Attribute.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "barcodes": obj.get("barcodes"),
            "categories_ids": obj.get("categories_ids"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "images": [Image.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "items_per_pack": obj.get("items_per_pack") if obj.get("items_per_pack") is not None else 1,
            "name": obj.get("name"),
            "pack_type": obj.get("pack_type") if obj.get("pack_type") is not None else 'per_item',
            "position": obj.get("position"),
            "status": obj.get("status") if obj.get("status") is not None else 'ACTIVE'
        })
        return _obj


