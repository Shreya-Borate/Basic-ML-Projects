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


############################################################
# Function Name : EDA
# Description   : Exploring dataset to understand better
#                 about data
############################################################
#shape,col,datatype

def Eda(df):

    print(Border)
    print("---------------EDA on Dataset---------------")
    print(Border)
    print()
    print(subborder)
    print()


    #shape,col,datatype
    print(Border)
    print("1. Shape of Dataset : ",df.shape)
    print("2. columns of Dataset : ",list(df.columns))
    print("3. Datatype of Dataset :\n",df.dtypes)
    print()


    #discriptive Statistics
    print(Border)
    print("3. discriptive Statistics :\n",df.describe())
    print()

    #Add New column to Data set ADD as sum of all subject marks
    print(Border)
    print("4. Adding new column to dataset : Total")
    df['Total'] = df['Math'] + df['Science'] + df ['English']
    print("Column Added successfully")
    print(df['Total'])

    print(Border)
    print("5. List of students who score more than 85 marks : ")
    print(df[df['Science'] > 85])

    #Replace Name
    print(Border)
    print("6. Replace Name Pooja to Puja ")
    df['Name'] = df['Name'].replace('Pooja','Puja')
    print(df)
    print("Name Replaced Succesfully")

    #sort df['Total'] in desc
    print(Border)
    print("7. Sort Total marks columns in Descending")
    df = df.sort_values(by ='Total' , ascending = False)
    print(df)
    print("Sorted Succesfully")
    print()

    #Bar plot student names vs Total marks
    print(Border)
    plt.bar(df['Name'],df['Total'])
    plt.xlabel("Student Names")
    plt.ylabel("Total marks")
    plt.title("Bar Plot Student names Vs Marks")
    plt.show()
    print("9. Bar plotted sucessfully")
    print()

    #Line graph for marks for amit across all subjects
    print(Border)
    Amit = df[df['Name'] == 'Amit']
    subjects = ['Math',  'Science',  'English']

    Marks = [Amit['Math'].values[0],
             Amit['Science'].values[0],
             Amit['English'].values[0]]

    plt.plot(subjects,Marks,marker ="o")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit Subject Vs Marks")
    plt.show()
    print("10. Line Graph plotted sucessfully")
    print()

    #Create another dataset with missing values and fill them with column mean
    print(Border)
    print("11. Dataset with Missing Values")

    Data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }
    df2 = pd.DataFrame(Data2)

    print("DataSet: 2 Before filling missing values")
    print(df2)
    print()

    print("Missing values : ")
    print(df2.isnull().sum())

    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())
    print("Dataset after Filling Missing Values : ")
    print(df2)
    print()

    #Drop English column from Original dataset
    print(Border)
    print("Dropping English column from Dataset")

    df.drop('English', axis=1, inplace = True)
    print(df)
    print("Successfully completed !")







    
    








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

    Eda(df)


############################################################
# Starter
############################################################

if __name__ =="__main__":
    main()