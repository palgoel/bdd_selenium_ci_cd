from config.test_config import *
import time
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)
        time.sleep(10)

