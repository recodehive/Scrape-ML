from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

path = '/Users/hmharsh/Downloads/chromedriver'
driver = webdriver.Chrome(path)

def product_listing(txt):
    name_list = []
    driver.get("https://www.amazon.in/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.clear()
    search_box.send_keys(txt)
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()

    while True:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')))
        items = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
        for item in items:
            name_list.append(item.text)
        
        try:
            next_button = driver.find_element(By.CLASS_NAME, 's-pagination-next')
            if 's-pagination-disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
        except:
            break
    return name_list

names = ['Laptop', 'Phones', 'Printers', 'Desktops', 'Monitors', 'Mouse', 'Pendrive', 'Earphones', 'Smart TV', 'Power banks']
all_product_listings = []

for name in names:
    all_product_listings.extend(product_listing(name))

# Convert the list to a DataFrame and save it as a CSV file
df = pd.DataFrame(all_product_listings, columns=['Product Name'])
df.to_csv('./prod_listings.csv', index=False)
print(df)

driver.quit()
