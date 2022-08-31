import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.backends.backend_pdf as bbpdf


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
    plt.title("PRICE AND FLOOR AREA COMPARISON AND PREDICTION")
    plt.xlabel("FLOOR AREA")
    plt.ylabel("PRICE")

    return plt.figure()

def price_bedrooms(data_file):
    x = data_file["BEDROOMS"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.title("PRICE AND BEDROOMS COMPARISON AND PREDICTION")
    plt.xlabel("BEDROOMS")
    plt.ylabel("PRICE")

    return plt.figure()

def price_bathrooms(data_file):
    x = data_file["BATHROOMS"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.title("PRICE AND BATHROOM COMPARISON AND PREDICTION")
    plt.xlabel("BATHROOMS")
    plt.ylabel("PRICE")

    return plt.figure()

def price_build_year(data_file):
    x = data_file["BUILD_YEAR"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.title("PRICE AND BUILD YEAR COMPARISON AND PREDICTION")
    plt.xlabel("BUILD YEAR")
    plt.ylabel("PRICE")

    return plt.figure()

def price_school_rank(data_file):
    x = data_file["NEAREST_SCH_RANK"].values.reshape(-1,1)
    y = data_file["PRICE"].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)

    plt.scatter(x,y)
    plt.plot(x, y_pred, color='red')
    plt.title("PRICE AND NEAREST SCHOOL RANK COMPARISON AND PREDICTION")
    plt.xlabel("NEAREST SCHOOL RANK")
    plt.ylabel("PRICE")

    return plt.figure()


empty_plot = plt.figure()
plot_list = [empty_plot, price_floor_area(n_raw), price_bedrooms(n_raw), price_bathrooms(n_raw), price_build_year(n_raw), price_school_rank(n_raw)]
# NO IDEA WHY, but the savefig() method below will not put in the first figure regardless of what it is, so I added an empty_plot as first in the list
# ALSO, it keeps adding an extra page, which is irritating, but whatever

def write_to_pdf(list_1, file_name):
    with bbpdf.PdfPages(file_name) as pp:
        firstPage = plt.figure(figsize=(11.69,8.27))
        firstPage.clf()
        txt = "HOUSING PRICES COMPARISON AND PREDICTION GRAPHS"
        firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=24, ha="center")
        pp.savefig()
        
        for item in list_1:
            fig = item
            pp.savefig(fig)

       


if __name__ == "__main__":
    correlate = correlation(raw_dropped)
    write_to_pdf(plot_list, 'housing_prediction.pdf')

