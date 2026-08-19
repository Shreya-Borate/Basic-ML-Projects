import numpy as np
from sklearn.linear_model import LinearRegression


def predictor ():

    # Load The Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]


    print("Values of Indepenent variables X :",X)
    print("Values of Depenent variables   Y :",Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x +=X[i]
        sum_y +=Y[i]

    mean_x = sum_x /len(X)
    mean_y = sum_y /len(Y)

    print("Mean_x is :",mean_x)
    print("Mean_y is :",mean_y)

    n = len(X)

    numerator = 0
    denomerator = 0

    for i in range (n):
        numerator = numerator + ((X[i] -mean_x) * (Y[i] - mean_y))
        denomerator = denomerator + ((X[i] - mean_x) ** 2)

    m = numerator / denomerator

    print("Slop of Line ie m : ",m)

    ##############################################################################
    #
    # Calculating Intercept ie C
    # y = mx+c
    # c = y-mx
    # c = ymean - m*xmean
    #
    ###############################################################################
    
    c = mean_y - m * mean_x 
    print("Y Intercept is i.e c : ",c)

    print("Regression Equations is : ", m,"X + ",c)

    test_x = 6
    predicted_y = m * test_x + c
    print("Predicted value of Y for X =", test_x, "is:", predicted_y)

      # Predict all Y values
    print("Predicted Y values:")

    Predicted_Y = []

    for i in range(len(X)):
        y_pred = m * X[i] + c
        Predicted_Y.append(y_pred)
        print("X =", X[i], "Actual Y =", Y[i], "Predicted Y =", y_pred)

    # Calculate MSE
    print("\nCalculating Mean Squared Error")

    squared_error = 0

    for i in range(len(Y)):
        error = Y[i] - Predicted_Y[i]
        squared_error = squared_error + (error ** 2)

    MSE = squared_error / len(Y)

    print("Sum of Squared Errors :", squared_error)
    print("Mean Squared Error :", MSE)

    # Calculate R2 Score
    print("\nCalculating R2 Score")

    mean_y = sum(Y) / len(Y)

    SST = 0

    for i in range(len(Y)):
        SST = SST + ((Y[i] - mean_y) ** 2)

    R2 = 1 - (squared_error / SST)

    print("Mean of Y :", mean_y)
    print("Total Sum of Squares :", SST)
    print("R2 Score :", R2)


def main():
    predictor()




###########################################################################
#
#     Starter
#
###########################################################################

if __name__ == "__main__":
    main()