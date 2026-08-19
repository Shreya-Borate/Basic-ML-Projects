import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def marvellousRegression(DataPath):
    border = "-"*40

    #step 1. Load the data
    print(border)
    print("step 1. Load the data")
    print(border)

    df = pd.read_csv(DataPath)
    print(df.head())

    #step 2. Remove unwanted columns
    print(border)
    print("step 2. Remove unwanted columns")
    print(border)

    if "Unnamed: 0" in df.columns :
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #step 3. Check Missing Values
    print(border)
    print("step 3. Check Missing Values")
    print(border)
    
    print("Total Missing values : ")
    print(border)
    print(df.isnull().sum())
    print(border)

    #step 4. Statistical summmary
    print(border)
    print("step 4. Statistical summmary")
    print(border)

    print(df.describe())

    # step 5. Correlation
    print(border)
    print("step 5. Correlation")
    print(border)

    print(df.corr())

    # step 6. Separate independent and dependent variables
    print(border)
    print("step 6. Split independent and dependent variables")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent Variables : ")
    print(X.head())

    print("Dependent Variables : ")
    print(Y.head())

    # step 7. Split the dataset
    print(border)
    print("step 7. Split the dataset")
    print(border)

    X_train, X_test, Y_train, Y_test =train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        )

    print("Traning data : ",X_train.shape)
    print("Testing data : ",X_test.shape)

    # step 8. Create and Train the Model
    print(border)
    print("step 8. Create and Train the Model")
    print(border)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)
    print("Model trained successfully...")

    # step 9. Test the Model
    print(border)
    print("step 9. Test the Model")
    print(border)

    y_pred = model.predict(X_test)

    
    print("Expected Anwers :")
    print(Y_test[:3])

    print("Predicted Anwers :")
    print(y_pred[:3])

    #step 10. Evaluate the model
    print(border)
    print("step 10. Evaluate the model")
    print(border)

    MSE = mean_squared_error(Y_test,y_pred)
    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test,y_pred)

    print("MSE  : ",MSE)
    print("RMSE : ",RMSE)
    print("R2   : ",R2)

    #step 11. Diplay Coefficent
    print(border)
    print("step 11. Diplay Coefficent")
    print(border)

    print("TV Coefficent        :",model.coef_[0])
    print("radio Coefficent     :",model.coef_[1])
    print("newspaper Coefficent :",model.coef_[2])

    print("Intercept : ",model.intercept_)


def main():
    marvellousRegression("Advertising.csv")


if __name__ == "__main__":
    main()