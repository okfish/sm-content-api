# coding: utf-8




import unittest

from sm_content_api.models.attribute import Attribute

class TestAttribute(unittest.TestCase):
    """Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attribute:
        """Test Attribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attribute`
        """
        model = Attribute()
        if include_optional:
            return Attribute(
                attribute = '',
                values = [
                    ''
                    ]
            )
        else:
            return Attribute(
                attribute = '',
                values = [
                    ''
                    ],
        )
        """

    def testAttribute(self):
        """Test Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
