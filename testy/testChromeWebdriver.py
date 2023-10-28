import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebdriverTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
    def test_spustit(self):
        self.driver.get("http://www.google.com/")
        time.sleep(5)
        self.driver.findElement(By.name("q")).sendKeys("ChromeDriver")
        self.driver.findElement(By.name("q")).submit()
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
