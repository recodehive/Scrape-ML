<h1 align="center">IMDb Movie Review Analysis and Recommendation System</h1>
<blockquote align="center">Analyzing movie reviews and providing recommendations using Python and Streamlit. 🎬💻</blockquote>
<p align="center">For new data generation and <b>sentiment analysis</b>, we have written a Python script to fetch📊 data from IMDb, analyze sentiments, and provide movie recommendations, all converted into an interactive web app using Streamlit. 🌐📈</p>


## Features

- **Scraping Movie Reviews**: Collects user reviews from IMDb using BeautifulSoup.
- **Customizable Scraper**: Target specific movies and the number of pages to scrape.
- **Sentiment Analysis**: Uses Support Vector Machine (SVM) to classify reviews as positive or negative.
- **Recommendations**: Recommends top movies based on positive reviews.
- **CSV Output**: Saves the scraped data into a CSV file for further analysis.

## Installation

1. **Install the dependencies:**
   ```bash
   pip install streamlit
   pip install beautifulsoup4
   pip install requests
   pip install pandas
   pip install scikit-learn

## Usage

1. **Run the scraping script** to collect movie reviews and save them into a CSV file. Open and execute the Jupyter notebook:

   ```bash
   jupyter notebook notebooks/movie_review_imdb_scrapping.ipynb

2. **Navigate to the Web_app directory:**
   ```bash
   cd Web_app

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

4. **Upload a CSV file** containing the reviews when prompted by the app.






 
