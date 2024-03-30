# coding: utf-8




import unittest

import sm_content_api
from sm_content_api.models.import_categories_request import ImportCategoriesRequest


class TestImportCategoriesRequest(unittest.TestCase):
    """ImportCategoriesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportCategoriesRequest:
        """Test ImportCategoriesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included
        """
        if include_optional:
            data = [sm_content_api.models.category.Category(
                    id='100',
                    name='Cheese',
                    parent_id='1',
                    position=1,
                    status='ACTIVE', )
                ]
        else:
            data = [sm_content_api.models.category.Category(
                    id='100',
                    name='Cheese',
                    position=1, )
                ]
        return ImportCategoriesRequest(data=data)

    def testImportCategoriesRequest(self):
        """Test ImportCategoriesRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        # print(inst_req_only.to_str())
        # print(inst_req_and_optional.to_str())
        self.assertEqual(inst_req_only.data[0].id, '100')
        self.assertEqual(inst_req_and_optional.data[0].status, 'ACTIVE')


if __name__ == '__main__':
    unittest.main()
