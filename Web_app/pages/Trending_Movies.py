import streamlit as st
import requests
import time

# Your TMDB API key
API_KEY = "Imdb_api_key"


# Function to fetch trending movies from TMDB
def fetch_trending_movies():
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        st.error("Failed to fetch data from TMDB.")
        return []


# Function to display loading spinner
def show_loading():
    with st.spinner("Fetching trending movies..."):
        time.sleep(2)  # Simulate a delay
        return fetch_trending_movies()


# Configure the page
st.set_page_config(
    page_title="Trending Movies",
    page_icon="🎥",
)

# Custom CSS for enhanced styling
st.markdown(
    """
<style>
    body {
        background-color: #f4f4f4;
    }
    .movie-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 20px;
        padding: 20px;
        text-align: center;
        cursor: pointer;
    }
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
    }
    .movie-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin: 10px 0;
    }
    .movie-overview {
        color: #34495e;
        font-size: 0.9rem;
        height: 60px; /* Fixed height for uniformity */
        overflow: hidden; /* Hide overflow text */
    }
    .movie-release {
        color: #7f8c8d;
        font-size: 0.85rem;
        margin-top: 5px;
    }
    .movie-poster {
        border-radius: 10px;
        width: 100%;
        height: auto;
        max-height: 300px; /* Set max height for uniform poster sizes */
        object-fit: cover; /* Maintain aspect ratio */
    }
    .loading {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <h1 style="text-align: center; color: #2980b9;">Trending Movies</h1>
    <p style="text-align: center; color: #34495e;">Check out the latest trending movies of the week!</p>
    """,
    unsafe_allow_html=True,
)

# Fetch trending movies
trending_movies = show_loading()

# Display the movies
if trending_movies:
    # Create a container for movie cards
    cols = st.columns(3)  # Adjust the number of columns as needed
    for i, movie in enumerate(trending_movies):
        title = movie["title"]
        overview = movie["overview"]
        release_date = movie["release_date"]
        poster_path = movie["poster_path"]
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

        # Create a card for each movie
        with cols[i % 3]:  # Cycle through columns
            st.markdown(
                f"""
                <div class="movie-card" onclick="window.open('https://www.themoviedb.org/movie/{movie['id']}', '_blank');">
                    <img src="{poster_url}" alt="{title}" class="movie-poster"/>
                    <div class="movie-title">{title}</div>
                    <p class="movie-overview">{overview}</p>
                    <div class="movie-release">Release Date: {release_date}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
else:
    st.warning("No trending movies available.")
