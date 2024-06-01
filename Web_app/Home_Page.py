import streamlit as st

st.set_page_config(
    page_title="Home Page",
    page_icon="👋",
)

st.write("# Welcome to Movie Review Analysis and Recommendation System 👋")

st.sidebar.success("Select above part.")

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