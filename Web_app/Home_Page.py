import streamlit as st
import streamlit.components.v1 as components


# Custom CSS for enhanced styling
st.markdown(
    """
<style>
iframe{
        position: fixed;
        bottom: 40px;
        right: 0;
        boder: 1px solid black;
        border-radius:1em;
        # height: 400px;
        # width:300px;
        margin: 10px;
        # z-index: 9999;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: #1E88E5;
        text-align: center;
        animation: fadeInDown 1.5s;
    }
    .sub-header {
        font-size: 1.2rem;
        margin-bottom: 1rem;
        color: #424242;
        text-align: center;
        animation: fadeInUp 1.5s;
    }
    .feature-badge {
        background-color: #E1F5FE;
        color: #0277BD;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-weight: 600;
        margin: 0.2rem;
        display: inline-block;
        animation: pulse 2s infinite;
    }
    .stat-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 0.8rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-3px);
    }
    .stat-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1E88E5;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #757575;
    }
    @keyframes fadeInDown {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.05);}
        100% {transform: scale(1);}
    }
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar (keeping existing content)
with st.sidebar:
    # Animated header
    st.markdown(
        """
        <style>
        .animated-header {
            animation: fadeIn 2s;
            font-size: 24px;
            color: black;
            text-align: center;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
        <h2 class="animated-header">🎬 Movie Insights</h2>
        """,
        unsafe_allow_html=True,
    )

    # Adding selectboxes for user customization
    genre_filter = st.selectbox(
        "🎭 **Select Movie Genre**",
        options=["Action", "Comedy", "Drama", "Horror", "Romantic", "Sci-Fi"],
    )

    rating_filter = st.selectbox(
        "⭐ **Filter Movies by Rating**",
        options=["All", "1-3 stars", "4-6 stars", "7-8 stars", "9-10 stars"],
    )

    sentiment_analysis = st.checkbox("🔍 Enable Sentiment Analysis", value=True)

    # Fun fact section
    st.markdown(
        """
        <style>
        .fun-fact {
            font-size: 14px;
            color: #3498db;
            font-style: italic;
            text-align: center;
        }
        </style>
        <p class="fun-fact">Did you know? The highest-grossing movie of all time is **Avatar** (2009)!</p>
        """,
        unsafe_allow_html=True,
    )

    # Random movie suggestion button
    if st.button("🎉 Get a Random Movie Recommendation!"):
        st.success(
            "How about watching **Inception**? A mind-bending thriller that will keep you on the edge of your seat!"
        )

    # Movie trivia quiz section
    st.markdown("### 🎲 Movie Trivia Challenge!")
    trivia_questions = [
        "What is the name of the wizarding school in Harry Potter?",
        "Which movie features a character named 'Forrest Gump'?",
        "In which film does the phrase 'Here's looking at you, kid' appear?",
    ]
    selected_question = st.selectbox("Select a trivia question:", trivia_questions)

    if st.button("📝 Submit Answer"):
        st.success(
            f"You selected: '{selected_question}'. Now, what's your answer? Type below!"
        )

    # Crazy challenge
    st.markdown(
        """
        <style>
        .crazy-fun {
            background-color: #f1c40f;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 18px;
            color: #2c3e50;
        }
        </style>
        <div class="crazy-fun">
            🚀 **Crazy Challenge!** 🚀<br>
            Try to guess the movie from this emoji: 🍕👨‍🍳👊
            If you think you know the answer, type it in the box below!
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input box for the movie guessing game
    guess_movie = st.text_input("🤔 Your Guess:")
    if guess_movie:
        st.write(f"You guessed: {guess_movie}. Let's see if you're right!")

    # Movie recommendation trends
    st.markdown("### 📊 Movie Recommendation Trends")
    st.write("**Popular Genres:**")
    st.progress(0.7)  # Simulating a genre popularity chart
    st.write("**Top Rated Movies:**")
    st.progress(0.85)  # Simulating a top-rated movies chart

    # Conclusion
    st.success("Select options to refine your movie recommendations and have fun!")

# Main content
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #2b0751, #52057b, #832ab9, #ff2a6d, #ff5e7a, #ff9e99);
        -webkit-background-clip: text;
        color: transparent;
        text-align: center;
        animation: fadeInDown 1.5s;
    }
    </style>
    <h1 class="main-header">Movie Maestro: Your Cinema Companion</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="sub-header">Discover, Analyze, and Fall in Love with Movies</p>',
    unsafe_allow_html=True,
)

