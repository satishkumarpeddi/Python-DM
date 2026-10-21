import matplotlib.pyplot as plt;
names = ['A','B','C','D','E','F']
marks = [98,85,83,78,88,81]

plt.subplot(2,2,1);
plt.hist(marks,bins=5,color="skyblue",edgecolor='black')
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")


plt.subplot(2,2,2)
plt.boxplot(marks)
plt.title("Box plot")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()