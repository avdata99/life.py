from matplotlib import pyplot as plt
import pandas as pd


def show_histogram_from_dataframe(dataframe):
    """ Show a histogram of the data """
    dataframe.value_counts().plot(kind='bar')
    plt.show()


def show_histogram_from_numpy_array(array):
    """ Show a histogram of the data """
    show_histogram_from_dataframe(pd.Series(array))
