# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSearch():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 30)
        self.vars = {}

    def teardown_method(self, method):
        # time.sleep(3)
        self.driver.quit()

    def test_testingstudio(self):
        self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#search-button').click()
        input_element=self.driver.find_element(By.CSS_SELECTOR, '#search-term')
        input_element.send_keys("selenium")
        input_element.send_keys(Keys.ENTER)
        actual=self.driver.find_element(By.CSS_SELECTOR, '.topic-title').text
        print(actual)
        assert "Selenium".lower() in actual