import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Movie Review Analysis and Recommendation System",
    page_icon="👋",
)

# Welcome message
st.write("# Welcome to Movie Review Analysis and Recommendation System 👋")

# Sidebar with enhanced content
with st.sidebar:
    # Animated header
    st.markdown(
        """
        <style>
        .animated-header {
            animation: fadeIn 2s;
            font-size: 24px;
            color: #f39c12;
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
    
    **👈 Select the part from the sidebar** 
    """
)

# Adding some animation to the main content
st.markdown(
    """
    <style>
    .animated-text {
        animation: bounce 2s infinite;
        text-align: center;
        color: #e74c3c;
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-10px);
        }
        60% {
            transform: translateY(-5px);
        }
    }
    </style>
    <h3 class="animated-text">🌟 Discover Your Next Favorite Movie! 🌟</h3>
    """,
    unsafe_allow_html=True,
)
