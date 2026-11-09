import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram , linkage
from sklearn.datasets import make_blobs 

X ,_ = make_blobs(n_samples=50, centers=3,cluster_std=0.60, random_state=42)

linked = linkage(X,method='ward')

plt.figure(figsize=(10,5))
dendrogram(linked,orientation='top',distance_sort='ascending',show_leaf_counts=True)

