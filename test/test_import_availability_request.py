# coding: utf-8




import unittest

from sm_content_api.models.import_availability_request import ImportAvailabilityRequest

class TestImportAvailabilityRequest(unittest.TestCase):
    """ImportAvailabilityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportAvailabilityRequest:
        """Test ImportAvailabilityRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportAvailabilityRequest`
        """
        model = ImportAvailabilityRequest()
        if include_optional:
            return ImportAvailabilityRequest(
                data = [
                    sm_content_api.models.availability.Availability(
                        active = True, 
                        active_from = '2023-02-18', 
                        active_to = '2023-02-18', 
                        intraday_active_from = '09:30:00', 
                        intraday_active_to = '12:00:00', 
                        offer_id = '1001', 
                        outlet_id = '12', )
                    ]
            )
        else:
            return ImportAvailabilityRequest(
                data = [
                    sm_content_api.models.availability.Availability(
                        active = True, 
                        active_from = '2023-02-18', 
                        active_to = '2023-02-18', 
                        intraday_active_from = '09:30:00', 
                        intraday_active_to = '12:00:00', 
                        offer_id = '1001', 
                        outlet_id = '12', )
                    ],
        )
        """

    def testImportAvailabilityRequest(self):
        """Test ImportAvailabilityRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
