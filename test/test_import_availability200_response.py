# coding: utf-8




import unittest

from sm_content_api.models.import_availability200_response import ImportAvailability200Response

class TestImportAvailability200Response(unittest.TestCase):
    """ImportAvailability200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportAvailability200Response:
        """Test ImportAvailability200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportAvailability200Response`
        """
        model = ImportAvailability200Response()
        if include_optional:
            return ImportAvailability200Response(
                data = sm_content_api.models.import_availability_200_response_data.importAvailability_200_response_data(
                    task_id = 'abc-edf-15', )
            )
        else:
            return ImportAvailability200Response(
                data = sm_content_api.models.import_availability_200_response_data.importAvailability_200_response_data(
                    task_id = 'abc-edf-15', ),
        )
        """

    def testImportAvailability200Response(self):
        """Test ImportAvailability200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
