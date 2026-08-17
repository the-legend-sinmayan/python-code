import pandas as pd
import numpy as np
import matplotlib.pyplot asplt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

data.dtypes

data.isnull().sum()