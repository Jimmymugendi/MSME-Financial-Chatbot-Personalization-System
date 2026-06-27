from sklearn.cluster import KMeans

def run_kmeans(X_scaled, n_clusters=4):
    """Simple K-Means clustering"""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    return labels, kmeans