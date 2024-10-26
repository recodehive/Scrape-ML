import streamlit as st
import requests
import time
from datetime import datetime
import json

# Initialize session state for favorites
if "favorites" not in st.session_state:
    st.session_state.favorites = set()

# TMDB API Configuration
API_KEY = "Imdb_api_key"
BASE_URL = "https://api.themoviedb.org/3"


def fetch_movies(list_type="trending"):
    """Fetch movies from TMDB API"""
    if list_type == "trending":
        url = f"{BASE_URL}/trending/movie/week?api_key={API_KEY}"
    else:
        url = f"{BASE_URL}/movie/popular?api_key={API_KEY}"

    try:
        response = requests.get(url)
        return response.json()["results"] if response.status_code == 200 else []
    except:
        st.error("Failed to fetch movies")
        return []


# Page Configuration
st.set_page_config(page_title="Movie Collection", page_icon="🎬", layout="wide")

# Custom CSS for the new compact design
st.markdown(
    """
    <style>
        /* General Styles */
        [data-testid="stAppViewContainer"] {
            background: #1a1d29;
            color: #ffffff;
        }
        
        .movie-list-container {
            padding: 10px;
            background: #1a1d29;
        }
        
        /* Compact Movie Card */
        .movie-card {
            background: #242836;
            border-radius: 8px;
            height: 90px;
            margin: 8px 0;
            display: flex;
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
        }
        
        .movie-card:hover {
            transform: translateX(5px);
            box-shadow: -4px 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        /* Poster Style */
        .poster-container {
            width: 60px;
            height: 90px;
            flex-shrink: 0;
        }
        
        .movie-poster {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        /* Movie Info */
        .movie-info {
            padding: 8px 12px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .movie-title {
            font-size: 0.95rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .movie-meta {
            font-size: 0.8rem;
            color: #a0a0a0;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        /* Rating Badge */
        .rating {
            background: #ffd700;
            color: #000000;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 0.75rem;
        }
        
        /* Action Buttons */
        .action-buttons {
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            gap: 8px;
        }
        
        .btn {
            padding: 6px 12px;
            border-radius: 4px;
            border: none;
            cursor: pointer;
            font-size: 0.75rem;
            transition: all 0.2s;
            text-decoration: none;
        }
        
        .btn-favorite {
            background: none;
            border: none;
            padding: 4px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .btn-favorite:hover {
            transform: scale(1.2);
        }
        
        .btn-share {
            background: #4267B2;
            color: white;
        }
        
        .btn-share:hover {
            background: #365899;
        }
        
        /* Filter Section */
        .filter-section {
            background: #242836;
            padding: 16px;
            border-radius: 8px;
            margin: 16px 0;
        }
        
        /* Custom Checkbox Style */
        .stCheckbox {
            color: white !important;
        }
        
        /* Custom Select Box Style */
        .stSelectbox {
            background: #242836;
            color: white !important;
        }
        
        /* Header Styling */
        .main-header {
            text-align: center;
            color: #ffffff;
            padding: 20px 0;
            background: linear-gradient(90deg, #1a1d29 0%, #242836 100%);
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 40px;
            color: #a0a0a0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <div class="main-header">
        <h1>🎬 Movie Collection</h1>
        <p style="color: #a0a0a0;">Discover and collect your favorite movies</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Filter Section
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    show_favorites = st.checkbox("Show Favorites", key="show_favorites")
with col2:
    sort_by = st.selectbox(
        "Sort by", ["Rating", "Release Date", "Title"], key="sort_by"
    )
with col3:
    list_type = st.selectbox("List Type", ["Trending", "Popular"], key="list_type")

# Fetch and process movies
movies = fetch_movies(list_type.lower())

# Filter favorites if needed
if show_favorites:
    movies = [m for m in movies if m["id"] in st.session_state.favorites]

# Sort movies
if sort_by == "Rating":
    movies.sort(key=lambda x: x["vote_average"], reverse=True)
elif sort_by == "Release Date":
    movies.sort(key=lambda x: x["release_date"], reverse=True)
else:
    movies.sort(key=lambda x: x["title"])

# Display movies
if not movies:
    st.markdown(
        """
        <div class="empty-state">
            <h3>No movies found</h3>
            <p>Try adjusting your filters or check back later for new movies.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
else:
    for movie in movies:
        # Create columns for layout
        movie_id = movie["id"]
        is_favorite = movie_id in st.session_state.favorites

        # Movie card HTML
        st.markdown(
            f"""
            <div class="movie-card">
                <div class="poster-container">
                    <img class="movie-poster" 
                         src="https://image.tmdb.org/t/p/w92{movie['poster_path']}" 
                         alt="{movie['title']}"/>
                </div>
                <div class="movie-info">
                    <div>
                        <div class="movie-title">{movie['title']}</div>
                        <div class="movie-meta">
                            <span>{movie['release_date'][:4]}</span>
                            <span class="rating">★ {movie['vote_average']:.1f}</span>
                        </div>
                    </div>
                </div>
                <div class="action-buttons">
                    {'❤️' if is_favorite else '🤍'}
                    <button class="btn-share" onclick="shareMovie('{movie['title']}')">Share</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Toggle favorite button
        if st.button(
            f"{'Remove from' if is_favorite else 'Add to'} Favorites",
            key=f"toggle_{movie_id}",
        ):
            if is_favorite:
                st.session_state.favorites.remove(movie_id)
            else:
                st.session_state.favorites.add(movie_id)
            st.experimental_rerun()

# JavaScript for interactivity
st.markdown(
    """
<script>
    function handleFavorite(movieId) {
        // Find and click the hidden toggle button
        document.querySelector(`button[key="toggle_${movieId}"]`).click();
    }
    
    function shareMovie(title) {
        const url = encodeURIComponent(window.location.href);
        const text = encodeURIComponent(`Check out "${title}" on Movie Collection!`);
        
        // Twitter share
        const twitterUrl = `https://twitter.com/intent/tweet?text=${text}&url=${url}`;
        
        // LinkedIn share
        const linkedinUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${url}&title=${text}`;
        
        // Instagram doesn't support direct web-sharing, open Instagram website instead
        const instaUrl = "https://www.instagram.com/";
        
        const options = `
            <button onclick="window.open('${twitterUrl}', '_blank')">Twitter</button>
            <button onclick="window.open('${linkedinUrl}', '_blank')">LinkedIn</button>
            <button onclick="window.open('${instaUrl}', '_blank')">Instagram</button>
        `;
        
        const popup = document.createElement("div");
        popup.innerHTML = options;
        document.body.appendChild(popup);
    }
</script>
<script>
""",
    unsafe_allow_html=True,
)
