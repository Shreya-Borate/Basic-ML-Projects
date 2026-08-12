from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

print("Result Prediction case Study")

#Dataset

X = [[2,60],[5,80],[6,85],[1,50]]

Y = ["Fail","Pass","Pass","Fail"]

#create Model
K=3
model = KNeighborsClassifier(n_neighbors=K)

#Train Model
model.fit(X,Y)

#Accept input from user
hours = float(input("Enter study Hours : "))
attendence = float(input("Enter Attendence : "))

#Predict result
prediction = model.predict([[hours,attendence]])

#display result
print("Predicted Result : ",prediction[0])