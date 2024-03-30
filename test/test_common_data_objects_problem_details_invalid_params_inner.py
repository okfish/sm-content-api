# coding: utf-8




import unittest

from sm_content_api.models.common_data_objects_problem_details_invalid_params_inner import CommonDataObjectsProblemDetailsInvalidParamsInner

class TestCommonDataObjectsProblemDetailsInvalidParamsInner(unittest.TestCase):
    """CommonDataObjectsProblemDetailsInvalidParamsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonDataObjectsProblemDetailsInvalidParamsInner:
        """Test CommonDataObjectsProblemDetailsInvalidParamsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonDataObjectsProblemDetailsInvalidParamsInner`
        """
        model = CommonDataObjectsProblemDetailsInvalidParamsInner()
        if include_optional:
            return CommonDataObjectsProblemDetailsInvalidParamsInner(
                name = 'age',
                reason = 'must be a positive integer'
            )
        else:
            return CommonDataObjectsProblemDetailsInvalidParamsInner(
                name = 'age',
                reason = 'must be a positive integer',
        )
        """

    def testCommonDataObjectsProblemDetailsInvalidParamsInner(self):
        """Test CommonDataObjectsProblemDetailsInvalidParamsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
