import streamlit as st 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

st.text("math calculations with no functions defined")
"Adding 7923 & 2341 = ", 7923+2341 

'a =', 'kakashi'

#markdown with magic
'''
# magic markdown

working wit markdown without explictly caling its function
'''

st.text("dataframe with magic")

df = pd.DataFrame(np.random.randn(30,30), columns=
                  ('col %i' %i for i in range(30) ))
'dataframe', df

# Magic working on Charts


s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart