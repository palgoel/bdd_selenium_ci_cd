from behave import *
from config.test_config import *
use_step_matcher("re")
from selenium.webdriver.common.keys import Keys

def login_input(driver):
    elem = driver.find_element_by_name("q")
    return elem

@step('user has launched the application')
def step_impl(context):
    pass

@step('user enters text in textbox')
def step_impl(context):
    login_input(context.driver).clear()
    # login_input(context.driver).send_keys(LOGIN)
    login_input(context.driver).send_keys("python")
    login_input(context.driver).send_keys(Keys.RETURN)

@step('check for present string')
def step_impl(context):
    assert "No results found." not in context.driver.page_source

@step('check for current url')
def step_impl(context):
    assert "org" in context.driver.current_url

@step('check for page title')
def step_impl(context):
    assert "org" in context.driver.title