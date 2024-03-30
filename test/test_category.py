# coding: utf-8




import unittest

from sm_content_api.models.category import Category


class TestCategory(unittest.TestCase):
    """Category unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Category:
        """Test Category
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Category`
        if include_optional:
            return Category(
                id = '100',
                name = 'Сыры',
                parent_id = '1',
                position = 1,
                status = 'ACTIVE'
            )
        else:
            return Category(
                id = '100',
                name = 'Сыры',
                position = 1,
        )

    def testCategory(self):
        """Test Category"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_only.id, '100')
        self.assertEqual(inst_req_and_optional.status, 'ACTIVE')


if __name__ == '__main__':
    unittest.main()
