# coding: utf-8




import unittest

from sm_content_api.models.get_token200_response import GetToken200Response

class TestGetToken200Response(unittest.TestCase):
    """GetToken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetToken200Response:
        """Test GetToken200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetToken200Response`
        """
        model = GetToken200Response()
        if include_optional:
            return GetToken200Response(
                access_token = '',
                expires_in = 1.337,
                refresh_expires_in = 1.337,
                token_type = 'Bearer',
                not_before_policy = 1.337,
                scopes = ''
            )
        else:
            return GetToken200Response(
                access_token = '',
                expires_in = 1.337,
                token_type = 'Bearer',
                scopes = '',
        )
        """

    def testGetToken200Response(self):
        """Test GetToken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
