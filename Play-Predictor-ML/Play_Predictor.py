############################################################
#
#   Play Predictor using KNN
#
#   Description:
#   Predict whether we can play or not based on
#   Weather and Temperature.
#
############################################################

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


############################################################
# Function Name : GetData
# Description   : Loads dataset from CSV file
############################################################

def GetData():

    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    return df


############################################################
# Function Name : PrepareData
# Description   : Converts categorical data into numerical
#                 data using LabelEncoder
############################################################

def PrepareData(df):

    le_weather = LabelEncoder()
    le_temperature = LabelEncoder()
    le_play = LabelEncoder()

    df["Weather"] = le_weather.fit_transform(df["Weather"])

    df["Temperature"] = le_temperature.fit_transform(df["Temperature"])

    df["Play"] = le_play.fit_transform(df["Play"])

    return df, le_weather, le_temperature, le_play


############################################################
# Function Name : TrainData
# Description   : Trains KNN using complete dataset
############################################################

def TrainData(df):

    X = df[["Weather", "Temperature"]]

    Y = df["Play"]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    return model


############################################################
# Function Name : TestData
# Description   : Predicts Play using Weather and Temperature
############################################################

def TestData(model, le_weather, le_temperature, le_play):

    weather = input(
        "Enter Weather (Sunny/Overcast/Rainy): "
    )

    temperature = input(
        "Enter Temperature (Hot/Mild/Cool): "
    )

    weather_encoded = le_weather.transform([weather])[0]

    temperature_encoded = le_temperature.transform([temperature])[0]

    prediction = model.predict(
        [[weather_encoded, temperature_encoded]]
    )

    result = le_play.inverse_transform(prediction)

    print("\nPrediction:", result[0])


############################################################
# Function Name : CheckAccuracy
# Description   : Calculates accuracy by splitting dataset
#                 into 50% training and 50% testing data
############################################################

def CheckAccuracy(df):

    X = df[["Weather", "Temperature"]]

    Y = df["Play"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("\nAccuracy:", accuracy * 100, "%")


############################################################
# Main Program
############################################################

def main():

    # Step 1
    df = GetData()

    print("Original Dataset:")
    print(df)

    # Step 2
    df, le_weather, le_temperature, le_play = PrepareData(df)

    print("\nEncoded Dataset:")
    print(df)

    # Step 3
    model = TrainData(df)

    print("\nModel training completed.")

    # Step 4
    TestData(
        model,
        le_weather,
        le_temperature,
        le_play
    )

    # Step 5
    CheckAccuracy(df)


############################################################
# Starter
############################################################

if __name__ == "__main__":
    main()