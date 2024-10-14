import streamlit as st
import os
import pandas as pd

# Set the path for storing the reviews
reviews_file = "movie_reviews.csv"

# Initialize the reviews file if it doesn't exist
if not os.path.exists(reviews_file):
    df = pd.DataFrame(columns=["Name", "Movie", "Review"])
    df.to_csv(reviews_file, index=False)

# Read the existing reviews from the file
df = pd.read_csv(reviews_file)

# Initialize session state for showing the review form
if "show_review_form" not in st.session_state:
    st.session_state.show_review_form = False

st.title("🎬 Submit Your Movie Review")

st.markdown(
    "<div style='height: 5px; background: linear-gradient(to right, #FF5733, #FFC300, #DAF7A6, #33FF57, #3380FF);'></div>",
    unsafe_allow_html=True,
)

# Updated Custom CSS for Reddit-style reviews with dynamic sizing
st.markdown(
    """
    <style>
        .review-box {
            background-color: #f8f9fa;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 16px;
            border: 1px solid #e3e6e8;
            width: auto;
            max-width: 100%;
            height: auto;
            overflow-wrap: break-word;
            word-wrap: break-word;
            hyphens: auto;
        }
        .review-header {
            color: #1a1a1b;
            font-size: 12px;
            font-weight: 400;
            line-height: 16px;
            display: flex;
            align-items: center;
            margin-bottom: 8px;
            flex-wrap: wrap;
        }
        .review-author {
            color: #1c1c1c;
            font-weight: 700;  /* Changed to bold */
            margin-right: 4px;
            text-transform: capitalize;
        }
        .review-movie {
            color: red;
            text-transform: capitalize;
        }
        .review-content {
            font-size: 14px;
            line-height: 21px;
            font-weight: 400;
            color: #1a1a1b;
            white-space: pre-wrap;  /* Preserves line breaks and spaces */
        }
        .toggle-button {
            cursor: pointer;
            color: #0079D3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Toggle for review form visibility
show_review_form = st.checkbox(
    "➕ Submit Review", value=st.session_state.show_review_form, key="review_checkbox"
)

# Update session state based on checkbox
st.session_state.show_review_form = show_review_form

# Form for submitting reviews
if st.session_state.show_review_form:
    with st.form(key="review_form"):
        name = st.text_input("Your Name")
        movie_name = st.text_input("Movie Name")
        review = st.text_area("Your Review", height=80)
        submit_button = st.form_submit_button(label="Submit Review")

    if submit_button:
        if name and movie_name and review:
            new_review = pd.DataFrame(
                {
                    "Name": [name],
                    "Movie": [movie_name],
                    "Review": [review],
                }
            )
            df = pd.concat([df, new_review], ignore_index=True)
            df.to_csv(reviews_file, index=False)
            st.success("Thank you for your review!")
            st.session_state.show_review_form = False
            st.rerun()
        else:
            st.error("Please fill in all fields before submitting.")

# Display the reviews in a Reddit-style comment format
st.subheader("📜 Reviews")

if not df.empty:
    for index, row in df.iterrows():
        st.markdown(
            f"""
            <div class="review-box">
                <div class="review-header">
                    <span class="review-author">{row['Name']}</span>
                    <span class="review-movie">{row['Movie']}</span>
                </div>
                <div class="review-content">{row['Review']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.write("No reviews yet. Be the first to leave one!")
