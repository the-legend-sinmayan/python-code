import pandas as pd
import numpy as np
import matplotlib.pyplot asplt
import seaborn as sns
import statistics as stats


from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')
data.head()
median_age = np.median(data['age'])
print("median value of age-",median_age)

median_fare = np.median(data['fare'])
print("median value of far-",median_fare)

mode_age = np.mode(data['age'])
print("mode value of age-",mode_age)

mode_class = stats.mode(data['pclass'])
print("mode value of pclass-",mode_class)

mode_gender = data['gender'].value_counts().index[0]
print("modeof feature gender", mode_gender)
