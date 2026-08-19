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
import matplotlib.pyplot as plt

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


    # Add new column Status where total >250 ->Pass else ->Fail
    print(Border)
    print("6.Adding new column to dataset : Status")
    df['Status'] = np.where(df['Total'] > 250, 'Pass', 'Fail')
    print("Status column added successfully")
    print(df)

    #Print Number of Pass
    print(Border)
    print("7. Number of student pass : ",(df['Status'] == 'Pass').sum())



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

    #Pie Chart of Marks of Sagar Acc to Subjects
    print(Border)
    print("5. Pie Chart of Sagar's Marks")

    Sagar = df[df['Name'] == 'Sagar']
    subjects = ['Math','Science','English']

    Marks = [
        Sagar['Math'].values[0],
        Sagar['Science'].values[0],
        Sagar['English'].values[0]

    ]
    plt.pie(Marks, labels=subjects, autopct='%1.1f%%')
    plt.title("Sagar's Marks According to Subjects")
    plt.show()

    print("Pie Chart plotted successfully")

    #


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