# Feature badges
st.markdown(
    """
<div style="text-align: center;">
    <span class="feature-badge">🎭 Genre Analysis</span>
    <span class="feature-badge">🌟 Personalized Recommendations</span>
    <span class="feature-badge">📊 Sentiment Analysis</span>
    <span class="feature-badge">🔍 Advanced Search</span>
</div>
""",
    unsafe_allow_html=True,
)

# Quick stats
st.markdown("### 📈 Movie Insights at a Glance")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
    <div class="stat-card">
        <div class="stat-value">500K+</div>
        <div class="stat-label">Movies Analyzed</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="stat-card">
        <div class="stat-value">98%</div>
        <div class="stat-label">Recommendation Accuracy</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
    <div class="stat-card">
        <div class="stat-value">50+</div>
        <div class="stat-label">Genres Covered</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        """
    <div class="stat-card">
        <div class="stat-value">24/7</div>
        <div class="stat-label">Movie Magic</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Main content with a structured introduction
st.markdown(
    """
    ### Introduction
    The IMDb Movie Review Analysis and Recommendation System is a comprehensive 
    tool designed to analyze movie reviews and provide personalized movie recommendations. 
    It leverages natural language processing (NLP) techniques and machine learning 
    algorithms to deliver insightful analysis and effective recommendations based on user preferences.

    ### Features
    1. **Sentiment Analysis** : Analyzes the sentiment of movie reviews (positive, negative).
    2. **Personalized Recommendations** : Recommends movies based on content filtering.
    
    **👈 Select options from the sidebar to refine your experience** 
    """
)

# Interactive elements
st.markdown("### 🎬 Dive into the World of Cinema")

# Movie mood selector
movie_mood = st.select_slider(
    "What's your movie mood today?",
    options=["😴 Relaxed", "😊 Happy", "🤔 Thoughtful", "😢 Emotional", "😱 Thrilled"],
)
st.write(f"Based on your mood, we recommend: {movie_mood.split()[1]} movies!")

# Personalized recommendation
st.markdown("### 🎯 Get Your Personalized Movie Recommendation")
fav_genre = st.multiselect(
    "Select your favorite genres:",
    ["Action", "Comedy", "Drama", "Sci-Fi", "Romance", "Horror"],
)
watch_time = st.slider("How much time do you have? (in minutes)", 60, 240, 120)

if st.button("Generate Recommendation"):
    st.balloons()
    st.success(
        f"Based on your preferences, we recommend watching 'Inception'! It's a mind-bending {', '.join(fav_genre)} film that fits your {watch_time}-minute watch time."
    )

# Call-to-action
st.markdown("### 🚀 Ready to Explore?")
st.markdown(
    """
<div style="text-align: center;">
    <a href="#" style="background-color: #1E88E5; color: white; padding: 0.8rem 1.5rem; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; transition: all 0.3s;">
        Start Your Movie Journey
    </a>
</div>
""",
    unsafe_allow_html=True,
)

# Footer
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; color: #757575;">
    Made with ❤️ by Movie Maestro Team | © 2024 All Rights Reserved
</div>
""",
    unsafe_allow_html=True,
)

iframe_code = """
<script>
window.embeddedChatbotConfig = {
chatbotId: "AAa0qs7ETyQtByIHFYTMD",
domain: "www.chatbase.co"
}
</script>
<script
src="https://www.chatbase.co/embed.min.js"
chatbotId="AAa0qs7ETyQtByIHFYTMD"
domain="www.chatbase.co"
defer>
</script>
"""

components.html(iframe_code, height=450,width=300)