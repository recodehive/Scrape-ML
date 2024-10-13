import streamlit as st

st.title("🎥 FAQ - Frequently Asked Questions?")
st.markdown(
    "<div style='height: 5px; background: linear-gradient(to right, #FF5733, #FFC300, #DAF7A6, #33FF57, #3380FF);'></div>",
    unsafe_allow_html=True,
)

# Custom CSS for styling
st.markdown(
    """
<style>
    body {
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .important {
        color: #FF5733;
        font-weight: bold;
    }
    .highlight {
        background-color: #FFFFA8;
        padding: 0.2em;
        border-radius: 5px;
    }
    .faq-title {
        color: #FFFFFF;
        font-size: 24px;
        margin-bottom: 10px;
    }
    .faq-subtitle {
        color: #333;
        font-size: 20px;
        margin-top: 20px;
        font-weight: bold;
    }
    .code-text {
        font-family: 'Courier New', monospace;
        background-color: #f0f0f0;
        padding: 2px 4px;
        border-radius: 3px;
    }
    .red-text {
        color: #FF0000;
    }
    .emoji-bullet {
        font-size: 18px;
        margin-right: 8px;
    }
    .underline-once {
        text-decoration: underline;
        text-decoration-color: #FFD700;
        text-decoration-thickness: 3px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# General Questions
st.subheader("🧐 General Questions")

# Question 1
st.markdown(
    '<div class="faq-title">1. 🤔 What is the IMDb Movie Review Analysis and Recommendation System?</div>',
    unsafe_allow_html=True,
)
st.write(
    "This system analyzes movie reviews and provides personalized movie recommendations using "
    "Natural Language Processing (NLP) and machine learning algorithms."
)

# Question 2
st.markdown(
    '<div class="faq-title">2. 😃😠 How does the sentiment analysis work?</div>',
    unsafe_allow_html=True,
)
st.write(
    "The sentiment analysis utilizes a Support Vector Machine (SVM) model to classify movie reviews as "
    "<span class='important'>positive</span> or <span class='important'>negative</span>. "
    "This helps in understanding audience sentiment towards different movies."
)

# Question 3
st.markdown(
    '<div class="faq-title">3. 📤 How can I upload my movie reviews?</div>',
    unsafe_allow_html=True,
)
st.write(
    "You can upload a CSV file containing movie reviews through the sidebar. "
    "<span class='red-text'>Ensure your file includes a 'review' or 'user_review' column for proper analysis.</span>"
)

# Question 4
st.markdown(
    '<div class="faq-title">4. 📁 What formats are supported for the uploaded CSV file?</div>',
    unsafe_allow_html=True,
)
st.write("The supported formats for the uploaded CSV file are:")
st.markdown(
    """
    <span class='emoji-bullet'>📌</span> UTF-8 encoding
    <span class='emoji-bullet'>📌</span> Latin1 encoding
""",
    unsafe_allow_html=True,
)
st.write("Make sure your file is in one of these formats to avoid encoding errors.")

# Question 5
st.markdown(
    '<div class="faq-title">5. 🔍 How are recommendations generated?</div>',
    unsafe_allow_html=True,
)
st.write(
    "Recommendations are generated using a combination of user ratings and review sentiment analysis, "
    "which helps identify similar movies based on user preferences."
)

# Question 6
st.markdown(
    '<div class="faq-title">6. 🔄 Can I get recommendations for TV shows as well?</div>',
    unsafe_allow_html=True,
)
st.write(
    "Yes! The system can also provide recommendations for TV shows based on your viewing history and preferences."
)

# Add a footer or additional info section
st.markdown("---")
st.markdown(
    "<small>For any further assistance, feel free to contact our support team at support@moviereviewsystem.com</small>",
    unsafe_allow_html=True,
)
