import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def predictor(X,Y):

    X = np.array(X).reshape(-1, 1)
    Y = np.array(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    print("Actual Y are  : ", Y_test)
    print("Predicted Y are  : ",y_pred)

    plt.plot(X_test, Y_test, marker='o', label='Actual Y')
    plt.plot(X_test, y_pred, marker='o', label='Predicted Y')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Actual vs Predicted Values")
    plt.legend()
    plt.show()

    y_new_pred = model.predict([[6]])
    print(y_new_pred)

def main():
    x = [1,2,3,4,5]
    y = [2000,2500,3000,3500,4000]

    predictor(x,y)

if __name__ == "__main__":
    main()