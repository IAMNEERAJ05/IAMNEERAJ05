#importing libraries
import streamlit as st 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

#loading iris dataset
iris = load_iris()
x = iris.data 
y = iris.target 

#training ml model
clf = RandomForestClassifier()
clf.fit(x,y)

#create user input interface
def UI_features():
    sepal_len = st.sidebar.slider('Sepal length(cm)',
                float(x[:,0].max()),float(x[:,0].mean()) )
    sepal_width = st.sidebar.slider('Sepal width(cm)', float(x[:,1].min()),
                float(x[:,1].max()), float(x[:,1].mean()))
    petal_len = st.sidebar.slider('Petal Length(cm)', float(x[:,2].min()),
                float(x[:,2].max()),float(x[:,2].mean()))
    petal_width = st.sidebar.slider('Petal width(cm)',float(x[:,3].min()), float(x[:,3].max())
                , float(x[:,3].mean()))
    data = {
        'sepal_length' : sepal_len,
        'sepal_width' : sepal_width,
        'petal_length': petal_len,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features
df = UI_features()

#display user input
st.subheader('User Input Features: ')
st.write(df)

#making predictions
pred = clf.predict(df)
pred_prob = clf.predict_proba(df)

#display predictions and its probabilities
st.subheader('Prediction: ')
st.write(iris.target_names[pred][0])

st.subheader('Prediction Probability: ')
st.write(pd.DataFrame(pred_prob, columns= iris.target_names))