from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from parameterized import parameterized


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["init.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = FirefoxOptions()
        options.add_argument("--headless")
        cls.selenium = webdriver.Firefox(options=options)
        cls.selenium.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # test index

    def test_index(self):
        self.selenium.get(f'{self.live_server_url}/')
        response = self.selenium.find_elements(By.TAG_NAME, 'h1')
        self.assertEqual('PySteam', response[0].text)

    def test_bibliotheque_direct(self):
        self.selenium.get(f'{self.live_server_url}/bibliotheques/1')
        jeux_dans_bibliotheque_une = self.selenium.find_elements(By.TAG_NAME, 'li')
        self.assertLessEqual(1, len(jeux_dans_bibliotheque_une))

    # list with id : 1, 1 item
    # list with id : 2, 0 item
    @parameterized.expand([
        (0, 2),
        (1, 2)
    ])
    def test_click_on_first_list(self, list_position, nb_items):
        self.selenium.get(f'{self.live_server_url}/')
        links = self.selenium.find_elements(By.TAG_NAME, 'a')
        links[list_position].click()
        jeux_dans_bibliotheque = self.selenium.find_elements(By.TAG_NAME, 'li')
        self.assertEqual(nb_items, len(jeux_dans_bibliotheque))