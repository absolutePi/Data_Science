import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data=pd.read_csv("stats_data.csv",header=0,sep=",")
##creating linear regression 
# x=full_health_data["Average_Pulse"]
x=full_health_data["Duration"]
y=full_health_data["Calorie_Burnage"]
slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope*x+intercept

mymodel=list(map(myfunc,x))

plt.scatter(x,y)
# plt.plot(x,slope*x+intercept)
plt.plot(x,mymodel)
plt.ylim(ymin=0,ymax=2000)
plt.xlim(xmin=0,xmax=200)
# plt.xlabel("Average_Pulse")
plt.xlabel("Duration")
plt.ylabel ("Calorie_Burnage")
plt.show()