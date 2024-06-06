import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import csv
import re
from bs4 import BeautifulSoup
import os

# Function to scrape IMDb data
def scrape_imdb_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')  # Run Chrome in headless mode

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    driver.get('https://www.imdb.com/search/title/?title_type=tv_series,feature,tv_movie,tv_episode,tv_miniseries,tv_special&release_date=2000-01-01,2024-12-31')
    driver.set_script_timeout(10000)

    def load_more_results():
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ipc-see-more__button")]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
            driver.execute_script("arguments[0].click();", load_more_button)
            time.sleep(2) 
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def save_to_csv(movies, filename='movies.csv'):
        file_exists = os.path.isfile(filename)
        keys = movies[0].keys()
        with open(filename, 'a', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            if not file_exists:
                dict_writer.writeheader()
            dict_writer.writerows(movies)

    all_movies = []
    cnt = 0
    while cnt < 300:
        cnt += 1
        if not load_more_results():
            break

        movie_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'lister-item mode-advanced')]")
        
        for element in movie_elements:
            soup = BeautifulSoup(element.get_attribute('outerHTML'), 'html.parser')

            try:
                org_title = soup.find("h3", class_="lister-item-header").find("a").text
                title = re.sub(r'\d+\.\s*', '', org_title)
            except:
                title = "NA"

            try:
                year = soup.find("span", class_="lister-item-year").text
            except:
                year = "NA"

            try:
                rating = soup.find("div", class_="ratings-bar").find("strong").text
            except:
                rating = "NA"

            try:
                description = soup.find_all("p", class_="text-muted")[1].text.strip()
            except:
                description = "NA"

            all_movies.append({
                'title': title,
                'type': "Tv-Series",
                'year': year,
                'rating': rating,
                'description': description
            })

        if all_movies:
            save_to_csv(all_movies)
            all_movies = []

    driver.quit()

# Streamlit App
def main():
    st.title("IMDb Scraper")

    if st.button("Scrape IMDb Data"):
        with st.spinner("Scraping IMDb data..."):
            scrape_imdb_data()
        st.success("Data scraped successfully!")

        # Show the CSV file content
        st.subheader("Scraped IMDb Data:")
        filename = 'movies.csv'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                csv_content = file.read()
            st.code(csv_content, language='csv')
        else:
            st.error("CSV file not found.")

if __name__ == "__main__":
    main()
