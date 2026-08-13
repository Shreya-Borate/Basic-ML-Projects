################################################################################################################
#
# PLAY PREDICTION BASED ON WEATHER CONDITIONS
#
################################################################################################################
border = "="*30
#----------------- Import libraries -----------------
import pandas as pd 



#----------------- Load DataSet ---------------------

df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Dataset loaded Successfully.")

# ----------------- EDA -----------------------------
print(border)
print("First 5 Records are : ")
print(df.head())
print(border)

print(border)
print("Last 5 Records are : ")
print(df.tail())
print(border)

print(border)
print("Total Rows are : ",df.shape[0])
print("Total Columns are : ",df.shape[1])
print(border)

print(df.isnull().sum())

# ------ Separate Independent and Dependent Variables -----
print("Independent variables are : ")

