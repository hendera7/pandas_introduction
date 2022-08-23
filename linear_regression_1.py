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


def correlation(data_file):
    print(data_file.corr())  # shows the correlation between all the data columns
    return

def price_floor_area(data_file):
    data_file.plot(kind = 'scatter', x = 'FLOOR_AREA', y = 'PRICE')
    return plt.show()

def price_bedrooms(data_file):
    data_file(kind = 'scatter', x = 'BEDROOMS', y = 'PRICE')
    return plt.show()

def price_bathrooms(data_file):
    data_file(kind = 'scatter', x = 'BATHROOMS', y = 'PRICE')
    return plt.show()


test = price_floor_area(n_raw)
print(test)
