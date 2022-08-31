import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import datasets


FILE_PATH = 'all_perth_310121.csv'
raw = pd.read_csv(FILE_PATH)
n_raw = raw.dropna()  # data set which drops rows with n/a values
raw_dropped = n_raw.drop(['CBD_DIST', 'NEAREST_STN', 'NEAREST_STN_DIST', 'LATITUDE', 'LONGITUDE', 'POSTCODE', 'NEAREST_SCH', 'NEAREST_SCH_DIST'], axis=1)


def correlation(data_file):
    print(data_file.corr())  # shows the correlation between all the data columns
    return

def price_floor_area(data_file):
    x = data_file["FLOOR_AREA"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.show()

    return 

def price_bedrooms(data_file):
    x = data_file["BEDROOMS"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.show()

    return 

def price_bathrooms(data_file):
    x = data_file["BATHROOMS"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.show()

    return 

def price_build_year(data_file):
    x = data_file["BUILD_YEAR"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.show()

    return 



correlate = correlation(raw_dropped)
# print(correlate)
# print(raw_dropped)
# price_build_year_1(raw_dropped)
# plot(price_bathrooms(raw_dropped), price_build_year(raw_dropped))

print(price_bedrooms(n_raw))
print(price_floor_area(n_raw))

