import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='module')
def browser(request):

    options = Options()
    options.add_argument('-headless')
    browser_ = webdriver.Firefox(firefox_options=options)
    yield browser_
    browser_.quit()


@pytest.mark.django_db
def test_login(browser, live_server):
    browser.get(live_server.url)
    browser.find_element_by_id('sex').click()
    browser.find_element_by_id('animal_type').click()
    browser.find_element_by_id('size').click()
    browser.find_element_by_id('form').submit()
    # browser.find_element_by_id('sex').click()
    # browser.find_element_by_id('animal_type').click()
    # browser.find_element_by_id('size').click()
    # browser.find_element_by_id('form').submit()
    # browser.find_element_by_id('frequentQuestions').click()
    # browser.find_element_by_id('aboutUs').click()
    # browser.find_element_by_id('help').click()
    # browser.find_element_by_id('contact').click()
