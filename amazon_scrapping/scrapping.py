# product name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import csv
import pandas as pd

## One way to load chrome webdirver
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

## another way to load chrome webdriver
path = '/Users/mohammedrizwan/Downloads/chromedriver'
driver = webdriver.Chrome(path)

def product_listing(txt):

    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(2)
    search = driver.find_element_by_id('twotabsearchtextbox').send_keys(txt)
    driver.implicitly_wait(2)
    search_button = driver.find_element_by_id('nav-search-submit-button').click()
    driver.implicitly_wait(5)

    items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="a-link-normal a-text-normal"]')))

    for item in items:
        name_list.append(item.text)

    driver.implicitly_wait(5)
    c1 = driver.find_element_by_class_name("a-pagination")
    c2 = c1.text
    c3 = c2.splitlines()
    num_of_pg = c3[-2]

    for i in range(int(num_of_pg)-5):
        print(i)
        items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="a-link-normal a-text-normal"]')))
        for item in items:
            name_list.append(item.text)
        link = driver.find_element_by_class_name("a-section.a-spacing-none.a-padding-base")
        next_lin = link.find_element_by_class_name("a-last").find_element_by_tag_name("a").get_attribute("href")
        driver.get(next_lin)
        driver.implicitly_wait(2)


names = ['Laptop', 'Phones', 'Printers', 'Desktops', 'Monitors', 'Mouse', 'Pendrive', 'Earphones', 'Smart TV', 'Power banks']
name_list = []
for i in names:
    product_listing(i)
df=pd.DataFrame(name_list)
df.to_csv('./prod_listings.csv')
print(df)
driver.quit()

