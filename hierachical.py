import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# 1. Generate sample data
X, _ = make_blobs(n_samples=50, centers=3, cluster_std=0.60, random_state=42)

# 2. Compute the linkage matrix using Ward's method
linked = linkage(X, method='ward')

# 3. Plot and display the dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linked, orientation='top', distance_sort='ascending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Euclidean Distance')
plt.show()
