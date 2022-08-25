import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
# from sklearn.linear_model import LinearRegression
from sklearn import datasets


FILE_PATH = 'all_perth_310121.csv'
raw = pd.read_csv(FILE_PATH)
n_raw = raw.dropna()  # data set which drops rows with n/a values
raw_dropped = n_raw.drop(['CBD_DIST', 'NEAREST_STN', 'NEAREST_STN_DIST', 'LATITUDE', 'LONGITUDE', 'POSTCODE', 'NEAREST_SCH', 'NEAREST_SCH_DIST'], axis=1)


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
    # data_file(kind = 'scatter', x = 'BATHROOMS', y = 'PRICE')
    fig = data_file.plot(kind = 'scatter', x = 'BATHROOMS', y = 'PRICE')
    return fig
    # return plt.show()

def price_build_year(data_file):
    # data_file(kind = 'scatter', x = 'BUILD_YEAR', y = 'PRICE')
    fig = data_file.plot(kind = 'scatter', x = 'BUILD_YEAR', y = 'PRICE')
    return fig
    # return plt.show()

def price_build_year_1 (data_file):
    data_file.plot(kind = 'scatter', x = 'BUILD_YEAR', y = 'PRICE')
    # fig = data_file.plot(kind = 'scatter', x = 'BUILD_YEAR', y = 'PRICE')
    return plt.show()


def plot(data_frame_1, data_frame_2):
    figure, axes = plt.subplots(nrows = 2, ncols = 2)
    data_frame_1.plot(ax=axes[0,0])
    data_frame_2.plot(ax=axes[0,1])
    plt.show()


correlate = correlation(raw_dropped)
print(correlate)
# print(raw_dropped)

price_build_year_1(raw_dropped)

# plot(price_bathrooms(raw_dropped), price_build_year(raw_dropped))
