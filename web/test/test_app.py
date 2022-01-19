import unittest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class AppTest(unittest.TestCase):

    def setUp(self):
        s = Service("./chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_browser_show_homepage_with_image(self):
        b = self.driver.find_element(
            By.CSS_SELECTOR,
            f'[data-test-id="image-homepage"]')
        self.assertIsNotNone(b)
