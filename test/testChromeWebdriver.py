import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebdriverTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        print("Driver created.")

    def test_spustit(self):
        self.driver.get("http://www.google.com/")
        time.sleep(5)
        print(f"URL {self.driver.current_url}, page title {self.driver.title}")
        self.assertEqual("Google", self.driver.title)
        elem = self.driver.find_element(By.NAME, "q") # now the ID is different
        elem.send_keys("ChromeDriver")
        elem.submit()
        time.sleep(3)
        print(f"URL {self.driver.current_url}, page title {self.driver.title}")
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
