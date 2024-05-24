import streamlit as st
import pandas as pd
from utils import analyze_reviews, recommend_movies

st.title("IMDb Movie Review Analysis and Recommendation System")

st.sidebar.header("Upload your CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

def load_data(file):
    try:
        return pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            return pd.read_csv(file, encoding='latin1')
        except UnicodeDecodeError:
            st.error("File encoding not supported. Please upload a CSV file with UTF-8 or Latin1 encoding.")
            return None

if uploaded_file is not None:
    reviews_df = load_data(uploaded_file)

    if reviews_df is not None:
        st.write("Data Preview:")
        st.write(reviews_df.head())

        st.write("Column Names:")
        st.write(reviews_df.columns.tolist())

        # Check for 'review' or 'user-review' columns
        review_column = None
        if 'review' in reviews_df.columns:
            review_column = 'review'
        elif 'user_review' in reviews_df.columns:
            review_column = 'user_review'

        if review_column:
            st.write("Sentiment Analysis:")
            sentiment_df, analyzed_df = analyze_reviews(reviews_df, review_column)
            st.write(sentiment_df)

            st.write("Analyzed DataFrame with Sentiments:")
            st.write(analyzed_df.head())

            st.write("Movie Recommendations:")
            recommendations = recommend_movies(analyzed_df)
            st.write(recommendations)
        else:
            st.error("The uploaded CSV file does not contain a 'review' or 'user_review' column.")
else:
    st.write("Please upload a CSV file to proceed.")
