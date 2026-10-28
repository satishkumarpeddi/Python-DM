import numpy as np
from scipy.stats import chisquare


observed = [23, 24, 25, 17, 89]
expected = [32, 32, 12, 34, 52]


expected  = np.array(expected)*(sum(observed)/sum(expected))

chi,p = chisquare(observed,expected)

print(f"Chi-square: ",chi)

if p < 0.05 :
    print(f"Significant exists")
else:
    print(f"No significant exists")