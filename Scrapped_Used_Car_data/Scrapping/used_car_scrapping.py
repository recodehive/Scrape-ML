# Install selenium using pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Import Keys because Keys are used to send special keys like ENTER, F1, ALT etc.
from selenium.webdriver.common.keys import Keys
import time

# If your chrome close instantly then use below code --------------------->

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# ------------------------------------------------------------------------->

# Create a driver object
driver = webdriver.Chrome(options=options, service=Service("C:/Users/dhanr/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"))

# Open the website
driver.get('https://www.cardekho.com/used-cars+in+mumbai')
time.sleep(6)

# Scroll the page
old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:


    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(6)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

# Get the html of the page
html = driver.page_source

# Save the html in a file
with open('used_car.html','w',encoding='utf-8') as f:
    f.write(html)
