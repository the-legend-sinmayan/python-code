import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('travel_planner.csv')

data.head(5)

data.info()

data.isnull().sum()

mean_temp = np.mean(data['temperature'])
print("mean value of temperature-", mean_temp)

var_temp = np.var(data['temperature(c)'])
print("variance value of temperature-", var_temp)

standard_dev_temp = np.std(data['temperature(c)'])
print("standard deviation value of temperature-", standard_dev_temp)

for i in range(1,13):
    month_data = data.loc[data['month'] == i]["temperature(c)"]
    print("for month"+str(i))
    print("mean temperature for month", i, "-", np.mean(month_data))
    
    print("standard deviation temperature for month", i, "-", str(np.std(month_data))+"\n")