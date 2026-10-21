import numpy as np
from scipy.spatial.distance import pdist,squareform

data = np.array([
    [2,4],
    [4,6],
    [6,8],
    [8,10]
])

distance = pdist(data,metric='euclidean')

matrix = squareform(distance)

print("Original distance")
print(data)

print("\nDismiliarity Matrix")
print(np.round(matrix,2))