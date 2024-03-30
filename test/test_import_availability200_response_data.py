# coding: utf-8




import unittest

from sm_content_api.models.import_availability200_response_data import ImportAvailability200ResponseData

class TestImportAvailability200ResponseData(unittest.TestCase):
    """ImportAvailability200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportAvailability200ResponseData:
        """Test ImportAvailability200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportAvailability200ResponseData`
        """
        model = ImportAvailability200ResponseData()
        if include_optional:
            return ImportAvailability200ResponseData(
                task_id = 'abc-edf-15'
            )
        else:
            return ImportAvailability200ResponseData(
                task_id = 'abc-edf-15',
        )
        """

    def testImportAvailability200ResponseData(self):
        """Test ImportAvailability200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
