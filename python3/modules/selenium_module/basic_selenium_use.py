#!/usr/bin/python3


from selenium import webdriver
import time


# Creating new instance of browser
browser = webdriver.Firefox(executable_path='/usr/bin/firefox')


# perform a get request on the server
browser.get('https://www.linkedin.com/')



