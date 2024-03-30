# coding: utf-8




import unittest
from dotenv import dotenv_values

import sm_content_api as smc


config = smc.configuration.Configuration()

credentials = dotenv_values("../.env.test")

access_token_expired = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyOVFtNGxOV293N1JVei1wRVZvbnktTkU1YkhibVZhdXExZWF5SlBmdlBRIn0.eyJleHAiOjE3MTA2OTQwOTIsImlhdCI6MTcxMDY5Mzc5MiwianRpIjoiMGJjZGM2NTMtOWNjYi00YmUwLWI4ZjctZmRkNGVlY2FmNzVlIiwiaXNzIjoiaHR0cHM6Ly9tZXJjaGFudC1hcGkuc2Jlcm1hcmtldC5ydS9hdXRoL3JlYWxtcy9tZXJjaGFudC1zZXJ2aWNlIiwic3ViIjoiYWY5NmIzNjgtMmIyYi00MTE2LWJlMmItYWU3MzkwMDhiYjllIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoicmV0YWlsZXJfZm9vZDRnb29kIiwic2NvcGUiOiIiLCJjbGllbnRIb3N0IjoiMTg4LjE2Mi42NC4xMzIiLCJjbGllbnRJZCI6InJldGFpbGVyX2Zvb2Q0Z29vZCIsInJldGFpbGVyX2lkIjoiMjE1ODYiLCJjbGllbnRBZGRyZXNzIjoiMTg4LjE2Mi42NC4xMzIifQ.UX_uVPL_iLZr3XCC8eiMNqk3_mailfTGo7k211ME-CEsd1lZeoGDIIpfA8TAVLVN-E-vjVIWswCKHPZNXC6oCcyxkyuUp80VfUfzI8gIAPtXyhbjOVNq4ecEPiImRndQlwSBfKT6Oy0kUk605Y4skOOt9WYGLpbOgSdXv7Yg6W--GVH7-mROtrqra_PASoItJVpunf7u1mYVuGykxmnfQywRCzIMgTUJh5pQuiFr_jrGXSYWf_3zzDrmv4YdKSKwom4cC1EU3hLfTHOVc498X_U8W4C4DJ1Un6atr0I2MXDmLypYuxO8TKGE7394PB-eR8GxWhKVjup9MsvyaVbb8w'

config.access_token = access_token_expired
config.retries = 3  # this enables aiohttp_retry client
config.client_id = credentials['CLIENT_ID']  # str |
config.client_secret = credentials['CLIENT_SECRET']  # str |
config.grant_type = credentials['GRANT_TYPE']  # str |

IMG_URL_PREFIX = credentials.get('IMG_URL_PREFIX', "https://example.org/")


