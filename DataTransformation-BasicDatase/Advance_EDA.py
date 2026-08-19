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
    print(Border)
    print("Normalizing data using Min-Max Scaling")

    scaler = MinMaxScaler()
    df[['Math']] = scaler.fit_transform(df[['Math']])
    print("Data normalized successfully")
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