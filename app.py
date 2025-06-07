import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello streamlit")

df = pd.DataFrame({
    'colomn1': [1, 2, 3, 4, 5],
    'colomn2': [6, 7, 8, 9, 10],
    'Colomn3': [11, 12, 13, 14, 15]
    })

st.write("Herer is the dataframe")
st.write(df)

df = pd.DataFrame(
    np.random.randn(20, 5),columns=["a","b","c","d","e"]

)
st.write("Here is the dataframe line chart")
st.line_chart(df)

st.write("Using random forest ML alog for iris species classification")

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data= iris.data, columns= iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names

model = RandomForestClassifier()
df, target_names = load_data()
model.fit(df.iloc[:,:-1], df["species"])

sepal_length = st.sidebar.slider("Sepal length", float(df["sepal length (cm)"].min()), float(df["sepal length (cm)"].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df["sepal width (cm)"].min()), float(df["sepal width (cm)"].max()))
petal_length = st.sidebar.slider("Petal length", float(df["petal length (cm)"].min()), float(df["petal length (cm)"].max()))
petal_width = st.sidebar.slider("Petal width", float(df["petal width (cm)"].min()), float(df["petal width (cm)"].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
# prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")