class TestImportApi(unittest.IsolatedAsyncioTestCase):
    """ImportApi unit test stubs"""

    def setUp(self) -> None:
        self.client = smc.ApiClient(config)
        self.api = smc.ImportApi(self.client)

    async def asyncTearDown(self) -> None:
        await self.client.close()

    async def test_import_availability(self) -> None:
        """Test case for import_availability

        Указать доступность товаров/блюд
        """
        pass

    async def test_import_categories(self) -> None:
        """Test case for import_categories

        Создать или обновить категорию товаров
        """
        test_cat_parent = smc.models.Category(id='1889',
                                              name='Суши',
                                              position=1,
                                              status='ACTIVE')
        test_cat_parent_2 = smc.models.Category(id='1934',
                                              name='Роллы',
                                              position=2,
                                              status='ACTIVE')
        test_cat_child = smc.models.Category(id='1891',
                                             name='Фирменные роллы',
                                             parent_id='1934',
                                             position=1,
                                             status='INACTIVE')

        req = smc.models.ImportCategoriesRequest(data=[test_cat_parent, test_cat_child, test_cat_parent_2])
        print(req)

        api_response = None

        try:
            # Import categories
            api_response = await self.api.import_categories(req)
        except smc.ApiException as e:
            print("Exception when calling ImportApi->import_categories: %s\n" % e)

        self.assertIsInstance(api_response, smc.models.ImportAvailability200Response)
        self.assertGreater(len(api_response.data.task_id), 1)

        print(api_response.to_str())

    async def test_import_offers(self) -> None:
        """Test case for import_offers

        Создать или обновить товар
        """
        test_offer_1 = smc.Offer(categories_ids=["1891"],
                                 description='снежный краб в остром соусе',
                                 id='24141',
                                 images=[
                                     smc.Image(
                                         name='node_351.jpg',
                                         url=f'{IMG_URL_PREFIX}images/node_351.jpg', )
                                     ],
                                 attributes=[
                                     smc.Attribute(attribute='is_option', values=['false',]),
                                     smc.Attribute(attribute='weight_netto', values=['160',]),
                                     smc.Attribute(attribute='weight_netto_unit', values=['G',]),
                                     smc.Attribute(attribute='is_excisable', values=['false',]),
                                     smc.Attribute(attribute='calories_per_portion', values=['321',]),
                                     smc.Attribute(attribute='fats_per_portion', values=['11',]),
                                     smc.Attribute(attribute='proteins_per_portion', values=['9',]),
                                     smc.Attribute(attribute='carbohydrates_per_portion', values=['48',]),
                                     smc.Attribute(attribute='ingredients', values=['снежный краб в остром соусе',]),
                                 ],
                                 items_per_pack=1,
                                 name='Острый краб',
                                 position=1,
                                 status='ACTIVE')

        test_offer_2 = smc.Offer(categories_ids=["1889"],
                               description='японский омлет',
                               id='24107',
                               images=[
                                   smc.Image(
                                       name='node_102.jpg',
                                       url=f'{IMG_URL_PREFIX}images/node_102.jpg', )
                                   ],
                               attributes=[
                                     smc.Attribute(attribute='is_option', values=['false', ]),
                                     smc.Attribute(attribute='weight_netto', values=['89', ]),
                                     smc.Attribute(attribute='weight_netto_unit', values=['G', ]),
                                     smc.Attribute(attribute='is_excisable', values=['false', ]),
                                     smc.Attribute(attribute='calories_per_portion', values=['89', ]),
                                     smc.Attribute(attribute='fats_per_portion', values=['4', ]),
                                     smc.Attribute(attribute='proteins_per_portion', values=['3', ]),
                                     smc.Attribute(attribute='carbohydrates_per_portion', values=['10', ]),
                                     smc.Attribute(attribute='ingredients', values=['японский омлет', ]),
                                 ],
                               items_per_pack=1,
                               name='Суши с японским омлетом',
                               position=1,
                               status='ACTIVE')

        req = smc.ImportOffersRequest(data=[test_offer_1, test_offer_2])
        print(req)

        api_response = None

        try:
            # Import offers
            api_response = await self.api.import_offers(req)
        except smc.ApiException as e:
            print("Exception when calling ImportApi->import_offers: %s\n" % e)

        self.assertIsInstance(api_response, smc.models.ImportAvailability200Response)
        self.assertGreater(len(api_response.data.task_id), 1)

        print(api_response.to_str())

    async def test_import_options_groups(self) -> None:
        """Test case for import_options_groups

        Создать или обновить наборы опций блюд (для ресторанов)
        """
        pass

    async def test_import_prices(self) -> None:
        """Test case for import_prices

        Обновить цену товаров
        """
        req = smc.ImportPricesRequest(
                data=[
                    smc.OfferPrice(
                        offer_id='24107',
                        outlet_id='888',
                        price=smc.OfferPricePrice(
                            amount='69',
                            currency='RUB', ),
                        vat='NO_VAT'),
                    smc.OfferPrice(
                        offer_id='24141',
                        outlet_id='888',
                        price=smc.OfferPricePrice(
                            amount='195',
                            currency='RUB', ),
                        vat='NO_VAT'),
                    ],
            )
        print(req)

        api_response = None

        try:
            # Import prices
            api_response = await self.api.import_prices(req)
        except smc.ApiException as e:
            print("Exception when calling ImportApi->import_prices: %s\n" % e)

        self.assertIsInstance(api_response, smc.models.ImportAvailability200Response)
        self.assertGreater(len(api_response.data.task_id), 1)

        print(api_response.to_str())

    async def test_import_stocks(self) -> None:
        """Test case for import_stocks

        Обновить остатки товаров
        """
        req = smc.ImportStocksRequest(
                data=[
                    smc.Stock(
                        offer_id='24107',
                        outlet_id='888',
                        stock='100', ),
                    smc.Stock(
                        offer_id='24141',
                        outlet_id='888',
                        stock='100', ),
                    ],
                )
        print(req)

        api_response = None

        try:
            # Import prices
            api_response = await self.api.import_stocks(req)
        except smc.ApiException as e:
            print("Exception when calling ImportApi->import_stocks: %s\n" % e)

        self.assertIsInstance(api_response, smc.models.ImportAvailability200Response)
        self.assertGreater(len(api_response.data.task_id), 1)

        print(api_response.to_str())

    async def test_upload_offer_image(self) -> None:
        """Test case for upload_offer_image

        Загружает изображение товара (оффера)
        """
        pass


if __name__ == '__main__':
    unittest.main()
