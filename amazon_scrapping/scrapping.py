from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def product_listing(txt):
    name_list = []
    price_list = []
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
        prices = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
        
        for item, price in zip(items, prices):
            name_list.append(item.text)
            price_list.append(price.text if price else 'N/A')
        
        try:
            next_button = driver.find_element(By.CLASS_NAME, 's-pagination-next')
            if 's-pagination-disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    return name_list, price_list

# List of search terms
names = ['Laptop', 'Phones', 'Printers', 'Desktops', 'Monitors', 'Mouse', 'Pendrive', 'Earphones', 'Smart TV', 'Power banks']
all_product_listings = []
all_product_prices = []
category = []

# Scrape data for each search term
for name in names:
    products, prices = product_listing(name)
    all_product_listings.extend(products)
    all_product_prices.extend(prices)
    category.extend([name] * len(products))  # Extend category list with repeated entries for each product

# Convert the data to a DataFrame and save it as a CSV file
df = pd.DataFrame({'Category': category, 'Product Name': all_product_listings, 'Price': all_product_prices})
output_file = './prod_listings.csv'
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")

# Quit the WebDriver
driver.quit()
