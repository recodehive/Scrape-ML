import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


def scrape_imdb_top_movies(num_movies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request = requests.get('https://www.imdb.com/chart/top/?ref_=login', headers=headers)
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    movie_link = soup.find_all('a', {"class": "ipc-title-link-wrapper"})

    hrefs = []
    movie_titles = []
    for movie in movie_link:
        text = movie.text
        if text[0].isdigit():
            movie_titles.append(text)
            hrefs.append(movie.get("href"))

    summaries = []
    for index in range(num_movies):
        url = "https://www.imdb.com" + hrefs[index]
        print(f"Fetching summary for: {movie_titles[index]}")
        r = requests.get(url, headers=headers)
        url_soup = BeautifulSoup(r.content, 'html.parser')
        summary = url_soup.find('span', {'data-testid': 'plot-l'}).text if url_soup.find('span', {'data-testid': 'plot-l'}) else "No summary available"
        summaries.append(summary)

    return movie_titles[:num_movies], summaries


num_movies = 250
movie_titles, summaries = scrape_imdb_top_movies(num_movies)


vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(summaries)


pca = PCA(n_components=2)  
tfidf_pca = pca.fit_transform(tfidf_matrix.toarray())


# Elbow Method
sum_of_squared_distances = []
K = range(2, min(10, num_movies))  # Adjust the range to be less than or equal to the number of samples
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(tfidf_pca)
    sum_of_squared_distances.append(km.inertia_)

plt.figure(figsize=(10, 7))
plt.plot(K, sum_of_squared_distances, 'bx-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Sum of squared distances')
plt.title('Elbow Method for Optimal k')
plt.show()


silhouette_avg = []
for k in range(2, min(10, num_movies)):  # Adjust the range to be less than or equal to the number of samples
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(tfidf_pca)
    labels = kmeans.labels_
    silhouette_avg.append(silhouette_score(tfidf_pca, labels))

plt.figure(figsize=(10, 7))
plt.plot(range(2, min(10, num_movies)), silhouette_avg, 'bx-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Optimal k')
plt.show()

# Choose the optimal number of clusters
optimal_k = 5 
# K-means Clustering with Optimal k
kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(tfidf_pca)
labels = kmeans.labels_

# Visualization
plt.figure(figsize=(10, 7))
for i in range(optimal_k):
    points = tfidf_pca[labels == i]
    plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {i}')

plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('K-means Clustering of IMDb Movie Summaries (after PCA)')
plt.legend()
plt.show()
