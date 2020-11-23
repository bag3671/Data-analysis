import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.get('http://200.1.220.254:3000/')
uid = driver.find_element_by_css_selector('#uid')
uid.send_keys('djy')
pwd = driver.find_element_by_css_selector('#pwd')
pwd.send_keys('1234')
# element.send_keys('1234')
pwd.submit()

