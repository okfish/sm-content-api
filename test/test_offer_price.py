# coding: utf-8



import datetime
import unittest

import sm_content_api
from sm_content_api.models.offer_price import OfferPrice


class TestOfferPrice(unittest.TestCase):
    """OfferPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfferPrice:
        """Test OfferPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferPrice`
        if include_optional:
            return OfferPrice(
                offer_id = '1001',
                outlet_id = '12',
                price = sm_content_api.models.offer_price_price.OfferPricePrice(
                    amount = '198.99', 
                    currency = 'RUB', ),
                price_promo = sm_content_api.models.offer_price_price_promo.OfferPricePricePromo(
                    amount = '98.99',
                    currency = 'RUB', ),
                promo_end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                promo_start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                vat = 'VAT20'
            )
        else:
            return OfferPrice(
                offer_id = '1001',
                outlet_id = '12',
                price = sm_content_api.models.offer_price_price.OfferPricePrice(
                    amount = '198.99', 
                    currency = 'RUB', ),
                vat = 'VAT20',
        )

    def testOfferPrice(self):
        """Test OfferPrice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        self.assertEqual(inst_req_only.price.amount, '198.99')
        self.assertEqual(inst_req_and_optional.price_promo.amount, '98.99')


if __name__ == '__main__':
    unittest.main()
