import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


URL="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
COLUMN_NAMES=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']


def write_title():
    st.title("Iris Data")
    st.write("""This is one of the earliest datasets used in the literature on classification methods and widely used in statistics and
             machine learning. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.
             One class is linearly separable from the other 2; the latter are not linearly separable from each other: 
             https://archive.ics.uci.edu/dataset/53/iris""")
def get_data():
    return pd.read_csv(URL, header=None,names=COLUMN_NAMES)
def display_data(data_df):
    st.write("And here are the first 5 data rows:")
    st.write(data_df.head())
    st.write("And here are some basic statistics:")
    st.write(get_data().describe())
    st.write('Data distributions')
    for col in COLUMN_NAMES:
        fig, ax = plt.subplots()
        ax.set_title(col)
        plt.hist(data_df[col])
        st.pyplot(fig)
def main():
    write_title()
    display_data(get_data())

if __name__=="__main__":
    main()

