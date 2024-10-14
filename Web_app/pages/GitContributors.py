import streamlit as st
import requests

st.title("🤝 GitHub Contributors")
st.markdown(
    "<div style='height: 5px; background: linear-gradient(to right, #FF5733, #FFC300, #DAF7A6, #33FF57, #3380FF);'></div>",
    unsafe_allow_html=True,
)

# Instructions
st.write(
    "Thanks to our amazing contributors who help build and improve this project! 🎉"
)

# Load contributors data
contributors_url = "https://api.github.com/repos/Recode-Hive/Scrape-ML/contributors"
contributors_data = requests.get(contributors_url).json()

# Custom CSS styling
st.markdown(
    """
    <style>
        .contributor-container {
            display: flex;
            align-items: center;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 8px;
            margin-bottom: 8px;
            font-size: 14px;
        }
        .contributor-img {
            border-radius: 50%;
            width: 30px;
            height: 30px;
            margin-right: 10px;
        }
        .contributor-name {
            font-weight: bold;
            color: #333;
            flex: 1;
        }
        .contribution-count {
            color: green;
            font-weight: bold;
        }
        .github-icon {
            display: block;
            margin: 20px auto;
            width: 40px;
        }
        .github-text {
            text-align: center;
            font-weight: bold;
            color: #555;
            margin-top: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display each contributor in a compact, styled row
for contributor in contributors_data:
    avatar_url = contributor["avatar_url"]
    username = contributor["login"]
    contributions = contributor["contributions"]
    profile_url = contributor["html_url"]

    # HTML structure for each contributor row
    st.markdown(
        f"""
        <div class="contributor-container">
            <img src="{avatar_url}" class="contributor-img" />
            <a href="{profile_url}" target="_blank" class="contributor-name">{username}</a>
            <span class="contribution-count">{contributions} contributions</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# GitHub repository text and icon in white
st.markdown("---")
st.markdown(
    "<div class='github-text'>Explore more on our GitHub repository:</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <center>
    <a href="https://github.com/Recode-Hive/Scrape-ML" target="_blank">
        <img src="https://img.icons8.com/ios-glyphs/30/ffffff/github.png" alt="GitHub" class="github-icon" />
    </a>
    </center>
    """,
    unsafe_allow_html=True,
)
