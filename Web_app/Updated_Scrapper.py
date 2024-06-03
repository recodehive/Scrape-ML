import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import os

# Define constants for readability
MAX_PAGES = 300
LOAD_MORE_TIMEOUT = 10
SCRAPE_TIMEOUT = 10
WAIT_TIME = random.uniform(1, 3)

# Create a custom exception for scraping errors
class ScrapingError(Exception):
    pass

def load_more_results(driver):
    try:
        load_more_button = WebDriverWait(driver, LOAD_MORE_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ipc-see-more__button')] or contains(@class, 'next-page')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(WAIT_TIME)  
        return True
    except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
        print(f"Error loading more results: {e}")
        return False

def scrape_movie_data(driver):
    all_movies = []
    try:
        # Wait for the movie list to be present
        movie_list_container = WebDriverWait(driver, SCRAPE_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul"))
        )

        # Wait for the individual movie elements within the list to be present
        movie_elements = WebDriverWait(driver, SCRAPE_TIMEOUT).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[@class='ipc-metadata-list-summary-item']"))
        )

        for movie_element in movie_elements:
            try:
                org_title = movie_element.find_element(By.XPATH, ".//h3[@class='ipc-title__text']").text
                title = re.sub(r'\d+\.\s*', '', org_title)
            except:
                title = "NA"
            try:
                year = movie_element.find_element(By.XPATH, ".//span[@class='sc-b189961a-8 kLaxqf dli-title-metadata-item']").text
            except:
                year = "NA"
            try:
                rating = movie_element.find_element(By.XPATH, ".//span[@class='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating']").text.split()[0]
            except:
                rating = "NA"
            try:
                description = movie_element.find_element(By.XPATH, ".//div[@class='ipc-html-content-inner-div']").text
            except:
                description = "NA"

            all_movies.append({
                'title': title,
                'type': "Tv-Series",
                'year': year,
                'rating': rating,
                'description': description
            })
    except (NoSuchElementException, ElementNotInteractableException, TimeoutException, StaleElementReferenceException) as e:
        print(f"Error scraping movie data: {e}")
        raise ScrapingError("Error during scraping.")
    return all_movies

def main():
    # Replace with the actual path to your chromedriver executable
    driver_path =  "C:\chromedriver-win64\chromedriver-win64\chromedriver.exe" 
    user_data_dir = os.path.join(os.path.expanduser('~'), 'AppData/Local/Google/Chrome/User Data/Default')
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument(f'user-data-dir={user_data_dir}')
    service = Service(executable_path=driver_path) 
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.imdb.com/search/title/?title_type=tv_series,feature,tv_movie,tv_episode,tv_miniseries,tv_special&release_date=2000-01-01,2024-12-31')

    all_movies_data = []
    cnt = 0
    while cnt < MAX_PAGES:
        cnt += 1
        print(f"Scraping page {cnt}")
        try:
            movies_data = scrape_movie_data(driver)
            all_movies_data.extend(movies_data)
        except ScrapingError:
            print("Encountered a scraping error. Skipping page.")
            continue
        if not load_more_results(driver):
            break

    df = pd.DataFrame(all_movies_data)
    df.to_csv('imdb_movies.csv', index=False)
    driver.quit()
    print("Data scraped and saved to 'imdb_movies.csv'")

if __name__ == "__main__":
    main()