# coding: utf-8




import unittest

import sm_content_api
from sm_content_api.models.offer import Offer


class TestOffer(unittest.TestCase):
    """Offer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Offer:
        """Test Offer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included

            "attributes": [
            {
          "attribute": "is_option",
          "values": [
                "false"
          ]
        },
        {
          "attribute": "weight_netto",
          "values": [
            "650"
          ]
        },
        {
          "attribute": "calories_per_100g",
          "values": [
            "326"
          ]
        },
        {
          "attribute": "weight_netto_unit",
          "values": [
            "G"
          ]
        },
        {
          "attribute": "is_excisable",
          "values": [
            "false"
          ]
        },
        {
          "attribute": "ingredients",
          "values": [
            "Классический бургер с     бифштексом из 100% говядины с маринованными огурчиками, рубленым луком, расплавленным     ломтиком сыра, горчицей и кетчупом на мягкой булочке с кунужтом"
          ]
        }

            """
        if include_optional:
            return Offer(
                attributes = [
                    sm_content_api.models.attribute.Attribute(attribute='is_option', values=['false',]),
                    sm_content_api.models.attribute.Attribute(attribute='weight_netto', values=['120',]),
                    sm_content_api.models.attribute.Attribute(attribute='weight_netto_unit', values=['G',]),
                    sm_content_api.models.attribute.Attribute(attribute='is_excisable', values=['false',]),
                    ],
                barcodes = [
                    '4607004890287'
                    ],
                categories_ids = ["10","101","105"],
                description = 'В сыре не просто много, а очень много кусочков натуральной ветчины. Высококачественная натуральная ветчина измельчается на кусочки прямо перед добавлением.',
                id = '1000',
                images = [
                    sm_content_api.models.image.Image(
                        name = '1001.jpg', 
                        url = 'https://yoursite.ru/1001.jpg', )
                    ],
                items_per_pack = 1,
                name = 'Плавленый сыр Hochland с ветчиной 55% 120 г',
                pack_type = 'per_item',
                position = 1,
                status = 'ACTIVE'
            )
        else:
            return Offer(
                id = '1000',
                name = 'Плавленый сыр Hochland с ветчиной 55% 120 г',
                position = 1,
                status = 'ACTIVE',
        )

    def testOffer(self):
        """Test Offer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_only.id, '1000')
        self.assertEqual(inst_req_and_optional.barcodes[0], '4607004890287')


if __name__ == '__main__':
    unittest.main()
