import streamlit as st 
import pandas as pd 
import numpy as np 

st.title("Bar chart")

df = pd.DataFrame(
    np.random.randint(0,100,(10,3),),
    columns = ['c1','c2','c3']
)

"Data Frame", df
st.bar_chart(df)

st.title("Line chart")
st.line_chart(df)

st.title("Area")
st.area_chart(df)

st.title("Map")
locate_map = pd.DataFrame(
np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
columns = ['latitude', 'longitude'])
"map_locations",locate_map
st.map(locate_map)