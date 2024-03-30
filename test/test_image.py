# coding: utf-8




import unittest

from sm_content_api.models.image import Image

class TestImage(unittest.TestCase):
    """Image unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Image:
        """Test Image
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Image`
        """
        model = Image()
        if include_optional:
            return Image(
                name = '1001.jpg',
                url = 'https://yoursite.ru/1001.jpg'
            )
        else:
            return Image(
                name = '1001.jpg',
                url = 'https://yoursite.ru/1001.jpg',
        )
        """

    def testImage(self):
        """Test Image"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
