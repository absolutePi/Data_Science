import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

health_data=pd.read_csv("sports_data.csv")
# health_data.plot(x='Average_Pulse',y='Calorie_Burnage',kind='line')
# plt.ylim(ymin=0)
# plt.xlim(xmin=0)
# plt.show()

##finding slope
def slope(x1,y1,x2,y2):
    s=(y2-y1)/(x2-x1)
    return s
# print(slope(80,240,90,260))
x=health_data["Average_Pulse"]
y=health_data["Calorie_Burnage"]
slope_intercept=np.polyfit(x,y,1)
# print(slope_intercept)
def my_func(x):
    return 2*x+80
# print(my_func(135))
health_data.plot(x='Average_Pulse',y='Calorie_Burnage',kind='line')
plt.ylim(ymin=0,ymax=400)
plt.xlim(xmin=0,xmax=150)
plt.show()