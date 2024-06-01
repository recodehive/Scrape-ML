from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

DRIVER_PATH = 'E:/chromedriver-win64/chromedriver'
# Initialize the Chrome driver


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)

# Navigate to the URL
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
    keys = movies[0].keys()
    with open(filename, 'a', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(movies)


all_movies=[] 
cnt=0
while(cnt<300):
    cnt+=1   
    print(cnt)
    if not load_more_results():
            break
    
movie_elements = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul")
print("movie_list")

html_content = movie_elements.get_attribute('outerHTML')
print("html movie_list")
soup = BeautifulSoup(html_content, 'html.parser')

lst= soup.find_all("li", class_="ipc-metadata-list-summary-item")
print("list")
for i in lst:
    org_title= i.find("h3",class_="ipc-title__text").text
    try:
        title=re.sub(r'\d+\.\s*', '', org_title)
    except:
        title="NA"
    try:
        year = i.find("span", class_="sc-b189961a-8 kLaxqf dli-title-metadata-item").text
        
    except:
        year="NA"
    try:
        rating = i.find("span", class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.split()[0]
    except:
        rating="NA"
    try:
        description = i.find("div", class_='ipc-html-content-inner-div').text
    except:
        description = "NA"
    all_movies.append({
        'title': title,
        'type':"Tv-Series",
        'year': year,
        'rating': rating,
        'description': description
    })
   
print("saving started")
if all_movies:
    save_to_csv(all_movies)   
print("completed")
driver.quit()