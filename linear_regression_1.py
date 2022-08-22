import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# from sklearn.linear_model import LinearRegression
from sklearn import datasets


FILE_PATH = 'all_perth_310121.csv'
raw = pd.read_csv(FILE_PATH)
n_raw = raw.dropna()  # data set which drops rows with n/a values

print(n_raw.corr())  # shows the correlation between all the data columns

# n_raw.plot(kind = 'scatter', x = 'FLOOR_AREA', y = 'PRICE')
# n_raw.plot(kind = 'scatter', x = 'BEDROOMS', y = 'PRICE')
n_raw.plot(kind = 'scatter', x = 'BATHROOMS', y = 'PRICE')

plt.show()
