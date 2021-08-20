#!/usr/bin/python3

from selenium import webdriver

# fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd

print("mark0")


# additional setup for fix fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
options = Options()

# path to firefox profile
options.profile = '/home/cn1d4r14n/.mozilla/firefox/ct8fbiwt.default'

options.headless = False

service = Service('/home/cn1d4r14n/Documents/geckodriver')


driver = webdriver.Firefox(options=options, service=service)


USERNAME = input("Enter username: ")
PASSWORD = input("Enter password: ")
print(USERNAME)
print(PASSWORD)

print("mark1")

# initial get request that takes us to the login page
driver.get('https://www.linkedin.com/uas/login')
time.sleep(1)
print(driver.title)

print("mark2")

# We'll now login using the provided credentials
email = driver.find_element_by_id("username")
print(email)
email.send_keys(USERNAME)
password = driver.find_element_by_id("password")
print(password)
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)

time.sleep(5)

search_box = driver.find_elements_by_class_name("search-global-typeahead__input.always-show-placeholder")
# take the element out of the list
search_box = search_box[0]

print(search_box)

search_term = input("Input search term: ")


search_box.clear()

search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)


whatevs = input("Press enter to continue: ")

time.sleep(50)
print("mark3")



driver.quit()











