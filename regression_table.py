import pandas as pd
import statsmodels.formula.api as smf
full_health_data=pd.read_csv("stats_data.csv")

# model=smf.ols('Calorie_Burnage ~ Average_Pulse',data=full_health_data)
# results=model.fit()
# print(results.summary())
# def Predict_Calorie_Burnage(Average_Pulse):
#     return(0.3296*Average_Pulse+346.8662)
# print(Predict_Calorie_Burnage(120))
# print(Predict_Calorie_Burnage(130))
# print(Predict_Calorie_Burnage(150))
# print(Predict_Calorie_Burnage(180))
model=smf.ols('Calorie_Burnage ~ Average_Pulse + Duration',data=full_health_data)
results=model.fit()
# print(results.summary())
def Predict_Calorie_Burnage(Average_Pulse,Duration):
    return(3.1695*Average_Pulse+5.8434*Duration-334.5194)
print(Predict_Calorie_Burnage(110,60))
print(Predict_Calorie_Burnage(140,45))
print(Predict_Calorie_Burnage(175,20))


