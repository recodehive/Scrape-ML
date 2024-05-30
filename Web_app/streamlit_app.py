import streamlit as st
import pandas as pd
from utils import analyze_reviews, recommend_movies

# Page configuration
st.set_page_config(page_title="IMDb Movie Review Analysis and Recommendation System", page_icon="🎬", layout="wide")

with open("path/to/animated_logo.json", "r") as f:
    animated_logo_data = f.read()
    st.image(animated_logo_data, format="json")

    
# Title and description
st.markdown(

    """
    <style>
    .main-title {
        font-size: 3em;
        color: #FFA500;
        text-align: center;
    }
    .upload-section {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .section-title {
        font-size: 1.5em;
        color: #4169E1;
        margin-top: 20px;
    }
    .dataframe-preview {
        margin-top: 20px;
    }
    .error {
        color: red;
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">IMDb Movie Review Analysis and Recommendation System</h1>', unsafe_allow_html=True)

st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Upload your CSV</h2>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
st.markdown('</div>', unsafe_allow_html=True)

def load_data(file):
    try:
        return pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            return pd.read_csv(file, encoding='latin1')
        except UnicodeDecodeError:
            st.markdown('<p class="error">File encoding not supported. Please upload a CSV file with UTF-8 or Latin1 encoding.</p>', unsafe_allow_html=True)
            return None

if uploaded_file is not None:
    reviews_df = load_data(uploaded_file)

    if reviews_df is not None:
        st.markdown('<h2 class="section-title">Data Preview</h2>', unsafe_allow_html=True)
        st.dataframe(reviews_df.head(), width=1000)

        st.markdown('<h2 class="section-title">Column Names</h2>', unsafe_allow_html=True)
        st.write(reviews_df.columns.tolist())

        # Check for 'review' or 'user_review' columns
        review_column = None
        if 'review' in reviews_df.columns:
            review_column = 'review'
        elif 'user_review' in reviews_df.columns:
            review_column = 'user_review'

        if review_column:
            st.markdown('<h2 class="section-title">Sentiment Analysis</h2>', unsafe_allow_html=True)
            sentiment_df, analyzed_df = analyze_reviews(reviews_df, review_column)
            st.write(sentiment_df)

            st.markdown('<h2 class="section-title">Analyzed DataFrame with Sentiments</h2>', unsafe_allow_html=True)
            st.dataframe(analyzed_df.head(), width=1000)

            st.markdown('<h2 class="section-title">Movie Recommendations</h2>', unsafe_allow_html=True)
            recommendations = recommend_movies(analyzed_df)
            st.write(recommendations)
        else:
            st.markdown('<p class="error">The uploaded CSV file does not contain a \'review\' or \'user_review\' column.</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="error">Please upload a CSV file to proceed.</p>', unsafe_allow_html=True)
