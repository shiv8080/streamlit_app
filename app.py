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
st.line_chart(df)

