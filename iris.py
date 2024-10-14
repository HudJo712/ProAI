import pandas as pd
import matplotlib as mtl
import streamlit as st


df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None,names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
iris_frame=pd.DataFrame(df)
st.title("Iris Data")
st.write(iris_frame.head())
