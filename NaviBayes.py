from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score

X = [
    [22, 25000],
    [25, 30000],
    [28, 35000],
    [35, 60000],
    [40, 70000],
    [45, 80000],
    [23, 27000],
    [38, 65000]
]

y = [0,0,0,1,1,1,0,1]

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.25,random_state=42)

model = GaussianNB()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print("Actual values: ",y_test)
print("Predicted Values: ",y_pred)
print("Accuracy:",accuracy*100,"%")


new_data = [[30,40000]]
predication = model.predict(new_data)

print("New Prediction:","Yes" if predication[0] == 1 else "No")