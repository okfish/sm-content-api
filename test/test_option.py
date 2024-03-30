# coding: utf-8




import unittest

from sm_content_api.models.option import Option

class TestOption(unittest.TestCase):
    """Option unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Option:
        """Test Option
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Option`
        """
        model = Option()
        if include_optional:
            return Option(
                offer_id = '1000',
                selected = False
            )
        else:
            return Option(
                offer_id = '1000',
                selected = False,
        )
        """

    def testOption(self):
        """Test Option"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
