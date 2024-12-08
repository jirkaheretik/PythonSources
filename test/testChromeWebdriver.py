import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class WebdriverTestCase(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(chrome_options)
        print("Driver created.")
        self.to_search = "ChromeDriver"

    def test_spustit(self):
        self.driver.get("http://www.google.com/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[text()='Přijmout vše']").click()
        # print(f"URL {self.driver.current_url}, page title {self.driver.title}")
        time.sleep(2)
        self.assertEqual("Google", self.driver.title)
        elem = self.driver.find_element(By.NAME, "q") # now the ID is different
        elem.send_keys(self.to_search)
        elem.submit()
        time.sleep(3)
        self.assertTrue(self.driver.title.startswith(self.to_search))
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
