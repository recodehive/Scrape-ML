import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# GitHub repository URL
REPO_URL = "https://api.github.com/repos/recodehive/Scrape-ML"


# Function to fetch repository statistics
def fetch_repo_statistics():
    closed_pr_count = fetch_closed_pr_count()
    return {
        "total_prs": closed_pr_count,
        "total_projects": fetch_total_projects(),
        "total_contributors": fetch_contributors_count(),
    }


# Existing fetch functions remain the same
def fetch_closed_pr_count():
    closed_prs_url = f"{REPO_URL}/pulls?state=closed"
    closed_pr_count = 0
    page = 1
    while True:
        response = requests.get(f"{closed_prs_url}&page={page}")
        if response.status_code != 200 or not response.json():
            break
        closed_pr_count += len(response.json())
        page += 1
    return closed_pr_count


def fetch_total_projects():
    return 0


def fetch_closed_prs():
    closed_prs_url = f"{REPO_URL}/pulls?state=closed"
    closed_prs = []
    page = 1
    while True:
        response = requests.get(f"{closed_prs_url}&page={page}")
        if response.status_code != 200 or not response.json():
            break
        pulls = response.json()
        for pr in pulls:
            if pr["merged_at"]:
                closed_prs.append(
                    {
                        "title": pr["title"],
                        "url": pr["html_url"],
                        "date": pr["merged_at"],
                        "user": pr["user"]["login"],
                        "avatar_url": pr["user"]["avatar_url"],
                    }
                )
        page += 1
    return closed_prs


def fetch_upcoming_issues():
    issues_url = f"{REPO_URL}/issues?state=open"
    upcoming_issues = []
    response = requests.get(issues_url)
    if response.status_code == 200:
        issues = response.json()
        for issue in issues:
            if issue.get("assignee"):
                upcoming_issues.append(
                    {
                        "title": issue["title"],
                        "url": issue["html_url"],
                        "date": issue["created_at"],
                        "assignee": issue["assignee"]["login"],
                        "avatar_url": issue["assignee"]["avatar_url"],
                    }
                )
    return upcoming_issues


def fetch_contributors_count():
    contributors_url = f"{REPO_URL}/contributors"
    response = requests.get(contributors_url)
    if response.status_code == 200:
        return len(response.json())
    return 0


# Custom CSS for modern design
st.set_page_config(
    page_title="Changelog - Scrape ML",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
<style>
    /* Modern card design */
    .css-1r6slb0 {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Timeline design */
    .timeline-item {
        position: relative;
        padding: 20px;
        margin: 20px 0;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        color: black;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 50%;
        width: 16px;
        height: 16px;
        background: #6c5ce7;
        border-radius: 50%;
        transform: translateY(-50%);
    }
    
    /* Stats cards */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5em;
        font-weight: bold;
        color: #6c5ce7;
    }
    
    .stat-label {
        color: #666;
        font-size: 1.1em;
    }
    
    /* Avatar style */
    .avatar-small {
        border-radius: 50%;
        width: 30px;
        height: 30px;
        margin-right: 10px;
        vertical-align: middle;
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #6c5ce7;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Title with gradient
st.markdown(
    """
    <h1 style='text-align: center; background: linear-gradient(45deg, #6c5ce7, #a8c0ff);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent;
               margin-bottom: 30px;'>
        Scrape ML Changelog 📝
    </h1>
""",
    unsafe_allow_html=True,
)

# Fetch data
repo_stats = fetch_repo_statistics()
closed_prs = fetch_closed_prs()
upcoming_issues = fetch_upcoming_issues()

# Stats dashboard
st.markdown("### Project Statistics")
cols = st.columns(4)

with cols[0]:
    st.markdown(
        """
        <div class='stat-card'>
            <div class='stat-number'>{}</div>
            <div class='stat-label'>PRs Merged</div>
        </div>
    """.format(
            repo_stats["total_prs"]
        ),
        unsafe_allow_html=True,
    )

with cols[1]:
    st.markdown(
        """
        <div class='stat-card'>
            <div class='stat-number'>{}</div>
            <div class='stat-label'>Contributors</div>
        </div>
    """.format(
            repo_stats["total_contributors"]
        ),
        unsafe_allow_html=True,
    )

# Timeline section
st.markdown("### Recent Activity Timeline")

for pr in closed_prs[:5]:  # Show only last 5 PRs
    date = datetime.strptime(pr["date"], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y")
    st.markdown(
        f"""
        <div class='timeline-item'>
            <img src='{pr['avatar_url']}' class='avatar-small'>
            <strong>{pr['user']}</strong> merged PR: 
            <a href='{pr['url']}' target='_blank'>{pr['title']}</a>
            <div style='color: #666; font-size: 0.9em; margin-top: 5px;'>{date}</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

# Upcoming Features
st.markdown("### 🚀 Upcoming Features")
cols = st.columns(3)

upcoming_features = [
    {
        "title": "Personalized Watchlist",
        "progress": 75,
        "desc": "Implementation of user preferences-based watchlist",
    },
    {
        "title": "External DB Integration",
        "progress": 45,
        "desc": "Integration with external movie databases",
    },
    {
        "title": "Advanced Filtering",
        "progress": 30,
        "desc": "Enhanced search and filter capabilities",
    },
]

for idx, feature in enumerate(upcoming_features):
    with cols[idx]:
        st.markdown(
            f"""
            <div style='background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h4>{feature['title']}</h4>
                <p style='color: black; font-size: 0.9em;'>{feature['desc']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.progress(feature["progress"] / 100)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        <h3 style='color: #6c5ce7;'>About Scrape ML</h3>
        <p>Scrape ML is a robust web scraping tool designed to simplify the extraction of data from various online sources. 
           With its user-friendly interface and powerful features, Scrape ML allows users to collect, organize, 
           and analyze data seamlessly. Ideal for developers, data scientists, and anyone interested in leveraging 
           web data for their projects.</p>
        <p style='color: #666; margin-top: 20px;'>Made with 💜 by the Scrape ML Team</p>
    </div>
""",
    unsafe_allow_html=True,
)
