import pandas as pd
import numpy as np

full_health_data=pd.read_csv("stats_data.csv")
# print(full_health_data.describe())
Max_Pulse=full_health_data["Max_Pulse"]
percentile10=np.percentile(Max_Pulse,10)
# print(percentile10)
##finding standard deviation
std=np.std(full_health_data)
# print(std)
##finding coefficient of variation
cv=np.std(full_health_data)/np.mean(full_health_data)
# print(cv)
##finding variance
var=np.var(full_health_data)
# print(var)
import matplotlib.pyplot as plt

full_health_data.plot(x='Duration',y='Max_Pulse',kind='scatter')
plt.show()