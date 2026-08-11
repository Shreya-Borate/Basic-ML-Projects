import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    border = "-"*50

    #Step 1 : Load the dataset from csv file
    print(border)
    print("Step 1 : Load the dataset from csv file")
    print(border)

    df = pd.read_csv(Datapath)

    print(border)
    print("Some entries from dataset : ")
    print(df.head())
    print(border)


    #Step 2 : Clean the Dataset
    print(border)
    print("Step 2 : Clean the Dataset")
    print(border)

    df.dropna(inplace=True)

    print("Shape of Dataset : ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])

    print(border)

    #Step 3 : Separate Independent and Dependent Variable
    print(border)
    print("Step 3 : Separate Independent and Dependent Variable")
    print(border)

    X = df.drop(columns =['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)

    print("Input Columns : ",X.columns.tolist())
    print("Output column : Class")
    
    print(border)

    #step 4 : Split the dataset for traning and testing
    print(border)
    print("Step 4 : Split the dataset for traning and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.5,random_state=42, stratify=Y)

    print(border)
    print("details of Traning and Testing Data ")

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    print(border)

    #step 5 : Feature Scaling
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_train_Scaled = scaler.fit_transform(X_train)
    X_test_Scaled = scaler.fit_transform(X_test)

    print("Feature Scaling Done")

    print(border)

    #step 6 : Build the Model
    print(border)
    print("Step 6 : Build the Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=9)
    print("Classification model is Created")

    #Step 7 : Train the Model
    print(border)
    print("Step 7 : Train the Model")
    print(border)

    model = model.fit(X_train_Scaled,Y_train)

    print("Model Traning Completed")

    print(border)

    #Step 8 : Test the Model
    print(border)
    print("Step 8 : Test the Model")
    print(border)

    Y_pred = model.predict(X_test_Scaled)

    Accuracy = accuracy_score(Y_test,Y_pred)

    print("Model Accuracy is : ",Accuracy*100)



def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()