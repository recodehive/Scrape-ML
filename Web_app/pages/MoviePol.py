import streamlit as st
import pandas as pd
import os

# Path to the poll movies file
movies_file = os.path.join(os.path.dirname(__file__), "..", "pollmovies.csv")

# Load movies from pollmovies.csv if it exists
if os.path.exists(movies_file):
    df_movies = pd.read_csv(movies_file)
else:
    st.error(
        "The file 'pollmovies.csv' does not exist. Please make sure it is available in the directory."
    )
    st.stop()

# Ensure column names are stripped of whitespace
df_movies.columns = df_movies.columns.str.strip()

# Convert Votes column to numeric, filling NaNs with 0 (in case of non-numeric data)
df_movies["Votes"] = (
    pd.to_numeric(df_movies["Votes"], errors="coerce").fillna(0).astype(int)
)

# Set up dashboard title and header styling
st.title("🎜 Movie Poll Dashboard")
st.markdown("<hr style='border-top: 3px solid #FFA07A;'>", unsafe_allow_html=True)

# Search bar to find movies
search_query = st.text_input("Search for a movie")
filtered_df = (
    df_movies[df_movies["Title"].str.contains(search_query, case=False, na=False)]
    if search_query
    else df_movies
)

# Pagination variables
polls_per_page = 5
page_number = st.number_input(
    "Page Number",
    min_value=1,
    max_value=(len(filtered_df) // polls_per_page) + 1,
    step=1,
)
start_index = (page_number - 1) * polls_per_page
end_index = start_index + polls_per_page

# Create a two-column layout for main dashboard content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📜 Available Movies for Polling")

    # Display each movie in a "card" style format with pagination
    for index, row in filtered_df.iloc[start_index:end_index].iterrows():
        with st.container():
            st.markdown(
                f"""
                <div style="background-color: black; color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #E8E8E8; font-size: 20px;"
                onmouseover="this.style.border='2px solid red';" onmouseout="this.style.border='1px solid #E8E8E8';">
                    <h4 style="margin: 0;">{row['Title']}</h4>
                    <p style="color: gray; margin: 0;">Genre: {row['Genre']} | Industry: {row['Industry']}</p>
                    <p style="margin: 0;">Votes: {row['Votes']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Vote for {row['Title']}", key=index):
                df_movies.at[index, "Votes"] += 1
                df_movies.to_csv(movies_file, index=False)
                st.success(f"Thanks for voting for {row['Title']}!")

with col2:
    # Add new movie form in the right column
    st.subheader("➕ Add a New Movie")
    with st.form("add_movie_form"):
        new_title = st.text_input("Movie Title")
        new_genre = st.selectbox(
            "Genre",
            [
                "Action",
                "Comedy",
                "Crime",
                "Drama",
                "Romance",
                "Sci-Fi",
                "Adventure",
                "Musical",
            ],
        )
        new_industry = st.selectbox("Industry", ["Hollywood", "Bollywood"])
        submit_movie = st.form_submit_button("Add Movie")

        if submit_movie:
            if new_title:
                new_movie = {
                    "Title": [new_title],
                    "Genre": [new_genre],
                    "Industry": [new_industry],
                    "Votes": [0],
                }
                new_movie_df = pd.DataFrame(new_movie)
                df_movies = pd.concat([df_movies, new_movie_df], ignore_index=True)
                df_movies.to_csv(movies_file, index=False)
                st.success(f"{new_title} has been added to the poll!")
            else:
                st.error("Please enter a movie title.")

# Add a button to view poll results
if st.button("View Poll Results"):
    # Add a section to display poll results with sorting
    st.markdown("<hr style='border-top: 3px solid #FFA07A;'>", unsafe_allow_html=True)
    st.subheader("📊 Poll Results")

    # Sort and display poll results in a more structured table format
    sorted_df = df_movies[["Title", "Genre", "Industry", "Votes"]].sort_values(
        by="Votes", ascending=False
    )
    st.dataframe(sorted_df)
