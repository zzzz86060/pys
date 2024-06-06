import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import unittest

class TestLogin(unittest.TestCase):
    driver=None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('http://xczx2-portal.itheima.net/')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def test_login_and_logout(self,expect='13810000002'):
        driver=self.driver
        driver.find_element(By.PARTIAL_LINK_TEXT,'登录').click()
        time.sleep(5)
        username=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/div[1]/div/div/input')
        username.clear()
        username.send_keys('13810000002')

        password=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/div[2]/div/div/input')
        password.clear()
        password.send_keys('888itcast.CN764%...')

        driver.find_element(By.XPATH,'//button/span[text()="登录"]').click()
        time.sleep(10)

if __name__=='__main__':
    unittest.main()



