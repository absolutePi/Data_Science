import pandas as pd#for reading files

health_data=pd.read_csv("data.csv",header=0,sep=",")
# print(health_data)
# print(health_data.head())
##cleaning
health_data.dropna(axis=0,inplace=True)
# print(health_data)
##getting types
# print(health_data.info())
##converting data
health_data["Average_Pulse"]=health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"]=health_data["Max_Pulse"].astype(float)
# print(health_data.info())
##analyzing data
print(health_data.describe())
