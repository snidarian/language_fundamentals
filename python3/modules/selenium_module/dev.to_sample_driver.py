#!/usr/bin/python3

from selenium import webdriver

# fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from colorama import Fore


red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

# additional setup for fix fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
options = Options()

# path to firefox profile
options.profile = '/home/cn1d4r14n/.mozilla/firefox/ct8fbiwt.default'

options.headless = False

service = Service('/home/cn1d4r14n/Documents/geckodriver')


driver = webdriver.Firefox(options=options, service=service)


driver.get('https://dev.to')
print(f"Connected to {red}{driver.current_url}{reset}")
time.sleep(5)
print(driver.title)


driver.quit()





