# IMDb Movie Review Analysis and Recommendation System :film_projector:
Analyzing movie reviews and providing recommendations using Python and Streamlit. 🎬💻. We have created two part in this WebApp :sunglasses:!!! :  
1. We have created a movie review analysis part.
2. We have created a movie recommendation part.

<p align="center">
For new data generation for <b>sentiment analysis</b> and <b>recommendation system</b>, we have written different Python script to fetch📊 data from IMDb, analyze sentiments, and provide movie recommendations, all converted into an interactive web app using Streamlit. 🌐📈</p>


## Features

- **Scraping Movie Reviews**: Collects user reviews from IMDb using BeautifulSoup.
- **Customizable Scraper**: Collects Movie Description from IMDb using Selenium.
- **Sentiment Analysis**: Uses Support Vector Machine (SVM) to classify reviews as positive or negative.
- **Recommendations**: Recommends top movies based on content of previous movie watched by user .
- **CSV Output**: Saves the scraped data into a CSV file for further analysis.

## Installation

1. **Install the dependencies:**
   ```bash
   pip install streamlit
   pip install beautifulsoup4
   pip install requests
   pip install pandas
   pip install scikit-learn
   pip install selenium
   ```
## Usage

### For Sentiment Analysis Part 

1. **Run the scraping script** to collect movie reviews and save them into a CSV file. Open and execute the Jupyter notebook:

   ```bash
   jupyter notebook notebooks/movie_review_imdb_scrapping.ipynb
   ```
2. **Navigate to the Web_app directory:**
   ```bash
   cd Web_app
   ```

### For Content-Based Movie Recommendation Part 

1. **Run the scraping script** to collect movie desciption and save them into a CSV file. Open and execute the Python Script.
   
   ***Note: you have to download web chromedriver and add it's path in Scrapper.py where it's mentioned driver path.***

   ```bash
   python -u "Scrapper.py"   
   ```
3. **Run the similarity_model generating script** to find out similarity we have made a model which we will use in our webapp. Open and execute the Jupyter notebook

     ***Note: you have to necessarily run this model.ipynb as this will download similarity.pkl which is the model we use in Streamlit Webapp***

   ```bash
   jupyter notebook notebooks/model.ipynb
   ```

### For HomePage
1. **Navigate to the Web_app directory:**
   ```bash
   cd Web_app
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run Home_Page.py
   ````
### Home Page

![Home_Page](https://github.com/Shraman-jain/Scrape-ML/assets/60072287/dbbafd78-e6c2-4469-b55f-d7e555f382ae "Home Page")

### Sentiment Analysis Part

![Movie_review](https://github.com/Shraman-jain/Scrape-ML/assets/60072287/dd449b6f-680c-4b00-bc45-6662bc82e48c "Sentiment Analysis")

### Content-Based Movie Recommendation Part


![Recommendation](https://github.com/Shraman-jain/Scrape-ML/assets/60072287/90599178-3d63-4a4a-8879-68408b2cc235 "Content-Based Movie Recommendation Part")



 
