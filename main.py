# main.py

import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from scraper import scrape_imdb_top_movies  # Import the scraping function

# Scrape IMDb for summaries and titles of 250 top-rated movies
num_movies = 250
movie_titles, summaries = scrape_imdb_top_movies(num_movies)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(summaries)

# Dimensionality Reduction with PCA
pca = PCA(n_components=2)
tfidf_pca = pca.fit_transform(tfidf_matrix.toarray())

# Finding the Optimal Number of Clusters

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

# Silhouette Score
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
optimal_k = 5  # Example value; replace with the best k determined from the plots

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
