# coding: utf-8




import unittest

from sm_content_api.models.options_group import OptionsGroup

class TestOptionsGroup(unittest.TestCase):
    """OptionsGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGroup:
        """Test OptionsGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGroup`
        """
        model = OptionsGroup()
        if include_optional:
            return OptionsGroup(
                base_offer_id = '1001',
                id = '100',
                max_amount = 1,
                min_amount = 1,
                name = 'Выберите первое блюдо',
                options = [
                    sm_content_api.models.option.Option(
                        offer_id = '1000', 
                        selected = False, )
                    ]
            )
        else:
            return OptionsGroup(
                base_offer_id = '1001',
                id = '100',
                max_amount = 1,
                min_amount = 1,
                name = 'Выберите первое блюдо',
                options = [
                    sm_content_api.models.option.Option(
                        offer_id = '1000', 
                        selected = False, )
                    ],
        )
        """

    def testOptionsGroup(self):
        """Test OptionsGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
