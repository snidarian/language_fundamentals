#!/usr/bin/python3


from selenium import webdriver
import time


# Creating new instance of browser
browser = webdriver.Firefox(executable_path='/usr/bin/firefox')



# perform a get request on the server
browser.get('https://www.linkedin.com/')


browser.execute_script(
    "(function(){try{for(i in document.getElementsByTagName('a')){let el = document.getElementsByTagName('a')[i]; "
    "if(el.innerHTML.includes('Contact info')){el.click();}}}catch(e){}})()")

# Wait 5 seconds for the page to load
time.sleep(5)

# Scrape the email address from the 'Contact info' popup
email = browser.execute_script(
    "return (function(){try{for (i in document.getElementsByClassName('pv-contact-info__contact-type')){ let el = "
    "document.getElementsByClassName('pv-contact-info__contact-type')[i]; if(el.className.includes('ci-email')){ "
    "return el.children[2].children[0].innerText; } }} catch(e){return '';}})()")





