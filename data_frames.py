import streamlit as st 
import pandas as pd 
import numpy as np 
df = pd.DataFrame(
    np.random.randint(-255,255,(30,30)),
    columns = ('column %i' % i for i in range(30))
)
st.dataframe(df.style.highlight_min(axis=0))
st.text("epudu tabels chudam")
st.table(df)