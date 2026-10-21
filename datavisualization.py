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


plt.subplot(2,2,3)
plt.pie(marks,labels=names,autopct='%1.1f%%')
plt.title("Pie Chart")


plt.subplot(2,2,4)
plt.bar(names,marks,color='green')
plt.title("Bar chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()