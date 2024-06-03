import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

def load_more_results(driver):
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ipc-see-more__button')] or contains(@class, 'next-page')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(random.uniform(1, 3))  
        return True
    except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
        print(f"Error loading more results: {e}")
        return False

def scrape_movie_data(driver):
    all_movies = []
    movie_elements = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul")
    html_content = movie_elements.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    lst = soup.find_all("li", class_="ipc-metadata-list-summary-item")
    for i in lst:
        try:
            org_title = i.find("h3", class_="ipc-title__text").text
            title = re.sub(r'\d+\.\s*', '', org_title)
        except:
            title = "NA"
        try:
            year = i.find("span", class_="sc-b189961a-8 kLaxqf dli-title-metadata-item").text
        except:
            year = "NA"
        try:
            rating = i.find("span", class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.split()[0]
        except:
            rating = "NA"
        try:
            description = i.find("div", class_='ipc-html-content-inner-div').text
        except:
            description = "NA"

        all_movies.append({
            'title': title,
            'type': "Tv-Series",
            'year': year,
            'rating': rating,
            'description': description
        })
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
    while True:
        movies_data = scrape_movie_data(driver)
        all_movies_data.extend(movies_data)
        if not load_more_results(driver):
            break
    df = pd.DataFrame(all_movies_data)
    df.to_csv('imdb_movies.csv', index=False)
    driver.quit()
    print("Data scraped and saved to 'imdb_movies.csv'")
if __name__ == "__main__":
    main()