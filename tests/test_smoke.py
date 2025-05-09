# Generated by Selenium IDE
from selenium.webdriver.chrome.options import Options

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

class TestSmoke():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    # Add implicit wait
    self.driver.implicitly_wait(10)
    # Create wait object for explicit waits
    self.wait = WebDriverWait(self.driver, 10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_smoke(self):
    try:
      self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
      self.driver.set_window_size(1936, 1048)
      
      # Add explicit waits for elements
      self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()
      self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Join Us"))).click()
      self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Directory"))).click()
      self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "directory-grid"))).click()
      self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "directory-list"))).click()
      self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Join"))).click()
      
      # Form filling
      self.wait.until(expected_conditions.presence_of_element_located((By.NAME, "fname"))).send_keys("matt")
      self.wait.until(expected_conditions.presence_of_element_located((By.NAME, "lname"))).send_keys("felber")
      self.wait.until(expected_conditions.presence_of_element_located((By.NAME, "bizname"))).send_keys("ios")
      self.wait.until(expected_conditions.presence_of_element_located((By.NAME, "biztitle"))).send_keys("devo")
      self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "submit"))).click()
      
      # Admin section
      self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
      self.wait.until(expected_conditions.presence_of_element_located((By.ID, "username"))).send_keys("incorrect")
      self.wait.until(expected_conditions.presence_of_element_located((By.ID, "password"))).send_keys("incorrect")
      self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".mysubmit:nth-child(4)"))).click()
      
    except Exception as e:
      print(f"Test failed with error: {str(e)}")
      raise
