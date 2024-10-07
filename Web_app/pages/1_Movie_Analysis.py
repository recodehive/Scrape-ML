import streamlit as st
import pandas as pd
from utils import analyze_reviews, recommend_movies
from streamlit_lottie import st_lottie 
import json



st.sidebar.header("Upload your CSV!")
st.sidebar.write("Make sure your CSV file contains a 'review' or 'user_review' column.")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

with open('Web_app/pages/Movie_Animated.json', encoding='utf-8') as anim_source:
        animation_data = json.load(anim_source)
        st_lottie(animation_data, 1, True, True, "high", 150, -100)
# Adding custom CSS to centralize components and style the headline
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .centered .stFileUploader, .centered .stButton, .centered .stDataFrame, .centered .stTable {
        width: 80%;
    }
    .yellow-headline {
        color: yellow;
        text-align: center;
    }
    .line {
        margin: 20px 0;
    }
    
    /* Add hover effects */
    .stButton:hover {
        background-color: #FFD700;  /* Change background color on hover */
        color: #fff;  /* Change text color on hover */
        transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transition */
    }

    .stFileUploader:hover {
        border: 2px dashed #FFD700; /* Change border on hover */
    }

    /* Example for additional hover effects on specific elements */
    .hover-effect {
        transition: transform 0.3s ease;
    }

    .hover-effect:hover {
        transform: scale(1.05); /* Scale up on hover */
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown('<h1 class="yellow-headline">Movie Review Analysis</h1>', unsafe_allow_html=True)

# Adding slider to control the length of the line
line_length = st.write("__________________________________________________________________")



uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
#option selection for the type of file encoding
option = st.selectbox('Select file encoding: ' , ['utf-8', 'latin1'], index=None)

if st.button('Enter'):
    if option is not None:
        def load_data(file):
            try:
                return pd.read_csv(file, encoding=option)
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
    
                # Check for 'review' or 'user_review' columns
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
            st.write("Make sure your CSV file contains a 'review' or 'user_review' column.")
    else:
        st.write('No file encoding option selected.')
        
st.markdown('</div>', unsafe_allow_html=True)

