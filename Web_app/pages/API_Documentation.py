import streamlit as st

st.subheader(" API Documentation", divider="rainbow")
# Custom CSS for styling
st.markdown(
    """
<style>
    body {
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .faq-title {
        color: #FF5733;
        font-size: 24px;
        margin-top: 20px;
        font-weight: bold;
    }
    .code-snippet {
        font-family: 'Courier New', monospace;
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 5px;
        color: black;
    }
</style>
""",
    unsafe_allow_html=True,
)

# API Product Overview
st.subheader("🔍 API Product Overview")
st.write(
    "The IMDb API on AWS Data Exchange offers a GraphQL-based approach, enabling efficient data access for movie and TV series metadata, "
    "ratings, and box office data in real-time. It provides a streamlined JSON structure and single URL access for reduced API calls."
)

# Benefits
st.subheader("🌟 Key Benefits")
st.markdown(
    """
    - **One Call, All Data**: Access all data via a single URL.
    - **Flexible Queries**: Request only the specific fields you need, minimizing data over-fetching.
    - **Real-time Updates**: Receive IMDb’s latest data without delay.
    - **Multiple Entities**: Query multiple titles/names simultaneously.
    """,
    unsafe_allow_html=True,
)

# Getting Access to the API
st.subheader("🔑 Getting Access to the API")
st.write(
    "To access the IMDb API, you need an AWS account and AWS Access Keys. Follow these steps to set up your access."
)
st.markdown(
    """
    1. **Create an AWS Account**: The IMDb API is available through AWS Data Exchange.
    2. **Obtain AWS Access Keys**: Generate your keys for API authentication.
    3. **Enable Cost Explorer (Optional)**: View your usage and cost in AWS Cost Explorer.
    """,
    unsafe_allow_html=True,
)

# Authentication and API Key
st.subheader("🔒 Authentication and API Key")
st.write(
    "For API calls, the `x-api-key` header must include your API Key. Authenticate requests using AWS credentials in one of the following ways."
)

# Code Snippet for AWS CLI
st.markdown(
    """
    **Example API Call (AWS CLI)**:
    """,
    unsafe_allow_html=True,
)
st.code(
    """
aws dataexchange send-api-asset \\
--data-set-id <Dataset ID> \\
--revision-id <Revision ID> \\
--asset-id <Asset ID> \\
--request-headers "{ 'x-api-key': '<Your API Key>'}" \\
--region us-east-1 \\
--body "{ 'query': '{ title(id: \"tt0120338\") { ratingsSummary { aggregateRating voteCount } } }' }"
    """,
    language="bash",
)

# Sample GraphQL Query
st.subheader("💻 Sample Query")
st.write("Here’s a sample GraphQL query to retrieve the IMDb rating for *Titanic*:")

st.markdown(
    """
<div class="code-snippet">
{
  title(id: "tt0120338") {
    ratingsSummary {
      aggregateRating
      voteCount
    }
  }
}
</div>
""",
    unsafe_allow_html=True,
)

# Response Example
st.subheader("📊 Sample API Response")
st.write('{\n  "data": {\n    "title": {\n      "ratingsSummary": {')
st.write('        "aggregateRating": 7.9,\n        "voteCount": 1133828')
st.write("      }\n    }\n  }\n}")

# Additional Code Snippets
st.subheader("📜 Additional Code Snippets")

# Code Snippet for Postman Request
st.write("**Making Requests via Postman**")
st.markdown(
    """
1. **Set Method**: Use `POST` method.
2. **Request URL**: `https://api-fulfill.dataexchange.us-east-1.amazonaws.com/v1`
3. **Headers**:
    - `Content-Type`: `application/json`
    - `x-api-key`: `<Your API Key>`
4. **Body (GraphQL Query)**:
    ```graphql
    {
      title(id: "tt0120338") {
        ratingsSummary {
          aggregateRating
          voteCount
        }
      }
    }
    ```
    """,
    unsafe_allow_html=True,
)

# Code Snippet for Python API Call
st.write("**Python Code to Make an API Call**")
st.code(
    """
import requests

url = "https://api-fulfill.dataexchange.us-east-1.amazonaws.com/v1"
headers = {
    "x-api-key": "<Your API Key>",
    "Content-Type": "application/json"
}
query = '''
{
  title(id: "tt0120338") {
    ratingsSummary {
      aggregateRating
      voteCount
    }
  }
}
'''
response = requests.post(url, headers=headers, data=query)
print(response.json())
""",
    language="python",
)

# Example Use Cases
st.subheader("📄 Example Use Cases")
st.markdown(
    """
1. **Retrieve Ratings**: Query title ratings and vote counts.
2. **Box Office Data**: Access box office gross data.
3. **Cast and Crew**: Fetch top cast or crew details for movies and shows.
4. **Search Functionality**: Use keywords to find specific titles or names.
5. **Real-time Data Access**: Display data updates as they become available on IMDb.
""",
    unsafe_allow_html=True,
)

# Footer
st.markdown("---")
st.markdown(
    "<small>For further assistance, contact support at support@imdbapi.com</small>",
    unsafe_allow_html=True,
)
