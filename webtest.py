import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\webdriver(chrome)\\chromedriver")
        

    def test_search(self):
        driver = self.driver
        driver.get("https://hpkala.com/")
        #self.assertTrue('تماس با ما' in self.driver.page_source)
        content = driver.page_source
        if content.find("تماس با ما"):
            print("this is ok")
        else:
            print("oh! shit")
        
        time.sleep(10)

    def tear(self):
        
        self.driver.close()
        

if __name__ == "__main__":
    
    unittest.main()