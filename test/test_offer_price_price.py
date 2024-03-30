# coding: utf-8




import unittest

from sm_content_api.models.offer_price_price import OfferPricePrice

class TestOfferPricePrice(unittest.TestCase):
    """OfferPricePrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfferPricePrice:
        """Test OfferPricePrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferPricePrice`
        """
        model = OfferPricePrice()
        if include_optional:
            return OfferPricePrice(
                amount = '198.99',
                currency = 'RUB'
            )
        else:
            return OfferPricePrice(
                amount = '198.99',
                currency = 'RUB',
        )
        """

    def testOfferPricePrice(self):
        """Test OfferPricePrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
