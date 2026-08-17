import pandas as pd
import numpy as np
import matplotlib.pyplot asplt
import seaborn as sns

from google.colab import files
uploaded = pd.lead_csv('Titanic Dataset.csv')

data.head()

mean_age = np.mean(data['Age'])
print("mean age of passengers is -",mean_age)

mean_fare = np.mean(data['fare'])
print("mean fare is -",mean_fare)