from selenium import webdriver
from lib.utility_functions import *
from page_model.login_page import LoginPage
from config.test_config import *

def before_feature(context,feature):
    BROWSER = context.config.userdata.get('browser')
    if BROWSER == "Firefox":
        caps = webdriver.DesiredCapabilities().FIREFOX
        caps["marionette"] = True
        fp = set_browser_preference(webdriver,'Firefox')
        context.driver = webdriver
        context.driver = webdriver.Firefox(executable_path=r'./utilities/Drivers/geckodriver.exe',
                                                firefox_profile=fp)
        context.driver.maximize_window()
    feature.login_page = LoginPage(context.driver)
    feature.page = feature.login_page
    feature.page.go(URL)
