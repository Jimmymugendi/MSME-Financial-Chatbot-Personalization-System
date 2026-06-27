from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def run_pca(X_scaled):
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)
    return pca, X_pca

def plot_scree(pca):
    explained = pca.explained_variance_ratio_
    cumulative = np.cumsum(explained)
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(explained)+1), explained, 'bo-', label='Individual')
    plt.plot(range(1, len(cumulative)+1), cumulative, 'ro-', label='Cumulative')
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('Scree Plot')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return cumulative