# coding: utf-8




import unittest

from sm_content_api.models.common_data_objects_problem_details import CommonDataObjectsProblemDetails

class TestCommonDataObjectsProblemDetails(unittest.TestCase):
    """CommonDataObjectsProblemDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonDataObjectsProblemDetails:
        """Test CommonDataObjectsProblemDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonDataObjectsProblemDetails`
        """
        model = CommonDataObjectsProblemDetails()
        if include_optional:
            return CommonDataObjectsProblemDetails(
                detail = 'Basket must have more then 1 item',
                invalid_params = [
                    sm_content_api.models.common_data_objects_problem_details_invalid_params_inner.CommonDataObjectsProblemDetails_invalid_params_inner(
                        name = 'age', 
                        reason = 'must be a positive integer', )
                    ],
                status = 400,
                title = 'Your request parameters didn't validate',
                type = 'validation-error'
            )
        else:
            return CommonDataObjectsProblemDetails(
                status = 400,
                title = 'Your request parameters didn't validate',
                type = 'validation-error',
        )
        """

    def testCommonDataObjectsProblemDetails(self):
        """Test CommonDataObjectsProblemDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
