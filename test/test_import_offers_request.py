# coding: utf-8




import unittest

import sm_content_api
from sm_content_api.models.import_offers_request import ImportOffersRequest


class TestImportOffersRequest(unittest.TestCase):
    """ImportOffersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportOffersRequest:
        """Test ImportOffersRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportOffersRequest`
        if include_optional:
            return ImportOffersRequest(
                data = [
                    sm_content_api.models.offer.Offer(
                        attributes = [
                            sm_content_api.models.attribute.Attribute(
                                attribute = '', 
                                values = [
                                    ''
                                    ], )
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
                        status = 'ACTIVE', )
                    ]
            )
        else:
            return ImportOffersRequest(
                data = [
                    sm_content_api.models.offer.Offer(
                        id = '1000',
                        name = 'Плавленый сыр Hochland с ветчиной 55% 120 г',
                        position = 1,
                        status = 'ACTIVE', )
                    ],
            )

    def testImportOffersRequest(self):
        """Test ImportOffersRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        self.assertEqual(inst_req_only.data[0].id, '1000')
        self.assertEqual(inst_req_and_optional.data[0].items_per_pack, 1)


if __name__ == '__main__':
    unittest.main()
