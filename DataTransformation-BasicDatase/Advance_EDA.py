############################################################
#
#   EDA (Exploratiory Data Analysis)
#
#   Description:
#   Performing EDA operations on 
#   Simple Data set
#
############################################################
Border = "="*50
subborder = "*"*50

#-----------Import Libraries------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler



############################################################
# Function Name : AEDA
# Description   : Adavance Exploring dataset to understand better
#                 about data
############################################################
def AEDA(df):
    # Normalize data using Min-Max Scaling

    #Add New column to Data set Gender
    print(Border)
    print("2. Adding new column to dataset : Gender")
    df['Gender'] = ['Male','Male','Female']
    print("Gender column added successfully")
    print(df)


    #group students by gender and calculate avg marks
    print(Border)
    print("4. Group students by gender and calculate avg marks")
    df['Total'] = df['Math'] + df['Science'] + df['English']
    print("Average marks by Gender : ")
    print(df.groupby('Gender')['Total'].mean())

    print(Border)
    print("1.Normalizing data using Min-Max Scaling")

    scaler = MinMaxScaler()
    df[['Math']] = scaler.fit_transform(df[['Math']])
    print("Data normalized successfully")
    print(df)

    #Perform One-Hot Encoding on Gender Column
    print(Border)
    print("3. Performing One-Hot Encoding on Column : Gender")
    df = pd.get_dummies(df, columns=['Gender'], dtype=int)
    print("One-Hot Encoding performed successfully")
    print(df)

############################################################
# Main Program
############################################################
def main ():
    Data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    AEDA(df)


############################################################
# Starter
############################################################

if __name__ =="__main__":
    main()