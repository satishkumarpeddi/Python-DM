from scipy.stats import chisquare;

observed = [20,30,25,25]
expected = [25,25,25,25]

chi,p = chisquare(observed,expected);

print(f"The chi-square value: ", chi)

print(f"The P-value: ",p)

if p < 0.05 : 
    print("Significant difference exists")
else :
    print("No significant differece exists")