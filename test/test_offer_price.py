# coding: utf-8

"""
    Content and Auth API

    Sbermarket API для мерчантов и ресторанов.  Позволяет управлять: - ассортиментом товаров; - меню; - остатками товаров в магазинах; - доступностью блюд; - ценами и акциями на товары и блюда.  Базовый URL для запросов: `https://merchant-api.sbermarket.ru`  API для мерчантов для получения access tokens. # Порядок работы 1. Получить access token, выполнив POST /auth/token по oAuth 2.0 flow (client credentials)

    The version of the OpenAPI document: 0.0.2a
    Contact: merchant.api@sbermarket.ru
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sm_content_api.models.offer_price import OfferPrice

class TestOfferPrice(unittest.TestCase):
    """OfferPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfferPrice:
        """Test OfferPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferPrice`
        """
        model = OfferPrice()
        if include_optional:
            return OfferPrice(
                offer_id = '1001',
                outlet_id = '12',
                price = sm_content_api.models.offer_price_price.OfferPrice_price(
                    amount = '198.99', 
                    currency = 'RUB', ),
                price_promo = sm_content_api.models.offer_price_price_promo.OfferPrice_price_promo(
                    amount = '198.99', 
                    currency = 'RUB', ),
                promo_end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                promo_start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                vat = 'VAT20'
            )
        else:
            return OfferPrice(
                offer_id = '1001',
                outlet_id = '12',
                price = sm_content_api.models.offer_price_price.OfferPrice_price(
                    amount = '198.99', 
                    currency = 'RUB', ),
                vat = 'VAT20',
        )
        """

    def testOfferPrice(self):
        """Test OfferPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
