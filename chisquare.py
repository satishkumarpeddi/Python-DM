import numpy as np
from scipy.stats import chisquare, chi2

observed = [23, 24, 25, 17, 89]
expected = [32, 32, 12, 34, 52]

# Normalize expected frequencies
expected = np.array(expected) * (sum(observed) / sum(expected))

# Calculate Chi-Square
chi, p = chisquare(observed, expected)

# Degrees of freedom
df = len(observed) - 1

# Calculate p-value separately
p_value = chi2.sf(chi, df)

print("Chi-Square:", chi)
print("Degrees of Freedom:", df)
print("P-value:", p_value)

if p_value < 0.05:
    print("Significant difference exists")
else:
    print("No significant difference exists")